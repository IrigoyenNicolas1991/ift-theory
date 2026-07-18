# ETAPA ESPECULATIVA TCI 2.0 - calculo preliminar, no validado
# ============================================================================
# COULOMB DEL MAR (batalla del acople §29, parte ESTATICA -> bitacora §30):
# ¿que ley de fuerza da el mar D4-BN entre dos nudos (HQV)?
#
# Parte A — limite de London desde el funcional GL textual (1810.04901):
#   rigideces de la fase (rho_phi) y del marco (rho_alpha) para gradientes
#   en el plano perpendicular al eje especial, con y sin el termino de
#   divergencia (K2+K3); busqueda de termino cruzado; cambio de base a los
#   sectores q+/q- (windings de las componentes psi_{-+2}) y tabla de
#   interaccion de las 4 especies fundamentales de HQV.
# Parte B — relajacion GL 2D no lineal (campo completo de 10 componentes,
#   potencial caso C textual al=-1,be=1,ga=+0.15,eps=0.05; gradiente
#   ISOTROPO K1 solamente — DECLARADO) con nucleos anclados: E(d) por par
#   de especies, pendiente dE/dln(d) vs prediccion London.
# Parte C — vortice entero (w_phi=1, w_alpha=0) SIN anclar: ¿se parte en
#   dos HQV (una por sector)? ¿a que distancia queda la "molecula"?
#   (control cualitativo vs la molecula de HQVs de la literatura 3P2)
#
# Controles internos: (i) vacio D4 = minimo del potencial 10-dim (§16);
# (ii) autotest de la vectorizacion del sexto orden contra la version
# escalar de espectro_biaxial_3p2.py; (iii) limite U(1): un solo sector
# cargado reproduce el superfluido escalar con densidad a^2.
# ============================================================================
import numpy as np, time, sys

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(7)

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
    """version escalar de referencia (identica a espectro_biaxial_3p2.py)"""
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
    """x: (10, M) -> energia potencial por sitio (M,). Vectorizada."""
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
    """Gradiente ANALITICO del potencial por sitio (Wirtinger). V es real =>
    dF/dAb = conj(dF/dA); g_a = 2 Re tr(P E_a), g_{5+a} = -2 Im tr(P E_a)."""
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

# autotest vectorizacion + gradiente analitico
xt = 0.4 * rng.standard_normal((10, 6))
err = max(abs(V_sites(xt, *PARAMS)[m] - V_scalar(xt[:, m], *PARAMS)) for m in range(6))
print(f"[autotest] vectorizacion del potencial vs escalar: err max = {err:.2e}")
assert err < 1e-10
gnum = np.empty((10, 6))
for a in range(10):
    xp = xt.copy(); xp[a] += 1e-6; xm = xt.copy(); xm[a] -= 1e-6
    gnum[a] = (V_sites(xp, *PARAMS) - V_sites(xm, *PARAMS)) / 2e-6
gana = gradV_sites(xt, *PARAMS)
errg = np.max(np.abs(gana - gnum))
print(f"[autotest] gradiente analitico vs numerico: err max = {errg:.2e}")
assert errg < 1e-6

# ------------------------------------------------------- vacio D4 (caso C)
# A0 = a * diag(1,-1,0)  (clase D4-BN r=-1, eje especial = z)
D = np.diag([1., -1., 0.])
S = np.array([[0., 1., 0.], [1., 0., 0.], [0., 0., 0.]])

def x_of_A(A):
    return np.concatenate([[np.real(np.trace(A @ E5[a])) for a in range(5)],
                           [np.imag(np.trace(A @ E5[a])) for a in range(5)]])

aa = np.linspace(0.05, 1.2, 2000)
Va = np.array([V_scalar(x_of_A(a * D), *PARAMS) for a in aa])
a0 = aa[np.argmin(Va)]
for _ in range(60):  # refinamiento parabolico
    h = 1e-4
    d1 = (V_scalar(x_of_A((a0+h)*D), *PARAMS) - V_scalar(x_of_A((a0-h)*D), *PARAMS))/(2*h)
    d2 = (V_scalar(x_of_A((a0+h)*D), *PARAMS) - 2*V_scalar(x_of_A(a0*D), *PARAMS)
          + V_scalar(x_of_A((a0-h)*D), *PARAMS))/h**2
    a0 -= d1/d2
