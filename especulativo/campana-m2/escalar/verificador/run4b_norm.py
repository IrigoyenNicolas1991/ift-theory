# Paso 4b: factor de normalizacion EH de Dubovsky (86)/(85) vs canonico; y control RG puro escalar.
import sympy as sp
from lib_eh import t, z, p, Mp2, zavg, EL

w = sp.symbols('omega', real=True)
r = sp.symbols('r', positive=True)
tau = sp.Function('tau')(t); sig = sp.Function('sigmaD')(t)
vD = sp.Function('v')(t); psD = sp.Function('psiD')(t)
d2 = -p**2

# EH de su (86) con prefactor r*Mp2 en lugar de MpD:
L86_EH = (r*Mp2/2)*(4*(psD - 2*sp.diff(vD, t) + sp.diff(sig, (t, 2)))*d2*tau
                    + 6*tau*sp.diff(tau, (t, 2)) - 2*tau*d2*tau)
# mi EH canonico (paso 1) sin promediar (x2), en variables de Dubovsky (tau=2psi, psiD=2phi, v=B, sigma=E)
LEH_can = 2*Mp2*(-3*sp.diff(tau/2, t)**2 + p**2*(tau/2)**2 - 2*p**2*(psD/2)*(tau/2)
                 - 2*p**2*vD*sp.diff(tau/2, t) + p**2*sp.diff(tau/2, t)*sp.diff(sig, t))
dif = sp.expand(L86_EH - LEH_can)
sols = set()
for f in (tau, sig, vD, psD):
    ex = sp.simplify(sp.together(EL(dif, f)))
    if ex != 0:
        ss = sp.solve(ex, r)
        sols.update([sp.simplify(x) for x in ss])
        print("EL dif en", f, "-> r =", ss)
print("valores de r que igualan (86)EH al canonico:", sols)

# ---------- control RG puro escalar (m0=m1=0, sin NLO): det == 0, rango 2 ----------
c = sp.cos(p*z)
ph = sp.Function('phi')(t); B = sp.Function('B')(t)
ps = sp.Function('psi')(t); E = sp.Function('E')(t)
psd = sp.diff(ps, t); Ed = sp.diff(E, t)
LEH = Mp2*(-3*psd**2 + p**2*ps**2 - 2*p**2*ph*ps - 2*p**2*B*psd + p**2*psd*Ed)
fields = [ph, B, ps, E]; amps = sp.symbols('a0:4')
sub = {f: a*sp.exp(sp.I*w*t) for f, a in zip(fields, amps)}
eqs = [sp.expand(EL(LEH, f).subs(sub).doit()/sp.exp(sp.I*w*t)) for f in fields]
M = sp.Matrix([[ex.coeff(a) for a in amps] for ex in eqs])
print("RG puro escalar: det =", sp.simplify(M.det()), " rango =", M.rank())
