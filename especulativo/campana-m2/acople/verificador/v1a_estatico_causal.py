# Verificador adversarial - columnas A (estatico/PPN + causal LO), rehecho desde cero.
# Convencion (deducida de Phi=-phi, Psi=-psi, gamma=psi/phi): h00=2phi, h0i=di B, hij=2psi dij + didj E.
import sys, os
# fix 2026-07-21: la lib vive en escalar/verificador (en la sesion original de la campana estaba en una carpeta 'verificador-m2/' que no entro al repo)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'escalar', 'verificador'))
import sympy as sp
from lib_eh import t, z, p, Mp2, build_L, zavg, EL

c = sp.cos(p*z); s = sp.sin(p*z)
m02, m12 = sp.symbols('m02 m12', real=True)
M = sp.symbols('M', positive=True)

ph = sp.Function('phi')(t); B = sp.Function('B')(t)
ps = sp.Function('psi')(t); E = sp.Function('E')(t)
rho = sp.Function('rho')(t)

# ---------- 1. EH propio ----------
H = sp.zeros(4, 4)
H[0, 0] = 2*ph*c
H[0, 3] = H[3, 0] = -p*B*s
H[1, 1] = H[2, 2] = 2*ps*c
H[3, 3] = 2*ps*c - p**2*E*c
L1, L2 = build_L(H)
LEH = Mp2*zavg(L2)
print("[1] tadpole:", sp.simplify(zavg(L1)))

# ---------- 2. invariancia gauge de Phi_obs ----------
a = sp.Function('a')(t); b = sp.Function('b')(t)
dph, dB, dps, dE = sp.diff(a, t), a + sp.diff(b, t)/p, sp.S(0), 2*b/p
Phi_obs = lambda f, Bv, Ev: f - sp.diff(Bv - sp.diff(Ev, t)/2, t)
print("[2] delta Phi_obs =", sp.simplify(Phi_obs(dph, dB, dE)))
# y que la EOM de EH se anule sobre gauge puro (control del pipeline)
sub_g = {ph: dph, B: dB, ps: dps, E: dE}
okg = all(sp.simplify(EL(LEH, f).subs(sub_g).doit()) == 0 for f in (ph, B, ps, E))
print("[2] EH EOMs sobre gauge puro == 0 ?", okg)

# ---------- 3. masas + fuente conservada ----------
Lm = zavg(sp.Rational(1, 4)*(m02*(2*ph*c)**2 + 2*m12*(-p*B*s)**2))
T00 = rho*c
T0z = -(sp.diff(rho, t)/p)*s
Tzz = -(sp.diff(rho, (t, 2))/p**2)*c
# control conservacion
print("[3] dT^mu0 =", sp.simplify(sp.diff(T00, t) + sp.diff(T0z, z)),
      " dT^muz =", sp.simplify(sp.diff(T0z, t) + sp.diff(Tzz, z)))
Lint = zavg(sp.Rational(1, 2)*(H[0, 0]*T00 + 2*H[0, 3]*T0z + H[3, 3]*Tzz))
Ltot = sp.expand(LEH + Lm + Lint)

# ---------- 4. estatica eterna ----------
Ls = Ltot.subs(rho, M)
sub_static = {}
for f, aa in zip((ph, B, ps, E), sp.symbols('f0:4')):
    sub_static[f] = aa
Lss = Ls.subs(sub_static).doit()
f0, f1, f2, f3 = [sub_static[f] for f in (ph, B, ps, E)]
print("[4] dL/dE (estatica) =", sp.simplify(sp.diff(Lss, f3)), " (claim: identicamente 0)")
sols = sp.solve([sp.diff(Lss, v) for v in (f0, f1, f2)], (f0, f1, f2), dict=True)[0]
mu2 = m02/(2*Mp2)
claim = (M/(4*Mp2))/(p**2 - mu2)
print("[4] B =", sols[f1], "  phi-claim =", sp.simplify(sols[f0] - claim),
      "  psi-phi =", sp.simplify(sols[f2] - sols[f0]))
print("[4] gamma_PPN = psi/phi =", sp.simplify(sols[f2]/sols[f0]))
print("[4] limite RG (m0->0): phi =", sp.simplify(sols[f0].subs(m02, 0)), " (claim M/(4 Mp2 p^2))")

# ---------- 5. teorema causal LO ----------
psN = rho/(4*Mp2*p**2)
Edd = 2*psN + sp.diff(rho, (t, 2))/(Mp2*p**4)
cand = {ph: sp.S(0), B: sp.S(0), ps: psN}
def residuos(L):
    out = []
    for f in (ph, B, ps, E):
        ex = EL(L, f).subs(cand).doit()
        for k in (4, 3, 2):
            ex = ex.replace(sp.Derivative(E, (t, k)), sp.diff(Edd, t, k - 2))
        out.append(sp.simplify(ex))
    return out
print("[5] residuos EOMs masivas (candidato causal):", residuos(Ltot))
print("[5] residuos EOMs RG pura (mismo candidato):", residuos(sp.expand(LEH + Lint)))
print("[5] L_m on-shell =", sp.simplify(Lm.subs(cand).doit()))
# Bardeen del candidato: Phi_obs = Edd/2 = psN + rhodd/(2 Mp2 p^4); Psi_obs = psN
print("[5] Phi_obs - Psi_obs =", sp.simplify(Edd/2 - psN), " (claim rho''/(2 Mp2 p^4))")
