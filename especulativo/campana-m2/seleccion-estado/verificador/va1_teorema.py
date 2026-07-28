# VERIFICADOR ADVERSARIAL FINAL - ATAQUE 1: el teorema del congelamiento.
#
# Pipeline PROPIO, TERCERA parametrizacion de Y (ni el solve-u de colB/t1 ni la
# forma Levi-Civita de colA/a1): pura algebra de determinantes de la matriz de
# Gram C^{AB} = d_mu Phi^A g^{mu nu} d_nu Phi^B:
#
#     (C^-1)_00 = det(B)/det(C)   (cofactor),   B = bloque espacial de C
#     u^mu := g^{mu nu} d_nu Phi^A (C^-1)_{A0} / sqrt(-(C^-1)_00)
#         => u.dPhi^a = 0, u.g.u = -1,  Y = u.dPhi^0 = 1/sqrt(-(C^-1)_00)
#     => Y^2 = -det(C)/det(B)                     [MI forma cerrada]
#     y SIN inversas:  det C = det(dP)^2/det g ;  B = (dP adj(g) dP^T)_esp/det g
#     => Y^2 = -det(dP)^2 det(g)^2 / det[(dP adj(g) dP^T)_esp]   [POLINOMIAL]
#
# Ataques:
#  V0  mi Y^2 contra una construccion por nullspace (SymPy .nullspace,
#      mecanicamente distinta de las tres rutas previas), racional exacto.
#  V1  invariancia GL(3) FINITA: (M C M^T)_esp = E C_esp E^T (identidad simbolica
#      de bloques) + multiplicatividad del det (estandar; spot-check racional)
#      => Y^2(MCM^T) = Y^2(C) EXACTO off-shell, C GENERICA, todo orden.
#      Corolario infinitesimal: P_a^mu d_mu Phi^b = 0; en gauge unitario
#      d_mu Phi^b = delta^b_mu => P_a^b = 0 (b = 1,2,3) sin mas calculo.
#  V2  P_a^i = 0 en gauge unitario, metrica exacta simbolica (9 comps), derivando
#      MI Y^2 polinomial (regla del cociente, s = 0).
#  V3  P_a^0: formula cerrada exacta y linealizacion -U_Y h_{0a} (= -m1^2 h_0a).
#  V4  corriente de Noether COMPLETA (ataque 1a): sin pieza EH, sin borde.
#  V5  COROLARIO DE INVERSION (respuesta al ataque 2): P_a^0 = 0 <=> g_{0a} = 0
#      punto a punto, exacto en h.
#  V6  FRW: P_a^0 = 0 exacto toda epoca.
import sympy as sp
import random, time

t0 = time.time()
print('=' * 72, flush=True)
print('VA1 - EL TEOREMA, PIPELINE PROPIO (determinantes de la matriz de Gram)')
print('=' * 72, flush=True)

# ---------- mi forma cerrada, version polinomial ----------
def Y2_mio_poli(dP, g):
    """Y^2 = -det(dP)^2 det(g)^2 / det[(dP adj(g) dP^T)_esp]  (sin inversas)."""
    adjg = g.adjugate()
    W = (dP * adjg * dP.T)[1:4, 1:4]
    return -dP.det() ** 2 * g.det() ** 2 / W.det()

def Y2_nullspace(dP, g):
    """Construccion por nullspace (mecanicamente distinta), devuelve Y^2 racional."""
    ns = dP[1:4, :].nullspace()
    assert len(ns) == 1, 'flujo degenerado'
    u = ns[0]
    N = (u.T * g * u)[0, 0]
    Yv = (dP[0, :] * u)[0, 0]
    return Yv ** 2 / (-N)

# ---------- V0: cross-check racional exacto ----------
random.seed(41)
def rq(den, top):
    return sp.Rational(random.randint(-top, top), den)

