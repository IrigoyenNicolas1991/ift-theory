# -*- coding: utf-8 -*-
"""
SOTANO — EL VEREDICTO DE BULK: ¿la espuma de anillos ordena un oceano uniforme,
o el mosaico es intrinseco? Metodo de Luttinger-Tisza (k-space) + Ewald 3D.

LOGICA (teorema, no recocido):
  Para dipolos puntuales en una red de Bravais, E = (s/2) sum_{i!=j} n_i.T(R_ij).n_j
  con T(R) = (I - 3 Rhat Rhat)/R^3;  s=+1 magnetico, s=-1 VORTICES (Neumann).
  En Fourier: E/N = (s/2) sum_k c_k^dag J(k) c_k, con J(k) = sum_{R!=0} T(R) e^{ikR}.
  Cota de Luttinger-Tisza (restriccion debil): E/N >= (s/2) * extremo_BZ de autovalor.
    - magnetico: E/N >= (1/2) min_k lambda_min(J(k))
    - vortices : E/N >= -(1/2) max_k lambda_max(J(k))
  Si el extremo se alcanza en un modo CONMENSURADO (e^{ikR} = +-1 en toda la red,
  k = semiperiodo), ese modo satisface |n_i|=1 exacto => ES el fundamental de bulk,
  y NINGUN estado (mosaico, vidrio, multi-k) puede superarlo. Veredicto cerrado.

J(k) por Ewald (derivado a mano, controles abajo):
  J(k) = sum_{R!=0} T_sr(R) e^{ikR}                                   [real, erfc]
       + (4pi/v_c) sum_G qhat qhat^T e^{-q^2/4a^2},  q = k+G           [reciproco]
       - (4 a^3 / 3 sqrt(pi)) I                                        [auto]
  T_sr(R)_ab = B(r) d_ab - C(r) R_a R_b
  B(r) = erfc(ar)/r^3 + (2a/sqrt(pi)) e^{-a^2r^2}/r^2
  C(r) = 3 erfc(ar)/r^5 + (2a/sqrt(pi)) (3/r^2 + 2a^2) e^{-a^2r^2}/r^2

CONTROLES:
  C1 (interno): independencia del parametro de Ewald alpha (3 valores).
  C2 (interno): Tr J(k) ~ 0 (T es sin traza).
  C3 (literatura): signo MAGNETICO en SC debe dar el antiferro de
      Luttinger-Tisza 1946 con su constante tabulada (comparar con lo que
      traigan los agentes; el valor sale impreso).
  C4 (interno): J(k) hermitica/real-simetrica a precision numerica.

PRODUCCION (signo VORTICE):
  - Barrido BZ en SC, FCC, BCC a igual volumen por sitio v_c=1.
  - Barrido tetragonal (a=b, c/a variable, v_c=1): la red que el modo prefiera.
  - Identificar el modo ganador (k*, autovector), chequear conmensurabilidad,
    clasificar: columnar (eps || k*) / laminar (eps perp k*) / otro.
"""
import numpy as np
from math import erfc, pi, sqrt, exp

I3 = np.eye(3)

def make_lattice(kind, ca=1.0):
    """Devuelve (A = filas a1,a2,a3, v_c) con v_c = 1."""
    if kind == "sc":
        A = np.diag([1.0, 1.0, 1.0])
    elif kind == "tet":
        a = ca**(-1.0/3.0)
        A = np.diag([a, a, a*ca])
    elif kind == "fcc":
        A = 0.5*np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]], float)
        A *= (1.0/np.linalg.det(A))**(1/3)
    elif kind == "bcc":
        A = 0.5*np.array([[-1, 1, 1], [1, -1, 1], [1, 1, -1]], float)
        A *= (1.0/abs(np.linalg.det(A)))**(1/3)
    else:
        raise ValueError(kind)
    v_c = abs(np.linalg.det(A))
    B = 2*pi*np.linalg.inv(A).T   # filas b1,b2,b3
    return A, B, v_c

def real_points(A, rcut):
    nmax = int(np.ceil(rcut/np.min(np.linalg.norm(A, axis=1)))) + 2
    rng = np.arange(-nmax, nmax+1)
    m = np.stack(np.meshgrid(rng, rng, rng, indexing='ij'), axis=-1).reshape(-1, 3)
    R = m @ A
    r = np.linalg.norm(R, axis=1)
    keep = (r > 1e-9) & (r < rcut)
    return R[keep], r[keep]

