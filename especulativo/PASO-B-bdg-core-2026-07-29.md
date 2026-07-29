# Paso B — El BdG del core: LA COMPUERTA CIERRA DEL LADO VIVO — el nudo lleva una rama quiral de serie

**Compuerta única (§34.D de la bitácora madre) · 2026-07-29 · Fable · diseño del
acta del Paso A §7, ejecutado con `paso_b_bdg_core.py` (BdG sparse + FHS + flujo
espectral con tracking por solapamiento) · ~44 min de máquina, sin agentes**

**Veredicto en una línea: C_neto = −1 — el core real del HQV (mezcla FM+cíclica
del Paso A) sostiene EXACTAMENTE UNA rama fermiónica quiral neta tipo Majorana,
cuasi-plana (quince veces bajo el minigap CdGM), que cruza E=0 en k_z=0 y conecta
los dos nodos polares del fondo; la quiralidad se invierte exacta con el winding
(espejo: +1), el conteo es topológico (4 deformaciones de Δ₀ y μ: idéntico), y el
MECANISMO queda probado por el control de vaciado: sin el relleno cíclico del
core el flujo neto se apaga (C_neto = 0). El criterio de muerte pre-declarado
(C_neto=0 ⟹ 10ª lápida) NO se gatilla: los tubos NO son estériles — la
Arquitectura A tiene su materia, y las dos mitades de la compuerta (bisagra
energética del A + conteo del B) se sostienen mutuamente.**

Contexto: el Paso A (2026-07-21) cerró la bisagra energética — el core del HQV del
D₄-BN se llena espontáneamente con la mezcla FM+cíclica ALINEADA (C₃ ∥ eje, L ∥ +ẑ),
pinning duro, matriz de gap medida a·Y₊₂ + b·Y₋₁ con perfiles del `paso_b_core.npz`.
Quedaba la segunda mitad de la compuerta: **contar la materia**. Criterio de muerte
pre-declarado (§34.D, intacto): **C_neto = 0 ⟹ 10ª lápida** — tubos estériles, el
sector de defectos pierde materia quiral y candidato a fotón, la Arquitectura A muere,
el programa queda en la ruta geométrica 𝒢(t) sin candidato de luz.

---

## 1. Setup (declarado)

- **Hamiltoniano**: BdG del ³P₂ en la sección 2D del tubo (Nambu×spin = 4 comp/sitio,
  base de bloques [u↑, u↓, v↑, v↓]):
  - estado normal ξ = k² + k_z² − μ (m=½, ħ=1), laplaciano de 5 puntos en la grilla
    del GL (h=1, la misma caja 80×80 del npz), k_z parámetro continuo;
  - pairing p-wave triplete d_μ(r,k) = (Δ₀/k_F)[ ½{A_μx(r), k̂_x} + ½{A_μy(r), k̂_y}
    + A_μz(r)·k_z ], con ½{A,k̂} discretizado por promedio de enlace (diferencia
    centrada) — hermiticidad EXACTA por construcción;
  - Δ_spin = (d·σ)iσ_y = [[−d₁+id₂, d₃],[d₃, d₁+id₂]] (triplete, simétrica).
- **Parámetros**: μ = 0.64 (k_F = 0.8; los nodos polares del fondo D₄ caen en
  k_z = ±√μ = ±0.8 EXACTO en esta red porque k_z es continuo), Δ₀ = 0.6 → gap máximo
  del fondo ≈ Δ₀·a₀ ≈ 0.28 (gap/E_F ≈ 0.44), ξ_BdG = v_F/gap ≈ 5.7 ≪ caja/2.
- **El campo**: el REAL del Paso A (`paso_b_core.npz`, regenerable con
  `paso_b_core_input.py`; verificado al cargar: E_GL = +11.88573 y pesos del core
  r<1 = {+2: 0.473, −1: 0.406} exactos a la tabla del acta §7). El gap NO es
  axisimétrico (el core rompe la axisimetría combinada — perla del Paso A): el BdG
  come el campo 2D completo, sin reglas de selección.
