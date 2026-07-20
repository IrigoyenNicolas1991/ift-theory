# -*- coding: utf-8 -*-
"""
Batalla del core (bitácora §33) — dos verificaciones numéricas:

  1. CONTROL JACKIW-ROSSI EN RED (el teorema de índice que sostiene todo):
     fermión de Dirac 2D (regularización de Wilson, cono único en k=0) + vórtice
     s-wave Δ(r)e^{inθ} a μ=0. Teorema (Jackiw-Rossi 1981; Fu-Kane a μ=0):
     |n| modos cero ligados al core.
     GEOMETRÍA (tercer intento, los dos anteriores documentados): disco interior
     con Dirac sin masa + pairing con vórtice; exterior con masa de Wilson
     grande (aislante trivial). La pared interior-SC/exterior-masivo es la
     frontera de Fu-Kane y lleva SU PROPIO canal Majorana 1D (física real, se
     cuenta aparte por radio de localización). Esperado: n=0 → 0 modos de CORE
     (pared puede tener estados ~0: legítimos); n=1 → 1 de core; n=2 → 2 de core.
     Intentos previos: (a) borde abierto con m0=0 global: borde crítico
     contamina E~0 — FALLA; (b) toro con par vórtice/antivórtice por imagen
     mínima: la fase tiene costuras discontinuas que dispersan y corren los
     modos — FALLA. Ambas documentadas como lección de método.

  2. EL CONTEO DEL CORE CÍCLICO (combinatoria de cargas de Weyl, verificada
     contra la fuente 1607.07266: 8 nodos en ±k_F n̂_α, carga q_m = ±1 en ±):
     para un tubo con eje ĝ, el número de Chern por rebanada C(k∥) suma las
     cargas cruzadas; una línea de vórtice de winding n lleva n·C(k∥) ramas
     quirales (flujo espectral estándar). Se calcula el perfil C(k∥) para ejes
     especiales y para un barrido aleatorio de orientaciones:
     - eje (001): cancelación exacta rebanada a rebanada → C ≡ 0 (tubo "mudo")
     - eje (111): perfil (0, +1, -2, +1, 0) → tubo con materia quiral
     - genérico: ¿qué fracción del cielo es muda? (conjetura: medida cero)

Uso: python core_indice_toy.py   (imprime PASS/FAIL + tablas)
NOTA: juguete mínimo — un solo cono de Dirac y pairing s; el core real de TCI 2.0
(HQV con winding fraccionario + orden cíclico) hereda el MECANISMO, no los números.
"""

import sys
import numpy as np

SOLO_CICLICO = "--solo-ciclico" in sys.argv
rng = np.random.default_rng(20260719)
ok_all = True


def check(nombre, cond):
    global ok_all
    print(f"[{'PASS' if cond else 'FAIL'}] {nombre}")
    ok_all = ok_all and cond


# ============================================================================
# 1. JACKIW-ROSSI EN RED (disco Dirac+vórtice, pared de masa afuera)
# ============================================================================
L = 41           # red L x L abierta, vórtice en el centro
v, t = 1.0, 0.5  # velocidad y término de Wilson
D0, xi = 0.5, 2.0
R0, wR = 14.0, 1.5   # radio de la pared de masa y su ancho
M_out = 2.0          # masa de Wilson exterior (aislante trivial)

sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
isy = 1j * sy

N = L * L
c = (L - 1) / 2.0


def idx(x, y):
    return x * L + y


def m0_local(r):
    return M_out / (1.0 + np.exp(-(r - R0) / wR))


def hamiltoniano(n_wind):
    """BdG 4N x 4N en base (psi_up, psi_dn, psi_up^dag, psi_dn^dag)."""
    H0 = np.zeros((2 * N, 2 * N), complex)
    for x in range(L):
        for y in range(L):
            i = idx(x, y)
            r = np.hypot(x - c, y - c)
            H0[2 * i:2 * i + 2, 2 * i:2 * i + 2] += (m0_local(r) + 4 * t) * sz
            for (dx, dy, s) in [(1, 0, sx), (0, 1, sy)]:
                if x + dx < L and y + dy < L:
                    j = idx(x + dx, y + dy)
                    T = (-1j * v / 2) * s - t * sz
                    H0[2 * j:2 * j + 2, 2 * i:2 * i + 2] += T
                    H0[2 * i:2 * i + 2, 2 * j:2 * j + 2] += T.conj().T
    Delta = np.zeros((2 * N, 2 * N), complex)
    for x in range(L):
        for y in range(L):
            i = idx(x, y)
            r = np.hypot(x - c, y - c)
            th = np.arctan2(y - c, x - c)
            d = D0 * np.tanh(r / xi) * np.exp(1j * n_wind * th)
            Delta[2 * i:2 * i + 2, 2 * i:2 * i + 2] = d * isy
    HB = np.zeros((4 * N, 4 * N), complex)
    HB[:2 * N, :2 * N] = H0
    HB[2 * N:, 2 * N:] = -H0.conj()
    HB[:2 * N, 2 * N:] = Delta
    HB[2 * N:, :2 * N] = Delta.conj().T
    return HB


