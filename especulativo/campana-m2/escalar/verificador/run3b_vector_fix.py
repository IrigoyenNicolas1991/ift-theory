# Paso 3b: comparar L_red vectorial modulo derivada total (test EL).
import sympy as sp
from lib_eh import t, z, p, Mp2, build_L, zavg, EL

c = sp.cos(p*z); s = sp.sin(p*z)
m12 = sp.symbols('m12', real=True)
al = sp.symbols('alpha', real=True)

S = sp.Function('S')(t); F = sp.Function('F')(t)
H = sp.zeros(4, 4)
H[0, 1] = H[1, 0] = S*c
H[1, 3] = H[3, 1] = -p*F*s
_, L2V = build_L(H)
LV_EH = Mp2*zavg(L2V)
Lm = zavg(sp.Rational(1, 2)*m12*(S*c)**2)
Kxz = sp.diff(-p*F*s, t) - sp.diff(S*c, z)
LNLO = zavg(sp.Rational(1, 4)*al*2*Kxz**2)
Ltot = sp.expand(LV_EH + Lm + LNLO)
solS = sp.solve(sp.diff(Ltot, S), S)[0]
print("S_sol =", sp.simplify(solS))
Lred = sp.expand(Ltot.subs(S, solS))
Fd = sp.diff(F, t)
claimred = (m12*(Mp2 + al)*p**2/(4*((Mp2 + al)*p**2 + m12)))*Fd**2
dif = sp.expand(Lred - claimred)
print("EL(L_red - claim, F) == 0 ?", sp.simplify(sp.together(EL(dif, F))) == 0)