- **Conteo**: flujo espectral en k_z — cruces de E=0 de ramas localizadas en el core
  (POR PESO, lección §33.E: disco r<8; borde = franja a <6 del borde de caja, donde
  viven los Majoranas DIII de superficie del D₄, que son física y se cuentan aparte),
  con signo = sign(dE/dk_z) al cruzar; C_neto = #(↑) − #(↓) dentro de la ventana
  entre nodos polares (|k_z| < 0.8). Tracking de ramas por solapamiento de
  autovectores entre k_z consecutivos; cruce REAL vs anticruce de hibridización
  core↔borde (artefacto de caja finita) separados por bisección: se registra
  min|E| de la rama seguida — cruce real si min|E| < 0.02 (≪ minigap ~0.06);
  resolución declarada dk_z = 0.008.
- **Diagonalización**: shift-invert sparse (σ=0, 60 autovalores por k_z,
  scipy/ARPACK; Python 3.14 + numpy + scipy 1.18, esta máquina).

**QA de armado**: hermiticidad |H−H†|_∞ = 0.0 exacta y partícula-hueco
|Ξ H(k_z) Ξ⁻¹ + H(−k_z)|_∞ = 0.0 exacta (Ξ = τ_x⊗1·K), autotesteadas en grilla
chica con campo random ANTES de correr.

## 2. La lectura física del armado (por qué la compuerta se juega acá)

El armado del BdG hace explícita la física de la compuerta — tres piezas:

1. **El fondo D₄ tiene la columna z NULA** (diag(1,−1,0)·ẑ = 0). Visto por espines:
   el sector ↑↑ aparea con p_x+ip_y y el ↓↓ con p_x−ip_y — Chern por rebanada +1 y
   −1, total CERO. Es la clase DIII del §24 hecha matriz: el fondo es mudo, y toda
   quiralidad neta tiene que nacer del defecto.
2. **A k_z fijo, el D₄ puro conserva una partícula-hueco DE REBANADA** (la columna z
   nula ⟹ el término A_μz·k_z no existe ⟹ k_z solo corre μ). Consecuencia: el HQV
   DESNUDO (vórtice en ψ₋₂ con core vacío) tendría su rama de core anclada en E≈0
   por esa simetría — rama PLANA, flujo espectral CERO.
3. **El relleno cíclico del core (Paso A) tiene columna z NO NULA** (Y₋₁ toca ẑ):
   dentro del core la PH de rebanada se ROMPE ⟹ la rama del core adquiere dispersión
   en k_z. La bisagra que el Paso A cerró (el core se llena de cíclica alineada) es
   EXACTAMENTE el ingrediente que inclina la rama; la compuerta pregunta si esa
   rama inclinada cruza E=0 un número NETO de veces.

(Esta lectura motivó un control extra del mecanismo, no pre-declarado: el "HQV
vaciado" — proyectar el campo a m ∈ {+2,−2} y verificar que el flujo neto se apaga.
Ver §5.)

## 3. Controles pre-declarados, parte k-space (los dos PASS)

**Control 1a — la cíclica uniforme reproduce el conteo topológico del §33.**
FHS (Fukui-Hatsugai-Suzuki) sobre la BZ entera de la red, proyector de las 2 bandas
negativas, con las MISMAS funciones sin/cos que la discretización real-space (la
consistencia interna que hace al control vinculante). La cíclica C₃∥z con la norma
del fondo (‖A‖ = a₀√2):

- Nodos de la red localizados (mínimos del gap exacto del 4×4, E² = ξ² + |d|² ±
  |d×d*|): proyecciones k_z = {−0.800, −0.250, +0.250, +0.800} — la estructura
  1-3-3-1 del tetraedro C₃∥z (el vértice solo proyecta a ±k_F, los tríos a ∓k_F/3;
  el 0.250 vs 0.267 del continuo es el corrimiento sin(k)≠k de la red).
- Perfil de Chern por ventana: **[0, −1, +2, −1, 0]** — el (1,−2,1,0) del §33 con
  signo global invertido. El signo global es CONVENCIÓN (orientación de la cíclica
  del GL respecto del cubo de Weyl abstracto del toy §33); lo invariante y
  verificado: |C| por ventana {0,1,2,1,0}, cargas alternadas (el vértice solo y el
  trío llevan cargas opuestas), cierre en 0 fuera de los nodos. **PASS.**