def analiza(n_wind, umbral=0.06):
    """Cuenta modos de core por PESO DE CORE ACUMULADO (robusto a hibridización:
    lección del diagnóstico n=1 — el Majorana del core y el de la pared se
    hibridizan en un par (core±pared)/sqrt(2) a E=±0.004 con medio peso cada
    uno; clasificar por radio medio los pierde, sumar peso de core los cuenta
    bien: 0.47+0.47 = 0.94 = UN modo de core)."""
    HB = hamiltoniano(n_wind)
    E, V = np.linalg.eigh(HB)
    cerca = np.where(np.abs(E) < umbral)[0]
    xs = np.arange(N) // L
    ys = np.arange(N) % L
    rs = np.hypot(xs - c, ys - c)
    peso_core = 0.0
    for k in cerca:
        w = np.abs(V[:, k]) ** 2
        wsite = w[:2 * N].reshape(N, 2).sum(1) + w[2 * N:].reshape(N, 2).sum(1)
        # r<7: región de core (la mitad de la distancia a la pared en R0=14);
        # los modos JR de |n|=2 son más anchos que el de n=1 — con r<5 el peso
        # daba 1.69 y el corte estricto los subcontaba (afinado documentado)
        peso_core += float(wsite[rs < 7.0].sum())
    return peso_core, len(cerca)


if not SOLO_CICLICO:
    w0, m0_ = analiza(0)
    check(f"JR n=0: peso de core acumulado ~0 (medido {w0:.2f}; estados en "
          f"ventana: {m0_}, de pared, legítimos Fu-Kane)", w0 < 0.2)
    w1, m1_ = analiza(1)
    check(f"JR n=1: peso de core acumulado ~1 (medido {w1:.2f}; el Majorana "
          f"del core partido con su compañero de pared)", 0.7 < w1 < 1.3)
    w2, m2_ = analiza(2)
    check(f"JR n=2: peso de core acumulado ~2 (medido {w2:.2f})",
          1.6 < w2 < 2.4)

# ============================================================================
# 2. CONTEO DEL CORE CÍCLICO: perfil de Chern por rebanada
# ============================================================================
# 8 nodos verificados en 1607.07266: q k_alpha con alpha = 4 vértices del
# tetraedro y q=±1; carga de monopolo q_m = q.
tetra = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]]) / np.sqrt(3)
nodos = [(+1, n) for n in tetra] + [(-1, -n) for n in tetra]  # (carga, posición)


def perfil_chern(eje, tol=1e-9):
    """C(k) entre rebanadas: al cruzar un nodo de carga q (bajando en k), C += q.
    Devuelve la lista de valores de C entre proyecciones consecutivas."""
    eje = np.asarray(eje, float); eje = eje / np.linalg.norm(eje)
    proy = [(float(np.dot(pos, eje)), q) for q, pos in nodos]
    proy.sort(key=lambda p: -p[0])
    Cs, C, i = [], 0, 0
    while i < len(proy):
        k0 = proy[i][0]
        while i < len(proy) and abs(proy[i][0] - k0) < tol:
            C += proy[i][1]; i += 1
        Cs.append(C)
    return Cs  # el último debe ser 0 (suma total de cargas)


p001 = perfil_chern([0, 0, 1])
check(f"cíclico eje (001): cancelación exacta por rebanada, C = 0 en todas — tubo MUDO {p001}",
      all(x == 0 for x in p001))
p111 = perfil_chern([1, 1, 1])
check(f"cíclico eje (111): perfil (1,-2,1,0) — tubo CON materia quiral {p111}",
      p111 == [1, -2, 1, 0])
p110 = perfil_chern([1, 1, 0])
print(f"       eje (110): perfil {p110}")

# barrido del cielo: ¿qué fracción de orientaciones es muda?
mudos, maxC = 0, 0
for _ in range(2000):
    g = rng.normal(size=3)
    Cs = perfil_chern(g)
    if all(x == 0 for x in Cs):
        mudos += 1
    maxC = max(maxC, max(abs(x) for x in Cs))
check(f"cíclico barrido 2000 ejes aleatorios: tubos mudos = {mudos} (conjetura: "
      f"solo ejes especiales tipo (001), medida cero) — |C|_max = {maxC}",
      mudos == 0)

# la suma total de cargas es 0 (los perfiles siempre cierran en 0): consistencia
check("cíclico: carga total de los 8 Weyl = 0 (todo perfil cierra en C=0)",
      perfil_chern(rng.normal(size=3))[-1] == 0)

# CARACTERIZACIÓN DE LOS TUBOS MUDOS (conjetura afilada y verificada):
# mudo <=> el eje vive en uno de los tres círculos máximos n·e_i = 0
# (cada vértice + de un tetraedro se cancela con el vértice - que difiere
# en un solo signo: a - b = 2 e_i; si n·e_i = 0 proyectan igual).
mudos_circ, no_mudos_circ = 0, 0
for _ in range(300):
    # eje aleatorio DENTRO del círculo n_z = 0
    phi = rng.uniform(0, 2 * np.pi)
    Cs = perfil_chern([np.cos(phi), np.sin(phi), 0.0])
    mudos_circ += int(all(x == 0 for x in Cs))
    # eje aleatorio FUERA de los tres círculos (componentes todas no nulas)
    g = rng.normal(size=3)
    while np.min(np.abs(g)) < 0.05:
        g = rng.normal(size=3)
    Cs2 = perfil_chern(g)
    no_mudos_circ += int(all(x == 0 for x in Cs2))
check(f"cíclico: TODO el círculo n_z=0 es mudo (300/300={mudos_circ}) y NINGÚN "
      f"eje genérico lo es (0/300={no_mudos_circ}) — mudos = 3 círculos máximos "
      f"perpendiculares a los ejes del cubo, medida cero",
      mudos_circ == 300 and no_mudos_circ == 0)

print()
print("RESULTADO GLOBAL:", "TODO PASS" if ok_all else "HAY FALLAS")
