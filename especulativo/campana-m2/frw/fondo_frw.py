"""
Campana m2=0 - tarea 4 (FRW): FONDO cosmologico del medio U(X,Y).
Convenciones BCP: signatura (-,+,+,+), M_Pl=1 (M2 simbolico aca).

Mini-superspace: ds2 = -N(t)^2 dt^2 + a(t)^2 dx^2, gauge unitario cosmologico
Phi^0 = phi(t), Phi^a = x^a (comoviles).
Invariantes sobre este fondo: X = -phid^2/N^2, Y = phid/N  (=> X = -Y^2, con
V=0 la identidad de Schur X + Y^2 = V.B^{-1}.V = 0).

CRITERIOS DE MUERTE (declarados antes de calcular, 2026-07-21):
 D1. Fondo inconsistente en toda la esquina sana (rho<0 estructural, sin
     soluciones de expansion) => muerte cosmologica de la fase.
 D2. El atractor se ALEJA de la superficie de tadpoles => la proteccion
     m2=m3=m4=0 exige ajuste fino cosmologico (se degrada el claim; se publica).
 D3. Perturbaciones sobre FRW con inestabilidad rapida nueva en la esquina
     sana => muerte fenomenologica (se publica). [Se examina en la parte B.]

Chequeos de este script:
 F1. rho y p del medio desde la accion (variacion en N; EOM de a como control).
 F2. Conservacion de Bianchi: rhod + 3H(rho+p) = 0 (identidad simbolica).
 F3. EOM de phi <=> J = a^3(U_Y - 2 phid U_X) constante de movimiento; la
     superficie J=0 con phid=1 ES la condicion de tadpole U_Y = 2U_X.
 F4. rho + p = phid * J/a^3  => en el atractor J/a^3 -> 0: w -> -1.
 F5. Desviacion del atractor: delta(phid) ~ a^-3 y delta(rho) ~ a^-3 (dust);
     coeficiente K = d/dphid[U_Y - 2 phid U_X] en la esquina sana != 0.
 F6. Control CCP: la subclase isentropica U(X+Y^2) es DEGENERADA en FRW
     (U=U(0) const, w=-1 exacto sin dinamica) — la U(X,Y) general no.
"""
import sympy as sp

t = sp.symbols('t', real=True)
N = sp.Function('N', positive=True)(t)
a = sp.Function('a', positive=True)(t)
ph = sp.Function('phi', real=True)(t)
M2 = sp.symbols('M2', positive=True)

X = -sp.diff(ph, t)**2 / N**2
Y = sp.diff(ph, t) / N

U = sp.Function('U')
Um = U(X, Y)

# accion mini-superspace: S = int dt [ L_EH + L_m ],  L_m = N a^3 U
# EH: (M2/2) sqrt(-g) R -> mini-superspace: -3 M2 a ad^2 / N  (mod deriv. total)
L_EH = -3*M2*a*sp.diff(a, t)**2/N
L_m = N*a**3*Um
L = L_EH + L_m

# ---------- F1: rho desde la variacion en N ----------
dLdN = sp.diff(L, N)
# constraint: dL/dN = 0  =>  3 M2 a ad^2/N^2 = -(dL_m/dN)  =>  3M2 H^2 = rho
Ngauge = {N: 1, sp.diff(N, t): 0}
rho = sp.simplify((-sp.diff(L_m, N)/a**3).subs(Ngauge).doit())
constraint = sp.Eq(3*M2*(sp.diff(a, t)/a)**2, rho)
print("F1  rho =", rho)

# p desde la EOM de a: d/dt(dL/dad) - dL/da = 0  =>  forma estandar
# 2 (add/a) + H^2 = -p/M2 ... la leemos y despejamos p.
eom_a = (sp.diff(sp.diff(L, sp.diff(a, t)), t) - sp.diff(L, a)).subs(Ngauge).doit()
eom_a = sp.expand(sp.simplify(eom_a))
# eom_a = -6 M2 (a add + ad^2/2 ...)... despejamos p identificando:
#   eom_a == -3 a^2 [ M2 (2 add/a + H^2) + p ]   (candidato)
p_cand = sp.symbols('p_cand')
add, ad = sp.diff(a, t, 2), sp.diff(a, t)
p_expr = sp.solve(sp.Eq(eom_a, -3*a**2*(M2*(2*add/a + ad**2/a**2) + p_cand)), p_cand)
p_medio = sp.simplify(p_expr[0])
print("F1  p =", p_medio)

