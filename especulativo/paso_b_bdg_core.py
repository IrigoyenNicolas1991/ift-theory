# ETAPA ESPECULATIVA TCI 2.0 - calculo preliminar, no validado
# ============================================================================
# PASO B — EL BdG DEL CORE (compuerta unica, bitacora §34.D; diseño en el
# acta PASO-A-bisagra-core-2026-07-21.md §7):
#
#   ¿El core REAL del HQV del D4-BN (mezcla FM+ciclica alineada, Paso A)
#   sostiene ramas fermionicas quirales NETAS a lo largo del tubo?
#
# CRITERIO DE MUERTE PRE-DECLARADO (§34.D): C_neto = 0 => 10a lapida el mismo
# dia — el sector de defectos pierde materia quiral y candidato a foton, la
# Arquitectura A muere, el programa queda en la ruta geometrica G(t) sin
# candidato de luz. (El otro gatillo, "pinning blando", ya quedo descartado
# por el Paso A: pinning duro, atractor unico alineado.)
#
# FISICA: BdG del 3P2 en la seccion 2D del tubo. Pairing p-wave triplete:
#   d_mu(r,k) = (Delta0/kF) [ 1/2{A_mux(r), kx} + 1/2{A_muy(r), ky}
#                             + A_muz(r) kz ]           (mu = indice de espin)
#   Delta_spin = (d . sigma) i sigma_y = [[-d1+i d2, d3],[d3, d1+i d2]]
#   H = [[xi x 1_spin, Delta],[Delta^dag, -xi x 1_spin]]   (Nambu x spin = 4)
#   xi = k^2 + kz^2 - mu   (m=1/2, hbar=1; laplaciano 5 puntos, kz continuo)
# El campo A(r) es el REAL del Paso A (paso_b_core.npz, regenerable con
# paso_b_core_input.py): HQV (+1/2,+1/4) con core FM+ciclica alineada C3||z.
# El gap NO es axisimetrico (el core rompe la axisimetria combinada — perla
# del acta §7): el BdG come el campo 2D completo, sin regla de seleccion.
#
# CONTEO: flujo espectral en kz — cruces de E=0 de ramas localizadas en el
# core (POR PESO, leccion §33.E), con signo = sign(dE/dkz) al cruzar:
#   C_neto = #(cruces hacia arriba) - #(cruces hacia abajo)
# dentro de la ventana entre los nodos polares del fondo D4 (kz = +-sqrt(mu)
# EXACTO en esta red: el D4 diag(1,-1,0) anula el gap en k || z; fuera de la
# ventana el gap de bulk cierra y el conteo no esta definido).
# Cruce REAL vs anticruce de hibridizacion core-borde (artefacto de caja):
# al refinar por biseccion se registra min|E| de la rama seguida; cruce real
# si min|E| < EPS_CRUCE; si se estanca por encima, se lista como anticruce y
# NO se cuenta (resolucion declarada en el acta).
#
# CONTROLES PRE-DECLARADOS (acta Paso A §7):
#   (1a) ciclica uniforme, k-space: FHS Chern por rebanada en la BZ de la red
#        (mismas funciones sin/cos que el real-space) => perfil (1,-2,1,0)-like
#        con nodos 1-3-3-1 en alturas y cargas alternadas |q|=1 (el §33);
#        el signo global del perfil es convencion (orientacion de la ciclica
#        GL respecto del cubo de Weyl abstracto del toy) — lo invariante es
#        |C| por ventana + alternancia + cierre en 0.
#   (1a-bis) D4 uniforme, k-space: C=0 en TODAS las ventanas (fondo mudo,
#        clase con TRS) + nodos SOLO polares en kz=+-sqrt(mu).
#   (1b) ciclica uniforme, real-space: estados sub-gap de BORDE presentes
#        (el Chern!=0 puebla el borde de la muestra) y CERO cruces de core.
#   (2)  D4 uniforme, real-space: cero cruces de core (los DIII de borde son
#        fisica del borde, se cuentan aparte por peso).
#   (3)  espejo (campo conjugado = HQV(-1/2,-1/4)) => C_neto invertido.
#   (4)  estabilidad del conteo bajo Delta0 (x0.7, x1.4) y mu (x0.8, x1.2)
#        (topologico mientras el gap de bulk no cierre; regimen declarado;
#        el prefactor Delta0/KF mantiene KF=0.8 fijo — es normalizacion).
#
# QA heredado: hermiticidad y PH exactas (autotest en grilla chica random);
# contar por PESO, no por centroide (§33.E).
# Uso:  python -u paso_b_bdg_core.py [todo|controles|real|espejo|estabilidad]
# ============================================================================
import numpy as np, time, os, sys, json
import scipy.sparse as sp
import scipy.sparse.linalg as spla