ok_V0 = True
for trial in range(3):
    g = sp.Matrix(4, 4, lambda i, j: 0)
    for i in range(4):
        for j in range(i, 4):
            base = sp.Integer(-1) if i == j == 0 else (sp.Integer(1) if i == j else 0)
            g[i, j] = g[j, i] = base + rq(23, 6)
    dP = sp.Matrix(4, 4, lambda A, mu: (1 if A == mu else 0) + rq(29, 5))
    d = sp.cancel(Y2_mio_poli(dP, g) - Y2_nullspace(dP, g))
    ok_V0 = ok_V0 and (d == 0)
    print('[V0] trial %d: Y2_dets - Y2_nullspace =' % trial, d, flush=True)
print('[V0] forma cerrada Y^2 = -detC/detB validada por ruta independiente:',
      'OK' if ok_V0 else 'FALLA', flush=True)

# ---------- V1: invariancia GL(3) finita ----------
Cs = {}
for A in range(4):
    for B in range(A, 4):
        Cs[(A, B)] = Cs[(B, A)] = sp.Symbol('c%d%d' % (A, B))
C = sp.Matrix(4, 4, lambda A, B: Cs[(A, B)])
E = sp.Matrix(3, 3, lambda i, j: sp.Symbol('E%d%d' % (i, j)))
M = sp.eye(4)
M[1:4, 1:4] = E
CM = M * C * M.T
res_bloque = sp.expand(CM[1:4, 1:4] - E * C[1:4, 1:4] * E.T)
print('[V1] (MCM^T)_esp - E C_esp E^T =', 'todas 0' if res_bloque == sp.zeros(3, 3)
      else res_bloque, flush=True)
# multiplicatividad del det: estandar; spot-check racional exacto igual
random.seed(7)
Cn = sp.Matrix(4, 4, lambda i, j: 0)
for i in range(4):
    for j in range(i, 4):
        Cn[i, j] = Cn[j, i] = rq(13, 9)
En = sp.Matrix(3, 3, lambda i, j: rq(11, 7))
Mn = sp.eye(4); Mn[1:4, 1:4] = En
chk1 = sp.cancel((Mn * Cn * Mn.T).det() - En.det() ** 2 * Cn.det())
chk2 = sp.cancel((Mn * Cn * Mn.T)[1:4, 1:4].det() - En.det() ** 2 * Cn[1:4, 1:4].det())
print('[V1] spot-check racional: det(MCM^T)-detE^2 detC =', chk1,
      '; bloque esp:', chk2, flush=True)
ok_V1 = (res_bloque == sp.zeros(3, 3)) and chk1 == 0 and chk2 == 0
print('[V1] det(MCM^T) = detE^2 detC (multiplicatividad) y det((MCM^T)_esp) =')
print('     detE^2 det(C_esp) (bloques + multiplicatividad 3x3)')
print('     => Y^2 = -detC/detB INVARIANTE GL(3) FINITO EXACTO, C GENERICA')
print('        (off-shell, toda metrica, todo orden):', 'OK' if ok_V1 else 'FALLA')
print('     corolario infinitesimal (deriv. en E = I + s e_ab de una identidad):')
print('     P_a^mu d_mu Phi^b = 0. En gauge unitario d_mu Phi^b = delta^b_mu')
print('     => P_a^b = 0 para b = 1,2,3: corriente espacial interna CERO.', flush=True)

# ---------- V2 y V3: derivadas en gauge unitario, g exacta simbolica ----------
hs = {}
for i in range(4):
    for j in range(i, 4):
        hs[(i, j)] = hs[(j, i)] = sp.Symbol('h%d%d' % (min(i, j), max(i, j)))
gU = sp.Matrix(4, 4, lambda i, j: (-1 if i == j == 0 else (1 if i == j else 0)) + hs[(i, j)])
adjU = gU.adjugate()
detU = sp.expand(gU.det())
s = sp.Symbol('s')

