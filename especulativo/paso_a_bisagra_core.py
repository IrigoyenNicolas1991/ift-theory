# ETAPA ESPECULATIVA TCI 2.0 - calculo preliminar, no validado
# ============================================================================
# PASO A — LA BISAGRA DEL CORE (compuerta unica, bitacora §34.D):
# ¿que orden llena el nucleo del HQV del D4-BN, y con que orientacion
# respecto del eje del tubo?
#
# Contexto: el preliminar de la batalla de la red ("core mezcla FM+ciclica
# 76/24, C3 || eje, dE=-0.0114 vs FM puro") fue REFUTADO como evidencia
# (errata #12: plateau no convergido, drift/400 subestimo ~50x). Este script
# lo rehace con el QA exigido por la REGLA NUEVA DE LA CASA (tronco §9.9):
#
#   QA1  convergencia por NORMA DE GRADIENTE (g_rms sitios libres), JAMAS
#        drift por ventana de pasos; el drift residual se mide y reporta
#        aparte y debe ser << dE entre estados.
#   QA2  test espejo: HQV (+1/2,+1/4) vs (-1/2,-1/4) con semilla conjugada
#        deben dar E identica y L invertido (quiralidad esclava del winding).
#   QA3  semillas multiples e inclinadas (7): desnuda / FM+z / FM-z /
#        ciclica C3||z / ciclica C3 a 55 grados / ciclica C3||x / ruido.
#   QA4  control de h a caja fisica fija: N=80 (h=1) vs N=120 (h=2/3),
#        misma caja 80x80 fisica; ganador y ordenamiento deben sostenerse.
#
# Fisica: seccion 2D perpendicular al tubo (eje z = eje especial del D4 de
# fondo, la geometria estandar del proyecto, §30). Funcional GL caso C
# TEXTUAL (al=-1, be=1, ga=+0.15, eps=0.05, §16) con gradiente COMPLETO
# K1 + 2K(div) (K1=K2=K3 textual de 1810.04901; el div es el termino que
# acopla la orientacion interna al eje — sin el, la bisagra no es fisica);
# corrida de contraste con K1 solo para conectar con §30.
#
# Salida clave (input directo del Paso B): pesos m_J del core convergido.
#   FM puro alineado        -> peso en {+2}          (gap a*Y+2)
#   mezcla FM+ciclica C3||z -> peso en {+2, -1}      (gap a*Y+2 + b*Y-1)
#   otra orientacion        -> peso fuera de {+2,-1} (bisagra hacia mudos)
# (espejo (-1/2,-1/4): {-2, +1})
#
# Maquinaria heredada y certificada: potencial caso C + gradiente Wirtinger
# (coulomb_del_mar.py, autotest 6e-9), F_div autotesteada, vacio D4 §16.
# ============================================================================
import numpy as np, time, sys

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(11)

E5 = np.zeros((5, 3, 3))
E5[0] = np.diag([1, -1, 0]) / np.sqrt(2)
E5[1] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / np.sqrt(2)
E5[2] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]]) / np.sqrt(2)
E5[3] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]]) / np.sqrt(2)
E5[4] = np.diag([-1, -1, 2]) / np.sqrt(6)

AL, BE, GA, EPS = -1.0, 1.0, +0.15, 0.05   # caso C (§16)
K = 1.0
PARAMS = (AL, BE, GA, EPS)

