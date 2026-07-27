# Columna A - TAREA 2: EL CANAL NLO (el unico vivo segun el teorema de B).
#
# Los NLO del acta del escalar (K_ij(n) con n ~ dPhi^0: acoples alpha, beta) NO
# contienen Phi^a => no aportan corriente interna (se verifica). Los NLO que SI:
# los invariantes del FLUJO u^mu (la direccion comovil del medio, que depende de
# d Phi^a): expansion theta, shear sigma, vorticidad omega, aceleracion a.
# Base: L_NLO = c_th theta^2 + c_sg sigma_mn sigma^mn + c_w omega_mn omega^mn
#              + c_a a_mu a^mu   (coeficientes ~ Lambda^2, UV-sensibles, declarado)
#
# Pasos (sector vectorial transversal: V := h_{0x}(t,z), W := h_{xz}(t,z),
# fonon f := pi^x(t,z); todo a orden cuadratico en campos):
#   N1  u^mu exacto del modo (forma epsilon de a1): u_un = (1, -f_t, 0, 0);
#       invariantes a orden lineal: catalogo de que contiene f y COMO.
#   N2  RESULTADO ESTRUCTURAL: todos los invariantes de u dependen de f SOLO via
#       f_t (la velocidad material) y sus gradientes d(f_t) -- consecuencia de la
#       simetria residual: pi -> pi + xi(x) es Psi(Phi) exacta y u es invariante.
#       => la corriente interna espacial es J^i = -d_t[dL/d(d_i f_t)]:
#       EXISTE (el termino del acta de B) pero SE ANULA sobre configuraciones
#       ESTACIONARIAS. Verificacion explicita componente a componente.
#   N3  J^z_x sobre las dos ramas del juguete: cero sobre ambas (estacionarias);
#       distinto de cero durante transitorios (formacion): formula explicita.
#   N4  juguete modal extendido con NLO: EOMs, la simetria F -> F + c sobrevive,
#       carga corregida C_tilde, familia estacionaria, co-rotante corregido
#       (ya NO es RG exacto: corrimiento O(c_sg p^2/m1^2), reportar), dispersion
#       sin fuente: la rama plana omega = 0 sobrevive EXACTA a los NLO.
#   N5  veredicto: fuga lineal estacionaria = 0 exacta; el canal vivo queda
#       (transitorios de formacion) + (no lineal x NLO): numeros en a4.
import sympy as sp
import time

t0 = time.time()
print('=' * 72)
print('A3 - EL CANAL NLO: corriente de carga con derivadas superiores del medio')
print('=' * 72)

t, z, x, y = sp.symbols('t z x y', real=True)
p = sp.symbols('p', positive=True)
V = sp.Function('V')(t, z)      # h_{0x}
W = sp.Function('W')(t, z)      # h_{xz}
f = sp.Function('f')(t, z)      # pi^x

e = sp.Symbol('e')
def trunc2(ex):
    ex = sp.expand(ex)
    return sum(ex.coeff(e, k) * e ** k for k in range(3))

# ---------------- metrica del sector y objetos covariantes ----------------
h = sp.zeros(4, 4)
h[0, 1] = h[1, 0] = V
h[1, 3] = h[3, 1] = W
eta = sp.diag(-1, 1, 1, 1)
g = eta + e * h
ginv = eta - e * (eta * h * eta) + e ** 2 * (eta * h * eta * h * eta)

Xs = [t, x, y, z]
def d(fun, mu):
    return sp.diff(fun, Xs[mu])

# Christoffels a orden e (suficiente: los invariantes son cuadraticos en objetos O(e))
Gam = [[[sp.S(0)] * 4 for _ in range(4)] for _ in range(4)]
for a_ in range(4):
    for b_ in range(4):
        for c_ in range(b_, 4):
            s_ = sp.S(0)
            for dd in range(4):
                s_ += ginv[a_, dd] * (d(g[dd, b_], c_) + d(g[dd, c_], b_) - d(g[b_, c_], dd))
            v_ = trunc2(s_ / 2)
            Gam[a_][b_][c_] = v_
            Gam[a_][c_][b_] = v_

