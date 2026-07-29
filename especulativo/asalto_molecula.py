# ETAPA ESPECULATIVA TCI 2.0 - calculo preliminar, no validado
# ============================================================================
# EL FERMION DE LA RED, PRIMER ASALTO: LA MOLECULA DE DIRAC (2026-07-29)
#
# Continuacion directa de la compuerta unica (Paso B, C_neto=-1 por HQV).
# El U(1) fermionico de la red (§34.A) necesita un portador CARGADO: una rama
# Majorana sola es "media materia" y no carga U(1). El mar organiza sus
# vortices enteros como MOLECULAS de dos medios (§30): (w_phi,w_alpha) =
# (1/2,+1/4) [especie A] + (1/2,-1/4) [especie B] — fase sumada entera,
# marco neto cero.
#
# LA PREGUNTA CENTRAL (genuinamente abierta): ¿la quiralidad de la rama del
# core sigue a la FASE o al MARCO?
#   - sigue a la fase  => C_B = C_A = -1 => C_molecula = -2: fermion de
#     Dirac QUIRAL cargado — el portador del U(1) existe (FALTA 1 en camino).
#   - sigue al marco   => C_B = +1 => C_molecula = 0: molecula esteril,
#     el U(1) de la red pierde su portador quiral (crisis del FALTA 1).
# El espejo del Paso A/B no la separa (invierte fase Y marco a la vez). El
# argumento "rotacion interna pura m->-m es unitaria => mismo C" es FALAZ:
# esa operacion NO es simetria del funcional (el termino div — donde vive la
# bisagra — acopla indices internos con el plano); la simetria verdadera
# involucra k_z -> -k_z y puede invertir el conteo. Lo decide el numero.
#
# PLAN:
#   MODO especieB : relajar el HQV(1/2,-1/4) con QA (3 semillas: ciclica
#     espejada / ciclica original / ruido) -> core y E vs especie A ->
#     BdG + flujo espectral -> C_B.
#   MODO molecula : ansatz de dos centros a d=6 (phi = (th1+th2)/2,
#     alpha = (th1-th2)/4; London congelado en el borde = vortice de fase
#     entero con marco trivial lejos), cores sembrados con los ganadores
#     de cada especie -> relajar -> BdG -> C_mol; control espejo (conjugado
#     total => C_mol invertido); consistencia C_mol vs C_A+C_B.
#
# HERENCIA DECLARADA: el GL (potencial caso C, gradiente Wirtinger, F_div,
# relajador por norma de gradiente) es el de paso_a_bisagra_core.py /
# paso_b_core_input.py, textual; el BdG (ensamblado sparse, pesos por sitio,
# tracking por solapamiento, refinador con min|E|) es el de
# paso_b_bdg_core.py, textual. Autotests re-corridos aca.
#
# Uso: python -u asalto_molecula.py [especieB|molecula]
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
A_cyc_z = (Ym[+2] + sq2 * Ym[-1]) / np.sqrt(3)      # ciclica C3||z, L=0
A_cyc_sw = (Ym[-2] + sq2 * Ym[+1]) / np.sqrt(3)     # su imagen m->-m
assert abs(np.trace(A_cyc_z @ A_cyc_z)) < 1e-12
assert abs(np.trace(A_cyc_sw @ A_cyc_sw)) < 1e-12

AL, BE, GA, EPS = -1.0, 1.0, +0.15, 0.05   # caso C (§16)
K = 1.0
PARAMS = (AL, BE, GA, EPS)

# =========================== GL heredado (Paso A, textual) ===========================
def V_sites(x, al, be, ga, eps):
    xc = x[:5] + 1j * x[5:]
    A = np.einsum('am,aij->mij', xc, E5)
    Ab = A.conj()
    t  = np.einsum('mij,mij->m', A, Ab).real
    u  = np.einsum('mij,mji->m', A, A); ub = u.conj()
    A2 = A @ A; Ab2 = Ab @ Ab
    tr = lambda P, Q: np.einsum('mij,mji->m', P, Q)
    q4 = t**2 - tr(Ab2, A2).real
    M1 = Ab @ A
    s6 = (-3 * t * (u * ub).real + 4 * t**3
          + 6 * t * tr(Ab2, A2).real
          + 12 * t * tr(M1, M1).real
          - 6 * (ub * tr(Ab @ A2, A)).real
          - 6 * (u * tr(Ab2 @ Ab, A)).real
          - 12 * tr(Ab2 @ Ab, A @ A2).real
          + 12 * tr(Ab2 @ A2, M1).real
          + 8 * tr(M1 @ M1, M1).real)
    return al * t + be * q4 + ga * s6 + eps * t**4

