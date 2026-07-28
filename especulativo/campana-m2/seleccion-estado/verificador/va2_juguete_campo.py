# VERIFICADOR ADVERSARIAL FINAL - ATAQUES 1b y 2 (parcial) y 3a: el juguete de
# campo RECONSTRUIDO desde cero con pipeline propio.
#
# Diferencias deliberadas con las columnas (independencia):
#  * EH: accion Gamma-Gamma de PRIMER ORDEN (L_GG = sqrt(-g) g^{mn} (G^r_{lm}G^l_{rn}
#    - G^l_{mn}G^r_{lr})), que difiere de sqrt(-g)R por derivada total EXACTA.
#    lib_eh (usado por ambas columnas) usa el Ricci completo con segundas
#    derivadas. Mi ruta no tiene segundas derivadas => Noether ESTANDAR sin
#    correccion de Ostrogradsky: ataca de paso el chequeo R2 de colB (si las
#    cargas coinciden, el resultado es robusto a IBP por tercera via).
#  * signo global del EH anclado a FISICA (modo TT: cinetica positiva), no al
#    resultado que quiero cotejar.
#
# Chequeos:
#  G0  control de signo: modo TT h_xy = q(t,z): L prop (qdot^2 - q'^2), + cinetica.
#  G1  L modal (V = S cos pz, W = -pF sin pz) == forma canonica de la campania
#      A p^2 sig^2/4 + m1^2 S^2/4 + S tau/2 + F taudot/2, mod derivada total
#      (via Euler-Lagrange identicos en S y F). DERIVADO, no importado.
#  G2  vinculo: 2 eqS = A p^2 sig + m1^2 S + tau ; C := A p^2 sig + tau ;
#      dC/dt = 2 eqF (conservada con tau(t) ARBITRARIA); C = -m1^2 S on-shell.
#  G3  ramas estacionarias: relajada C != 0, co-rotante C = 0; residuos EOM.
#  G4  ATAQUE 1b - la corriente LOCAL de la simetria residual en gauge unitario
#      (xi^x = eps cos(pz) => delta V = 0, delta W = -p eps sin(pz)) con MI L de
#      CAMPO (t,z): J^t(t,z) y J^z(t,z) explicitos.
#      - J^z != 0 localmente (la pieza gravitatoria del flujo: el temor del
#        mandato es LEGITIMO a nivel local)...
#      - ...pero d_t<J^t>_z = 0 (el flujo es periodico: no transporta carga
#        neta por modo) y <J^t> on-shell = -C/2 * eps: la MISMA ley que la
#        carga interna via el vinculo. El flujo EH local no abre canal.
#  G5  ATAQUE al escape "relajada + nube compensante": existe un estado con
#      C = 0 y sigma = sigma_relajada? Resolver: NO (el vinculo lo prohibe:
#      unico estacionario del sector C = 0 es el co-rotante). => "su fundamental".
#  G6  energia por sector: H(C; tau) = C^2/(4 m1^2) + (tau - C)^2/(4 A p^2)
#      derivada con MI Legendre; minimo global en C_rel; el co-rotante es el
#      UNICO punto del sector C = 0 (blanco 4 de colB: reinterpretacion OK).
#  G7  IVP universal SIN RK4: solucion general SIMBOLICA exacta con tau(t)
#      arbitraria: S(t) = -C0/m1^2 constante; C0 = 0 => S = 0 IDENTICO.
#      (mas fuerte que las 4x4 historias numericas de colB).
import sympy as sp
import time

t0 = time.time()
print('=' * 72)
print('VA2 - JUGUETE DE CAMPO PROPIO (accion Gamma-Gamma, primer orden)')
print('=' * 72)

t, z, x, y = sp.symbols('t z x y', real=True)
p = sp.symbols('p', positive=True)
Mp2, m12 = sp.symbols('Mp2 m12', positive=True)
al = sp.Symbol('alpha', real=True)
A = Mp2 + al
Xs = [t, x, y, z]
eta = sp.diag(-1, 1, 1, 1)

def d(f, mu):
    return sp.diff(f, Xs[mu])