# ---------------------------------------------------------------- potencial
def V_scalar(x, al, be, ga, eps):
    A = np.einsum('a,aij->ij', x[:5], E5) + 1j * np.einsum('a,aij->ij', x[5:], E5)
    Ab = np.conj(A)
    t  = np.real(np.trace(A @ Ab))
    u  = np.trace(A @ A); ub = np.conj(u)
    q4 = t**2 - np.real(np.trace(Ab @ Ab @ A @ A))
    A2 = A @ A; Ab2 = Ab @ Ab
    s6 = (-3 * t * np.real(u * ub) + 4 * t**3
          + 6 * t * np.real(np.trace(Ab2 @ A2))
          + 12 * t * np.real(np.trace(Ab @ A @ Ab @ A))
          - 6 * np.real(ub * np.trace(Ab @ A @ A @ A))
          - 6 * np.real(u * np.trace(Ab @ Ab @ Ab @ A))
          - 12 * np.real(np.trace(Ab @ Ab @ Ab @ A @ A @ A))
          + 12 * np.real(np.trace(Ab2 @ A2 @ Ab @ A))
          + 8 * np.real(np.trace(Ab @ A @ Ab @ A @ Ab @ A)))
    return al * t + be * q4 + ga * s6 + eps * t**4

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

# autotests heredados
xt = 0.4 * rng.standard_normal((10, 6))
err = max(abs(V_sites(xt, *PARAMS)[m] - V_scalar(xt[:, m], *PARAMS)) for m in range(6))
assert err < 1e-10
gnum = np.empty((10, 6))
for a in range(10):
    xp = xt.copy(); xp[a] += 1e-6; xm = xt.copy(); xm[a] -= 1e-6
    gnum[a] = (V_sites(xp, *PARAMS) - V_sites(xm, *PARAMS)) / 2e-6
errg = np.max(np.abs(gradV_sites(xt, *PARAMS) - gnum))
assert errg < 1e-6
print(f"[autotest] potencial vectorizado {err:.1e} | gradiente Wirtinger {errg:.1e}")

# vacio D4
D = np.diag([1., -1., 0.])
def x_of_A(A):
    return np.concatenate([[np.real(np.trace(A @ E5[a])) for a in range(5)],
                           [np.imag(np.trace(A @ E5[a])) for a in range(5)]])
aa = np.linspace(0.05, 1.2, 2000)
Va = np.array([V_scalar(x_of_A(a * D), *PARAMS) for a in aa])
a0 = aa[np.argmin(Va)]
for _ in range(60):
    h_ = 1e-4
    d1 = (V_scalar(x_of_A((a0+h_)*D), *PARAMS) - V_scalar(x_of_A((a0-h_)*D), *PARAMS))/(2*h_)
    d2 = (V_scalar(x_of_A((a0+h_)*D), *PARAMS) - 2*V_scalar(x_of_A(a0*D), *PARAMS)
          + V_scalar(x_of_A((a0-h_)*D), *PARAMS))/h_**2
    a0 -= d1/d2
V0 = V_scalar(x_of_A(a0 * D), *PARAMS)
print(f"[vacio] a0 = {a0:.5f}  V0 = {V0:.6f}  (control §16: a=0.472)")

# ---------------------------------------------------- base m_J (armonicos)
sq2 = np.sqrt(2.0)
mvec = np.array([1, 1j, 0]) / sq2          # (x + i y)/sqrt2
nvec = np.array([1, -1j, 0]) / sq2         # (x - i y)/sqrt2
zvec = np.array([0, 0, 1.0])
Ym = {
    +2: np.outer(mvec, mvec),
    +1: (np.outer(mvec, zvec) + np.outer(zvec, mvec)) / sq2,
     0: np.diag([-1., -1., 2.]) / np.sqrt(6),
    -1: (np.outer(nvec, zvec) + np.outer(zvec, nvec)) / sq2,
    -2: np.outer(nvec, nvec),
}
for m_, Y_ in Ym.items():
    assert abs(np.sum(np.abs(Y_)**2) - 1) < 1e-12
    assert abs(np.trace(Y_)) < 1e-12
# ciclica C3||z = (Y+2 + sqrt2 Y-1)/sqrt3  (TrA^2=0 verificado abajo)
A_cyc_z = (Ym[+2] + sq2 * Ym[-1]) / np.sqrt(3)
assert abs(np.trace(A_cyc_z @ A_cyc_z)) < 1e-12
def rot_x(th):
    c, s = np.cos(th), np.sin(th)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
def rotar_A(A, R):
    return R @ A @ R.T