def gradV_sites(x, al, be, ga, eps):
    xc = x[:5] + 1j * x[5:]
    A = np.einsum('am,aij->mij', xc, E5); Ab = A.conj()
    t = np.einsum('mij,mij->m', A, Ab).real
    u = np.einsum('mij,mji->m', A, A); ub = u.conj()
    A2 = A @ A; Ab2 = Ab @ Ab; A3 = A2 @ A; Ab3 = Ab2 @ Ab
    AbA = Ab @ A; AAb = A @ Ab
    trc = lambda P_, Q_: np.einsum('mij,mji->m', P_, Q_)
    Tr32 = trc(Ab2, A2); Tr1212 = trc(AbA, AbA); T6 = trc(Ab3, A)
    sc = lambda s: s[:, None, None]
    Ab2A = Ab2 @ A; AAb2 = A @ Ab2; AbA2 = Ab @ A2; A2Ab = A2 @ Ab
    P = (al * Ab
         + be * (2 * sc(t) * Ab - (Ab2A + AAb2))
         + eps * 4 * sc(t**3) * Ab)
    if ga != 0.0:
        P = P + ga * (
            -3 * (sc(u * ub) * Ab + 2 * sc(t) * sc(ub) * A)
            + 12 * sc(t**2) * Ab
            + 6 * (sc(Tr32) * Ab + sc(t) * (Ab2A + AAb2))
            + 12 * (sc(Tr1212) * Ab + 2 * sc(t) * (Ab @ AAb))
            - 6 * sc(ub) * (AbA2 + A @ AbA + A2Ab)
            - 6 * (2 * sc(T6) * A + sc(u) * Ab3)
            - 12 * (Ab3 @ A2 + A @ Ab3 @ A + A2 @ Ab3)
            + 12 * (Ab2A @ AbA + AAb2 @ AAb + AbA2 @ Ab2)
            + 24 * AbA @ AbA @ Ab)
    tp = np.einsum('mij,aij->am', P, E5)
    g = np.empty_like(x)
    g[:5] = 2 * tp.real
    g[5:] = -2 * tp.imag
    return g

# autotest del gradiente (heredado)
xt = 0.4 * rng.standard_normal((10, 6))
gnum = np.empty((10, 6))
for a in range(10):
    xp = xt.copy(); xp[a] += 1e-6; xm = xt.copy(); xm[a] -= 1e-6
    gnum[a] = (V_sites(xp, *PARAMS) - V_sites(xm, *PARAMS)) / 2e-6
errg = np.max(np.abs(gradV_sites(xt, *PARAMS) - gnum))
assert errg < 1e-6
stamp(f"[autotest GL] gradiente Wirtinger {errg:.1e}")

# vacio D4 (re-verificado)
D = np.diag([1., -1., 0.])
def x_of_A(A):
    return np.concatenate([[np.real(np.trace(A @ E5[a])) for a in range(5)],
                           [np.imag(np.trace(A @ E5[a])) for a in range(5)]])
def V_scalar_x(xv):
    return float(V_sites(xv.reshape(10, 1), *PARAMS)[0])
aa = np.linspace(0.05, 1.2, 2000)
Va = np.array([V_scalar_x(x_of_A(a * D)) for a in aa])
a0 = aa[np.argmin(Va)]
for _ in range(60):
    h_ = 1e-4
    d1 = (V_scalar_x(x_of_A((a0+h_)*D)) - V_scalar_x(x_of_A((a0-h_)*D)))/(2*h_)
    d2 = (V_scalar_x(x_of_A((a0+h_)*D)) - 2*V_scalar_x(x_of_A(a0*D))
          + V_scalar_x(x_of_A((a0-h_)*D)))/h_**2
    a0 -= d1/d2
