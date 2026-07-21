"""Sector vectorial (LO y NLO) + tensor con NLO + esquina numerica escalar.
Vector: h_0x = S(t) cos(pz), h_xz = d_z(F(t) cos(pz))  (transverso, pol x).
Masa: (1/4) 2 m1^2 h_0i h_0i -> m1^2 S^2/4.  NLO: alpha (K_ij tipo), beta y
sigma no tocan el vector (trK_vec = 0, R3_vec = 0; se verifica).
"""
import sympy as sp
from eh_lib import t, z, x, y, p, X, zavg, check_zavg, L12_of_ansatz, EL

Mp2 = sp.Symbol('Mpl2', positive=True)
m0s, m1s = sp.symbols('m0sq m1sq', real=True)
al, be, si = sp.symbols('alpha beta sigma', real=True)

S = sp.Function('S')(t)
F = sp.Function('F')(t)
c = sp.cos(p * z)

H = sp.zeros(4, 4)
H[0, 1] = H[1, 0] = S * c
H[1, 3] = H[3, 1] = sp.diff(F * c, z)

L1d, L2d = L12_of_ansatz(H)
print("check_zavg vector:", check_zavg(L2d))
LEHv = sp.expand(zavg(L2d))
print("L_EH vector =", sp.simplify(LEHv))

# masa
Lmassv = sp.expand(zavg(sp.Rational(1, 4) * 2 * m1s
                        * (H[0, 1]**2 + H[0, 2]**2 + H[0, 3]**2)))
print("L_masa vector =", Lmassv)

# NLO
Kb = sp.zeros(3, 3)
for a in range(3):
    for b in range(3):
        Kb[a, b] = (sp.diff(H[a + 1, b + 1], t)
                    - sp.diff(H[0, b + 1], X[a + 1])
                    - sp.diff(H[0, a + 1], X[b + 1]))
trK = sum(Kb[a, a] for a in range(3))
R3 = (sum(sp.diff(H[a + 1, b + 1], X[a + 1], X[b + 1])
          for a in range(3) for b in range(3))
      - sum(sp.diff(H[b + 1, b + 1], X[a + 1], X[a + 1])
            for a in range(3) for b in range(3)))
print("trK vector (esperado 0):", sp.simplify(trK))
print("R3 vector (esperado 0):", sp.simplify(R3))
DLv = sp.expand(zavg(sp.Rational(1, 4) * al
                     * sum(Kb[a, b]**2 for a in range(3) for b in range(3))))
print("DL_alpha vector =", sp.simplify(DLv))

Ltot = sp.expand(Mp2 * LEHv + Lmassv + DLv)

w = sp.Symbol('omega')
S0, F0 = sp.symbols('S0 F0')
ex = sp.exp(-sp.I * w * t)
repl = {S: S0 * ex, F: F0 * ex}
eqs = [sp.expand(sp.simplify(EL(Ltot, f).subs(repl).doit() / ex)) for f in [S, F]]
M = sp.Matrix([[sp.expand(eq).coeff(a) for a in [S0, F0]] for eq in eqs])
det = sp.factor(M.det())
print("det vector =", det)
print("raices omega^2 vector:", sp.solve(sp.Eq(det, 0), w**2))

# reduccion: S auxiliar
assert sp.diff(Ltot, sp.Derivative(S, t)) == 0
elS = sp.diff(Ltot, S)
solS = sp.solve(elS, S)[0]
print("S resuelto =", sp.simplify(solS))
Lredv = sp.simplify(sp.expand(Ltot.subs(S, solS)))
print("L_red vector =", Lredv)

# control RG puro vector
det0 = sp.factor(det.subs({m1s: 0, al: 0}))
print("det vector RG puro:", det0, " (rango:",
      M.subs({m1s: 0, al: 0}).rank(), ")")

# --- tensor con NLO alpha (masa cero protegida) ---
gam = sp.Function('gamma_x')(t)
H2 = sp.zeros(4, 4)
H2[1, 2] = H2[2, 1] = gam * c
L1t, L2t = L12_of_ansatz(H2)
Kb2 = sp.zeros(3, 3)
for a in range(3):
    for b in range(3):
        Kb2[a, b] = (sp.diff(H2[a + 1, b + 1], t)
                     - sp.diff(H2[0, b + 1], X[a + 1])
                     - sp.diff(H2[0, a + 1], X[b + 1]))
trK2 = sum(Kb2[a, a] for a in range(3))
R32 = (sum(sp.diff(H2[a + 1, b + 1], X[a + 1], X[b + 1])
           for a in range(3) for b in range(3))
       - sum(sp.diff(H2[b + 1, b + 1], X[a + 1], X[a + 1])
             for a in range(3) for b in range(3)))
print("trK tensor (esperado 0):", sp.simplify(trK2))
print("R3 tensor (esperado 0):", sp.simplify(R32))
DLt = sp.expand(zavg(sp.Rational(1, 4) * al
                     * sum(Kb2[a, b]**2 for a in range(3) for b in range(3))
                     + sp.Rational(1, 4) * si * R32**2))
Ltt = sp.expand(Mp2 * zavg(L2t) + DLt)
g0 = sp.Symbol('g0')
eqt = sp.expand(sp.simplify(EL(Ltt, gam).subs(gam, g0 * ex).doit() / ex))
print("dispersion tensor con NLO:", sp.solve(sp.Eq(eqt, 0), w**2))

# --- esquina escalar (m0^2, m1^2) = (1, 2), Mpl2 = 1 ---
print()
print("== esquina (m0^2,m1^2)=(1,2), Mpl=1, NLO representativo beta=-eps ==")
epsn = sp.Symbol('epsilon_n', positive=True)
num = p**2 * (2 * Mp2**2 * al * p**2 + 2 * Mp2**2 * be * p**2
              - Mp2 * al * m0s - Mp2 * be * m0s
              - 2 * al * m0s * p**2 * si - 2 * be * m0s * p**2 * si
              + m0s * p**2 * sp.Symbol('rho')**2 / 2)
den = m0s * (-2 * Mp2**2 - Mp2 * al + 3 * Mp2 * be + al**2 + 3 * al * be)
w2 = num / den
subs_corner = {m0s: 1, m1s: 2, Mp2: 1, al: 0, be: -epsn, si: 0,
               sp.Symbol('rho'): 0}
w2c = sp.simplify(w2.subs(subs_corner))
print("omega^2(p) esquina =", sp.factor(w2c))
Kc = sp.simplify(((-2 * Mp2**2 - Mp2 * al + 3 * Mp2 * be + al**2 + 3 * al * be)
                  / (al + be)).subs(subs_corner))
print("K esquina =", Kc)
for ev, pv in [(sp.Rational(1, 10), sp.Rational(1, 2)),
               (sp.Rational(1, 10), 1),
               (sp.Rational(1, 10), 2)]:
    print(f"  eps={ev}, p={pv}: omega^2 =",
          sp.nsimplify(w2c.subs({epsn: ev, p: pv})),
          "=", float(w2c.subs({epsn: ev, p: pv})),
          " K =", float(Kc.subs(epsn, ev)))
