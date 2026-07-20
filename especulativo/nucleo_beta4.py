# ETAPA ESPECULATIVA TCI 2.0 - calculo preliminar, no validado
# ============================================================================
# EL NUCLEO: puede el mar contar hasta 4?
# ----------------------------------------------------------------------------
# TCI 1.0 calibro beta=4 (eclipse 1919): c_s^2(phi) = c^2 (1 - 4 phi), con la
# no linealidad SOLO en el termino cinetico temporal (Mercurio, sigma=0).
# TCI 2.0 dice que el mar es un condensado J=2 (3P2, fase D4-BN). Un
# condensado a potencial quimico mu tiene EOS DERIVABLE, no calibrable:
# este script le pregunta al mar cuanto vale beta.
#
# CONVENCION DE SIGNO (unica, en todo el script):
#     beta_M := - d ln v_M^2 / d phi ,  phi = deficit fraccional del fondo
#     beta > 0  <=> la vacancia FRENA el modo <=> refraccion HACIA la masa
#     TCI 1.0 / observacion exigen beta_luz = +4; GW170817 (Shapiro GW=EM)
#     lo exige tambien para los TT del bulk.
# Parametrizacion (I) on-shell: phi = -delta ln rho  => beta = +d ln v^2/d ln rho
# Parametrizacion (II) vacancia a mu fijo: phi = 1-s^2 => beta = -Dln v^2/Dphi
#
# METODO NUMERICO: v^2 por PENDIENTE de omega^2 entre dos k (elimina el
# offset m^2: ruido del Hessiano a k chico en (I); tachion real del fondo
# off-shell en (II) - en ambos casos el offset cancela exacto en la pendiente).
#
# CADENA DE VERIFICACION:
#   [C1] juguete U(1): pencil vs formula analitica exacta
#        c_s^2 = t0 V''/(t0 V'' + 2 mu^2), y beta analitico exacto
#   [C2] mu=0 del funcional 3P2 caso C: clasificacion 2TT+2V sobre el eje
#        (velocidades salvo factor global de convencion, declarado)
#   [C3] estabilidad de la pendiente entre dos ventanas de k distintas
#
# Dinamica de 2do orden DECLARADA (como toda la campana). c=1, K=1.
# Python: usar el 3.14 (el del PATH puede no tener numpy).
# ============================================================================
import numpy as np

np.set_printoptions(precision=4, suppress=True)

# ---------------------------------------------------------------- base J=2
E5 = np.zeros((5, 3, 3))
E5[0] = np.diag([1, -1, 0]) / np.sqrt(2)
E5[1] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / np.sqrt(2)
E5[2] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]]) / np.sqrt(2)
E5[3] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]]) / np.sqrt(2)
E5[4] = np.diag([-1, -1, 2]) / np.sqrt(6)

def Amat(x):
    return np.einsum('a,aij->ij', x[:5], E5) + 1j * np.einsum('a,aij->ij', x[5:], E5)

def V3p2(x, al, be, ga, eps):
    A = Amat(x); Ab = np.conj(A)
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

# --------------------------------------------- maquinaria generica (dim n)
def num_grad(f, x, h=1e-6):
    g = np.zeros(len(x))
    for a in range(len(x)):
        d = np.zeros(len(x)); d[a] = h
        g[a] = (f(x + d) - f(x - d)) / (2 * h)
    return g

def num_hess(f, x, h=1e-4):
    n = len(x); H = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            di = np.zeros(n); di[i] = h
            dj = np.zeros(n); dj[j] = h
            H[i, j] = (f(x+di+dj) - f(x+di-dj) - f(x-di+dj) + f(x-di-dj)) / (4*h*h)
            H[j, i] = H[i, j]
    return H

def minimize(f, x0, iters=40000, lr=0.008, tol=1e-11):
    x = x0.astype(float).copy()
    for _ in range(iters):
        g = num_grad(f, x)
        if np.linalg.norm(g) < tol:
            break
        x -= lr * g
        if np.linalg.norm(x) > 50:
            raise RuntimeError("runaway")
    return x

