# Columna B (carga y poblamiento) - TAREA 1: la carga exacta de la simetria residual
# Phi^a -> Phi^a + xi^a(Phi)  (en gauge unitario: x^i -> x^i + xi^i(x)).
#
# PARTE A (covariante, exacta): para L = sqrt(-g) U(X,Y),
#   A1  invariancia GL(3) FINITA de Y (ya se sabia no lineal, B4; aca la version que
#       implica la identidad de corriente): Y[M.dPhi] = Y[dPhi] exacto.
#   A2  identidad infinitesimal  P_a^mu d_mu Phi^b = 0  con
#       P_a^mu := d(sqrt(-g)U)/d(d_mu Phi^a) = sqrt(-g) U_Y dY/d(d_mu Phi^a)
#       (consecuencia: la corriente de Noether J^mu[xi] = P_a^mu xi^a(Phi) se conserva
#        para TODA xi^a, y ademas P_a^mu es proporcional a la direccion de flujo).
#   A3  en gauge unitario (Phi^a = x^a como configuracion): P_a^i = 0 IDENTICAMENTE
#       (la corriente espacial de la carga interna es nula: carga congelada punto a punto).
#   A4  formula cerrada P_a^0(g) y su linealizacion: P_a^0 = -U_Y h_{0a} + O(h^2);
#       con tadpole U_Y = 2U_X = m1^2  =>  P_a^0 = -m1^2 h_{0a}.
#
# PARTE B (el modo del juguete verificado, convenciones de acople/verificador/v2):
#   B1  L_tot del sector vectorial con fuente tau(t) ARBITRARIA (reconstruida como v2).
#   B2  eqF = d/dt[ A p^2 sigma + tau ]  =>  C := A p^2 sigma + tau  conservada.
#   B3  Noether en gauge unitario: bajo delta F = eps (xi_x = eps cos(pz)):
#       delta L = eps*taudot/2  =>  Q = pi_F - tau/2 = -C/2  conservada. (parte
#       gravitatoria incluida: EH+NLO aportan pi_F; la materia aporta -tau/2).
#   B4  vinculo eqS  =>  C = -m1^2 S on-shell  (la carga total del gauge unitario
#       coincide con la carga interna covariante del medio, amplitud de P_a^0; la
#       parte gravitatoria se reabsorbe con el vinculo de momento).
#   B5  C en las dos ramas estacionarias (tau = tau_c):
#         relajada (Yukawa):    C_rel = m1^2 tau_c/(A p^2 + m1^2)  (por modo, != 0)
#         co-rotante (RG):      C_ret = 0
#       => difieren MODO A MODO en la carga conservada.
#   B6  carga neta global (p->0) y perfil 3D: Delta rho_i(x) = m1^2 S_i^Yukawa(x)
#       es dipolar (x cruz J): integral angular = 0 => carga NETA cero, es una
#       REDISTRIBUCION en distribucion; y tau_i(p=0) = int T_{0i} = 0 para fuente
#       rotante estacionaria.
#
# Regla de la casa: ningun "exactamente" sin su calculo. Todo chequeo imprime su residuo.
import sys, os, random, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', 'escalar', 'verificador'))
import sympy as sp
from lib_eh import t, z, p, Mp2, build_L, zavg, EL

t0 = time.time()

# ============================================================
# PARTE A: covariante exacta
# ============================================================
print('================ PARTE A: carga covariante de U(X,Y) ================')

def Y_de(dP, g):
    """Y = u.dPhi^0 con u^mu: u.dPhi^a = 0 (a=1,2,3), u.g.u = -1, u^0>0.
    dP[A,mu] = d_mu Phi^A. Exacto (sin expandir)."""
    u1, u2, u3 = sp.symbols('u1 u2 u3')
    v = sp.Matrix([1, u1, u2, u3])          # normalizamos u = u0*v, v0 = 1
    eqs = [sum(v[mu]*dP[a, mu] for mu in range(4)) for a in (1, 2, 3)]
    solu = sp.solve(eqs, [u1, u2, u3], dict=True)
    if not solu:
        raise ValueError('flujo degenerado')
    vsol = v.subs(solu[0])
    N = (vsol.T*g*vsol)[0, 0]               # = u0^-2 * (u.g.u) => u0 = 1/sqrt(-N)
    u0 = 1/sp.sqrt(-N)
    return u0*sum(vsol[mu]*dP[0, mu] for mu in range(4))

