# -*- coding: utf-8 -*-
"""
COLUMNA A -- parte 3 (cierre): controles finos.

D1. Dispersion con TODOS los NLO (alpha,beta,sigma,rho_op) por la RUTA DEL DET
    (la valida cuando hay acoples de primera derivada, que rho_op introduce):
    cotejo contra la formula exacta de la acta SECTOR-ESCALAR-2026-07-21.
    (El chequeo C5d del script causal usaba una reduccion no apta para rho_op:
     este es el control correcto.)
D2. Forma factorizada y limpia de DPhi(t,p) del IVP NLO (alpha,beta) y chequeos:
    DPhi = (phi_stat - Phi_N) * [1 - cos(Om t) * Mp2(m0^2+2 al p^2)/(m0^2(Mp2+al))]
    DPsi = (phi_stat - Phi_N) * [1 - cos(Om t)]   (exacta)
    => con al=0 (kappa=beta): gamma(t) = 1 EXACTA incluso durante el crecimiento.
D3. Acrecion LO: Eddot = 2 psi_N (E = psi_N t^2): el medio cae libre (sincrono).
"""
import sympy as sp

t, z = sp.symbols('t z', real=True)
p = sp.symbols('p', positive=True)
Mp2 = sp.Symbol('Mpl2', positive=True)
m0s, m1s = sp.symbols('m0sq m1sq', positive=True)
al, be, si, rh = sp.symbols('alpha beta sigma rho_op', real=True)
rho0 = sp.Symbol('rho0', real=True)

phi = sp.Function('phi')(t)
B = sp.Function('B')(t)
psi = sp.Function('psi')(t)
E = sp.Function('Ef')(t)
fields = [phi, B, psi, E]
dpsi = sp.Derivative(psi, t); dE = sp.Derivative(E, t)

# LEH canonico (verificado en C0 del script causal contra sqrt(-g)R desde cero)
LEH_can = (-3 * dpsi**2 + p**2 * psi**2 - 2 * p**2 * phi * psi
           - 2 * p**2 * B * dpsi + p**2 * dpsi * dE)

# masas y NLO por modo (promedio z incluido; identico a colA_causal)
Xc = [t, sp.Symbol('x'), sp.Symbol('y'), z]
c = sp.cos(p * z)
H = sp.zeros(4, 4)
H[0, 0] = 2 * phi * c
H[0, 3] = H[3, 0] = sp.diff(B * c, z)
H[1, 1] = 2 * psi * c
H[2, 2] = 2 * psi * c
H[3, 3] = 2 * psi * c + sp.diff(E * c, (z, 2))

def zavg(expr):
    half = sp.Rational(1, 2)
    c_, s_ = sp.cos(p * z), sp.sin(p * z)
    e = sp.expand(expr).subs({c_**2: half, s_**2: half})
    e = sp.expand(e)
    return sp.Add(*[T for T in sp.Add.make_args(e) if not (T.has(c_) or T.has(s_))])

Lmass = sp.expand(zavg(sp.Rational(1, 4) * (
    m0s * H[0, 0]**2 + 2 * m1s * (H[0, 1]**2 + H[0, 2]**2 + H[0, 3]**2))))
Kb = sp.zeros(3, 3)
for a in range(3):
    for b in range(3):
        Kb[a, b] = (sp.diff(H[a + 1, b + 1], t)
                    - sp.diff(H[0, b + 1], Xc[a + 1])
                    - sp.diff(H[0, a + 1], Xc[b + 1]))
trK = sum(Kb[a, a] for a in range(3))
R3 = (sum(sp.diff(H[a + 1, b + 1], Xc[a + 1], Xc[b + 1])
          for a in range(3) for b in range(3))
      - sum(sp.diff(H[b + 1, b + 1], Xc[a + 1], Xc[a + 1])
            for a in range(3) for b in range(3)))
DLfull = sp.expand(zavg(sp.expand(
    sp.Rational(1, 4) * al * sum(Kb[a, b]**2 for a in range(3) for b in range(3))
    + sp.Rational(1, 4) * be * trK**2
    + sp.Rational(1, 4) * si * R3**2
    + sp.Rational(1, 4) * rh * trK * R3)))

def EL(L, f):
    e = sp.diff(L, f)
    for k in range(1, 5):
        d = sp.Derivative(f, (t, k))
        pl = sp.diff(L, d)
        if pl != 0:
            e += (-1)**k * sp.diff(pl, (t, k))
    return sp.expand(e)

# ---------- D1: dispersion completa por la ruta del det ----------
Ltot4 = sp.expand(Mp2 * LEH_can + Lmass + DLfull)
w = sp.Symbol('omega')
amps = sp.symbols('phi0 B0 psi0 E0')
ex = sp.exp(-sp.I * w * t)
repl = {f: a * ex for f, a in zip(fields, amps)}
eqs = [sp.expand(sp.simplify(EL(Ltot4, f).subs(repl).doit() / ex)) for f in fields]
M = sp.Matrix([[sp.expand(eq).coeff(a) for a in amps] for eq in eqs])
det = sp.factor(M.det())
roots = sp.solve(sp.Eq(det, 0), w**2)
w2nz = [r for r in roots if sp.simplify(r) != 0]
print("D1: raices omega^2 no nulas del det (todos los NLO):", len(w2nz))
kap = al + be
W2_acta4 = p**2 * (kap * (2 * p**2 - m0s) + p**2 * m0s * (rh**2 / 2 - 2 * kap * si)) \
    / (m0s * (-2 - al + 3 * be + al**2 + 3 * al * be))