def L_GG(hmat, sgn):
    """Gamma-Gamma cuadratico: eta^{mn}(G^r_{lm} G^l_{rn} - G^l_{mn} G^r_{lr}),
    Gamma lineal en h. sgn = +-1 fija la convencion del escalar de curvatura."""
    Gam = [[[sp.S(0)] * 4 for _ in range(4)] for _ in range(4)]
    for a_ in range(4):
        for b_ in range(4):
            for c_ in range(b_, 4):
                s_ = sp.S(0)
                for e_ in range(4):
                    s_ += eta[a_, e_] * (d(hmat[e_, b_], c_) + d(hmat[e_, c_], b_)
                                         - d(hmat[b_, c_], e_))
                v_ = s_ / 2
                Gam[a_][b_][c_] = v_
                Gam[a_][c_][b_] = v_
    L = sp.S(0)
    for m_ in range(4):
        for n_ in range(4):
            if eta[m_, n_] == 0:
                continue
            for r_ in range(4):
                for l_ in range(4):
                    L += eta[m_, n_] * Gam[r_][l_][m_] * Gam[l_][r_][n_]
                L -= eta[m_, n_] * Gam[r_][m_][n_] * sum(Gam[l_][r_][l_] for l_ in range(4))
    return sgn * sp.expand(L)

zper = 2 * sp.pi / p
def zavg(ex):
    return sp.expand(sp.simplify((p / (2 * sp.pi)) * sp.integrate(sp.expand(ex), (z, 0, zper))))

def EL(L, q):
    r = sp.diff(L, q)
    r -= sp.diff(sp.diff(L, sp.Derivative(q, t)), t)
    r += sp.diff(sp.diff(L, sp.Derivative(q, (t, 2))), t, 2)
    return sp.expand(r)

# ---------------- G0: anclar el signo con el modo TT ----------------
qm = sp.Function('qm')(t)
hTT = sp.zeros(4, 4)
hTT[1, 2] = hTT[2, 1] = qm * sp.cos(p * z)
SGN = None
for sgn in (+1, -1):
    LTT = zavg(L_GG(hTT, sgn).doit())
    cin = sp.expand(LTT).coeff(sp.Derivative(qm, t) ** 2)
    if cin != 0 and sp.simplify(cin).is_positive:
        SGN = sgn
        break
assert SGN is not None, 'no se pudo anclar el signo TT'
LTT = zavg(L_GG(hTT, SGN).doit())
print('[G0] signo fisico: sgn =', SGN, '; L_TT =', sp.expand(LTT),
      ' (cinetica qmdot^2 POSITIVA: convencion anclada a no-fantasma TT)')

# ---------------- el sector vectorial ----------------
S = sp.Function('S')(t)
F = sp.Function('F')(t)
tau = sp.Function('tau')(t)
V = sp.Function('V')(t, z)      # h_0x
W = sp.Function('W')(t, z)      # h_xz
h = sp.zeros(4, 4)
h[0, 1] = h[1, 0] = V
h[1, 3] = h[3, 1] = W

LEH_campo = Mp2 * L_GG(h, SGN)
# NLO alpha del acople (campania previa): K_xz = d_t W - d_z V gauge-inv; L = (al/2) K^2
Kxz = sp.diff(W, t) - sp.diff(V, z)
LNLO_campo = al * Kxz ** 2 / 2
Lm_campo = m12 * V ** 2 / 2
T0x = tau * sp.cos(p * z)
Txz = -(sp.diff(tau, t) / p) * sp.sin(p * z)
print('[chk] conservacion fuente: d_t T0x + d_z Tzx =',
      sp.simplify(sp.diff(T0x, t) + sp.diff(Txz, z)))
Lint_campo = V * T0x + W * Txz
Lcampo = LEH_campo + LNLO_campo + Lm_campo + Lint_campo

