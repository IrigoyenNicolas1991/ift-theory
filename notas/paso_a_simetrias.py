# -*- coding: utf-8 -*-
"""
Paso A (nota 12) — Verificaciones del patrón de ruptura SL(3) x SO(3) -> SO(3)_diag.

Cuatro chequeos, cada uno con su criterio de éxito explícito:

  1. COSET: los generadores rotos de SL(3)/SO(3) son las matrices simétricas sin
     traza (5 = dimensión de un J=2), y forman una representación IRREDUCIBLE
     bajo el SO(3) diagonal no roto (conmutar con so(3) no saca del espacio,
     y ningún subespacio propio es invariante).

  2. NO-POTENCIAL (el candidato a teorema de protección de m2=0): la órbita de
     la identidad bajo congruencia SL(3) (Q -> M Q M^T, det M = 1) cubre TODO
     el espacio de matrices simétricas definidas positivas unimodulares.
     => toda función invariante es constante => no existe potencial para el
     sector de forma => término de masa prohibido por simetría.

  3. ESPECTRO DEL SIGMA MODEL: expandiendo Q = exp(pi) (pi simétrica sin traza)
     el lagrangiano L = (1/4)[Tr((Q^-1 dQ/dt)^2) - c^2 Tr((Q^-1 dQ/dx_i)^2)]
     da a orden cuadrático 5 ondas SIN MASA desacopladas con omega = c k,
     que bajo helicidad (propagación en z) se parten en 0, ±1, ±2.
     HONESTIDAD: acá los 5 modos son no masivos; silenciar 0 y ±1 es tarea
     del acople con vínculos (Paso C), no de esta nota.

  4. LA MINA (declarada, no escondida): si el sector fluido B_ab = d_phi·d_phi
     transforma bajo el MISMO SL(3) que Q, el invariante mixto Tr(Q^-1 B)
     evaluado en el fondo B = delta genera masa: Tr(exp(-pi)) = 3 + Tr(pi^2)/2 + ...
     (la traza de pi es cero, así que el término lineal muere pero el
     cuadrático NO). => el acople fluido-cuadrupolo puede resucitar m2.
     Este es EL peligro del Paso B.

Uso: python paso_a_simetrias.py   (imprime PASS/FAIL por chequeo)
"""

import numpy as np
import sympy as sp

rng = np.random.default_rng(20260719)
ok_all = True


def check(nombre, cond):
    global ok_all
    print(f"[{'PASS' if cond else 'FAIL'}] {nombre}")
    ok_all = ok_all and cond


# ----------------------------------------------------------------------------
# 1. COSET: sl(3) = so(3) (antisimétricas) + simétricas sin traza (5, J=2)
# ----------------------------------------------------------------------------
# base de so(3) (rotaciones no rotas, diagonal)
J = [np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]], float),
     np.array([[0, 0, 1], [0, 0, 0], [-1, 0, 0]], float),
     np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0]], float)]

# base de simétricas sin traza (los 5 generadores rotos)
S = []
for (i, j) in [(0, 1), (0, 2), (1, 2)]:
    m = np.zeros((3, 3)); m[i, j] = m[j, i] = 1.0
    S.append(m)
S.append(np.diag([1.0, -1.0, 0.0]))
S.append(np.diag([1.0, 1.0, -2.0]) / np.sqrt(3))

# dimensión: sl(3) tiene 8 = 3 (so(3)) + 5 (rotos)
check("coset: dim sl(3) = 3 + 5 (rotos = simétricas sin traza, cuenta J=2)",
      len(J) + len(S) == 8)

# cerradura: [so(3), simétrica-sin-traza] sigue siendo simétrica sin traza
def es_sim_sin_traza(m, tol=1e-12):
    return np.allclose(m, m.T, atol=tol) and abs(np.trace(m)) < tol

cerr = all(es_sim_sin_traza(Ji @ Sk - Sk @ Ji) for Ji in J for Sk in S)
check("coset: [so(3), rotos] no sale del espacio (es una representación)", cerr)

# irreducibilidad bajo SO(3): la acción adjunta de rotaciones sobre el espacio
# de 5 dims no deja subespacio invariante propio. Test: el conmutante de la
# representación es trivial (solo múltiplos de la identidad) — Schur.
def vec(m):
    # coordenadas de m en la base S (base ortogonal respecto a Tr(a·b))
    return np.array([np.trace(m @ s) / np.trace(s @ s) for s in S])