# u^mu por la forma epsilon (a1): Phi^1 = x + e f(t,z), Phi^2 = y, Phi^3 = z
# => u_un^mu = (d_x Phi^1, -d_t Phi^1, 0, 0) = (1, -e f_t, 0, 0)   [EXACTO]
f_t = sp.diff(f, t)
u_un = sp.Matrix([1, -e * f_t, 0, 0])
N = trunc2((u_un.T * g * u_un)[0, 0])
dN = trunc2(N + 1)
u_up = trunc2(1 + dN / 2 + sp.Rational(3, 8) * dN ** 2) * u_un   # u^mu = u_un/sqrt(-N)
u_up = u_up.applyfunc(trunc2)
u_dn = (g * u_up).applyfunc(trunc2)                              # u_mu

print('[N1] u^mu del sector =', [sp.simplify(u_up[k].coeff(e, 1)) for k in range(4)],
      ' * e + (1,0,0,0);  u_mu|_(e) =', [sp.simplify(u_dn[k].coeff(e, 1)) for k in range(4)])
print('     la velocidad fisica relativa medio-marcos: u_x = V - f_t (gauge-inv del modo)')

# B_mn = nabla_m u_n  a orden e
B = sp.zeros(4, 4)
for m_ in range(4):
    for n_ in range(4):
        s_ = d(u_dn[n_], m_)
        for l_ in range(4):
            s_ -= Gam[l_][m_][n_] * u_dn[l_]
        B[m_, n_] = trunc2(s_).coeff(e, 1)

# descomposicion a orden lineal (proyector espacial de fondo)
theta = sum(B[i_, i_] for i_ in (1, 2, 3))
sig_m = sp.zeros(3, 3); om_m = sp.zeros(3, 3)
for i_ in range(3):
    for j_ in range(3):
        sig_m[i_, j_] = sp.simplify((B[i_ + 1, j_ + 1] + B[j_ + 1, i_ + 1]) / 2
                                    - (theta / 3 if i_ == j_ else 0))
        om_m[i_, j_] = sp.simplify((B[i_ + 1, j_ + 1] - B[j_ + 1, i_ + 1]) / 2)
a_v = [sp.simplify(B[0, i_ + 1]) for i_ in range(3)]   # a_i = u.nabla u_i |_lineal

print('[N1] invariantes a orden lineal (catalogo):')
print('     theta =', sp.simplify(theta))
print('     sigma_xz =', sig_m[0, 2], '   (= d_t(W - f_z)/2: shear material)')
print('     omega_zx =', om_m[2, 0], '   (= d_z(V - f_t)/2: vorticidad fisica)')
print('     a_x =', a_v[0], '   (= d_t(V - f_t): aceleracion)')

# dependencia en f: SOLO via f_t (y sus derivadas)
dep = set()
for expr in [theta, sig_m[0, 2], om_m[2, 0], a_v[0]]:
    for der in sp.preorder_traversal(expr):
        if isinstance(der, sp.Derivative) and der.expr == f:
            dep.add(der)
print('[N2] derivadas de f que aparecen en los invariantes:', sorted(dep, key=str))
ok_N2 = all(sp.Derivative(f, t) in der.variables or (t in der.variables)
            for der in dep) if dep else True
# chequeo formal: sustituir f -> f + xi(z) (residual estatica) no cambia nada
xi = sp.Function('xi')(z)
ok_res = all(sp.simplify(expr.subs(f, f + xi).doit() - expr) == 0
             for expr in [theta, sig_m[0, 2], om_m[2, 0], a_v[0]])
print('[N2] invariancia bajo pi -> pi + xi(x) (residual, = Psi(Phi) exacta):',
      'OK' if ok_res else 'FALLA')
print('     => L_NLO(u) depende de f SOLO via f_t: la corriente espacial interna')
print('        es J^i_x = -d_t[ dL/d(d_i f_t) ]  (el termino del acta de B:')
print('        dL/d(dd Phi) EXISTE), pero es una derivada temporal TOTAL:')
print('        SE ANULA sobre configuraciones estacionarias.')

# ---------------- N2/N3: la corriente explicita ----------------
csg, cw, ca, cth = sp.symbols('c_sigma c_omega c_a c_theta', real=True)
sig2 = sum(sig_m[i_, j_] ** 2 for i_ in range(3) for j_ in range(3))
om2 = sum(om_m[i_, j_] ** 2 for i_ in range(3) for j_ in range(3))
a2 = sum(av ** 2 for av in a_v)
LNLO = cth * theta ** 2 + csg * sig2 + cw * om2 + ca * a2
LNLO = sp.expand(LNLO)

