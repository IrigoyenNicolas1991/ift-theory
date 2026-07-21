# -*- coding: utf-8 -*-
"""
COLUMNA B - paso 2: solucion exacta de la ecuacion vectorial estacionaria
   (M_Pl^2+alpha) nabla^2 S_i - m1^2 S_i = T^{0i},   T^{0i} = rho(r) (omega x vec)_i
para esfera rigida uniforme (fuente declarada), y limite RG contra Kerr.

Definiciones: A = M_Pl^2+alpha,  mu^2 = m1^2/A,  Gtilde = G M_Pl^2/A.
En RG (harmonica): nabla^2 h_{0i} = 16 pi G T^{0i}  =>  h_0 = 2G (x x J)/r^3 (Kerr).
"""
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
r = sp.sqrt(x**2 + y**2 + z**2)
mu, R, rho0, G, w = sp.symbols('mu R rho0 G omega', positive=True)
rr = sp.Symbol('r', positive=True)

# ---------- A: identidad vectorial nabla^2 [g(r) (omega x vec)] ----------
g = sp.Function('g')
wv = sp.Matrix([0, 0, w])          # omega en z, sin perdida de generalidad
xv = sp.Matrix([x, y, z])
V = g(r) * wv.cross(xv)
lapl = lambda f: sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)
target = [sp.simplify(lapl(V[i])
                      - (sp.diff(g(rr), rr, 2) + 4 * sp.diff(g(rr), rr) / rr)
                      .subs(rr, r) * wv.cross(xv)[i]) for i in range(3)]
assert target == [0, 0, 0]
print("A: nabla^2[g(r)(omega x x)_i] = (g'' + 4g'/r)(omega x x)_i   OK")

# ---------- B: soluciones homogeneas del operador radial ----------
Lop = lambda gg: sp.diff(gg, rr, 2) + 4 * sp.diff(gg, rr) / rr - mu**2 * gg
gK = sp.exp(-mu * rr) * (1 + mu * rr) / rr**3          # decae (tipo K_{3/2})
gI = (mu * rr * sp.cosh(mu * rr) - sp.sinh(mu * rr)) / rr**3   # regular en 0 (tipo i_1)
assert sp.simplify(Lop(gK)) == 0 and sp.simplify(Lop(gI)) == 0
serie_gI = sp.series(gI, rr, 0, 2)
print("B: g_ext = e^(-mu r)(1+mu r)/r^3  y  g_reg = (mu r cosh - sinh)/r^3 resuelven")
print("   g'' + 4g'/r - mu^2 g = 0 ;  g_reg ~", serie_gI, " (regular en r=0)  OK")
print("   limite mu->0 de g_ext:", sp.limit(gK, mu, 0), " (el 1/r^3 de RG)")

# ---------- C: esfera uniforme, matching exacto ----------
# Ecuacion: g'' + 4g'/r - mu^2 g = s(r),  s = 16 pi Gtilde rho(r)
# (normalizacion RG: A nabla^2 S = tau con A=M_Pl^2=1/16 pi G => s=16 pi G rho)
Gt = sp.Symbol('Gtilde', positive=True)
s0 = 16 * sp.pi * Gt * rho0
b, c = sp.symbols('b c')
g_in = -s0 / mu**2 + b * gI          # particular constante + homogenea regular
g_out = c * gK
assert sp.simplify(Lop(g_in) - s0) == 0
m1 = sp.Eq(g_in.subs(rr, R), g_out.subs(rr, R))
m2 = sp.Eq(sp.diff(g_in, rr).subs(rr, R), sp.diff(g_out, rr).subs(rr, R))
sol = sp.solve([m1, m2], [b, c])
c_sol = sp.simplify(sol[c])
print("\nC: amplitud exterior c(mu) =", sp.simplify(c_sol))

# ---------- D: limite RG y cotejo con Kerr ----------
J = sp.Rational(8, 15) * sp.pi * rho0 * R**5 * w   # J = (2/5) M R^2 omega, M=(4/3)pi R^3 rho0
c_GR = sp.limit(c_sol, mu, 0)
print("D: c(mu->0) =", sp.simplify(c_GR), "  vs  -2 G J/omega =", sp.simplify(-2 * Gt * J / w))
assert sp.simplify(c_GR + 2 * Gt * J / w) == 0
print("   => exterior RG: S = -2G(J x x)/r^3 = +2G(x x J)/r^3 = KERR linealizado  OK")

# ---------- E: factor de forma de la fuente extensa ----------
# escribo c(mu) = -(2 Gtilde J / omega) * FF(mu R): FF -> 1 cuando mu R -> 0
FF = sp.simplify(-c_sol * w / (2 * Gt * J))
FF_y = sp.simplify(FF.subs(mu, sp.Symbol('y', positive=True) / R))
yy = sp.Symbol('y', positive=True)
print("\nE: factor de forma FF(y=mu R) =", sp.simplify(FF_y))
print("   serie:", sp.series(FF_y, yy, 0, 5))
for yv in [0.05, 0.11, 0.2, 0.36]:
    print(f"   FF({yv}) = {float(FF_y.subs(yy, yv)):.6f}")

print("\nRESULTADO: h_0i(x) exterior = 2 Gtilde (x x J)_i (1+mu r) e^(-mu r)/r^3 * FF(mu R)")
print("           con Gtilde = G M_Pl^2/(M_Pl^2+alpha),  mu^2 = m1^2/(M_Pl^2+alpha)")