A_fm_up = Ym[+2]                            # FM con L || +z
A_fm_dn = Ym[-2]                            # FM con L || -z
A_cyc_55 = rotar_A(A_cyc_z, rot_x(np.deg2rad(55)))
A_cyc_x  = rotar_A(A_cyc_z, rot_x(np.deg2rad(90)))

def Lvec_of(A):
    """L_k = -i eps_kab (A^dag A)_ab = +Im(M_ab - M_ba); FM puro: L = +z, |L|=1"""
    M = A.conj().T @ A
    return np.array([np.imag(M[1, 2] - M[2, 1]),
                     np.imag(M[2, 0] - M[0, 2]),
                     np.imag(M[0, 1] - M[1, 0])])
def Lvec_check():
    L = Lvec_of(Ym[+2])
    assert np.allclose(L, [0, 0, 1], atol=1e-12), L
    L = Lvec_of(A_cyc_z)
    assert np.linalg.norm(L) < 1e-12, L
Lvec_check()
print("[base m_J] ortonormal; ciclica C3||z con TrA2=0 y L=0; FM: L=+z  [OK]")

# ============================================== geometria, energia, fuerzas
def setup(N, Lbox=80.0, xi=2.0):
    h = Lbox / N
    yy, xx = np.mgrid[0:N, 0:N].astype(float)
    xx = (xx + 0.5) * h; yy = (yy + 0.5) * h   # coords fisicas centradas
    cx = cy = Lbox / 2
    return {"N": N, "h": h, "xx": xx, "yy": yy, "cx": cx, "cy": cy, "xi": xi,
            "borde": max(2, int(np.ceil(3.0 / h)))}

def ansatz_hqv(G, w, v, core=None, amp_core=0.8, r_core=6.0):
    """HQV (w,v) centrado; core: matriz 3x3 a inyectar suavemente en el nucleo."""
    N, h = G["N"], G["h"]
    th = np.arctan2(G["yy"] - G["cy"], G["xx"] - G["cx"])
    r = np.hypot(G["xx"] - G["cx"], G["yy"] - G["cy"])
    phi = w * th; alp = v * th
    amp = np.tanh(np.maximum(r, 1e-9) / G["xi"])
    c0 = amp * a0 * sq2 * np.cos(2 * alp)
    c1 = amp * a0 * sq2 * np.sin(2 * alp)
    x = np.zeros((10, N, N))
    x[0] = c0 * np.cos(phi); x[5] = c0 * np.sin(phi)
    x[1] = c1 * np.cos(phi); x[6] = c1 * np.sin(phi)
    if core is not None:
        g = amp_core * a0 * np.exp(-(r / r_core)**2)
        xc = x_of_A(core)
        for a in range(10):
            x[a] += g * xc[a]
    return x

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

# autotest F_div (heredado, grilla chica)
Nt = 6
xt6 = 0.3 * rng.standard_normal((10, Nt, Nt))
gnum6 = np.zeros_like(xt6)
for a in range(10):
    for iy in range(Nt):
        for ix in range(Nt):
            xp = xt6.copy(); xp[a, iy, ix] += 1e-6
            xm = xt6.copy(); xm[a, iy, ix] -= 1e-6
            gnum6[a, iy, ix] = (E_div(xp) - E_div(xm)) / 2e-6
errd = np.max(np.abs(-F_div(xt6) - gnum6))
assert errd < 1e-6
print(f"[autotest] fuerza del div {errd:.1e}")

def energia(x, G, con_div):
    gx = x[:, :, 1:] - x[:, :, :-1]
    gy = x[:, 1:, :] - x[:, :-1, :]
    Eg = K * (np.sum(gx**2) + np.sum(gy**2))
    Ev = G["h"]**2 * np.sum(V_sites(x.reshape(10, -1), *PARAMS) - V0)
    if con_div:
        Eg += E_div(x)
    return Eg + Ev