# matrices 5x5 de la acción ad_J sobre el espacio roto
ad = []
for Ji in J:
    cols = [vec(Ji @ Sk - Sk @ Ji) for Sk in S]
    ad.append(np.array(cols).T)

# conmutante: resolver [X, ad_i] = 0 para X 5x5 -> espacio de soluciones dim 1
filas = []
for A in ad:
    # (X A - A X) = 0 como sistema lineal en las 25 entradas de X
    I5 = np.eye(5)
    filas.append(np.kron(A.T, I5) - np.kron(I5, A))
M_sys = np.vstack(filas)
nulidad = 25 - np.linalg.matrix_rank(M_sys, tol=1e-10)
check("coset: representación IRREDUCIBLE bajo SO(3) diagonal (Schur: conmutante dim 1)",
      nulidad == 1)

# ----------------------------------------------------------------------------
# 2. NO-POTENCIAL: la órbita de la identidad cubre todo el espacio de orden
# ----------------------------------------------------------------------------
# Toda Q simétrica def. positiva con det Q = 1 se escribe Q = L L^T con
# det L = 1 (Cholesky reescalado). Entonces Q = M I M^T con M = L en SL(3):
# la identidad llega a cualquier punto => función invariante = constante.
exitos = 0
for _ in range(200):
    A = rng.normal(size=(3, 3))
    Q = A @ A.T + 0.1 * np.eye(3)          # sim. def. positiva
    Q = Q / np.linalg.det(Q) ** (1.0 / 3)  # unimodular
    L = np.linalg.cholesky(Q)              # det L = sqrt(det Q) = 1
    exitos += (abs(np.linalg.det(L) - 1) < 1e-9 and
               np.allclose(L @ L.T, Q, atol=1e-9))
check("no-potencial: 200/200 Q unimodulares alcanzadas desde la identidad vía SL(3)",
      exitos == 200)

# contraste: los candidatos a potencial NO son invariantes (dependen del punto
# de la órbita) — Tr(Q), Tr(Q^2), autovalores... solo det Q es invariante.
A = rng.normal(size=(3, 3)); Q = A @ A.T + 0.1 * np.eye(3)
Q /= np.linalg.det(Q) ** (1 / 3)
Mr = rng.normal(size=(3, 3)); Mr /= np.linalg.det(Mr) ** (1 / 3)  # det = 1
Q2 = Mr @ Q @ Mr.T
check("no-potencial: Tr(Q) NO es invariante (candidato a potencial, muere)",
      abs(np.trace(Q) - np.trace(Q2)) > 1e-6)
check("no-potencial: det(Q) SÍ es invariante (y vale 1: constante, no potencial)",
      abs(np.linalg.det(Q2) - 1) < 1e-9)

# ----------------------------------------------------------------------------
# 3. ESPECTRO: sigma model en SL(3)/SO(3), orden cuadrático -> 5 ondas sin masa
# ----------------------------------------------------------------------------
t, z, c, k, w = sp.symbols("t z c k omega", real=True, positive=True)
eps = sp.symbols("epsilon", real=True)

# pi simétrica sin traza, 5 funciones de (t, z): propagación en z
p = [sp.Function(f"p{i}")(t, z) for i in range(5)]
Pi = sp.Matrix([[p[3] + p[4] / sp.sqrt(3), p[2], p[0]],
                [p[2], -p[3] + p[4] / sp.sqrt(3), p[1]],
                [p[0], p[1], -2 * p[4] / sp.sqrt(3)]])
check("espectro: Pi es simétrica y sin traza (parametrización del coset)",
      sp.simplify(Pi - Pi.T) == sp.zeros(3, 3) and sp.simplify(sp.trace(Pi)) == 0)

# Q = exp(eps*Pi) a segundo orden; Q^-1 dQ = eps dPi + O(eps^2)
Qm = sp.eye(3) + eps * Pi + eps**2 * Pi * Pi / 2
Qinv = sp.eye(3) - eps * Pi + eps**2 * Pi * Pi / 2  # inversa a O(eps^2)
check("espectro: Q*Q^-1 = 1 + O(eps^3)",
      sp.simplify(sp.expand(Qm * Qinv).applyfunc(
          lambda e: sp.series(e, eps, 0, 3).removeO())) == sp.eye(3))

def cuad(dvar):
    Mx = Qinv * sp.diff(Qm, dvar)
    tr = sp.trace(Mx * Mx)
    return sp.simplify(sp.expand(sp.series(tr, eps, 0, 3).removeO() / eps**2))