def recip_points(B, gcut, k):
    nmax = int(np.ceil(gcut/np.min(np.linalg.norm(B, axis=1)))) + 2
    rng = np.arange(-nmax, nmax+1)
    m = np.stack(np.meshgrid(rng, rng, rng, indexing='ij'), axis=-1).reshape(-1, 3)
    G = m @ B
    q = G + k
    qq = np.linalg.norm(q, axis=1)
    keep = (qq < gcut) & (qq > 1e-9)
    return q[keep], qq[keep]

def Jk(k, A, B, v_c, alpha, rcut_f=5.5, gcut_f=7.0):
    rcut = rcut_f/alpha
    gcut = gcut_f*alpha*2.0
    R, r = real_points(A, rcut)
    ar = alpha*r
    erfc_v = np.vectorize(erfc)(ar)
    gau = np.exp(-ar*ar)
    Bf = erfc_v/r**3 + (2*alpha/sqrt(pi))*gau/r**2
    Cf = 3*erfc_v/r**5 + (2*alpha/sqrt(pi))*(3/r**2 + 2*alpha**2)*gau/r**2
    ph = np.exp(1j*(R @ k))
    Jr = np.einsum('n,n->', Bf, ph)*I3.astype(complex) \
         - np.einsum('n,na,nb,n->ab', Cf, R, R, ph)
    q, qq = recip_points(B, gcut, k)
    w = np.exp(-qq**2/(4*alpha**2))/qq**2
    Jg = (4*pi/v_c)*np.einsum('n,na,nb->ab', w, q, q)
    Jself = (4*alpha**3/(3*sqrt(pi)))*I3
    J = Jr + Jg - Jself
    return 0.5*(J + J.conj().T)   # hermitizar (C4 se chequea aparte)

def bz_scan(kind, ca=1.0, ngrid=14, alpha=3.0):
    A, B, v_c = make_lattice(kind, ca)
    fr = (np.arange(ngrid) + 0.5)/ngrid - 0.5   # ngrid PAR: nunca pisa k=0
    best_max = (-np.inf, None, None)   # (lambda_max, k, vec)
    best_min = (+np.inf, None, None)
    for fx in fr:
        for fy in fr:
            for fz in fr:
                k = fx*B[0] + fy*B[1] + fz*B[2]
                if np.linalg.norm(k) < 1e-8:
                    continue
                J = Jk(k, A, B, v_c, alpha)
                w, v = np.linalg.eigh(J)
                if w[-1] > best_max[0]:
                    best_max = (w[-1], np.array([fx, fy, fz]), v[:, -1].real, k)
                if w[0] < best_min[0]:
                    best_min = (w[0], np.array([fx, fy, fz]), v[:, 0].real, k)
    return best_max, best_min, A, B

def refine(kind, ca, frac0, which, alpha=3.0, steps=3, ngrid=7):
    """refina alrededor de frac0 en fracciones de red reciproca"""
    A, B, v_c = make_lattice(kind, ca)
    span = 1.0/15
    frac = frac0.copy()
    for s in range(steps):
        grid = np.linspace(-span, span, ngrid)
        best = None
        for dx in grid:
            for dy in grid:
                for dz in grid:
                    f = frac + np.array([dx, dy, dz])
                    k = f @ B
                    if np.linalg.norm(k) < 1e-6:
                        continue
                    J = Jk(k, A, B, v_c, alpha)
                    w, v = np.linalg.eigh(J)
                    val = w[-1] if which == 'max' else w[0]
                    keyv = val if which == 'max' else -val
                    if best is None or keyv > best[0]:
                        best = (keyv, f, val, v[:, -1 if which == 'max' else 0].real, k)
        frac = best[1]
        span /= 3.0
    return best[2], frac, best[3], best[4]

