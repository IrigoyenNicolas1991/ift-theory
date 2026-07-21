"""
Maquinaria: masas del graviton para medios auto-gravitantes en gauge unitario.
Convenciones BCP (arXiv:1603.02956): signatura (-,+,+,+), fondo Minkowski,
gauge unitario Phi^0 = t, Phi^a = x^a.  Mpl = 1.

Patron de masas (BCP eq. 7.3):
  sqrt(-g) U = t^mn h_mn + (1/4)[ m0^2 h00^2 + 2 m1^2 h0i h0i
                                  - 2 m4^2 h00 hii + m3^2 hii^2 - m2^2 hij hij ]

Implementacion por ordenes explicitos: cada objeto = (O0, O1, O2).
"""
import sympy as sp

def hsym(i, j):
    i, j = min(i, j), max(i, j)
    return sp.Symbol('h%d%d' % (i, j))

h = sp.Matrix(4, 4, lambda i, j: hsym(i, j))
eta = sp.diag(-1, 1, 1, 1)

# g^{-1} = eta - e (eta h eta) + e^2 (eta h eta h eta)
G1 = -(eta * h * eta)
G2 = (eta * h * eta * h * eta)

# ---- operadores: (fondo, orden1, orden2) ----
X0, X1, X2 = -1, G1[0, 0], G2[0, 0]
V1 = [G1[0, a] for a in (1, 2, 3)]                    # V^a = O(e)
B1 = G1[1:4, 1:4]; B2 = G2[1:4, 1:4]                  # B = I + e B1 + e^2 B2

trB1 = B1.trace(); trB2 = B2.trace(); trB1sq = (B1 * B1).trace()
tau = {1: (3, trB1, trB2),
       2: (3, 2 * trB1, 2 * trB2 + trB1sq),
       3: (3, 3 * trB1, 3 * trB2 + 3 * trB1sq)}
y2 = sp.expand(sum(v**2 for v in V1))                 # y_n = TrZ + O(e^3), todos n
yops = {n: (0, 0, y2) for n in (0, 1, 2, 3)}
d1, d2 = trB1, trB2 + (trB1**2 - trB1sq) / 2          # det B
bop = (1, d1 / 2, d2 / 2 - d1**2 / 8)                 # b = sqrt(det B)
T1 = (eta * h).trace()
T2 = ((eta * h).trace()**2 - ((eta * h) * (eta * h)).trace()) / 2
sqg = (1, T1 / 2, T2 / 2 - T1**2 / 8)                 # sqrt(-det g)
h00 = hsym(0, 0)
Yop = (1, h00 / 2, 3 * h00**2 / 8)                    # Y = (1 - e h00)^(-1/2)

ops = {'X': (X0, X1, X2), 'Y': Yop,
       't1': tau[1], 't2': tau[2], 't3': tau[3],
       'y0': yops[0], 'y1': yops[1], 'y2': yops[2], 'y3': yops[3],
       'b': bop}
names = list(ops)

U0 = sp.Symbol('U0')
D1 = {k: sp.Symbol('U_' + k) for k in names}
D2 = {}
for i, k in enumerate(names):
    for l in names[i:]:
        D2[(k, l)] = D2[(l, k)] = sp.Symbol('U_' + k + l)

# U = U0 + sum U_k Dk + 1/2 sum U_kl Dk Dl ; Dk = e*Ok1 + e^2*Ok2
Ulin1 = sp.expand(sum(D1[k] * ops[k][1] for k in names))
Ulin2 = sp.expand(sum(D1[k] * ops[k][2] for k in names))
Uquad2 = sp.expand(sp.Rational(1, 2) * sum(D2[(k, l)] * ops[k][1] * ops[l][1]
                                           for k in names for l in names))
# sqrt(-g) U por ordenes
L1 = sp.expand(U0 * sqg[1] + Ulin1)
L2 = sp.expand(U0 * sqg[2] + sqg[1] * Ulin1 + Ulin2 + Uquad2)

ceros = {hsym(i, j): 0 for i in range(4) for j in range(i, 4)}

def cf(expr, s1, s2=None):
    """Coeficiente de s1*s2 (o s1^2 si s2 None)."""
    if s2 is None or s1 == s2:
        return sp.expand(expr.coeff(s1, 2).subs(ceros))
    return sp.expand(expr.coeff(s1, 1).coeff(s2, 1).subs(ceros))

def masas(L2expr):
    h01, h02, h11, h22, h12 = [hsym(*p) for p in [(0,1),(0,2),(1,1),(2,2),(1,2)]]
    return {'m0^2': sp.expand(4 * cf(L2expr, h00)),
            'm1^2': sp.expand(2 * cf(L2expr, h01)),
            'm2^2': sp.expand(-2 * cf(L2expr, h12)),
            'm3^2': sp.expand(2 * cf(L2expr, h11, h22)),
            'm4^2': sp.expand(-2 * cf(L2expr, h00, h11))}

if __name__ == '__main__':
    h01, h02, h11, h22, h33, h12, h13 = [hsym(*p) for p in
        [(0,1),(0,2),(1,1),(2,2),(3,3),(1,2),(1,3)]]
    print('== TADPOLES (coef de e^1) ==')
    print('t(h00):', sp.expand(L1.coeff(h00, 1).subs(ceros)))
    print('t(h11):', sp.expand(L1.coeff(h11, 1).subs(ceros)))
    print('t(h01):', sp.expand(L1.coeff(h01, 1).subs(ceros)),
          '| t(h12):', sp.expand(L1.coeff(h12, 1).subs(ceros)))

    print('\n== CONSISTENCIA ISOTROPIA (deben ser 0) ==')
    print('h01^2-h02^2 :', sp.simplify(cf(L2, h01) - cf(L2, h02)))
    print('h12^2-h13^2 :', sp.simplify(cf(L2, h12) - cf(L2, h13)))
    print('h11^2-h22^2 :', sp.simplify(cf(L2, h11) - cf(L2, h22)))
    print('h11h22-h11h33:', sp.simplify(cf(L2, h11, h22) - cf(L2, h11, h33)))
    print('h00h11-h00h22:', sp.simplify(cf(L2, h00, h11) - cf(L2, h00, h22)))

    ms = masas(L2)
    print('\n== MASAS (diccionario propio, general) ==')
    for k, v in ms.items():
        print(k, '=', v)
    print('check h11^2 = (m3^2-m2^2)/4:',
          sp.simplify(4 * cf(L2, h11) - (ms['m3^2'] - ms['m2^2'])))