# sanity Minkowski: phid=1, U(vac)=0, U_Y=2U_X  => rho=0, p=0
phd = sp.symbols('phid', positive=True)
UX, UY = sp.symbols('U_X U_Y', real=True)
U0s = sp.symbols('U0', real=True)
subsfun = lambda e: e.subs({sp.Derivative(ph, t): phd}).replace(
    lambda ex: isinstance(ex, sp.Subs) or (hasattr(ex, 'func') and ex.func == sp.Derivative and ex.has(U)),
    lambda ex: ex
)
# version simbolica plana de rho y p con derivadas parciales como simbolos:
Xf, Yf = -phd**2, phd
rho_flat = sp.simplify(-U0s - 2*phd**2*UX + phd*UY)   # de la derivacion de arriba
p_flat = U0s
mink = {phd: 1, UY: 2*UX, U0s: 0}
print("F1  sanity Minkowski: rho =", rho_flat.subs(mink), " p =", p_flat.subs(mink))
# cotejo de rho y p contra las formas planas con una U concreta:
#   U = (X+1) + 2(Y-1) + (1/2)(X+1)^2   (la esquina sana del paper)
Uc = lambda x, y: (x+1) + 2*(y-1) + sp.Rational(1, 2)*(x+1)**2
L_m_c = (N*a**3*Uc(X, Y))
rho_c = sp.simplify((-sp.diff(L_m_c, N)/a**3).subs(Ngauge).doit())
eom_a_c = (sp.diff(sp.diff(L_EH + L_m_c, sp.diff(a, t)), t) - sp.diff(L_EH + L_m_c, a)).subs(Ngauge).doit()
p_c = sp.solve(sp.Eq(sp.expand(eom_a_c), -3*a**2*(M2*(2*add/a + ad**2/a**2) + p_cand)), p_cand)[0]
# formas planas con la misma U: U_X = 1+(X+1), U_Y = 2, U0 = U(X,Y)
Xn = -sp.Derivative(ph, t)**2; Yn = sp.Derivative(ph, t)
UXc = 1 + (Xn + 1); UYc = 2; U0c = Uc(Xn, Yn)
rho_flat_c = -U0c - 2*sp.Derivative(ph, t)**2*UXc + sp.Derivative(ph, t)*UYc
p_flat_c = U0c
print("F1  cotejo rho (U concreta):", sp.simplify(rho_c - rho_flat_c))
print("F1  cotejo p   (U concreta):", sp.simplify(p_c - p_flat_c))

# ---------- F3: EOM de phi => corriente conservada ----------
J = sp.diff(L, sp.diff(ph, t)).subs(Ngauge).doit()
eom_phi = sp.diff(sp.diff(L, sp.diff(ph, t)), t) - sp.diff(L, ph)
print("F3  J = dL/dphid =", sp.simplify(J.subs(Ngauge)))
print("F3  EOM(phi) == dJ/dt (phi ciclica):", sp.simplify((eom_phi - sp.diff(sp.diff(L, sp.diff(ph, t)), t))) == 0)
# con U concreta:
J_c = sp.simplify(sp.diff(L_m_c, sp.diff(ph, t)).subs(Ngauge).doit())
print("F3  J (U concreta) =", J_c, "  [claim: a^3 (U_Y - 2 phid U_X)]")
J_claim = a**3*(UYc - 2*sp.Derivative(ph, t)*UXc)
print("F3  J - claim =", sp.simplify(J_c - J_claim))
print("F3  J(phid=1) =", sp.simplify(J_c.subs(sp.Derivative(ph, t), 1)), "  [tadpole: 0 => atractor = esquina protegida]")

# ---------- F2: Bianchi con U concreta ----------
H = sp.Derivative(a, t)/a
bianchi = sp.diff(rho_c, t) + 3*H*(rho_c + p_c)
# sobre la EOM de phi: sustituimos phidd despejado de dJ/dt = 0
phidd = sp.Derivative(ph, t, 2)
sol_phidd = sp.solve(sp.Eq(sp.diff(J_c, t).doit(), 0), phidd)
bianchi_on = sp.simplify(bianchi.doit().subs(phidd, sol_phidd[0]))
print("F2  Bianchi on-shell (U concreta):", bianchi_on)

# ---------- F4: rho + p = phid * J/a^3 ----------
print("F4  rho+p - phid*J/a^3 =", sp.simplify((rho_c + p_c) - sp.Derivative(ph, t)*J_c/a**3))

# ---------- F5: desviacion del atractor (dust) ----------
# J = const: linealizamos phid = 1 + d(t):  J/a^3 = K*d + O(d^2),
# K = d/dphid [U_Y - 2 phid U_X] en phid=1.
dsym = sp.symbols('delta')
Jd = sp.expand((J_c/a**3).subs(sp.Derivative(ph, t), 1 + dsym))
K = sp.simplify(sp.diff(Jd, dsym).subs(dsym, 0))
print("F5  K = d(J/a^3)/dphid en el atractor =", K, " (esquina sana: K != 0 => delta ~ a^-3)")
# delta rho a primer orden:
drho = sp.simplify(sp.diff(rho_c.subs(sp.Derivative(ph, t), 1 + dsym), dsym).subs(dsym, 0))
print("F5  d(rho)/d(delta) en el atractor =", drho, " => delta_rho = (este coef)*(J/(K a^3)) ~ a^-3: dust")

# ---------- F6: la isentropica U(X+Y^2) es degenerada en FRW ----------
W = sp.Function('W')
L_m_i = N*a**3*W(X + Y**2)
rho_i = sp.simplify((-sp.diff(L_m_i, N)/a**3).subs(Ngauge).doit())
J_i = sp.simplify(sp.diff(L_m_i, sp.diff(ph, t)).subs(Ngauge).doit())
print("F6  isentropica: rho =", rho_i, " | J =", J_i, "  [rho=-W(0) const, J=0 identico: pura CC, sin dinamica]")
