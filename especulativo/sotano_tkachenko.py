# -*- coding: utf-8 -*-
"""
SOTANO — Fase C, calculo 1 (CONTROL): dispersion de Tkachenko desde la
dinamica exacta de vortices puntuales, con suma de Ewald.

Red triangular infinita de vortices identicos (kappa=1, a=1) en el marco
rotante a Omega = n_v*kappa/2 (Feynman). Linearizamos la dinamica de primer
orden (cada vortice se mueve con la velocidad inducida por los demas)
alrededor de la red, ansatz de Bloch u_j = eps*exp(i k.R_j):

    udot = A(k) u,   A(k) = S_short(k) + S_long(k) - Omega*J

donde M(k) = sum_{R!=0} DK(R) exp(-i k.R)  se parte a la Ewald:
  - DK_g = jacobiano del kernel de un blob gaussiano de vorticidad (ancho s)
  - S_short = sum_{R!=0} [DK - DK_g](R) e^{-ikR}   (decae gaussiano, rapido)
  - S_long  = n_v sum_G DKhat_g(k+G) - DK_g(0)     (Poisson; converge rapido)
  con DKhat_g,ab(q) = -kappa q_b (q_y,-q_x)_a e^{-s^2 q^2/2} / q^2
  y DK_g(0) = (kappa/4pi s^2) J   (el termino de contacto, antisimetrico).

(Nota: la parte "1" de (1 - e^{-ikR}) se cancela capa a capa por simetria
hexagonal/cuadrada — verificado aparte — asi que M(k) = -sum DK e^{-ikR} + 0;
el termino DK_g(0) y el G=0 llevan la fisica del flujo medio inducido.)

CONTROLES:
  A1: triangular -> omega = c_T k con c_T = sqrt(kappa*Omega/8pi) (Tkachenko
      1966 JETP 22:1282; Fetter RMP 81:647), isotropo en direccion de k.
  A2: resultado independiente del parametro de Ewald s (interno).
  B : red cuadrada -> INESTABLE (Tkachenko JETP 23:1049).
"""
import numpy as np

KAPPA = 1.0
A = 1.0
J = np.array([[0.0, -1.0], [1.0, 0.0]])

def lattices(kind):
    if kind == "tri":
        a1 = np.array([A, 0.0]); a2 = np.array([0.5*A, 0.5*np.sqrt(3)*A])
        nv = 2.0/(np.sqrt(3)*A*A)
    else:
        a1 = np.array([A, 0.0]); a2 = np.array([0.0, A])
        nv = 1.0/(A*A)
    # reciproca: b_i . a_j = 2pi delta_ij
    Bmat = 2*np.pi*np.linalg.inv(np.array([a1, a2]).T).T  # filas = b1, b2
    return a1, a2, Bmat[0], Bmat[1], nv

def points(a1, a2, rmax):
    nmax = int(rmax/np.min([np.linalg.norm(a1), np.linalg.norm(a2)])) + 3
    m, n = np.meshgrid(np.arange(-nmax, nmax+1), np.arange(-nmax, nmax+1))
    R = m[..., None]*a1 + n[..., None]*a2
    R = R.reshape(-1, 2)
    r = np.linalg.norm(R, axis=1)
    keep = (r > 1e-9) & (r <= rmax)
    return R[keep], r[keep]

def DK_exact(R, r):
    x, y = R[:, 0], R[:, 1]
    r4 = r**4
    p = KAPPA/(2*np.pi)
    dk = np.empty((len(R), 2, 2))
    dk[:, 0, 0] = p*2*x*y/r4
    dk[:, 0, 1] = p*(y*y - x*x)/r4
    dk[:, 1, 0] = p*(y*y - x*x)/r4
    dk[:, 1, 1] = -p*2*x*y/r4
    return dk

def DK_gauss(R, r, s):
    """Jacobiano del kernel del blob gaussiano: K = (kappa/2pi)(-y,x) g(r),
    g = (1 - E)/r^2, E = exp(-r^2/2s^2)."""
    x, y = R[:, 0], R[:, 1]
    E = np.exp(-r*r/(2*s*s))
    g = (1.0 - E)/(r*r)
    gp = (E*r*r/(s*s) - 2.0*(1.0 - E))/r**3   # dg/dr
    p = KAPPA/(2*np.pi)
    dk = np.empty((len(R), 2, 2))
    dk[:, 0, 0] = p*(-y)*gp*x/r
    dk[:, 0, 1] = p*(-g - y*gp*y/r)
    dk[:, 1, 0] = p*( g + x*gp*x/r)
    dk[:, 1, 1] = p*( x*gp*y/r)
    return dk