t_ini = time.time()
np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(11)
AQUI = os.path.dirname(os.path.abspath(__file__))

def stamp(msg):
    print(f"[{time.time()-t_ini:7.1f}s] {msg}", flush=True)

# ---------------------------------------------------------------- bases
E5 = np.zeros((5, 3, 3))
E5[0] = np.diag([1, -1, 0]) / np.sqrt(2)
E5[1] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / np.sqrt(2)
E5[2] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]]) / np.sqrt(2)
E5[3] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]]) / np.sqrt(2)
E5[4] = np.diag([-1, -1, 2]) / np.sqrt(6)
sq2 = np.sqrt(2.0)
mvec = np.array([1, 1j, 0]) / sq2
nvec = np.array([1, -1j, 0]) / sq2
zvec = np.array([0, 0, 1.0])
Ym = {+2: np.outer(mvec, mvec),
      +1: (np.outer(mvec, zvec) + np.outer(zvec, mvec)) / sq2,
       0: np.diag([-1., -1., 2.]) / np.sqrt(6),
      -1: (np.outer(nvec, zvec) + np.outer(zvec, nvec)) / sq2,
      -2: np.outer(nvec, nvec)}
A_cyc_z = (Ym[+2] + sq2 * Ym[-1]) / np.sqrt(3)
assert abs(np.trace(A_cyc_z @ A_cyc_z)) < 1e-12
A0_GL = 0.47211                       # amplitud del vacio D4 (control §16)

# ------------------------------------------------------ parametros fisicos
H_LAT  = 1.0     # paso de red (el del GL)
MU     = 0.64    # kF_continuo = 0.8; nodos polares del D4 en kz=+-0.8 EXACTO
KF     = 0.8     # normalizacion del prefactor del gap (fija SIEMPRE)
DELTA0 = 0.6     # gap max del fondo ~ Delta0*a0 ~ 0.28; xi_BdG ~ vF/gap ~ 5.7
R_CORE = 8.0     # disco de peso de core (~1.4 xi_BdG, ~4 xi_GL)
W_BORDE = 6.0    # franja de peso de borde (distancia al borde de la caja)
UMBRAL_CORE = 0.40   # peso de core para clasificar rama (sensib.: .25/.55)
NEV    = 60      # autovalores por kz (shift-invert sigma=0)
EPS_CRUCE = 0.02     # min|E| para declarar cruce real (minigap ~0.06)
DKZ_MIN = 0.008      # resolucion de la biseccion en kz

