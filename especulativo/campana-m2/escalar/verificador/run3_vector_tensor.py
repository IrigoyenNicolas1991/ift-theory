# Paso 3: vector (S,F) y tensor con NLO, desde mi propio pipeline EH.
import sympy as sp
from lib_eh import t, z, p, Mp2, build_L, zavg, EL

c = sp.cos(p*z); s = sp.sin(p*z)
m12 = sp.symbols('m12', real=True)
al = sp.symbols('alpha', real=True)
w = sp.symbols('omega', real=True)

S = sp.Function('S')(t); F = sp.Function('F')(t)
H = sp.zeros(4, 4)
H[0, 1] = H[1, 0] = S*c          # h_{0x} = S cos(pz)
H[1, 3] = H[3, 1] = -p*F*s       # h_{xz} = dz(F cos(pz))
L1V, L2V = build_L(H)
LV_EH = Mp2*zavg(L2V)
print("tadpole vector:", sp.simplify(zavg(L1V)))
print("L_EH vector avg =", sp.simplify(LV_EH))

# masas: (1/4)*2*m1^2*h0i^2
Lm = zavg(sp.Rational(1, 2)*m12*(S*c)**2)
# NLO alpha: Kbar_xz = dt h_xz - dz h_0x = -p Fdot s + p S s ; dos componentes (xz,zx)
Kxz = sp.diff(-p*F*s, t) - sp.diff(S*c, z)
LNLO = zavg(sp.Rational(1, 4)*al*2*Kxz**2)
Ltot = sp.expand(LV_EH + Lm + LNLO)

fields = [S, F]; amps = sp.symbols('b0:2')
sub = {f: a*sp.exp(sp.I*w*t) for f, a in zip(fields, amps)}
eqs = [sp.expand((EL(Ltot, f).subs(sub).doit())/sp.exp(sp.I*w*t)) for f in fields]
M = sp.Matrix([[ex.coeff(a) for a in amps] for ex in eqs])
det = sp.factor(sp.simplify(M.det()))
print("det vector =", det)
claim = (m12/4)*w**2*p**2*(Mp2 + al)
print("ratio det/claim:", sp.simplify(det/claim))

# reduccion: S auxiliar
solS = sp.solve(sp.diff(Ltot, S), S)[0]
Lred = sp.simplify(sp.expand(Ltot.subs(S, solS)))
print("L_red vector =", Lred)
Fd = sp.diff(F, t)
claimred = (m12*(Mp2 + al)*p**2/(4*((Mp2 + al)*p**2 + m12)))*Fd**2
print("L_red - claim == 0 ?", sp.simplify(Lred - claimred) == 0)

# RG puro vector (m1=0, al=0): rango
M0 = M.subs({m12: 0, al: 0})
print("rango RG puro vector:", M0.rank())

# ---------- tensor NLO ----------
gam = sp.Function('gamma')(t)
Ht = sp.zeros(4, 4); Ht[1, 2] = Ht[2, 1] = gam*c
_, L2T = build_L(Ht)
LT = Mp2*zavg(L2T)
Kxy = sp.diff(gam*c, t)
LTn = sp.expand(LT + zavg(sp.Rational(1, 4)*al*2*Kxy**2))
elT = EL(LTn, gam)
g0 = sp.symbols('g0')
ex = sp.expand(elT.subs(gam, g0*sp.exp(sp.I*w*t)).doit()/sp.exp(sp.I*w*t)).coeff(g0)
w2T = sp.solve(ex, w**2)[0]
print("tensor w2 con NLO =", sp.simplify(w2T), " (claim Mp2*p^2/(Mp2+alpha))")