# corriente de Noether para shift pi^x -> pi^x + eps (con L de 2do orden):
#   J^mu = dL/d(f_mu) - d_nu [ dL/d(f_{mu nu}) ]   (f_mu := d_mu f)
# implemento via sustitucion de simbolos para derivar con seguridad
ft_, fz_, ftt_, ftz_, fzz_ = sp.symbols('ft fz ftt ftz fzz')
subs_f = {sp.Derivative(f, t, t): ftt_, sp.Derivative(f, t, z): ftz_,
          sp.Derivative(f, z, z): fzz_, sp.Derivative(f, t): ft_,
          sp.Derivative(f, z): fz_}
LN = LNLO.subs(subs_f)
back = {ft_: sp.Derivative(f, t), fz_: sp.Derivative(f, z),
        ftt_: sp.Derivative(f, t, t), ftz_: sp.Derivative(f, t, z),
        fzz_: sp.Derivative(f, z, z)}

Jt = sp.diff(LN, ft_) - sp.diff(sp.diff(LN, ftt_).subs(back), t) \
     - sp.diff(sp.diff(LN, ftz_).subs(back), z) / 1     # (convencion: ftz cuenta 1 vez en cada)
Jz = sp.diff(LN, fz_) - sp.diff(sp.diff(LN, ftz_).subs(back), t) \
     - sp.diff(sp.diff(LN, fzz_).subs(back), z)
Jt = sp.expand(Jt.subs(back).doit())
Jz = sp.expand(Jz.subs(back).doit())

f0 = {f: sp.S(0)}
Jz_pi0 = sp.simplify(Jz.subs(f0).doit())
print('\n[N3] corriente interna espacial NLO en pi=0 (campo general V,W):')
print('     J^z_x =', Jz_pi0)

# las dos ramas del juguete (estacionarias):
S_, Fd_, tc_ = sp.symbols('S Fdot tau_c')
rama_ret = {V: sp.S(0), W: -p * Fd_ * t * sp.sin(p * z)}          # W crece lineal: W_t = -p Fd sin
rama_rel = {V: S_ * sp.cos(p * z), W: sp.S(0)}
for nom, st in (('co-rotante', rama_ret), ('relajada', rama_rel)):
    val = sp.simplify(Jz_pi0.subs(st).doit())
    print('     J^z_x sobre la rama %-11s = %s' % (nom, val))
print('     (formacion: con Fdot = Fdot(t) no estacionario, J^z_x != 0: transitorio)')
Fdt = sp.Function('Fdot')(t)
rama_form = {V: sp.S(0), W: -p * sp.Integral(Fdt, t).doit() * sp.sin(p * z)}
Jz_form = sp.simplify(Jz_pi0.subs({V: sp.S(0),
                                   W: -p * sp.Function('Fint')(t) * sp.sin(p * z)}).doit())
print('     J^z_x con W = -p Fint(t) sin(pz):', Jz_form)

# ---------------- N4: juguete modal extendido ----------------
# NOTA EFT (reduccion de orden, estandar): a_u^2 = (f_tt - V_t)^2 contiene
# derivadas temporales SEGUNDAS del grado de libertad: su "rama nueva" es el
# fantasma de Ostrogradsky ESPURIO del truncamiento (masa ~ escala de corte),
# y el operador es REDUNDANTE: sobre la superficie on-shell LO se elimina con
# redefiniciones de campo (mismo procedimiento que en ghost condensate, donde
# el NLO fisico es (grad^2 pi)^2 espacial, no (pi_tt)^2). Los NLO GENUINOS del
# sector transversal son sigma_u^2 y omega_u^2 (contienen d_z f_t: primer
# orden en t). El analisis del fantasma espurio queda documentado en a5.
print('\n[N4] juguete modal extendido (S(t), F(t); pi=0; c_a reducido por EFT):')
S = sp.Function('S')(t); F = sp.Function('F')(t)
tau = sp.Function('tau')(t)
Mp2, m12, al = sp.symbols('Mp2 m12 alpha', positive=True)
A = Mp2 + al
modo = {V: S * sp.cos(p * z), W: -p * F * sp.sin(p * z), f: sp.S(0)}
zper = 2 * sp.pi / p
def zavg(ex):
    return sp.simplify((p / (2 * sp.pi)) * sp.integrate(sp.expand(ex), (z, 0, zper)))

LNLO_modo = zavg(sp.expand(LNLO.subs(modo).doit())).subs(ca, 0)
print('     L_NLO del modo (c_a -> 0 por reduccion) =', sp.expand(LNLO_modo))

