"""
VERIFICACION INDEPENDIENTE del diccionario medio -> masas (tarea 1 del handoff).

Ruta B': totalmente independiente de masas_medio.py. Aquella implementacion
expandia A MANO cada operador orden por orden (inversa perturbativa, trazas,
sqrt precalculadas) -- justo donde vive un posible error de pesos. Aca:

  1. g = eta + e*h con h NUMERICA (configuraciones dirigidas, entradas racionales)
     y e simbolico.
  2. g^{-1} EXACTA (inversa de sympy de la matriz 4x4), sin serie perturbativa.
  3. Operadores BCP exactos en e: X=g^00, V^a=g^0a, B=bloque espacial de g^{-1},
     tau_n=Tr(B^n), Z=V V^T, y_n=Tr(B^n Z), b=sqrt(det B), Y=1/sqrt(-g_00),
     sqrt(-g). Aritmetica racional exacta.
  4. U generica a segundo orden en los operadores (derivadas U_k, U_kl simbolicas).
  5. Serie en e RECIEN AL FINAL (funciones de UNA variable) -> coef de e^2.
  6. De configuraciones dirigidas de h se despejan las 5 masas via el patron
     BCP (7.3) y se comparan con (a) el diccionario del handoff y (b) las
     formulas IMPRESAS de BCP (7.6)-(7.7) en a=N=1.

Control global: h aleatoria generica -> el coef de e^2 debe reconstruirse con
las 5 masas despejadas (valida que el patron (7.3) capture todo).

Ejecutar: python verificacion_independiente.py   (~1 min, sympy)
"""
import sympy as sp

e = sp.Symbol('e')

OPS = ['X', 'Y', 't1', 't2', 't3', 'y0', 'y1', 'y2', 'y3', 'b']
FONDO = {'X': -1, 'Y': 1, 't1': 3, 't2': 3, 't3': 3,
         'y0': 0, 'y1': 0, 'y2': 0, 'y3': 0, 'b': 1}
U0 = sp.Symbol('U0')
D1 = {k: sp.Symbol('U_' + k) for k in OPS}
D2 = {}
for i, k in enumerate(OPS):
    for l in OPS[i:]:
        D2[(k, l)] = D2[(l, k)] = sp.Symbol('U_' + k + l)


def operadores_exactos(h):
    """Operadores BCP exactos para g = eta + e*h (h matriz sympy 4x4 simetrica)."""
    eta = sp.diag(-1, 1, 1, 1)
    g = eta + e * h
    gi = g.inv()                      # inversa EXACTA, no perturbativa
    X = gi[0, 0]
    V = sp.Matrix([gi[0, a] for a in (1, 2, 3)])
    B = gi[1:4, 1:4]
    Z = V * V.T
    ops = {'X': X, 'Y': 1 / sp.sqrt(-g[0, 0])}
    Bn = sp.eye(3)
    for n in (1, 2, 3):
        Bn = Bn * B
        ops['t%d' % n] = sp.trace(Bn)
    Bn = sp.eye(3)
    for n in (0, 1, 2, 3):
        ops['y%d' % n] = sp.trace(Bn * Z)
        Bn = Bn * B
    ops['b'] = sp.sqrt(B.det())
    sqg = sp.sqrt(-g.det())
    return ops, sqg


def coef_e2(h):
    """Coeficiente de e^2 de sqrt(-g)*U para la configuracion h."""
    ops, sqg = operadores_exactos(h)
    dl = {k: ops[k] - FONDO[k] for k in OPS}
    U = U0 + sum(D1[k] * dl[k] for k in OPS)
    U += sp.Rational(1, 2) * sum(D2[(k, l)] * dl[k] * dl[l]
                                 for k in OPS for l in OPS)
    L = sqg * U
    ser = sp.series(L, e, 0, 3).removeO()
    return sp.expand(ser.coeff(e, 2))


def hmat(**kv):
    h = sp.zeros(4, 4)
    for key, val in kv.items():
        i, j = int(key[1]), int(key[2])
        h[i, j] = h[j, i] = val
    return h


print('== Despeje de las masas desde configuraciones dirigidas ==')
c_h01 = coef_e2(hmat(h01=1))            # = m1^2/2
c_h12 = coef_e2(hmat(h12=1))            # = -m2^2/2
c_h11 = coef_e2(hmat(h11=1))            # = (m3^2 - m2^2)/4
c_h1122 = coef_e2(hmat(h11=1, h22=1))   # = m3^2 - m2^2/2
c_h00 = coef_e2(hmat(h00=1))            # = m0^2/4
c_h0011 = coef_e2(hmat(h00=1, h11=1))   # = (m0^2 - 2 m4^2 + m3^2 - m2^2)/4