def DKhat_gauss(q, s):
    """FT: DKhat_ab(q) = -kappa q_b (q_y,-q_x)_a e^{-s^2 q^2/2}/q^2."""
    qx, qy = q
    q2 = qx*qx + qy*qy
    if q2 < 1e-14:
        return np.zeros((2, 2))
    damp = np.exp(-s*s*q2/2.0)
    vec = np.array([qy, -qx])           # indice a
    return -KAPPA*np.outer(vec, q)*damp/q2   # [a,b]

def M_ewald(kvec, kind, s, rshort_fac=9.0, gmax_fac=9.0):
    a1, a2, b1, b2, nv = lattices(kind)
    # corto alcance
    Rl, rl = points(a1, a2, rshort_fac*s)
    dks = DK_exact(Rl, rl) - DK_gauss(Rl, rl, s)
    phase = np.exp(-1j*(Rl @ kvec))
    S_short = -np.tensordot(phase, dks, axes=(0, 0))   # signo: M = -sum DK e^{-ikR}
    # largo alcance (Poisson)
    gmax = gmax_fac/s
    nb = int(gmax/min(np.linalg.norm(b1), np.linalg.norm(b2))) + 2
    S_long = np.zeros((2, 2), dtype=complex)
    for mm in range(-nb, nb+1):
        for nn in range(-nb, nb+1):
            G = mm*b1 + nn*b2
            q = G + kvec
            if np.linalg.norm(q) > gmax + np.linalg.norm(kvec):
                continue
            S_long += DKhat_gauss(q, s)
    S_long *= nv
    S_long -= (KAPPA/(4*np.pi*s*s))*J          # -DK_g(0)
    S_long = -S_long                            # mismo signo global que S_short
    return S_short + S_long, nv

def omega_k(kvec, kind, s):
    M, nv = M_ewald(kvec, kind, s)
    Om = nv*KAPPA/2.0
    Amat = M - Om*J
    lam = np.linalg.eigvals(Amat)
    return np.max(np.abs(lam.imag)), np.max(lam.real), Om

print("=== CONTROL A: red TRIANGULAR (Ewald) ===")
_, _, _, _, nv = lattices("tri")
Om = nv*KAPPA/2.0
cT = np.sqrt(KAPPA*Om/(8*np.pi))
print(f"Omega = {Om:.5f}   c_T teorico = {cT:.6f}")
print(f"{'ka':>6} {'omega':>10} {'omega/k':>10} {'inestab':>11}   (s=2a)")
for ka in (0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.6, 0.8, 1.0):
    om, gr, _ = omega_k(np.array([ka, 0.0]), "tri", 2.0*A)
    print(f"{ka:6.2f} {om:10.6f} {om/ka:10.6f} {gr:11.2e}")

print()
print("--- Control interno A2: independencia del parametro de Ewald (ka=0.2) ---")
for s in (1.5, 2.0, 3.0):
    om, gr, _ = omega_k(np.array([0.2, 0.0]), "tri", s*A)
    print(f"  s={s:.1f}a: omega={om:.6f}  omega/k={om/0.2:.6f}")

print()
print("--- Control interno A3: isotropia (ka=0.2, k a 0deg vs 30deg vs 90deg) ---")
for th in (0.0, 30.0, 90.0):
    kv = 0.2*np.array([np.cos(np.radians(th)), np.sin(np.radians(th))])
    om, gr, _ = omega_k(kv, "tri", 2.0*A)
    print(f"  theta={th:5.1f}: omega/k = {om/0.2:.6f}")

print()
print("=== CONTROL B: red CUADRADA — debe ser INESTABLE ===")
for ka in (0.4, 0.8, 1.5, 2.5):
    om, gr, _ = omega_k(np.array([ka, 0.0]), "sq", 2.0*A)
    print(f"  ka={ka:4.1f}: Re(lambda)max = {gr:+.5f}  (>0 = inestable)")