# Lagrangiano de fluctuaciones (fondo x_bg, quimico mu):
#   L2 = |ydot|^2 + 2 mu (J y)^T ydot - y^T Ghat(k) y - (1/2) y^T (H_V - 2mu^2) y
# EOM => pencil:  (-w^2 I - 2 i mu w J + W(k)) u = 0,
#   W(k) = Ghat(k) + (1/2) H_V(x_bg) - mu^2 I
# companion 2n x 2n:  w z = [[0, I], [W, -2 i mu J]] z
def pencil_modes(W, J, mu):
    n = W.shape[0]
    C = np.zeros((2*n, 2*n), dtype=complex)
    C[:n, n:] = np.eye(n)
    C[n:, :n] = W
    C[n:, n:] = -2j * mu * J
    w, Z = np.linalg.eig(C)
    out = []
    for i in range(len(w)):
        if w[i].real > 1e-9 and abs(w[i].imag) < 1e-3 * max(1.0, abs(w[i].real)):
            out.append((w[i].real, Z[:n, i]))
    out.sort(key=lambda p: p[0])
    return out

# ============================================================================
# [C1] CONTROL: juguete U(1) — escalar complejo, V = a t + (g/2) t^2
# ============================================================================
print("=" * 78)
print("[C1] CONTROL U(1): pendiente de omega^2 vs formula analitica")
a_toy, g_toy = -1.0, 1.0
J2 = np.array([[0., -1.], [1., 0.]])
K1c, K2c = 0.01, 0.02
ok_all = True
for mu in [0.3, 0.7, 1.2]:
    t0 = (mu**2 - a_toy) / g_toy
    cs2_ana = t0 * g_toy / (t0 * g_toy + 2 * mu**2)
    Vt = lambda x: a_toy * (x @ x) + 0.5 * g_toy * (x @ x)**2
    x0 = minimize(lambda x: Vt(x) - mu**2 * (x @ x), np.array([1.0, 0.1]))
    H = num_hess(Vt, x0)
    w2 = []
    for k in (K1c, K2c):
        W = k**2 * np.eye(2) + 0.5 * H - mu**2 * np.eye(2)
        pm = pencil_modes(W, J2, mu)
        w2.append(pm[0][0]**2)
    cs2_num = (w2[1] - w2[0]) / (K2c**2 - K1c**2)
    match = abs(cs2_num - cs2_ana) / cs2_ana < 2e-3
    ok_all = ok_all and match
    print(f"  mu={mu}: t0={t0:.3f}  c_s^2 ana={cs2_ana:.5f}  "
          f"pendiente={cs2_num:.5f}  match={'OK' if match else 'FALLA'}")
print(f"  CONTROL C1: {'PASA' if ok_all else 'FALLA'}")

# beta analitico exacto del juguete, rama sombrero mexicano (a<0):
#   c_s^2=(u-a)/(3u-a), rho=2 mu t0  =>  d ln c_s^2/d ln rho = 4 a u/(3u-a)^2
print("  beta analitico del juguete (a<0), beta := +d ln c_s^2/d ln rho:")
for mu in [0.3, 0.7, 1.2]:
    u = mu**2
    beta = 4 * a_toy * u / (3 * u - a_toy)**2
    print(f"    mu={mu}:  beta = {beta:+.4f}   "
          f"({'signo CORRECTO' if beta > 0 else 'signo CONTRARIO a TCI'})")

# ============================================================================
# funcional 3P2 caso C (gamma>0, D4-BN) a mu finito
# ============================================================================
AL, BE, GA, EPS = -1.0, 1.0, +0.15, 0.05
K = 1.0
params = (AL, BE, GA, EPS)
Vfull = lambda x: V3p2(x, *params)
J10 = np.zeros((10, 10))
J10[:5, 5:] = -np.eye(5)
J10[5:, :5] = np.eye(5)

