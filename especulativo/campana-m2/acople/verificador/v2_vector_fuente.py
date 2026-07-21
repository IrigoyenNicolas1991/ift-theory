# Verificador adversarial - columna B: vector con fuente rotante, desde cero.
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
tau = sp.Function('tau')(t)

# ---------- 1. EH vectorial propio ----------
H = sp.zeros(4, 4)
H[0, 1] = H[1, 0] = S*c
H[1, 3] = H[3, 1] = -p*F*s
L1, L2 = build_L(H)
LEH = Mp2*zavg(L2)
sig = S - sp.diff(F, t)
dif = sp.expand(LEH - Mp2*p**2*sig**2/4)
okEH = all(sp.simplify(sp.together(EL(dif, f))) == 0 for f in (S, F))
print("[1] tadpole:", sp.simplify(zavg(L1)), "; L_EH == (Mp2 p^2/4) sigma^2 (mod dt) ?", okEH)
Kxz = sp.diff(-p*F*s, t) - sp.diff(S*c, z)
print("[1] Kxz/s =", sp.simplify(Kxz/s), " (claim: -dz sigma => p*sigma en amplitud)")

# ---------- 2. L total con NLO alpha y fuente conservada ----------
LNLO = zavg(sp.Rational(1, 4)*al*2*Kxz**2)
Lm = zavg(sp.Rational(1, 2)*m12*(S*c)**2)
T0x = tau*c
Txz = -(sp.diff(tau, t)/p)*s
print("[2] conservacion dT^mux =", sp.simplify(sp.diff(T0x, t) + sp.diff(Txz, z)))
Lint = zavg(sp.Rational(1, 2)*(2*(S*c)*T0x + 2*(-p*F*s)*Txz))
print("[2] L_int =", sp.simplify(Lint), " (claim: S tau/2 + F taudot/2)")
Ltot = sp.expand(LEH + LNLO + Lm + Lint)
Lclaim = A*p**2*sig**2/4 + m12*S**2/4 + S*tau/2 + F*sp.diff(tau, t)/2
okL = all(sp.simplify(sp.together(EL(sp.expand(Ltot - Lclaim), f))) == 0 for f in (S, F))
print("[2] L_tot == claim (mod dt) ?", okL)

# ---------- 3. EOMs, ley de conservacion, dos ramas ----------
eqS = sp.expand(EL(Ltot, S))
eqF = sp.expand(EL(Ltot, F))
r3 = sp.simplify(eqS/(A*p**2/2*sig + m12*S/2 + tau/2))
print("[3] eqS / (A p^2 sigma/2 + m12 S/2 + tau/2) =", r3)
cons = A*p**2*sig + tau
r4 = sp.simplify(eqF/sp.diff(cons, t))
print("[3] eqF / d/dt[A p^2 sigma + tau] =", r4)
tc = sp.symbols('tau_c')
gs = {S: -tc/(A*p**2 + m12), F: sp.S(0)}
print("[3] fundamental: eqS =", sp.simplify(eqS.subs(tau, tc).subs(gs).doit()),
      " eqF =", sp.simplify(eqF.subs(tau, tc).subs(gs).doit()))
Fret = sp.integrate(tau/(A*p**2), t)
ret = {S: sp.S(0), F: Fret}
print("[3] retardada: eqS =", sp.simplify(eqS.subs(ret).doit()),
      " eqF =", sp.simplify(eqF.subs(ret).doit()),
      " sigma_ret =", sp.simplify(sig.subs(ret).doit()), " (= -tau/(A p^2))")
solS = sp.solve(sp.diff(Ltot, S), S)[0]
Lred = sp.expand(Ltot.subs(S, solS))
Fd = sp.diff(F, t)
Lred_claim = (m12*A*p**2/(4*(A*p**2 + m12)))*Fd**2
dif = sp.expand((Lred - Lred_claim).subs(tau, 0))
print("[3] L_red(sin fuente) == claim campania ?", sp.simplify(sp.together(EL(dif, F))) == 0)