# ============================================================ ensamblado BdG
def bdg_sparse(Afield, kz, mu=MU, D0=DELTA0, h=H_LAT):
    """Afield (Ny,Nx,3,3) complejo -> H csr 4M x 4M, bloques [uu, ud, vu, vd].
    xi: laplaciano 5 puntos; {A,k}/2 con promedio de enlace (dif. centrada):
    hermiticidad EXACTA por construccion."""
    Ny, Nx = Afield.shape[:2]
    M = Ny * Nx
    ii = np.arange(M).reshape(Ny, Nx)

    diag_xi = np.full(M, 4.0 / h**2 + kz**2 - mu)
    rows, cols, vals = [np.arange(M)], [np.arange(M)], [diag_xi]
    for (di, dj) in ((0, 1), (1, 0)):
        src = ii[:Ny - di, :Nx - dj].ravel()
        dst = ii[di:, dj:].ravel()
        hop = np.full(src.size, -1.0 / h**2)
        rows += [src, dst]; cols += [dst, src]; vals += [hop, hop]
    XI = sp.csr_matrix((np.concatenate(vals),
                        (np.concatenate(rows), np.concatenate(cols))),
                       shape=(M, M))

    Amu = np.transpose(Afield, (2, 3, 0, 1))     # (spin, orb, Ny, Nx)
    pref = D0 / KF
    Dmu = []
    for mu_s in range(3):
        rowsD = [np.arange(M)]; colsD = [np.arange(M)]
        valsD = [pref * kz * Amu[mu_s, 2].ravel().astype(complex)]
        for j_orb, (di, dj) in ((0, (0, 1)), (1, (1, 0))):
            Aj = Amu[mu_s, j_orb]
            src = ii[:Ny - di, :Nx - dj]
            dst = ii[di:, dj:]
            Aenl = 0.5 * (Aj[:Ny - di, :Nx - dj] + Aj[di:, dj:])
            c = -1j / (2.0 * h) * pref * Aenl.ravel()
            rowsD += [src.ravel(), dst.ravel()]
            colsD += [dst.ravel(), src.ravel()]
            valsD += [c, -c]
        Dmu.append(sp.csr_matrix((np.concatenate(valsD),
                                  (np.concatenate(rowsD), np.concatenate(colsD))),
                                 shape=(M, M)))
    D1, D2, D3 = Dmu
    Del_uu = -D1 + 1j * D2
    Del_dd = D1 + 1j * D2
    H = sp.bmat([[XI, None, Del_uu, D3],
                 [None, XI, D3, Del_dd],
                 [Del_uu.conj().T, D3.conj().T, -XI, None],
                 [D3.conj().T, Del_dd.conj().T, None, -XI]], format='csr')
    return H

# --------------------------------------------- autotests (grilla chica random)
def autotest_bdg():
    N = 20; kz0 = 0.37
    xr = np.zeros((10, N, N))
    for a in range(10):
        base = rng.standard_normal((5, 5))
        xr[a] = 0.3 * np.kron(base, np.ones((4, 4)))
    Ar = np.einsum('aij,ayx->yxij', E5, xr[:5] + 1j * xr[5:])
    H = bdg_sparse(Ar, kz0)
    herm = spla.norm((H - H.conj().T).tocsr(), np.inf)
    M = N * N
    P = sp.bmat([[None, None, sp.eye(M), None],
                 [None, None, None, sp.eye(M)],
                 [sp.eye(M), None, None, None],
                 [None, sp.eye(M), None, None]], format='csr')
    ph = spla.norm((P @ bdg_sparse(Ar, kz0).conj() @ P
                    + bdg_sparse(Ar, -kz0)).tocsr(), np.inf)
    stamp(f"[autotest] hermiticidad {herm:.1e} | PH {ph:.1e}")
    assert herm < 1e-12 and ph < 1e-12

autotest_bdg()

# ============================================ FHS: Chern por rebanada (bulk)
def h_k(Auni, kx, ky, kz, mu=MU, D0=DELTA0, h=H_LAT):
    xi = (4 - 2 * np.cos(kx * h) - 2 * np.cos(ky * h)) / h**2 + kz**2 - mu
    d = (D0 / KF) * (Auni[:, 0] * np.sin(kx * h) / h
                     + Auni[:, 1] * np.sin(ky * h) / h + Auni[:, 2] * kz)
    Dsp = np.array([[-d[0] + 1j * d[1], d[2]], [d[2], d[0] + 1j * d[1]]])
    Hk = np.zeros((4, 4), complex)
    Hk[:2, :2] = xi * np.eye(2); Hk[2:, 2:] = -xi * np.eye(2)
    Hk[:2, 2:] = Dsp; Hk[2:, :2] = Dsp.conj().T
    return Hk

def chern_slice(Auni, kz, nk=90):
    """FHS sobre la BZ entera, proyector de las 2 bandas negativas."""
    ks = np.linspace(-np.pi, np.pi, nk, endpoint=False)
    V = np.empty((nk, nk, 4, 2), complex)
    gapmin = 1e9
    for i, kx in enumerate(ks):
        for j, ky in enumerate(ks):
            w, v = np.linalg.eigh(h_k(Auni, kx, ky, kz))
            V[i, j] = v[:, :2]
            gapmin = min(gapmin, w[2] - w[1])
    F = 0.0
    for i in range(nk):
        ip = (i + 1) % nk
        for j in range(nk):
            jp = (j + 1) % nk
            U1 = np.linalg.det(V[i, j].conj().T @ V[ip, j])
            U2 = np.linalg.det(V[ip, j].conj().T @ V[ip, jp])
            U3 = np.linalg.det(V[ip, jp].conj().T @ V[i, jp])
            U4 = np.linalg.det(V[i, jp].conj().T @ V[i, j])
            F += np.angle(U1 * U2 * U3 * U4)
    return F / (2 * np.pi), gapmin