def fuerza(x, G, con_div):
    N = G["N"]
    lap = np.zeros_like(x)
    lap[:, 1:-1, 1:-1] = (x[:, 2:, 1:-1] + x[:, :-2, 1:-1] +
                          x[:, 1:-1, 2:] + x[:, 1:-1, :-2] - 4 * x[:, 1:-1, 1:-1])
    F = 2 * K * lap - G["h"]**2 * gradV_sites(x.reshape(10, -1), *PARAMS).reshape(10, N, N)
    if con_div:
        F += F_div(x)
    return F

# ------------------------------------------ relajacion con QA por gradiente
def relajar_qa(x, G, con_div, max_pasos=60000, lr=0.02, mom=0.95,
               tol_grms=2e-7, informar=10000, tag=""):
    """Converge por NORMA DE GRADIENTE en sitios libres (regla de la casa).
    Devuelve (x, g_rms, convergio, historia)."""
    N = G["N"]; b = G["borde"]
    libre = np.ones((N, N), bool)
    libre[:b, :] = libre[-b:, :] = libre[:, :b] = libre[:, -b:] = False
    nlibre = np.sqrt(10.0 * libre.sum())
    vel = np.zeros_like(x)
    hist = []
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
                print(f"      [{tag}] paso {it+1}: E={energia(x,G,con_div):.5f} "
                      f"g_rms={g_rms:.2e} lr={lr_now:.4f}", flush=True)
            hist.append((it + 1, g_rms))
            if g_rms < tol_grms:
                break
            if g_prev < np.inf and g_rms > 0.98 * g_prev:
                stall += 1
                if stall >= 3:
                    lr_now = min(lr_now * 1.3, 0.06)   # empujar si estanca
                    stall = 0
            if not np.isfinite(g_rms):
                lr_now *= 0.5; vel[:] = 0; stall = 0
    # pulido sin momentum
    for _ in range(2000):
        F = fuerza(x, G, con_div)
        F[:, ~libre] = 0.0
        x = x + 0.5 * lr * F
    F = fuerza(x, G, con_div); F[:, ~libre] = 0.0
    g_rms = np.linalg.norm(F) / nlibre
    return x, g_rms, (g_rms < tol_grms * 3), hist

def drift_test(x, G, con_div, pasos=5000, lr=0.02, mom=0.95):
    """corre pasos extra y devuelve |dE| (debe ser << dE entre estados)"""
    E1 = energia(x, G, con_div)
    N = G["N"]; b = G["borde"]
    libre = np.ones((N, N), bool)
    libre[:b, :] = libre[-b:, :] = libre[:, :b] = libre[:, -b:] = False
    vel = np.zeros_like(x)
    for _ in range(pasos):
        F = fuerza(x, G, con_div)
        F[:, ~libre] = 0.0
        vel = mom * vel + lr * F
        x = x + vel
    return abs(energia(x, G, con_div) - E1), x

# --------------------------------------------------------- metricas del core
def medir_core(x, G, r_max=4.0):
    """invariantes y pesos m_J en el disco r_fisico < r_max (=2 xi default)"""
    N = G["N"]
    r = np.hypot(G["xx"] - G["cx"], G["yy"] - G["cy"])
    disco = r < r_max
    xc = x[:5] + 1j * x[5:]
    A = np.einsum('am,aij->mij', xc.reshape(5, -1)[:, disco.ravel()], E5)
    t = np.einsum('mij,mij->m', A, A.conj()).real
    T = t.sum()
    u = np.einsum('mij,mji->m', A, A)
    a20 = np.abs(u).sum() / max(T, 1e-30)
    dets = np.abs(np.linalg.det(A))
    dethat = (3**1.5 * dets / np.maximum(t, 1e-30)**1.5)
    dethat_w = (dethat * t).sum() / max(T, 1e-30)
    M = np.einsum('mji,mjk->mik', A.conj(), A)     # A^dag A por sitio
    L = np.stack([(M[:, 1, 2] - M[:, 2, 1]).imag,
                  (M[:, 2, 0] - M[:, 0, 2]).imag,
                  (M[:, 0, 1] - M[:, 1, 0]).imag], axis=1)
    Lsum = L.sum(axis=0) / max(T, 1e-30)
    pesos = {}
    for m_, Y_ in Ym.items():
        psi = np.einsum('ij,mij->m', Y_.conj(), A)
        pesos[m_] = float((np.abs(psi)**2).sum() / max(T, 1e-30))
    return {"t_med": T / disco.sum(), "a20": float(a20), "dethat": float(dethat_w),
            "L": Lsum, "absL": float(np.linalg.norm(Lsum)), "pesos": pesos}

