# Verificador adversarial - NLO estatico (alpha,beta,sigma,rho_op) y causal NLO (IVP cerrado).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'verificador-m2'))
import sympy as sp
from lib_eh import t, z, p, Mp2, build_L, zavg, EL

c = sp.cos(p*z); s = sp.sin(p*z)
m02, m12 = sp.symbols('m02 m12', positive=True)
al, be, si, rh = sp.symbols('alpha beta sigma_op rho_op', real=True)
M = sp.symbols('M', positive=True)

ph = sp.Function('phi')(t); B = sp.Function('B')(t)
ps = sp.Function('psi')(t); E = sp.Function('E')(t)

# EH canonico re-verificado en v1a via build_L; lo reconstruyo aqui (identico al de run1, ya validado):
psd = sp.diff(ps, t); Ed = sp.diff(E, t)
LEH = Mp2*(-3*psd**2 + p**2*ps**2 - 2*p**2*ph*ps - 2*p**2*B*psd + p**2*psd*Ed)
Lm = sp.Rational(1, 2)*m02*ph**2 + sp.Rational(1, 4)*m12*p**2*B**2

# Kbar_ij = hij_dot - di h0j - dj h0i (modo): xx=yy=2 psid c ; zz=(2 psid - p^2 Ed + 2 p^2 B) c
Kxx = 2*psd*c
Kzz = (2*psd - p**2*Ed)*c - 2*sp.diff(-p*B*s, z)
KK = 2*Kxx**2 + Kzz**2
trK = 2*Kxx + Kzz
R3 = 4*p**2*ps*c   # R3 lineal para hij = 2 psi dij + didj E (E no entra: didj - lap se cancela)
LNLO = zavg(sp.Rational(1, 4)*(al*KK + be*trK**2) + sp.Rational(1, 4)*si*R3**2 + sp.Rational(1, 4)*rh*trK*R3)

# fuente estatica
Lint_s = sp.Rational(1, 2)*ph*M

# ---------- A. estatica con alpha,beta: nada cambia ----------
Lst = (LEH + Lm + zavg(sp.Rational(1, 4)*(al*KK + be*trK**2)) + Lint_s)
subs_st = {f: aa for f, aa in zip((ph, B, ps, E), sp.symbols('f0:4'))}
Lss = Lst.subs(subs_st).doit()
f0, f1, f2, f3 = [subs_st[f] for f in (ph, B, ps, E)]
print("[A] dL/dE =", sp.simplify(sp.diff(Lss, f3)))
sols = sp.solve([sp.diff(Lss, v) for v in (f0, f1, f2)], (f0, f1, f2), dict=True)[0]
mu2 = m02/(2*Mp2)
claimLO = (M/(4*Mp2))/(p**2 - mu2)
print("[A] con alpha,beta: B =", sols[f1], " phi-claimLO =", sp.simplify(sols[f0] - claimLO),
      " psi-phi =", sp.simplify(sols[f2] - sols[f0]))

# ---------- B. estatica con sigma, rho_op: gamma(p) ----------
Lst2 = (LEH + Lm + LNLO + Lint_s)
Lss2 = Lst2.subs(subs_st).doit()
sols2 = sp.solve([sp.diff(Lss2, v) for v in (f0, f1, f2)], (f0, f1, f2), dict=True)[0]
gam = sp.cancel(sols2[f2]/sols2[f0])
ser = sp.series(gam.subs({al: 0, be: 0}), p, 0, 6).removeO()
print("[B] gamma(p) serie =", sp.expand(ser))
print("[B] claim: 1 - 2*sigma p^2/Mp2 + rho^2 p^4/(Mp2 m12) ;  dif =",
      sp.simplify(sp.expand(ser - (1 - 2*si*p**2/Mp2 + rh**2*p**4/(Mp2*m12)))))
