# Nota 10 — El bug es la feature: el marco propio del medio es lo que silencia los modos sobrantes

**Fecha:** 2026-07-11 (mismo día que la nota 9; continuación directa)
**Pregunta:** el quinteto spin-2 de un medio tensorial tiene 5 modos (helicidades 0, ±1, ±2).
LIGO ve exactamente 2 (las ±2, sin masa, a velocidad c). ¿Se pueden silenciar los otros 3
sin tocar los 2 buenos? ¿Y quién paga el ghost?
**Método:** verificación bibliográfica web de la literatura de gravedad masiva con violación
de Lorentz (todas las citas chequeadas).

---

## 1. El resultado central (verificado, textual)

En gravedad masiva **con marco de referencia privilegiado** —exactamente lo que un medio
provee gratis— los cinco términos de masa del gravitón (m₀…m₄ de Rubakov) son parámetros
independientes, a diferencia del caso Lorentz-invariante donde vienen atados. Y existe el
rincón sano que necesitamos:

- **Dubovsky, "Phases of massive gravity" (JHEP 0410:076, hep-th/0409124), textual:** si
  m₂² = 0, *"nothing changes in the scalar sector, while both vector degrees of freedom
  become non-dynamical and the tensor mode is massless"*. Es decir: **helicidad ±2
  exactamente sin masa y a velocidad c; helicidades ±1 directamente no-dinámicas; el
  escalar, gapeado o no-propagante según la fase.**
- **Sin fantasmas**: la elección m₀ = 0 convierte h₀₀ en multiplicador de Lagrange y mata
  el ghost de Boulware-Deser (Rubakov, hep-th/0407104); sin discontinuidad vDVZ; escala de
  acople fuerte elevada a √(mM_Pl). Review: Rubakov & Tinyakov, Phys. Usp. 51:759 (2008),
  arXiv:0802.4379 — "no pathologies in the spectrum".
- En el caso Lorentz-invariante esto es IMPOSIBLE (Fierz-Pauli obliga a mover las 5
  componentes juntas). **El marco privilegiado del medio —el "defecto" que TCI arrastró
  siempre como vergüenza— es precisamente la licencia que permite desarmar el quinteto.**

## 2. El regalo: el diccionario medio ↔ gravedad masiva ya existe