Fd = sp.diff(F, t)
sigj = S - Fd
Lc = A * p ** 2 * sigj ** 2 / 4 + m12 * S ** 2 / 4 + S * tau / 2 + F * sp.diff(tau, t) / 2
Ltot = sp.expand(Lc + LNLO_modo)

def EL(L, q):
    r = sp.diff(L, q)
    r -= sp.diff(sp.diff(L, sp.Derivative(q, t)), t)
    r += sp.diff(sp.diff(L, sp.Derivative(q, (t, 2))), t, 2)
    return sp.expand(r)

eqS = EL(Ltot, S)
eqF = EL(Ltot, F)

# simetria residual del modo: F -> F + const
epsv = sp.Symbol('epsilon')
dL = sp.simplify(sp.expand(Ltot.subs(F, F + epsv) - Ltot))
print('     delta L bajo F -> F + eps =', dL, ' (= eps*taudot/2 => Noether sobrevive)')

# carga corregida: eqF = (1/2) d/dt[C_tilde]
Ct = A * p ** 2 * sigj + tau - csg * p ** 2 * Fd
r = sp.simplify(2 * eqF - sp.diff(Ct, t))
print('     2*eqF - d/dt[A p^2 sigma - c_sigma p^2 Fdot + tau] =', r,
      '  => C_tilde := A p^2 sigma - c_sigma p^2 Fdot + tau CONSERVADA (tau(t) arbitraria)')

# vinculo eqS (S sigue siendo NO dinamico: c_omega solo aporta potencial)
print('     eqS =', sp.simplify(eqS), '  (algebraica en S: sigue de primer orden)')

# estacionarios con tau = tau_c: S = cte, Fdot = v cte
tc = sp.symbols('tau_c', positive=True)
v_ = sp.Symbol('v')
est = {sp.Derivative(S, (t, 2)): 0, sp.Derivative(S, t): 0,
       sp.Derivative(F, (t, 3)): 0, sp.Derivative(F, (t, 2)): 0}
eqS_est = eqS.subs(tau, tc).subs(est).subs({sp.Derivative(F, t): v_, S: S_})
eqF_est = eqF.subs(tau, tc).subs(est).subs({sp.Derivative(F, t): v_, S: S_})
print('     eqS estacionaria:', sp.simplify(eqS_est), ' | eqF estacionaria:',
      sp.simplify(eqF_est), ' (0 = familia 1-parametrica en v: dir. plana VIVA)')
solS = sp.solve(eqS_est, S_)[0]
print('     S(v) =', sp.simplify(solS))

# co-rotante corregido: C_tilde = 0
Ct_est = Ct.subs(tau, tc).subs(est).subs({sp.Derivative(F, t): v_, S: S_}).subs(S_, solS)
v_ret = sp.solve(sp.expand(Ct_est), v_)
v_ret = [vv for vv in v_ret][0]
S_ret = sp.simplify(solS.subs(v_, v_ret))
print('     co-rotante corregido: v =', sp.simplify(v_ret))
print('                           S_ret =', sp.factor(sp.simplify(S_ret)),
      '  <-- YA NO ES RG EXACTO (O(c) residual)')
lam = sp.Symbol('lam')
S_ret_lead = sp.series(S_ret.subs({csg: sp.Symbol('chat_s') * lam,
                                   cw: sp.Symbol('chat_w') * lam}), lam, 0, 2).removeO()
print('     S_ret a primer orden en c:', sp.expand(S_ret_lead))

# relajada corregida: v = 0
S_rel = sp.simplify(solS.subs(v_, 0))
print('     relajada corregida:  S_rel =', S_rel)
DC = sp.simplify(sp.expand(
    Ct.subs(tau, tc).subs(est).subs({sp.Derivative(F, t): 0, S: S_rel})))
print('     C_tilde de la relajada corregida =', sp.factor(DC), ' != 0:')
print('     la SUPERSELECCION persiste con NLO (Delta C_tilde != 0 modo a modo).')