def Ghat(k):
    kE = np.einsum('i,aij->aj', k, E5)
    G5 = K * (k @ k) * np.eye(5) + 2 * K * np.einsum('aj,bj->ab', kE, kE)
    G = np.zeros((10, 10))
    G[:5, :5] = G5; G[5:, 5:] = G5
    return G

def helicity(vec, k):
    khat = k / np.linalg.norm(k)
    B = Amat(vec.astype(complex))
    P = np.eye(3) - np.outer(khat, khat)
    BTT = P @ B @ P - 0.5 * P * np.trace(P @ B @ P)
    Bv = P @ B @ khat
    n2 = np.sum(np.abs(BTT)**2); n1 = 2 * np.sum(np.abs(Bv)**2)
    tot = np.sum(np.abs(B)**2)
    return n2 / tot, n1 / tot, max(0.0, 1 - n2/tot - n1/tot)

def gapless_v2(x_bg, mu, kdir, k1, k2, nmodes=4, thr=0.75):
    """v^2 de los nmodes modos mas bajos por pendiente de omega^2 entre k1,k2.
    Clasifica helicidad en k2. Devuelve lista (clase, v2, h2)."""
    H = num_hess(Vfull, x_bg)
    res = {}
    for k in (k1, k2):
        kv = k * kdir
        W = Ghat(kv) + 0.5 * H - mu**2 * np.eye(10)
        pm = pencil_modes(W, J10, mu)
        res[k] = pm[:nmodes]
    out = []
    for j in range(min(len(res[k1]), len(res[k2]))):
        w2a, w2b = res[k1][j][0]**2, res[k2][j][0]**2
        v2 = (w2b - w2a) / (k2**2 - k1**2)
        h2, h1, h0 = helicity(res[k2][j][1], k2 * kdir)
        cls = "TT" if h2 > thr else ("V" if h1 > thr else
              ("S" if h0 > thr else "mix"))
        out.append((cls, v2, h2))
    return out

def r_of_state(A0):
    ev = np.sort(np.real(np.linalg.eigvals(
        A0 * np.exp(-1j * np.angle(np.trace(A0 @ A0)) / 2))))
    mx = ev[2]
    return ev[0] / mx if abs(mx) > 1e-9 else np.nan

def background(mu, x_start):
    return minimize(lambda x: Vfull(x) - mu**2 * (x @ x), x_start)

ez = np.array([0., 0., 1.])

print()
print("=" * 78)
print("[C2] CONTROL mu=0: clasificacion del espectro caso C sobre el eje")
rng = np.random.default_rng(7)
x00 = minimize(Vfull, np.concatenate([np.array([0.9, 0, 0, 0, 0.]),
                                      np.zeros(5)]) + 0.01 * rng.standard_normal(10))
print(f"  r del fondo: {r_of_state(Amat(x00)):.3f} (D4-BN si -1)   "
      f"t0 = {x00 @ x00:.4f}")
KA, KB = 0.01, 0.02
cl0 = gapless_v2(x00, 0.0, ez, KA, KB)
for c, v2, h2 in cl0:
    print(f"    {c}  v={np.sqrt(max(v2,0)):.4f}  (h2={h2:.2f})")
print("  esperado: TT TT V V (salvo factor global de convencion)")
# [C3] estabilidad de pendiente en otra ventana
cl0b = gapless_v2(x00, 0.0, ez, 0.02, 0.04)
drift = max(abs(b[1] - a[1]) / a[1] for a, b in zip(cl0, cl0b))
print(f"  [C3] drift de v^2 entre ventanas (0.01,0.02) y (0.02,0.04): "
      f"{drift*100:.2f}%  {'OK' if drift < 0.02 else 'REVISAR'}")

