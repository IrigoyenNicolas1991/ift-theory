"""
PARTE B: el medio U(X,Y) como realizacion de la fase protegida de Dubovsky.

  Simetria: Phi^a -> Psi^a(Phi^b)  (difeos espaciales internos, indep. de Phi^0)
  Invariantes LO: X = C^00,  Y = u.dPhi^0   (y W := V.B^{-1}.V = X + Y^2, Schur)

Chequeos:
  B1) masas de U(X,Y) off-shell y on-shell (tadpoles Minkowski)
  B2) ejemplo explicito con m0^2 m1^2 > 0 (condicion no-fantasma, Dubovsky eq 75)
  B3) identidad de Schur V.B^{-1}.V = X + Y^2 (numerico, metrica aleatoria)
  B4) invariancia NO-lineal de X e Y bajo Phi^a -> Psi^a(Phi^b) (numerico)
  B5) CAL-5: invariancia del patron de masas bajo delta h_ij = d_i xi_j + d_j xi_i
      (xi indep. de t)  <=>  m2 = m3 = m4 = 0   (Dubovsky eq 71 => 72)
  B6) lema de exclusion: rigidez de corte del medio general vs fase protegida
"""
import sympy as sp
import random
from masas_medio import L1, L2, masas, ceros, hsym, names, D1, D2, U0

# ---------- B1: masas de U(X,Y) ----------
solo_XY = {D1[k]: 0 for k in names if k not in ('X', 'Y')}
for (k, l), s in list(D2.items()):
    if k not in ('X', 'Y') or l not in ('X', 'Y'):
        solo_XY[s] = 0

L2XY = sp.expand(L2.subs(solo_XY))
L1XY = sp.expand(L1.subs(solo_XY))
ms = {k: sp.expand(v.subs(solo_XY)) for k, v in masas(L2).items()}
print('== B1: masas U(X,Y) OFF-shell ==')
for k, v in ms.items():
    print(' ', k, '=', v)

t00 = sp.expand(L1XY.coeff(hsym(0, 0), 1).subs(ceros))
t11 = sp.expand(L1XY.coeff(hsym(1, 1), 1).subs(ceros))
print('tadpoles: t00 =', t00, ' | t11 =', t11)
sol = sp.solve([t00, t11], [U0, D1['Y']])
print('solucion de vacio Minkowski:', sol)
print('== B1: masas U(X,Y) ON-shell (vacio Minkowski) ==')
on = {}
for k, v in ms.items():
    on[k] = sp.simplify(v.subs(sol))
    print(' ', k, '=', on[k])

# ---------- B2: ejemplo explicito ----------
#  U = (X+1) + 2(Y-1) + (1/2)(X+1)^2   =>  U_X=1, U_Y=2, U_XX=1, resto 0
ej = {D1['X']: 1, D2[('X', 'X')]: 1, D2[('X', 'Y')]: 0, D2[('Y', 'Y')]: 0}
print('\n== B2: ejemplo U = (X+1) + 2(Y-1) + (X+1)^2/2 ==')
vals = {k: sp.simplify(v.subs(ej)) for k, v in on.items()}
print('  masas on-shell:', vals)
print('  no-fantasma m0^2*m1^2 > 0 :', vals['m0^2'] * vals['m1^2'] > 0)

# ---------- B3: identidad de Schur (numerico) ----------
random.seed(7)
def rnd(): return sp.Rational(random.randint(-20, 20), 37)
while True:
    g = sp.Matrix(4, 4, lambda i, j: 0)
    for i in range(4):
        for j in range(i, 4):
            g[i, j] = g[j, i] = sp.Rational(-1 if i == j == 0 else (1 if i == j else 0)) + rnd()
    if g.det() != 0 and g[0, 0] != 0:
        break
gi = g.inv()
X_ = gi[0, 0]; V_ = sp.Matrix([gi[0, a] for a in (1, 2, 3)])
B_ = gi[1:4, 1:4]
Y_ = 1 / sp.sqrt(-g[0, 0])
lhs = (V_.T * B_.inv() * V_)[0, 0]
print('\n== B3: Schur  V.B^{-1}.V - (X + Y^2) =',
      sp.simplify(lhs - (X_ + Y_**2)), '==')