V0 = V_scalar(x_of_A(a0 * D), *PARAMS)
print(f"[vacio] a = {a0:.5f}   V0 = {V0:.6f}  (control §16: autovalores +-0.472 -> a=0.472)")

# control: minimo 10-dim desde semilla aleatoria cae a la misma energia
def find_min(x0, iters=40000, lr=0.01):
    x = x0.copy()
    for _ in range(iters):
        g = np.zeros(10)
        for a in range(10):
            dx = np.zeros(10); dx[a] = 1e-6
            g[a] = (V_scalar(x+dx, *PARAMS) - V_scalar(x-dx, *PARAMS)) / 2e-6
        if np.linalg.norm(g) < 1e-9: break
        x -= lr * g
    return x
xr = find_min(0.4 * rng.standard_normal(10))
print(f"[vacio] minimo 10-dim desde semilla aleatoria: V = {V_scalar(xr, *PARAMS):.6f} (debe = V0)")

# ============================================================ PARTE A: LONDON
print("\n" + "=" * 76)
print("PARTE A — limite de London: las monedas del mar (rigideces por canal)")
print("=" * 76)
# textura A(s) = e^{i phi} R(alpha) A0 R^T(alpha),  dA/ds = i g_phi A + g_al B
A0m = a0 * D
Bm = np.array([[0., 2*a0, 0.], [2*a0, 0., 0.], [0., 0., 0.]])  # Lz A0 + A0 Lz^T

def f_grad(e, gphi, gal, con_div):
    dA = 1j * gphi * A0m + gal * Bm
    f = K * np.sum(np.abs(dA)**2)
    if con_div:
        f += 2 * K * np.sum(np.abs(e @ dA)**2)
    return f

for con_div, tag in [(False, "solo K1 (isotropo)"), (True, "K1 + 2K (div, forma completa §14-16)")]:
    print(f"\n  --- gradiente: {tag} ---")
    for e, en in [(np.array([1., 0, 0]), "e=x"), (np.array([0., 1, 0]), "e=y"),
                  (np.array([1., 1, 0]) / np.sqrt(2), "e=45deg")]:
        kpp = f_grad(e, 1, 0, con_div)
        kaa = f_grad(e, 0, 1, con_div)
        kpa = (f_grad(e, 1, 1, con_div) - kpp - kaa) / 2
        # sectores q+- : g_chi+- = g_phi -+ ... (chi+- = phi +- 2 alpha)
        kQpp = kpp/4 + kpa/4 + kaa/16
        kQmm = kpp/4 - kpa/4 + kaa/16
        kQpm = kpp/4 - kaa/16
        print(f"  {en}:  k_phiphi={kpp:.4f}  k_alal={kaa:.4f}  k_phial={kpa:.4f}"
              f"   ||  sectores: k++={kQpp:.4f}  k--={kQmm:.4f}  k+-={kQpm:.4f}")
print(f"\n  control U(1): k_phiphi(K1 solo) = K*tr(A0*A0) = {K*2*a0**2:.4f} = 2Ka^2 [check]")
print(f"  razon rho_alpha/rho_phi (K1 solo) = {f_grad(np.eye(3)[0],0,1,False)/f_grad(np.eye(3)[0],1,0,False):.4f}"
      f"  (4 exacto <=> el marco acopla con carga 2: psi_-+2 ~ e^(i(phi-+2alpha)))")

# tabla de especies: (w_phi, w_alpha) en unidades de vuelta completa (2pi)
especies = {"(+1/2,+1/4)": (0.5, 0.25), "(+1/2,-1/4)": (0.5, -0.25),
            "(-1/2,+1/4)": (-0.5, 0.25), "(-1/2,-1/4)": (-0.5, -0.25)}