**Control 1a-bis — el D₄ uniforme es mudo con nodos SOLO polares.** Nodos localizados:
k_z = {−0.800, +0.800} (±√μ exacto, la dirección del autovalor cero del D₄ = el eje
del tubo). Chern C = 0 en k_z ∈ {0, 0.3, 0.6, 0.75}. **PASS.** El fondo no fabrica
quiralidad: todo C_neto del cálculo real es del defecto.

## 4. Controles pre-declarados, parte real-space

**Control 2 — D₄ uniforme sin defecto (caja 80×80): PASS.** Barrido de 13 k_z en
[−0.76, 0.76]: CERO cruces de E=0 con peso de core — el detector no fabrica ramas
donde no hay defecto. (Los estados sub-gap que existen son de borde/DIII, como
corresponde, y quedan fuera del conteo por peso.)

**Control 1b — cíclica uniforme sin defecto: PASS.** Mismo barrido: CERO cruces de
core, y los estados sub-gap que el Chern≠0 exige están donde deben estar — en el
BORDE de la muestra (peso de borde máximo de los 8 estados más cercanos a E=0:
0.77). El detector distingue borde de core también cuando el bulk es topológico.

## 5. El cálculo real: flujo espectral del HQV

**Resultado: C_neto = −1. Un cruce real, cero anticruces. La compuerta cierra del
lado vivo — el tubo NO es estéril.**

Barrido de 40 k_z en [−0.78, 0.78] + bisecciones (resolución dk_z = 0.008):

- **UN cruce de rama de core**, refinado a k_z ≈ 0 (el refinador reporta +0.018 con
  resolución 0.008; ver abajo la rama completa: el cruce es en k_z = 0 exacto),
  signo −1, peso de core en el cruce 0.85, min|E| = 0.0000 (cruce real, no
  anticruce). Cero anticruces de hibridización en todo el barrido.
- **Robustez al umbral de peso**: C_neto = −1 con umbral 0.25 y con 0.55 (idéntico).
- **En k_z = 0 exacto**: |E|_min = 4×10⁻⁵ con peso repartido core/borde 0.45/0.46 —
  el patrón "fermión partido" del control JR del §33 (par core±borde con peso
  0.47/0.44 allá, 0.45/0.46 acá): el Majorana del core resuena con su compañero de
  borde SOLO en el punto del cruce; el splitting 4×10⁻⁵ es el acople exponencial de
  la caja finita, seis órdenes bajo el minigap.

**La rama de core, extraída completa del barrido** (estado con peso de core >0.55
más cercano a E=0, por k_z):

| k_z | E | peso core |
|---|---|---|
| ∓0.660 | ±0.00481 | 0.58 |
| ∓0.500 | ±0.00423 | 0.81 |
| ∓0.300 | ±0.00269 | 0.87 |
| ∓0.100 | ±0.00092 | 0.89 |
| ∓0.020 | ±0.00019 | 0.85 |

- **E(k_z) es IMPAR exacta dígito a dígito** (E(−k_z) = −E(k_z) en las 34 filas):
  la rama es self-conjugada bajo la PH global — por eso UN cruce único en k_z=0 es
  consistente (no exige partner espejado; un cruce en k_z*≠0 sí lo exigiría).
- **Cuasi-plana**: |E|_max ≈ 0.0048 — QUINCE veces por debajo del primer nivel CdGM
  (~0.075, visible en el espectro como la escalera del core). Es la herencia
  cuantitativa de la PH de rebanada del fondo (§2): la inclinación viene solo del
  relleno cíclico, que vive en r≲3 — efecto ~6% del minigap.
- **Velocidad del modo quiral: v = dE/dk_z ≈ −0.009** (ajuste |k_z|<0.35), o sea
  v/v_F ≈ 0.006: la materia del tubo es quiral y LENTA.
- **Extensión**: la rama es rastreable con peso de core alto hasta |k_z| ≈ 0.66 y
  ahí empieza a deslocalizarse (peso 0.58) — muere fundiéndose en los nodos polares
  del fondo (±0.8): la rama del defecto CONECTA las proyecciones de los dos nodos
  del D₄ pasando por E=0 — anatomía de rama tipo Callan-Harvey entre nodos.

