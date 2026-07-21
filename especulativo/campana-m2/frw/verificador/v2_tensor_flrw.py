# -*- coding: utf-8 -*-
"""
v2_tensor_flrw.py — Tarea 2: masa del graviton (sector tensorial TT) sobre FLRW
para el medio U(X,Y). CLAIM a verificar: M_2^2 = 0 IDENTICAMENTE sobre cualquier
fondo FLRW (sin pedir tadpoles), porque U(X,Y) no depende de tau_n, y_n, b.

Pipeline propio, TODO polinomico en eps (sin sp.series: la version anterior
perdia terminos con series() sobre funciones de dos variables — bug de truncado
detectado por el control interno y corregido):
  - inversa metrica por serie de Neumann manual + check g.ginv = 1 + O(eps^3)
  - sqrt(-g) por raiz cuadrada en serie manual sobre el det polinomico exacto
  (i)   delta X = delta Y = 0 EXACTO bajo h_ij TT (inversa exacta, no en serie).
  (ii)  Accion cuadratica S2[h]: EOM de h por Euler-Lagrange de campos (t,z).
  (iii) Ruta independiente: (G_mn - T_mn) a orden h, con T_mn covariante.
  (iv)  On-shell del fondo (Friedmann II: 2 addot/a + H^2 = -p = -U): masa -> 0.
  (v)   CONTROL POSITIVO: U -> U + c1*tau1 + c2*tau2: la masa DEBE aparecer,
        con pesos relativos 4/a^2 : 1 (BCP 7.21, M2^2 = sum n^2 a^{-2(n-1)} U_tau_n).
Convenciones: signatura (-,+,+,+), S = int sqrt(-g)[R/2 + U + ...], M_Pl=1.
h_ij TT con k // z: g_ij = a^2 (delta_ij + h_ij), h_xx=-h_yy=hp(t,z), h_xy=hx(t,z).
"""
import sympy as sp

ok = True
def check(nombre, expr, esperado=0):
    global ok
    r = sp.simplify(sp.expand(expr - esperado))
    estado = "PASS" if r == 0 else "FAIL"
    if r != 0: ok = False
    print(f"  [{estado}] {nombre}: residuo = {r}")

t, z, x, y = sp.symbols('t z x y', real=True)
coords = (t, x, y, z)
eps = sp.Symbol('eps')
a = sp.Function('a', positive=True)(t)
ph = sp.Function('phi', real=True)(t)
hp = sp.Function('h_p', real=True)(t, z)
hx = sp.Function('h_x', real=True)(t, z)
w = sp.diff(ph, t)
H = sp.diff(a, t)/a

def ptrunc(e, n=2):
    """truncado POLINOMICO en eps (la expresion debe ser polinomica en eps)"""
    e = sp.expand(e)
    return sum(e.coeff(eps, k)*eps**k for k in range(n+1))

# ---------- metrica perturbada TT ----------
hmat = sp.Matrix([[hp, hx, 0], [hx, -hp, 0], [0, 0, 0]])   # bloque (x,y,z)
gamma = a**2*(sp.eye(3) + eps*hmat)
g = sp.zeros(4, 4)
g[0, 0] = -1
for i in range(3):
    for j in range(3):
        g[i+1, j+1] = gamma[i, j]

# inversa por Neumann: gamma^{-1} = a^{-2} (1 - eps h + eps^2 h^2)
gamma_inv = (sp.eye(3) - eps*hmat + eps**2*hmat*hmat)/a**2
ginv_s = sp.zeros(4, 4)
ginv_s[0, 0] = -1
for i in range(3):
    for j in range(3):
        ginv_s[i+1, j+1] = gamma_inv[i, j]
# check interno del truncado
resid_inv = (g*ginv_s).applyfunc(lambda e: ptrunc(e, 2)) - sp.eye(4)
check("interno: g.ginv == 1 + O(eps^3)", sum(sp.Abs(sp.simplify(e)) for e in resid_inv))

# sqrt(-g) por serie manual sobre el det polinomico exacto
detg = sp.expand(-g.det())              # polinomio en eps
p0 = detg.coeff(eps, 0)
u = sp.expand((detg - p0)/p0)           # O(eps^2) aqui (tr h = 0)
sqrtg = ptrunc(sp.sqrt(p0)*(1 + u/2 - u**2/8), 2)
check("interno: sqrtg^2 == -det g + O(eps^3)", ptrunc(sqrtg**2 - detg, 2))
print(f"  sqrt(-g) = {sqrtg}")

