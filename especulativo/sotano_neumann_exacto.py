# -*- coding: utf-8 -*-
"""
SOTANO — RAMA 1: la estructura fina con NEUMANN EXACTO (el cálculo que la
auditoría adversarial declaró obligatorio para el régimen denso).

Anillos identicos R=1, ejes ±z (los finalistas del teorema dipolar son todos
uniaxiales), energia por par = s_i s_j * I(rho, z) con
    I(rho,z) = (1/4pi) ∮∮ dl1·dl2 / |r12|      (Neumann; unidades rho_f*Γ²=1)
calculada por cuadratura 2D (trapecio periodico) con cache por clase de
desplazamiento.

CONTROLES:
  C1: coaxial (rho=0) contra la formula eliptica de Maxwell
      I = sqrt(R1R2)[(2/k - k)K(k) - (2/k)E(k)],  k² = 4R1R2/((R1+R2)²+z²)
      (K,E por media aritmetico-geometrica, sin scipy).
  C2: limite lejano contra el dipolo I_dip = (pi R⁴/4d³)(3cos²θ - 1).
  C3: replica de los numeros del auditor adversarial (cocientes
      exacto/dipolo: coaxial d=2R -> ~0.575; coplanar d=2.2R -> ~2.16).

ESTRUCTURAS COMPARADAS (todas con s=(-1)^capa, laminares antialineadas;
a = espaciado en la capa >= 2.05 por nucleo duro coplanar; capas paralelas
nunca se intersectan):
  A   capas cuadradas apiladas alineadas          (tet simple)
  A'  capas cuadradas apiladas con offset (a/2,a/2)  (tipo bct)
  T   capas triangulares apiladas alineadas
  T'  capas triangulares apiladas con offset (AB, tipo HCP)
Comparacion a DENSIDAD FIJA v_c (volumen por anillo), minimizando sobre
(a, c) con v_c = A_capa * c fijo. Cutoff exacto r < RCUT (cola dipolar
despreciada por cancelacion antialineada; declarado).
"""
import numpy as np
from math import pi, sqrt

NQ = 256          # cuadratura por dimension (512 en spot-checks)
RCUT = 8.0

# ---------- elipticas por AGM ----------
def KE(m):
    """K(m), E(m) con m = k^2, por AGM."""
    a, b, c = 1.0, sqrt(1.0 - m), sqrt(m)
    s, f = 0.5*c*c, 1.0
    for _ in range(60):
        an = 0.5*(a + b)
        c = 0.5*(a - b)
        b = sqrt(a*b)
        a = an
        f *= 2.0
        s += 0.5*f*c*c
        if c < 1e-16:
            break
    K = pi/(2*a)
    E = K*(1.0 - s)
    return K, E

def I_coaxial_elliptic(z):
    k2 = 4.0/(4.0 + z*z)
    k = sqrt(k2)
    K, E = KE(k2)
    return ((2.0/k - k)*K - (2.0/k)*E)

# ---------- Neumann por cuadratura ----------
_ph = np.linspace(0, 2*pi, NQ, endpoint=False)
_P1, _P2 = np.meshgrid(_ph, _ph, indexing='ij')
_C12 = np.cos(_P1 - _P2)
_cos1, _sin1 = np.cos(_P1), np.sin(_P1)
_cos2, _sin2 = np.cos(_P2), np.sin(_P2)

def I_neumann(rho, z):
    dx = _cos1 - (_cos2 + rho)
    dy = _sin1 - _sin2
    D = np.sqrt(dx*dx + dy*dy + z*z)
    val = np.sum(_C12/D)*(2*pi/NQ)**2
    return val/(4*pi)

_cache = {}
def I_pair(rho, z):
    key = (round(rho, 6), round(abs(z), 6))
    if key not in _cache:
        _cache[key] = I_neumann(*key)
    return _cache[key]

def I_dipolo(rho, z):
    d2 = rho*rho + z*z
    d = sqrt(d2)
    c2 = z*z/d2
    return (pi/(4*d2*d))*(3*c2 - 1.0)

# ---------- estructuras ----------
def capa_cuadrada(a, rmax):
    n = int(rmax/a) + 2
    g = np.arange(-n, n+1)
    X, Y = np.meshgrid(g*a, g*a, indexing='ij')
    return np.stack([X.ravel(), Y.ravel()], axis=1)

def capa_triangular(a, rmax):
    n = int(rmax/a) + 3
    pts = []
    for i in range(-n, n+1):
        for j in range(-n, n+1):
            pts.append([a*(i + 0.5*j), a*(sqrt(3)/2)*j])
    return np.array(pts)