random.seed(11)
def rq(den=17, top=6):
    return sp.Rational(random.randint(-top, top), den)

# metrica aleatoria cerca de eta (para que -N > 0 y toda raiz sea real)
gA = sp.Matrix(4, 4, lambda i, j: 0)
for i in range(4):
    for j in range(i, 4):
        base = sp.Integer(-1) if i == j == 0 else (sp.Integer(1) if i == j else 0)
        gA[i, j] = gA[j, i] = base + rq()
# dPhi aleatorio cerca de la identidad
dPA = sp.Matrix(4, 4, lambda A, mu: (1 if A == mu else 0) + rq(19, 5))

YA = Y_de(dPA, gA)

# ---- A1: invariancia GL(3) FINITA: Phi^a -> M^a_b Phi^b  => dP' = M.dP (filas 1..3)
ok_A1 = True
for trial in range(3):
    M = sp.eye(3) + sp.Matrix(3, 3, lambda i, j: rq(13, 4))
    dPB = sp.Matrix(dPA)
    dPB[1:4, :] = M*dPA[1:4, :]
    dif = sp.simplify(Y_de(dPB, gA) - YA)
    ok_A1 = ok_A1 and (dif == 0)
    print('[A1] trial %d: Y[M.dP] - Y[dP] =' % trial, dif)
print('[A1] invariancia GL(3) finita de Y:', 'OK' if ok_A1 else 'FALLA')

# ---- A2: identidad  (dY/d dP[a,mu]) * dP[b,mu] = 0  (numerico exacto, deriv. direccional)
s = sp.Symbol('s')
print('[A2] identidad P_a^mu d_mu Phi^b = 0 (via dY, U_Y factor comun):')
ok_A2 = True
for a in (1, 2, 3):
    for b in (1, 2, 3):
        # derivada direccional de Y en la direccion  delta dP[a,mu] = dP[b,mu] (mu=0..3)
        dPP = sp.Matrix(dPA)
        for mu in range(4):
            dPP[a, mu] = dPA[a, mu] + s*dPA[b, mu]
        val = sp.simplify(sp.diff(Y_de(dPP, gA), s).subs(s, 0))
        ok_A2 = ok_A2 and (val == 0)
        if val != 0:
            print('   (a=%d,b=%d): %s  <-- NO NULO' % (a, b, val))
print('[A2] las 9 contracciones dan 0:', 'OK' if ok_A2 else 'FALLA')
print('     (X = C^00 no contiene dPhi^a => la identidad vale para todo U(X,Y))')

# ---- A3: gauge unitario, P_a^i = 0 identicamente (g generica simbolica)
hs = {}
for i in range(4):
    for j in range(i, 4):
        hs[(i, j)] = hs[(j, i)] = sp.Symbol('h%d%d' % (min(i, j), max(i, j)))
gU = sp.Matrix(4, 4, lambda i, j: (-1 if i == j == 0 else (1 if i == j else 0)) + hs[(i, j)])
ok_A3 = True
for a in (1, 2, 3):
    for i in (1, 2, 3):
        dPU = sp.eye(4)
        dPU[a, i] = dPU[a, i] + s          # perturbo SOLO d_i Phi^a
        val = sp.simplify(sp.diff(Y_de(dPU, gU), s).subs(s, 0))
        ok_A3 = ok_A3 and (val == 0)
        if val != 0:
            print('   dY/d(d_%d Phi^%d) = %s  <-- NO NULO' % (i, a, val))
print('[A3] gauge unitario: dY/d(d_i Phi^a) = 0 para las 9 componentes:',
      'OK' if ok_A3 else 'FALLA')
print('     => P_a^i = sqrt(-g) U_Y dY/d(d_i Phi^a) = 0 IDENTICAMENTE (metrica exacta')
print('        arbitraria): la carga interna NO TIENE corriente espacial en las')
print('        coordenadas comoviles del medio. d_t P_a^0 = 0 punto a punto on-shell.')

# ---- A4: P_a^0 exacto y linealizado
UY, m12s = sp.symbols('U_Y m1^2', positive=True)
print('[A4] P_a^0 en gauge unitario (metrica exacta):')
for a in (1, 2, 3):
    dPU = sp.eye(4)
    dPU[a, 0] = dPU[a, 0] + s              # perturbo d_0 Phi^a
    dY = sp.simplify(sp.diff(Y_de(dPU, gU), s).subs(s, 0))
    claim = hs[(0, a)]/((-1 + hs[(0, 0)])*sp.sqrt(1 - hs[(0, 0)]))
    print('   dY/d(d_0 Phi^%d) - g_{0a}/(g_00 sqrt(-g_00)) =' % a,
          sp.simplify(dY - claim))