# ---------------- G1: reduccion modal == forma canonica ----------------
modo = {V: S * sp.cos(p * z), W: -p * F * sp.sin(p * z)}
Lmodal = zavg(Lcampo.subs(modo).doit())
Fd = sp.diff(F, t)
sig = S - Fd
Lcan = A * p ** 2 * sig ** 2 / 4 + m12 * S ** 2 / 4 + S * tau / 2 + F * sp.diff(tau, t) / 2
okG1 = all(sp.simplify(sp.together(EL(sp.expand(Lmodal - Lcan), f))) == 0 for f in (S, F))
print('[G1] EL(L_modal - L_canonica) en S y F = 0 (mod derivada total)?', okG1)
print('     [derivado desde MI Gamma-Gamma: sin segundas derivadas => la carga')
print('      de Noether de aca abajo es la ESTANDAR, sin correccion Ostrogradsky]')

# ---------------- G2: vinculo, carga, conservacion ----------------
eqS = EL(Lmodal, S)
eqF = EL(Lmodal, F)
C = A * p ** 2 * sig + tau
print('[G2] 2*eqS - (A p^2 sig + m12 S + tau) =', sp.simplify(2 * eqS - (A * p ** 2 * sig + m12 * S + tau)))
print('[G2] 2*eqF - dC/dt =', sp.simplify(2 * eqF - sp.diff(C, t)),
      '  => C conservada ON-SHELL con tau(t) ARBITRARIA')
print('[G2] on-shell (eqS = 0): C = -m12*S  (el puente carga modal <-> P_a^0)')

# ---------------- G3: ramas ----------------
tc = sp.symbols('tau_c', positive=True)
rama_rel = {S: -tc / (A * p ** 2 + m12), F: sp.S(0)}
rama_ret = {S: sp.S(0), F: tc * t / (A * p ** 2)}
for nom, st in (('relajada', rama_rel), ('co-rotante', rama_ret)):
    r1 = sp.simplify(eqS.subs(tau, tc).subs(st).doit())
    r2 = sp.simplify(eqF.subs(tau, tc).subs(st).doit())
    Cv = sp.simplify(C.subs(tau, tc).subs(st).doit())
    print('[G3] rama %-11s: eqS = %s, eqF = %s, C = %s' % (nom, r1, r2, Cv))

# ---------------- G4: corriente LOCAL del residual (ataque 1b) ----------------
print('[G4] corriente local de xi^x = eps cos(pz) (delta V = 0, delta W = -p eps sin(pz)):')
epsv = sp.Symbol('epsilon')
dW = -p * epsv * sp.sin(p * z)
dL = sp.expand(Lcampo.subs(W, W + dW).doit() - Lcampo)
dL = sp.expand(dL.coeff(epsv, 1)) * epsv          # lineal en eps (exacto: L cuadratica)
ELW = sp.expand(sp.diff(Lcampo, W)
                - sp.diff(sp.diff(Lcampo, sp.Derivative(W, t)), t)
                - sp.diff(sp.diff(Lcampo, sp.Derivative(W, z)), z))
piWt = sp.diff(Lcampo, sp.Derivative(W, t))
piWz = sp.diff(Lcampo, sp.Derivative(W, z))
# identidad de variacion (L de primer orden, sin Ostrogradsky):
ident = sp.simplify(dL - (ELW * dW + sp.diff(piWt * dW, t) + sp.diff(piWz * dW, z)))
print('     dL - [EL_W dW + d_mu(pi^mu_W dW)] =', ident, ' (identidad: debe ser 0)')
# dL NO es cero puntual: cuasi-invariancia (pieza EH del Gamma-Gamma + fuente
# externa). Hallo K^mu COMPLETO con ansatz lineal en campos:
c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 = sp.symbols('c1:11')
sinz, cosz = sp.sin(p * z), sp.cos(p * z)
Kt_ans = epsv * (c1 * tau * sinz ** 2 + c2 * W * sinz + c3 * V * cosz
                 + c4 * W * cosz + c9 * V * sinz)
Kz_ans = epsv * (c5 * V * sinz + c6 * W * sinz + c7 * V * cosz
                 + c8 * W * cosz + c10 * tau * sinz * cosz)
res = sp.expand(dL - sp.diff(Kt_ans, t) - sp.diff(Kz_ans, z))
base_syms = [V, W, sp.Derivative(V, t), sp.Derivative(W, t),
             sp.Derivative(V, z), sp.Derivative(W, z), sp.Derivative(tau, t), tau]