m1 = sp.expand(2 * c_h01)
m2 = sp.expand(-2 * c_h12)
m3 = sp.expand(4 * c_h11 + m2)
m0 = sp.expand(4 * c_h00)
m4 = sp.expand((m0 + m3 - m2 - 4 * c_h0011) / 2)

# consistencia interna del patron (7.3):
chk_m3 = sp.simplify(c_h1122 - (m3 - m2 / 2))
print('consistencia h11=h22 (debe ser 0):', chk_m3)

masas = {'m0^2': m0, 'm1^2': m1, 'm2^2': m2, 'm3^2': m3, 'm4^2': m4}
for k, v in masas.items():
    print(k, '=', v)

print('\n== Control global: h generica aleatoria racional (x2 semillas) ==')
import random
for semilla, denom in ((11, 13), (23, 17)):
    random.seed(semilla)
    kv = {}
    for i in range(4):
        for j in range(i, 4):
            kv['h%d%d' % (i, j)] = sp.Rational(random.randint(-9, 9), denom)
    hg = sp.zeros(4, 4)
    for key, val in kv.items():
        i, j = int(key[1]), int(key[2])
        hg[i, j] = hg[j, i] = val
    c_gen = coef_e2(hg)
    h00_, h11_, h22_, h33_ = kv['h00'], kv['h11'], kv['h22'], kv['h33']
    hii = h11_ + h22_ + h33_
    h0i2 = kv['h01']**2 + kv['h02']**2 + kv['h03']**2
    hij2 = (h11_**2 + h22_**2 + h33_**2
            + 2 * (kv['h12']**2 + kv['h13']**2 + kv['h23']**2))
    patron = (m0 * h00_**2 + 2 * m1 * h0i2 - 2 * m4 * h00_ * hii
              + m3 * hii**2 - m2 * hij2) / 4
    print('semilla %d: coef(e^2) - patron(7.3) (debe ser 0):' % semilla,
          sp.simplify(c_gen - patron))

print('\n== Comparacion (a): diccionario del handoff (masas_medio.py) ==')
handoff = {
    'm0^2': -U0/2 - 2*D1['X'] + 2*D2[('X','X')] - 2*D2[('X','Y')]
            + D1['Y']/2 + D2[('Y','Y')]/2,
    'm1^2': U0 + 2*D1['X'] - D1['b'] - 2*D1['t1'] - 4*D1['t2'] - 6*D1['t3']
            + 2*(D1['y0'] + D1['y1'] + D1['y2'] + D1['y3']),
    'm2^2': U0 - D1['b'] - 4*D1['t1'] - 12*D1['t2'] - 24*D1['t3'],
}
for k in ('m0^2', 'm1^2', 'm2^2'):
    print(k, 'independiente - handoff =', sp.simplify(masas[k] - handoff[k]))

print('\n== Comparacion (b): BCP IMPRESAS (7.6)-(7.7) en a=N=1 (ar5iv, LaTeX de los autores) ==')
# (7.6): m1^2 = U + 2 U_X - U_b + sum_{n=0}^{3} 2n U_yn - 2 sum_{n=1}^{3} U_tn
bcp_m1 = (U0 + 2*D1['X'] - D1['b']
          + 2*1*D1['y1'] + 2*2*D1['y2'] + 2*3*D1['y3']
          - 2*(D1['t1'] + D1['t2'] + D1['t3']))
# (7.7): m2^2 = U - U_b - 4 sum_{n=1}^{3} (n+1) U_tn
bcp_m2 = U0 - D1['b'] - 4*(2*D1['t1'] + 3*D1['t2'] + 4*D1['t3'])
print('m1^2 independiente - BCP impresa =', sp.simplify(masas['m1^2'] - bcp_m1))
print('m2^2 independiente - BCP impresa =', sp.simplify(masas['m2^2'] - bcp_m2))

print('\n== Veredicto de pesos (solo tau_n, y_n) ==')
for n in (1, 2, 3):
    print('peso U_t%d en m1^2: independiente' % n, masas['m1^2'].coeff(D1['t%d' % n]),
          '| handoff', handoff['m1^2'].coeff(D1['t%d' % n]),
          '| BCP impresa', bcp_m1.coeff(D1['t%d' % n]))
for n in (0, 1, 2, 3):
    print('peso U_y%d en m1^2: independiente' % n, masas['m1^2'].coeff(D1['y%d' % n]),
          '| handoff', handoff['m1^2'].coeff(D1['y%d' % n]),
          '| BCP impresa', bcp_m1.coeff(D1['y%d' % n]))
for n in (1, 2, 3):
    print('peso U_t%d en m2^2: independiente' % n, masas['m2^2'].coeff(D1['t%d' % n]),
          '| handoff', handoff['m2^2'].coeff(D1['t%d' % n]),
          '| BCP impresa', bcp_m2.coeff(D1['t%d' % n]))
