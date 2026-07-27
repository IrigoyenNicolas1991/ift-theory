# -*- coding: utf-8 -*-
"""
exhaustividad_XY.py — item 9 de la lista de bloqueo del paper "missing row":
COMPLETITUD del par {X, Y} al orden dominante (los scripts previos verifican
invariancia; ESTE verifica exhaustividad).

LEMA (completitud de {X, Y} a LO) que este script respalda:

  Contrato LO (Dubovsky ecs. 14-15; BCP sec. 2): el Lagrangiano de orden
  dominante es una funcion de las primeras derivadas de los Phi^A solamente
  (un derivativo por campo). Sus bloques escalares bajo difeos del
  espacio-tiempo son la matriz de Gram C^{AB} = g^{mn} d_m Phi^A d_n Phi^B
  — es decir X = C^00, V^a = C^{0a}, B^{ab} = C^{ab} — mas el jacobiano
  orientado Z = eps^{mnlr} d_m Phi^0 d_n Phi^1 d_l Phi^2 d_r Phi^3 / sqrt(-g)
  (el unico bloque LO que no es funcion de C: porta la orientacion; Z^2 si es
  funcion de C). Todo operador con d^2 Phi (equivalentemente dC, o curvatura
  extrinseca) es NLO por definicion y queda fuera del lema.

  Grupo: difeos espaciales internos IRRESTRICTOS, Phi^a -> Psi^a(Phi^b) con
  det(dPsi/dPhi) != 0 arbitrario (orientacion interna preservada: det > 0),
  Phi^0 intacto. Accion puntual inducida (regla de la cadena, chequeo E1):

      X -> X ,  V -> J V ,  B -> J B J^T ,  Z -> det(J) Z ,
      J = (dPsi/dPhi)|_{Phi(x)} en GL+(3), arbitraria punto a punto.

  Dominio fisico D: B definida positiva (etiquetas espaciales no degeneradas)
  y det C != 0 (el reloj no cae en el span de las etiquetas). El fondo
  Minkowski (X=-1, V=0, B=Id, Y=1) esta en D.

  ENUNCIADO. Sobre D, con la orientacion temporal fijada (u futuro-dirigido):
   (i)   X y W := V.B^{-1}.V son invariantes exactos del grupo;
   (ii)  las orbitas de GL+(3) en D son EXACTAMENTE las fibras del par (X, W)
         [forma normal (X, V, B) -> (X, (sqrt(W),0,0), Id); vale tambien en el
         estrato V = 0, donde la fibra de (X, 0) es una sola orbita];
   (iii) por lo tanto todo invariante continuo construido con C es funcion de
         (X, W); el numero de invariantes funcionalmente independientes es
         2 = dim(espacio 10) - dim(orbita generica 8);
   (iv)  Schur: det C = det B * (X - W), (C^{-1})_00 = 1/(X - W), y por la
         definicion geometrica de u (u.dPhi^a = 0, normalizada):
         Y^2 = W - X y (Z/b)^2 = Y^2, con el signo de Y fijado por la
         orientacion temporal y el de Z/b por la interna. Sobre D el par
         (X, Y) es entonces equivalente al par (X, W): U(X, W) = U(X, Y).
   (v)   El bloque Z NO es invariante (Z -> det J * Z, y det J es libre): la
         columna volumen-preservante de la tabla (b, y todo lo que dependa de
         Z mas alla de Z/b) muere; Z/b = +-Y no agrega nada nuevo.

  Corolario (E7): sin el reloj Phi^0 no hay fila: la accion de GL(3) sobre B
  sola es localmente transitiva (rank 6 = dim), asi que un medio de solo Phi^a
  con simetria irrestricta solo admite U = const. El reloj es obligatorio.

Chequeos (todo en aritmetica exacta, racionales; sin flotantes):
  E1  reduccion puntual: un difeo interno NO lineal actua sobre C(x0) y Z(x0)
      exactamente via su jacobiana K = diag(1, J) y det J (regla de la cadena).
      Justifica que jacobianas LINEALES agotan la accion puntual: los datos
      superiores del jet (d^2 Psi) solo entran via dC = NLO.
  E2  Schur simbolico general: det C - det B*(X - W) = 0 en las 10 variables;
      y sobre una configuracion exacta (Phi, g) aleatoria: Y^2 = W - X con Y
      computado por su definicion geometrica, y Z^2 = -det C * (-det g)^{-1}
      (aqui Zhat := det dPhi, Zhat^2 = -det C * (-det g)).
  E3  conteo de orbitas: accion infinitesimal de gl(3) en R^10; en puntos
      genericos rank = 8 y estabilizador dim 1 => 10 - 8 = 2 invariantes.
      E3b calibracion contra fila CONOCIDA: restringiendo a sl(3) (volumen
      preservante) rank = 7 => 3 invariantes {X, W, det B} — la fila
      superfluida U(X, Y, b) de BCP Tabla 2. El metodo reproduce lo conocido.
  E4  invariancia infinitesimal SIMBOLICA de W (delta W = 0 identicamente en
      B, V, eps genericos) y clausura: {grad X, grad W} generan el anulador
      del tangente de la orbita => todo invariante local es funcionalmente
      dependiente de (X, W).
  E5  separacion GLOBAL constructiva: dos configuraciones con los mismos
      (X, W) se conectan por un J EXPLICITO racional del grupo (factorizacion
      B = A A^T + reflexion de Householder), con det J generico != 1; idem en
      el estrato V = 0. Las fibras de (X, W) son orbitas exactas.
  E6  candidatos dirimidos: W = V.B^{-1}.V es invariante y W = X + Y^2 (Schur);
      Z' = V.(C^{-1})_esp.V es invariante pero Z' = W X/(X - W) (Sherman-
      Morrison); (C^{-1})_00 = 1/(X - W) = -1/Y^2. Ninguno agrega nada.
      Controles negativos: tau_1 = Tr B, b^2 = det B, y_0 = V.V NO son
      invariantes del grupo irrestricto (mueren al liberar el determinante).
  E7  corolario sin-reloj: rank de la accion sobre B sola = 6 => 0 invariantes.

Ejecutar:  py -3.14 exhaustividad_XY.py   (sympy; ~10-30 s)
"""