def resumen(nombre, met, E, g_rms, conv):
    p = met["pesos"]
    L = met["L"]
    print(f"  {nombre:>12}: E={E:+.5f}  g_rms={g_rms:.1e} {'CONV' if conv else '**NO CONV**'}"
          f"  |  core(r<2xi): t={met['t_med']:.3f} a20={met['a20']:.3f} "
          f"det^={met['dethat']:.3f} |L|={met['absL']:.3f} Lz={L[2]:+.3f}")
    print(f"               pesos m_J: " +
          "  ".join(f"[{m_:+d}]={p[m_]:.3f}" for m_ in (+2, +1, 0, -1, -2)) +
          f"   fuera de {{+2,-1}}: {p[+1]+p[0]+p[-2]:.3f}")

# =========================================================== CAMPAÑA PASO A
CON_DIV = True     # principal: gradiente textual completo K1+2K(div)
G80 = setup(80)
print("\n" + "=" * 76)
print(f"PASO A - PRINCIPAL: N=80 h={G80['h']:.3f} caja 80x80 fisica, "
      f"gradiente K1+2K(div) TEXTUAL, HQV (+1/2,+1/4)")
print("=" * 76)

semillas = [
    ("desnuda",  None),
    ("FM+z",     A_fm_up),
    ("FM-z",     A_fm_dn),
    ("cyc-z",    A_cyc_z),
    ("cyc-55",   A_cyc_55),
    ("cyc-x",    A_cyc_x),
    ("ruido",    "ruido"),
]
t0 = time.time()
res = {}
for nombre, core in semillas:
    if core is None:
        x = ansatz_hqv(G80, 0.5, 0.25)
    elif isinstance(core, str):
        x = ansatz_hqv(G80, 0.5, 0.25)
        r = np.hypot(G80["xx"] - G80["cx"], G80["yy"] - G80["cy"])
        x += 0.15 * np.exp(-(r / 6.0)**2) * rng.standard_normal(x.shape)
    else:
        x = ansatz_hqv(G80, 0.5, 0.25, core=core)
    x, g_rms, conv, _ = relajar_qa(x, G80, CON_DIV, tag=nombre)
    E = energia(x, G80, CON_DIV)
    met = medir_core(x, G80)
    res[nombre] = (E, g_rms, conv, met, x)
    resumen(nombre, met, E, g_rms, conv)
    print(f"               [{time.time()-t0:.0f}s]", flush=True)

ganador = min(res, key=lambda n: res[n][0])
Eg = res[ganador][0]
print(f"\n  GANADOR N=80: {ganador} con E={Eg:+.5f}")
print("  dE vs ganador: " + "  ".join(f"{n}:{res[n][0]-Eg:+.5f}" for n in res))

# drift residual del ganador (QA1: debe ser << dE tipico entre estados)
dr, _ = drift_test(res[ganador][4].copy(), G80, CON_DIV)
print(f"  drift residual del ganador (5000 pasos extra): |dE| = {dr:.2e}")

