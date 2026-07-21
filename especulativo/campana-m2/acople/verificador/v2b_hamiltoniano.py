# Verificador adversarial - [4bis] Hamiltoniano vectorial: claim en la forma canonica de la campania
# + energia de Noether en MI forma cruda (EH sin IBP) para chequear robustez del ordenamiento.
import sys, os
# fix 2026-07-21: la lib vive en escalar/verificador (en la sesion original de la campana estaba en una carpeta 'verificador-m2/' que no entro al repo)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'escalar', 'verificador'))
import sympy as sp
from lib_eh import t, z, p, Mp2, build_L, zavg, EL

c = sp.cos(p*z); s = sp.sin(p*z)
m12 = sp.symbols('m12', positive=True)
al = sp.symbols('alpha', real=True)
A = Mp2 + al
S = sp.Function('S')(t); F = sp.Function('F')(t)
tc = sp.symbols('tau_c', positive=True)
Fd = sp.diff(F, t)
sig = S - Fd

# ---------- forma canonica de la campania ----------
Lc = A*p**2*sig**2/4 + m12*S**2/4 + S*tc/2
pi_c = sp.diff(Lc, Fd)
piv, Sv, Fdv = sp.symbols('piv Sv Fdv')
pi_sym = pi_c.subs({S: Sv, Fd: Fdv})
Fd_of = sp.solve(sp.Eq(pi_sym, piv), Fdv)[0]
Hh = sp.expand(piv*Fd_of - Lc.subs({S: Sv, Fd: Fdv}).subs(Fdv, Fd_of))
solSv = sp.solve(sp.diff(Hh, Sv), Sv)[0]
Hred = sp.simplify(Hh.subs(Sv, solSv))
Hclaim = (2*piv - tc)**2/(4*m12) + piv**2/(A*p**2)
print("[4] H(pi) - claim =", sp.simplify(Hred - Hclaim))
print("[4] S(pi) =", sp.simplify(solSv), " (claim (2pi-tau)/m12)")
pimin = sp.solve(sp.diff(Hred, piv), piv)[0]
print("[4] pi_min =", sp.simplify(pimin), " S_min =", sp.simplify(solSv.subs(piv, pimin)),
      " Fdot_min =", sp.simplify(Fd_of.subs({piv: pimin, Sv: solSv.subs(piv, pimin)})))
# estados: retardada S=0, Fdot=tc/(A p^2) => pi_ret = pi_c en ese estado
pi_ret = pi_c.subs({S: 0, Fd: tc/(A*p**2)})
print("[4] pi_ret =", sp.simplify(pi_ret), " (claim tau/2)")
Hret = sp.simplify(Hred.subs(piv, pi_ret))
Hmin = sp.simplify(Hred.subs(piv, pimin))
print("[4] H_ret =", Hret, " H_min =", Hmin)
print("[4] H_ret - H_min =", sp.factor(Hret - Hmin), " (claim > 0)")
num = {Mp2: 1, al: 0, p: 1, m12: sp.Rational(1, 10), tc: 1}
print("[4] modo test: H_ret =", float(Hret.subs(num)), " H_min =", float(Hmin.subs(num)),
      " (claim 0.250 vs 0.227)")

# ---------- energia de Noether en la forma cruda (build_L, sin IBP) ----------
H4 = sp.zeros(4, 4)
H4[0, 1] = H4[1, 0] = S*c
H4[1, 3] = H4[3, 1] = -p*F*s
_, L2V = build_L(H4)
LEH_raw = Mp2*zavg(L2V)
Kxz = sp.diff(-p*F*s, t) - sp.diff(S*c, z)
Lraw = sp.expand(LEH_raw + zavg(sp.Rational(1, 4)*al*2*Kxz**2) + zavg(sp.Rational(1, 2)*m12*(S*c)**2)
                 + sp.Rational(1, 2)*S*tc)
print("\n[raw] L cruda =", sp.simplify(Lraw))
def noether_E(L, qs):
    Ee = -L
    for q in qs:
        q1 = sp.Derivative(q, t); q2 = sp.Derivative(q, (t, 2))
        Ee += q1*sp.diff(L, q1)
        if L.has(q2):
            Ee += q2*sp.diff(L, q2) - q1*sp.diff(sp.diff(L, q2), t)
    return sp.expand(Ee)
Eraw = noether_E(Lraw, (S, F))
Ecan = noether_E(Lc, (S, F))
st_ret = {S: sp.S(0), F: tc*t/(A*p**2)}
st_gnd = {S: -tc/(A*p**2 + m12), F: sp.S(0)}
for nom, st in (("retardada", st_ret), ("fundamental", st_gnd)):
    er = sp.simplify(Eraw.subs(st).doit())
    ec = sp.simplify(Ecan.subs(st).doit())
    print(f"[raw] E({nom}): cruda = {er} ; canonica = {ec}")