**Lectura**: |C_neto| = 1 con el winding fraccionario del HQV — "el winding
fraccionario parte el conteo a la Majorana" que el §33.F dejó declarado como
refinamiento pendiente, ahora CALCULADO: el nudo lleva exactamente UNA rama quiral
neta tipo Majorana (media materia de Dirac por tubo). Figura:
`paso_b_flujo_hqv.png`; datos: `paso_b_flujo_hqv.npz` (regenerable).

## 6. Espejo y estabilidad (controles 3 y 4)

**Control 3 — espejo: PASS.** Campo conjugado (x_im → −x_im ⟹ A → A*, el HQV
(−½,−¼) del QA2 del Paso A): UN cruce, mismo |k_z| y peso (0.85), **signo +1 —
C_neto = +1 = −C_neto(real), inversión exacta**. La quiralidad de la materia
fermiónica del tubo es esclava del winding — lo que el Paso A probó a nivel GL
(cores espejados), ahora en los fermiones: nudo y anti-nudo llevan media-rama
quiral de signos opuestos (las anti-clases del scorecard, versión materia).

**Control 4 — estabilidad en Δ₀ y μ: PASS.** Cuatro deformaciones, mismo protocolo
(28 k_z en ±0.97·k_F de cada μ, refinamiento incluido):

| corrida | C_neto | cruces | anticruces | peso core en el cruce |
|---|---|---|---|---|
| Δ₀×0.7 | **−1** | 1 | 0 | 0.69 |
| Δ₀×1.4 | **−1** | 1 | 0 | 0.95 |
| μ×0.8 | **−1** | 1 | 0 | 0.81 |
| μ×1.2 | **−1** | 1 | 0 | 0.90 |

El conteo NO se mueve con el gap ni con la densidad (régimen declarado: gap de
bulk abierto fuera de los nodos polares, que se corren a ±√μ). El peso del modo
sube con Δ₀ (más localizado, ξ_BdG más chica) y viceversa — la física esperada,
sin sorpresas. **C_neto = −1 es topológico.**

## 6-bis. El control del mecanismo: el HQV vaciado (bonus, no pre-declarado)

Proyectando el campo del npz a m ∈ {+2,−2} (se quita el 15.9% de la norma — todo
el relleno m=±1/0 del core) el campo queda con columna z IDÉNTICAMENTE NULA ⟹ la
PH de rebanada es exacta en toda la muestra (§2). Resultado del mismo barrido:

- **C_neto = 0.** Los eventos que aparecen son 14 PARES de cruces (+1,−1) EN EL
  MISMO k_z (±0.732, ±0.698, ±0.657, ±0.603, ±0.532, ±0.443, ±0.308 — espejados
  exactos por la PH global), cada par con neto CERO: son las rotaciones de
  carácter del par core↔borde degenerado (±ε con el acople oscilando por cero,
  tipo Friedel), no flujo espectral. Peso ~0.45 (mezcla 50/50) en todos — la
  firma del par partido, nunca la rama pura de 0.85 del cálculo real.
- **CERO eventos en el origen**: el cruce central del real — el que da C_neto=−1 —
  DESAPARECE al vaciar el core. En k_z=0 el Majorana del HQV desnudo sigue
  existiendo (|E|_min = 4×10⁻⁵, peso 0.45) pero PLANO: no cruza, no fluye.

**El mecanismo queda probado punta a punta: la rama quiral neta del tubo NO es
del HQV desnudo — es del relleno cíclico del core.** La bisagra que el Paso A
cerró (el core se llena de cíclica alineada) es la condición NECESARIA de la
materia del tubo; el Paso B muestra que también es SUFICIENTE. Figura:
`paso_b_flujo_vaciado.png` (la rama plana con sus pares cancelados, para
contrastar con `paso_b_flujo_hqv.png`).

## 7. Veredicto para la compuerta única

1. **El criterio de muerte NO se gatilla.** §34.D pre-declaró: C_neto=0 o pinning
   blando ⟹ 10ª lápida (tubos estériles, la Arquitectura A pierde materia y
   fotón). El Paso A dio pinning DURO; el Paso B da **C_neto = −1 ≠ 0**. La
   compuerta única — de la que colgaban la materia de los tubos, el U(1)
   fermiónico candidato a fotón (§34.A) y el M1 de Newton — cierra del lado vivo.