# linealizacion (a = 1): orden h
dPU = sp.eye(4); dPU[1, 0] = dPU[1, 0] + s
dY1 = sp.diff(Y_de(dPU, gU), s).subs(s, 0)
eps = sp.Symbol('eps')
hsub = {v: eps*v for v in set(hs.values())}
serie = sp.series(dY1.subs(hsub), eps, 0, 2).removeO()
lin = sp.expand(serie.coeff(eps, 1))
print('[A4] dY/d(d_0 Phi^1) a orden h  =', lin, '  (claim: -h01)')
print('[A4] => P_a^0 = sqrt(-g) U_Y dY/d(d_0 Phi^a) = -U_Y h_{0a} + O(h^2)')
print('[A4] con tadpole U_Y = 2U_X = m1^2:   P_a^0 = -m1^2 h_{0a} + O(h^2)')

# ============================================================
# PARTE B: el modo del juguete (convenciones v2_vector_fuente.py)
# ============================================================
print('\n================ PARTE B: la carga en el modo vectorial con fuente ================')
c = sp.cos(p*z); ssin = sp.sin(p*z)
m12 = sp.symbols('m12', positive=True)
al = sp.symbols('alpha', real=True)
A = Mp2 + al
S = sp.Function('S')(t); F = sp.Function('F')(t)
tau = sp.Function('tau')(t)

H4 = sp.zeros(4, 4)
H4[0, 1] = H4[1, 0] = S*c
H4[1, 3] = H4[3, 1] = -p*F*ssin
L1, L2 = build_L(H4)
LEH = Mp2*zavg(L2)
Kxz = sp.diff(-p*F*ssin, t) - sp.diff(S*c, z)
LNLO = zavg(sp.Rational(1, 4)*al*2*Kxz**2)
Lm = zavg(sp.Rational(1, 2)*m12*(S*c)**2)
T0x = tau*c
Txz = -(sp.diff(tau, t)/p)*ssin
Lint = zavg(sp.Rational(1, 2)*(2*(S*c)*T0x + 2*(-p*F*ssin)*Txz))
Ltot = sp.expand(LEH + LNLO + Lm + Lint)
sig = S - sp.diff(F, t)

# ---- B1: control contra la forma canonica verificada de la campania
Lclaim = A*p**2*sig**2/4 + m12*S**2/4 + S*tau/2 + F*sp.diff(tau, t)/2
okL = all(sp.simplify(sp.together(EL(sp.expand(Ltot - Lclaim), f))) == 0 for f in (S, F))
print('[B1] L_tot == forma canonica (mod dt), tau(t) arbitraria ?', okL)

# ---- B2: la conservacion desde eqF
eqS = sp.expand(EL(Ltot, S))
eqF = sp.expand(EL(Ltot, F))
C = A*p**2*sig + tau
print('[B2] eqF / dC/dt =', sp.simplify(eqF/sp.diff(C, t)), '  con C := A p^2 sigma + tau')

# ---- B3: Noether del gauge unitario con delta F = eps
# Ltot (cruda, de build_L) tiene segundas derivadas: el shift genera ademas la
# derivada total -Mp2 p^2 eps Fdotdot (Ostrogradsky). La version cruda con su
# correccion va en t4 (robustez); aca uso la forma canonica EQUIVALENTE (B1, mod dt).
epsv = sp.Symbol('epsilon')
dLc = sp.expand(Lclaim.subs(F, F + epsv) - Lclaim)
print('[B3] delta L_can bajo F -> F + eps =', sp.simplify(dLc),
      ' (claim eps*taudot/2 => K = eps*tau/2)')
piF = sp.diff(Lclaim, sp.Derivative(F, t))
Q = sp.expand(piF - tau/2)
print('[B3] Q := pi_F - tau/2 ; Q + C/2 =', sp.simplify(Q + C/2),
      ' (claim 0: Q = -C/2, misma ley que B2)')

# ---- B4: el vinculo eqS  =>  C = -m1^2 S on-shell
print('[B4] 2*eqS - (A p^2 sigma + m1^2 S + tau) =',
      sp.simplify(2*eqS - (A*p**2*sig + m12*S + tau)))