def gap_bulk_min(Auni, kz, nk=160):
    """gap minimo 2|E_min| del bulk uniforme en la rebanada kz.
    Espectro exacto del 4x4: E^2 = xi^2 + |d|^2 +- |d x d*|,
    con |d x d*|^2 = |d|^4 - |d.d|^2 (no-unitariedad)."""
    ks = np.linspace(-np.pi, np.pi, nk, endpoint=False)
    KX, KY = np.meshgrid(ks, ks, indexing='ij')
    xi = (4 - 2 * np.cos(KX) - 2 * np.cos(KY)) + kz**2 - MU
    pref = DELTA0 / KF
    d = (np.einsum('s,yx->syx', Auni[:, 0], np.sin(KX))
         + np.einsum('s,yx->syx', Auni[:, 1], np.sin(KY))
         + Auni[:, 2][:, None, None] * kz) * pref
    dd = np.einsum('syx,syx->yx', d, d.conj()).real
    q = np.abs(np.einsum('syx,syx->yx', d, d))
    dxd = np.sqrt(np.maximum(dd**2 - q**2, 0.0))
    Emin2 = xi**2 + dd - dxd
    return 2.0 * np.sqrt(np.maximum(Emin2, 0.0)).min()

def localizar_nodos(Auni):
    """proyecciones kz de los ceros del gap de bulk (nodos de la RED):
    minimos locales ~0 de gap(kz), refinados por busqueda ternaria."""
    kz_grid = np.linspace(-1.05, 1.05, 211)
    gaps = np.array([gap_bulk_min(Auni, kz, nk=120) for kz in kz_grid])
    nodos = []
    for i in range(1, len(kz_grid) - 1):
        if gaps[i] < gaps[i - 1] and gaps[i] < gaps[i + 1] and gaps[i] < 0.02:
            lo, hi = kz_grid[i - 1], kz_grid[i + 1]
            for _ in range(40):
                m1 = lo + (hi - lo) / 3; m2 = hi - (hi - lo) / 3
                if gap_bulk_min(Auni, m1, nk=120) < gap_bulk_min(Auni, m2, nk=120):
                    hi = m2
                else:
                    lo = m1
            nodos.append(0.5 * (lo + hi))
    return np.array(nodos), gaps, kz_grid

# ==================================================== real-space: clasificador
def setup_geo(N, h=H_LAT):
    yy, xx = np.mgrid[0:N, 0:N].astype(float)
    xx = (xx + 0.5) * h; yy = (yy + 0.5) * h
    cx = cy = N * h / 2
    r = np.hypot(xx - cx, yy - cy)
    dist_borde = np.minimum.reduce([xx, yy, N * h - xx, N * h - yy])
    return {"N": N, "M": N * N, "rr": r.ravel(),
            "mask_core": (r < R_CORE).ravel(),
            "mask_borde": (dist_borde < W_BORDE).ravel()}

def pesos_estado(vec, G):
    """(peso_core, peso_borde, r_medio); peso por sitio sumando las 4
    componentes Nambu-espin (leccion §33.E: contar por peso)."""
    M = G["M"]
    w = np.abs(vec)**2
    wsite = w[:M] + w[M:2*M] + w[2*M:3*M] + w[3*M:]
    tot = max(wsite.sum(), 1e-30)
    wc = float(wsite[G["mask_core"]].sum() / tot)
    wb = float(wsite[G["mask_borde"]].sum() / tot)
    rm = float((wsite * G["rr"]).sum() / tot)
    return wc, wb, rm

def espectro_en(Afield, kz, G, nev=NEV, mu=MU, D0=DELTA0):
    Hc = bdg_sparse(Afield, kz, mu=mu, D0=D0).tocsc()
    E, V = spla.eigsh(Hc, k=nev, sigma=0.0, which='LM')
    orden = np.argsort(E)
    return E[orden], V[:, orden]