if w2nz:
    dif = sp.simplify(w2nz[0].subs(Mp2, 1) - W2_acta4)
    print("D1: omega^2(det, Mp2=1) - formula exacta de la acta (esperado 0):", dif)
# de paso: det a LO (NLO=0), cotejo con la acta: -(Mpl^4 m0^2 m1^2/2) w^4 p^6
detLO = sp.factor(det.subs({al: 0, be: 0, si: 0, rh: 0}))
print("D1b: det LO =", detLO)
print("D1b: det LO - [-(Mp2^2 m0^2 m1^2/2) w^4 p^6 * (1/8)]:",
      sp.simplify(detLO + Mp2**2 * m0s * m1s * w**4 * p**6 / 16))

# ---------- D2: forma factorizada del IVP NLO (alpha, beta) ----------
DLab = DLfull.subs({si: 0, rh: 0})
Lsrc0 = sp.Rational(1, 2) * phi * rho0          # fuente estatica: zavg(1/2 h00 T00) = phi rho0/2
Ltot = sp.expand(Mp2 * LEH_can + Lmass + DLab + Lsrc0)
elphi = sp.expand(sp.diff(Ltot, phi))
elB = sp.expand(sp.diff(Ltot, B))
solc = sp.solve([elphi, elB], [phi, B], dict=True)[0]
Lred = sp.expand(sp.simplify(Ltot.subs(solc)))
eq1 = sp.expand(EL(Lred, psi)); eq2 = sp.expand(EL(Lred, E))
# control de estructura: sin psi', E' sueltos (sistema conservativo puro)
for eq in (eq1, eq2):
    assert sp.simplify(eq.coeff(sp.Derivative(psi, t))) == 0
    assert sp.simplify(eq.coeff(sp.Derivative(E, t))) == 0
D2psi, D2E = sp.Derivative(psi, (t, 2)), sp.Derivative(E, (t, 2))
soldd = sp.solve([eq1, eq2], [D2psi, D2E], dict=True)[0]
psidd = sp.expand(soldd[D2psi]); Edd = sp.expand(soldd[D2E])
W2 = sp.simplify(-psidd.coeff(psi))
psiN = rho0 / (4 * Mp2 * p**2)
phistat = rho0 / (2 * (2 * Mp2 * p**2 - m0s))
Om = sp.sqrt(W2)
psi_t = phistat + (psiN - phistat) * sp.cos(Om * t)
gpsi = sp.simplify(Edd.coeff(psi)); gc = sp.simplify(Edd - gpsi * psi)
# integral manual (evita Piecewise): Edot(0)=0
Edot_t = (gpsi * phistat + gc) * t + gpsi * (psiN - phistat) * sp.sin(Om * t) / Om
phi_t = sp.simplify(solc[phi].subs(psi, psi_t).doit())
B_t = solc[B].subs({sp.Derivative(psi, t): sp.diff(psi_t, t),
                    sp.Derivative(E, t): Edot_t})
Phi_obs_t = sp.simplify(phi_t - sp.diff(B_t, t) + sp.diff(Edot_t, t) / 2)
DPhi = sp.simplify(Phi_obs_t - psiN)
DPsi = sp.simplify(psi_t - psiN)

DPhi_fact = (phistat - psiN) * (1 - sp.cos(Om * t) * Mp2 * (m0s + 2 * al * p**2)
                                / (m0s * (Mp2 + al)))
print("\nD2a: DPhi - forma factorizada (esperado 0):", sp.simplify(DPhi - DPhi_fact))
DPsi_fact = (phistat - psiN) * (1 - sp.cos(Om * t))
print("D2b: DPsi - (phi_stat - Phi_N)(1 - cos Om t) (esperado 0):",
      sp.simplify(DPsi - DPsi_fact))
print("D2c: con al=0: DPhi - DPsi (esperado 0 => gamma(t)=1 exacta):",
      sp.simplify((DPhi - DPsi).subs(al, 0)))
gam_dev = sp.simplify((DPhi - DPsi).subs(be, 0))
lam = sp.Symbol('lam')
gam_ser = sp.series(gam_dev.subs(al, lam * al), lam, 0, 2).removeO().subs(lam, 1)
print("D2d: (DPhi-DPsi) con be=0, lineal en alpha:", sp.simplify(gam_ser))

# amplitud de la correccion (identidad estatica)
amp = sp.simplify(phistat - psiN)
print("D2e: amplitud phi_stat - Phi_N =", amp,
      " = Phi_N * mu^2/(p^2-mu^2), mu^2=m0^2/(2Mp2):",
      sp.simplify(amp - psiN * (m0s / (2 * Mp2)) / (p**2 - m0s / (2 * Mp2))))

# ---------- D3: acrecion LO ----------
print("\nD3: a LO (kappa->0) el modo se congela y Eddot -> ", end="")
Edd_LO = sp.simplify(Edd.subs({al: 0, be: 0}).subs(psi, psiN))
print(Edd_LO, " = 2 psi_N?", sp.simplify(Edd_LO - 2 * psiN) == 0,
      " (E = psi_N t^2: caida libre del medio, estiramiento secular sincrono)")
print("\nFIN colA_cierre")