# ---------- (i) invariancia exacta de X e Y ----------
print()
print("=" * 72)
print("(i) X e Y bajo h TT (con la inversa metrica EXACTA de sympy)")
print("=" * 72)
ginv_exact = g.inv()
Xpert = sp.simplify(ginv_exact[0, 0]*w**2)
Ypert = sp.simplify(w/sp.sqrt(-g[0, 0]))
check("X = -phid^2 exacto (delta X == 0 a TODO orden en h)", Xpert, -w**2)
check("Y = +phid  exacto (delta Y == 0 a TODO orden en h)", Ypert, w)
print("  => U(X,Y) NO se entera de h_TT; el unico acople es via sqrt(-g).")

# ---------- rutina de curvatura propia (truncado polinomico) ----------
def christoffel(g_, ginv_, coords_):
    n = len(coords_)
    Gam = [[[0]*n for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for m in range(n):
            for v in range(m, n):
                e = sum(ginv_[r, s]*(sp.diff(g_[s, m], coords_[v])
                                     + sp.diff(g_[s, v], coords_[m])
                                     - sp.diff(g_[m, v], coords_[s]))
                        for s in range(n))/2
                e = ptrunc(e, 2)
                Gam[r][m][v] = e
                Gam[r][v][m] = e
    return Gam

def ricci_tensor(Gam, coords_):
    n = len(coords_)
    Ric = sp.zeros(n, n)
    for m in range(n):
        for v in range(m, n):
            e = 0
            for r in range(n):
                e += sp.diff(Gam[r][m][v], coords_[r]) - sp.diff(Gam[r][r][m], coords_[v])
                for lam in range(n):
                    e += Gam[r][r][lam]*Gam[lam][m][v] - Gam[r][v][lam]*Gam[lam][r][m]
            e = ptrunc(e, 2)
            Ric[m, v] = e
            Ric[v, m] = e
    return Ric

Gam = christoffel(g, ginv_s, coords)
Ric = ricci_tensor(Gam, coords)
R = ptrunc(sum(ginv_s[m, v]*Ric[m, v] for m in range(4) for v in range(4)), 2)
# control del fondo: R(eps^0) = 6(addot/a + H^2)
check("interno: R fondo == 6(addot/a + adot^2/a^2)",
      R.coeff(eps, 0) - 6*(sp.diff(a, t, 2)/a + sp.diff(a, t)**2/a**2))

print()
print("=" * 72)
print("(ii) Accion cuadratica y EOM de h por Euler-Lagrange de campos")
print("=" * 72)
Ub = sp.Function('U_b')(t)     # valor de fondo de U(X,Y); bajo TT no fluctua
L_full = ptrunc(sp.expand(sqrtg*(R/2 + Ub)), 2)
L2 = sp.expand(L_full.coeff(eps, 2))

def euler_lagrange_field(L, q):
    eom = sp.diff(L, q)
    for i in range(3):
        for j in range(3):
            if i == 0 and j == 0:
                continue
            D = sp.Derivative(q, *([t]*i + [z]*j))
            dLdD = sp.diff(L, D)
            if dLdD != 0:
                term = dLdD
                for _ in range(i): term = sp.diff(term, t)
                for _ in range(j): term = sp.diff(term, z)
                eom += (-1)**(i + j)*term
    return sp.expand(eom)

# chequeo del termino del medio en L2 (solo algebraico, sin derivadas de h)
dL_U2 = sp.expand((ptrunc(sqrtg*Ub, 2)).coeff(eps, 2))
check("delta2(sqrt-g U) == -(a^3 U_b/2)(hp^2 + hx^2): SOLO algebraico",
      dL_U2 + a**3*Ub*(hp**2 + hx**2)/2)
tiene_deriv_h = any(dL_U2.has(sp.Derivative(f, v)) for f in (hp, hx) for v in (t, z))
check("delta2(sqrt-g U) sin derivadas de h (no toca cinetico => c_T de EH)",
      sp.Integer(1 if tiene_deriv_h else 0))

addot = sp.Derivative(a, t, 2)
for f, nombre in ((hp, "h_p"), (hx, "h_x")):
    eom = euler_lagrange_field(L2, f)
    ckin = sp.simplify(eom.coeff(sp.Derivative(f, t, 2)))
    cfric = sp.simplify(eom.coeff(sp.Derivative(f, t)))
    cgrad = sp.simplify(eom.coeff(sp.Derivative(f, z, 2)))
    cmass = sp.expand(eom.coeff(f))
    print(f"  EOM({nombre}): coef(fdd) = {ckin}")
    check(f"{nombre}: friccion/kin == 3H", sp.simplify(cfric/ckin) - 3*H)
    check(f"{nombre}: grad/kin == -1/a^2  (c_T^2 = 1)", sp.simplify(cgrad/ckin) + 1/a**2)
    cmass_n = sp.simplify(cmass/ckin)
    print(f"    masa OFF-shell/kin = {sp.factor(cmass_n)}")
    M2_on = sp.simplify(cmass_n.subs(addot, -(Ub + H**2)*a/2))
    check(f"{nombre}: MASA on-shell (Friedmann II, p=U, SIN tadpoles) == 0", M2_on)

print()
print("=" * 72)
print("(iii) Ruta covariante independiente: (G_mn - T_mn) a orden h")
print("=" * 72)
# T_mn covariante:  T_mn = -2 dU/dg^{mn} + g_mn U ; con dY/dg^{mn} =
# -(phid/2)(-g00)^{-3/2} g_0m g_0n  =>  el termino U_Y entra con signo +.
UX_s, UY_s = sp.symbols('U_X U_Y', real=True)
T = sp.zeros(4, 4)
for mu in range(4):
    for nu in range(4):
        T[mu, nu] = (-2*w**2*UX_s*(1 if mu == 0 and nu == 0 else 0)
                     + w*UY_s*(-g[0, 0])**sp.Rational(-3, 2)*g[0, mu]*g[0, nu]
                     + g[mu, nu]*Ub)
G_E = sp.zeros(4, 4)
for mu in range(4):
    for nu in range(4):
        G_E[mu, nu] = ptrunc(Ric[mu, nu] - g[mu, nu]*R/2, 2)
# control de fondo: G_00 - T_00 = 0 <=> 3H^2 = rho; G_11 - T_11 = 0 <=> Friedmann II
rho_bg = -Ub - 2*w**2*UX_s + w*UY_s
check("fondo: (G_00 - T_00)|_eps0 == 3H^2 - rho",
      sp.expand(G_E[0, 0] - T[0, 0]).coeff(eps, 0) - (3*H**2 - rho_bg))
# OJO: expand ANTES de coeff — coeff sobre un Mul no expandido pierde terminos
Exy = sp.expand(G_E[1, 2] - T[1, 2]).coeff(eps, 1)
Epp = sp.expand((sp.expand(G_E[1, 1] - T[1, 1]) - sp.expand(G_E[2, 2] - T[2, 2]))/2).coeff(eps, 1)
for nombre, E, f in (("E_xy (h_x)", Exy, hx), ("(E_xx-E_yy)/2 (h_p)", Epp, hp)):
    ckin = sp.simplify(E.coeff(sp.Derivative(f, t, 2)))
    cfric = sp.simplify(E.coeff(sp.Derivative(f, t)))
    cgrad = sp.simplify(E.coeff(sp.Derivative(f, z, 2)))
    cmass = sp.expand(E.coeff(f))
    check(f"{nombre}: friccion/kin == 3H", sp.simplify(cfric/ckin) - 3*H)
    check(f"{nombre}: grad/kin == -1/a^2", sp.simplify(cgrad/ckin) + 1/a**2)
    M2_on = sp.simplify(sp.simplify(cmass/ckin).subs(addot, -(Ub + H**2)*a/2))
    check(f"{nombre}: masa on-shell == 0", M2_on)

print()
print("=" * 72)
print("(v) CONTROL POSITIVO: U + c1*tau1 + c2*tau2 (el pipeline detecta masa)")
print("=" * 72)
c1, c2 = sp.symbols('c1 c2', real=True)
Bmat = ginv_s[1:, 1:]
tau1 = ptrunc(sp.trace(Bmat), 2)
tau2 = ptrunc(sp.expand(sp.trace(Bmat*Bmat)), 2)
print(f"  fondo: tau1 = {tau1.coeff(eps,0)},  tau2 = {tau2.coeff(eps,0)}  [3/a^2, 3/a^4 OK]")
check("delta1 tau1 == 0 (TT sin traza)", sp.simplify(tau1.coeff(eps, 1)))
check("delta1 tau2 == 0", sp.simplify(tau2.coeff(eps, 1)))
d2t1 = sp.simplify(tau1.coeff(eps, 2)); d2t2 = sp.simplify(tau2.coeff(eps, 2))
print(f"  delta2 tau1 = {d2t1}   [teoria: n(n+1)/2 = 1 por tr h^2 = 2(hp^2+hx^2)]")
print(f"  delta2 tau2 = {d2t2}   [teoria: n(n+1)/2 = 3]")

L_ctrl = ptrunc(sp.expand(sqrtg*(R/2 + Ub + c1*tau1 + c2*tau2)), 2)
L2c = sp.expand(L_ctrl.coeff(eps, 2))
eom_c = euler_lagrange_field(L2c, hp)
ckinc = sp.simplify(eom_c.coeff(sp.Derivative(hp, t, 2)))
massc = sp.expand(eom_c.coeff(hp))
massc_n = sp.simplify(massc/ckinc)
# Friedmann II del fondo con tau_n. Presion extra p_tau POR DOS RUTAS:
# (a) T covariante: T_ij = -2 c_n d(tau_n)/dg^{ij} + g_ij c_n tau_n; en el fondo
#     d(tau_n)/dg^{ij} = n (B^{n-1})_ij = n a^{-2(n-1)} delta_ij =>
#     T_ij = c_n(-2n a^{-2(n-1)} + 3 a^{-2n} a^2) delta_ij... => p = c_n (3-2n) a^{-2n}
# (b) mini-superspace con MI convencion de EL del V1 (EL_a = +3a^2(2addot/a+H^2+p)):
#     la parte de materia da  d(a^3 c_n taubar_n)/da = +3 a^2 p_tau_n
Lm_tau = a**3*(c1*3/a**2 + c2*3/a**4)
p_tau = sp.solve(sp.Eq(sp.diff(Lm_tau, a), 3*a**2*sp.Symbol('p_')), sp.Symbol('p_'))[0]
p_tau_cov = c1*(3-2)*a**-2 + c2*(3-4)*a**-4
check("p_tau (mini-superspace, convencion V1) == p_tau (T covariante)",
      sp.expand(p_tau - p_tau_cov))
print(f"  p_tau = {sp.expand(p_tau)}   [= +c1/a^2 - c2/a^4; chequeo fisico: solo c1")
print("   => w = p/rho = -1/3, curvatura-like: el resultado clasico de gradientes")
print("   escalares congelados. La primera version de este control tenia el signo")
print("   de p_tau volteado (matching con la convencion EL de la casa en vez de la")
print("   mia) y daba pesos falsos (0, -20): corregido y declarado.]")
M2_ctrl = sp.simplify(sp.expand(massc_n.subs(addot, -(Ub + p_tau + H**2)*a/2)))
print(f"  masa_eff (control, on-shell) = {sp.factor(M2_ctrl)}")
peso1 = sp.simplify(sp.expand(M2_ctrl).coeff(c1)); peso2 = sp.simplify(sp.expand(M2_ctrl).coeff(c2))
print(f"  peso(c1) = {peso1},  peso(c2) = {peso2}")
check("masa DETECTADA (el pipeline NO es ciego a masas): peso(c1) != 0",
      sp.Integer(0 if peso1 != 0 else 1))
# BCP (7.21): M2^2 M_Pl^2 = sum_n n^2 a^{-2(n-1)} U_tau_n  (leida del PDF fuente).
# Mi masa_eff de la EOM debe ser proporcional a M2^2/a^2 con pesos n^2 a^{-2(n-1)}:
check("PESOS BCP (7.21): masa_eff == -(4/a^2)[1*c1 + 4*a^{-2}*c2]  (n^2 a^{-2(n-1)})",
      sp.expand(M2_ctrl + (4/a**2)*(c1 + 4*c2/a**2)))
# y en a=1 reproduce el diccionario Minkowski VERIFICADO de la campana:
# masa_eff = 2*m2^2 con m2^2 = -2 sum n^2 U_tau_n  =>  masa_eff = -4(c1+4c2)
check("limite a=1 == 2*m2^2(Minkowski, campana) = -4(c1+4c2)",
      sp.expand(M2_ctrl.subs(a, 1) + 4*(c1 + 4*c2)))

print()
print("VEREDICTO TAREA 2:", "TODO PASS" if ok else "HAY FALLOS — revisar arriba")
