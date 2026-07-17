# ETAPA ESPECULATIVA TCI 2.0 - calculo preliminar, no validado (backup autorizado 2026-07-17)
# ============================================================================
# PRIMER CALCULO TCI 2.0 (version minima): espectro de un condensado J=2 REAL
# ----------------------------------------------------------------------------
# Modelo: campo B_ij(x,t) = matriz 3x3 real simetrica sin traza (5 componentes),
# lagrangiano L = chi Tr(dB/dt)^2 - c1 Tr(dB_i dB_i) - c2 (d_i B_ij)(d_k B_kj) - V(B)
# V(B) = a TrB^2 + b TrB^3 + g (TrB^2)^2 + d (TrB^3)^2
#   - b<0, d=0  -> minimo UNIAXIAL  (control: 2 angulones, Bedaque-Nicholson)
#   - b=0, d>0  -> minimo BIAXIAL espontaneo (TrB^3=0), sin campo externo
#   - b=0, d=0  -> punto SO(5) accidental (vacio = esfera S^4 en R^5)
# El termino c2 es EL LOCK ESPACIAL: acopla el indice interno con la direccion
# de propagacion (es el unico termino que distingue helicidades).
# NOTA IMPORTANTE declarada: el orden real de 3P2 es COMPLEJO; esta es la
# version minima real (fases nematicas reales). Segundo orden en tiempo
# (invariante bajo inversion temporal, sin termino de Berry) - declarado.
# ============================================================================
import numpy as np

np.set_printoptions(precision=6, suppress=True)
rng = np.random.default_rng(7)

# ---------- base ortonormal de matrices simetricas sin traza: Tr(Ea Eb)=delta
E = np.zeros((5, 3, 3))
E[0] = np.diag([1, -1, 0]) / np.sqrt(2)                    # (x2-y2)/sqrt2   m=+-2 (eje z)
E[1] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / np.sqrt(2)  # xy        m=+-2
E[2] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]]) / np.sqrt(2)  # xz        m=+-1
E[3] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]]) / np.sqrt(2)  # yz        m=+-1
E[4] = np.diag([-1, -1, 2]) / np.sqrt(6)                   # (2z2-x2-y2)     m=0

def Bmat(phi):
    return np.einsum('a,aij->ij', phi, E)

# ---------- potencial y derivadas numericas
def V(phi, a, b, g, d):
    B = Bmat(phi)
    t2 = np.trace(B @ B)
    t3 = np.trace(B @ B @ B)
    return a * t2 + b * t3 + g * t2**2 + d * t3**2

def grad(phi, *p, h=1e-6):
    return np.array([(V(phi + h*np.eye(5)[a], *p) - V(phi - h*np.eye(5)[a], *p)) / (2*h)
                     for a in range(5)])

def hess(phi, *p, h=1e-4):
    H = np.zeros((5, 5))
    for i in range(5):
        for j in range(5):
            pp = phi.copy(); pp[i] += h; pp[j] += h; f1 = V(pp, *p)
            pp = phi.copy(); pp[i] += h; pp[j] -= h; f2 = V(pp, *p)
            pp = phi.copy(); pp[i] -= h; pp[j] += h; f3 = V(pp, *p)
            pp = phi.copy(); pp[i] -= h; pp[j] -= h; f4 = V(pp, *p)
            H[i, j] = (f1 - f2 - f3 + f4) / (4*h*h)
    return 0.5 * (H + H.T)

# ---------- generadores de rotacion actuando sobre B: delta_B = [L, B]
L = np.zeros((3, 3, 3))
L[0] = np.array([[0,0,0],[0,0,-1],[0,1,0]])   # Lx
L[1] = np.array([[0,0,1],[0,0,0],[-1,0,0]])   # Ly
L[2] = np.array([[0,-1,0],[1,0,0],[0,0,0]])   # Lz

def rot_dirs(phi):
    """direcciones rotacionales en el espacio de los 5 phi (pueden ser < 3 si hay estabilizador)"""
    B = Bmat(phi)
    dirs = []
    for i in range(3):
        dB = L[i] @ B - B @ L[i]
        v = np.array([np.trace(dB @ E[a]) for a in range(5)])
        if np.linalg.norm(v) > 1e-8:
            dirs.append(v / np.linalg.norm(v))
    return np.array(dirs)

# ---------- forma cuadratica de gradiente K(k):  c1 k^2 delta_ab + c2 (k.Ea)_j (k.Eb)_j
def Kgrad(k, c1, c2):
    kE = np.einsum('i,aij->aj', k, E)           # (k_i Ea_ij) -> vector j por cada a
    return c1 * (k @ k) * np.eye(5) + c2 * np.einsum('aj,bj->ab', kE, kE)