V0 = V_scalar_x(x_of_A(a0 * D))
stamp(f"[vacio] a0 = {a0:.5f}  V0 = {V0:.6f}  (control §16: 0.47211)")
assert abs(a0 - 0.47211) < 1e-4

def A_grid(x):
    xc = x[:5] + 1j * x[5:]
    return np.einsum('aij,ayx->ijyx', E5, xc)

def D_vec(Ag):
    Dx = np.zeros_like(Ag[0]); Dy = np.zeros_like(Ag[1])
    Dx[:, :, :-1] = Ag[0, :, :, 1:] - Ag[0, :, :, :-1]
    Dy[:, :-1, :] = Ag[1, :, 1:, :] - Ag[1, :, :-1, :]
    return Dx + Dy

def E_div(x):
    Dv = D_vec(A_grid(x))
    return 2 * K * np.sum(np.abs(Dv)**2)

def F_div(x):
    Dv = D_vec(A_grid(x))
    Gm = np.zeros((3, 3) + Dv.shape[1:], dtype=complex)
    Gm[0][:, :, :-1] -= Dv[:, :, :-1]
    Gm[0][:, :, 1:] += Dv[:, :, :-1]
    Gm[1][:, :-1, :] -= Dv[:, :-1, :]
    Gm[1][:, 1:, :] += Dv[:, :-1, :]
    Gm = 2 * K * Gm
    tp = np.einsum('ijyx,aij->ayx', Gm, E5)
    f = np.empty((10,) + Dv.shape[1:])
    f[:5] = -2 * tp.real
    f[5:] = -2 * tp.imag
    return f

def setup(N, Lbox=80.0, xi=2.0):
    h = Lbox / N
    yy, xx = np.mgrid[0:N, 0:N].astype(float)
    xx = (xx + 0.5) * h; yy = (yy + 0.5) * h
    cx = cy = Lbox / 2
    return {"N": N, "h": h, "xx": xx, "yy": yy, "cx": cx, "cy": cy, "xi": xi,
            "borde": max(2, int(np.ceil(3.0 / h)))}

def ansatz_2c(G, centros, ws, vs, cores=None, amp_core=0.8, r_core=6.0):
    """generalizacion del ansatz_hqv del Paso A a M centros:
    phi = sum w_i th_i ; alpha = sum v_i th_i ; amp = prod tanh(r_i/xi).
    centros: [(x,y)...], cores: [matriz 3x3 o None]..."""
    N = G["N"]
    phi = np.zeros((N, N)); alp = np.zeros((N, N))
    amp = np.ones((N, N))
    rs = []
    for (cx, cy), w, v in zip(centros, ws, vs):
        th = np.arctan2(G["yy"] - cy, G["xx"] - cx)
        r = np.hypot(G["xx"] - cx, G["yy"] - cy)
        rs.append(r)
        phi += w * th; alp += v * th
        amp *= np.tanh(np.maximum(r, 1e-9) / G["xi"])
    c0 = amp * a0 * sq2 * np.cos(2 * alp)
    c1 = amp * a0 * sq2 * np.sin(2 * alp)
    x = np.zeros((10, N, N))
    x[0] = c0 * np.cos(phi); x[5] = c0 * np.sin(phi)
    x[1] = c1 * np.cos(phi); x[6] = c1 * np.sin(phi)
    if cores is not None:
        for r, core in zip(rs, cores):
            if core is None: continue
            g = amp_core * a0 * np.exp(-(r / r_core)**2)
            xc = x_of_A(core)
            for a_ in range(10):
                x[a_] += g * xc[a_]
    return x

def energia(x, G, con_div=True):
    gx = x[:, :, 1:] - x[:, :, :-1]
    gy = x[:, 1:, :] - x[:, :-1, :]
    Eg = K * (np.sum(gx**2) + np.sum(gy**2))
    Ev = G["h"]**2 * np.sum(V_sites(x.reshape(10, -1), *PARAMS) - V0)
    if con_div:
        Eg += E_div(x)
    return Eg + Ev

def fuerza(x, G, con_div=True):
    N = G["N"]
    lap = np.zeros_like(x)
    lap[:, 1:-1, 1:-1] = (x[:, 2:, 1:-1] + x[:, :-2, 1:-1] +
                          x[:, 1:-1, 2:] + x[:, 1:-1, :-2] - 4 * x[:, 1:-1, 1:-1])
    F = 2 * K * lap - G["h"]**2 * gradV_sites(x.reshape(10, -1), *PARAMS).reshape(10, N, N)
    if con_div:
        F += F_div(x)
    return F

