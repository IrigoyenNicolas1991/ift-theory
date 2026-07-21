import sympy as sp
m12 = sp.symbols("m12", positive=True)
al = sp.symbols("alpha", real=True)
Mp2 = sp.symbols("Mp2", positive=True)
A = Mp2 + al
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
Bclaim = -(2*f(rr) + rr*sp.Derivative(f(rr), rr))*J + (rr*sp.Derivative(f(rr), rr))*(J.dot(rhat))*rhat
print("[6] B - Bclaim =", list(sp.simplify(sp.expand(Bv - Bclaim.doit()))))
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