# ---------- B4: invariancia no lineal de X, Y (numerico) ----------
# campo Phi generico y difeo espacial Psi^a cuadratico; metrica aleatoria g
tx = sp.symbols('t x y z', real=True)
Phi0 = tx[0] + sp.Rational(1, 5) * tx[1] * tx[3] + sp.Rational(1, 7) * tx[0]**2
Phia = [tx[a] + sp.Rational(1, 3 + a) * tx[0] * tx[(a % 3) + 1] for a in (1, 2, 3)]
def invariantes(Ph0, Pha, gmat, punto):
    dP = sp.Matrix(4, 4, lambda A, m: sp.diff(([Ph0] + Pha)[A], tx[m]))
    gi_ = gmat.inv()
    C_ = dP * gi_ * dP.T
    Xv = C_[0, 0]
    # u: resolver u.dPhi^a = 0, normalizar con g
    uv = sp.Matrix(sp.symbols('v0 v1 v2 v3'))
    eqs = [(uv.T * dP[a, :].T)[0, 0] for a in (1, 2, 3)]
    solu = sp.solve(eqs, [uv[1], uv[2], uv[3]], dict=True)[0]
    uvec = uv.subs(solu)
    n2 = (uvec.T * gmat * uvec)[0, 0]
    uvec = uvec / sp.sqrt(-n2)
    Yv = (uvec.T * dP[0, :].T)[0, 0]
    reemp = dict(zip(tx, punto))
    return (Xv.subs(reemp), sp.simplify(Yv.subs(reemp).subs(uv[0], 1)))
punto = [sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(-1, 4), sp.Rational(2, 5)]
Xa, Ya = invariantes(Phi0, Phia, g, punto)
# difeo espacial interno Psi^a(Phi^b) (cuadratico, indep de Phi^0):
Psi = [Phia[0] + sp.Rational(1, 6) * Phia[1]**2,
       Phia[1] - sp.Rational(1, 4) * Phia[0] * Phia[2],
       Phia[2] + sp.Rational(1, 9) * Phia[0]**2]
Xb, Yb = invariantes(Phi0, Psi, g, punto)
print('\n== B4: invariancia no lineal bajo Phi^a -> Psi^a(Phi^b) ==')
print('  Delta X =', sp.simplify(Xa - Xb), ' | Delta Y =', sp.simplify(Ya - Yb),
      '  (Y^2:', sp.simplify(Ya**2 - Yb**2), ')')

# ---------- B5 (CAL-5): variacion de L_m bajo h_ij -> h_ij + d_i xi_j + d_j xi_i ----------
# xi = xi(x) indep de t => delta h_00 = 0, delta h_0i = 0.
# A nivel de masas: basta chequear invariancia del patron cuadratico:
xi = sp.MatrixSymbol('xi', 3, 3)  # representamos d_i xi_j como matriz constante s
s = sp.Matrix(3, 3, lambda i, j: sp.Symbol('s%d%d' % (i, j)))
hshift = {}
for i in range(1, 4):
    for j in range(i, 4):
        hshift[hsym(i, j)] = hsym(i, j) + s[i - 1, j - 1] + s[j - 1, i - 1]
dL = sp.expand(L2.subs(hshift) - L2)
# terminos lineales en h (los cuadraticos en s no importan para la variacion):
dL_h = sum(sp.expand(dL.coeff(hsym(i, j), 1).subs(ceros)) * hsym(i, j)
           for i in range(4) for j in range(i, 4))
msym = masas(L2)
cond = sp.solve([msym['m2^2'], msym['m3^2'], msym['m4^2']],
                exclude=[], dict=False, manual=False) if False else None
dL_h_en_fase = sp.expand(dL_h.subs(solo_XY).subs(sol))
print('\n== B5: variacion de L_m bajo la simetria (71), fase U(X,Y) on-shell ==')
print('  delta L_m (parte lineal en h) =', sp.simplify(dL_h_en_fase))

# ---------- B6: lema de exclusion ----------
# rigidez de corte (coef de fz^2 en L_T, CAL-4b) para el medio general:
G_T = D1['t1'] + 4 * D1['t2'] + 9 * D1['t3']
K_T = D1['X'] + D1['y0'] + D1['y1'] + D1['y2'] + D1['y3']
m1g = masas(L2)['m1^2']; m2g = masas(L2)['m2^2']
tad00g = sp.expand(L1.coeff(hsym(0, 0), 1).subs(ceros))
tad11g = sp.expand(L1.coeff(hsym(1, 1), 1).subs(ceros))
solg = sp.solve([tad00g, tad11g], [D1['Y'], D1['b']])
print('\n== B6: lema de exclusion (medio general, on-shell) ==')
print('  m1^2 = 2*K_T ? ->', sp.simplify(sp.expand(m1g.subs(solg)) - 2 * K_T))
print('  m2^2 = -2*G_T ? ->', sp.simplify(sp.expand(m2g.subs(solg)) + 2 * G_T))
print('  => v_T^2 = m2^2/m1^2 ; fonones de corte propagan  <=>  m1^2 m2^2 != 0')