kpp = f_grad(np.array([1., 0, 0]), 1, 0, False)
kaa = f_grad(np.array([1., 0, 0]), 0, 1, False)
rphi, ral = 2 * kpp, 2 * kaa
print("\n  Tabla London E_int/L = 2pi [rho_phi w1w2 + rho_al v1v2] ln(R/d)  (K1 solo):")
print("  (coef > 0 = repulsion; en unidades de K a^2)")
nombres = list(especies)
print("            " + "  ".join(f"{n:>12}" for n in nombres))
for n1 in nombres:
    w1, v1 = especies[n1]
    fila = []
    for n2 in nombres:
        w2, v2 = especies[n2]
        lam = 2 * np.pi * (rphi * w1 * w2 + ral * v1 * v2) / (K * a0**2)
        fila.append(f"{lam:>12.4f}")
    print(f"  {n1:>10}" + "  ".join(fila))
print(f"  prediccion pendiente |dE/dln d| pares cargados = 4 pi K a^2 = {4*np.pi*K*a0**2:.4f}")

# ===================================================== PARTE B: RELAJACION 2D
print("\n" + "=" * 76)
print("PARTE B — relajacion GL 2D no lineal: E(d) por par de especies")
print("=" * 76)
N = 120
BORDE = 3          # ancho del marco congelado
RPIN = 2.5         # radio de anclaje de cada nucleo
XI = 2.0

yy, xx = np.mgrid[0:N, 0:N].astype(float)

def ansatz(vortices):
    """vortices: lista de (cx, cy, w_phi, w_alpha). Devuelve x (10, N, N)."""
    phi = np.zeros((N, N)); alp = np.zeros((N, N)); amp = np.ones((N, N))
    for (cx, cy, w, v) in vortices:
        th = np.arctan2(yy - cy, xx - cx)
        r = np.hypot(xx - cx, yy - cy)
        phi += w * th; alp += v * th
        amp *= np.tanh(np.maximum(r, 1e-9) / XI)
    # A = amp * a0 e^{i phi} (cos 2alpha D + sin 2alpha S); D=sqrt2 E0, S=sqrt2 E1
    c0 = amp * a0 * np.sqrt(2) * np.cos(2 * alp)
    c1 = amp * a0 * np.sqrt(2) * np.sin(2 * alp)
    x = np.zeros((10, N, N))
    x[0] = c0 * np.cos(phi); x[5] = c0 * np.sin(phi)
    x[1] = c1 * np.cos(phi); x[6] = c1 * np.sin(phi)
    return x

def energia(x):
    gx = x[:, :, 1:] - x[:, :, :-1]
    gy = x[:, 1:, :] - x[:, :-1, :]
    Eg = K * (np.sum(gx**2) + np.sum(gy**2))
    Ev = np.sum(V_sites(x.reshape(10, -1), *PARAMS) - V0)
    return Eg + Ev

def relajar(x, libre, pasos, lr=0.04, mom=0.9, informar=0, rastrear=False, tol=2e-3):
    """libre: mascara (N,N) True donde el campo evoluciona. Corta cuando la energia
    deja de bajar (|dE| < tol entre chequeos cada 200 pasos), salvo rastrear=True."""
    vel = np.zeros_like(x)
    traza = []
    E_prev = None
    for it in range(pasos):
        lap = np.zeros_like(x)
        lap[:, 1:-1, 1:-1] = (x[:, 2:, 1:-1] + x[:, :-2, 1:-1] +
                              x[:, 1:-1, 2:] + x[:, 1:-1, :-2] - 4 * x[:, 1:-1, 1:-1])
        gV = gradV_sites(x.reshape(10, -1), *PARAMS).reshape(10, N, N)
        F = 2 * K * lap - gV
        vel = mom * vel + lr * F
        vel[:, ~libre] = 0.0
        x = x + vel
        if informar and (it + 1) % informar == 0:
            print(f"      paso {it+1}: E = {energia(x):.4f}", flush=True)
        if rastrear and (it + 1) % 400 == 0:
            t = np.einsum('am,am->m', x.reshape(10, -1), x.reshape(10, -1)).reshape(N, N)
            traza.append(nucleos(t))
        if not rastrear and (it + 1) % 200 == 0:
            E_now = energia(x)
            if E_prev is not None and abs(E_prev - E_now) < tol:
                break
            E_prev = E_now
    return x, traza