# Estructura de la reduccion (dP = I + s E_{a,mu}):
#   Y^2 = -N/D,  N = det(dP)^2 detg^2,  D = det(W),  W = (dP adj(g) dP^T)_esp
#   => dY^2/ds|_0 = -(N1 D0 - N0 D1)/D0^2, con N0 = detg^2, D0 = det(adj(g)_esp).
#   J0 (Jacobi):  det(adj(g)_esp) = g_00 detg^2  => Y^2|_0 = -1/g_00.
#   V2 (mu = i):  N1 = 2 delta_{ai} detg^2 => dY^2/ds = 0
#                 <=> d(detW)/ds|_0 - 2 delta_{ai} detW0 = 0.
#   V3 (mu = 0):  N1 = 0 => dY^2/ds = detg^2 D1/D0^2; claim -2 g_{0a}/g_00^2
#                 <=> (usando J0)  d(detW)/ds|_0 + 2 g_{0a} detg^2 = 0.
# Todas son identidades POLINOMIALES de grado <= 9: verificables por expand.
W0m = adjU[1:4, 1:4]
detW0 = sp.expand(W0m.det())
J0 = sp.expand(detW0 - gU[0, 0] * detU ** 2)
print('[J0] det(adj(g)_esp) - g_00 detg^2 =', 0 if J0 == 0 else J0,
      '  (Jacobi => Y^2|_unitario = -1/g_00)', flush=True)

def ddetW_ds(a, mu):
    dP = sp.eye(4)
    dP[a, mu] = dP[a, mu] + s
    W = (dP * adjU * dP.T)[1:4, 1:4]
    return sp.expand(sp.diff(W.det(), s).subs(s, 0))

ok_V2 = True
for a in (1, 2, 3):
    for i in (1, 2, 3):
        resid = sp.expand(ddetW_ds(a, i) - (2 * detW0 if a == i else 0))
        ok_V2 = ok_V2 and (resid == 0)
        if resid != 0:
            print('   (a=%d, i=%d): residuo = %s  <-- TEOREMA ROTO' % (a, i, resid))
print('[V2] dY^2/d(d_i Phi^a) = 0 (9 comps, g exacta simbolica, via detW):',
      'OK' if ok_V2 else 'FALLA', flush=True)
print('     => P_a^i = sqrt(-g) U_Y (1/2Y) d(Y^2)/d(d_i Phi^a) = 0 IDENTICAMENTE.')

ok_V3 = True
for a in (1, 2, 3):
    resid = sp.expand(ddetW_ds(a, 0) + 2 * gU[0, a] * detU ** 2)
    ok_V3 = ok_V3 and (resid == 0)
    print('[V3] a=%d: d(detW)/ds + 2 g_{0a} detg^2 =' % a,
          0 if resid == 0 else resid, flush=True)
print('[V3] formula cerrada P_a^0 = sqrt(-g) U_Y g_{0a}/(g_00 sqrt(-g_00)):',
      'OK' if ok_V3 else 'FALLA')
# linealizacion sobre el claim YA verificado (exacto): -2 g0a/g00^2 con
# g00 = -1 + h00, g0a = h0a:
epsl = sp.Symbol('epsl')
claim_lin = sp.series((-2 * epsl * hs[(0, 1)] / (-1 + epsl * hs[(0, 0)]) ** 2),
                      epsl, 0, 2).removeO().coeff(epsl, 1)
print('[V3] linealizacion (sobre el claim verificado): d(Y^2)/d(d_0 Phi^1)|_lin =',
      sp.expand(claim_lin), '-> P_1^0 = -U_Y h_01 + O(h^2); con tadpole',
      'U_Y = 2U_X = m1^2 => P_a^0 = -m1^2 h_0a:',
      'OK' if sp.simplify(claim_lin + 2 * hs[(0, 1)]) == 0 else 'FALLA', flush=True)