# ============================== flujo espectral con tracking por solapamiento
def _refina_cruce(Afield, kz1, kz2, vec1, E1, G, nev, mu, D0):
    """Biseccion siguiendo la rama por solapamiento: en kz1 la rama tiene
    E1 (signo s1) y vector vec1; en kz2 el apareo vio signo opuesto.
    Registra min|E| de la rama para separar cruce real de anticruce."""
    s1 = np.sign(E1)
    minabs = abs(E1)
    while (kz2 - kz1) > DKZ_MIN:
        km = 0.5 * (kz1 + kz2)
        E, V = espectro_en(Afield, km, G, nev=nev, mu=mu, D0=D0)
        j = int(np.argmax(np.abs(vec1.conj() @ V)))
        Em = E[j]
        minabs = min(minabs, abs(Em))
        if np.sign(Em) == s1:
            kz1, vec1, E1 = km, V[:, j], Em
        else:
            kz2 = km
    signo = +1 if s1 < 0 else -1        # de s1 a -s1 al crecer kz
    return 0.5 * (kz1 + kz2), signo, minabs

def barrido_flujo(Afield, kzs, G, tag="", nev=NEV, mu=MU, D0=DELTA0,
                  umbral_core=UMBRAL_CORE, refinar=True, guardar=None):
    """Barre kz; trackea por solapamiento; detecta cruces de E=0 de ramas
    con peso de core; separa cruces reales de anticruces por min|E|."""
    datos, cruces, anticruces = [], [], []
    E_prev = V_prev = wc_prev = None
    kz_prev = None
    for kz in kzs:
        E, V = espectro_en(Afield, kz, G, nev=nev, mu=mu, D0=D0)
        wc = np.empty(len(E)); wb = np.empty(len(E))
        for n in range(len(E)):
            wc[n], wb[n], _ = pesos_estado(V[:, n], G)
        datos.append((kz, E.copy(), wc.copy(), wb.copy()))
        if E_prev is not None:
            S = np.abs(V_prev.conj().T @ V)
            usados = set()
            for i in range(len(E_prev)):
                j = int(np.argmax(S[i]))
                if S[i, j] < 0.5 or j in usados:
                    continue
                usados.add(j)
                if E_prev[i] * E[j] < 0:
                    wcm = 0.5 * (wc[j] + wc_prev[i])
                    if wcm >= umbral_core:
                        if refinar:
                            kzc, sgn, mab = _refina_cruce(
                                Afield, kz_prev, kz, V_prev[:, i], E_prev[i],
                                G, nev, mu, D0)
                        else:
                            kzc = 0.5 * (kz_prev + kz)
                            sgn = int(np.sign(E[j] - E_prev[i]))
                            mab = 0.0
                        reg = dict(kz=float(kzc), signo=int(sgn),
                                   wc=float(wcm), minabs=float(mab),
                                   E1=float(E_prev[i]), E2=float(E[j]))
                        if mab <= EPS_CRUCE:
                            cruces.append(reg)
                            stamp(f"  [{tag}] CRUCE core kz~{kzc:+.3f} "
                                  f"signo {int(sgn):+d} wc={wcm:.2f} "
                                  f"min|E|={mab:.4f}")
                        else:
                            anticruces.append(reg)
                            stamp(f"  [{tag}] anticruce (hibridizacion) "
                                  f"kz~{kzc:+.3f} min|E|={mab:.4f} wc={wcm:.2f}")
        E_prev, V_prev, wc_prev, kz_prev = E, V, wc, kz
    if guardar:
        np.savez_compressed(guardar,
                            kzs=np.array([d[0] for d in datos]),
                            Es=np.array([d[1] for d in datos]),
                            wcs=np.array([d[2] for d in datos]),
                            wbs=np.array([d[3] for d in datos]),
                            cruces=json.dumps(cruces),
                            anticruces=json.dumps(anticruces))
    return datos, cruces, anticruces

def C_de(cruces, umbral=None):
    if umbral is None:
        return int(sum(c["signo"] for c in cruces))
    return int(sum(c["signo"] for c in cruces if c["wc"] >= umbral))

