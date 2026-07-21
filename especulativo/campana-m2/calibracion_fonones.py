"""
CALIBRACION 4 (la de oro): equivalencia exacta entre
  (i)  el diccionario de masas en gauge unitario (masas_medio.py), y
  (ii) la expansion en fonones de Goldstone en espacio plano g = eta,
       Phi^A = x^A + e * pi^A(x). Solo aparecen derivadas: J^A_mu = d_mu pi^A.
Por invariancia de difeomorfismos, impuestos los tadpoles debe valer
  L_fonones == L_masas[ h_mn -> d_m pi_n + d_n pi_m ]  (mod derivadas totales)

CALIBRACION 3a: U(X, w1,w2,w3) [sim. Phi^a -> Phi^a + f^a(Phi^0)] => m1^2 = 0.
CALIBRACION 4b: sector transversal: L_T = (1/2)[m1^2 f'_t^2 - m2^2 f'_z^2].
"""
import sympy as sp
from masas_medio import L1, L2, masas, ceros, hsym, names, D1, D2, U0
import masas_medio as mm

e = sp.Symbol('e')
J = {(A, mu): sp.Symbol('J_%d_%d' % (A, mu)) for A in range(4) for mu in range(4)}

def trunc2(expr):
    expr = sp.expand(expr)
    return sum(expr.coeff(e, k) * e**k for k in range(3))

# ---- operadores en gauge de fonones (algebraico en J) ----
# dPhi^A_mu = delta^A_mu + e J^A_mu ; C^{AB} = eta^{mn} dPhi^A_m dPhi^B_n
eta_d = [-1, 1, 1, 1]
dPhi = sp.Matrix(4, 4, lambda A, mu: (1 if A == mu else 0) + e * J[(A, mu)])
C = sp.Matrix(4, 4, lambda A, B: trunc2(
    sum(eta_d[m] * dPhi[A, m] * dPhi[B, m] for m in range(4))))

Xop = C[0, 0]
Vv = [C[0, a] for a in (1, 2, 3)]
Bm = C[1:4, 1:4]

def tr_pow2(M, n):
    R = sp.eye(3)
    for _ in range(n):
        R = (R * M).applyfunc(trunc2)
    return trunc2(R.trace())

tau = {n: tr_pow2(Bm, n) for n in (1, 2, 3)}
Zm = sp.Matrix(3, 3, lambda a, b: trunc2(Vv[a] * Vv[b]))
yop = {n: trunc2(((Bm**n).applyfunc(trunc2) * Zm).trace()) for n in (0, 1, 2, 3)}
Nb = (Bm - sp.eye(3)).applyfunc(trunc2)
trN = trunc2(Nb.trace()); trN2 = trunc2((Nb * Nb).trace())
dd = trunc2(trN + (trN**2 - trN2) / 2)          # det B - 1
bop = trunc2(1 + dd / 2 - dd**2 / 8)

# u^mu ortogonal a dPhi^a, normalizado (resuelto orden a orden a mano):
#   u^a = -e J^a_0 + e^2 J^b_0 J^a_b ,  u^0 = 1 + e^2 (sum_a J^a_0^2)/2
# Y = u^mu d_mu Phi^0
S2 = sum(J[(a, 0)]**2 for a in (1, 2, 3))
ua = {a: -e * J[(a, 0)] + e**2 * sum(J[(b, 0)] * J[(a, b)] for b in (1, 2, 3))
      for a in (1, 2, 3)}
u0 = 1 + e**2 * S2 / 2
Yop = trunc2(u0 * (1 + e * J[(0, 0)]) + sum(ua[a] * e * J[(0, a)] for a in (1, 2, 3)))

opsP = {'X': (Xop, -1), 'Y': (Yop, 1),
        't1': (tau[1], 3), 't2': (tau[2], 3), 't3': (tau[3], 3),
        'y0': (yop[0], 0), 'y1': (yop[1], 0), 'y2': (yop[2], 0), 'y3': (yop[3], 0),
        'b': (bop, 1)}
Dl = {k: trunc2(v[0] - v[1]) for k, v in opsP.items()}

Lpi = U0 + sum(D1[k] * Dl[k] for k in names)
Lpi += sp.Rational(1, 2) * sum(D2[(k, l)] * Dl[k] * Dl[l] for k in names for l in names)
Lpi2 = sp.expand(trunc2(Lpi).coeff(e, 2))

# ---- lado (i): L2 con h_mn = d_m pi_n + d_n pi_m ; pi_mu = eta_mn pi^n ----
# d_mu pi_nu = eta_nu_nu * J^nu_mu
hsub = {hsym(i, j): eta_d[j] * J[(j, i)] + eta_d[i] * J[(i, j)]
        for i in range(4) for j in range(i, 4)}
