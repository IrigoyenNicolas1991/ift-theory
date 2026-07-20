# -*- coding: utf-8 -*-
"""
SOTANO — CIERRE DEL VEREDICTO DE BULK:
 (a) verificar que el maximo vortice esta EXACTAMENTE en el punto conmensurado
     k*=(0,0,1/2) (en fracciones de red reciproca) y que es maximo AISLADO
     (cae cuadratico en toda direccion) — con el test de conmensurabilidad
     corregido (el del script madre tenia un bug con negativos, errata);
 (b) agregar el nucleo repulsivo A/d^9 y minimizar TODO (modo + c/a + escala):
     prediccion de bulk del c/a optimo y de la razon d_apilado/d_lateral,
     confrontada contra la geometria MEDIDA en la gota abierta del calculo 3
     (d_par/d_perp ~ 1.45/1.16 ~ 1.25) — bulk y gota deben rimar.
"""
import numpy as np
from math import erfc, pi, sqrt
import importlib.util as ilu

spec = ilu.spec_from_file_location(
    "svb", r"C:\ClaudeInMyComputer\TCI CON Fable New folder\ift-theory\especulativo\sotano_bulk_veredicto.py")
# no importamos el script madre (ejecuta todo); duplicamos el kernel minimo:

I3 = np.eye(3)

def make_tet(ca):
    a = ca**(-1.0/3.0)
    A = np.diag([a, a, a*ca])
    B = 2*pi*np.linalg.inv(A).T
    return A, B, 1.0

def real_points(A, rcut):
    nmax = int(np.ceil(rcut/np.min(np.linalg.norm(A, axis=1)))) + 2
    r_ = np.arange(-nmax, nmax+1)
    m = np.stack(np.meshgrid(r_, r_, r_, indexing='ij'), axis=-1).reshape(-1, 3)
    R = m @ A
    r = np.linalg.norm(R, axis=1)
    keep = (r > 1e-9) & (r < rcut)
    return R[keep], r[keep]

def Jk(k, A, B, v_c, alpha=3.0, rcut_f=5.5, gcut_f=7.0):
    rcut = rcut_f/alpha
    R, r = real_points(A, rcut)
    ar = alpha*r
    erfc_v = np.vectorize(erfc)(ar)
    gau = np.exp(-ar*ar)
    Bf = erfc_v/r**3 + (2*alpha/sqrt(pi))*gau/r**2
    Cf = 3*erfc_v/r**5 + (2*alpha/sqrt(pi))*(3/r**2 + 2*alpha**2)*gau/r**2
    ph = np.exp(1j*(R @ k))
    Jr = np.einsum('n,n->', Bf, ph)*I3.astype(complex) \
         - np.einsum('n,na,nb,n->ab', Cf, R, R, ph)
    gcut = gcut_f*alpha*2.0
    nmax = int(np.ceil(gcut/np.min(np.linalg.norm(B, axis=1)))) + 2
    r_ = np.arange(-nmax, nmax+1)
    m = np.stack(np.meshgrid(r_, r_, r_, indexing='ij'), axis=-1).reshape(-1, 3)
    q = m @ B + k
    qq = np.linalg.norm(q, axis=1)
    keep = (qq < gcut) & (qq > 1e-9)
    q, qq = q[keep], qq[keep]
    w = np.exp(-qq**2/(4*alpha**2))/qq**2
    Jg = (4*pi/v_c)*np.einsum('n,na,nb->ab', w, q, q)
    J = Jr + Jg - (4*alpha**3/(3*sqrt(pi)))*I3
    return 0.5*(J + J.conj().T)

def lam_max(frac, ca):
    A, B, v_c = make_tet(ca)
    k = frac @ B
    return np.linalg.eigvalsh(Jk(k, A, B, v_c))[-1]

print("=== (a) EL MAXIMO ES EL PUNTO CONMENSURADO, AISLADO ===")
for ca in (1.10, 1.25, 1.40):
    f0 = np.array([0.0, 0.0, 0.5])
    l0 = lam_max(f0, ca)
    print(f"c/a={ca:.2f}: lambda(0,0,1/2) = {l0:.6f}")
    for d in (0.02, 0.05):
        vals = []
        for df in ([d,0,0],[0,d,0],[0,0,-d],[d,d,0],[d,0,-d]):
            vals.append(lam_max(f0+np.array(df), ca))
        drop = l0 - max(vals)
        print(f"   desplazando |df|~{d}: max vecino = {max(vals):.6f}  (cae {drop:+.6f}) "
              f"{'AISLADO' if drop > 0 else '<-- NO aislado!'}")

print()
print("=== (b) DIPOLO + NUCLEO: el bulk elige su c/a ===")
# modo k*=(0,0,1/2), eps=z (verificar eps de paso); energia dipolar E/N = -lambda/2
# nucleo: E_rep/N = (A/2) K9(ca) con K9 = sum_{R!=0} 1/d^9 (converge rapido)
# escala s: E(s) = -(lambda/2)/s^3 + (A K9/2)/s^9  ->  s*^6 = 3 A K9 / lambda
# E_min = -(lambda/3) / s*^3 = -(1/3) lambda^(3/2) / sqrt(3 A K9)
Acore = 2.0/3.0   # mismo A del calculo 3 (d*=1 para el par optimo aislado)
def K9(ca, rcut=6.0):
    A, B, v_c = make_tet(ca)
    R, r = real_points(A, rcut)
    return np.sum(1.0/r**9)

print(f"{'c/a':>6} {'lambda':>10} {'K9':>10} {'E_min/N':>10} {'s*':>7} {'d_apil/d_lat':>13}")
best = None
for ca in (0.9, 1.0, 1.1, 1.2, 1.25, 1.3, 1.35, 1.4, 1.5, 1.6, 1.8, 2.0):
    A, B, v_c = make_tet(ca)
    J = Jk(np.array([0, 0, 0.5]) @ B, A, B, v_c)
    w, v = np.linalg.eigh(J)
    lam, eps = w[-1], v[:, -1].real
    k9 = K9(ca)
    s6 = 3*Acore*k9/lam
    s = s6**(1/6)
    Emin = -(lam/3)/s**3
    # geometria fisica: apilado = c*s, lateral = a*s -> razon = c/a
    if best is None or Emin < best[0]:
        best = (Emin, ca, lam, s, eps)
    print(f"{ca:6.2f} {lam:10.5f} {k9:10.3f} {Emin:10.5f} {s:7.4f} {ca:13.3f}"
          + ("   eps=" + str(np.round(eps, 3)) if ca in (1.0, 1.4) else ""))

Emin, ca, lam, s, eps = best
print()
print(f"OPTIMO DE BULK: c/a = {ca:.2f}  (E/N = {Emin:.5f}, escala s* = {s:.4f}, eps = {np.round(eps,3)})")
print(f"razon apilado/lateral predicha por el bulk: {ca:.2f}")
print(f"razon MEDIDA en la gota abierta (calculo 3): d_par/d_perp ~ 1.45/1.16 ~ 1.25")
print()
print("=== test de conmensurabilidad corregido (errata del flag del script madre) ===")
def conmensurado(frac, tol=0.01):
    f = np.abs(np.asarray(frac))
    return bool(np.all((np.abs(f) < tol) | (np.abs(f - 0.5) < tol)))
for f in ([0, 0, 0.5], [-0.499, -0.001, -0.499], [0.25, 0, 0]):
    print(f"   {f}: conmensurado={conmensurado(f)}")