# ---------- contenido de helicidad respecto de k: proyecciones TT / vector / escalar
def helicity_content(vec, k):
    khat = k / np.linalg.norm(k)
    B = Bmat(vec)
    P = np.eye(3) - np.outer(khat, khat)
    BTT = P @ B @ P - 0.5 * P * np.trace(P @ B @ P)      # transverse-traceless (helicidad +-2)
    Bvec = P @ B @ khat                                   # helicidad +-1
    n2 = np.sum(BTT**2); n1 = 2*np.sum(Bvec**2)
    n0 = np.sum(B**2) - n2 - n1                           # helicidad 0 (2 combinaciones)
    tot = np.sum(B**2)
    return n2/tot, n1/tot, n0/tot

# ---------- espectro: omega^2 = autovalores de (M + K(k)), chi=1
def spectrum(phi0, params, k, c1, c2):
    M = hess(phi0, *params)
    K = Kgrad(k, c1, c2)
    w2, U = np.linalg.eigh(M + K)
    return w2, U

def analyse(tag, phi0, params, c1, c2):
    print("=" * 78)
    print(tag)
    g = grad(phi0, *params)
    print(f"  |grad V| en el minimo = {np.linalg.norm(g):.2e}  (control: ~0)")
    M = hess(phi0, *params)
    wM = np.sort(np.linalg.eigvalsh(M))
    print(f"  autovalores de la masa M: {wM}")
    R = rot_dirs(phi0)
    rank = np.linalg.matrix_rank(R, tol=1e-6) if len(R) else 0
    print(f"  # rotaciones rotas (rango del espacio rotacional) = {rank}")
    for v in R:
        print(f"    control Goldstone |M v| = {np.linalg.norm(M @ v):.2e} (debe ser ~0)")
    nzero = np.sum(np.abs(wM) < 1e-6)
    print(f"  modos sin masa en k=0: {nzero}")
    # dispersion y helicidad en varias direcciones
    for kdir, name in [(np.array([0,0,1.]), "k||z"), (np.array([1,0,0.]), "k||x"),
                       (np.array([0,1,0.]), "k||y"),
                       (np.array([1,1,1.])/np.sqrt(3), "k||(111)")]:
        kk = 1e-3 * kdir   # k chico: separar gapless de masivos
        w2, U = spectrum(phi0, params, kk, c1, c2)
        print(f"  --- {name}  (k={np.linalg.norm(kk):.0e})")
        for m in range(5):
            if w2[m] < (10 * 1e-3)**2:   # solo modos gapless (omega ~ v k)
                v = np.sqrt(max(w2[m], 0)) / np.linalg.norm(kk)
                h2, h1, h0 = helicity_content(U[:, m], kk)
                print(f"    modo gapless: v = {v:.4f}   helicidad: +-2:{h2:.2f}  +-1:{h1:.2f}  0:{h0:.2f}")

# ---------- minimizador propio (sin scipy): descenso por gradiente con paso adaptativo
def find_min(phi0, params, iters=20000, lr=0.02):
    phi = phi0.astype(float).copy()
    for _ in range(iters):
        gv = grad(phi, *params)
        n = np.linalg.norm(gv)
        if n < 1e-10:
            break
        phi -= lr * gv
    return phi

# ============================ CASOS ============================
c1, c2 = 1.0, 0.8   # c2 != 0 = lock espacial encendido

# ---- CONTROL 1: UNIAXIAL (b<0 selecciona uniaxial; esperado: 2 angulones +-1)
a, b, g, d = -1.0, -0.5, 1.0, 0.0
phi_uni = find_min(np.eye(5)[4] * 0.8 + 0.01 * rng.standard_normal(5), (a, b, g, d))
print("estado uniaxial: autovalores de B0:", np.sort(np.linalg.eigvalsh(Bmat(phi_uni))))
analyse("CONTROL UNIAXIAL (esperado: 2 gapless, helicidad +-1 dominante segun k)",
        phi_uni, (a, b, g, d), c1, c2)

# ---- CASO PRINCIPAL: BIAXIAL espontaneo (b=0, d>0)
a, b, g, d = -1.0, 0.0, 1.0, 2.0
phi_bi = find_min(np.array([0.7, 0, 0, 0, 0.05]) + 0.01 * rng.standard_normal(5), (a, b, g, d))
print()
print("estado biaxial encontrado:  B0 =")
print(Bmat(phi_bi))
print("autovalores de B0:", np.sort(np.linalg.eigvalsh(Bmat(phi_bi))))
analyse("BIAXIAL ESPONTANEO (la pregunta: gapless +-2 GENUINO?)",
        phi_bi, (a, b, g, d), c1, c2)

# ---- CASO SO(5) (b=0, d=0): punto de simetria accidental
a, b, g, d = -1.0, 0.0, 1.0, 0.0
phi_s5 = find_min(np.array([0.7, 0, 0, 0, 0.0]) + 0.01 * rng.standard_normal(5), (a, b, g, d))
analyse("PUNTO SO(5) ACCIDENTAL (esperado: 4 gapless, vacio = S^4)",
        phi_s5, (a, b, g, d), c1, c2)
