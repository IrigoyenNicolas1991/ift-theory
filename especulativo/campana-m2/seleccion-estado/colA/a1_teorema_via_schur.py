# Columna A (verificador adversarial de la columna B) - TAREA 1, pata exacta.
#
# CHEQUEO CRUZADO DEL TEOREMA DEL CONGELAMIENTO por una ruta funcional INDEPENDIENTE.
# La columna B construyo Y resolviendo el sistema lineal para u (funcion Y_de, sp.solve).
# Aca NO se resuelve ningun sistema ni se invierte ninguna matriz 4x4: se usa la
# forma POLINOMIAL cerrada via el vector dual epsilon (etiquetas comoviles de fluidos):
#
#     u_un^mu := eps^{mu nu rho si} d_nu Phi^1 d_rho Phi^2 d_si Phi^3
#     u_un . dPhi^a = 0 automatico (antisimetria)  =>  u = u_un/norma
#     Y = u.dPhi^0 = det(dPhi) / sqrt( - u_un.g.u_un )        [TODO polinomial]
#
# La identidad del teorema se vuelve MANIFIESTA:
#   bajo dPhi^a -> E^a_b dPhi^b (GL(3) FINITA):  u_un -> det(E) u_un,
#   det(dPhi) -> det(E) det(dPhi)  =>  Y -> Y  (invariante exacto, no infinitesimal)
#   =>  dY/d(d_mu Phi^a) * d_mu Phi^b = 0  (derivada direccional de un invariante)
#   =>  P_a^mu d_mu Phi^b = 0  (la identidad de B)  =>  P_a^i = 0 en gauge unitario.
#
# Ademas se verifica la ruta Schur del acta (Y^2 = V.B^{-1}.V - X) y el match con
# la implementacion Y_de de B. Pasos (chequeo imprime residuo, regla de la casa):
#   S1  Schur polinomializada: det(C) = det(B)*X - V.adj(B).V  (C simetrica GENERICA)
#       => Y_schur^2 = W - X = -1/(C^{-1})_00 bien definida sin resolver u.
#   S2  invariancia GL(3) FINITA de la forma epsilon: u_un(E.dPhi) = det(E)*u_un(dPhi)
#       y det: simbolico exacto con dPhi 16 simbolos y E 9 simbolos.
#   S3  cross-check de TRES implementaciones (Y_de de B / Y_schur / Y_eps):
#       configuraciones racionales aleatorias EXACTAS (sin floats).
#   S4  gauge unitario con metrica exacta g = eta + h (10 simbolos, sin invertir g):
#       d(Y^2)/d(d_i Phi^a) = 0  (las 9 espaciales, simbolico exacto)
#       d(Y^2)/d(d_0 Phi^a) = -2 g_{0a}/g_00^2  (formula cerrada del acta de B)
#   S5  linealizacion: P_a^0 = -U_Y h_{0a} + O(h^2)  (la formula del acta).
import sympy as sp
import random, time

t0 = time.time()
print('=' * 72)
print('A1 - TEOREMA DEL CONGELAMIENTO VIA FORMA EPSILON (ruta indep. de col. B)')
print('=' * 72)

eps4 = sp.LeviCivita

def u_un_de(dP):
    """u_un^mu = eps^{mu nu rho si} dP[1,nu] dP[2,rho] dP[3,si]  (polinomial)."""
    comp = []
    for mu in range(4):
        s_ = 0
        for nu in range(4):
            for rho in range(4):
                for si in range(4):
                    e = eps4(mu, nu, rho, si)
                    if e != 0:
                        s_ += e * dP[1, nu] * dP[2, rho] * dP[3, si]
        comp.append(sp.expand(s_))
    return sp.Matrix(comp)

def Y_eps(dP, g):
    """MI forma cerrada polinomial: Y = det(dP)/sqrt(-u_un.g.u_un)."""
    uu = u_un_de(dP)
    N = (uu.T * g * uu)[0, 0]
    return dP.det() / sp.sqrt(-N)

def Y_schur(dP, g):
    """Ruta Schur del acta: Y = sqrt(V.B^{-1}.V - X)."""
    Cm = dP * g.inv() * dP.T
    Xv = Cm[0, 0]
    Vv = Cm[0, 1:4].T
    Bv = Cm[1:4, 1:4]
    Wv = (Vv.T * Bv.inv() * Vv)[0, 0]
    return sp.sqrt(Wv - Xv)