import random
import sys

import sympy as sp

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

random.seed(9)
RES = []


def check(nombre, cond):
    ok = bool(cond)
    RES.append((nombre, ok))
    print(('  [PASS] ' if ok else '  [FAIL] ') + nombre)
    return ok


def rq(lo=-6, hi=6):
    return sp.Rational(random.randint(lo, hi), random.choice((1, 2, 3, 5)))


def rq_nz(lo=-6, hi=6):
    while True:
        v = rq(lo, hi)
        if v != 0:
            return v


# =====================================================================
# E1 — Reduccion puntual: el difeo NO lineal actua sobre C(x0), Z(x0)
#      exactamente via su jacobiana en el punto (regla de la cadena).
# =====================================================================
print('== E1: reduccion puntual (difeo no lineal = su jacobiana en x0) ==')

tx = sp.symbols('t x y z', real=True)
Phi0 = tx[0] + sp.Rational(1, 5) * tx[1] * tx[3] + sp.Rational(1, 7) * tx[0] ** 2
Phia = [tx[1] + sp.Rational(1, 4) * tx[0] * tx[2],
        tx[2] - sp.Rational(1, 6) * tx[1] * tx[3],
        tx[3] + sp.Rational(1, 9) * tx[0] * tx[1]]

# difeo interno NO lineal en el espacio de etiquetas (det variable, != 1):
ph = sp.symbols('ph1 ph2 ph3')
Psi_forma = [ph[0] + sp.Rational(1, 6) * ph[1] ** 2 + sp.Rational(1, 3) * ph[0],
             ph[1] - sp.Rational(1, 4) * ph[0] * ph[2],
             ph[2] + sp.Rational(1, 9) * ph[0] ** 2 - sp.Rational(1, 5) * ph[2]]