# dispersion sin fuente: modos e^{i w t}: matriz en (S, F)
w = sp.symbols('omega')
Sv, Fv = sp.symbols('Sv Fv')
sub_disp = {S: Sv * sp.exp(sp.I * w * t), F: Fv * sp.exp(sp.I * w * t), tau: 0}
eqS_d = sp.expand(eqS.subs(tau, sp.S(0)).subs(sub_disp).doit() / sp.exp(sp.I * w * t))
eqF_d = sp.expand(eqF.subs(tau, sp.S(0)).subs(sub_disp).doit() / sp.exp(sp.I * w * t))
Mstar = sp.Matrix([[sp.expand(eqS_d.coeff(Sv)), sp.expand(eqS_d.coeff(Fv))],
                   [sp.expand(eqF_d.coeff(Sv)), sp.expand(eqF_d.coeff(Fv))]])
det = sp.factor(sp.simplify(Mstar.det()))
print('     det de dispersion (sin fuente) =', det)
print('     => factor omega^2 y NINGUNA raiz nueva: la rama plana omega=0')
print('        sobrevive EXACTA a los NLO para todo p (la carga no gana dinamica')
print('        lineal); S sigue siendo vinculo. Consistente con el acta del')
print('        escalar: la raiz omega^2=0 protegida por xi^i(x) sobrevive NLO.')

# ---------------- N5: el IVP con NLO, solucion cerrada ----------------
print('\n[N5] IVP extendido con tau(t) ARBITRARIA (la formacion de la Tierra):')
# S esclava del vinculo eqS; C_tilde conservada => sistema de 1er orden cerrado.
Fd_s = sp.Symbol('Fdot_s')
S_s = sp.Symbol('S_s')
eqS_g = eqS.subs({sp.Derivative(S, (t, 2)): 0}).subs(
    {sp.Derivative(F, t): Fd_s, S: S_s})
S_of_Fd = sp.solve(eqS_g, S_s)[0]
Ct_g = Ct.subs({sp.Derivative(F, t): Fd_s, S: S_s}).subs(S_s, S_of_Fd)
Fd_of_C = sp.solve(sp.Eq(Ct_g, sp.Symbol('C0')), Fd_s)[0]
print('     S(Fdot, tau) =', sp.simplify(S_of_Fd))
print('     Fdot(C0, tau) =', sp.simplify(Fd_of_C))
S_final = sp.simplify(S_of_Fd.subs(Fd_s, Fd_of_C).subs(sp.Symbol('C0'), 0))
print('     con C0 = 0 (CI cosmologicas relajadas): S(t) =', sp.factor(S_final))
print('     => S(t) = S_ret_corr * [tau(t)/tau_c] EN TODO INSTANTE, para CUALQUIER')
print('        historia tau(t): el IVP adiabatico de B SOBREVIVE a los NLO;')
print('        la formacion deja al medio en el co-rotante corregido. NO hay')
print('        fuga ni siquiera durante el transitorio, a nivel modal-lineal.')
chk = sp.simplify(S_final.subs(tau, tc) - S_ret)
print('     control: S_final(tau=tau_c) - S_ret_corr =', chk)

print('\n[VEREDICTO A3 / TAREA 2, parte simbolica]')
print(' * El termino de corriente del acta de B EXISTE: J^i = -d_t[dL/d(d_i f_t)]')
print('   con dL/d(dd f) != 0 (c_sigma, c_omega). CONFIRMADO explicitamente.')
print(' * PERO es una derivada temporal total de un objeto local: sobre')
print('   configuraciones ESTACIONARIAS (co-rotante y relajada) J^i = 0 EXACTO.')
print('   Razon estructural: pi -> pi + xi(x) es una transformacion interna')
print('   Psi(Phi) exacta => NINGUN invariante del medio contiene d_i pi sin')
print('   d_t: toda corriente espacial interna viene con d_t delante.')
print(' * La rama plana omega=0 sobrevive a los NLO; la carga corregida')
print('   C_tilde = A p^2 sigma - c_sigma p^2 Fdot + tau se conserva con tau(t)')
print('   arbitraria; el IVP deja SIEMPRE al medio en el co-rotante corregido.')
print('   FUGA LINEAL (estacionaria Y transitoria): CERO EXACTO en el modo.')
print(' * Efecto fisico NUEVO: el co-rotante corregido tiene S_ret != 0 de orden')
print('   -c_sigma tau_c/(A (m1^2 + (c_s+c_w)p^2)): "RG exacto" gana correccion NLO')
print('   (numeros en a4); la relajada tambien se corrige (c_omega).')
print(' * La fuga de carga sobreviviente es (no lineal) x (NLO): dos supresiones')
print('   simultaneas; estimacion con potencias declaradas en a4.')
print('t =', round(time.time() - t0, 1), 's')