print("[B] B~ =", sp.simplify(sols2[f1].subs({al: 0, be: 0})), "  (claim: prop a rho_op p^2 psi)")
print("[B] B~/(rho_op p^2 psi~) =", sp.simplify(sols2[f1].subs({al: 0, be: 0})/(rh*p**2*sols2[f2].subs({al: 0, be: 0}))))

# ---------- C. causal NLO (alpha=0, kappa=beta<0): reduccion y solucion cerrada ----------
LtotC = (LEH + Lm + zavg(sp.Rational(1, 4)*be*trK**2) + Lint_s)
# phi y B auxiliares
solph = sp.solve(sp.diff(LtotC, ph), ph)[0]
print("[C] phi(psi) =", sp.simplify(solph))
LC = sp.expand(LtotC.subs(ph, solph))
solB = sp.solve(sp.diff(LC, B), B, dict=True)[0][B]
LC2 = sp.expand(LC.subs(B, solB))
# E ciclico: pi_E const
piE = sp.diff(LC2, Ed)
c0 = sp.symbols('c0')
solEd = sp.solve(sp.Eq(piE, c0), Ed)[0]
LC3 = sp.expand(LC2.subs(Ed, solEd))  # (Routhiano salvo c0*Ed; para la EOM de psi da igual? -> verifico EOM directa)
# EOM de psi sin atajos: sistema completo, sustituyo soluciones auxiliares en EL(psi)
elps = EL(LtotC, ps)
# elimino phi, B, Edd via: phi=solph, B=solB (y sus derivadas), Edd de d(piE)/dt = 0
Bt = sp.diff(solB, t)
piE_full = sp.diff(LtotC, Ed)
dpiE = sp.expand(sp.diff(piE_full, t))
Edd_sol = sp.solve(sp.Eq(dpiE.subs(ph, solph).doit(), 0), sp.Derivative(E, (t, 2)))[0]
ex = elps.subs(sp.Derivative(ph, (t, 2)), sp.diff(solph, t, 2)).subs(sp.Derivative(ph, t), sp.diff(solph, t)).subs(ph, solph)
ex = ex.subs(sp.Derivative(B, (t, 2)), sp.diff(solB, t, 2)).subs(sp.Derivative(B, t), sp.diff(solB, t)).subs(B, solB)
ex = sp.expand(ex.doit())
ex = ex.replace(sp.Derivative(E, (t, 3)), sp.diff(Edd_sol, t)).replace(sp.Derivative(E, (t, 2)), Edd_sol)
ex = sp.simplify(sp.expand(ex.doit()))
# despejo psi'' :
psdd = sp.solve(sp.Eq(ex, 0), sp.Derivative(ps, (t, 2)))
print("[C] psi'' =", sp.simplify(psdd[0]))
Om2 = -sp.simplify(sp.diff(psdd[0], ps))
print("[C] Omega^2 =", sp.factor(Om2))
eps = sp.symbols('epsilon', positive=True)
Om2_acta = eps*p**2*(2*p**2 - 1)/(2 + 3*eps)
print("[C] esquina (Mp2=1,m02=1,beta=-eps): Omega^2 - acta =",
      sp.simplify(Om2.subs({Mp2: 1, m02: 1, be: -eps}) - Om2_acta))
serO = sp.series(Om2.subs(be, eps*be), eps, 0, 2).removeO().subs(eps, 1)
print("[C] EFT O(beta): Omega^2 =", sp.expand(sp.simplify(serO)),
      "  claim (be/(2Mp2))p^2 - (be/m02)p^4:", sp.simplify(serO - (be*p**2/(2*Mp2) - be*p**4/m02)))
# punto fijo
psstar = sp.solve(sp.Eq(psdd[0], 0), ps)[0]
print("[C] psi* - estatica =", sp.simplify(psstar - claimLO))
# solucion cerrada del IVP psi(0)=psiN, psi'(0)=0: psi = psi* + (psiN-psi*)cos(Om t)
psN = M/(4*Mp2*p**2)
A_claim = psN*mu2/(p**2 - mu2)
print("[C] A = psi*-psiN - claim :", sp.simplify((psstar - psN) - A_claim))
