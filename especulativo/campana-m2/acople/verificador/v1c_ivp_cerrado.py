# Verificador adversarial - IVP causal NLO (alpha=0, kappa=beta): solucion cerrada contra las 4 EOMs.
# Rama con datos RG + medio en reposo (c0=0 => B=0): psi = psi* + (psiN-psi*) cos(Om t),
# phi = (4 Mp2 p^2 psi - M)/(2 m02), B=0, Edot = (6 - 4Mp2/beta) psidot / p^2.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'verificador-m2'))
import sympy as sp
from lib_eh import t, z, p, Mp2, zavg, EL

c = sp.cos(p*z); s = sp.sin(p*z)
m02, m12 = sp.symbols('m02 m12', positive=True)
be = sp.symbols('beta', real=True)
M = sp.symbols('M', positive=True)

ph = sp.Function('phi')(t); B = sp.Function('B')(t)
ps = sp.Function('psi')(t); E = sp.Function('E')(t)
psd = sp.diff(ps, t); Ed = sp.diff(E, t)

LEH = Mp2*(-3*psd**2 + p**2*ps**2 - 2*p**2*ph*ps - 2*p**2*B*psd + p**2*psd*Ed)
Lm = sp.Rational(1, 2)*m02*ph**2 + sp.Rational(1, 4)*m12*p**2*B**2
Kxx = 2*psd*c
Kzz = (2*psd - p**2*Ed)*c - 2*sp.diff(-p*B*s, z)
trK = 2*Kxx + Kzz
Ltot = LEH + Lm + zavg(sp.Rational(1, 4)*be*trK**2) + sp.Rational(1, 2)*ph*M

mu2 = m02/(2*Mp2)
psN = M/(4*Mp2*p**2)
psstar = (M/(4*Mp2))/(p**2 - mu2)
Om2 = -be*p**2*(2*Mp2*p**2 - m02)/(m02*(2*Mp2 - 3*be))   # derivado en v1b, esquina==acta
Om = sp.symbols('Omega', positive=True)

psi_sol = psstar + (psN - psstar)*sp.cos(Om*t)
phi_sol = (4*Mp2*p**2*psi_sol - M)/(2*m02)
E_sol = ((6*be - 4*Mp2)/(be*p**2))*(psi_sol - psN)   # Edot = (6-4Mp2/be) psidot/p^2, E(0)=0
cand = {ph: phi_sol, B: sp.S(0), ps: psi_sol, E: E_sol}

res = []
for f in (ph, B, ps, E):
    ex = EL(Ltot, f).subs(cand).doit()
    ex = sp.expand(ex.rewrite(sp.cos))
    ex = ex.subs(Om**2, Om2)  # solo potencias pares de Om aparecen
    ex = sp.simplify(sp.expand(ex))
    res.append(ex)
print("residuos 4 EOMs (solucion cerrada NLO):", res)

# ICs y amplitud
print("psi(0) - psiN =", sp.simplify(psi_sol.subs(t, 0) - psN),
      "; psidot(0) =", sp.simplify(sp.diff(psi_sol, t).subs(t, 0)),
      "; Edot(0) =", sp.simplify(sp.diff(E_sol, t).subs(t, 0)))
A_claim = psN*mu2/(p**2 - mu2)
print("amplitud (psi*-psiN) - claim =", sp.simplify((psstar - psN) - A_claim))

# gamma(t) = 1: Phi_obs = phi - d/dt(B - Edot/2) == psi ?
Phi_obs = phi_sol - sp.diff(0 - sp.diff(E_sol, t)/2, t)
difg = sp.simplify(sp.expand((Phi_obs - psi_sol).rewrite(sp.cos)).subs(Om**2, Om2))
print("Phi_obs - psi (gamma(t)=1, alpha=0) =", sp.simplify(difg))

# kappa->0: Delta Psi -> 0 (Newton eterno)  [beta->0 con Om2 -> 0: psi* - psiN no depende de beta...]
# el claim es: con kappa=0 la solucion causal es Newton para todo t; el modo NLO desaparece (Om2->0, A finita
# pero 1-cos(Om t) -> 0 puntualmente). Verifico limite de DeltaPsi a t fijo:
DPsi = (psstar - psN)*(1 - sp.cos(sp.sqrt(Om2)*t))
print("lim beta->0 DeltaPsi(t fijo) =", sp.limit(DPsi.subs({Mp2: 1, m02: 1, m12: 2, p: 2}), be, 0))

# banda de Jeans: Om2 < 0 para p^2 < mu2 (beta<0): chequeo de signo en la esquina
esq = {Mp2: 1, m02: 1, be: -sp.Rational(1, 100)}
print("esquina: Om2(p=0.5) =", sp.nsimplify(Om2.subs(esq).subs(p, sp.Rational(1, 2))),
      " (<0: Jeans/cosh), Om2(p=1) =", sp.nsimplify(Om2.subs(esq).subs(p, 1)), " (>0: oscila)")
# t_c = 1/Gamma_max con Gamma^2 max en p^2 = mu2/2: verifico analiticamente
pp = sp.symbols('pp', positive=True)
G2 = (-Om2).subs(p, sp.sqrt(pp))
pmax = sp.solve(sp.diff(G2, pp), pp)
print("p^2 que maximiza Gamma^2:", pmax, " (claim mu2/2 =", sp.simplify(mu2/2), ")")
G2max = sp.simplify(G2.subs(pp, mu2/2))
tc_claim = 4*Mp2**2/(sp.sqrt(-be)*sp.sqrt(m02))   # t_c = 4 Mp2^2/(sqrt|kappa| m0) en Mp2=1?  claim: 4 M_Pl^2/(sqrt|k| m0)
print("Gamma_max =", sp.simplify(sp.sqrt(G2max)), " 1/tc_claim =", sp.simplify(1/tc_claim))
print("ratio Gamma_max*tc_claim =", sp.simplify(sp.sqrt(G2max)*tc_claim), " (esperado ~1 salvo (1-3be/2Mp2)^(-1/2))")