- **Ballesteros, Comelli & Pilo, arXiv:1603.02956** ("Massive and modified gravity as
  self-gravitating media"): la gravedad masiva LV es, en gauge unitario, **la teoría de un
  medio continuo propagándose en el espacio-tiempo** — los cuatro escalares de Dubovsky son
  las coordenadas comóviles del medio; las simetrías internas seleccionan el tipo de medio
  (fluido, superfluido, sólido, supersólido). La correspondencia es literal, no metafórica.
- **Gabadadze & Older, arXiv:1712.09378 ("Medium Generated Gap in Gravity")**: un medio
  físico que fija un marco genera términos de masa LV para el gravitón, con positividad de
  energía y subluminalidad acotando la ecuación de estado del medio. El título dice todo.
- Clasificación por simetrías de todos los medios con marco propio: Nicolis, Penco, Piazza
  & Rattazzi, arXiv:1501.03845 ("Zoology of condensed matter: framids...").

## 3. Los modos silenciados pasan los tests automáticamente

- Un modo con gap m no puede ser radiado por una fuente de frecuencia ω < m (no hay estado
  on-shell). Banda LIGO ~10²-10³ Hz ↔ ~10⁻¹³ eV; púlsares binarios ~10⁻⁴ Hz ↔ ~10⁻¹⁹ eV.
  **Cualquier gap ≳ 10⁻¹² eV silencia los canales extra en TODAS las observaciones GW
  actuales**; los modos no-dinámicos evaden trivialmente.
- Hulse-Taylor: decaimiento orbital = RG a 0.9983 ± 0.0016 (Weisberg & Huang,
  arXiv:1606.02744) — los modos gapeados no aportan nada; el vínculo residual queda en el
  sector estático (PPN), donde TCI ya rinde cuentas (notas 1-3).
- Tests de polarización (GW170814 Bayes >200 tensor vs vector; GW170817 ~10²⁰; GWTC-3
  arXiv:2112.06861): discriminan contenido puro o dominante — un espectro "±2 sin masa +
  resto mudo" es exactamente lo que favorecen.

## 4. La letra chica (las dos piedras en el zapato, con nombre)

1. **Lección de solid inflation** (Endlich, Nicolis & Wang, arXiv:1210.0569): un medio
   genérico CON rigidez de corte le da masa al gravitón (m₂ ≠ 0). O sea: el problema de la
   masa cero (escalón 2 de la nota 9) ahora está afilado en una sola pregunta técnica:
   **¿qué simetría del condensado prohíbe el acople de corte que generaría m₂?** (candidata
   documentada: la invariancia xⁱ → xⁱ + ξⁱ(t) de la fase m₁ = 0 de Dubovsky; y la
   selección fluido/superfluido/supersólido de Ballesteros-Comelli-Pilo). Nótese la ironía:
   TCI 1.0 había concluido "el medio debe ser sólido elástico" para radiar — y era al revés.
2. **Matiz técnico**: en la fase m₀ = 0 los gaps de vectores y escalar son proporcionales a
   m₂ mismo, así que con m₂ = 0 los sobrantes no quedan "gapeados y propagantes" sino
   **no-dinámicos/desacoplados** — observacionalmente igual o mejor, pero el lenguaje
   correcto es "silenciados", no "masivos".

## 5. Territorio virgen (verificado por búsqueda: no existe)

No se encontró ningún paper que parta de un **parámetro de orden tensorial** (spin-2) de un
condensado y derive la fase m₂ = 0. La literatura existente usa multipletes escalares
(coordenadas del medio) u orden vectorial. **La construcción específica que TCI 2.0
necesita —condensado con orden cuadrupolar → fase sana con solo ±2 sin masa— está sin
reclamar.** Es exactamente el tipo de hueco donde un proyecto chico puede plantar bandera.

## 6. Cómo queda el tablero después de las notas 9 y 10

| Problema (nota 9) | Estado tras nota 10 |
|---|---|
| ¿Puede un medio tener modos spin-2? | Sí — verificado con experimentos (nota 9) |
| ¿Se pueden silenciar las helicidades 0, ±1? | **Sí — fase m₂=0 de Dubovsky, sana, sin ghosts** |
| ¿Masa exactamente cero para ±2? | Afilado: encontrar la simetría que prohíbe el acople de corte |
| ¿Marco privilegiado = defecto fatal? | **Invertido: es la licencia que permite todo lo anterior** |
| ¿Una sola velocidad límite (Carlip)? | Abierto — la apuesta monometricidad de TCI (nota 9 §5) |
| ¿Dinámica de Einstein completa? | Abierto para todo el campo (nota 9 §4) |

**Primer cálculo concreto (actualizado):** escribir el lagrangiano del condensado
cuadrupolar en el lenguaje de Ballesteros-Comelli-Pilo, identificar a qué fase de Dubovsky
cae, e imponer las condiciones de la fase m₂ = 0. Recién después, las antenas (el pipeline
de las notas 6-7 espera intacto).

## 7. Marcador honesto

**Qué NO es:** todavía no hay lagrangiano de TCI 2.0; la simetría protectora de m₂ = 0 no
está construida; monometricidad y dinámica siguen abiertas.
**Qué SÍ es:** las tres objeciones tácticas a "un medio que radie como LIGO manda" (¿spin-2?
¿modos sobrantes? ¿ghosts?) tienen respuesta afirmativa y sana en literatura publicada y
verificada; el diccionario medio↔gravedad-masiva existe; y el caso específico de orden
tensorial está sin explorar — es nuestro si lo trabajamos.