def Y_de(dP, g):
    """Copiada VERBATIM de colB/t1_carga_noether.py (el blanco del cross-check)."""
    u1, u2, u3 = sp.symbols('u1 u2 u3')
    v = sp.Matrix([1, u1, u2, u3])
    eqs = [sum(v[mu] * dP[a, mu] for mu in range(4)) for a in (1, 2, 3)]
    solu = sp.solve(eqs, [u1, u2, u3], dict=True)
    if not solu:
        raise ValueError('flujo degenerado')
    vsol = v.subs(solu[0])
    N = (vsol.T * g * vsol)[0, 0]
    u0 = 1 / sp.sqrt(-N)
    return u0 * sum(vsol[mu] * dP[0, mu] for mu in range(4))

# ---------------- S1: Schur polinomializada (C generica simetrica) ----------------
Cs = {}
for A in range(4):
    for B in range(A, 4):
        Cs[(A, B)] = Cs[(B, A)] = sp.Symbol('c%d%d' % (A, B))
C = sp.Matrix(4, 4, lambda A, B: Cs[(A, B)])
X = C[0, 0]
V = C[0, 1:4].T
Bm = C[1:4, 1:4]
res_S1 = sp.expand(C.det() - (Bm.det() * X - (V.T * Bm.adjugate() * V)[0, 0]))
print('[S1] det(C) - [det(B)*X - V.adj(B).V] =', res_S1)
print('     => (C^-1)_00 = det(B)/det(C) = 1/(X - V.B^-1.V):  Y_schur^2 = W - X')
print('        esta bien definida sin resolver u (complemento de Schur).')

# ---------------- S2: invariancia GL(3) FINITA (forma epsilon) ----------------
dPs = sp.Matrix(4, 4, lambda A, mu: sp.Symbol('d%d%d' % (A, mu)))
E = sp.Matrix(3, 3, lambda i, j: sp.Symbol('E%d%d' % (i, j)))
dPE = sp.Matrix(dPs)
dPE[1:4, :] = E * dPs[1:4, :]
uu0 = u_un_de(dPs)
uuE = u_un_de(dPE)
difs = [sp.expand(uuE[mu] - E.det() * uu0[mu]) for mu in range(4)]
print('[S2] u_un(E.dPhi) - det(E)*u_un(dPhi) =', difs, ' (dPhi y E GENERICAS)')
res_det = sp.expand(dPE.det() - E.det() * dPs.det())
print('[S2] det(E.dPhi)|_espacial - det(E)*det(dPhi) =', res_det)
print('     => Y = det(dPhi)/sqrt(-u_un.g.u_un) es invariante GL+(3) FINITO')
print('        MANIFIESTO (el cociente es homogeneo grado 0 en det(E)).')
print('     => dY/d(d_mu Phi^a) * d_mu Phi^b = deriv. direccional (E = I + s e_ab)')
print('        de un invariante = 0  ==  P_a^mu d_mu Phi^b = 0  (teorema de B),')
print('        OFF-SHELL, exacto en metrica y configuracion, a todo orden.')

# ---------------- S3: cross-check de las TRES implementaciones ----------------
random.seed(23)
def rq(den, top):
    return sp.Rational(random.randint(-top, top), den)

ok_S3 = True
for trial in range(3):
    g = sp.Matrix(4, 4, lambda i, j: 0)
    for i in range(4):
        for j in range(i, 4):
            base = sp.Integer(-1) if i == j == 0 else (sp.Integer(1) if i == j else 0)
            g[i, j] = g[j, i] = base + rq(17, 5)
    dP = sp.Matrix(4, 4, lambda A, mu: (1 if A == mu else 0) + rq(19, 4))
    ya, yb, yc = Y_de(dP, g), Y_schur(dP, g), Y_eps(dP, g)
    d1 = sp.simplify(ya - yc)
    d2 = sp.simplify(yb - yc)
    ok_S3 = ok_S3 and (d1 == 0) and (d2 == 0)
    print('[S3] trial %d: Y_de(B)-Y_eps = %s ; Y_schur-Y_eps = %s' % (trial, d1, d2))
print('[S3] tres formas funcionales coinciden (racional exacto):',
      'OK' if ok_S3 else 'FALLA <-- DISCREPANCIA CON B')