# ---------- 4. Hamiltoniano y seleccion de estado (tau const) ----------
LtotH = Ltot.subs(tau, tc).doit()
pi = sp.diff(LtotH, Fd)
print("[4] pi =", sp.simplify(pi), " (claim -(A p^2/2) sigma)")
piv, Sv, Fdv = sp.symbols('piv Sv Fdv')
pi_sym = pi.subs({S: Sv, Fd: Fdv})
Fd_of = sp.solve(sp.Eq(pi_sym, piv), Fdv)[0]
Hh = sp.expand(piv*Fd_of - LtotH.subs({S: Sv, Fd: Fdv}).subs(Fdv, Fd_of))
solSv = sp.solve(sp.diff(Hh, Sv), Sv)[0]
Hred = sp.simplify(Hh.subs(Sv, solSv))
Hclaim = (2*piv - tc)**2/(4*m12) + piv**2/(A*p**2)
print("[4] H(pi) - claim =", sp.simplify(Hred - Hclaim))
pimin = sp.solve(sp.diff(Hred, piv), piv)[0]
Smin = sp.simplify(solSv.subs(piv, pimin))
sigmin = sp.simplify(-2*pimin/(A*p**2))
print("[4] minimo: S =", Smin, " Fdot = S - sigma =", sp.simplify(Smin - sigmin),
      " (claim S=-tau/(Ap^2+m12), Fdot=0)")
Hret = sp.simplify(Hred.subs(piv, tc/2))
Hmin = sp.simplify(Hred.subs(piv, pimin))
print("[4] H_ret - H_min =", sp.simplify(Hret - Hmin))
# fix 2026-07-21: A = Mp2 + al es una expresion, no un simbolo — subs con {A: 1} dejaba
# Mp2 y al libres y el float() de abajo moria. Mismo punto de test: Mp2=1, al=0 => A=1.
num = {Mp2: 1, al: 0, p: 1, m12: sp.Rational(1, 10), tc: 1}
print("[4] modo test: H_ret =", float(Hret.subs(num)), " H_min =", float(Hmin.subs(num)))

# ---------- 5. solucion radial Yukawa + esfera uniforme + Kerr ----------
r, mu, R = sp.symbols('r mu R', positive=True)
fk = (1 + mu*r)*sp.exp(-mu*r)/r**3
fi = (mu*r*sp.cosh(mu*r) - sp.sinh(mu*r))/r**3
op = lambda f: sp.diff(f, r, 2) + 4*sp.diff(f, r)/r - mu**2*f
print("[5] op(exterior k):", sp.simplify(op(fk)), "; op(interior i):", sp.simplify(op(fi)))
rho0 = sp.symbols('rho0', positive=True)
bb, cc = sp.symbols('b c')
g_in = -rho0/(A*mu**2) + bb*fi
g_out = cc*fk
solm = sp.solve([sp.Eq(g_in.subs(r, R), g_out.subs(r, R)),
                 sp.Eq(sp.diff(g_in, r).subs(r, R), sp.diff(g_out, r).subs(r, R))], (bb, cc), dict=True)[0]
cex = sp.simplify(solm[cc])
FFs = sp.simplify(15*(((mu*R)**2 + 3)*sp.sinh(mu*R) - 3*mu*R*sp.cosh(mu*R))/(mu*R)**5)
Jw = sp.Rational(8, 15)*sp.pi*rho0*R**5          # J/omega
claim_out = -2*(1/(16*sp.pi*A))*Jw*FFs           # amplitud g: h = g(r) (omega x x), Gt=1/(16 pi A)
print("[5] c_ext/claim(FF) =", sp.simplify(cex/claim_out))
print("[5] FF serie =", sp.series(FFs.subs(R, 1), mu, 0, 6))
print("[5] FF(0.11) =", float(FFs.subs({mu: sp.Rational(11, 100), R: 1})))
kerr = sp.simplify(sp.limit(cex, mu, 0))
print("[5] mu->0: c_ext + 2 Gt J/w =", sp.simplify(kerr + 2*(1/(16*sp.pi*A))*Jw), " (0 => Kerr exacto)")