Psia = [f.subs(dict(zip(ph, Phia))) for f in Psi_forma]

# metrica racional aleatoria cerca de eta (invertible en el punto):
while True:
    gm = sp.zeros(4, 4)
    for i in range(4):
        for j in range(i, 4):
            base = sp.Integer(-1 if i == j == 0 else (1 if i == j else 0))
            gm[i, j] = gm[j, i] = base + sp.Rational(random.randint(-3, 3), 17)
    if gm.det() != 0:
        break

punto = dict(zip(tx, [sp.Rational(1, 3), sp.Rational(1, 2),
                      sp.Rational(-1, 4), sp.Rational(2, 5)]))
gp = gm.subs(punto)
gip = gp.inv()


def C_y_dP(campos):
    dP = sp.Matrix(4, 4, lambda A, m: sp.diff(campos[A], tx[m])).subs(punto)
    return sp.expand(dP * gip * dP.T), dP


C1, dP1 = C_y_dP([Phi0] + Phia)
C2, dP2 = C_y_dP([Phi0] + Psia)

Jint = sp.Matrix(3, 3, lambda a, b: sp.diff(Psi_forma[a], ph[b]))
Jp = Jint.subs(dict(zip(ph, [f.subs(punto) for f in Phia])))
K = sp.diag(1, Jp)

check('C(Psi o Phi) = K C(Phi) K^T exacto (K = diag(1, dPsi/dPhi|x0))',
      sp.simplify(C2 - K * C1 * K.T) == sp.zeros(4, 4))
Zh1 = dP1.det()
Zh2 = dP2.det()
check('Zhat(Psi o Phi) = det(J) * Zhat(Phi) exacto (bloque de orientacion)',
      sp.simplify(Zh2 - Jp.det() * Zh1) == 0)
print('   det J en x0 =', Jp.det(), ' (ni 1 ni constante: grupo irrestricto)')

# =====================================================================
# E2 — Schur simbolico general + Y geometrico sobre la configuracion E1.
# =====================================================================
print('\n== E2: identidad de Schur y el par (X, W) <-> (X, Y) ==')

xs = sp.Symbol('X')
vs = sp.Matrix(sp.symbols('v1 v2 v3'))
bs = sp.Matrix(3, 3, lambda i, j: sp.Symbol('b%d%d' % (min(i, j) + 1, max(i, j) + 1)))
Cs = sp.Matrix(4, 4, lambda i, j: xs if i == j == 0
               else (vs[j - 1] if i == 0 else (vs[i - 1] if j == 0 else bs[i - 1, j - 1])))
Ws = (vs.T * bs.adjugate() * vs)[0, 0]          # W * det B (polinomico)
schur = sp.expand(Cs.det() - (xs * bs.det() - Ws))
check('det C = det B * (X - W) identicamente (10 variables libres)', schur == 0)

# Y por su definicion geometrica sobre la configuracion exacta de E1:
uv = sp.Matrix(sp.symbols('u0 u1 u2 u3'))
eqs = [(uv.T * dP1[a, :].T)[0, 0] for a in (1, 2, 3)]
solu = sp.solve(eqs, [uv[1], uv[2], uv[3]], dict=True)[0]
uvec = uv.subs(solu).subs(uv[0], 1)
n2 = (uvec.T * gp * uvec)[0, 0]
Yg = (uvec / sp.sqrt(-n2)).T * dP1[0, :].T      # Y = u . dPhi^0
Yg = Yg[0, 0]