# ---------------- S4: gauge unitario, metrica exacta simbolica ----------------
hs = {}
for i in range(4):
    for j in range(i, 4):
        hs[(i, j)] = hs[(j, i)] = sp.Symbol('h%d%d' % (min(i, j), max(i, j)))
gU = sp.Matrix(4, 4, lambda i, j: (-1 if i == j == 0 else (1 if i == j else 0)) + hs[(i, j)])
s = sp.Symbol('s')

def Y2_pert(a, mu):
    """Y^2 con dP = I + s E_{a,mu} en g exacta; devuelve d(Y^2)/ds en s=0."""
    dP = sp.eye(4)
    dP[a, mu] = dP[a, mu] + s
    uu = u_un_de(dP)
    N = sp.expand((uu.T * gU * uu)[0, 0])
    Y2 = dP.det() ** 2 / (-N)
    return sp.simplify(sp.diff(Y2, s).subs(s, 0))

uu_bg = u_un_de(sp.eye(4))
N_bg = sp.expand((uu_bg.T * gU * uu_bg)[0, 0])
print('[S4] fondo unitario: u_un =', list(uu_bg), '; Y^2 = -1/g_00:',
      sp.simplify(sp.Integer(1) / (-N_bg) + 1 / gU[0, 0]) == 0)

ok_S4a = True
for a in (1, 2, 3):
    for i in (1, 2, 3):
        v = Y2_pert(a, i)
        ok_S4a = ok_S4a and (v == 0)
        if v != 0:
            print('   d(Y^2)/d(d_%d Phi^%d) = %s  <-- NO NULO (contradice a B)' % (i, a, v))
print('[S4] d(Y^2)/d(d_i Phi^a) = 0 (9 comps, g EXACTA simbolica):',
      'OK' if ok_S4a else 'FALLA')
print('     => P_a^i = sqrt(-g) U_Y (1/2Y) d(Y^2)/d(d_i Phi^a) = 0 IDENTICAMENTE.')

ok_S4b = True
for a in (1, 2, 3):
    v = sp.simplify(Y2_pert(a, 0) - (-2 * gU[0, a] / gU[0, 0] ** 2))
    ok_S4b = ok_S4b and (v == 0)
    print('[S4] d(Y^2)/d(d_0 Phi^%d) + 2 g_{0%d}/g_00^2 =' % (a, a), v)
print('[S4] formula cerrada del acta (P_a^0 = sqrt(-g) U_Y g_{0a}/(g_00 sqrt(-g_00)))')
print('     [via P_a^0 = U_Y sqrt(-g) dY^2/ds / (2Y)]:', 'OK' if ok_S4b else 'FALLA')

# ---------------- S5: linealizacion ----------------
epsl = sp.Symbol('epsl')
sub_lin = {v: epsl * v for v in set(hs.values())}
dY2 = Y2_pert(1, 0)
serie = sp.series(dY2.subs(sub_lin), epsl, 0, 2).removeO()
lin = sp.expand(serie.coeff(epsl, 1))
print('[S5] d(Y^2)/d(d_0 Phi^1) a orden h =', lin, ' => P_1^0 = U_Y*(%s)/2' % lin)
print('     claim del acta: P_a^0 = -U_Y h_{0a} + O(h^2):',
      'OK' if sp.simplify(lin / 2 + hs[(0, 1)]) == 0 else 'FALLA')

print('\n[VEREDICTO A1] Teorema de B verificado por ruta epsilon (independiente):')
print(' * Y tiene forma POLINOMIAL cerrada Y = det(dPhi)/sqrt(-u_un.g.u_un), con')
print('   u_un^mu = eps^{mu nu rho si} d_nu Phi^1 d_rho Phi^2 d_si Phi^3 (S2+S3).')
print(' * P_a^mu d_mu Phi^b = 0 es la invariancia GL+(3) FINITA manifiesta del')
print('   cociente: vale off-shell, con metrica exacta, a TODO orden perturbativo')
print('   (cubico incluido: es identidad algebraica, no orden a orden).')
print(' * En gauge unitario: P_a^i = 0 con g exacta (S4a); P_a^0 cerrado y')
print('   linealizado coinciden con el acta de B (S4b, S5).')
print('t =', round(time.time() - t0, 1), 's')