# ------------------------------------------------------------- QA2: espejo
print("\n" + "=" * 76)
print("QA2 ESPEJO: HQV (-1/2,-1/4) desde el conjugado del ganador")
print("=" * 76)
xg = res[ganador][4]
x_esp = xg.copy()
x_esp[5:] *= -1          # A -> A* : espejo exacto del funcional
x_esp, g_rms_e, conv_e, _ = relajar_qa(x_esp, G80, CON_DIV, max_pasos=20000, tag="espejo")
E_esp = energia(x_esp, G80, CON_DIV)
met_e = medir_core(x_esp, G80)
resumen("espejo", met_e, E_esp, g_rms_e, conv_e)
print(f"  |E_espejo - E_ganador| = {abs(E_esp - Eg):.2e}  (debe ~0)")
print(f"  L_z ganador {res[ganador][3]['L'][2]:+.4f} vs espejo {met_e['L'][2]:+.4f} (debe invertir)")
pg, pe = res[ganador][3]["pesos"], met_e["pesos"]
print(f"  pesos: ganador [+2]={pg[+2]:.3f} [-1]={pg[-1]:.3f}  |  "
      f"espejo [-2]={pe[-2]:.3f} [+1]={pe[+1]:.3f}  (deben espejarse)")

# ------------------------------------------------- QA4: control de h (N=120)
print("\n" + "=" * 76)
print(f"QA4 CONTROL DE h: N=120 h={80/120:.3f}, misma caja fisica; ganador y top-2")
print("=" * 76)
G120 = setup(120)
orden = sorted(res, key=lambda n: res[n][0])
top = []
vistos = set()
for n in orden:                      # ganador + primer rival con otro caracter
    if not top:
        top.append(n)
    elif len(top) == 1 and abs(res[n][0] - res[top[0]][0]) > 1e-4:
        top.append(n)
    if len(top) == 2:
        break
if len(top) < 2:
    top = orden[:2]
for nombre in top:
    core = dict(semillas)[nombre]
    if core is None:
        x = ansatz_hqv(G120, 0.5, 0.25)
    elif isinstance(core, str):
        x = ansatz_hqv(G120, 0.5, 0.25)
        r = np.hypot(G120["xx"] - G120["cx"], G120["yy"] - G120["cy"])
        x += 0.15 * np.exp(-(r / 6.0)**2) * rng.standard_normal(x.shape)
    else:
        x = ansatz_hqv(G120, 0.5, 0.25, core=core)
    x, g_rms, conv, _ = relajar_qa(x, G120, CON_DIV, max_pasos=80000, tag=f"h:{nombre}")
    E = energia(x, G120, CON_DIV)
    met = medir_core(x, G120)
    resumen(f"h:{nombre}", met, E, g_rms, conv)
    print(f"               [{time.time()-t0:.0f}s]", flush=True)

# --------------------------------------------- contraste K1 solo (como §30)
print("\n" + "=" * 76)
print("CONTRASTE K1 solo (sin div, como §30): ganador y top-2 en N=80")
print("=" * 76)
for nombre in top:
    core = dict(semillas)[nombre]
    if core is None:
        x = ansatz_hqv(G80, 0.5, 0.25)
    elif isinstance(core, str):
        x = ansatz_hqv(G80, 0.5, 0.25)
        r = np.hypot(G80["xx"] - G80["cx"], G80["yy"] - G80["cy"])
        x += 0.15 * np.exp(-(r / 6.0)**2) * rng.standard_normal(x.shape)
    else:
        x = ansatz_hqv(G80, 0.5, 0.25, core=core)
    x, g_rms, conv, _ = relajar_qa(x, G80, False, tag=f"K1:{nombre}")
    E = energia(x, G80, False)
    met = medir_core(x, G80)
    resumen(f"K1:{nombre}", met, E, g_rms, conv)

print(f"\n[tiempo total {time.time()-t0:.0f}s]")
print("""
LECTURA (para el acta): si todas las semillas convergen al MISMO estado
(dE ~ 0, mismos pesos m_J), el atractor es unico — el enunciado fuerte que la
refutacion sugeria queda probado o refutado por las diferencias de energia con
drift residual medido. La composicion del core en pesos m_J es el input del
Paso B: {+2} puro = gap a*Y+2; {+2,-1} = a*Y+2 + b*Y-1 (mezcla C3||z);
peso fuera de {+2,-1} = orientacion inclinada (bisagra hacia los mudos).""")
