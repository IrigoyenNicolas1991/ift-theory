# Paso 2: sector escalar completo con masas + NLO. Ruta A (det 4x4) y Ruta B (reduccion).
import sympy as sp
from lib_eh import t, z, p, Mp2, zavg, EL

c = sp.cos(p*z); s = sp.sin(p*z)
m02, m12 = sp.symbols('m02 m12', real=True)
al, be, si, rh = sp.symbols('alpha beta sigma rho', real=True)
w = sp.symbols('omega', real=True)

ph = sp.Function('phi')(t); B = sp.Function('B')(t)
ps = sp.Function('psi')(t); E = sp.Function('E')(t)
psd = sp.diff(ps, t); Ed = sp.diff(E, t)

# EH canonico (verificado en paso 1 contra derivacion primera-principios propia)
LEH = Mp2*(-3*psd**2 + p**2*ps**2 - 2*p**2*ph*ps - 2*p**2*B*psd + p**2*psd*Ed)

# Masas (promedio en z hecho a mano y verificado abajo con la integral)
h00 = 2*ph*c; h0z = -p*B*s
Lm_int = zavg(sp.Rational(1, 4)*(m02*h00**2 + 2*m12*h0z**2))
Lm_hand = sp.Rational(1, 2)*m02*ph**2 + sp.Rational(1, 4)*m12*p**2*B**2
print("masas avg ok:", sp.simplify(Lm_int - Lm_hand) == 0)

# NLO: Kbar_ij = hij_dot - di h0j - dj h0i ; R3lin = 4 p^2 psi
hxx = 2*ps*c; hzz = 2*ps*c - p**2*E*c
Kxx = sp.diff(hxx, t); Kyy = Kxx
Kzz = sp.diff(hzz, t) - 2*sp.diff(h0z, z)
KK = Kxx**2 + Kyy**2 + Kzz**2
trK = Kxx + Kyy + Kzz
R3 = 4*p**2*ps*c
LNLO = zavg(sp.Rational(1, 4)*(al*KK + be*trK**2) + sp.Rational(1, 4)*si*R3**2 + sp.Rational(1, 4)*rh*trK*R3)
print("LNLO =", sp.simplify(LNLO))

Ltot = sp.expand(LEH + Lm_int + LNLO)

# ---------- RUTA A: det ----------
fields = [ph, B, ps, E]
amps = sp.symbols('a0:4')
subs_mode = {}
for f, a in zip(fields, amps):
    subs_mode[f] = a*sp.exp(sp.I*w*t)
eqs = []
for f in fields:
    ex = EL(Ltot, f)
    ex = ex.subs(subs_mode).doit()
    ex = sp.expand(ex/sp.exp(sp.I*w*t))
    eqs.append(ex)
M = sp.zeros(4, 4)
for i, ex in enumerate(eqs):
    for j, a in enumerate(amps):
        M[i, j] = sp.expand(ex.coeff(a))
det = sp.factor(sp.simplify(M.det()))
print("det 4x4 =", det)

detLO = sp.factor(det.subs({al: 0, be: 0, si: 0, rh: 0}))
print("det LO =", detLO)
claimLO = -Mp2**2*m02*m12*w**4*p**6/2
print("ratio det LO / claim:", sp.simplify(detLO/claimLO))

# raiz no nula del det NLO
poly = sp.Poly(sp.expand(det), w)
# det = w^2 * (A w^2 + C)  (esperado); extraigo
detw2 = sp.factor(sp.cancel(det/w**2))
pol2 = sp.Poly(sp.expand(detw2), w)
A2 = pol2.coeff_monomial(w**2)
C0 = pol2.coeff_monomial(1)
print("grado en w del det/w^2:", pol2.degree())
w2root = sp.simplify(-C0/A2)
print("raiz w^2 =", sp.simplify(w2root))

# comparo con la formula EXACTA afirmada
kap = al + be
w2claim = p**2*(kap*Mp2*(2*Mp2*p**2 - m02) + p**2*m02*(rh**2/2 - 2*kap*si)) / (m02*(-2*Mp2**2 - Mp2*al + 3*Mp2*be + al**2 + 3*al*be))
print("raiz - claim == 0 ?", sp.simplify(w2root - w2claim) == 0)

# ---------- RUTA B: reduccion ----------
solph = sp.solve(sp.diff(Ltot, ph), ph)[0]
print("phi_sol =", sp.simplify(solph))
L2 = sp.expand(Ltot.subs(ph, solph))
solB = sp.solve(sp.diff(L2, B), B)[0]
L3 = sp.expand(L2.subs(B, solB))
print("dL/dE == 0 ?", sp.simplify(sp.diff(L3, E)) == 0)
PiE = sp.diff(L3, Ed)
solEd = sp.solve(PiE, Ed)[0]
L4 = sp.expand(L3.subs(Ed, solEd))
K = sp.simplify(sp.diff(L4, psd, 2)/2)
Xt = sp.simplify(sp.diff(sp.diff(L4, psd), ps) - sp.diff(L4, psd, 2)*0)  # coef cruzado
cross = sp.simplify(L4 - K*psd**2 + sp.Rational(0))
V = -sp.simplify(sp.diff(L4, ps, 2)/2)
crossterm = sp.simplify(sp.expand(L4 - K*psd**2 + V*ps**2))
print("termino cruzado psi*psidot:", crossterm)
print("K =", sp.simplify(K))
Kclaim = (-2*Mp2**2 - Mp2*al + 3*Mp2*be + al**2 + 3*al*be)/(al + be)
print("K - K_claim == 0 ?", sp.simplify(K - Kclaim) == 0)
print("V/K - raizA == 0 ?", sp.simplify(V/K - w2root) == 0)

# ---------- LO: congelamiento ----------
L3LO = L3.subs({al: 0, be: 0, si: 0, rh: 0})
PiELO = sp.simplify(sp.diff(L3LO, Ed))
print("Pi_E en LO =", PiELO, " (si ~psidot => vinculo congela)")

# ---------- esquina ----------
esq = {Mp2: 1, m02: 1, m12: 2, al: 0, si: 0, rh: 0, be: -sp.Rational(1, 10)}
w2e = sp.simplify(w2root.subs(esq))
print("esquina w2(p) =", w2e)
for pv in [sp.Rational(1, 2), 1, 2]:
    print("  p =", pv, " w2 =", sp.nsimplify(w2e.subs(p, pv)))
print("K esquina =", sp.simplify(K.subs(esq)))
# limites
print("decoupling Mp->oo: w2 ->", sp.limit(w2root, Mp2, sp.oo))
ser = sp.series(w2root.subs(Mp2, 1), p, 0, 6).removeO()
print("serie p->0 (Mp=1):", sp.expand(ser))