def relajar_qa(x, G, con_div=True, max_pasos=60000, lr=0.02, mom=0.95,
               tol_grms=2e-7, informar=10000, tag=""):
    N = G["N"]; b = G["borde"]
    libre = np.ones((N, N), bool)
    libre[:b, :] = libre[-b:, :] = libre[:, :b] = libre[:, -b:] = False
    nlibre = np.sqrt(10.0 * libre.sum())
    vel = np.zeros_like(x)
    g_rms = np.inf
    lr_now = lr
    stall = 0
    for it in range(max_pasos):
        F = fuerza(x, G, con_div)
        F[:, ~libre] = 0.0
        vel = mom * vel + lr_now * F
        x = x + vel
        if (it + 1) % 1000 == 0:
            g_prev = g_rms
            g_rms = np.linalg.norm(F) / nlibre
            if informar and (it + 1) % informar == 0:
                stamp(f"      [{tag}] paso {it+1}: E={energia(x,G,con_div):.5f} "
                      f"g_rms={g_rms:.2e} lr={lr_now:.4f}")
            if g_rms < tol_grms:
                break
            if g_prev < np.inf and g_rms > 0.98 * g_prev:
                stall += 1
                if stall >= 3:
                    lr_now = min(lr_now * 1.3, 0.06)
                    stall = 0
            if not np.isfinite(g_rms):
                lr_now *= 0.5; vel[:] = 0; stall = 0
    for _ in range(2000):
        F = fuerza(x, G, con_div)
        F[:, ~libre] = 0.0
        x = x + 0.5 * lr * F
    F = fuerza(x, G, con_div); F[:, ~libre] = 0.0
    g_rms = np.linalg.norm(F) / nlibre
    return x, g_rms, (g_rms < tol_grms * 3)

def pesos_mJ_en(x, G, cx, cy, rmax):
    r = np.hypot(G["xx"] - cx, G["yy"] - cy).ravel()
    xc = x[:5] + 1j * x[5:]
    Afull = np.einsum('am,aij->mij', xc.reshape(5, -1), E5)
    tloc = np.einsum('mij,mij->m', Afull, Afull.conj()).real
    sel = r < rmax
    T = max(tloc[sel].sum(), 1e-30)
    out = {}
    for m_, Y_ in Ym.items():
        psi = np.einsum('ij,mij->m', Y_.conj(), Afull)
        out[m_] = float((np.abs(psi[sel])**2).sum() / T)
    return out

def winding_en(x, G, m_, cx, cy, R0, nth=96):
    xc = x[:5] + 1j * x[5:]
    Afull = np.einsum('am,aij->mij', xc.reshape(5, -1), E5)
    psi = np.einsum('ij,mij->m', Ym[m_].conj(), Afull).reshape(G["N"], G["N"])
    th = np.linspace(0, 2 * np.pi, nth, endpoint=False)
    fases = []
    for t_ in th:
        px = cx + R0 * np.cos(t_); py = cy + R0 * np.sin(t_)
        ix = int(round(px / G["h"] - 0.5)); iy = int(round(py / G["h"] - 0.5))
        fases.append(np.angle(psi[iy, ix]))
    fases = np.unwrap(np.array(fases))
    return (fases[-1] + (fases[1] - fases[0]) - fases[0]) / (2 * np.pi)

# =========================== BdG heredado (Paso B, textual) ===========================
H_LAT  = 1.0
MU     = 0.64
KF     = 0.8
DELTA0 = 0.6
W_BORDE = 6.0
UMBRAL_CORE = 0.40
NEV    = 60
EPS_CRUCE = 0.02
DKZ_MIN = 0.008

def bdg_sparse(Afield, kz, mu=MU, D0=DELTA0, h=H_LAT):
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
    Amu = np.transpose(Afield, (2, 3, 0, 1))
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
    stamp(f"[autotest BdG] hermiticidad {herm:.1e} | PH {ph:.1e}")
    assert herm < 1e-12 and ph < 1e-12

autotest_bdg()