X1 = C1[0, 0]
V1 = C1[1:4, 0]
B1 = C1[1:4, 1:4]
W1 = (V1.T * B1.inv() * V1)[0, 0]
check('Y^2 = W - X sobre configuracion exacta (Y geometrico, u.dPhi^a = 0)',
      sp.simplify(Yg ** 2 - (W1 - X1)) == 0)
check('Zhat^2 = -det C * (-det g)  (Z^2 es funcion de C: solo el signo es extra)',
      sp.simplify(Zh1 ** 2 - (-C1.det()) * (-gp.det())) == 0)

X2 = C2[0, 0]
V2 = C2[1:4, 0]
B2 = C2[1:4, 1:4]
W2 = (V2.T * B2.inv() * V2)[0, 0]
check('invariancia no lineal: Delta X = 0 y Delta W = 0 bajo Psi',
      sp.simplify(X2 - X1) == 0 and sp.simplify(W2 - W1) == 0)

# =====================================================================
# E3 — Conteo de orbitas: accion infinitesimal de gl(3) sobre (X, V, B).
# =====================================================================
print('\n== E3: conteo de invariantes = dim(espacio) - dim(orbita generica) ==')


def coords(dX, dV, dB):
    return [dX, dV[0], dV[1], dV[2],
            dB[0, 0], dB[0, 1], dB[0, 2], dB[1, 1], dB[1, 2], dB[2, 2]]


def matriz_accion(base_eps, V, B):
    filas = []
    for e in base_eps:
        dV = e * V
        dB = e * B + B * e.T
        filas.append(coords(0, dV, dB))
    return sp.Matrix(filas)


gl3 = [sp.Matrix(3, 3, lambda a, b: 1 if (a, b) == (i, j) else 0)
       for i in range(3) for j in range(3)]
sl3 = ([sp.Matrix(3, 3, lambda a, b: 1 if (a, b) == (i, j) else 0)
        for i in range(3) for j in range(3) if i != j]
       + [sp.diag(1, -1, 0), sp.diag(0, 1, -1)])


def punto_generico():
    while True:
        A = sp.Matrix(3, 3, lambda i, j: rq())
        if A.det() != 0:
            break
    B = A * A.T                       # definida positiva racional
    V = sp.Matrix([rq_nz(), rq_nz(), rq()])
    X = rq_nz()
    return X, V, B


rangos, kers = [], []
puntos = [punto_generico() for _ in range(3)]
for X_, V_, B_ in puntos:
    M = matriz_accion(gl3, V_, B_)
    rangos.append(M.rank())
    kers.append(9 - M.rank())
check('rank(accion gl(3)) = 8 en 3 puntos genericos => orbita 8-dim', rangos == [8, 8, 8])
check('estabilizador generico dim 1 (kernel de la accion)', kers == [1, 1, 1])
print('   invariantes funcionalmente independientes = 10 - 8 = 2  <->  {X, W}')

M0 = matriz_accion(gl3, sp.zeros(3, 1), sp.eye(3))
print('   (estrato no generico V = 0: rank cae a %d; la separacion global' % M0.rank())
print('    de ese estrato la da E5b, no el conteo local)')

rangos_sl = [matriz_accion(sl3, V_, B_).rank() for X_, V_, B_ in puntos]
check('E3b calibracion sl(3) (volumen-pres.): rank = 7 => 3 invariantes {X, W, det B} '
      '= fila U(X,Y,b) de BCP', rangos_sl == [7, 7, 7])

# =====================================================================
# E4 — delta W = 0 simbolico y {dX, dW} generan el anulador de la orbita.
# =====================================================================
print('\n== E4: invariancia simbolica de W y clausura de {X, W} ==')

eps_s = sp.Matrix(3, 3, lambda i, j: sp.Symbol('e%d%d' % (i + 1, j + 1)))
Badj = bs.adjugate()
detb = bs.det()
dVs = eps_s * vs
dBs = eps_s * bs + bs * eps_s.T
# delta W * (det B)^2, polinomico (W = v.B^{-1}.v, B^{-1} = adj/det):
dW_pol = sp.expand(
    detb * (dVs.T * Badj * vs)[0, 0]
    + detb * (vs.T * Badj * dVs)[0, 0]
    - (vs.T * Badj * dBs * Badj * vs)[0, 0])
