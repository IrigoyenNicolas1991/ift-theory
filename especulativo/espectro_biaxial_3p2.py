# ETAPA ESPECULATIVA TCI 2.0 - calculo preliminar, no validado (backup autorizado 2026-07-17)
# ============================================================================
# TERCER CALCULO TCI 2.0: condensado J=2 complejo con el funcional GL TEXTUAL
# de la literatura 3P2 (Yasui-Chatterjee-Nitta 1810.04901 eqs. 17-19; weak
# coupling: cuartico = beta[(trA*A)^2 - tr(A*^2A^2)], gradientes K1=K2=K3=K).
# Sexto orden textual (9 terminos, eq. 19). Octavo orden NO extraido de la
# literatura: se usa SOLO un regularizador eps*(trA*A)^4 que NO rompe la
# degeneracion nematica (t es constante sobre la familia) - declarado.
# CASOS: (A) solo cuartico [degeneracion SO(5)]; (B) gamma<0 (signo de materia
# de neutrones, B=0 -> UN); (C) gamma>0 (signo hipotetico declarado para el
# medio TCI -> ver si selecciona D4-BN espontaneamente).
# ============================================================================
import numpy as np

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(23)

E = np.zeros((5, 3, 3))
E[0] = np.diag([1, -1, 0]) / np.sqrt(2)
E[1] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / np.sqrt(2)
E[2] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]]) / np.sqrt(2)
E[3] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]]) / np.sqrt(2)
E[4] = np.diag([-1, -1, 2]) / np.sqrt(6)

def Amat(x):
    return np.einsum('a,aij->ij', x[:5], E) + 1j * np.einsum('a,aij->ij', x[5:], E)

def xvec(A):
    return np.concatenate([[np.real(np.trace(A @ E[a])) for a in range(5)],
                           [np.imag(np.trace(A @ E[a])) for a in range(5)]])

def V(x, al, be, ga, eps):
    A = Amat(x); Ab = np.conj(A)
    t  = np.real(np.trace(A @ Ab))                    # tr(A A*)
    u  = np.trace(A @ A)                              # tr(A^2), complejo
    ub = np.conj(u)
    q4 = t**2 - np.real(np.trace(Ab @ Ab @ A @ A))    # cuartico weak coupling
    # sexto orden textual (1810.04901 eq. 19):
    A2 = A @ A; Ab2 = Ab @ Ab
    s6 = (-3 * t * np.real(u * ub)
          + 4 * t**3
          + 6 * t * np.real(np.trace(Ab2 @ A2))
          + 12 * t * np.real(np.trace(Ab @ A @ Ab @ A))
          - 6 * np.real(ub * np.trace(Ab @ A @ A @ A))
          - 6 * np.real(u * np.trace(Ab @ Ab @ Ab @ A))
          - 12 * np.real(np.trace(Ab @ Ab @ Ab @ A @ A @ A))
          + 12 * np.real(np.trace(Ab2 @ A2 @ Ab @ A))
          + 8 * np.real(np.trace(Ab @ A @ Ab @ A @ Ab @ A)))
    return al * t + be * q4 + ga * s6 + eps * t**4

def grad(x, *p, h=1e-6):
    g = np.zeros(10)
    for a in range(10):
        dx = np.zeros(10); dx[a] = h
        g[a] = (V(x + dx, *p) - V(x - dx, *p)) / (2 * h)
    return g

def hess(x, *p, h=1e-4):
    H = np.zeros((10, 10))
    for i in range(10):
        for j in range(i, 10):
            di = np.zeros(10); di[i] = h
            dj = np.zeros(10); dj[j] = h
            H[i, j] = (V(x+di+dj, *p) - V(x+di-dj, *p) - V(x-di+dj, *p) + V(x-di-dj, *p)) / (4*h*h)
            H[j, i] = H[i, j]
    return H

def find_min(x0, params, iters=60000, lr=0.01):
    x = x0.astype(float).copy()
    for _ in range(iters):
        gv = grad(x, *params)
        if np.linalg.norm(gv) < 1e-10:
            break
        x -= lr * gv
        if np.linalg.norm(x) > 50:
            print("    (RUNAWAY: energia no acotada con estos parametros)")
            return x
    return x

L = np.zeros((3, 3, 3))
L[0] = np.array([[0,0,0],[0,0,-1],[0,1,0]])
L[1] = np.array([[0,0,1],[0,0,0],[-1,0,0]])
L[2] = np.array([[0,-1,0],[1,0,0],[0,0,0]])

def broken_dirs(x):
    A = Amat(x)
    dirs = []
    for i in range(3):
        v = xvec(L[i] @ A - A @ L[i])
        if np.linalg.norm(v) > 1e-8:
            dirs.append(v / np.linalg.norm(v))
    vph = xvec(1j * A)
    if np.linalg.norm(vph) > 1e-8:
        dirs.append(vph / np.linalg.norm(vph))
    return np.array(dirs)