# ---------- 6. Lense-Thirring ----------
x1, x2, x3 = sp.symbols('x1 x2 x3', real=True)
J1, J2, J3 = sp.symbols('J1 J2 J3', real=True)
rr = sp.sqrt(x1**2 + x2**2 + x3**2)
f = sp.Function('f')
X = sp.Matrix([x1, x2, x3]); J = sp.Matrix([J1, J2, J3])
h = (X.cross(J)).applyfunc(lambda e_: e_*f(rr))
def curl(V):
    return sp.Matrix([sp.diff(V[2], x2) - sp.diff(V[1], x3),
                      sp.diff(V[0], x3) - sp.diff(V[2], x1),
                      sp.diff(V[1], x1) - sp.diff(V[0], x2)])
Bv = curl(h)
rhat = X/rr
# fix 2026-07-21: Derivative(f(rr), rr) con rr compuesto no es valido en sympy — se
# deriva respecto de un simbolo auxiliar y se sustituye (misma identidad, misma f generica).
r_aux = sp.symbols('r_aux', positive=True)
fp_rr = sp.diff(f(r_aux), r_aux).subs(r_aux, rr)
Bclaim = -(2*f(rr) + rr*fp_rr)*J + (rr*fp_rr)*(J.dot(rhat))*rhat
print("[6] B - Bclaim =", list(sp.simplify(sp.expand(Bv - Bclaim))))
# promedio orbital con Bclaim evaluado en la orbita (identidad ya verificada)
th, i_ = sp.symbols('theta iota', real=True)
av, Om = sp.symbols('a_orb Omega_orb', positive=True)
e1 = sp.Matrix([1, 0, 0]); e2 = sp.Matrix([0, sp.cos(i_), sp.sin(i_)])
n = e1.cross(e2)
pos = av*(sp.cos(th)*e1 + sp.sin(th)*e2)
vel = av*Om*(-sp.sin(th)*e1 + sp.cos(th)*e2)
fa, fpa = sp.symbols('f_a fp_a')
Borb = -(2*fa + av*fpa)*J + (av*fpa)*(J.dot(pos)/av)*(pos/av)
dL = pos.cross(vel.cross(Borb))
dLav = sp.simplify((1/(2*sp.pi))*sp.Matrix([sp.integrate(dL[k], (th, 0, 2*sp.pi)) for k in range(3)]))
claimv = fa*(J.cross(n))
dif6 = sp.simplify(dLav/(av**2*Om) - claimv)
print("[6] <n_dot> - f(a)(J x n) =", list(dif6), " (0 => Omega_nodo = f(a) J, inclinacion arbitraria)")
xx = sp.symbols('x', positive=True)
print("[6] serie S_nodo (1+x)e^-x:", sp.series((1 + xx)*sp.exp(-xx), xx, 0, 4))
# GP-B: orbita polar (i=pi/2), J=(0,0,J3) en el plano orbital; <Omega_gyro> = <-B/2>
Bpol = Borb.subs({i_: sp.pi/2, J1: 0, J2: 0})
avg = sp.simplify(-sp.Rational(1, 2)*(1/(2*sp.pi))*sp.Matrix([sp.integrate(Bpol[k], (th, 0, 2*sp.pi)) for k in range(3)]))
print("[6] <Omega_gyro> =", list(avg), " (claim: (f + a f'/4) J3 en z)")
print("[6]   dif z:", sp.simplify(avg[2] - (fa + av*fpa/4)*J3))
Gt = sp.symbols('Gtilde', positive=True)
fY = 2*Gt*(1 + mu*av)*sp.exp(-mu*av)/av**3
SGPB = sp.simplify((fY + av*sp.diff(fY, av)/4)/(Gt/(2*av**3)))
print("[6] S_GPB =", sp.factor(SGPB), " (claim (1+x-x^2)e^{-x}, x=mu a)")
print("[6] serie S_GPB:", sp.series(SGPB.subs(av, xx/mu), xx, 0, 4))