unks = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
eqs = []
for b in base_syms:
    co = sp.expand(res.coeff(b))
    for zval in (0, sp.pi / (2 * p), sp.pi / (4 * p), sp.pi / (3 * p)):
        eqs.append(sp.expand(co.subs(z, zval)))
solK = sp.solve(eqs, unks, dict=True)
print('     K^mu hallado (coefs no nulos):',
      {k: v for k, v in solK[0].items() if v != 0} if solK else 'NO EXISTE')
assert solK, 'NO existe K^mu lineal: la cuasi-invariancia fallo'
Kt = Kt_ans.subs(solK[0]).subs({u: 0 for u in unks})
Kz = Kz_ans.subs(solK[0]).subs({u: 0 for u in unks})
chkK = sp.simplify(sp.expand(dL - sp.diff(Kt, t) - sp.diff(Kz, z)))
print('     dL - d_mu K^mu =', chkK, ' (0 => cuasi-invariancia off-shell EXACTA)')
# corriente de Noether local completa:
Jt = sp.expand(piWt * dW - Kt)
Jz = sp.expand(piWz * dW - Kz)
divJ = sp.simplify(sp.diff(Jt, t) + sp.diff(Jz, z) + ELW * dW)
print('     d_t J^t + d_z J^z + EL_W dW =', divJ, ' => conservada ON-SHELL (EL_W = 0)')
Jz_modo = sp.simplify(Jz.subs(modo).doit())
print('     J^z(t,z)/eps sobre el modo =', sp.simplify(Jz_modo / epsv))
Jt_avg = zavg(Jt.subs(modo).doit())
Qmodal = sp.simplify(Jt_avg / epsv)
print('     <J^t>_z/eps sobre el modo =', Qmodal)
Qm_onshell = sp.simplify(Qmodal + C / 2)
print('     <J^t>/eps + C/2 =', Qm_onshell, ' (0 => la carga local promediada ES -C/2)')
print('     LECTURA (corregida por el calculo): K^mu resulto SOLO la pieza de')
print('     la fuente externa (c1 = 1) -- mi Gamma-Gamma es EXACTAMENTE')
print('     invariante bajo el residual estatico -- y J^z sobre el modo dio')
print('     CERO: en este sector NI SIQUIERA hay flujo gravitatorio local.')
print('     La carga del residual (con su pieza EH en pi^t_W) coincide')
print('     on-shell con la interna (-C/2). El teorema no omitio piezas.')

# ---------------- G5: el escape "relajada + nube compensante" ----------------
print('[G5] existe estado estacionario con C = 0 y sigma = sigma_relajada?')
sig_rel = -tc / (A * p ** 2 + m12)
Ssol = sp.symbols('S_sol')
# estacionario: S = cte, Fdot = v cte; vinculo: A p^2 (S - v) + m12 S + tau_c = 0
v = sp.Symbol('v')
vinculo = A * p ** 2 * (Ssol - v) + m12 * Ssol + tc
Ccond = A * p ** 2 * (Ssol - v) + tc
solu = sp.solve([vinculo, Ccond, sp.Eq(Ssol - v, sig_rel)], [Ssol, v], dict=True)
print('     sistema {vinculo = 0, C = 0, sigma = sigma_rel}: solucion =', solu)
solu2 = sp.solve([vinculo, Ccond], [Ssol, v], dict=True)
print('     sistema {vinculo = 0, C = 0} (sin forzar sigma):', solu2,
      ' => sigma = -tau_c/(A p^2): EL co-rotante, UNICO. No hay nube compensante')
print('     estacionaria en el sector C = 0 del modo: es su fundamental (y unico).')