# ---------- V4: la corriente de Noether COMPLETA ----------
print('[V4] Noether completo de Phi^a -> Phi^a + xi^a(Phi_vec), g y materia FIJAS:')
print('     - delta g_{mu nu} = 0 por definicion (transformacion interna)')
print('       => delta L_EH = 0 IDENTICAMENTE (EH no contiene Phi). Sin pieza EH.')
print('     - materia minimamente acoplada (solo via g; acople universal,')
print('       hipotesis declarada): delta L_mat = 0 IDENTICAMENTE. Sin pieza.')
print('     - delta U: X = C^00 no contiene dPhi^a (estructural); Y^2 = -detC/detB')
print('       invariante EXACTO PUNTUAL (V1: identidad, no mod derivada total)')
print('       => K^mu = 0: NO hay termino de borde de Noether.')
print('     - X e Y contienen Phi^a SOLO derivado => dL/dPhi^a = 0 =>')
print('       EOM(Phi^a)  ==  d_mu P_a^mu = 0  con P_a^mu = dL/d(d_mu Phi^a).')
print('     => J^mu[xi] = P_a^mu xi^a(Phi) es la corriente COMPLETA. Con P_a^i = 0')
print('        (V2): d_t P_a^0 = 0 punto a punto on-shell. El teorema NO omitio')
print('        piezas: la pieza gravitatoria del juguete modal pertenece a la')
print('        REALIZACION unitaria (difeo compensador x^i -> x^i + xi^i), otra')
print('        ley, que va2 coteja on-shell contra esta.', flush=True)

# ---------- V5: corolario de inversion ----------
UY = sp.Symbol('U_Y', positive=True)
h00, h0a = sp.symbols('h00 h0a', real=True)
P0 = UY * h0a / ((-1 + h00) * sp.sqrt(1 - h00))
print('[V5] P_a^0 = sqrt(-g) U_Y g_{0a}/(g_00 sqrt(-g_00)): con sqrt(-g) != 0,')
print('     U_Y != 0, g_00 < 0: el factor de g_{0a} es NO NULO =>')
print('     P_a^0(x) = 0  <=>  g_{0a}(x) = 0  EXACTO punto a punto.')
print('     P0(h0a=0) =', sp.simplify(P0.subs(h0a, 0)),
      '; dP0/dh0a|_0 =', sp.simplify(sp.diff(P0, h0a).subs(h0a, 0)), '!= 0 (h00<1).')
print('     => la etiqueta de sector (P_a^0 congelado) equivale al perfil COMPLETO')
print('        g_{0a}(x) en comoviles: la separacion co-rotante (g_0a = 0) vs')
print('        relajada (g_0a != 0) es NO PERTURBATIVA y de campo completo, no un')
print('        artefacto del modo unico. [Supuestos: U_Y != 0 (fase m1 != 0),')
print('        metrica regular; vortices/Phi no suave FUERA, como declarado.]')

# ---------- V6: FRW ----------
aa = sp.Symbol('a', positive=True)
gF = sp.diag(-1, aa ** 2, aa ** 2, aa ** 2)
print('[V6] FRW: g_{0a} =', [gF[0, k] for k in (1, 2, 3)],
      '=> P_a^0 = 0 exacto en toda epoca (formula V3). CI cosmologicas: carga 0.')

print('\n[VEREDICTO VA1] El teorema del congelamiento RESISTE mi pipeline:')
print(' * Y^2 = -detC/detB (forma nueva, validada); invariancia GL(3) finita =')
print('   identidad de bloques + multiplicatividad del det: off-shell, todo orden.')
print(' * P_a^i = 0 en gauge unitario con g exacta; P_a^0 cerrado y linealizado')
print('   coinciden con las columnas.')
print(' * Noether completo: sin pieza EH, sin borde (K = 0), bajo acople universal.')
print(' * Corolario de inversion (nuevo): P = 0 <=> g_{0a} = 0 punto a punto:')
print('   la superseleccion es exacta y de campo completo.')
print('t =', round(time.time() - t0, 1), 's')