L2 = sp.Rational(1, 4) * (cuad(t) - c**2 * cuad(z))
# esperado: (1/2) * sum_i [ (dp_i/dt)^2 - c^2 (dp_i/dz)^2 ]  (con la norma de S)
esperado = 0
for i in range(5):
    esperado += sp.diff(p[i], t)**2 - c**2 * sp.diff(p[i], z)**2
# ojo con normas: Tr(S_a S_b) = 2 delta_ab en esta base
esperado = sp.Rational(2, 4) * esperado
check("espectro: L2 = (1/2) sum [(dp/dt)^2 - c^2 (dp/dz)^2] — 5 modos DESACOPLADOS",
      sp.simplify(L2 - esperado) == 0)

# sin masa: L2 no contiene términos p_i^2 (sin derivar)
sin_masa = all(sp.diff(L2, pi_) == 0 for pi_ in p)
check("espectro: ningún término de masa p^2 en L2 (m=0 para las 5 helicidades)",
      sin_masa)

# helicidades bajo rotación alrededor de z: p0,p1 -> ±1 ; p2,p3 -> ±2 ; p4 -> 0
th = sp.symbols("theta", real=True)
Rz = sp.Matrix([[sp.cos(th), -sp.sin(th), 0],
                [sp.sin(th), sp.cos(th), 0],
                [0, 0, 1]])
Pi_const = sp.Matrix([[sp.Symbol(f"a{i}{j}") for j in range(3)] for i in range(3)])
# armar Pi constante simétrica sin traza con 5 símbolos
a = sp.symbols("a0:5", real=True)
Pi_c = sp.Matrix([[a[3] + a[4] / sp.sqrt(3), a[2], a[0]],
                  [a[2], -a[3] + a[4] / sp.sqrt(3), a[1]],
                  [a[1 - 1], a[1], -2 * a[4] / sp.sqrt(3)]])
Pi_c[0, 2] = a[0]; Pi_c[2, 0] = a[0]  # asegurar simetría
Pi_rot = sp.simplify(Rz * Pi_c * Rz.T)
# leer cómo rotan las componentes:
c02 = Pi_rot[0, 2]  # debería mezclar (a0, a1) con ángulo theta  -> helicidad 1
c01 = Pi_rot[0, 1]  # debería mezclar (a2, a3) con ángulo 2*theta -> helicidad 2
c22 = Pi_rot[2, 2]  # debería quedar fija -> helicidad 0
h1 = sp.simplify(c02 - (a[0] * sp.cos(th) - a[1] * sp.sin(th))) == 0
h2 = sp.simplify(c01 - (a[2] * sp.cos(2 * th) + a[3] * sp.sin(2 * th))) == 0
h0 = sp.simplify(c22 - (-2 * a[4] / sp.sqrt(3))) == 0
check("espectro: helicidades bajo R_z — (p0,p1)~e^{i theta} (±1), "
      "(p2,p3)~e^{i 2theta} (±2), p4 fijo (0)", h0 and h1 and h2)

# ----------------------------------------------------------------------------
# 4. LA MINA: Tr(Q^-1 B) con B = delta genera masa para pi
# ----------------------------------------------------------------------------
# Tr(exp(-eps Pi)) = 3 - eps Tr(Pi) + eps^2/2 Tr(Pi^2) + ... ; Tr(Pi) = 0
# => queda 3 + (eps^2/2) Tr(Pi^2): TERMINO DE MASA para las 5 componentes.
Pi_sym = Pi_c  # constante, simétrica sin traza
serie = sp.simplify(sp.trace(sp.eye(3) - eps * Pi_sym + eps**2 * Pi_sym * Pi_sym / 2))
masa = sp.simplify(serie - 3 - eps**2 * sp.trace(Pi_sym * Pi_sym) / 2)
check("mina: Tr(Q^-1 delta) = 3 + (1/2) Tr(pi^2) + O(pi^3) — MASA regenerada "
      "si el fluido comparte el SL(3) del cuadrupolo", masa == 0)
# y el coeficiente de masa NO es cero:
coef = sp.simplify(sp.trace(Pi_sym * Pi_sym))
check("mina: el término de masa es genuino (Tr(pi^2) > 0 para pi != 0)",
      sp.simplify(coef.subs([(a[0], 1), (a[1], 0), (a[2], 0), (a[3], 0), (a[4], 0)])) == 2)

print()
print("RESULTADO GLOBAL:", "TODO PASS" if ok_all else "HAY FALLAS — revisar antes de escribir la nota")
