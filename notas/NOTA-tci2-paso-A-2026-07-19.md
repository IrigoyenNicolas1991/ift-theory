# Nota 12 — Paso A ejecutado: el patrón de ruptura es SL(3)×SO(3) → SO(3), y el cuadrupolo es el Goldstone

**Fecha:** 2026-07-19
**Contexto:** se levanta la pausa (Nicolás, 2026-07-19: "sin nada que demostrar,
encaminá la investigación por donde decidas"). Se ejecuta el Paso A del plan de la
nota 11: elegir el patrón de ruptura del condensado. Todas las afirmaciones marcadas
[verificado] tienen chequeo en `paso_a_simetrias.py` (13/13 PASS) o cita web chequeada.

---

## 1. El patrón elegido

**G = SL(3,R)_interno × SO(3)_espacial (× traslaciones), roto a H = SO(3)_diagonal
(× traslaciones diagonales).**

En criollo: el estado interno del condensado es una "forma" — una matriz Q simétrica,
definida positiva, de determinante 1 (un elipsoide de volumen fijo en cada punto).
La simetría interna SL(3) dice que *ninguna forma es preferida* (eso ES ser fluido:
deformar sin cambiar volumen no cuesta energía potencial). El vacío elige Q = 𝟙
(la esfera), que solo es invariante si rotás el espacio y el índice interno juntos:
queda el SO(3) diagonal.

**Los tres checkpoints del Paso A, cumplidos [verificado]:**

1. **No rompe traslaciones.** El patrón es puramente orientacional/de forma; las
   traslaciones (diagonales) quedan intactas. No hay red, no hay sólido. La lección
   de solid inflation se respeta de fábrica.
2. **No deja dirección observable.** El vacío Q = 𝟙 es isótropo — es la esfera. Es
   el truco de ³He-B (orden sin dirección) pero en el coset correcto.
3. **Espacio de orden no trivial con J=2.** El coset SL(3)/SO(3) tiene exactamente
   5 generadores rotos = matrices simétricas sin traza = **una representación J=2
   irreducible** del SO(3) no roto (chequeado con Schur: el conmutante de la
   representación es unidimensional). El cuadrupolo no se agrega a mano: **es el
   Goldstone del patrón.** Bajo helicidad (propagación en z): 0, ±1, ±2.

## 2. El candidato a teorema de protección (la pieza que buscábamos)

**Enunciado:** ninguna función invariante bajo SL(3) de una matriz unimodular
simétrica definida positiva puede depender de Q. **Demostración (esquema):** toda Q
de ese tipo se escribe Q = L·Lᵀ con det L = 1 (Cholesky), o sea Q = M·𝟙·Mᵀ con
M ∈ SL(3): la órbita de la identidad cubre TODO el espacio de orden [verificado:
200/200 matrices aleatorias alcanzadas]. Una función invariante es constante sobre
la órbita ⇒ es constante en todo el espacio ⇒ **no existe potencial para el sector
de forma ⇒ el término de masa de las 5 helicidades está prohibido por simetría.**
El único invariante es det Q = 1, que es un número, no un potencial [verificado].

Con el término de gradiente tipo sigma-model (la métrica de Cartan del coset,
Tr[(Q⁻¹∂Q)²]), el espectro cuadrático da **5 ondas desacopladas sin masa con
ω = ck** [verificado con sympy, término a término].

Esto convierte la conjetura de la nota 11 §2 ("la simetría que protege m₂=0 es
rotacional, no traslacional") en una afirmación precisa: **la protectora es la
simetría de forma SL(3) — la fluidez llevada al sector interno.** Y coincide con lo
que la literatura ya sabía por otro camino: para fluidos perfectos, los diffs
espaciales transversos prohíben el término de masa de helicidad 2 (verificado
textual en la literatura de supersolid inflation, arXiv:2103.10402 §fluid limit).

## 3. La mina, declarada y CALCULADA antes de pisarla

Si el sector fluido (B_ab = ∂φ·∂φ, las coordenadas comóviles de BCP) transforma
bajo **el mismo** SL(3) que Q, entonces el invariante mixto Tr(Q⁻¹B) está permitido
por la simetría — y evaluado en el fondo B = 𝟙 da:

    Tr(Q⁻¹) = 3 + ½·Tr(π²) + O(π³)    [verificado]

**Eso es un término de masa para las 5 componentes del cuadrupolo.** La traza de π
es cero (mata el término lineal) pero el cuadrático sobrevive. Conclusión dura: el
teorema del §2 protege al sector Q *aislado*; el acople con el sector de
desplazamientos puede regenerar la masa. Es exactamente el mecanismo por el que los
modos J=2 de ³He-B tienen gap, ahora visto desde simetrías.

**El Paso B queda entonces afilado en una sola pregunta:** ¿qué estructura impide
los invariantes mixtos tipo Tr(Q⁻¹B) sin romper lo demás? Tres rutas declaradas,
con sus criterios de muerte:

- **Ruta (a) — Q esclavo del fluido:** Q ≡ parte unimodular de B. No hay campo
  nuevo; la rigidez orientacional entra como término de gradiente de orden superior
  del EFT del fluido. *Riesgo:* los modos ±2 saldrían con dispersión blanda
  (ω² ~ k⁴), y GW170817 exige ω = ck a 10⁻¹⁵. Probable muerte; hay que calcularlo.
- **Ruta (b) — dos grupos distintos:** el SL(3) de Q independiente de la simetría
  del fluido; el locking espacial-interno debe emerger espontáneamente (no explícito
  en el lagrangiano, o los Goldstones pierden protección). *Riesgo:* sin locking no
  hay helicidades definidas; con locking explícito, gap (el problema del dipole
  locking de ³He, en versión J=2).
- **Ruta (c) — Q como métrica interna dinámica:** el espacio comóvil del fluido no
  tiene métrica propia (VsDiff se la come); Q(φ) ES esa métrica, campo local en el
  espacio interno. Los invariantes mixtos son entonces *pullbacks* (Q_ab∂φᵃ∂φᵇ) y al
  minimizar sobre Q el sistema podría relajar la masa dinámicamente, dejando la
  parte propagante sin gap. Es la ruta más profunda y la más cercana a la gravedad
  (Q jugaría el rol de métrica espacial emergente contraída con TODO). *Riesgo:*
  que la relajación se coma también la dinámica de Q (que quede esclavo = ruta (a)).

## 4. Honestidad sobre precedentes (corrección a la nota 10)

La búsqueda de hoy obliga a matizar el "territorio virgen" de la nota 10 §5:

- **Borisov-Ogievetsky (1974):** la métrica de la relatividad general como Goldstone
  de la simetría afín GL(4) rota a Lorentz — la idea "gravitón = Goldstone de
  deformaciones de forma" tiene 50 años y linaje ilustre (verificado web). Lo
  nuestro es su versión de medio condensado, espacial y no relativista de entrada.
- **Gromov & Son (PRX 2017, arXiv:1705.06739):** en Hall cuántico fraccionario, un
  tensor simétrico unimodular como parámetro de orden dinámico con modo spin-2 — el
  pariente de materia condensada más cercano. **Pero su spin-2 es masivo** (el gap
  GMP), es 2D, y la masa ahí es física, no un problema.
- **Lo que sigue sin reclamar** (refinado): la construcción 3D en lenguaje de medios
  (BCP) donde la fase m₂=0 de Dubovsky salga *protegida* por la simetría de forma —
  incluyendo la resolución de los invariantes mixtos del §3. Ese es ahora el
  enunciado preciso de nuestra bandera.

## 5. Lo que esta nota NO dice

- NO dice que TCI 2.0 tiene lagrangiano: tiene patrón de ruptura + teorema de
  protección del sector aislado + mina identificada en el acople.
- NO dice que los modos 0 y ±1 están silenciados: en el sigma model aislado las 5
  helicidades son igual de no-masivas. Silenciar 0 y ±1 dejando ±2 es tarea del
  acople con los vínculos (Paso C) — si no se logra, las cotas de polarización de
  LIGO matan la construcción. Peligro transferido, no resuelto.
- NO dice nada de Hulse-Taylor todavía (Paso E espera).

## 6. Próximo movimiento

**Paso B por la ruta (c)** (la más rica: si falla, cae a (a) y se evalúa la
dispersión blanda contra GW170817). Concretamente: escribir el lagrangiano
L[φᵃ, Q_ab] con Q métrica interna dinámica, expandir alrededor de ⟨φ⟩=x, ⟨Q⟩=𝟙,
y calcular el espectro completo de 3+5 campos con los acoples mixtos incluidos.
El checkpoint de la nota 11 sigue: reproducir un medio conocido de BCP como límite
de control antes de leer nada nuevo.