check('delta W = 0 identicamente (B, V, eps genericos; 18 simbolos)', dW_pol == 0)

vars10 = [xs, vs[0], vs[1], vs[2],
          bs[0, 0], bs[0, 1], bs[0, 2], bs[1, 1], bs[1, 2], bs[2, 2]]
W_sym = (vs.T * Badj * vs)[0, 0] / detb
gradW_sym = [sp.diff(W_sym, q) for q in vars10]
gradX = sp.Matrix([1] + [0] * 9)

ok4 = True
for X_, V_, B_ in puntos:
    sub = dict(zip(vars10, coords(X_, V_, B_)))
    gW = sp.Matrix([sp.cancel(gexpr.subs(sub)) for gexpr in gradW_sym])
    M = matriz_accion(gl3, V_, B_)
    anulado = sp.simplify(M * gW) == sp.zeros(9, 1)
    indep = sp.Matrix.hstack(gradX, gW).rank() == 2
    # anulador de la orbita: dim = 10 - rank(M) = 2; contiene 2 independientes
    ok4 = ok4 and anulado and indep and (10 - M.rank() == 2)
check('{grad X, grad W} generan el anulador (dim 2) del tangente de la orbita '
      '=> todo invariante local depende de (X, W)', ok4)

# =====================================================================
# E5 — Separacion global: mismos (X, W) => mismo punto por un J explicito.
# =====================================================================
print('\n== E5: dos configuraciones con mismos (X, W) estan en la MISMA orbita ==')


def A_invertible():
    while True:
        A = sp.Matrix(3, 3, lambda i, j: rq())
        if A.det() != 0:
            return A


A1, A2 = A_invertible(), A_invertible()
V0 = sp.Matrix([rq_nz(), rq_nz(), rq_nz()])
V0p = sp.Matrix([-V0[2], V0[0], -V0[1]])        # misma norma, otra direccion
Bx, By = A1 * A1.T, A2 * A2.T
Vx, Vy = A1 * V0, A2 * V0p
Xc = rq_nz()

Wx = (Vx.T * Bx.inv() * Vx)[0, 0]
Wy = (Vy.T * By.inv() * Vy)[0, 0]
check('las dos configuraciones tienen el mismo W = V.B^{-1}.V (por construccion)',
      sp.simplify(Wx - Wy) == 0 and sp.simplify(Wx - (V0.T * V0)[0, 0]) == 0)

u_h = V0 - V0p
H = sp.eye(3) - 2 * (u_h * u_h.T) / (u_h.T * u_h)[0, 0]   # Householder: H V0 = V0p
Jsep = A2 * H * A1.inv()
check('J explicito del grupo: J Vx = Vy y J Bx J^T = By (exacto, racional)',
      sp.simplify(Jsep * Vx - Vy) == sp.zeros(3, 1)
      and sp.simplify(Jsep * Bx * Jsep.T - By) == sp.zeros(3, 3))
print('   det J =', sp.nsimplify(Jsep.det()), ' (generico: la conexion NO usa det = 1)')

Jb = A2 * A1.inv()
check('E5b estrato V = 0: (X, 0, B) ~ (X, 0, B\') via J = A\' A^{-1} '
      '(la fibra de (X, 0) es una sola orbita)',
      sp.simplify(Jb * Bx * Jb.T - By) == sp.zeros(3, 3))

# =====================================================================
# E6 — Candidatos dirimidos y controles negativos.
# =====================================================================
print('\n== E6: candidatos (todos funcion de (X, W)) y controles negativos ==')