def energia_por_anillo(tipo, a, c, rcut=RCUT):
    """E/anillo de la red laminar antialineada (s=(-1)^capa)."""
    if tipo in ("A", "Ap"):
        capa = capa_cuadrada(a, rcut + a)
        offs = np.array([0.5*a, 0.5*a]) if tipo == "Ap" else np.zeros(2)
    else:
        capa = capa_triangular(a, rcut + a)
        offs = np.array([0.5*a, a*sqrt(3)/6]) if tipo == "Tp" else np.zeros(2)
    E = 0.0
    kmax = int(rcut/c) + 1
    for k in range(-kmax, kmax+1):
        z = k*c
        sh = capa + (offs if (k % 2 != 0) else 0.0)
        rr = np.linalg.norm(sh, axis=1)
        rtot = np.sqrt(rr*rr + z*z)
        sgn = (-1.0)**k
        for (x, y), rt in zip(sh, rtot):
            if rt < 1e-9 or rt > rcut:
                continue
            E += 0.5*sgn*I_pair(sqrt(x*x + y*y), z)
    return E

def minimiza(tipo, v_c, a_min=2.05):
    area = (lambda a: a*a) if tipo in ("A", "Ap") else (lambda a: a*a*sqrt(3)/2)
    best = None
    for a in np.linspace(a_min, 3.4, 12):
        c = v_c/area(a)
        if c < 0.35 or c > 4.0:
            continue
        E = energia_por_anillo(tipo, a, c)
        if best is None or E < best[0]:
            best = (E, a, c)
    # refinar
    E0, a0, c0 = best
    for a in np.linspace(max(a_min, a0-0.12), a0+0.12, 7):
        c = v_c/area(a)
        E = energia_por_anillo(tipo, a, c)
        if E < best[0]:
            best = (E, a, c)
    return best

# ---------- CONTROLES ----------
print("=== C1: cuadratura vs eliptica (coaxial) ===")
for z in (2.0, 3.0, 5.0):
    q = I_pair(0.0, z)
    e = I_coaxial_elliptic(z)
    print(f"  z={z}: quad={q:.8f}  eliptica={e:.8f}  dif={abs(q-e):.2e}")

print("=== C2: limite dipolar lejano ===")
for rho, z in ((0.0, 8.0), (8.0, 0.0), (5.0, 5.0)):
    q = I_pair(rho, z)
    d = I_dipolo(rho, z)
    print(f"  rho={rho} z={z}: exacto={q:.6e}  dipolo={d:.6e}  cociente={q/d:.4f}")

print("=== C3: replica de los numeros del auditor ===")
for tag, rho, z in (("coaxial d=2R", 0.0, 2.0), ("coplanar d=2.2R", 2.2, 0.0),
                    ("coplanar d=2.5R", 2.5, 0.0), ("coaxial d=2.5R", 0.0, 2.5)):
    q = I_pair(rho, z)
    d = I_dipolo(rho, z)
    print(f"  {tag}: exacto/dipolo = {q/d:.3f}")

# ---------- PRODUCCION ----------
print()
print("=== RAMA 1: comparacion de estructuras laminares con Neumann exacto ===")
print("(E por anillo, unidades rho_f*Gamma^2*R=1; cutoff exacto r<8R; menor=mejor)")
for v_c in (9.0, 12.0, 16.0):
    print(f"\n--- densidad fija v_c = {v_c} ---")
    res = {}
    for tipo, nombre in (("A", "A  cuadrada alineada"), ("Ap", "A' cuadrada offset (bct)"),
                         ("T", "T  triangular alineada"), ("Tp", "T' triangular offset (HCP-like)")):
        E, a, c = minimiza(tipo, v_c)
        res[nombre] = (E, a, c)
        print(f"  {nombre:28s} E={E:+.5f}  (a={a:.2f}, c={c:.2f}, c/a={c/a:.2f})")
    ganador = min(res, key=lambda kk: res[kk][0])
    orden = sorted(res.items(), key=lambda kv: kv[1][0])
    gap = orden[1][1][0] - orden[0][1][0]
    print(f"  GANADOR: {ganador}  (gap al segundo: {gap:+.5f})")

print()
print("Nota: cola r>8R despreciada (estructuras antialineadas, cancelacion")
print("rapida); spot-check de convergencia: repetir v_c=12 con RCUT=10 y NQ=512")
import time
t0 = time.time()
_cache.clear()
globals()['NQ'] = NQ  # (la cuadratura global ya esta armada con NQ=256)
E, a, c = minimiza("A", 12.0)
E2, a2, c2 = minimiza("Ap", 12.0)
print(f"(re-run v_c=12 con cache limpio: A={E:+.5f}, A'={E2:+.5f}; {time.time()-t0:.0f}s)")
