# Paso 1: EH cuadratico propio. Controles: tensor (signo/normalizacion), tadpole, forma canonica escalar, gauge.
import sympy as sp
from lib_eh import t, z, p, Mp2, build_L, zavg, EL

c = sp.cos(p*z); s = sp.sin(p*z)

# ---------- TENSOR ----------
gam = sp.Function('gamma')(t)
H = sp.zeros(4, 4); H[1, 2] = H[2, 1] = gam*c
L1T, L2T = build_L(H)
LT = zavg(L2T)
print("L_TT (avg, sin Mp2):", sp.simplify(LT))
# esperado (afirmado): (1/4)(gamdot^2 - p^2 gam^2) por Mp2, cinetico positivo
dif = sp.expand(LT - (sp.Rational(1, 4)*(sp.diff(gam, t)**2 - p**2*gam**2)))
elT = sp.simplify(EL(dif, gam))
print("EL(L_TT - claimed) == 0 ?", elT == 0)
print("tadpole tensor avg:", sp.simplify(zavg(L1T)))

# ---------- ESCALAR ----------
ph = sp.Function('phi')(t); B = sp.Function('B')(t)
ps = sp.Function('psi')(t); E = sp.Function('E')(t)
H = sp.zeros(4, 4)
H[0, 0] = 2*ph*c
H[0, 3] = H[3, 0] = -p*B*s
H[1, 1] = H[2, 2] = 2*ps*c
H[3, 3] = 2*ps*c - p**2*E*c
L1S, L2S = build_L(H)
LS = zavg(L2S)
print("tadpole escalar avg:", sp.simplify(zavg(L1S)))
psd = sp.diff(ps, t); Ed = sp.diff(E, t)
Lclaim = -3*psd**2 + p**2*ps**2 - 2*p**2*ph*ps - 2*p**2*B*psd + p**2*psd*Ed
dif = sp.expand(LS - Lclaim)
ok = all(sp.simplify(EL(dif, f)) == 0 for f in (ph, B, ps, E))
print("EL(L_EH_scalar - claimed) == 0 en los 4 campos ?", ok)
if not ok:
    for f in (ph, B, ps, E):
        print("  EL dif", f, "=", sp.simplify(EL(dif, f)))

# gauge puro: phi=Adot, B=Cdot+A, psi=0, E=2C con A(t),C(t) arbitrarias
A = sp.Function('A')(t); C = sp.Function('C')(t)
sub = {ph: sp.diff(A, t), B: sp.diff(C, t) + A, ps: sp.S(0), E: 2*C}
allz = True
for f in (ph, B, ps, E):
    ex = EL(Mp2*LS, f)
    ex = ex.subs(sub).doit()
    r = sp.simplify(ex)
    if r != 0:
        allz = False
        print("  gauge EL", f, "=", r)
print("gauge puro: 4 EOMs de EH se anulan ?", allz)

sp.pickle = None
# guardar L escalar para paso 2
with open(__file__.replace('run1_eh_checks.py', 'LS_scalar.txt'), 'w') as fo:
    fo.write(sp.srepr(LS))
print("LS guardado.")