# ============================================================================
# (I) ON-SHELL: beta variando mu.  beta = +d ln v^2 / d ln rho
# ============================================================================
print()
print("=" * 78)
print("(I) ON-SHELL (fondo en su minimo a cada mu). beta = +d ln v^2/d ln rho")
mus = [0.15, 0.25, 0.40, 0.60, 0.90]
rows = []
x_prev = x00
for mu in mus:
    xb = background(mu, x_prev); x_prev = xb
    t0 = xb @ xb
    rho = 2 * mu * t0
    cl = gapless_v2(xb, mu, ez, KA, KB)
    rows.append((mu, t0, rho, cl))
    tag = "  ".join(f"{c}(v={np.sqrt(max(v2,0)):.4f})" for c, v2, _ in cl)
    print(f"  mu={mu:.2f}  t0={t0:.4f}  rho={rho:.4f}  "
          f"r={r_of_state(Amat(xb)):.3f}   {tag}")

print()
print("  beta on-shell por modo (posicion j en el espectro bajo):")
for i in range(len(rows) - 1):
    mu1, t1, r1, cl1 = rows[i]
    mu2, t2, r2, cl2 = rows[i + 1]
    line = []
    for j in range(min(len(cl1), len(cl2))):
        c1, v21, _ = cl1[j]; c2, v22, _ = cl2[j]
        b = (np.log(v22) - np.log(v21)) / (np.log(r2) - np.log(r1))
        bt = (np.log(v22) - np.log(v21)) / (np.log(t2) - np.log(t1))
        line.append(f"{c1}{j}: {b:+.3f} (vs t0: {bt:+.3f})")
    print(f"    mu {mu1:.2f}->{mu2:.2f}: " + "   ".join(line))
print("  (beta>0 = signo correcto; TCI exige +4)")

# ============================================================================
# [C4] LA LEY Y EL SESGO DE VENTANA (toy U(1), todo cerrado analiticamente):
#   dispersion exacta del fonon off-shell:  W(K) = K + Y-(K),  K = k^2,
#     Y-(K) = [B - sqrt(B^2 + 4(eps*delta + 4u K))]/2,
#     eps = mu^2 - V'(t) = g t0 phi,  delta = 2tV'' - eps,  B = delta+4u-eps
#   => pendiente a K->0:  c^2 = 1 - 4u/B   =>   LEY:  beta(k->0) = 2(1-c^2)
#   PERO la pendiente medida en ventana K1..K2 arrastra el termino cruzado
#   8u*eps*delta*K/B^3 del radical (prop. a phi Y a K: NO cancela) => la
#   medicion en ventana SUBESTIMA beta. Control: numerico vs formula cerrada
#   EN LA MISMA VENTANA (valida maquinaria + sesgo a la vez).
# ============================================================================
print()
print("=" * 78)
print("[C4] toy U(1): beta numerico vs formula cerrada (misma ventana) y ley k->0")
KA2, KB2 = 0.15, 0.25
def toy_slope_ana(mu, phi, k1, k2):
    t0 = (mu**2 - a_toy) / g_toy
    u = mu**2
    eps = g_toy * t0 * phi
    t = t0 * (1 - phi)
    delta = 2 * t * g_toy - eps
    B = delta + 4 * u - eps
    def W(K):
        return K + (B - np.sqrt(B**2 + 4 * (eps * delta + 4 * u * K))) / 2
    return (W(k2**2) - W(k1**2)) / (k2**2 - k1**2)
for mu in [0.3, 0.7, 1.2]:
    Vt = lambda x: a_toy * (x @ x) + 0.5 * g_toy * (x @ x)**2
    x0t = minimize(lambda x: Vt(x) - mu**2 * (x @ x), np.array([1.0, 0.1]))
    def v2_toy(s):
        w2 = []
        Hs = num_hess(Vt, s * x0t)
        for k in (KA2, KB2):
            W = k**2 * np.eye(2) + 0.5 * Hs - mu**2 * np.eye(2)
            pm = pencil_modes(W, J2, mu)
            w2.append(pm[0][0]**2)
        return (w2[1] - w2[0]) / (KB2**2 - KA2**2)
    phi = 1 - 0.9975**2
    b_num = -(np.log(v2_toy(0.9975)) - np.log(v2_toy(1.0))) / phi
    b_ana_win = -(np.log(toy_slope_ana(mu, phi, KA2, KB2)) -
                  np.log(toy_slope_ana(mu, 0.0, KA2, KB2))) / phi
    c2 = toy_slope_ana(mu, 0.0, 1e-6, 2e-6)
    b_ley = 2 * (1 - c2)
    ok = abs(b_num - b_ana_win) < 0.03 * max(abs(b_ana_win), 0.05)
    print(f"  mu={mu}: beta_num(ventana)={b_num:+.4f}  "
          f"cerrada(ventana)={b_ana_win:+.4f} [{'OK' if ok else 'FALLA'}]  "
          f"LEY k->0 = 2(1-c^2) = {b_ley:+.4f}")