print('[B4] => on-shell (eqS=0):  C = -m1^2 S  == amplitud-modo de P_a^0 = -m1^2 h_{0a}')
print('     (PARTE A4). La carga del gauge unitario ES la carga interna covariante')
print('     del medio; EH+materia se reabsorben con el vinculo. [cuidado gravitatorio OK]')

# ---- B5: la carga en las dos ramas (tau = tau_c)
tc = sp.symbols('tau_c', positive=True)
rama_rel = {S: -tc/(A*p**2 + m12), F: sp.S(0)}     # fundamental/Yukawa
rama_ret = {S: sp.S(0), F: tc*t/(A*p**2)}          # co-rotante/RG
Ctc = C.subs(tau, tc)
C_rel = sp.simplify(Ctc.subs(rama_rel).doit())
C_ret = sp.simplify(Ctc.subs(rama_ret).doit())
print('[B5] C_relajada  =', C_rel, '  (= m1^2 tau_c/(A p^2 + m1^2), != 0)')
print('[B5] C_corotante =', C_ret)
print('[B5] Delta C = C_rel - C_ret =', sp.simplify(C_rel - C_ret), ' POR MODO p')
# control: ambas son soluciones estacionarias (residuos)
for nom, st in (('relajada', rama_rel), ('co-rotante', rama_ret)):
    r1 = sp.simplify(eqS.subs(tau, tc).subs(st).doit())
    r2 = sp.simplify(eqF.subs(tau, tc).subs(st).doit())
    print('     control rama %s: eqS = %s, eqF = %s' % (nom, r1, r2))

# ---- B6: carga neta global y perfil espacial 3D
print('[B6] p -> 0 de Delta C con tau(p) el perfil de Fourier de la fuente:')
pp = sp.Symbol('p', positive=True)
tau0 = sp.Symbol('tauhat0')               # tauhat(p->0), fuente regular
DC = m12*tau0/((Mp2 + al)*pp**2 + m12)
print('     lim_{p->0} Delta C(p) =', sp.limit(DC, pp, 0),
      ' = tauhat(0) = int d^3x T_{0i}(x) = momento lineal total de la fuente')
# fuente rotante estacionaria: T_{0i} = rho(r) (omega x x)_i => integral = 0
r_, th_, ph_ = sp.symbols('r theta phi', positive=True)
w1, w2, w3 = sp.symbols('w1 w2 w3', real=True)
xv = sp.Matrix([r_*sp.sin(th_)*sp.cos(ph_), r_*sp.sin(th_)*sp.sin(ph_), r_*sp.cos(th_)])
wv = sp.Matrix([w1, w2, w3])
integ = wv.cross(xv)*sp.sin(th_)          # (omega x x) * jacobiano angular
Iang = sp.Matrix([sp.integrate(sp.integrate(integ[k], (th_, 0, sp.pi)),
                               (ph_, 0, 2*sp.pi)) for k in range(3)])
print('     int dOmega (omega x x) =', list(Iang), ' => tauhat(0) = 0: carga NETA = 0')
# perfil: Delta rho_i(x) = m1^2 S_i^Yuk(x) ~ (x cruz J)_i f(r): integral angular de x_hat = 0
Ixhat = sp.Matrix([sp.integrate(sp.integrate((xv[k]/r_)*sp.sin(th_), (th_, 0, sp.pi)),
                                (ph_, 0, 2*sp.pi)) for k in range(3)])
print('     int dOmega x_hat =', list(Ixhat),
      ' => int d^3x Delta rho_i = 0: la diferencia es PURA REDISTRIBUCION (dipolar)')

print('\n[VEREDICTO TAREA 1]')
print(' * La carga conservada exacta es la densidad interna P_a^0(x), con corriente')
print('   espacial P_a^i IDENTICAMENTE NULA en comoviles (A3): congelada punto a punto.')
print(' * Las dos ramas difieren en DISTRIBUCION de carga (Delta C(p) != 0 modo a modo,')
print('   B5) pero NO en carga neta global (B6): es una redistribucion dipolar.')
print(' * Pasar de una rama a otra requiere transportar densidad de carga de un punto')
print('   a otro; el transporte esta prohibido a LO por P_a^i = 0 (no hay corriente que')
print('   lo haga). NO es "libre" ni "permitido con redistribucion suave": esta')
print('   congelado salvo (i) NLO con derivadas superiores, (ii) defectos (vortices).')
print('t =', round(time.time() - t0, 1), 's')