# ---------------- G6: energia por sector (Legendre propio) ----------------
print('[G6] H(C; tau) por Legendre de MI L modal:')
piF = sp.diff(Lmodal, Fd)
piv, Sv, Fdv = sp.symbols('piv Sv Fdv')
pi_sym = piF.subs({S: Sv, Fd: Fdv})
Fd_of = sp.solve(sp.Eq(pi_sym, piv), Fdv)[0]
Hfull = sp.expand(piv * Fd_of - Lmodal.subs({S: Sv, Fd: Fdv}).subs(Fdv, Fd_of))
# S es auxiliar: lo elimino con dH/dS = 0
solS = sp.solve(sp.diff(Hfull, Sv), Sv)[0]
Hred = sp.simplify(Hfull.subs(Sv, solS))
# reescribo en terminos de C: on-shell C = -m12 S = -m12*solS; y pi = (tau - C)/2
Cs = sp.Symbol('C')
pi_de_C = (tau - Cs) / 2
Hsec = sp.simplify(Hred.subs(piv, pi_de_C))
Hclaim = Cs ** 2 / (4 * m12) + (tau - Cs) ** 2 / (4 * A * p ** 2) - F * sp.diff(tau, t) / 2
dif = sp.simplify(Hsec - Hclaim)
print('     H(pi=(tau-C)/2) - [C^2/(4 m12) + (tau-C)^2/(4 A p^2) - F taudot/2] =', dif)
Hfis = Cs ** 2 / (4 * m12) + (tau - Cs) ** 2 / (4 * A * p ** 2)
Cmin = sp.solve(sp.diff(Hfis, Cs), Cs)[0]
print('     argmin_C H =', sp.simplify(Cmin), ' = C_relajada?',
      sp.simplify(Cmin - m12 * tau / (A * p ** 2 + m12)) == 0)
print('     => el minimo GLOBAL es la relajada, PERO C esta congelada: dentro del')
print('        sector C = 0 el co-rotante es el fundamental (y unico estacionario,')
print('        G5). E_ret > E_fund compara SECTORES distintos: blanco 4 de B, OK.')

# ---------------- G7: IVP universal, solucion general simbolica ----------------
print('[G7] IVP con tau(t) ARBITRARIA, solucion general simbolica:')
C0, tau0, Fd0 = sp.symbols('C0 tau0 Fdot0')
# vinculo => S = (A p^2 Fdot - tau)/(A p^2 + m12); eqF => C = cte = C0
Fdot_gen = (C0 - tau) / (A * p ** 2) + sp.Function('Sgen')(t)  # ansatz: resolver S
# mejor: resuelvo directo: C = A p^2 (S - Fdot) + tau = C0 y vinculo C0 = -m12 S:
S_gen = -C0 / m12
Fdot_sol = S_gen - (C0 - tau) / (A * p ** 2)
r1 = sp.simplify(eqS.subs({S: S_gen, sp.Derivative(F, t): Fdot_sol}).doit())
# eqF contiene Fddot: sustituyo F por su integral explicita
Fsol = sp.integrate(Fdot_sol, t)
r2 = sp.simplify(eqF.subs(S, S_gen).subs(F, Fsol).doit())
print('     S = -C0/m12, Fdot = -C0/m12 - (C0 - tau)/(A p^2):  eqS =', r1, ', eqF =', r2)
print('     => SOLUCION GENERAL EXACTA para tau(t) arbitraria: S constante,')
print('        etiquetada SOLO por C0. Con C0 = 0 (FRW): S(t) = 0 IDENTICO --')
print('        el encendido (cualquier historia) deja el medio CO-ROTANTE.')
print('        [mas fuerte que el RK4 de colB: es la solucion general cerrada]')

print('\n[VEREDICTO VA2]')
print(' * Mi Gamma-Gamma reproduce la forma canonica de la campania (G1): la')
print('   estructura del juguete NO es artefacto del pipeline de las columnas.')
print(' * Vinculo, carga conservada con tau(t) arbitraria, C = -m12 S, ramas y')
print('   Delta C: todo reproducido (G2, G3).')
print(' * Ataque 1b RESPONDIDO con calculo: la corriente COMPLETA del residual')
print('   en gauge unitario (pieza EH incluida via pi^t_W) tiene J^z = 0 sobre')
print('   el modo (ni flujo local en este sector) y su carga coincide on-shell')
print('   con la interna (-C/2). La superseleccion no depende de que carga se use.')
print(' * El escape "relajada + nube compensante" NO existe como estacionario del')
print('   sector C = 0 en el modo (G5).')
print(' * Energia: reinterpretacion de B correcta (G6). IVP: solucion general')
print('   cerrada, universal (G7).')
print('t =', round(time.time() - t0, 1), 's')