# gradientes: weak coupling K1=K2=K3=K  =>  c1 = K, y (K2+K3 en Fourier) = 2K
def Kgrad(k, K):
    kE = np.einsum('i,aij->aj', k, E)
    K5 = K * (k @ k) * np.eye(5) + 2 * K * np.einsum('aj,bj->ab', kE, kE)
    Kfull = np.zeros((10, 10))
    Kfull[:5, :5] = K5; Kfull[5:, 5:] = K5
    return Kfull

def helicity_content(vec, k):
    khat = k / np.linalg.norm(k)
    B = Amat(vec)
    P = np.eye(3) - np.outer(khat, khat)
    BTT = P @ B @ P - 0.5 * P * np.trace(P @ B @ P)
    Bv = P @ B @ khat
    n2 = np.sum(np.abs(BTT)**2); n1 = 2 * np.sum(np.abs(Bv)**2)
    tot = np.sum(np.abs(B)**2)
    return n2/tot, n1/tot, max(0.0, 1 - n2/tot - n1/tot)

def r_of_state(A0):
    """extraer r de autovalores ordenados como diag(r,-(1+r),1)*A00 (fase real)"""
    ev = np.sort(np.real(np.linalg.eigvals(A0 * np.exp(-1j*np.angle(np.trace(A0@A0))/2))))
    mx = ev[2]
    return ev[0]/mx if abs(mx) > 1e-9 else np.nan

def analyse(tag, x0, params, K, kmag=1e-3):
    print("=" * 78)
    print(tag)
    print(f"  |grad V| = {np.linalg.norm(grad(x0, *params)):.2e}   V = {V(x0, *params):.6f}")
    A0 = Amat(x0)
    ev = np.linalg.eigvals(A0)
    print(f"  autovalores A0: {np.sort_complex(ev)}   r estimado: {r_of_state(A0):.3f}")
    M = hess(x0, *params)
    wM = np.sort(np.linalg.eigvalsh(M))
    nzero = np.sum(np.abs(wM) < 1e-6)
    R = broken_dirs(x0)
    rank = np.linalg.matrix_rank(R, tol=1e-6) if len(R) else 0
    print(f"  rotos (rot+U1): {rank}   modos sin masa k=0: {nzero}   masas^2: {wM[wM>1e-6][:3]}...")
    for kdir, name in [(np.array([0,0,1.]), "k||z"), (np.array([1,0,0.]), "k||x"),
                       (np.array([1,1,1.])/np.sqrt(3), "k||(111)")]:
        kk = kmag * kdir
        w2, U = np.linalg.eigh(M + Kgrad(kk, K))
        line = []
        for m in range(10):
            if w2[m] < (10 * kmag)**2:
                vph = np.sqrt(max(w2[m], 0)) / kmag
                h2, h1, h0 = helicity_content(U[:, m], kk)
                cls = "TT" if h2 > 0.9 else ("V" if h1 > 0.9 else ("S" if h0 > 0.9 else "mix"))
                line.append(f"{cls}(v={vph:.3f})")
        print(f"  {name}: " + "  ".join(line))

# ============================ CASOS ============================
K = 1.0
al, be = -1.0, 1.0

print("############ CASO A: solo cuartico weak-coupling (degeneracion) ############")
paramsA = (al, be, 0.0, 0.0)
for seed, name in [(np.array([0.9,0,0,0,0.]), "semilla D4 (r=-1)"),
                   (np.array([0,0,0,0,0.9]), "semilla UN (r=-1/2)"),
                   (0.4*rng.standard_normal(10), "semilla aleatoria")]:
    x0 = seed.copy() if len(seed)==10 else np.concatenate([seed, np.zeros(5)])
    x0 = x0 + 0.01*rng.standard_normal(10)
    xm = find_min(x0, paramsA)
    analyse(f"A / {name}", xm, paramsA, K)

print()
print("############ CASO B: gamma<0 (signo materia de neutrones, B=0) ############")
paramsB = (al, be, -0.15, 0.05)
xmB = find_min(np.concatenate([0.4*rng.standard_normal(5), np.zeros(5)]), paramsB)
analyse("B / minimo global (esperado UN, r=-1/2)", xmB, paramsB, K)

print()
print("############ CASO C: gamma>0 (signo hipotetico TCI) ############")
paramsC = (al, be, +0.15, 0.05)
xmC = find_min(np.concatenate([0.4*rng.standard_normal(5), np.zeros(5)]), paramsC)
analyse("C / minimo global (pregunta: se selecciona D4-BN, r=-1?)", xmC, paramsC, K)
# verificacion cruzada desde semilla UN
xmC2 = find_min(np.array([0,0,0,0,0.8,0,0,0,0,0.]) + 0.01*rng.standard_normal(10), paramsC)
analyse("C / desde semilla UN (control de convergencia)", xmC2, paramsC, K)