print("  (la ventana subestima; la ley k->0 es la fisica. El C4 de la corrida")
print("   anterior fallaba por este sesgo: errata propia, cazada y explicada.)")

# ============================================================================
# (II) VACANCIA A MU FIJO: fondo s*x0, phi = 1-s^2. beta = -Dln v^2/Dphi
# ventana de k alta (0.15, 0.25): el m^2 tachionico del fondo off-shell
# cancela exacto en la pendiente; la contaminacion por curvatura de mezcla
# se cancela al comparar s con la MISMA ventana. phi chico (<=0.01) para
# que el tachion no alcance la ventana (el s=0.99 de la corrida anterior
# la alcanzaba y contaminaba: descartado, declarado).
# ============================================================================
print()
print("=" * 78)
print("(II) VACANCIA A MU FIJO (fondo s*x0), DOS ventanas + extrapolacion k->0")
print("     (el sesgo de ventana [C4] es lineal en k1^2+k2^2: se extrapola)")
svals = [1.0, 0.9975]
VENTANAS = [(0.10, 0.20), (0.20, 0.30)]
phi = 1 - svals[-1]**2
for mu_star in [0.25, 0.60, 0.90, 1.20]:
    xb = background(mu_star, x00)
    print(f"  --- mu = {mu_star} (t0 = {xb @ xb:.4f}, "
          f"r = {r_of_state(Amat(xb)):.3f}) ---")
    betas = {}   # (ventana_idx) -> lista por modo (clase, beta, v2_eq)
    for wi, (ka, kb) in enumerate(VENTANAS):
        cl_eq = gapless_v2(xb, mu_star, ez, ka, kb)
        cl_s = gapless_v2(svals[-1] * xb, mu_star, ez, ka, kb)
        bs = []
        for j in range(min(len(cl_eq), len(cl_s))):
            c1, v21, _ = cl_eq[j]
            c2, v22, _ = cl_s[j]
            if v21 <= 0 or v22 <= 0:
                bs.append((c1, np.nan, v21))
                continue
            bs.append((c1, -(np.log(v22) - np.log(v21)) / phi, v21))
        betas[wi] = bs
    S1 = VENTANAS[0][0]**2 + VENTANAS[0][1]**2
    S2 = VENTANAS[1][0]**2 + VENTANAS[1][1]**2
    for j in range(min(len(betas[0]), len(betas[1]))):
        c, b1, v2eq = betas[0][j]
        _, b2, _ = betas[1][j]
        if np.isnan(b1) or np.isnan(b2):
            print(f"    {c}{j}: (modo perdido en alguna ventana)")
            continue
        b0 = b1 - S1 * (b2 - b1) / (S2 - S1)
        ley = 2 * (1 - v2eq)
        print(f"    {c}{j}: v_eq={np.sqrt(max(v2eq,0)):.4f}  "
              f"beta(W1)={b1:+.3f}  beta(W2)={b2:+.3f}  "
              f"beta(k->0)={b0:+.3f}   ley 2(1-v^2)={ley:+.3f}")
print()
print("  (beta>0 = la vacancia frena el modo = refraccion hacia la masa;")
print("   TCI 1.0 / GW-Shapiro exigen beta_TT = +4. La ley beta=2(1-v^2)")
print("   implica beta_TT<2 SIEMPRE y beta_TT->0 cuando v_TT->c_cinetica:")
print("   velocidad GW correcta y Shapiro GW correcto incompatibles en la")
print("   clase GL minima con cinetica canonica.)")
