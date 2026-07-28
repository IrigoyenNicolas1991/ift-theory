# Selección de estado — SÍNTESIS FINAL: D2 confirmado

**Campaña m₂=0 · frente selección de estado · abierta 2026-07-27 (OK de Nico),
cerrada 2026-07-28 · 3 columnas (A vértices/NLO/números, B carga/poblamiento,
C bibliografía de fuentes primarias) + verificador adversarial final con
pipeline propio (tercera parametrización de Y, EH ΓΓ independiente; acta
`verificador/VERIFICADOR-FINAL-2026-07-28.md`). Criterios D1/D2/D3
pre-declarados en `APERTURA-2026-07-27.md`. El verificador reprodujo las 8
corridas de las columnas e intentó romper el teorema por 5 flancos: RESISTE.**

## El veredicto

**D2 — GANA LA CO-ROTANTE, uniforme en toda la ventana Λ ∈ [10⁻³ eV, 1 MeV].**

**El resultado central es un TEOREMA DE SUPERSELECCIÓN**: para √−g·U(X,Y)+EH,
la carga interna de la simetría Φᵃ→Φᵃ+ξᵃ(Φ⃗) no tiene corriente espacial
(P_aⁱ = 0, identidad algebraica off-shell, exacta a todo orden — verificada por
CUATRO rutas independientes: solve-u de B, Levi-Civita de A, Gram/determinantes
del verificador, y vértice a vértice explícito). La densidad de carga está
congelada punto a punto, con **corolario de inversión** (del verificador):
P_a⁰(x) = 0 ⟺ g₀ₐ(x) = 0 exacto — la separación de sectores es no
perturbativa y de campo completo. Consecuencias encadenadas, todas verificadas:

1. Las dos ramas del frame dragging viven en **sectores de superselección
   desconectados**: la co-rotante tiene carga cero (la que las condiciones
   iniciales cosmológicas — nuestro atractor FRW — proveen); la relajada
   (la del Yukawa apantallado) requiere una distribución de carga imposible de
   crear: no existe la corriente que la transportaría. El escape "relajada +
   nube compensante" NO existe (verificador: el sistema no tiene solución).
2. El **poblamiento es universal**: S = 0 es solución exacta del encendido con
   τ(t) arbitraria — rápido, lento, no monótono, e incluso con la fuente
   DESPLAZÁNDOSE (acreción real; solución cerrada del verificador). La
   formación de la Tierra deja el medio co-rotando, siempre.
3. Los **NLO no abren puerta trasera**: la corrección del co-rotante es una
   renormalización universal del acople gravitomagnético, δ ≈ −ĉ(Λ/M̄_Pl)² =
   10⁻⁶¹…10⁻⁴³ (LARES-2 está a ≥40 órdenes: la firma NO revive); la fuga de
   carga es cero exacto a orden lineal y (no-lineal)×(NLO) da
   Γ·t_edad ≤ 10⁻³⁵…10⁻¹⁴ (≥14 órdenes de colchón). Sin fuga inter-modo a
   orden cuadrático (verificador, dos modos con NLO). Sin patologías.
4. Los canales restantes, muertos por la bibliografía (columna C, fuentes
   primarias): phase slips con barrera ∝ 1/v divergente; Cherenkov escalar con
   tasa importada despreciable (ACLM+Thaler 2007 — de ellos, se cita);
   superradiancia gapeada prohibida bajo el gap; spin-down terrestre con 26
   órdenes de margen.

**En una frase: la fase predice relatividad general en el gravitomagnetismo —
no porque el medio se esconda bien, sino porque un teorema de superselección le
prohíbe delatarse. La firma del frame dragging apantallado (la "predicción
falsable propia" de la campaña madre) queda SUPRIMIDA, y lo decimos con la
misma prominencia con que la anunciamos.**

## Qué se pierde y qué se gana (marcador honesto)

| Se pierde | Se gana |
|---|---|
| La firma falsable del Yukawa gravitomagnético (LARES-2 ya no discrimina esta fase de RG) | La predicción LIMPIA: indistinguible de Einstein en TODO el régimen medido, por teorema, no por ajuste — el "caveat central" del paper se resuelve |
| Las cotas Λ ≲ 2.0–2.6 MeV y Λ < 1.12 MeV (eran de la rama no poblada: pasan a contrafácticas) | El teorema de superselección + corolario de inversión como estructura nueva y publicable por derecho propio (nadie lo vio en 22 años de la fase) |
| El ítem "selección de estado" como problema abierto | La respuesta: la seleccionó una ley de conservación exacta del orden cuadrático — y la irrotacionalidad del ghost condensate (columna C) explica por qué NADIE pudo siquiera plantear esta pregunta antes: hace falta m₁² ≠ 0 |

**Corrección de coherencia (grieta menor del verificador, asumida acá):** la
frase del acta de A "sin cota nueva (manda la nodal Λ ≲ 2.0–2.6 MeV)" es
incoherente con D2 — la cota nodal pertenece a la rama no poblada. Con D2, la
ventana de Λ vuelve a regirse por el sector escalar (Λ ≲ 10 MeV conservadora /
~100 GeV twinkling, acta SECTOR-ESCALAR). El paper no debe heredar la frase.
**Typo interno de a4_numeros.py** (párrafo final imprime "6e-14/7e-36" contra
su propia tabla, que es la correcta y la que citan las actas): anotado acá,
script intacto como registro.

## Hipótesis que condicionan D2 (todas ya declaradas, ninguna nueva)

Acople de materia universal; Φᵃ suave (sin vórtices — con barrera ∝1/v
divergente si los hubiera); exhaustividad de la base NLO (θ,σ,ω,a) como
argumento estructural, no teorema formal; U_Y ≠ 0; perturbaciones vectoriales
primordiales despreciables.

## PARA EL HILO DEL PAPER (integración pendiente — NO hecha acá)

El verificador listó las frases exactas del acta ACOPLE y del paper v0.6 que
este resultado corrige (lista completa en su acta, §"Frases a corregir").
Lo grande, que requiere DECISIÓN DE NICO porque cambia la identidad del paper:

- **El título** ("…and a screened frame-dragging signature") ya no describe el
  resultado: la firma está suprimida. Candidato: "…and a superselection theorem
  for frame dragging" o similar.
- §8 se reescribe: de "dos ramas + caveat de selección" a "el teorema
  selecciona la co-rotante; RG exacto predicho; el Yukawa queda como
  contrafáctico de la fase espejo de condiciones iniciales".
- §11: ítem 1 (selección de estado) RESUELTO; ítem 5 respondido
  (δ = −ĉ(Λ/M̄_Pl)², inobservable).
- El acta ACOPLE recibe adenda de corrección (hecha: ver
  `../ACOPLE-MATERIA-PPN-2026-07-21.md`, adenda 2026-07-28).

*Síntesis escrita al cierre de la campaña, el día del veredicto. Cuatro rutas
independientes para el teorema, tres columnas, un verificador que quiso
romperlo y no pudo. El dulce de leche recuerda la cuchara para siempre — y esa
memoria es exactamente lo que lo vuelve invisible.*