def setup_geo(N, r_core, h=H_LAT):
    yy, xx = np.mgrid[0:N, 0:N].astype(float)
    xx = (xx + 0.5) * h; yy = (yy + 0.5) * h
    cx = cy = N * h / 2
    r = np.hypot(xx - cx, yy - cy)
    dist_borde = np.minimum.reduce([xx, yy, N * h - xx, N * h - yy])
    return {"N": N, "M": N * N, "rr": r.ravel(),
            "mask_core": (r < r_core).ravel(),
            "mask_borde": (dist_borde < W_BORDE).ravel()}

def pesos_estado(vec, G):
    M = G["M"]
    w = np.abs(vec)**2
    wsite = w[:M] + w[M:2*M] + w[2*M:3*M] + w[3*M:]
    tot = max(wsite.sum(), 1e-30)
    wc = float(wsite[G["mask_core"]].sum() / tot)
    wb = float(wsite[G["mask_borde"]].sum() / tot)
    return wc, wb

def espectro_en(Afield, kz, G, nev=NEV, mu=MU, D0=DELTA0):
    Hc = bdg_sparse(Afield, kz, mu=mu, D0=D0).tocsc()
    E, V = spla.eigsh(Hc, k=nev, sigma=0.0, which='LM')
    orden = np.argsort(E)
    return E[orden], V[:, orden]

def _refina_cruce(Afield, kz1, kz2, vec1, E1, G, nev, mu, D0):
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
    signo = +1 if s1 < 0 else -1
    return 0.5 * (kz1 + kz2), signo, minabs

def barrido_flujo(Afield, kzs, G, tag="", nev=NEV, mu=MU, D0=DELTA0,
                  umbral_core=UMBRAL_CORE, refinar=True, guardar=None):
    datos, cruces, anticruces = [], [], []
    E_prev = V_prev = wc_prev = None
    kz_prev = None
    for kz in kzs:
        E, V = espectro_en(Afield, kz, G, nev=nev, mu=mu, D0=D0)
        wc = np.empty(len(E)); wb = np.empty(len(E))
        for n in range(len(E)):
            wc[n], wb[n] = pesos_estado(V[:, n], G)
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
                                   wc=float(wcm), minabs=float(mab))
                        if mab <= EPS_CRUCE:
                            cruces.append(reg)
                            stamp(f"  [{tag}] CRUCE core kz~{kzc:+.3f} "
                                  f"signo {int(sgn):+d} wc={wcm:.2f} "
                                  f"min|E|={mab:.4f}")
                        else:
                            anticruces.append(reg)
                            stamp(f"  [{tag}] anticruce kz~{kzc:+.3f} "
                                  f"min|E|={mab:.4f} wc={wcm:.2f}")
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
MODO = sys.argv[1] if len(sys.argv) > 1 else "especieB"
resultados = {}
N = 80