Lmass_sub = sp.expand(L2.subs(hsub))

# ---- tadpoles ----
tad00 = sp.expand(L1.coeff(hsym(0, 0), 1).subs(ceros))
tad11 = sp.expand(L1.coeff(hsym(1, 1), 1).subs(ceros))
sol_tad = sp.solve([tad00, tad11], [D1['Y'], D1['b']])

dif = sp.expand((Lpi2 - Lmass_sub).subs(sol_tad))

# ---- canonicalizacion mod derivadas totales:
#      J^A_m J^B_n ~ J^A_n J^B_m  para A != B  (integracion por partes) ----
def simetrizar(expr):
    expr = sp.expand(expr)
    out = 0
    for term in expr.as_ordered_terms():
        c, facts = term.as_coeff_Mul()
        pw = sp.Poly(facts, *J.values()).monoms()[0] if facts != 1 else None
        Jlist = []
        for idx, exp_ in enumerate(pw or []):
            for _ in range(exp_):
                Jlist.append(list(J.values())[idx])
        if len(Jlist) != 2:
            out += term
            continue
        s1, s2 = Jlist
        inv = {v: k for k, v in J.items()}
        (A, mu), (B, nu) = inv[s1], inv[s2]
        if A == B:
            out += term
        else:
            out += c * sp.Rational(1, 2) * (J[(A, mu)] * J[(B, nu)] +
                                            J[(A, nu)] * J[(B, mu)])
    return sp.expand(out)

resto = sp.simplify(simetrizar(dif))
print('== CAL-4: L_fonones - L_masas[dpi], mod deriv. totales, con tadpoles ==')
print('resto =', resto)

# ---- CAL-4b: sector transversal pi^1 = f(t,z) ----
sub_T = {v: 0 for v in J.values()}
ft, fz = sp.symbols('ft fz')
sub_T[J[(1, 0)]] = ft; sub_T[J[(1, 3)]] = fz
LT = sp.expand(Lpi2.subs(sub_T).subs(sol_tad))
ms = masas(L2)
m1_tad = sp.expand(ms['m1^2'].subs(sol_tad))
m2_tad = sp.expand(ms['m2^2'].subs(sol_tad))
print('\n== CAL-4b: sector transversal ==')
print('L_T =', sp.collect(LT, [ft, fz]))
print('L_T - (1/2)(m1^2 ft^2 - m2^2 fz^2) =',
      sp.simplify(LT - sp.Rational(1, 2) * (m1_tad * ft**2 - m2_tad * fz**2)))

# ---- CAL-3a: U(X, w1, w2, w3)  =>  m1^2 = 0 identicamente ----
eta4 = sp.diag(-1, 1, 1, 1)
G1m = -(eta4 * mm.h * eta4)
G2m = (eta4 * mm.h * eta4 * mm.h * eta4)
Bu1 = G1m[1:4, 1:4]; Bu2 = G2m[1:4, 1:4]
Vu = [G1m[0, a] for a in (1, 2, 3)]
Zu = sp.Matrix(3, 3, lambda a, b: Vu[a] * Vu[b])
W1, W2 = Bu1, Bu2 + Zu     # W = B - Z/X, X0 = -1
trW1 = W1.trace(); trW2 = W2.trace(); trW1sq = (W1 * W1).trace()
wops = {1: (3, trW1, trW2), 2: (3, 2 * trW1, 2 * trW2 + trW1sq),
        3: (3, 3 * trW1, 3 * trW2 + 3 * trW1sq)}
nmW = ['X', 'w1', 'w2', 'w3']
opsW = {'X': (mm.ops['X'][0], mm.ops['X'][1], mm.ops['X'][2]),
        'w1': wops[1], 'w2': wops[2], 'w3': wops[3]}
G1s = {k: sp.Symbol('G_' + k) for k in nmW}
G2s = {}
for i, k in enumerate(nmW):
    for l in nmW[i:]:
        G2s[(k, l)] = G2s[(l, k)] = sp.Symbol('G_' + k + l)
G0 = sp.Symbol('G0')
Glin1 = sp.expand(sum(G1s[k] * opsW[k][1] for k in nmW))
Glin2 = sp.expand(sum(G1s[k] * opsW[k][2] for k in nmW))
Gquad2 = sp.expand(sp.Rational(1, 2) * sum(G2s[(k, l)] * opsW[k][1] * opsW[l][1]
                                           for k in nmW for l in nmW))
L2W = sp.expand(G0 * mm.sqg[2] + mm.sqg[1] * Glin1 + Glin2 + Gquad2)
msW = masas(L2W)
print('\n== CAL-3a: U(X,wn) [Phi^a -> Phi^a + f^a(Phi^0)] ==')
for k, v in msW.items():
    print(k, '=', sp.simplify(v))