# ============================================================================
MODO = sys.argv[1] if len(sys.argv) > 1 else "todo"
resultados = {}

def cargar_npz():
    dat = np.load(os.path.join(AQUI, "paso_b_core.npz"))
    x = dat["x"]; N = int(dat["N"])
    assert N == 80 and abs(float(dat["E"]) - 11.88573) < 5e-4
    return x, N, float(dat["E"])

# ---------------------------------------------------------------- CONTROLES
if MODO in ("todo", "controles"):
    stamp("== CONTROL 1a: nodos y perfil de Chern de la CICLICA (FHS red) ==")
    A_c = A_cyc_z * (A0_GL * sq2)       # misma norma que el fondo D4
    nodos_c, _, _ = localizar_nodos(A_c)
    stamp(f"  proyecciones kz de nodos de la red: {np.round(nodos_c, 4)}")
    kz_bordes = np.concatenate([[-1.15], np.sort(nodos_c), [1.15]])
    perfil = []
    for i in range(len(kz_bordes) - 1):
        km = 0.5 * (kz_bordes[i] + kz_bordes[i + 1])
        C, g = chern_slice(A_c, km, nk=90)
        perfil.append(round(C))
        stamp(f"  ventana ({kz_bordes[i]:+.3f},{kz_bordes[i+1]:+.3f}): "
              f"C = {C:+.3f} -> {round(C):+d} (gap {g:.3f})")
    ok1a = (len(nodos_c) == 4 and perfil[0] == 0 and perfil[-1] == 0
            and sorted(map(abs, perfil)) == [0, 0, 1, 1, 2]
            and perfil[1] * perfil[2] < 0 and perfil[2] * perfil[3] < 0)
    resultados["control1a"] = {"nodos": nodos_c.tolist(), "perfil": perfil,
                               "PASS": bool(ok1a)}
    stamp(f"  CONTROL 1a: perfil {perfil} "
          f"{'PASS: (1,-2,1,0)-like, alternado, cierra en 0' if ok1a else 'FAIL'}")

    stamp("== CONTROL 1a-bis: D4 uniforme => C=0 y nodos SOLO polares ==")
    A_d4 = A0_GL * np.diag([1., -1., 0.]).astype(complex)
    nodos_d, _, _ = localizar_nodos(A_d4)
    stamp(f"  nodos del D4 (esperado: kz=+-{np.sqrt(MU):.3f} exacto): "
          f"{np.round(nodos_d, 4)}")
    Cs_d4 = []
    for kz in (0.0, 0.3, 0.6, 0.75):
        C, g = chern_slice(A_d4, kz, nk=90)
        Cs_d4.append(round(C))
        stamp(f"  kz={kz:+.2f}: C = {C:+.3f} (gap {g:.3f})")
    ok1ab = (all(c == 0 for c in Cs_d4) and len(nodos_d) == 2
             and np.allclose(np.abs(nodos_d), np.sqrt(MU), atol=0.01))
    resultados["control1a_d4"] = {"nodos": nodos_d.tolist(), "Cs": Cs_d4,
                                  "PASS": bool(ok1ab)}
    stamp(f"  CONTROL 1a-bis: {'PASS' if ok1ab else 'FAIL'}")

    N = 80; G = setup_geo(N)
    stamp("== CONTROL 2: D4 uniforme sin defecto (real-space, caja 80x80) ==")
    A_d4f = np.broadcast_to(A_d4, (N, N, 3, 3)).copy()
    kzs = np.linspace(-0.76, 0.76, 13)
    _, cr_d4, ac_d4 = barrido_flujo(A_d4f, kzs, G, tag="D4-unif", refinar=False)
    resultados["control2_d4"] = {"cruces": len(cr_d4), "PASS": len(cr_d4) == 0}
    stamp(f"  CONTROL 2 (D4): cruces de core = {len(cr_d4)} "
          f"{'PASS' if len(cr_d4) == 0 else 'FAIL'}")

    stamp("== CONTROL 1b: ciclica uniforme (borde poblado, core vacio) ==")
    A_cf = np.broadcast_to(A_c, (N, N, 3, 3)).copy()
    _, cr_cy, ac_cy = barrido_flujo(A_cf, kzs, G, tag="cyc-unif", refinar=False)
    E_mid, V_mid = espectro_en(A_cf, 0.1, G)
    orden_abs = np.argsort(np.abs(E_mid))[:8]
    wb_mid = [pesos_estado(V_mid[:, n], G)[1] for n in orden_abs]
    ok1b = (len(cr_cy) == 0 and max(wb_mid) > 0.5)
    resultados["control1b"] = {"cruces_core": len(cr_cy),
                               "wb_subgap": [float(v) for v in wb_mid],
                               "PASS": bool(ok1b)}
    stamp(f"  CONTROL 1b: cruces core={len(cr_cy)}, peso de borde max de los "
          f"8 sub-gap = {max(wb_mid):.2f} {'PASS' if ok1b else 'FAIL'}")