if MODO == "especieB":
    stamp("== ESPECIE B: HQV(1/2,-1/4) — GL con QA de atractor (3 semillas) ==")
    G = setup(N)
    finales = {}
    for nombre, core in (("cyc-sw", A_cyc_sw), ("cyc-z", A_cyc_z), ("ruido", None)):
        x0 = ansatz_2c(G, [(G["cx"], G["cy"])], [0.5], [-0.25], cores=[core])
        if nombre == "ruido":
            b = G["borde"]
            pert = 0.3 * a0 * rng.standard_normal((10, N, N))
            mask = np.zeros((N, N)); mask[b:-b, b:-b] = 1.0
            r = np.hypot(G["xx"] - G["cx"], G["yy"] - G["cy"])
            pert *= (np.exp(-(r / 8.0)**2) * mask)[None]
            x0 = x0 + pert
        x1, g_rms, conv = relajar_qa(x0, G, tag=f"B-{nombre}", informar=20000)
        E1 = energia(x1, G)
        p = pesos_mJ_en(x1, G, G["cx"], G["cy"], 4.0)
        stamp(f"  [B-{nombre}] E={E1:+.5f} g_rms={g_rms:.1e} "
              f"{'CONV' if conv else '**NO CONV**'} core r<2xi: "
              + " ".join(f"[{m_:+d}]={p[m_]:.3f}" for m_ in (+2, +1, 0, -1, -2)))
        finales[nombre] = (x1, E1, conv)
    Es = {k: v[1] for k, v in finales.items()}
    ganador = min(Es, key=Es.get)
    x_B, E_B, _ = finales[ganador]
    stamp(f"  ganador: {ganador} E={E_B:+.5f} (control A: +11.88573; "
          f"degenerada si |dE|<~0.01)")
    resultados["especieB_GL"] = {"Es": {k: float(v) for k, v in Es.items()},
                                 "ganador": ganador, "E": float(E_B)}
    # windings del ganador (esperado: psi+2 con +1, psi-2 con 0 — invertido vs A)
    for m_ in (+2, -1, -2, +1):
        wnds = [winding_en(x_B, G, m_, G["cx"], G["cy"], R0) for R0 in (3., 8., 20.)]
        stamp(f"    winding psi[{m_:+d}]: " + "  ".join(f"{w_:+.2f}" for w_ in wnds))
    np.savez_compressed(os.path.join(AQUI, "asalto_especieB.npz"),
                        x=x_B, a0=a0, E=E_B, N=N, h=G["h"], w=0.5, v=-0.25)
    stamp("  [BdG de la especie B]")
    Afield = np.einsum('aij,ayx->yxij', E5, x_B[:5] + 1j * x_B[5:])
    Gb = setup_geo(N, r_core=8.0)
    kzs = np.linspace(-0.78, 0.78, 40)
    _, cr_B, ac_B = barrido_flujo(Afield, kzs, Gb, tag="espB", refinar=True,
                                  guardar=os.path.join(AQUI, "asalto_flujo_espB.npz"))
    C_B = C_de(cr_B)
    resultados["especieB_BdG"] = {"C_neto": C_B, "cruces": cr_B,
                                  "anticruces": ac_B}
    stamp(f"  >>> ESPECIE B: C_B = {C_B:+d}  "
          f"(C_A=-1; fase manda si C_B=-1, marco manda si C_B=+1) <<<")

elif MODO == "especieA_sw":
    # VERIFICACION URGENTE (hallazgo del 29/7): la simetria exacta K.T
    # (conjugar . reflejar y . rotar pi_x interno) conecta (1/2,+1/4) con
    # (1/2,-1/4) => fundamentales degenerados. Si el B da E=9.29 y el A dio
    # 11.89, el Paso A NO encontro el fundamental (su QA3 nunca sembro la
    # ciclica espejada). Test: relajar el (1/2,+1/4) con semilla A_cyc_sw.
    stamp("== ESPECIE A, SEMILLA ESPEJADA: HQV(1/2,+1/4) desde cyc-sw ==")
    G = setup(N)
    x0 = ansatz_2c(G, [(G["cx"], G["cy"])], [0.5], [+0.25], cores=[A_cyc_sw])
    x1, g_rms, conv = relajar_qa(x0, G, tag="A-sw", informar=20000)
    E1 = energia(x1, G)
    p = pesos_mJ_en(x1, G, G["cx"], G["cy"], 4.0)
    stamp(f"  [A-sw] E={E1:+.5f} g_rms={g_rms:.1e} "
          f"{'CONV' if conv else '**NO CONV**'} core r<2xi: "
          + " ".join(f"[{m_:+d}]={p[m_]:.3f}" for m_ in (+2, +1, 0, -1, -2)))
    stamp(f"  (Paso A publicado: +11.88573; especie B: +9.29373 — si A-sw ~9.29,"
          f" el fundamental del A es OTRO y el BdG del Paso B se recalcula)")
    for m_ in (+2, -1, -2, +1):
        wnds = [winding_en(x1, G, m_, G["cx"], G["cy"], R0) for R0 in (3., 8., 20.)]
        stamp(f"    winding psi[{m_:+d}]: " + "  ".join(f"{w_:+.2f}" for w_ in wnds))
    np.savez_compressed(os.path.join(AQUI, "asalto_especieA_sw.npz"),
                        x=x1, a0=a0, E=E1, N=N, h=G["h"], w=0.5, v=0.25)
    resultados["especieA_sw"] = {"E": float(E1), "conv": bool(conv)}
    if E1 < 11.5:
        stamp("  [A-sw] FUNDAMENTAL NUEVO CONFIRMADO — BdG sobre el:")
        Afield = np.einsum('aij,ayx->yxij', E5, x1[:5] + 1j * x1[5:])
        Gb = setup_geo(N, r_core=8.0)
        kzs = np.linspace(-0.78, 0.78, 40)
        _, cr_A2, ac_A2 = barrido_flujo(
            Afield, kzs, Gb, tag="A-sw", refinar=True,
            guardar=os.path.join(AQUI, "asalto_flujo_Asw.npz"))
        resultados["especieA_sw_BdG"] = {"C_neto": C_de(cr_A2),
                                         "cruces": cr_A2, "anticruces": ac_A2}
        stamp(f"  >>> A-sw: C = {C_de(cr_A2):+d} "
              f"(el C=-1 del Paso B era del metaestable) <<<")