2. **Lo que el nudo lleva de serie**: exactamente UNA rama quiral tipo Majorana
   (media materia de Dirac por tubo), lenta (v/v_F ≈ 0.006), con la quiralidad
   esclava del winding (nudo y anti-nudo llevan quiralidades opuestas — las
   anti-clases del scorecard de partículas, ahora a nivel fermiónico). El
   refinamiento "el winding fraccionario puede partir el conteo a la Majorana"
   (§33.F) queda CALCULADO: |C_neto| = 1, la mitad del vórtice entero.
3. **La cadena §25→§33→§34 se cierra**: el Weyl 3D no sobrevivía en el tubo (§25),
   el conteo del cíclico puro no aplicaba textual (§34.D, el crítico tenía razón:
   hizo falta comer el campo 2D completo), y la respuesta real es la mínima
   posible pero NO nula. "El nudo no es estéril: viene con su materia alineada
   de fábrica — y ahora está contada: una."
4. **Consecuencias río abajo (sin calcular, declaradas)**: (a) el U(1) fermiónico
   de los tubos (§34.A) tiene su portador — el siguiente eslabón es el fermión
   ENTERO por tubo vía anomaly inflow y el Gauss en las uniones de la red (los 2
   FALTA duros del §34.A siguen pendientes); (b) para anillos (partículas), la
   rama quiral sobre un lazo cerrado discretiza — conecta con la escalera de
   niveles del §25 y el twist como número cuántico (§33.D, abierta); (c) la
   velocidad chica del modo (v≪v_F) es un dato nuevo para la fenomenología de
   la materia de nudos (masa efectiva grande del portador 1D).
5. **Deudas heredadas que NO se tocan hoy**: anisotropía de la energía de línea
   del tubo según orientación (Paso A §5.4), espectro de fluctuación del
   tetraedro, tubo→anillo (¿el tetraedro co-rota?), y los dos FALTA del U(1) de
   la red. El examen de Carlip (tétrada nodal vs métrica TT del bulk) sigue
   intacto en la cola.

## 8. Reproducibilidad y erratas

`paso_b_bdg_core.py` (este directorio; modos: `controles` / `real` / `espejo` /
`estabilidad` / `vaciado`; Python 3.14 + numpy + scipy 1.18, esta máquina,
2026-07-29, ~44 min total). Recibos commiteados: `paso_b_resultados_*.json`
(controles/real/espejo/estabilidad/vaciado) y las figuras
`paso_b_flujo_hqv.png` / `paso_b_flujo_vaciado.png` (generadas con
`paso_b_grafico.py`). Los barridos completos (`paso_b_flujo_*.npz`) y el campo
de entrada (`paso_b_core.npz`) son locales regenerables (excluidos de git; el
campo se regenera con `paso_b_core_input.py` del Paso A).

Detalles numéricos de los recibos: el cruce del real tiene E = ±0.000193 en
k_z = ∓0.0175 alrededor del cero (pendiente local 0.011, consistente con el
ajuste global v ≈ 0.009); el espejo lo invierte con los pesos idénticos a
1×10⁻¹³ (misma maquinaria, campo conjugado — la inversión es exacta, no
aproximada).

**Erratas propias de la sesión: cero en producción.** Dos defectos de
herramienta cazados ANTES de correr y reescritos: (1) un error de sintaxis en el
graficador (argumento posicional tras keyword); (2) el refinador de cruces v1
tenía lógica de anclaje frágil (re-diagonalizaba el extremo izquierdo en cada
bisección y el criterio de signo era confuso) — reescrito con seguimiento por
solapamiento + registro de min|E| antes de producir ningún número. El detector
de "cruce vs anticruce" por min|E| (umbral 0.02 ≪ minigap 0.075, resolución
dk_z = 0.008) no encontró ningún anticruce en el real — la separación core-borde
de la caja (splitting 4×10⁻⁵) nunca contaminó el conteo.

*Acta del Paso B, escrita el mismo día de la corrida. La compuerta de la que
colgaba todo el mundo de baja energía de la Arquitectura A estaba en verde por
el lado de la energía (Paso A) y hoy queda en verde por el lado del conteo: el
mar anuda sus defectos Y los puebla — una rama quiral por nudo, con el signo
del nudo. Lo próximo: de la rama del tubo al fermión de la red (anomaly inflow
+ Gauss en las uniones), y del tubo recto al anillo.*