# ------------------------------------------------------------- CALCULO REAL
if MODO in ("todo", "real"):
    stamp("== CALCULO REAL: flujo espectral del HQV (campo del Paso A) ==")
    x, N, E_gl = cargar_npz()
    G = setup_geo(N)
    Afield = np.einsum('aij,ayx->yxij', E5, x[:5] + 1j * x[5:])
    r_flat = G["rr"]
    tloc = np.einsum('yxij,yxij->yx', Afield, Afield.conj()).real.ravel()
    sel = r_flat < 1.0
    T = tloc[sel].sum()
    w_p2 = (np.abs(np.einsum('ij,yxij->yx', Ym[+2].conj(), Afield)
                   .ravel()[sel])**2).sum() / T
    w_m1 = (np.abs(np.einsum('ij,yxij->yx', Ym[-1].conj(), Afield)
                   .ravel()[sel])**2).sum() / T
    stamp(f"  [npz OK] E_GL={E_gl:+.5f}; core r<1: w[+2]={w_p2:.3f} "
          f"w[-1]={w_m1:.3f} (acta §7: 0.473/0.406)")
    assert abs(w_p2 - 0.473) < 0.02 and abs(w_m1 - 0.406) < 0.02

    kzs = np.linspace(-0.78, 0.78, 40)
    datos, cruces, anticr = barrido_flujo(
        Afield, kzs, G, tag="HQV", refinar=True,
        guardar=os.path.join(AQUI, "paso_b_flujo_hqv.npz"))
    resultados["real"] = {"cruces": cruces, "anticruces": anticr,
                          "C_neto": C_de(cruces),
                          "C_umbral_025": C_de(cruces, 0.25),
                          "C_umbral_055": C_de(cruces, 0.55)}
    stamp(f"  >>> HQV real: {len(cruces)} cruces reales, "
          f"{len(anticr)} anticruces, C_neto = {C_de(cruces):+d} <<<")
    stamp(f"      sensibilidad umbral de peso: "
          f"0.25 -> {C_de(cruces, 0.25):+d} | 0.55 -> {C_de(cruces, 0.55):+d}")
    # espectro en kz=0: ¿Majorana del HQV?
    E0, V0 = espectro_en(Afield, 0.0, G)
    j0 = int(np.argmin(np.abs(E0)))
    wc0, wb0, rm0 = pesos_estado(V0[:, j0], G)
    stamp(f"      kz=0: |E|_min = {abs(E0[j0]):.5f} "
          f"(wc={wc0:.2f}, wb={wb0:.2f}, <r>={rm0:.1f})")
    resultados["real"]["kz0_Emin"] = float(abs(E0[j0]))
    resultados["real"]["kz0_wc"] = float(wc0)

# ------------------------------------------------------------------- ESPEJO
if MODO in ("todo", "espejo"):
    stamp("== CONTROL 3: espejo (campo conjugado, HQV(-1/2,-1/4)) ==")
    x, N, _ = cargar_npz()
    G = setup_geo(N)
    x_esp = x.copy(); x_esp[5:] = -x_esp[5:]
    Aesp = np.einsum('aij,ayx->yxij', E5, x_esp[:5] + 1j * x_esp[5:])
    kzs = np.linspace(-0.78, 0.78, 40)
    _, cr_esp, ac_esp = barrido_flujo(
        Aesp, kzs, G, tag="espejo", refinar=True,
        guardar=os.path.join(AQUI, "paso_b_flujo_espejo.npz"))
    resultados["espejo"] = {"cruces": cr_esp, "anticruces": ac_esp,
                            "C_neto": C_de(cr_esp)}
    stamp(f"  >>> espejo: C_neto = {C_de(cr_esp):+d} "
          f"(esperado: el del real invertido) <<<")

