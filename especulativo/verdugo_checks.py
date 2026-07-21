# -*- coding: utf-8 -*-
# Verdugo del no-go: verificaciones simbolicas
# (1) Cadena semi-infinita de dipolos cabeza-cola => monopolo EXACTO (mecanismo hielo de espin / solenoide)
# (2) Elasticidad anomala esmectica: propagador B kz^2 + K kperp^4 => interaccion hueco-hueco on-axis ~ 1/z^2
import sympy as sp

print("=" * 70)
print("(1) Telescoping: linea semi-infinita de dipolos z => monopolo")
rho, z, zp = sp.symbols('rho z zp', positive=True)
G = 1 / (4 * sp.pi * sp.sqrt(rho**2 + (z - zp)**2))
phi = sp.integrate(sp.diff(G, zp), (zp, -sp.oo, 0))
print("  phi(rho,z) =", sp.simplify(phi))
print("  (esperado: 1/(4*pi*sqrt(rho^2+z^2)) => campo MONOPOLAR puro,")
print("   pese a que cada elemento es un dipolo y div del campo total = 0)")

print("=" * 70)
print("(2a) Integral transversal esmectica: I(kz) = int d2kperp/(2pi)^2 1/(B kz^2 + K kperp^4)")
B, K, kz, kperp = sp.symbols('B K k_z k_perp', positive=True)
I = sp.integrate(kperp / (B * kz**2 + K * kperp**4), (kperp, 0, sp.oo)) / (2 * sp.pi)
I = sp.simplify(I)
print("  I(kz) =", I)
print("  (esperado: 1/(8*sqrt(B*K)*kz) -> NO analitico en kz=0: cola de largo alcance)")

print("=" * 70)
print("(2b) FT regularizada de |k|: U(z) = int dk/(2pi) |k| e^{ikz} e^{-eps|k|}")
k, eps, zeta = sp.symbols('k epsilon zeta', positive=True)
U = sp.integrate(k * sp.cos(k * zeta) * sp.exp(-eps * k), (k, 0, sp.oo)) / sp.pi
U = sp.simplify(U)
Ulim = sp.limit(U, eps, 0)
print("  U(z; eps) =", U)
print("  lim eps->0:", Ulim, "  (esperado: -1/(pi z^2))")

print("=" * 70)
print("(2c) Interaccion on-axis entre dos centros de dilatacion (fuente P d/dz delta) en esmectico:")
# E_int = + P^2 * G''(z), G(kz) = 1/(8 sqrt(BK) |kz|)
# G''(z) = -(1/(8 sqrt(BK))) * FT[|k|](z) = -(1/(8 sqrt(BK))) * (-1/(pi z^2))
P = sp.symbols('P', positive=True)
E_int = P**2 * (-(sp.Rational(1, 8) / sp.sqrt(B * K)) * Ulim.subs(zeta, z))
print("  E_int(z) =", sp.simplify(E_int))
print("  => +P^2/(8*pi*sqrt(B*K)*z^2): potencia 1/z^2 (mas LENTA que el 1/r^3 del censo),")
print("     REPULSIVA on-axis para inclusiones del mismo signo => signo NO universal")

print("=" * 70)
print("(3) Crossover del regimen esmectico con gap de cizalla soft ~ 0.0008-0.005 (politipos)")
import math
for gap in (0.0008, 0.005):
    print(f"  gap {gap}: lambda_cross ~ a*sqrt(C_tip/C_soft) ~ {math.sqrt(1/gap):.1f} a")