elif MODO == "molecula":
    stamp("== MOLECULA: (1/2,+1/4) + (1/2,-1/4) a d=6 — GL + BdG ==")
    G = setup(N)
    d_half = 3.0
    cA = (G["cx"] - d_half, G["cy"]); cB = (G["cx"] + d_half, G["cy"])
    # cores sembrados con los ganadores de cada especie (ciclica y su swap)
    x0 = ansatz_2c(G, [cA, cB], [0.5, 0.5], [+0.25, -0.25],
                   cores=[A_cyc_z, A_cyc_sw])
    x1, g_rms, conv = relajar_qa(x0, G, tag="mol", informar=20000)
    E1 = energia(x1, G)
    stamp(f"  [mol] E={E1:+.5f} g_rms={g_rms:.1e} {'CONV' if conv else '**NO CONV**'}")
    for (cx_, cy_), lab in ((cA, "core A"), (cB, "core B")):
        p = pesos_mJ_en(x1, G, cx_, cy_, 3.0)
        stamp(f"    {lab} (r<3): " +
              " ".join(f"[{m_:+d}]={p[m_]:.3f}" for m_ in (+2, +1, 0, -1, -2)))
    # windings globales (lazo r=20 alrededor del centro: fase entera, marco 0)
    for m_ in (+2, -2):
        w_ = winding_en(x1, G, m_, G["cx"], G["cy"], 20.0)
        stamp(f"    winding global psi[{m_:+d}] (r=20): {w_:+.2f} (esperado +1)")
    np.savez_compressed(os.path.join(AQUI, "asalto_molecula.npz"),
                        x=x1, a0=a0, E=E1, N=N, h=G["h"])
    resultados["molecula_GL"] = {"E": float(E1), "conv": bool(conv)}
    stamp("  [BdG de la molecula]  (peso core = disco r<9 que envuelve ambos)")
    Afield = np.einsum('aij,ayx->yxij', E5, x1[:5] + 1j * x1[5:])
    Gb = setup_geo(N, r_core=9.0)
    kzs = np.linspace(-0.78, 0.78, 40)
    _, cr_M, ac_M = barrido_flujo(Afield, kzs, Gb, tag="mol", refinar=True,
                                  guardar=os.path.join(AQUI, "asalto_flujo_mol.npz"))
    C_M = C_de(cr_M)
    resultados["molecula_BdG"] = {"C_neto": C_M, "cruces": cr_M,
                                  "anticruces": ac_M}
    stamp(f"  >>> MOLECULA: C_mol = {C_M:+d}  "
          f"(Dirac quiral cargado si -2; esteril si 0) <<<")
    # control espejo de la molecula: conjugado total => C invertido
    stamp("  [control espejo de la molecula]")
    x_esp = x1.copy(); x_esp[5:] = -x_esp[5:]
    Aesp = np.einsum('aij,ayx->yxij', E5, x_esp[:5] + 1j * x_esp[5:])
    _, cr_E, ac_E = barrido_flujo(Aesp, kzs, Gb, tag="mol-esp", refinar=True)
    stamp(f"  >>> espejo de la molecula: C = {C_de(cr_E):+d} "
          f"(esperado {-C_M:+d}) <<<")
    resultados["molecula_espejo"] = {"C_neto": C_de(cr_E)}

out_json = os.path.join(AQUI, f"asalto_resultados_{MODO}.json")
with open(out_json, "w") as f:
    json.dump(resultados, f, indent=1)
stamp(f"resultados -> {out_json}")
stamp("FIN")