def clasificar(frac, eps, B):
    k = frac @ B
    kh = k/np.linalg.norm(k)
    ang = abs(eps @ kh)
    conm = np.all(np.abs(np.abs(np.mod(frac + 0.5, 1.0) - 0.5) - 0.5) < 0.02) or \
           np.all(np.abs(np.mod(frac, 0.5)) < 0.02)
    tipo = "COLUMNAR (eps||k)" if ang > 0.9 else ("LAMINAR (eps perp k)" if ang < 0.2 else f"mixto (|eps.kh|={ang:.2f})")
    return tipo, conm, ang

print("=== CONTROLES ===")
A, B, v_c = make_lattice("sc")
ktest = 0.3*B[0] + 0.2*B[1] + 0.1*B[2]
print("C1 alpha-independencia en k de prueba (autovalores de J):")
for al in (2.0, 3.0, 4.0):
    J = Jk(ktest, A, B, v_c, al)
    w = np.linalg.eigvalsh(J)
    print(f"   alpha={al:.1f}: {w[0]:+.6f} {w[1]:+.6f} {w[2]:+.6f}   TrJ={np.trace(J).real:+.2e} (C2)")
J = Jk(ktest, A, B, v_c, 3.0)
print(f"C4 no-hermiticidad relativa: {np.linalg.norm(J - J.conj().T)/np.linalg.norm(J):.1e}")

print()
print("C3 signo MAGNETICO en SC (control Luttinger-Tisza 1946):")
bm, bmin, A, B = bz_scan("sc", ngrid=14)
val, frac, eps, k = refine("sc", 1.0, bmin[1], 'min')
tipo, conm, ang = clasificar(frac, eps, B)
print(f"   minimo global: lambda={val:.5f} en frac k={np.round(frac,3)}  eps={np.round(eps,3)}")
print(f"   E/N (magnetico) = lambda/2 = {val/2:.5f} (unidades mu^2/a^3, v_c=1)")
print(f"   modo: {tipo}  conmensurado={conm}")
print(f"   [comparar contra la constante tabulada de LT que traigan los agentes]")

print()
print("=== PRODUCCION: signo VORTICE (E/N = -lambda_max/2) ===")
print(f"{'red':>10} {'c/a':>5} {'lambda_max':>11} {'E/N vort':>10}  {'k* (frac)':>18}  modo")
resultados = {}
for kind, ca in [("sc", 1.0), ("fcc", 1.0), ("bcc", 1.0)]:
    bm, _, A, B = bz_scan(kind, ca, ngrid=14)
    val, frac, eps, k = refine(kind, ca, bm[1], 'max')
    tipo, conm, ang = clasificar(frac, eps, B)
    resultados[(kind, ca)] = (val, frac, eps, tipo, conm)
    print(f"{kind:>10} {ca:5.2f} {val:11.5f} {-val/2:10.5f}  {str(np.round(frac,3)):>18}  {tipo} conm={conm}")

print()
print("Barrido tetragonal (v_c=1, la red elige su c/a):")
best_tet = None
for ca in (0.60, 0.70, 0.80, 0.90, 1.00, 1.10, 1.25, 1.40, 1.60):
    bm, _, A, B = bz_scan("tet", ca, ngrid=12)
    val, frac, eps, k = refine("tet", ca, bm[1], 'max')
    tipo, conm, ang = clasificar(frac, eps, B)
    print(f"{'tet':>10} {ca:5.2f} {val:11.5f} {-val/2:10.5f}  {str(np.round(frac,3)):>18}  {tipo} conm={conm}")
    if best_tet is None or val > best_tet[0]:
        best_tet = (val, ca, frac, eps, tipo, conm)

print()
val, ca, frac, eps, tipo, conm = best_tet
print("=== VEREDICTO ===")
print(f"Mejor estructura vortice: tetragonal c/a={ca:.2f}, lambda_max={val:.5f},")
print(f"E/N = {-val/2:.5f}, modo {tipo}, k*={np.round(frac,3)}, conmensurado={conm}")
print()
print("Si conmensurado=True: ese modo satisface |n_i|=1 exacto y alcanza la cota")
print("de Luttinger-Tisza => ES el fundamental de bulk; el mosaico de las gotas")
print("abiertas era efecto de superficie => EL OCEANO UNIFORME EXISTE.")
print("Si el maximo es no-conmensurado o degenerado en una linea/superficie de la")
print("BZ => la frustracion es intrinseca del material.")
