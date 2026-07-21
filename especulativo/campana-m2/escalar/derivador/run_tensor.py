"""Sector tensorial: h_ij TT, masa cero exacta (m2^2=0).
Control de maquinaria + confirmacion del graviton sin masa."""
import sympy as sp
from eh_lib import t, z, p, zavg, check_zavg, L12_of_ansatz, EL

c = sp.cos(p * z)

# Polarizacion cruz: h_xy = gam(t) cos(pz)
gam = sp.Function('gamma_x')(t)
H = sp.zeros(4, 4)
H[1, 2] = H[2, 1] = gam * c
L1d, L2d = L12_of_ansatz(H)
Lx = zavg(L2d)
print("check_zavg (cruz):", check_zavg(L2d))
print("L_tensor (cruz)  =", sp.simplify(Lx))
eq = EL(Lx, gam)
print("EL cruz:", sp.expand(eq))
w = sp.Symbol('omega')
g0 = sp.Symbol('g0')
ex = sp.exp(-sp.I * w * t)
eqw = sp.expand(eq.subs(gam, g0 * ex).doit() / ex)
print("dispersion cruz: ", sp.solve(sp.Eq(eqw, 0), w**2))

# Polarizacion mas: h_xx = -h_yy = gp(t) cos(pz)
gp = sp.Function('gamma_p')(t)
H2 = sp.zeros(4, 4)
H2[1, 1] = gp * c
H2[2, 2] = -gp * c
L1d2, L2d2 = L12_of_ansatz(H2)
Lp = zavg(L2d2)
print("L_tensor (mas)   =", sp.simplify(Lp))
eq2 = EL(Lp, gp)
gq = sp.Symbol('gq')
eqw2 = sp.expand(eq2.subs(gp, gq * ex).doit() / ex)
print("dispersion mas:  ", sp.solve(sp.Eq(eqw2, 0), w**2))