# -------------------------------------------------------------- ESTABILIDAD
if MODO in ("todo", "estabilidad"):
    stamp("== CONTROL 4: estabilidad en Delta0 y mu ==")
    x, N, _ = cargar_npz()
    G = setup_geo(N)
    Afield = np.einsum('aij,ayx->yxij', E5, x[:5] + 1j * x[5:])
    est = {}
    for nombre, D0v, muv in (("D0x0.7", DELTA0 * 0.7, MU),
                             ("D0x1.4", DELTA0 * 1.4, MU),
                             ("mux0.8", DELTA0, MU * 0.8),
                             ("mux1.2", DELTA0, MU * 1.2)):
        kf_v = np.sqrt(muv)
        kzs = np.linspace(-0.97 * kf_v, 0.97 * kf_v, 28)
        _, cr_e, ac_e = barrido_flujo(Afield, kzs, G, tag=nombre,
                                      mu=muv, D0=D0v, refinar=True)
        est[nombre] = {"C_neto": C_de(cr_e), "cruces": len(cr_e),
                       "anticruces": len(ac_e)}
        stamp(f"  [{nombre}] C_neto = {C_de(cr_e):+d} "
              f"({len(cr_e)} cruces, {len(ac_e)} anticruces)")
    resultados["estabilidad"] = est

# ---------------------------------------- BONUS: control del MECANISMO
# (no pre-declarado; se agrega tras la lectura fisica del armado del BdG):
# el fondo D4 tiene columna z NULA => a kz fijo conserva PH de rebanada =>
# el HQV DESNUDO (solo m=+-2) deberia dar rama de core ~plana en E~0 SIN
# flujo neto; el relleno ciclico (m=-1, columna z NO nula) es lo que inclina
# la rama. Proyectamos el campo del npz a m in {+2,-2} y repetimos el conteo:
# si el C_neto se apaga al vaciar el core, el mecanismo queda probado.
if MODO in ("vaciado",):
    stamp("== BONUS: HQV VACIADO (proyeccion m in {+2,-2}) ==")
    x, N, _ = cargar_npz()
    G = setup_geo(N)
    Afull = np.einsum('aij,ayx->yxij', E5, x[:5] + 1j * x[5:])
    Avac = np.zeros_like(Afull)
    for m_ in (+2, -2):
        c_m = np.einsum('ij,yxij->yx', Ym[m_].conj(), Afull)
        Avac += np.einsum('yx,ij->yxij', c_m, Ym[m_])
    quitado = float(np.linalg.norm(Afull - Avac) / np.linalg.norm(Afull))
    stamp(f"  norma quitada al proyectar: {quitado:.3f} (m=+-1 y m=0 fuera)")
    kzs = np.linspace(-0.78, 0.78, 40)
    _, cr_v, ac_v = barrido_flujo(
        Avac, kzs, G, tag="vaciado", refinar=True,
        guardar=os.path.join(AQUI, "paso_b_flujo_vaciado.npz"))
    resultados["vaciado"] = {"cruces": cr_v, "anticruces": ac_v,
                             "C_neto": C_de(cr_v),
                             "norma_quitada": quitado}
    stamp(f"  >>> vaciado: C_neto = {C_de(cr_v):+d} "
          f"(mecanismo probado si se apaga vs el real) <<<")
    E0, V0 = espectro_en(Avac, 0.0, G)
    j0 = int(np.argmin(np.abs(E0)))
    wc0, wb0, rm0 = pesos_estado(V0[:, j0], G)
    stamp(f"      kz=0: |E|_min = {abs(E0[j0]):.5f} (wc={wc0:.2f})")

# ------------------------------------------------------------------- resumen
sufijo = "" if MODO == "todo" else f"_{MODO}"
out_json = os.path.join(AQUI, f"paso_b_resultados{sufijo}.json")
with open(out_json, "w") as f:
    json.dump(resultados, f, indent=1)
stamp(f"resultados -> {out_json}")
stamp("FIN")