ok_zp, ok_c00, ok_inv = True, True, True
for X_, V_, B_ in puntos:
    C4 = sp.Matrix(4, 4, lambda i, j: X_ if i == j == 0
                   else (V_[j - 1] if i == 0 else (V_[i - 1] if j == 0 else B_[i - 1, j - 1])))
    if C4.det() == 0:
        continue
    Ci = C4.inv()
    W_ = (V_.T * B_.inv() * V_)[0, 0]
    Zp = sum(V_[a] * Ci[1 + a, 1 + b] * V_[b] for a in range(3) for b in range(3))
    ok_zp = ok_zp and sp.simplify(Zp - W_ * X_ / (X_ - W_)) == 0
    ok_c00 = ok_c00 and sp.simplify(Ci[0, 0] - 1 / (X_ - W_)) == 0
check("Z' = V.(C^{-1})_esp.V = W X/(X-W) exacto (Sherman-Morrison): nada nuevo", ok_zp)
check('(C^{-1})_00 = 1/(X - W) = -1/Y^2 exacto: nada nuevo', ok_c00)

while True:
    Jr = sp.Matrix(3, 3, lambda i, j: rq())
    if Jr.det() not in (0, 1, -1):
        break
X_, V_, B_ = puntos[0]
Vt, Bt = Jr * V_, Jr * B_ * Jr.T
Wt = (Vt.T * Bt.inv() * Vt)[0, 0]
W_ = (V_.T * B_.inv() * V_)[0, 0]
check('W invariante bajo J finita aleatoria con det J = %s' % Jr.det(),
      sp.simplify(Wt - W_) == 0)

d_tau1 = sp.simplify(Bt.trace() - B_.trace())
d_detB = sp.simplify(Bt.det() - B_.det())
d_y0 = sp.simplify((Vt.T * Vt)[0, 0] - (V_.T * V_)[0, 0])
check('controles negativos: tau_1, b^2 = det B, y_0 NO son invariantes '
      '(las columnas volumen-preservantes mueren)',
      d_tau1 != 0 and d_detB != 0 and d_y0 != 0)
print('   Delta tau_1 =', d_tau1, '| Delta det B =', d_detB, '| Delta y_0 =', d_y0)

# =====================================================================
# E7 — Corolario: sin reloj no hay fila (medio de solo Phi^a => U = const).
# =====================================================================
print('\n== E7: corolario sin-reloj ==')
rangos_B = []
for X_, V_, B_ in puntos:
    MB = sp.Matrix([[ (e * B_ + B_ * e.T)[i, j] for (i, j) in
                      [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)] ]
                    for e in gl3])
    rangos_B.append(MB.rank())
check('accion de gl(3) sobre B sola: rank = 6 = dim => 0 invariantes '
      '(solo Phi^a irrestricto => U = const; el reloj es obligatorio)',
      rangos_B == [6, 6, 6])

# =====================================================================
print('\n' + '=' * 70)
fallos = [n for n, ok in RES if not ok]
if fallos:
    print('VEREDICTO: FAIL — chequeos caidos:')
    for n in fallos:
        print('  -', n)
    raise SystemExit(1)
print('VEREDICTO: PASS — %d/%d chequeos.' % (len(RES), len(RES)))
print("""
Conclusion (item 9): al orden dominante (un derivativo por campo, bloques
C^{AB} y Z), los invariantes del grupo irrestricto Phi^a -> Psi^a(Phi^b) sobre
el dominio fisico (B > 0, det C != 0, orientaciones fijadas) son EXACTAMENTE
dos: {X, W = X + Y^2}, equivalentes a {X, Y}. Conteo 10 - 8 = 2 (E3), realizado
por X y W (E4), con separacion global constructiva (E5); Z aporta solo el signo
de Y (E1/E2); todo candidato adicional es funcion de (X, Y) (E6). La
clasificacion NO cubre operadores NLO (con dC / curvatura extrinseca): esos
son los de la sec. 6 del paper y no entran en U.""")