def nucleos(t):
    """posiciones de los 2 minimos locales mas profundos de t (lejos del borde)"""
    inner = t[8:-8, 8:-8]
    idx = np.argsort(inner, axis=None)[:400]
    ys, xs = np.unravel_index(idx, inner.shape)
    pts = np.stack([xs + 8, ys + 8], axis=1).astype(float)
    # clustering golpeado: primer punto = nucleo 1; el mas lejano a >6 = nucleo 2
    p1 = pts[0]
    lej = pts[np.hypot(*(pts - p1).T) > 6]
    p2 = lej[0] if len(lej) else p1
    m1 = pts[np.hypot(*(pts - p1).T) < 6].mean(axis=0)
    m2 = pts[np.hypot(*(pts - p2).T) < 6].mean(axis=0) if len(lej) else m1
    return m1, m2, float(np.hypot(*(m1 - m2)))

pares = [("mismo-mismo  (q+ q+)", (0.5, 0.25), (0.5, 0.25)),
         ("neutro-A     (q+ q-)", (0.5, 0.25), (0.5, -0.25)),
         ("neutro-B     (q+ -q-)", (0.5, 0.25), (-0.5, 0.25)),
         ("anti         (q+ -q+)", (0.5, 0.25), (-0.5, -0.25))]
dists = [12, 18, 26]
PASOS = 4000   # con corte por convergencia (tol)

resultados = {}
t_ini = time.time()
for (nombre, s1, s2) in pares:
    Es = []
    for d in dists:
        c1 = (N/2 - d/2, N/2); c2 = (N/2 + d/2, N/2)
        vort = [(c1[0], c1[1], *s1), (c2[0], c2[1], *s2)]
        x = ansatz(vort)
        libre = np.ones((N, N), bool)
        libre[:BORDE, :] = libre[-BORDE:, :] = libre[:, :BORDE] = libre[:, -BORDE:] = False
        for (cx, cy, _, _) in vort:
            libre[np.hypot(xx - cx, yy - cy) <= RPIN] = False
        x, _ = relajar(x, libre, PASOS)
        Ei = energia(x)
        Es.append(Ei)
        print(f"  {nombre}  d={d:2d}: E = {Ei:.4f}   [{time.time()-t_ini:.0f}s]", flush=True)
    lnd = np.log(dists)
    pend = np.polyfit(lnd, Es, 1)[0]
    resultados[nombre] = (Es, pend)
    print(f"  {nombre}  ->  dE/dln(d) = {pend:+.4f}")

print("\n  RESUMEN B (prediccion London K1: cargados -+{:.3f}, neutros 0):".format(4*np.pi*K*a0**2))
for nombre, (Es, pend) in resultados.items():
    print(f"    {nombre}: pendiente ajustada {pend:+.4f}")

# ===================================================== PARTE C: LA MOLECULA
print("\n" + "=" * 76)
print("PARTE C — vortice entero (1,0) sin anclar: ¿se parte en dos HQV?")
print("=" * 76)
x = ansatz([(N/2, N/2, 1.0, 0.0)])
x += 0.01 * rng.standard_normal(x.shape)   # semilla de la inestabilidad
libre = np.ones((N, N), bool)
libre[:BORDE, :] = libre[-BORDE:, :] = libre[:, :BORDE] = libre[:, -BORDE:] = False
E_ini = energia(x)
x, traza = relajar(x, libre, 6000, rastrear=True, informar=1500)
E_fin = energia(x)
print(f"  E inicial = {E_ini:.4f}  ->  E final = {E_fin:.4f}")
for i, (m1, m2, dd) in enumerate(traza):
    print(f"  paso {(i+1)*400:5d}: nucleos en {m1} y {m2}   separacion = {dd:.2f}")
print(f"\n[tiempo total: {time.time()-t_ini:.0f}s]")
