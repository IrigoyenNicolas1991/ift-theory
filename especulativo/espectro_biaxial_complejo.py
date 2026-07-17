# ETAPA ESPECULATIVA TCI 2.0 - calculo preliminar, no validado (backup autorizado 2026-07-17)
# ============================================================================
# SEGUNDO CALCULO TCI 2.0: condensado J=2 COMPLEJO (tipo GL de 3P2)
# ----------------------------------------------------------------------------
# A_ij(x,t) = matriz 3x3 COMPLEJA simetrica sin traza (10 componentes reales).
# L = chi Tr(dA/dt dAbar/dt) - c1 Tr(d_iA d_iAbar) - c2 (d_iA_ij)(d_kAbar_kj) - V
# V = alpha Tr(A Abar) + b1 |Tr A^2|^2 + b2 [Tr(A Abar)]^2 + b3 Tr(A A Abar Abar)
#   (los 3 invariantes cuarticos estandar; A simetrica => Adag = Abar)
#   + d6 * (levanta la degeneracion nematica; se define al conocer la literatura)
# COEFICIENTES: por defecto un SET DE PRUEBA declarado (para validar maquinaria);
# los valores de weak-coupling de la literatura 3P2 se enchufan al llegar
# (agente en vuelo). NADA de lo cuantitativo es final hasta ese momento.
# Tiempo: 2do orden (sin termino de Berry) - declarado, igual que la version real.
# ============================================================================
import numpy as np

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(11)

# base ortonormal simetrica sin traza (igual que la version real)
E = np.zeros((5, 3, 3))
E[0] = np.diag([1, -1, 0]) / np.sqrt(2)
E[1] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / np.sqrt(2)
E[2] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]]) / np.sqrt(2)
E[3] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]]) / np.sqrt(2)
E[4] = np.diag([-1, -1, 2]) / np.sqrt(6)

def Amat(x):
    """x = 10 reales: primeros 5 = parte real, ultimos 5 = imaginaria"""
    return np.einsum('a,aij->ij', x[:5], E) + 1j * np.einsum('a,aij->ij', x[5:], E)

def xvec(A):
    return np.concatenate([[np.real(np.trace(A @ E[a])) for a in range(5)],
                           [np.imag(np.trace(A @ E[a])) for a in range(5)]])

def V(x, al, b1, b2, b3, d6):
    A = Amat(x); Ab = np.conj(A)
    t = np.real(np.trace(A @ Ab))
    u = np.trace(A @ A)
    v = np.real(np.trace(A @ A @ Ab @ Ab))
    # d6: termino sexto generico provisorio (|TrA^2|^2 * TrAAbar) para levantar
    # la degeneracion nematica SI la literatura lo confirma; se reemplaza por el
    # termino textual cuando llegue el agente.
    return al * t + b1 * abs(u)**2 + b2 * t**2 + b3 * v + d6 * abs(u)**2 * t

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

def find_min(x0, params, iters=40000, lr=0.02):
    x = x0.astype(float).copy()
    for _ in range(iters):
        gv = grad(x, *params)
        if np.linalg.norm(gv) < 1e-10:
            break
        x -= lr * gv
    return x

# generadores rotos: 3 rotaciones + U(1) de fase
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
    vph = xvec(1j * A)      # U(1): A -> e^{i eps} A
    if np.linalg.norm(vph) > 1e-8:
        dirs.append(vph / np.linalg.norm(vph))
    return np.array(dirs)

# gradiente espacial: c1 k^2 * Id + c2 (k.Ea)_j (k.Eb)_j  (bloque real e imag iguales)
def Kgrad(k, c1, c2):
    kE = np.einsum('i,aij->aj', k, E)
    K5 = c1 * (k @ k) * np.eye(5) + c2 * np.einsum('aj,bj->ab', kE, kE)
    K = np.zeros((10, 10))
    K[:5, :5] = K5; K[5:, 5:] = K5
    return K

def helicity_content(vec, k):
    khat = k / np.linalg.norm(k)
    B = Amat(vec)                    # matriz compleja de la fluctuacion
    P = np.eye(3) - np.outer(khat, khat)
    BTT = P @ B @ P - 0.5 * P * np.trace(P @ B @ P)
    Bv = P @ B @ khat
    n2 = np.sum(np.abs(BTT)**2); n1 = 2 * np.sum(np.abs(Bv)**2)
    tot = np.sum(np.abs(B)**2)
    return n2/tot, n1/tot, max(0.0, 1 - n2/tot - n1/tot)

def analyse(tag, x0, params, c1, c2, kmag=1e-3):
    print("=" * 78)
    print(tag)
    print(f"  |grad V| = {np.linalg.norm(grad(x0, *params)):.2e} (control ~0)")
    A0 = Amat(x0)
    ev = np.linalg.eigvals(A0)
    print(f"  autovalores de A0: {np.sort_complex(ev)}")
    M = hess(x0, *params)
    wM = np.sort(np.linalg.eigvalsh(M))
    print(f"  masas^2 (autovalores de M): {wM}")
    R = broken_dirs(x0)
    rank = np.linalg.matrix_rank(R, tol=1e-6) if len(R) else 0
    print(f"  generadores rotos (rango, rot+U1) = {rank}")
    for v in R:
        r = np.linalg.norm(M @ v)
        if r > 1e-5:
            print(f"    OJO: direccion rota con |Mv| = {r:.2e} (pseudo-Goldstone?)")
    nzero = np.sum(np.abs(wM) < 1e-6)
    print(f"  modos sin masa en k=0: {nzero}")
    for kdir, name in [(np.array([0,0,1.]), "k||z"), (np.array([1,0,0.]), "k||x"),
                       (np.array([0,1,0.]), "k||y"),
                       (np.array([1,1,1.])/np.sqrt(3), "k||(111)")]:
        kk = kmag * kdir
        w2, U = np.linalg.eigh(M + Kgrad(kk, c1, c2))
        print(f"  --- {name}")
        for m in range(10):
            if w2[m] < (10 * kmag)**2:
                vph = np.sqrt(max(w2[m], 0)) / kmag
                h2, h1, h0 = helicity_content(U[:, m], kk)
                print(f"    gapless: v = {vph:.4f}  helicidad +-2:{h2:.2f} +-1:{h1:.2f} 0:{h0:.2f}")

# ============================ RUN (SET DE PRUEBA declarado) ============================
c1, c2 = 1.0, 0.8
# SET DE PRUEBA (a reemplazar por weak-coupling de la literatura):
# b1 < 0 favorece estados REALES (nematicos: |TrA^2| maximo); b2,b3 > 0 estabilizan.
al, b1, b2, b3, d6 = -1.0, -0.4, 1.0, 0.6, 0.0
print("SET DE PRUEBA (declarado):", dict(al=al, b1=b1, b2=b2, b3=b3, d6=d6))

# arranque cerca de biaxial real + ruido complejo chico
x0 = np.zeros(10); x0[0] = 0.7; x0 += 0.02 * rng.standard_normal(10)
x_min = find_min(x0, (al, b1, b2, b3, d6))
analyse("COMPLEJO, minimo encontrado desde semilla biaxial", x_min, (al, b1, b2, b3, d6), c1, c2)

# tambien desde semilla uniaxial
x1 = np.zeros(10); x1[4] = 0.7; x1 += 0.02 * rng.standard_normal(10)
x_min2 = find_min(x1, (al, b1, b2, b3, d6))
analyse("COMPLEJO, minimo encontrado desde semilla uniaxial", x_min2, (al, b1, b2, b3, d6), c1, c2)
