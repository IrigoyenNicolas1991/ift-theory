# BITÁCORA TCI 2.0 — La campaña del condensado (2026-07-16/17)

> **Versiones divulgativas de este trabajo** (con simulaciones jugables):
> [«El mar y sus nudos»](https://irigoyennicolas1991.github.io/ift-theory/mar-y-nudos/)
> (la materia) y
> [«El taller electromagnético del mar»](https://irigoyennicolas1991.github.io/ift-theory/taller-electromagnetico/)
> (el EM). Esta bitácora es su respaldo formal.

> ⚠️ **ETAPA ESPECULATIVA EN DESARROLLO** — Esto NO es parte del corpus TCI publicado
> (sitios/Pages/Zenodo). Es investigación exploratoria en curso, con hipótesis vivas,
> ideas muertas documentadas y cálculos preliminares. Nada de lo que sigue está
> validado ni reclamado. Backup en la nube autorizado por Nico el 2026-07-17,
> manteniendo separación total del material publicado. La línea de partículas queda
> fuera de la divulgación; material compartible solo a pedido.

Registro cronológico de una campaña de investigación (~12 horas, 10 agentes
bibliográficos, 3 scripts numéricos). Las secciones §1-6 son el pensamiento inicial de
la noche — varias ideas de ahí fueron FALSADAS horas después por los propios agentes
(ver §7 en adelante); se conservan sin editar como registro honesto del proceso.

---

## 1. La pregunta del paso A

Encontrar un patrón de ruptura G → H que cumpla: (i) no rompe traslaciones, (ii) no deja
dirección observable (CMB isótropo), (iii) da modos ±2 sin masa COMO GOLDSTONES, (iv)
tiene espacio de orden con topología para nudos.

## 2. Familia F — "la forma no cuesta" (candidata para la gravedad)

**Idea:** que la simetría protectora sea: *deformar uniformemente la FORMA del mar
(cizalla pura, volumen fijo) no cuesta energía*. Solo cuestan las variaciones de forma
de un lugar a otro (gradientes). Entonces, por Goldstone, las ondas de forma no tienen
masa — prohibida por simetría, no ajustada.

- La forma local de una región = deformación simétrica sin traza 3×3 = **5 componentes
  = exactamente un quinteto spin-2** (helicidades 0, ±1, ±2).
- En lenguaje de grupos: simetría interna SL(3,ℝ) sobre las coordenadas comóviles Φᴬ
  (transformaciones lineales que preservan volumen), rota al SO(3) diagonal con las
  rotaciones espaciales. Generadores rotos = las 5 cizallas → quinteto de Goldstones.
- **Consistencias que dan esperanza:**
  - Un medio al que la cizalla uniforme no le cuesta es *tipo fluido*, no sólido —
    encaja con la ironía de la nota 10 (solid inflation mata a los sólidos; TCI 1.0
    erró por "sólido").
  - En fluidos los modos transversales de desplazamiento no propagan (ω=0) — huele a
    los "vectores no-dinámicos" de la fase m₂=0 de Dubovsky. A verificar en paso C.
  - Estado base Φᴬ = xᴬ preserva el SO(3) diagonal → sin dirección privilegiada ✓ (iii)... 
    ojo: (ii) en realidad. Isotropía OK.
  - Traslaciones internas de Φᴬ intactas → checkpoint (i) OK a primera vista.
- **Peligros conocidos:** inverse Higgs puede comerse o degenerar modos (rotaciones
  espaciales y cizallas internas no conmutan trivialmente); que el quinteto PROPAGUE
  con término de gradiente sano es tarea del paso B; SL(3,ℝ) es no-compacto → cuidado
  con energías no acotadas / ghosts. TODO por verificar.

## 3. Familia N — cuadrupolo de norma fija (candidata para los nudos)

Parámetro de orden tipo nemático (cuadrupolo unitario):

- Uniaxial: espacio de orden ℝP² → π₁ = ℤ₂. Defectos de línea con carga mod 2 (una
  sola clase no trivial; +1 = −1). Curioso pero pobre para la tabla de partículas.
- Biaxial: π₁ = grupo de cuaterniones Q₈ — **defectos no abelianos** (Mermin, RMP 51:591
  1979, textbook). Taxonomía rica: varias clases, reglas de fusión no triviales.
- **Problema fatal para gravedad en esta familia sola:** los Goldstones del nemático
  son las inclinaciones ±1 del director (no ±2); los modos J=2 son de amplitud y
  MASIVOS (exactamente el problema de ³He-B, nota 11 §3.1); y un director fijo rompe
  isotropía observable → muerto para (ii) salvo truco tipo ³He-B (preservar rotación
  combinada).

## 4. LA TENSIÓN (el hallazgo honesto de la noche)

**Los frutos 1 y 2 de la nota 11 tiran para lados opuestos:**

- Masa cero por Goldstone pide un espacio de orden "abierto" tipo Familia F. Pero
  SL(3,ℝ)/SO(3) ≅ ℝ⁵ (matrices simétricas definidas positivas unimodulares: convexo)
  es **contráctil → π_n triviales → CERO defectos topológicos**. La no-compacidad que
  regala la masa cero mata los nudos.
- Los nudos piden espacio "cerrado" (compacto, con vueltas) tipo Familia N. Pero ahí
  los modos relevantes son masivos y hay anisotropía.

**En criollo: la gravedad quiere una pradera abierta; la materia quiere un laberinto.
El mar tiene que ser las dos cosas a la vez.**

## 5. Direcciones de síntesis (para la próxima sesión, en orden de prioridad)

1. **Producto:** espacio de orden = (parte no-compacta de forma: gravedad) × (parte
   compacta: nudos). ¿Existe un condensado natural con ambas? ¿Los defectos de la parte
   compacta se "visten" con deformación de la parte de forma (el nudo genera huella =
   masa/carga gravitatoria)? Eso realizaría la monometricidad: materia y gravedad del
   mismo objeto.
2. **Plan B conservador:** la materia sigue siendo el sector escalar φ (huecos/vacancias
   de TCI 1.0, que ya funciona) y la Familia F pone SOLO la gravedad. Se pierde el
   regalo de la cuantización de carga por topología; los nudos quedan como conjetura
   aparte. Menos lindo, más seguro.
3. **Truco ³He-B generalizado:** ¿hay patrón donde el grupo roto incluya un 5-plete
   compacto (p.ej. subgrupos de SO(5)? ¿SU(3), cuyos 8 generadores contienen un 5+3?)
   preservando una rotación combinada? Chequear si algún patrón compacto da Goldstones
   ±2 sin masa sin el costo de la no-compacidad. (Especulativo al cubo; mirar la
   zoología primero.)

## 7. VEREDICTO DE LA FLOTA (misma noche — 4 agentes bibliográficos, todo verificado en fuentes)

### A) Familia F (SL(3)) — MUERTA tal como se soñó en §2

- NPPR 1501.03845 §2.1 caso 7 la considera EXPLÍCITAMENTE (grupo afín especial): el medio
  existe y es consistente, pero tiene **solo 3 Goldstones, no 3+5** ("still featuring three
  Goldstones", textual), y a orden dominante recupera Diff′(3) como simetría accidental →
  **indistinguible de un fluido ordinario en el IR**. El quinteto de §2 no existe.
- Peor: el sector transverso del fluido perfecto cuántico es patológico (acoplamiento
  fuerte a toda escala, Endlich-Nicolis-Rattazzi-Wang 1011.6396). "Fluido con ondas de
  corte sanas no disipativas" NO existe como EFT conocida; el único shear propagante real
  en líquidos es disipativo con k-gap (Maxwell-Frenkel; Phys. Rep. 865 (2020) 1; PRL 118,
  215502).
- **Rescate confirmado:** m₂ = 0 ⟺ medios tipo fluido (Celoria-Comelli-Pilo 1704.00322
  Tabla 3: fluido M₁=M₂=0, sólido M₂≠0; Dubovsky hep-th/0409124 verificado textual). El
  destino era correcto; el mecanismo propuesto, no.
- Preocupación de ghosts por no-compacidad: TACHADA. SL(3,ℝ)/SO(3) es coset riemanniano
  (SO(3) = compacto maximal) — misma estructura que los escalares de supergravedad, sin
  patologías (1512.06838; Samtleben 0808.4076). El peligro real era otro (el de arriba).

### B) LA NUEVA CANDIDATA — cuadrupolo INTERNO tipo nemático de spin (Familia N revivida)

- **Kirby-Rau et al., arXiv:2310.10078 ("Gravitational wave analogues in spin nematics
  and cold atoms")**: en nemáticos de spin los Goldstones son **excitaciones spin-2 SIN
  MASA con dispersión relativista** — análogos explícitos de ondas gravitacionales;
  propuesta de observación en condensados de ²³Na. Complemento: arXiv:2503.13888 (posible
  observación de ondas cuadrupolares en un spin nematic). **El mecanismo que la Familia F
  no tenía, publicado y camino a medirse.**
- El espacio de orden es COMPACTO → **la tensión pradera/laberinto de §4 SE DISUELVE**:
  el mismo objeto da Goldstones ±2 sin masa (pradera dinámica) Y homotopía no trivial
  (nudos). No hacen falta dos factores.
- Costo declarado: el nemático de spin rompe rotaciones (director) → anisotropía. Arreglo
  con precedente doble: patrón ³He-B (pseudo-isotropía VERIFICADA en laboratorio: solo se
  rompe la rotación relativa interno↔espacial; sonda ninguna ve dirección) + su traslación
  a gravedad ya propuesta por Volovik (2111.07817: tetrad como parámetro de orden,
  SO(3)×SO(3)→SO(3) diagonal). Cotas que obligan a esto: tensor que elige dirección
  espacial muere (CMB 10⁻⁵; SME hasta 10⁻¹⁵ por canal); el patrón diagonal es viable por
  construcción (análogo vectorial vivo: Einstein-aether, Jacobson 0801.1547).
- **Lección estructural de Zaanen et al.** (1603.04254, 1703.03157, "Crystal gravity"
  2109.11325): el orden debe ser INTERNO (tipo spin), NO elástico-espacial. Los nemáticos
  cuánticos que vienen de fundir sólidos GAPEAN su sector de cizalla (Higgs dual), y
  sólido + gravedad dinámica = fase de Higgs del gravitón. "Gotas con orientación
  interna", no deformaciones de posiciones. Consistente con inverse Higgs (Low-Manohar
  hep-th/0110285; Brauner-Watanabe 1401.5596): **las traslaciones deben quedar intactas**
  para que los ±2 sean modos independientes — el nemático de spin cumple.
- **Territorio reclamable verificado por búsqueda**: la combinación completa (condensado
  cuadrupolar interno + isotropía por rotación combinada + spin-2 gapless) NO existe en
  la literatura. Riesgo simétrico de siempre: quizá nadie la armó porque no cierra.

### C) Los dragones con nombre (obstrucciones verificadas; cualquier construcción debe
enfrentarlas explícitamente, no ignorarlas)

1. **Carroll-Tam-Wehus 0904.4680**: aun cuando los Goldstones calcan al gravitón de GR a
   nivel clásico, las correcciones radiativas generan infinitos términos LV — velocidad
   dependiente de la dirección, gravi-Cherenkov. **La respuesta que TCI apuesta:
   monometricidad (materia = defectos del MISMO medio → todas las especies heredan las
   mismas anisotropías → Lorentz relativo preservado, à la Volovik). Este es ahora EL
   cálculo conceptualmente decisivo del programa a largo plazo.**
2. **Marolf 1409.2509** ("Emergent gravity requires kinematic nonlocality"): más fuerte
   que Weinberg-Witten, no asume Lorentz. Afecta la gravedad no lineal completa con
   acople universal; grieta conocida: cinemática no local. Pesa sobre el paso "dinámica
   de Einstein", no sobre el gravitón linealizado.
3. **Inverse Higgs**: no romper traslaciones, jamás (si se rompen, los ±2 se los comen
   los fonones). Restricción de diseño permanente.
4. **No-virginidad del eslogan**: gravitón-Goldstone existe desde 1966/1974 (Phillips;
   Borisov-Ogievetsky, Goldstones de cizallas de GL(4); Kraus-Tomboulis 2002). Lo
   distinto acá: condensado no relativista, marco privilegiado, cuadrupolo interno,
   materia = defectos del mismo orden. Citarlos siempre; no reclamar de más.

### D) Perla suelta para el fruto 3 (anotada, prioridad baja)

El único shear propagante en fluidos reales es disipativo (k-gap). La disipación no es
enemiga en el paso E: el decaimiento orbital ES el observable de Hulse-Taylor. Pregunta
especulativa anotada: ¿la radiación de una binaria de defectos en un medio con sector
k-gap tiene la forma del cuadrupolo? (Conecta con la 4ª lección de las sims del libro:
las órbitas decaen por fricción de onda.)

## 8. Paso A actualizado — próximo movimiento concreto

1. ~~Leer a fondo 2310.10078 + 2503.13888~~ HECHO (ver §9).
2. Diseñar el "lock" isotrópico: cuadrupolo interno + rotaciones espaciales → SO(3)
   diagonal (à la ³He-B/Volovik), verificando que los ±2 sigan gapless tras el lock.
3. Recién entonces, paso B: lagrangiano en lenguaje BCP → masas m₀…m₄ → fase de Dubovsky.

## 9. Lectura profunda del nemático de spin (misma noche)

**CORRECCIÓN DE ATRIBUCIÓN**: arXiv:2310.10078 es de **Chojnacki, Pohle, Yan, Akagi,
Shannon (OIST)**, PRB 109, L220407 (2024). "Kirby-Rau" (reporte del agente anterior) era
un dato falso — corregido acá y en memoria.

### Lo que el paper realmente da (letra chica primero)

- La analogía es **solo con gravedad linealizada en espacio plano**: misma acción
  cuadrática (su Eq. 16 ↔ Fierz-Pauli TT), misma ecuación de onda, mismas polarizaciones
  +/×. Sin métrica efectiva, sin acople a T_μν, sin no-linealidad, sin difeos.
- **El spin-2 es INTERNO** (espacio de spin): declaran textualmente que sus ondas
  cuadrupolares viven en spin-space "automáticamente 3D sea cual sea la dimensión
  espacial". La transversalidad respecto de la propagación se instala por un diccionario
  (transformación C(k,d) del Supplemental), no por física. Sin spin-orbit locking.
- La reducción 5→2 componentes es **energética** (solo las fluctuaciones transversas del
  director son gapless), no de gauge. Compatible con apuntar a la fase m₂=0 (que también
  es "los sobrantes no dinámicos", no gauge).
- Estado FQ de magneto spin-1: Q^mn = ½{S^m,S^n} − ⅓δ^mn S², director d, vacío ℝP²
  (π₁=ℤ₂ confirmado; sus propios vórtices son ℤ₂). Dispersión lineal genérica
  ω = √(ρ_s/χ⊥)|k| — la "c" del análogo es rigidez/susceptibilidad, sin ajuste. ✓
- Experimento (2503.13888, PRL 135, 156704): "Possible Observation" — el título fue
  degradado en referato; material Na₂BaNi(PO₄)₂, nematicidad inferida vía modelo (iPEPS
  sin parámetros libres), y NO es el estado FQ del paper 1. Estado: sugerente, no cerrado.

### La joya escondida (directo al fruto 3)

En el paper 1, la fuente de las ondas cuadrupolares son **pares de vórtices ℤ₂ del mismo
condensado que espiralan uno hacia el otro, radian ondas cuadrupolares y se aniquilan**
(numérico, tras un quench). Es un **mini-Hulse-Taylor del análogo**: binaria de defectos
que inspirala por radiación de los modos spin-2. Nadie lo formalizó con un T_μν efectivo
ni derivó la fórmula del cuadrupolo para estos vórtices (VERIFICADO: no encontrado). El
paso E de la nota 11 tiene precedente numérico publicado y hueco analítico reclamable.

### Los nudos disponibles (verificado, literatura estándar)

- Magneto FQ (ℝP²): π₁=ℤ₂ (vórtices que se aniquilan de a pares), π₂=ℤ (monopolos, con
  signo invertible al rodear un vórtice — carga física |n|), π₃=ℤ (texturas de Hopf).
- Condensado polar spin-1 (caso ²³Na): vacío (U(1)×S²)/ℤ₂ → π₁=ℤ generado por el
  **vórtice semicuántico (vórtice de Alice)** — ¡carga ENTERA, no mod 2! — observado
  experimentalmente (Seo et al. PRL 2015; también en ³He polar). π₂=ℤ, π₃=ℤ.
- Para la taxonomía del paso D, el candensado polar es más rico que el magneto puro:
  cargas enteras + fase U(1) (¿el sector EM?) + monopolos + Hopf.

### Los tres agujeros estructurales (nadie los tapa; son NUESTRO trabajo)

1. **El lock**: sin spin-orbit locking la helicidad ±2 espacial es un diccionario, no
   física. El ingrediente a robar es el del ³He-B: romper la rotación RELATIVA
   interno↔espacial, preservando la diagonal. Cálculo concreto: agregar al FQ un término
   de acople orbital y ver si (a) los 2 Goldstones sobreviven gapless, (b) se vuelven
   helicidad ±2 genuina, (c) no se viola isotropía. **ESTE ES EL PRÓXIMO CÁLCULO.**
   **ADVERTENCIA DE DISEÑO (detectada al armar la búsqueda)**: en ³He-B el lock es un
   término EXPLÍCITO del hamiltoniano (interacción dipolar) → el Goldstone acoplado se
   vuelve pseudo-Goldstone CON GAP (frecuencia de Leggett). Un lock explícito nos
   regalaría masa — exactamente lo que no podemos tener. El lock debe ser ESPONTÁNEO:
   G = SO(3)_int × SO(3)_esp exactas en el hamiltoniano, rotas por el condensado al
   diagonal. Verificación bibliográfica en curso (¿existe? ¿aparecen Goldstones extra
   vectoriales no deseados de la rotación relativa?).
2. **El acople universal**: derivar que toda excitación/defecto del condensado siente la
   misma métrica efectiva construida con Q (monometricidad = la apuesta estructural TCI).
3. **La no-linealidad de Einstein**: el dragón de Marolf espera al final del camino.

## 10. VEREDICTO DEL LOCK (misma noche, 5º agente) — el lock ingenuo MUERE; nace la ruta SU(3)

### Lo bueno (confirmado con precedentes sólidos)
- **El lock espontáneo de simetrías exactas NO gapea nada.** ³He-B ideal (sin dipolar):
  3 spin waves exactamente gapless; el gap de Leggett es 100% culpa del término dipolar
  EXPLÍCITO, y solo toca el modo del que depende ese potencial. Más precedentes: CFL en
  QCD densa (octete de Goldstones), color-spin locking (Brauner 0909.4201). Principio
  firme: ruptura espontánea de simetría exacta ⇒ gapless exacto.

### Lo malo (obstrucción de teoría de grupos, verificada empíricamente)
- **Ningún lock de SO(3)×SO(3) puede dar Goldstones de helicidad ±2**: los generadores
  rotos viven en la adjunta = J=1; el coset es VECTORIAL. Sistema real de control:
  materia de neutrones ³P₂ (¡orden tensorial J=2 genuino lockeado al espacio, existe en
  estrellas de neutrones!): 2 "angulones" gapless de helicidad ±1 y los modos m=±2
  MASIVOS (Bedaque-Nicholson-Sen 1408.5145; releer sección de modos si esto se vuelve
  load-bearing). 
- **Los "Goldstones spin-2" de Chojnacki, desnudados**: son fluctuaciones Q_xz, Q_yz
  (tilts del director, m=±1); la correspondencia con ε⁺,ε× se hace con una transformación
  unitaria C(k,d) que los autores admiten mal definida en k→0 (huele a obstrucción tipo
  hairy-ball; "future work"). Textual: la estructura del modo NO depende de k̂ — al revés
  que una GW real. Si lockeás el FQ al espacio: ondas de director helicidad ±1. **El
  candidato §B, tal como se formuló anoche, queda FALSADO por teoría de grupos.**
- Peligro inverso confirmado: el lock espontáneo AGREGA Goldstones (los 3 relativos J=1),
  no convierte los existentes. Espectro equivocado en número y helicidad.

### La salida señalada (nueva candidata, más afilada)
- **Para que los modos m=±2 sean Goldstones, los generadores cuadrupolares deben SER
  generadores de simetría** → grupo interno MÁS GRANDE que SO(3). Candidato natural:
  **SU(3)** — y el punto simulado por Chojnacki (BBQ con J₁=0) ¡tiene simetría SU(3)
  exacta! Descomposición clave (verificada a mano, teoría de grupos elemental):
  G = SU(3)_int × SO(3)_esp → SO(3)_diag deja **8 generadores rotos = 3 (J=1, rotación
  relativa) ⊕ 5 (J=2, ¡el quinteto!)** — la helicidad ±2 SÍ está disponible en este
  coset. Nadie publicó ese lock (verificado): territorio virgen con el obstáculo de
  grupos resuelto de frente, no esquivado.
- **Costos declarados de la ruta SU(3)**: (i) TCI debería postular SU(3) interna EXACTA
  (fuera del punto especial es explícita-rota → pseudo-Goldstones gapeados tipo Leggett);
  (ii) el triplete J=1 relativo también sale gapless → hay que silenciarlo (¿no-dinámico
  à la Dubovsky? ¿gapeado por qué?) — problema de espectro a confrontar, no ignorar;
  (iii) conteo type-A/B de Watanabe-Murayama (PRL 108 251602) por hacer con cuidado
  (los conmutadores de cuadrupolos dan spins; ⟨S⟩=0 en el nemático → naïve todo type-A,
  VERIFICAR); (iv) Weinberg-Witten siempre al fondo si hay T_μν Lorentz.
- **Control previo obligatorio**: espectro conocido del FQ en el punto SU(3) del BBQ
  (estabilizador U(2), coset CP², flavor waves) — pedido a agente de control.

## 11. CONTROL FQ@SU(3) (6º agente) — dos errores míos corregidos y la ruta SU(3) ingenua también cae

### Fe de erratas propia (documentada como corresponde)
1. **El punto SU(3) del FQ es J₁=J₂<0 (θ=−3π/4), NO J₁=0.** El punto que simula
   Chojnacki (J₁=0, biquadrático puro, triangular) es un punto GENÉRICO del FQ sin SU(3).
   Mi "coincidencia que eriza" de §10 era falsa. (Läuchli-Mila-Penc PRL 97 087205,
   textual; Völl-Wessel PRB 91 165128 — ambos leídos completos por el agente. Ojo además:
   LMP tiene un factor 2 errado en A(k),B(k), corregido en VW.)
2. **Mi heurística "⟨S⟩=0 ⟹ todo type-A" era incorrecta en el punto SU(3)**: el
   apareamiento de Watanabe-Murayama es S↔Q (⟨[S^x,Q^{yz}]⟩ = ⟨Q^{zz}−Q^{yy}⟩ = −1 ≠ 0)
   ⟹ n_B=2, n_A=0. Con carga cuadrupolar no nula el FQ@SU(3) es un "ferromagneto de
   SU(3)" aunque ⟨S⟩=0.

### El resultado de control (doble fuente, flavor-wave = QMC exacto en el punto)
- FQ@SU(3): rompe SU(3)→U(2), vacíos = **CP²** (dim 4, ¡π₁=0, π₂=ℤ — topología DISTINTA
  de RP²!), espectro = **2 modos CUADRÁTICOS degenerados** (ω ≈ (3/√8)|J|k², type-B).
- FQ genérico (fuera del punto): 2 modos LINEALES type-A, v ∝ √(J₂(J₂−J₁)) → 0 al
  acercarse al punto. Sin pseudo-Goldstones gapeados a orden armónico.
- **Estos números son ahora los controles de calidad obligatorios de cualquier cálculo
  nuestro**: si nos da otra cosa en estos límites, está mal el cálculo.

### Por qué esto mata la ruta SU(3) *tal como la formulé en §10*
1. **Dispersión**: en el punto SU(3) exacto los Goldstones son CUADRÁTICOS (type-B) —
   una onda gravitacional necesita ω = ck lineal. Lo lineal vive FUERA del punto, donde
   SU(3) está explícitamente rota y volvemos a la obstrucción de §10.
2. **Peor (verificado a mano por mí, aritmética de su(3))**: los generadores m=±2
   (Q^{x²−y²}, Q^{xy}) **ANIQUILAN el estado FQ** — son parte del estabilizador U(2),
   están NO-ROTOS. El coset CP² del FQ contiene solo los canales m=±1 (S^x,S^y,Q^{xz},
   Q^{yz}). O sea: ni siquiera con SU(3) exacta el nemático uniaxial rompe los
   generadores de forma ±2. Y como todo estado puro de la representación fundamental es
   SU(3)-equivalente a |z⟩, **ningún condensado coherente fundamental de SU(3) rompe los
   ±2**. La ruta necesita otra cosa.

### La bifurcación honesta que queda (las dos únicas rutas vivas)
- **(a) Goldstone con parámetro de orden en representación MÁS ALTA**: para romper los
  generadores ±2 hace falta orden tipo ADJUNTA de SU(3) (matriz 3×3 hermítica sin traza
  con autovalores distintos → estabilizador T² = U(1)×U(1), coset = variedad bandera
  SU(3)/T², dim 6, TODOS los canales m=±1 y m=±2 rotos). Literatura a verificar: flag
  manifold magnets (Lajkó-Wamer-Affleck-Mila y descendencia; el modelo staggered de
  2502.14605 con patrón SU(3)→U(1)×U(1) y N_B=2). Preguntas: ¿dispersiones? ¿type A/B
  por canal? ¿alguien lo lockeó al espacio? → 7º agente despachado.
- **(b) No-Goldstone: masa cero protegida por difeos espaciales NO ROTOS** (la fase
  m₂=0 de Dubovsky = fluido; la ruta Volovik-tétrada). La masa nula no viene del teorema
  de Goldstone sino de una simetría residual tipo gauge. Consistente con TODO lo
  aprendido esta noche (barco 1: m₂=0 ⟺ fluido; barco 4: Volovik). El rol del orden
  cuadrupolar sería otro: no dar los Goldstones, sino dar el SUSTRATO cuya dinámica
  efectiva cae en esa fase.
- El teorema de la noche (informal pero triple-verificado): **el camino Goldstone hacia
  helicidad ±2 lineal está cerrado para órdenes rotacionales y para condensados
  coherentes de SU(3); solo quedan la representación adjunta (a) o el mecanismo gauge
  (b).** El corredor es angosto y específico — así se ve un problema de verdad.

## 12. RUTA (a) VIVE — veredicto del 7º agente (bandera/trípode)

**Corrección de cita**: Tóth-Läuchli-Mila-Penc es arXiv:1009.1398 (PRL 105 265301 +
erratum), no 1010.3231.

### Los tres hallazgos (de menor a mayor)
1. **Bandera staggered (antiferro 3 subredes, SU(3)→T²)**: 6 Goldstones type-A
   **LINEALES** incluidos los canales ±2 (LFWT textual: 1706.06598, 1009.1398, 1112.1100).
   La dispersión correcta existe en el patrón bandera. PROBLEMA: es orden modulado
   espacialmente (3 subredes) → toca traslaciones (regla prohibida). La versión uniforme
   (ferro-adjunta) daría 3 type-B CUADRÁTICOS (inferencia WM sobre su(3); ojo:
   contradicción viva en literatura — Zhou et al. 2302.13126/2502.14605 reportan N_B=2 +
   flat bands ω=0 con estados entrelazados no coherentes; no zanjado).
2. **Nemático BIAXIAL de spin-2 (BEC F=2, real, átomos fríos)**: Uchino-Kobayashi-Ueda
   0912.0355 textual — 4 generadores rotos, **5 modos gapless TODOS LINEALES** (+1
   quasi-NG por SO(5) accidental), con el condensado viviendo en los canales m=±2 (el
   Goldstone de F_z = fase relativa ψ₂/ψ₋₂ es un modo de canal ±2: bajo rotación φ,
   ψ±2 → e^∓2iφ — ¡carga 2 genuina!). Sin SU(3): solo SO(3)×U(1). El biaxial rompe las
   3 rotaciones (no solo 2 como el uniaxial).
3. **EL SISTEMA REGALO: el superfluido ³P₂ de estrellas de neutrones** — condensado J=2
   con el LOCK ESPACIAL DE FÁBRICA (pairing con J=L+S=2: el tensor transforma bajo
   rotaciones espaciales totales; la naturaleza ya soldó interno↔espacial). Fase
   uniaxial calculada: 2 angulones lineales anisótropos (Bedaque-Nicholson 1307.8183).
   **Fases BIAXIALES (D₂-BN, D₄-BN) existen en el diagrama GL (Yasui-Chatterjee-Nitta
   1810.04901) pero NADIE calculó su espectro de angulones — hueco real verificado.**
   Formalismo listo para robar: GL de ³P₂ + EFT de angulones.

### El cálculo concreto no-reclamado que emerge (candidato a primer cálculo TCI 2.0)
**Espectro de angulones de la fase biaxial del condensado J=2 (tipo ³P₂-BN)**: ¿hay
modos gapless lineales de helicidad espacial ±2 genuina? El biaxial rompe la rotación
alrededor del eje principal, y esa rotación actúa con carga 2 sobre las componentes
m=±2 del condensado — la esperanza concreta de helicidad ±2 física sin diccionario.
Controles disponibles: límite uniaxial (2 angulones de 1307.8183), BEC spin-2 sin lock
(0912.0355).

### Obstáculo nuevo con nombre (declarado antes de enamorarse)
El biaxial deja estabilizador DISCRETO (D₂/D₄) → rompe la isotropía a grupo discreto →
**problema CMB para la versión cosmológica** (las cotas 10⁻⁵ del barco 4). Para el
análogo de laboratorio no importa; para TCI cosmológica hace falta un truco extra
(¿promedio sobre dominios? ¿fase biaxial solo local? ¿restaurar isotropía estadística?).
Anotado como el próximo dragón si el espectro da bien.

## 13. VEREDICTO RUTA (b) + SÍNTESIS FINAL DE LA NOCHE (8º agente)

### Ruta (b) — lo verificado (Visser, Volovik y Dubovsky leídos COMPLETOS por el agente)
1. **Sakharov induce la dinámica pero presupone la variedad**: la inducción a un loop
   genera EH automáticamente ("even if Einstein gravity is not there at zero loops...")
   pero la CINEMÁTICA (que exista métrica/tétrada) se asume. Signo/valor de G dependen
   del espectro y el cutoff; Λ inducida ~κ⁴ ("smallness put in by hand"). W-W se evade
   porque el gravitón no es estado de Fock de la teoría plana + el medio viola Lorentz.
2. **Maitiniyazi-Yamada 2512.08435 (Jilin/Kwansei, dic 2025)**: compuesto tensorial en
   el canal T_μν + flujo RG funcional ⟹ **EH emerge SOLO en el sector TT**; sectores
   traza/longitudinal contaminados con cinética no reproducible por ningún gauge-fixing
   covariante; sin propuesta de solución. Funciona con CUALQUIER materia (escalares u
   fermiones indistinto). No citan Sakharov ni W-W (omisión notable).
3. **Volovik NO deriva la dinámica**: el término de Palatini con rigidez 1/G está
   POSTULADO como término de gradiente del funcional GL ("gravitational stiffness...
   metrical elasticity", cita a Sakharov ahí mismo). Sus gravitones son **modos de
   HIGGS, no Goldstones** (textual, distinguiéndose de Phillips/Chkareuli); la masa
   cero de Jz=±2 viene de **transformaciones residuales de coordenadas** ("3 de los 5
   J=2 se remueven por transformación de coordenadas espaciales; los otros 2 = GW sin
   masa") — **estructuralmente idéntico al mecanismo m₂=0 de Dubovsky, y el puente
   formal Volovik↔Dubovsky NO existe en la literatura** [hueco 1].
4. **Puente medio↔m₂=0 confirmado y afilado**: ghost condensate = realización canónica
   (solo Φ⁰); la fase TT-sin-masa UV-insensible es la de difeos espaciales
   independientes del tiempo (m₂=m₃=m₄=0, requiere m₁²≠0, escalar ω²∝p⁴); "fine-tuning
   m₂²=0 alone is never enough" (textual). Y CCP Tabla 3: **superfluido ⟹ M₂=0, M₁≠0**;
   sólido/supersólido ⟹ M₂≠0.
5. **VEREDICTO SIN VUELTAS (pedido así)**: en la ruta (b), un cuadrupolo ESPACIAL
   (rigidez elástica de largo alcance) es **decorativo en el mejor caso y
   contraproducente en el peor** — la inducción no lo necesita y la fase m₂=0 exige su
   ausencia. El único rol no-decorativo que sobrevive: orden tensorial **INTERNO** tipo
   tétrada-Volovik (L_c×L_s→L_J), cuyo spin-2 es Higgs + simetría residual. [Hueco 2:
   imponer la simetría residual m₂=0 como condición sobre el flujo RG de
   Maitiniyazi-Yamada para matar su contaminación — nadie lo hizo.]

### LA CONVERGENCIA (hipótesis mía, marcada como tal — el hallazgo estructural de la noche)
Las rutas (a) y (b) parecen ser **dos mitades del mismo objeto**: un **SUPERFLUIDO con
orden tensorial J=2 interno lockeado de fábrica (tipo ³P₂)**.
- Sector traslacional: superfluido ⟹ **M₂=0 según CCP** (la fase de Dubovsky, ruta b ✓)
  — sin rigidez elástica espacial, traslaciones intactas (regla del inverse Higgs ✓,
  lección Zaanen ✓: el orden es interno, no elástico).
- Sector orientacional: orden J=2 con lock espontáneo (J=L+S) cuya fase BIAXIAL es la
  candidata a modos gapless lineales con carga 2 bajo rotaciones físicas (ruta a ✓).
- Los modos ±2 serían Higgs-o-Goldstones del orden interno con masa cero protegida por
  la combinación simetría-residual + ruptura espontánea — exactamente el esquema
  Volovik-Dubovsky sin puente, acá con un sistema concreto para construir el puente.
- NADIE estudió el espectro de esa fase biaxial (verificado, agente 7). Todo converge
  al mismo cálculo.

### DECISIÓN: primer cálculo de TCI 2.0 (próxima sesión)
**Espectro completo de la fase biaxial de un superfluido J=2 (formalismo GL de ³P₂ +
EFT de angulones).** Preguntas cerradas: (1) ¿modos gapless lineales? (2) ¿helicidad
espacial ±2 GENUINA (sin diccionario)? (3) ¿qué pasa con traza/vectores (silenciados)?
Controles obligatorios: límite uniaxial = 2 angulones anisótropos (1307.8183); límite
sin lock = 5 modos lineales del BEC spin-2 (0912.0355); y los controles FQ de §11.
Criterios de muerte: modos cuadráticos, o helicidad ±1 otra vez, o gap. Dragón en cola
si sale bien: anisotropía discreta vs CMB (§12).

### Marcador de la noche completa (2026-07-16, ~8 horas, 8 agentes)
- **Muertas con causa citada**: Familia F/SL(3) (NPPR caso 7); lock ingenuo SO(3)×SO(3)
  (coset vectorial, ³P₂ uniaxial como testigo); ruta SU(3)-coherente (±2 en el
  estabilizador, verificado a mano); cuadrupolo espacial en ruta (b) (CCP/solid
  inflation).
- **Erratas propias documentadas**: atribución "Kirby-Rau"; punto SU(3) del BBQ;
  heurística type-A; cita 1010.3231→1009.1398.
- **Vivas y afiladas**: el cálculo biaxial-J=2-lockeado (decisión de arriba); hueco
  Volovik↔Dubovsky; hueco Maitiniyazi-Yamada+simetría residual; mini-Hulse-Taylor de
  vórtices (§9); checkpoint velocidad-carga del paso D (magnetismo de nudos).
- **Nada publicado; todo local; memoria al día.**

## 14. PRIMER CÁLCULO EJECUTADO (misma noche) — el modo ±2 genuino EXISTE; el espectro completo aún no

**Script**: `BORRADOR-NO-PUBLICAR-biaxial_spectrum.py` (numpy puro, en esta carpeta,
excluido de git). Modelo mínimo REAL: B_ij simétrico sin traza (5 comp),
L = χTr(Ḃ²) − c₁Tr(∂B∂B) − c₂(∂_iB_ij)² − V, V = aTrB² + bTrB³ + g(TrB²)² + d(TrB³)²;
el término c₂ es el lock espacial (único que distingue helicidades). Declarado: el
orden real de ³P₂ es COMPLEJO — esto es la versión mínima; 2º orden en tiempo (sin
término de Berry, T-invariante).

### Controles pasados (los tres)
- Uniaxial (b<0): 2 rotaciones rotas = 2 gapless lineales anisótropos, helicidad ±1
  puros a lo largo del eje — cuadro Bedaque-Nicholson ✓.
- Biaxial espontáneo (b=0, d>0 vía (TrB³)²): autovalores EXACTOS (−½,0,½)Δ, 3 rotas =
  3 gapless ✓; Goldstone check |M·v|~10⁻⁷ ✓.
- Punto SO(5) accidental (b=d=0): 3 rotas pero 4 gapless — el extra es el cuasi-NG
  accidental, la MISMA estructura que Uchino-Kobayashi-Ueda reportan para el BEC
  spin-2 real ✓ (control no planeado, pasado).

### EL RESULTADO (primera vez en toda la noche)
**En la fase biaxial existe un modo sin masa, dispersión lineal, con helicidad espacial
±2 GENUINA — contenido TT = 1.00 respecto de la dirección de propagación, sin
diccionario.** El lock espacial (c₂) funciona: las velocidades dependen de la helicidad
física. El objeto que 4 rutas muertas decían imposible, existe en el modelo mínimo.

### Lo que falta (con la misma honestidad)
Por cada dirección principal el espectro gapless es: **1 modo TT + 2 modos vectoriales**
(y en direcciones genéricas, mezclas). La RG necesita **2 TT y 0 extras**:
- La segunda polarización TT (la "+") es el modo de amplitud del biaxial — MASIVO
  (gap = d·(...)). En el punto SO(5) se aplana pero trae un escalar gapless de yapa.
- Los 2 vectoriales gapless sobran (LIGO los acota) — el problema de silenciamiento
  reaparece acá, como se anticipó.
- Velocidad TT anisótropa (~4% entre ejes: 1.0396 vs 1.0819 con estos parámetros) —
  la anisotropía discreta del biaxial, medida. Dragón CMB confirmado en números.

### Próximo paso definido (el cálculo de verdad)
**Versión COMPLEJA (la GL real de ³P₂, 10 componentes reales)**: el parámetro de orden
de ³P₂ es complejo; las fases D₂/D₄-BN viven ahí; los modos de fase relativa entre
componentes son los candidatos naturales a: (i) la segunda polarización TT sin masa,
(ii) gapear/desacoplar los vectoriales. Usar los coeficientes GL de weak-coupling de
la literatura ³P₂ (Yasui-Chatterjee-Nitta 1810.04901 y refs) — no inventar números.
Misma maquinaria numérica; controles: esta versión real como límite + uniaxial de
1307.8183.

## 15. SEGUNDO CÁLCULO (complejo, set de PRUEBA) — LAS DOS POLARIZACIONES APARECEN, y el mecanismo es hermoso

**Script**: `BORRADOR-NO-PUBLICAR-biaxial_complex.py` (10 componentes reales = A compleja
simétrica sin traza; mismos términos de gradiente; cuárticos b₁|TrA²|² + b₂(TrAĀ)² +
b₃Tr(AAĀĀ); SET DE PRUEBA declarado — los coeficientes weak-coupling de ³P₂ están en
camino, 9º agente).

### Resultados (set de prueba)
- Dos semillas distintas → dos mínimos con **V idéntica hasta 16 dígitos** (−0.2778):
  la **degeneración nemática continua a orden cuártico confirmada en nuestro modelo**
  (la familia r que la literatura ³P₂ insinúa). Dirección plana accidental: REAL pura
  (el modo-r), dimensión 1. Total: 5 gapless con solo 4 generadores rotos (3 rot + U(1)).
- **A lo largo del eje especial (el de autovalor 0 del biaxial máximo): DOS modos sin
  masa con helicidad ±2 = 1.00 — LAS DOS POLARIZACIONES DE UNA GW, ambas gapless.**
- **EL MECANISMO (diagnóstico por proyección)**: los dos modos TT son 100% Goldstones
  EXACTOS (proyección sobre direcciones rotas = 1.00; sobre la dirección plana
  accidental = 0.00 — NO dependen de la degeneración accidental, sobreviven al 6º
  orden que la levante):
  1. Polarización **×**: el Goldstone rotacional [L_z, A₀] (el canal xy).
  2. Polarización **+**: **el modo de FASE U(1) del superfluido** — δA = iεA₀ hereda
     la estructura tensorial de A₀, y el biaxial máximo diag(a,−a,0) es EXACTAMENTE
     transverse-traceless respecto de su propio eje z → **el sonido del superfluido,
     vestido con el tensor biaxial, ES la segunda polarización gravitacional.**
     (La fase U(1) que en TCI 1.0 no sabíamos dónde poner, acá es protagonista.)
- Espectro gapless completo en k∥z: 2 TT (v≈1.035/1.039, casi degenerados — el split
  chico viene de la asimetría numérica del mínimo) + 2 vectoriales (v≈1.215) + 1
  escalar (v≈1.268). Velocidades DISTINTAS por sector — posible manija para
  silenciamiento/discriminación.

### Lo que sigue faltando (sin maquillaje)
- En direcciones genéricas los modos se MEZCLAN (contenidos 0.7/0.3): la pureza TT es
  exacta solo sobre el eje especial. La anisotropía sigue siendo EL problema (CMB).
- Los 2 vectoriales + 1 escalar gapless sobran para LIGO (el escalar U(1)… ¡es el que
  se disfrazó de TT en el eje especial! — un solo modo puede ser "+ gravitacional" en
  una dirección y "sonido" en otra: OJO conceptual, esto puede ser bug o feature).
- TODO con set de prueba: pendiente enchufar coeficientes de literatura (9º agente) y
  ver si el 6º orden/campo selecciona el biaxial máximo (el único miembro de la
  familia con el eje TT exacto).

### Idea a verificar contra literatura (posible aporte original)
"**La segunda polarización del gravitón emergente = fonón del superfluido vestido por
el orden tensorial biaxial**" — no recuerdo esto publicado en ningún lado (los papers
de ³P₂ tratan el fonón U(1) y los angulones por separado; Chojnacki no tiene U(1)).
Verificar novedad antes de entusiasmarse.

## 16. TERCER CÁLCULO — funcional GL TEXTUAL de ³P₂ (script `biaxial_3p2.py`): el cuadro completo

Funcional de la literatura (9º agente, 1810.04901 ecs. 17-19): cuártico weak-coupling
β[(trA*A)²−tr(A*²A²)], gradientes K₁=K₂=K₃=K (⟹ c₂=2c₁ — ya no es parámetro libre),
sexto orden textual de 9 términos, regularizador ε(trA*A)⁴ declarado (t constante sobre
la familia nemática → no sesga la selección de r; el 8º orden real quedó sin extraer).

### Resultados
- **CASO A (solo cuártico)**: toda semilla → V=−0.5 exacta (degeneración confirmada,
  incluye estados complejos — "any unitary order parameter", Sauls-Serene 1978 ✓).
  5 gapless; el subespacio degenerado provee 2 TT a lo largo de cualquier eje.
- **CASO B (γ<0 = signo de materia de neutrones, B=0)**: el mínimo cae en **UN
  (uniaxial, r=−1/2 tras gauge)** con **3 gapless (2 angulones + fonón)** —
  **exactamente la física publicada de ³P₂ (Bedaque-Nicholson). CONTROL MAYOR PASADO:
  con el signo real de la naturaleza, nuestra maquinaria reproduce la fase y el conteo
  de la literatura.**
- **CASO C (γ>0, hipotético para el medio TCI, declarado)**: desde cualquier semilla el
  mínimo cae en **D₄-BN exacto (r=−1.000, autovalores (−0.472, 0, +0.472), estado
  puramente real tras gauge)**. El modo-r (cuasi-NG) queda gapeado (m²=0.24 ✓ como
  debía al levantar la degeneración). Quedan **4 gapless exactos = 3 rotacionales + 1
  fase U(1)**. Y sobre el eje especial del condensado:
  **ESPECTRO = TT(v=1.078) + TT(v=1.083) + V(v=1.463) + V(v=1.464)** —
  **dos polarizaciones tensoriales sin masa, casi degeneradas en velocidad, y dos
  vectoriales. Composición verificada por proyección: un TT = 100% modo de fase U(1)
  (el fonón vestido), el otro TT = 100% Goldstone rotacional.** El escalar
  desapareció de la lista (el fonón ES uno de los TT sobre el eje).

### El enunciado central de la noche (borrador de teorema físico)
En un superfluido J=2 con lock espacial y sexto orden γ>0, el estado fundamental
espontáneo es el biaxial máximo D₄, y sobre su eje especial el espectro sin masa es
exactamente {helicidad +2, −2 (una rotacional, una de fase), helicidad ±1 ×2}. **Las
dos polarizaciones de LIGO, de un condensado, con el fonón superfluido como segunda
polarización — con el funcional de la literatura salvo un signo declarado.**

### Deudas exactas (la lista de la próxima batalla)
1. **γ>0 es postulado** (en materia de neutrones es negativo; el medio TCI no es
   materia de neutrones — el signo depende del micro-modelo; DECLARAR SIEMPRE).
2. **2 modos vectoriales gapless** sobre el eje (LIGO los acota) — silenciarlos o
   mostrar que no acoplan a la materia/defectos (la pregunta del acople universal).
3. **Anisotropía**: la pureza TT es exacta solo sobre el eje especial (k⊥ da 1 TT +
   mezclas). Dragón CMB intacto.
4. **8º orden real** de 1904.11399 ec. (40) sin transcribir (PDF pendiente).
5. **Controversia Leinson vs Bedaque-Nicholson** sobre la existencia misma de los
   angulones (1309.5451) — leerla antes de publicar nada.
6. **Verificar novedad** del mecanismo "fonón = segunda polarización" (§15).
7. Los pasos grandes de siempre: acople a defectos (T_μν efectivo, Hulse-Taylor),
   dinámica inducida, monometricidad.

## 17. NOVEDAD DEL MECANISMO + CONTROVERSIA LEINSON (10º agente) — dos buenas noticias

### Novedad: NO ENCONTRADO (confianza moderada-alta) → el mecanismo parece nuestro
14 búsquedas + fuentes primarias: nadie publicó "el fonón U(1) de un condensado
tensorial biaxial hereda la estructura TT de A₀ → helicidad ±2 gapless" ni "fonón +
Goldstone rotacional = par de polarizaciones GW". **Vecinos a citar SIEMPRE**: (1) FQH
chiral gravitons (Nature 628:78 2024) — quiralidad ±2 pero GAPPED, métrica interna;
(2) **Volovik 2111.07817 — sus gravitones son TODOS masivos (Higgs): el fonón gapless
como polarización es exactamente la pieza que a Volovik le falta**; (3) Zaanen-Beekman
dualidad (mecanismo distinto; ojo: cita "spin-2 masless" atribuida NO verificada);
(4) spin-2 BEC: el CONTEO de la fase biaxial ya está publicado (0912.0355, 1010.2864)
— reclamable es solo la lectura tensorial/GW del modo de fase. Deuda: barrido
full-text INSPIRE antes de reclamar nada en público. Caución técnica anotada: en
D₄-BN hay entrelazamiento discreto fase↔rotación (ψ±2 → e∓2iα bajo rotación α) —
nuestra proyección numérica dio separación limpia 1.00/0.00, pero revisar la
estructura del estabilizador al formalizar.

### Leinson: la controversia NO nos toca a T=0 — y nos regala una firma
Comment 1309.5451 leído completo (fuente primaria): **Leinson NO niega los angulones**
— a T=0 reproduce EXACTAMENTE las dispersiones de Bedaque-Nicholson (s=0.4757/0.7096/
0.5198 v_F). La disputa es SOLO a T>0: gap térmico exponencialmente chico (violación
del teorema de Goldstone a T finita en superfluidos anisótropos, precedente Wölfle
³He 1976) vs. masslessness a toda T (Bedaque-Nicholson-Sen 1408.5145: "We do not
understand the origin of this discrepancy" — abierto; Baldo Universe 7:16 (2021) se
inclina por Leinson pero lo declara no cerrado). **Nuestra suposición (SO(3) exacta
rota espontáneamente, gapless a T=0) está avalada por AMBOS bandos.**
**FIRMA POTENCIAL (especulativa, anotada)**: si Leinson tiene razón, a T>0 las dos
polarizaciones se DESDEGENERAN — el fonón sigue gapless (protegido por número de
partículas), el rotacional agarra gap térmico exponencialmente chico → un gravitón
emergente cuyas polarizaciones se separan con la temperatura (universo a T_CMB=2.7K:
¿cota observable? calcular algún día contra m_g<1.27e-23 eV y tests de polarización).
Ojo: Landau damping de modos gapless si el sustrato es fermiónico; si es bosónico
(BEC), no aplica — dato para el micro-modelo de TCI.

## 18. HILO PEDAGÓGICO DEL ÁTOMO (2026-07-17, charla con Nico — material para futuro capítulo; por ahora FUERA de divulgación según su política)

Secuencia que funcionó (Nico llegó solo a la condición de cierre; momento "acabo de
entender algo hermoso"):
1. El electrón es el NUDO, no la onda; el patrón es cómo el nudo se acomoda en el pozo.
   Agitación suave no crea electrones (ondas se dispersan); agitación > 2mc² anuda pares.
2. El núcleo no genera la onda: genera el POZO (la huella). La onda es el vestido del
   nudo, plegado sobre sí mismo por el encierro. Guitarra: pulsás cualquier lío, lo que
   no encaja se cancela/radía (¡luz de acomodamiento! → el CMB como flash cósmico de
   todos los átomos afinándose), queda la nota. Fundamental eterno: sin nota más grave
   + patrón estacionario no radia + topología sostiene el nudo.
3. Analogos mecánicos rankeados: Chladni (flojo: paredes duras + forzado externo) <
   montaña submarina (pozo blando: gradiente de velocidad curva y atrapa — MISMO
   mecanismo que la deflexión §7.4) < anillo de humo (el nudo: forma persistente del
   propio medio, Kelvin) < gota caminante en corral (Harris-Bush 2013: partícula +
   onda propia + jaula = patrones cuantizados — el único análogo completo).
4. La perilla correcta: se cuantiza la LONGITUD DE ONDA (la nota), no la amplitud (el
   volumen). Cierre: nº entero de ondulaciones en la vuelta + nº entero de nodos
   radiales. La velocidad NO es uniforme cerca de la intrusa — el desnivel ES la
   trampa. La energía justa cierra al radio justo (Bohr = la vuelta más chica). El
   volumen lo fija el nudo (uno solo = un traje).
5. Bohr conservado como límite (Rydberg circula como boleadora; medido), superado en el
   sótano (fundamental respira, ℓ=0). Foto real: Stodolna 2013 (microscopio de
   fotoionización). Universalidad de espectros = mismo nudo + mismo pozo = misma nota
   en toda la galaxia. Adiabático: mudanza lenta conserva electrones; brusca excita/
   ioniza (química/plasmas ✓).
Widget hecho en la sesión: atomo_tci_onda_estacionaria (4 notas conmutables).
Experimento propuesto sin dueño (idea anotada §17-bis): "átomo análogo" en condensado
— defecto ligado en la huella de otro con niveles discretos (Kibble-Zurek para crear
pares; nadie lo hizo).

### Cadena de precedentes citables (para cuando esto se escriba en serio)

FQH gravitones quirales medidos (Nature 628:78 2024 + seguimientos 2026) → métrica
interna dinámica es concepto publicado (Haldane) → ³He-B/Volovik: tétrada como parámetro
de orden, gravedad emergente propuesta → nemáticos de spin: análogo GW linealizado con
fuentes topológicas (OIST 2024) → **hueco nuestro: el lock + acople universal + defectos
como materia**.

---

## 19. PRÓXIMOS PASOS (hoja de ruta al cierre de la campaña, 2026-07-17)

### Frente A — el mar grande (gravedad emergente del condensado)
1. **La batalla de los vectoriales** (LA próxima): los 2 modos ±1 gapless del estado
   D₄-BN — ¿acoplan a la materia (defectos) o se desacoplan solos? Calcular el acople
   defecto↔modo por sector. Si acoplan, buscar mecanismo de silenciamiento (¿fase de
   Dubovsky? ¿no-dinámicos como en fluidos?). LIGO/GWTC-3 es el juez.
2. **El dragón de la anisotropía**: pureza TT solo sobre el eje especial; fuera, mezclas
   y velocidad TT ~4% anisótropa. Confrontar con CMB 10⁻⁵. Ideas a explorar: promedio
   sobre dominios, texturas, isotropía estadística, o el patrón combinado tipo ³He-B
   aplicado al eje del D₄.
3. **El 8º orden real**: bajar el PDF de 1904.11399 y transcribir la ec. (40) completa
   (nuestro regularizador ε·t⁴ es provisorio declarado).
4. **Novedad del mecanismo "fonón = segunda polarización"**: barrido full-text
   (INSPIRE/Scholar) en literatura ³P₂ y spin-2 BEC antes de reclamar nada. Formalizar
   con cuidado el entrelazamiento discreto fase↔rotación del estabilizador D₄.
5. **Firma térmica** (especulativa): si Leinson tiene razón, las dos polarizaciones se
   desdegeneran a T>0 (fonón protegido, rotacional con gap exponencial). Algún día:
   calcular contra m_g < 1.27×10⁻²³ eV y tests de polarización.
6. **Los huecos teóricos grandes**: (i) puente formal Volovik↔Dubovsky (Higgs +
   simetría residual ↔ fases m₀…m₄); (ii) imponer la simetría residual m₂=0 al flujo
   RG de Maitiniyazi-Yamada (2512.08435) para matar su contaminación traza/longitudinal.

### Frente B — la materia (nudos) y el examen final
7. **Paso D — taxonomía**: defectos del condensado candidato. El más rico: condensado
   polar spin-1 → vórtice de Alice (carga entera, observado). Para el nuestro (J=2
   biaxial D₄): π₁ del espacio de orden [U(1)×SO(3)]/D₄ — calcular (no-abeliano
   esperable). Checkpoints obligatorios: carga invariante con velocidad (topológica),
   flujo vectorial con signo de quiralidad (magnetismo), identidad exacta.
8. **Mini-Hulse-Taylor**: fórmula analítica de la radiación cuadrupolar de un par de
   vórtices en el condensado (el hueco detectado en el paper OIST — precedente
   numérico publicado, sin teoría). Es el ensayo del examen final.
9. **HULSE-TAYLOR (el examen)**: binaria de defectos → luminosidad → 0.16% de
   PSR B1913+16. En RG la tasa la fija G/c⁵; acá deben fijarla χ, K, β, γ del
   condensado. O da el número o no da.

### Frente C — experimentos y pedagogía (en el cajón hasta OK de Nico)
10. **"Átomo análogo"** en condensado: defecto ligado en la huella de otro con niveles
    discretos (Kibble-Zurek para crear pares). Idea experimental sin dueño.
11. **Hilo pedagógico del átomo** (§18): candidato a capítulo futuro del libro
    ("el mar afinado"). Siguiente escalón: el enlace químico (dos montañas comparten
    una onda). FUERA de divulgación por ahora (política vigente).

### Recordatorios de régimen
- γ>0 es POSTULADO declarado (en materia de neutrones es negativo).
- Nada de esta carpeta se mezcla con el corpus publicado ni se mergea a main.
- Toda idea nueva paga verificación bibliográfica antes de crecer; toda muerte se
  documenta el mismo día; los scripts reproducen lo publicado antes de calcular lo nuevo.

---

## 20. LA TABLA DE NUDOS DEL D₄-BN (11º agente, 2026-07-17) — rica, no-abeliana… y de cuerdas

### Lo confirmado (fuentes primarias: Masuda-Nitta 1602.07050; Masaki-Mizushima-Nitta
2107.02448 + 2301.11614; Kobayashi-Nitta 2209.07205; Mawson-Petersen-Simula 1805.10009)
- Vacío R = [U(1)×SO(3)]/D₄ con el D₄ MEZCLANDO fase y rotación (el elemento (−1, R_π/2):
  rotar π/2 = cambiar fase π — el "entrelazamiento discreto" anticipado en §17 es
  estructural). **π₁ = ℤ×_h D₄\* — NO-ABELIANO** (dihedral binario de 16), π₂ = 0,
  π₃ = ℤ, π₄ = ℤ₂. El π₁ más rico de todo el diagrama de fases nemáticas.
- **7 familias de vórtices**; los fundamentales son **semicuánticos (HQV)**: circulación
  ½ atada a rotación π/2 del marco. El vórtice entero DECAE en molécula de dos HQV
  (separación óptima ≃ 10.7ξ₀); moléculas con "enlaces covalentes" por solitones;
  fusión = doble cuántico D(D₄\*) (45 especies anyónicas por sector); cada HQV lleva un
  **Majorana de energía cero** → anyones no-abelianos POR DOS VÍAS (único sistema
  conocido con esa propiedad, textual 2301.11614).

### Scorecard contra la tabla de partículas (§ pedido del proyecto)
(a) Cargas aditivas: UNA sola (circulación, en medios-enteros) — pobre vs el Modelo
Estándar. (b) Anti-clases: ✓ todas; algunas auto-conjugadas (Majorana-like a nivel
defecto). (c) Aniquilación a vacío: condicional, con canales múltiples y vórtices
"rung" — realista (e⁺e⁻→γγ también deja algo). (d) Familias tipo e/μ/τ: NO hay nada
que parezca 3 generaciones. (e) Estabilidad: **el punto más "física de partículas" de
todos** — jerarquía documentada de decaimientos, estados ligados, moléculas y enlaces,
con los HQV como objetos absolutamente estables del fondo.

### EL PROBLEMA ESTRUCTURAL (sin suavizar, textual del agente)
**Los vórtices son defectos de LÍNEA — cuerdas, no partículas puntuales en 3D.**
Para puntos hace falta π₂ (monopolos) = 0 exacto sin apelación, o π₃ (skyrmions) = ℤ
— que EXISTE y daría una segunda carga entera aditiva (¡tipo número bariónico!) pero
sin estabilización calculada en esta fase (Derrick los encoge; nadie lo estudió).

### El giro: KELVIN VUELVE (dirección nueva, la más vieja de todas)
Si los nudos fundamentales son cuerdas, las partículas puntuales serían **anillos
cerrados de cuerda HQV** — vistos de lejos: puntos; por dentro: lazos, posiblemente
anudados/retorcidos (Hopfions ↔ π₃=ℤ). **Eso es literalmente el átomo-vórtice de
Kelvin (1867) — anillos — con topología no-abeliana moderna.** Precedente experimental:
solitones-nudo observados en BEC espinoriales (Hall et al. 2016, a verificar la cita).
Pregunta afilada nueva (paso D actualizado): ¿los anillos de HQV en D₄-BN tienen
tamaño/energía estables (algo que frene a Derrick: circulación atrapada, twist,
término tipo Skyrme de derivadas altas)? Territorio verificado como virgen: nadie
propuso la taxonomía D₄-BN como modelo de materia (los papers son astrofísica de
magnetares + computación cuántica topológica).

## 21. LA BATALLA DE LOS ANILLOS (2026-07-17) — Derrick pierde de dos maneras distintas

*(Nota de proceso: el 12º agente murió por límite de créditos; la verificación la hice
a mano con búsqueda web directa — menos profunda que un agente, deudas señaladas.)*

### El juguete (`anillos_toy.py`, en esta carpeta)
E(R;k) = αR(ln(R/ξ)+c) + βk²/R — tensión de cuerda vs twist atrapado (mecanismo vortón).
- Control k=0: colapso (Derrick gana sin twist) ✓.
- k≥1: **mínimo a radio finito** — anillo con tamaño y masa definidos. R₁≈0.76ξ, E₁≈1.87
  (unidades α=β=ξ=1; solo la FORMA es significativa).
- Torre E_k con exponente efectivo ~1.25 (superlineal por el log) ⟹ **E₂ > 2E₁: los k
  altos FISIONAN — el único anillo absolutamente estable es k=±1**. El mar tacaño:
  una especie estable y su espejo, todo lo demás decae hacia ellas (¿"leptón-like"?).

### La literatura (verificada a mano)
1. **Vortones: estabilidad clásica CONFIRMADA** — estudio detallado JHEP 2022
   (arXiv:2112.08066) + simulaciones lattice: lazos de cuerda superconductora se
   relajan a vortones estables **radiando Goldstones** (el anillo "encuentra su nota"
   emitiendo — la misma física del electrón cayendo al pozo). Caveat cuántico:
   disipación de corriente por efectos cuánticos (2209.03223) — vida larga, no eterna,
   según el modelo.
2. **Hopfions (π₃, mecanismo Skyrme-Faddeev): E ∝ Q^(3/4)** (cota Vakulenko-Kapitansky
   + numérica Battye-Sutcliffe hasta Q=8, con tréboles). **SUBLINEAL ⟹ los Q altos se
   LIGAN** (E(Q=2) < 2E(Q=1)): química opuesta al vortón — torres de compuestos
   estables ("nuclear-like"). Bonus notable: existen Hopfions del modelo
   Skyrme-Faddeev-Niemi sobre la VARIEDAD BANDERA F₂ = SU(3)/T² (arXiv:1805.10008) —
   la bandera de §11 reaparece por el lado de los nudos.
3. **Laboratorio real**: nudos cuánticos CREADOS en BEC espinorial (Hall-Möttönen,
   Nature Physics 2016); su decaimiento medido (PRL 123, 163003 (2019)): el nudo decae
   PERO en un **vórtice de spin polar-core ESTABLE con vida comparable al condensado
   entero**. Teoría: los nudos son inmunes energéticamente al encogimiento (conservación
   de energía) pero vulnerables a corrientes de spin; vida ∝ R². Y existe literatura de
   **anillos de Alice** (lazos cerrados de cuerda HQV — nuestro objeto exacto en el
   primo polar): PRR 5, 023104 (2023), evolución y decaimiento estudiados.
4. **Anillo en reposo**: problema abierto señalado — el anillo de vórtice común viaja a
   velocidad autoinducida (∝ ln R/R); un "anillo-partícula en reposo" necesita
   contraflujo, twist que cancele la autoinducción, o interpretarse con momento
   intrínseco (¿inercia gratis? ojo, puede ser bug o feature). Sin verificar a fondo.
5. **D₄-BN específico**: anillos de HQV en D₄-BN/³P₂ — no encontrado (esperado; sigue
   virgen).

### Síntesis del frente B tras la batalla
La conjetura de Kelvin sobrevive su primera prueba **con estructura**: hay DOS
mecanismos de estabilización con químicas opuestas — twist/vortón (superlineal →
una sola especie estable ± espejo) y Skyrme/Hopfion (sublineal → compuestos ligados
en torre). Un mar con ambos términos tendría ambas químicas (¿leptones y núcleos?).
En el primo de laboratorio los nudos existen, decaen a defectos estables, y los
anillos de Alice ya tienen literatura propia. Deudas: ~~el anillo en reposo~~, los
Majoranas en lazo cerrado, twist D₄ (¿ℤ o ℤ₄?), y TODO el capítulo cuantitativo en
nuestro condensado específico.

**ACTUALIZACIÓN (misma jornada): EL ANILLO EN REPOSO — RESUELTO A NIVEL LITERATURA.**
En BECs de DOS componentes existen anillos de vórtice **estables en reposo** (a
diferencia de ⁴He donde solo viven en movimiento): la segunda componente condensada
EN EL NÚCLEO de la cuerda lleva corriente a lo largo del anillo y contrarresta la
tensión — el paper los llama textualmente "vortons" (cond-mat/0307559, "Vortex Rings
in two Component Bose-Einstein Condensates"). **Convergencia con §20**: los núcleos de
nuestros HQV en D₄-BN ya llevan orden ferromagnético/cíclico (Kobayashi-Nitta
2209.07205) = la segunda componente en el núcleo YA ESTÁ en nuestro sistema. El
anillo-partícula quieto tiene todos sus ingredientes con precedente publicado; falta
el cálculo específico D₄ (virgen).

## 22. EL MAPA DE LA ANISOTROPÍA (2026-07-17, `anisotropia_mapa.py`) — el dragón tiene anatomía

Barrido de 400 direcciones (esfera de Fibonacci) sobre el estado D₄ del caso C
(parámetros de juguete — los PORCENTAJES son ilustrativos, la ESTRUCTURA es de simetría
y robusta):

- **SORPRESA A FAVOR: hay un modo casi-puro TT en TODO el cielo** — pureza media 0.951,
  mínimo 0.702; el 82% del cielo tiene TT≥0.9 y el 100% tiene TT≥0.7. Una polarización
  gravitacional robusta en toda dirección — no lo esperábamos (creíamos que la pureza
  vivía solo sobre el eje).
- **La segunda polarización es la anisótropa**: pureza 0.97 cerca del eje especial
  (0-15°), degradándose monótonamente a 0.20 en el ecuador (75-90°). Es el fonón: su
  carácter TT depende de la dirección (la estructura tensorial de A₀ es TT solo
  respecto de su propio eje). En el ecuador solo hay UNA polarización limpia.
- **Velocidad del sector TT: anisotropía del 12.6%** (con estos parámetros) — el
  número que el CMB/GW no perdonaría tal cual. Este es el corazón cuantificado del
  dragón.

Lectura: el dragón no es un muro uniforme — es un problema CON estructura: (1) una
polarización sana en todo el cielo (mejor de lo temido); (2) la segunda necesita un
mecanismo (¿promedio sobre dominios? ¿otra fase? ¿la dirección faltante la aporta otro
sector?); (3) la anisotropía de velocidad es la deuda dura — candidatos a domarla:
promedios de dominio/textura, isotropía estadística, o el argumento de monometricidad
(si TODO comparte el medio, la anisotropía es común y solo los observables relativos
cuentan — el examen de Carlip otra vez). Próximo: cuantificar qué observable acota qué
(GW170817 constriñe velocidad GW vs LUZ — si la luz viaja por el mismo medio con la
misma anisotropía, el test relativo puede pasar; calcular).

## 23. TEST DE MONOMETRICIDAD INGENUA (`monometricidad_test.py`) — FALSADA (5ª lápida)

Identificación ingenua declarada: "luz" = modos gapless de helicidad ±1 del mismo
condensado; "GW" = mejor modo TT. Test sobre 400 direcciones:

- **v_GW/v_luz medio = 0.774 ≠ 1** → GW170817 (que exige 1 a 15 decimales) la mata
  instantáneamente: sectores de Goldstone distintos tienen velocidades distintas de
  fábrica (1.10 vs 1.42; cocientes de rigideces diferentes).
- **Peor: las anisotropías NO se cancelan en el cociente — se COMPONEN**: anisotropía
  del cociente 26.9% > la de cada sector por separado (12.6% / 13.0%). Los perfiles
  angulares de los dos sectores son distintos (hasta anti-correlacionados).

**VEREDICTO (sin maquillaje): la esperanza "todo es Goldstone del mismo mar ⟹ misma
métrica efectiva" es FALSA.** La monometricidad NO puede venir de sectores de
Goldstone independientes del bulk. Muere la versión ingenua de la salida al dragón
de velocidad (§22) y de la objeción de Carlip.

**La consecuencia constructiva (por qué esta muerte vale oro):**
1. **La luz NO puede ser un Goldstone del bulk.** El sector EM debe emerger de OTRO
   lado — y la única ruta con precedente es la de Volovik en ³He-A: fermiones y campos
   de gauge efectivos emergiendo JUNTOS del mismo punto nodal del espectro, compartiendo
   UNA métrica efectiva por construcción (no por coincidencia de rigideces). Traducido
   a TCI 2.0: **la luz y la materia deben vivir en el sector de los DEFECTOS** (modos
   ligados a los cores — donde ya viven los Majoranas y las corrientes FM/cíclicas de
   los vortones §21-bis: TODO sigue convergiendo a los núcleos de los nudos), no en
   los Goldstones del mar liso.
2. **Silver lining para "sobran 2 vectoriales" (§16)**: si los modos ±1 NO son la luz,
   quizás tampoco acoplan a los detectores/materia — serían modos "oscuros" del bulk.
   Su peligro observacional pasa a depender enteramente del cálculo de acople a
   defectos (pendiente §19.1), no es automático.
3. El programa queda re-afilado: el examen de Carlip no se aprueba con Goldstones —
   se aprueba (si se aprueba) con la estructura nodal común del sector de defectos.
   Ese es ahora el nombre técnico del problema de monometricidad en TCI 2.0.

## 24. LA BATALLA NODAL (2026-07-17) — dónde vive la luz: la arquitectura de dos fases

Fuente primaria leída (vía ar5iv): **Mizushima-Masuda-Nitta, "³P₂ Superfluids Are
Topological" (PRB 95, 140503, arXiv:1607.07266)**.

### Fe de erratas propia #6
Mi sospecha "el D₄-BN tiene nodos puntuales sobre el eje especial" era FALSA: **las
fases nemáticas (UN, D₂, D₄) son completamente gapeadas en el bulk** — clase DIII
(TRS 𝒯²=−1), winding 3D w=1. Verificado textual antes de construir sobre la sospecha
(el método funcionando).

### Lo que el paper da (textual)
- Nemáticas (nuestro D₄): bulk gapeado, pero **fermiones de Majorana SIN MASA en las
  superficies, con dispersión relativista** E=±√(c_x²k_x²+c_y²k_y²) (su ec. 6, con
  estructura de ecuación de Dirac 2D: ℋ_surf = ψ̄(−iv̄^μγ_μ∂_μ)ψ). En clase DIII los
  defectos (vórtices) también ligan Majoranas (consistente con §20).
- **Fase CÍCLICA: 8 puntos de Weyl en configuración tetraédrica** (cargas de monopolo
  ±1), y el hamiltoniano efectivo cerca de cada nodo es LITERALMENTE el de Volovik:
  **ℋ = ê^μ_a τ^a(k_μ − qk_{α,μ}) — una TÉTRADA emergente** (su ec. 8). El paquete
  completo de la ruta Volovik (fermiones de Weyl + tétrada) EXISTE en la familia ³P₂
  — pero en la fase cíclica, no en la nemática.

### LA ARQUITECTURA DE DOS FASES (hipótesis de síntesis, mía, marcada)
Juntando §16 + §20 + §21-bis + §23 + esto:
- **El bulk D₄-BN** pone la GRAVEDAD: las dos polarizaciones TT sin masa (rotación +
  fonón vestido), bulk fermiónico gapeado (sin especies de luz compitiendo en el mar
  liso — consistente con §23: la luz NO debe ser del bulk).
- **Los CORES de los nudos llevan orden FM o CÍCLICO** (Kobayashi-Nitta 2209.07205,
  ya en §20) — y la fase cíclica es la que tiene los 8 Weyl y la tétrada. **Hipótesis:
  la luz y la materia relativista viven en los tubos/anillos de fase cíclica que
  forman los cores de los nudos** — el barrio nodal está DENTRO de los defectos,
  exactamente donde §23 exigía que estuviera. Recordar además (agente 9): la cíclica
  está CERCA en energía de las nemáticas en weak coupling ("nearly degenerate...
  may be replaced by cyclic with strong coupling") — las dos fases de la arquitectura
  son vecinas de energía, no extrañas.
- Cuadro completo TCI 2.0 v3: *mar liso D₄ = gravedad; nudos con corazón cíclico =
  materia + luz + (si Carlip aprueba) la métrica común de la tétrada.* Todo lo que
  falló por separado encuentra lugar: los Goldstones del bulk no son la luz (✓ §23),
  los Majoranas de superficie/defecto son relativistas de fábrica (✓ DIII), y la
  tétrada de Volovik tiene dirección concreta donde buscarse (✓ ec. 8 de 1607.07266).

### Deudas de esta batalla (grandes, declaradas)
1. ¿Los 8 Weyl de la cíclica sobreviven cuando la cíclica vive solo en un TUBO
   (core de vórtice) y no en bulk? (Confinamiento discretiza; puede matar o
   preservar la estructura nodal — cálculo BdG en el core, no hecho que yo sepa.)
2. ¿La tétrada emergente de los nodos coincide con la métrica efectiva que ven los
   modos TT del bulk? (ESTA es ahora la forma técnica exacta del examen de Carlip.)
3. Acople: ¿los modos TT del bulk se acoplan a los Majoranas/Weyl de los cores con
   la forma del T_μν? (El camino a Hulse-Taylor pasa por acá.)

## 25. LA BATALLA DEL TUBO (2026-07-17) — el Weyl 3D no sobrevive; lo que sobrevive es mejor para otra cosa

### Lo verificado (literatura estándar de estados de core)
- Un core de vórtice hospeda estados discretos **Caroli-de Gennes-Matricon (CdGM)**:
  escalera de niveles con "minigap" δε ≈ Δ²/E_F, etiquetados por (p_z a lo largo del
  tubo, n angular) — 1D branches dispersivas a lo largo del tubo, más la rama de
  **Majorana** protegida en los casos topológicos (coexisten; separarlos
  experimentalmente es difícil justamente porque el minigap es chico).
- **Veredicto del tubo**: la estructura Weyl 3D + tétrada del bulk cíclico NO
  sobrevive tal cual en un tubo delgado (~ξ): el confinamiento transversal la
  discretiza. Lo que sobrevive es un MUNDO 1D: la escalera CdGM + la rama Majorana.

### El regalo: el anillo tiene NIVELES INTERNOS (candidato a "familias")
Para un anillo cerrado de circunferencia 2πR, el momento a lo largo del tubo se
cuantiza (p_n = (n+ν)/R, con ν=0 ó ½ según la fase de Berry del winding — la deuda
"Majoranas en lazo cerrado" se vuelve una pregunta de condiciones de contorno,
periódicas vs antiperiódicas). Espectro interno del anillo-partícula, dos torres:
**E(n,m) ≈ m·(Δ²/E_F) + ħv_∥(n+ν)/R** — una partícula topológica con ESTADOS
EXCITADOS INTERNOS discretos. **Consecuencia conceptual mayor**: el requisito (d) del
scorecard §20 (familias tipo e/μ/τ — antes: CERO candidatos) ahora tiene un mecanismo
candidato: *misma carga topológica, distinto estado interno de los fermiones del
core = misma partícula, más pesada*. Electrón/muón/tau como el mismo anillo en
distintos niveles de su escalera interna — ESPECULATIVO AL CUBO, declarado, pero es
la primera vez que el hueco de las generaciones tiene una forma posible.

### La bifurcación honesta que queda (dos arquitecturas candidatas)
- **Arquitectura A (la de §24)**: bulk D₄ = gravedad; cores cíclicos = materia.
  Pendiente duro: la LUZ 3D no puede vivir en tubos 1D — necesitaría emerger a nivel
  colectivo/red de defectos (no construido) o la arquitectura falla para el fotón.
- **Arquitectura B (nueva, a explorar)**: bulk CÍCLICO (los 8 Weyl + tétrada de
  Volovik en 3D pleno = luz y materia relativistas de fábrica) y la pregunta
  invertida: ¿qué dan los Goldstones de la cíclica ([U(1)×SO(3)]/T, 4 rotos) como
  gravedad? Su historia GW está SIN explorar — nadie la miró con los ojos de §16.
  Nota: la cíclica es vecina de energía de las nemáticas (agente 9) — el diagrama de
  fases entero de ³P₂ podría ser el "multiverso" de arquitecturas de TCI 2.0.

## 26. EL EXAMEN DE LA CÍCLICA (`espectro_ciclico.py`) — dos arquitecturas, dos perfiles complementarios

### Resultados (selector b1|TrA²|² > 0 declarado como rol del strong coupling)
- Convergencia perfecta desde dos semillas: |autovalores| = (½,½,½) exactos,
  |TrA²| ~ 10⁻¹², V idéntica. Masas no nulas (1,1,1,4) — la simetría tetraédrica
  cantando (triplete degenerado + singlete). 4 rotos = 4 gapless ✓.
- **Gravedad de la cíclica (vía Goldstones): MEDIOCRE.** Sin eje especial limpio:
  1 modo TT decente en la mayoría de las direcciones (pureza media 0.909 < 0.951 del
  D₄; mínimo 0.76), el 2º modo pobre (0.485), direcciones (110) todas mezcladas.
  Anisotropía de velocidad 9.7% (vs 12.6% del D₄ — apenas mejor, mismo orden).
  CAVEAT declarado: la cíclica rompe T → posible término de Berry de 1er orden que
  esta maquinaria (2º orden) no captura; primera pasada.

### La lectura correcta (síntesis)
El examen NO dice "la cíclica es peor" — dice que **en la Arquitectura B la gravedad
no debe venir de los Goldstones**: en el programa de Volovik la gravedad es la
dinámica de la TÉTRADA (inducida por loops fermiónicos, Sakharov-style — con su
deuda conocida de §13: Volovik la postula), no los modos del parámetro de orden.
Nuestro test confirma que los Goldstones bosónicos de la cíclica no compiten — y
además son 4 modos gapless extra que B tendría que silenciar.

**Los perfiles finales de las dos arquitecturas (complementarios en espejo):**
| | Arquitectura A (bulk D₄) | Arquitectura B (bulk cíclico) |
|---|---|---|
| Gravedad | ✓✓ calculada (2 TT en eje; §16) | vía tétrada inducida (heredada de Volovik, dinámica sin derivar) |
| Materia | anillos con niveles internos (§21-25) | fermiones de Weyl de fábrica ✓✓ |
| Luz | ✗ problema 1D (§25) | ✓✓ estructura de gauge emergente en nodos |
| Modos sobrantes | 2 vectoriales (¿oscuros? §23) | 4 Goldstones bosónicos + dinámica por derivar |
| Anisotropía v_TT | 12.6% | 9.7% (Goldstones) |

Ninguna completa; cada una fuerte donde la otra flaquea. Preguntas que esto abre
(anotadas, sin resolver): ¿interfaz/mezcla de fases? ¿el medio TCI real como fase
propia con ambos caracteres? ¿o A con la luz emergiendo del nivel colectivo de la
RED de nudos (el hueco que nadie construyó)? El diagrama de fases ³P₂ como espacio
de búsqueda de TCI 2.0 quedó cartografiado de punta a punta con una sola maquinaria.

## 27. LA LUZ DE LA RED DE NUDOS (2026-07-17) — el precedente existe y se llama string-net

### El mecanismo (Levin-Wen, verificado)
**String-net condensation** (Levin-Wen, cond-mat/0404617 + "Photons and electrons as
emergent phenomena" cond-mat/0407140; y Wen, "QUANTUM ETHER: photons and electrons
from a rotor model", hep-th/0507118 — el título es literal): cuando una red de cuerdas
cuánticas condensa (las cuerdas proliferan y fluctúan como líquido), sus excitaciones
colectivas son **bosones de gauge (fotones = vibraciones de la red)** y **fermiones
(= extremos de cuerda, siempre con carga de gauge)**. En 3D unifica luz y materia de
un solo mecanismo. Es el marco publicado exacto para "la luz emerge de la red de
nudos" que la Arquitectura A necesitaba (§25).

### El encastre estructural con nuestra §20 (el hallazgo)
- Los modelos de Levin-Wen toman como input una **categoría de fusión** (tipos de
  cuerda + reglas de ramificación). ¿Y qué nos dio la taxonomía del D₄-BN? El **doble
  cuántico D(D₄\*)** con sus 45 especies y reglas de fusión (Mawson et al., §20) — 
  exactamente la clase de estructura algebraica que un string-net realiza.
- Nuestra red NO es de lazos sueltos: es una **red ramificada** — los vórtices
  no-abelianos que se cruzan quedan unidos por "rungs" (§20, textual) → red con
  nodos trivalentes = un string-NET genuino, no un gas de anillos.
- Los extremos/uniones de cuerda de Levin-Wen portan las cargas fermiónicas — y
  nuestras cuerdas ya llevan Majoranas (§20). π₂=0 dice que nuestras cuerdas no
  pueden TERMINAR en el vacío (sin monopolos) — pero sí pueden ramificarse (rungs):
  la carga fermiónica viviría en las UNIONES, no en puntas sueltas.
- La parte ℤ×_h del π₁ (windings semienteros de fase) es el candidato natural al
  sector U(1) del fotón.

### La tensión honesta (el problema afilado que queda)
La condensación de string-nets requiere que las cuerdas PROLIFEREN (tensión efectiva
→ 0, líquido cuántico de cuerdas); pero la gravedad de A necesita el ORDEN D₄ intacto
(los TT de §16). Proliferación de defectos normalmente DESTRUYE el orden. La salida a
investigar: coexistencia de orden topológico y orden roto (concepto conocido — p.ej.
superconductores tienen ambos), o condensación PARCIAL (solo algunos tipos de cuerda
del D(D₄\*) condensan, preservando el orden que sostiene la gravedad). **Pregunta
afilada nueva: ¿qué subconjunto de las 45 especies puede condensar sin matar el D₄?**
(Las "anyon condensation transitions" de la literatura de fases topológicas son la
herramienta hecha para esta pregunta.)

### Lo no-hecho (verificado como hueco)
Nadie construyó una condensación string-net de la red de vórtices HQV de un
superfluido tensorial — Levin-Wen vive en modelos de spin en red; el puente al
continuo superfluido está sin construir. Virgen, grande, con las dos puntas
(nuestra taxonomía + su mecanismo) ya publicadas por separado.

## 28. ANATOMÍA DEL EXAMEN HULSE-TAYLOR (2026-07-17, `scaling_cuadrupolo.py`) — la forma está aprobada; el examen real es el coeficiente y el dipolo

### Mitad 1 — LA FORMA: verificada numéricamente (aprobada)
Binaria de cargas acopladas a un canal sin masa de dispersión lineal, potencia
radiada integrada sin expansión multipolar (armónicos pares, 200 direcciones):
**P ∝ Ω^6.000 · d^4.000 · v^−5.000** — los tres exponentes de la fórmula del
cuadrupolo de Einstein, exactos. (Errata propia #7: mi primer conteo del flujo
far-field tenía v³ por v¹ en el denominador — el propio fit numérico me delató,
corregido y documentado en el script.)
**Conclusión estructural: la forma de Einstein es UNIVERSAL para cualquier canal
sin masa lineal — Hulse-Taylor (0.16%) no testea la forma; testea el COEFICIENTE.**
TCI 2.0 pasa la mitad estructural automáticamente por tener el canal TT sin masa.

### Mitad 2 — EL COEFICIENTE: el examen real, desarmado en tres piezas
1. **Universalidad del acople (G_rad = G_static)**: en RG la binaria radia con la
   MISMA G que gobierna la estática (una sola métrica). TCI 1.0 ya fijó G_static
   desde el sector escalar (G = Kμ⁴/4πρ₀², derivación de Newton). El examen exige
   que la carga del defecto bajo el canal TT reproduzca exactamente esa G — el
   principio de equivalencia en versión radiativa. CÁLCULO CONCRETO PENDIENTE: la
   carga de un defecto/anillo en movimiento bajo cada canal de Goldstone, desde la
   energía GL de la textura móvil (dinámica Magnus/Kelvin de vórtices).
2. **El factor tensorial (32/5)**: el coeficiente numérico exacto incluye la suma
   sobre las 2 polarizaciones TT con su estructura angular — distinto del canal
   escalar. El 0.16% de Weisberg-Huang testea ese factor completo.
3. **EL PELIGRO DIPOLAR (la pieza que afila todo)**: cualquier canal gapless EXTRA
   (nuestros 2 vectoriales; escalares) al que los defectos acoplen con momento
   dipolar no nulo radia a orden MÁS BAJO: P_dip ∝ Ω⁴d²/v³ — DOMINA sobre el
   cuadrupolo a baja frecuencia y arruinaría el 0.16%. Así mueren las teorías
   escalar-tensor en los púlsares: las binarias ASIMÉTRICAS (púlsar + enana blanca,
   p.ej. PSR J1738+0333) son el verdugo del dipolo, porque cargas desiguales no
   cancelan el momento dipolar. **La batalla del silenciamiento de los vectoriales
   (§19.1) queda ahora cuantitativamente motivada: o los defectos no acoplan a los
   vectoriales (modos oscuros, §23), o acoplan con carga proporcional a la masa
   (dipolo cancelado por equivalencia), o TCI 2.0 muere por dipolo en J1738+0333.**
   Tres salidas, todas calculables desde el acople defecto-canal.

### El estado del examen final tras esta sección
- Forma del cuadrupolo: ✓ APROBADA (automática + verificada).
- Coeficiente: pendiente del cálculo de cargas del defecto (el próximo gran cálculo
  del programa, común a ambas arquitecturas).
- Dipolo: el peligro está identificado con púlsar asignado y tres salidas nombradas.
El examen dejó de ser una consigna ("dar el 0.16%") y pasó a ser una lista de
tareas concreta. Nico preguntó al principio de todo si la disipación orbital de las
sims era pista o bug: era pista — y ahora tiene teoría de examen completa.

## 29. LA BATALLA DEL ACOPLE (abierta 2026-07-17) — una cuenta, tres tronos

**Elección de rumbo** (pregunta de Nico "¿seguimos con EM u otra cosa?"): la cuenta
que decide TODO a la vez es **el acople del nudo a los canales** — con qué carga un
defecto en movimiento habla con cada onda del mar (TT ×2, vectoriales ×2, fonón).
De ahí salen: (1) el coeficiente de Hulse-Taylor (G_rad vs G_static — §28.2), (2) el
veredicto dipolar (§28.3, púlsar J1738+0333), (3) si los vectoriales son oscuros
(§23), y (4) la teoría de interacciones entre nudos = el EM en construcción (la
respuesta a la pregunta del papá de Nico sobre masa/carga salió entera de estas
piezas — "la carga cuenta, la masa cobra" — y va a ser sección de la página).

**La caja de herramientas encontrada (reconocimiento a mano):**
- **Teoría efectiva de cuerdas de vórtice** generalizando Lund-Regge: Horn-Nicolis-
  Penco arXiv:1507.05635 ("Effective string theory for vortex lines in fluids and
  superfluids") — worldsheet + acople a modos del bulk, Kelvin waves, anillos. LA
  plantilla.
- **Vórtice-fonón resuelto en superfluidos U(1)**: emisión de sonido por vórtices en
  movimiento como único canal disipativo a T=0, con tasas y reacción de radiación
  (Kozik-Svistunov cond-mat/0505020; cond-mat/9409046; 1408.5913). **CONTROL DE
  CALIDAD OBLIGATORIO**: nuestro cálculo debe reproducir estas tasas en el límite
  U(1) antes de creerle los canales nuevos.
- Extensión a supersólidos ya existe (2409.04865) — precedente de vórtices acoplados
  a medios con más estructura.

**Plan de la cuenta (sesión fresca):**
1. Worldsheet del HQV en el mar D₄ (colectivas: posición + fase + orientación).
2. Acoples por canal DERIVADOS del funcional GL (K, β, γ — no inventados): el
   winding de fase → carga fonónica (control U(1)); el winding de marco → carga
   bajo los canales de orientación (TT y vectoriales).
3. Radiación de binaria por canal con la maquinaria §28 → G_rad, coeficiente
   dipolar vectorial.
4. Confrontar: G_rad vs G_static (equivalencia radiativa), dipolo vs púlsares
   asimétricos, y el mini-Hulse-Taylor numérico del paper OIST como control
   cualitativo (§9).
Criterios de muerte: G_rad ≠ G_static sin salida → se declara; dipolo vectorial no
nulo con acople no suprimido → TCI 2.0 muere en J1738+0333 y se publica.

### Consecuencia para "el libro de las partículas" (pregunta de Nico 2026-07-17)
Veredicto sostenido: TODAVÍA NO. La tabla es rica (no-abeliana, con decaimientos,
moléculas y antipartículas) pero da cuerdas donde necesitamos puntos, una sola carga
aditiva, y cero generaciones. La piedra angular pasa a ser: **estabilidad y espectro
de los anillos/skyrmions** — si los anillos se estabilizan con un espectro discreto
de masas, el cuadro "partícula = anillo anudado" revive a Kelvin con andamiaje real y
el libro tiene columna vertebral; si Derrick gana, se documenta y la conjetura de
nudos muere con honores. Anotado como próximo cálculo del Frente B.

## 30. EL COULOMB DEL MAR (2026-07-18) — la parte estática de la batalla del acople:
## dos electricidades exactas

**Elección de rumbo**: Nico propuso entrar por el EM ("la puerta más accesible para
el público") y el mapa técnico coincide — la §29 ya había identificado que la teoría
de interacciones entre nudos ES el EM en construcción. Hoy: la mitad ESTÁTICA de la
batalla del acople. Pregunta concreta: **¿qué ley de fuerza da el mar D₄-BN entre dos
nudos (HQV)?** El "mismo giro repele, opuesto atrae" de la página del taller, pero
calculado desde el funcional GL textual, no dibujado. Script: `coulomb_del_mar.py`
(controles internos: vacío D₄ reconfirmado a=0.47211 desde 1D y desde el mínimo
10-dim; autotest de la vectorización del potencial contra la versión escalar de
`espectro_biaxial_3p2.py`, error 10⁻¹⁵).

### A) Límite de London: el teorema de las dos monedas (exacto, y mejor de lo esperado)

Textura A(x) = e^{iφ(x)} R(α(x)) A₀ Rᵀ(α(x)) con A₀ = a·diag(1,−1,0) (eje especial z,
vórtices de línea a lo largo de z, gradientes en el plano xy). Resultado numérico
exacto del funcional textual (con y sin el término de divergencia K₂+K₃, en las
direcciones x, y y 45°):

- **Cero término cruzado fase↔marco** (k_φα = 0 en toda dirección y en ambas formas
  del gradiente).
- **Tipo de cambio exacto 4:1**: ρ_marco/ρ_fase = 4.0000. Mecanismo: el cuadrupolo
  acopla la rotación con carga 2 (ψ∓₂ ~ e^{i(φ±2α)}) — un cuarto de vuelta del marco
  vale lo mismo que media vuelta de fase.
- **Isotropía en el plano** incluso con el término de divergencia (x = y = 45°): el
  Coulomb estático del D₄ no ve la anisotropía discreta (esa vive en los modos
  propagantes, §22).
- Consecuencia (cambio de base χ± = φ ± 2α): **el mar D₄ es, para la estática de sus
  nudos, DOS superfluidos U(1) independientes con la misma rigidez** (k₊₊ = k₋₋ =
  Ka², k₊₋ = 0 exacto — la igualdad de rigideces es la simetría ψ₊₂↔ψ₋₂ del vacío).
  Dos electricidades que no se mezclan.

**Tabla de cargas de las 4 especies fundamentales** (w_fase, w_marco) → (q₊, q₋):
(½,¼)→(1,0); (½,−¼)→(0,1); (−½,¼)→(0,−1); (−½,−¼)→(−1,0). La interacción por par:
E_int/L = 2π·2Ka²·(q₊¹q₊² + q₋¹q₋²)·ln(R/d). O sea: **la mitad de los pares tiene
Coulomb logarítmico puro (coef ±4πKa² = ±2.80 con nuestros parámetros) y la otra
mitad es neutra a orden logarítmico** (con residuo de potencia ~1/R³ incluso en
London — ver E.1). "Mismo giro repele, opuesto atrae" —
confirmado y afinado: vale POR SECTOR, con fuerza F/L ∝ 1/d (el Coulomb genuino de
2D entre cuerdas).

- El HQV es literalmente un vórtice en UNA sola componente (ψ₊₂ o ψ₋₂) — la
  estructura conocida de los spinor BECs, acá emergiendo del funcional ³P₂.
- El vórtice entero (1,0) = un nudo de cada sector superpuestos: **la "molécula" de
  la taxonomía §20 es un compuesto NEUTRO bajo las dos electricidades** — el análogo
  del átomo. Su fuerza residual (tipo van der Waals del mar) debe venir de más allá
  de London: eso mide la Parte C.

### B) Confrontación no lineal (relajación GL 2D, campo completo de 10 componentes)

Protocolo: potencial caso C textual, gradiente isótropo K₁ solo (DECLARADO: el
término de divergencia no cambia la estructura de sectores — verificado en A — pero
sí valores; núcleos anclados en discos r≤2.5, borde congelado al ansatz, E(d) para
d = 12, 18, 26 en red 120², pendiente dE/d ln d contra la predicción London ±2.80 /
0 / 0 / ∓2.80.

**RESULTADOS (red 120², d = 12/18/26, corte por convergencia; London predice
∓2.80 para cargados y 0 para neutros):**

| par                  | dE/d ln d medido | London | veredicto |
|----------------------|------------------|--------|-----------|
| mismo-mismo (q₊ q₊)  | **−2.70**        | −2.80  | repulsión log ✓ (3.5%) |
| neutro-A (q₊ q₋)     | **−0.011**       | 0      | neutro ✓ |
| neutro-B (q₊ −q₋)    | **−0.011**       | 0      | neutro ✓ |
| anti (q₊ −q₊)        | **+2.77**        | +2.80  | atracción log ✓ (1.1%) |

- Los dos neutros dieron energías IDÉNTICAS dígito a dígito en cada d — control
  gratis: invertir el signo del winding del otro sector es una simetría exacta
  (ψ₋₂ ↔ conjugado), y la relajación no lineal la respeta.
- La variación de E en los neutros (±0.01 sobre E≈16.3, no monotónica) está dentro
  de la tolerancia de convergencia ⟹ cota: si hay interacción residual entre
  sectores (el ~1/R³ de Eto — ver E.1), acá es < 0.5% del término log. **En nuestro
  modelo mínimo NO se ve confinamiento lineal por solitón entre los dos
  medios-nudos** (un solitón daría E ∝ d, bien visible) — diferencia con las fases
  BN de Kobayashi-Nitta (ellos tienen campo magnético externo y otra jerarquía de
  términos; anotado como pregunta, no como contradicción).
- El teorema de las dos monedas SOBREVIVE la no linealidad completa: pendientes
  correctas al 1–3.5%, neutralidad al nivel de la tolerancia numérica.
- **ROBUSTEZ CON GRADIENTE COMPLETO (mismo día, modo `div` del script)**: la letra
  chica "solo K₁" quedó saldada — repetida la tabla con el término de divergencia
  (K₂+K₃; fuerza analítica por adjuntos, autotest 1.3×10⁻⁸, un signo cazado por el
  autotest en el primer intento): London predice pendientes duplicadas ∓5.60 y
  neutros 0; medido: mismo-mismo −5.31 (5.2%), anti +5.71 (1.9%), neutros
  +0.031/−0.032 ≈ 0. Detalle fino: con div las energías ABSOLUTAS de los dos
  neutros ya no son idénticas (28.1 vs 31.0 — el término distingue las texturas)
  pero la neutralidad de la FUERZA se mantiene exacta — que es lo que el teorema
  afirma. El teorema de las dos monedas queda verificado con el funcional de
  gradientes completo.
- **EL VAN DER WAALS DEL MAR: MEDIDO (misma noche, modo `residuo` del script)** —
  método de fuerza DIRECTA sobre el nudo anclado (F_c = Σ_disco R·∂x/∂c por
  teorema de la envolvente; mucho más sensible que diferencias de energía).
  **Doble control aprobado**: par cargado F·d = +2.7875 (d=12) y +2.7295 (d=18)
  vs +2.77 de las pendientes de §30 — dos métodos independientes al 0.6-1.5%; el
  nudo solo da fuerza de borde EXACTAMENTE cero (+0.000000). **Resultado**: la
  fuerza residual entre los socios de la molécula neutra (par de sectores
  cruzados) es **ATRACTIVA y cae como 1/d^3.19** (4 puntos, d=10→28, fuerza
  0.0069→0.00026): la ley de potencia tipo dipolo ~1/d³ confirmada en el medio
  tensorial. Letra fina anotada sin sobre-interpretar: la forma exacta de Eto
  (ln(d/ξ)/d³) daría exponente efectivo ~2.5 en este rango; nuestros 4 puntos
  prefieren ~3.2 — la potencia está clara, el prefactor/log queda abierto (¿el
  acople tensorial difiere del BEC de dos componentes? — pregunta para el paper).
  **Círculo cerrado con la Parte C**: atracción débil 1/d³ de largo alcance +
  repulsión de cores de corto alcance ⟹ la molécula tiene tamaño de equilibrio —
  explica el ~3ξ estable observado. La molécula neutra del mar está LIGADA, con
  mecanismo medido. (Bloqueo #3 del esqueleto de paper: SALDADO.)

### C) La molécula suelta (vórtice entero sin anclar)

Vórtice entero (w_φ, w_α) = (1, 0) + ruido, 6000 pasos libres (solo borde
congelado): **SE PARTE en dos núcleos** (dos mínimos de amplitud bien separados)
que quedan a **separación estable 6.4 celdas ≈ 3ξ** durante 5600 pasos, con E
plana (19.0548 → 19.0531). Coherencia total con la Parte B: los dos fragmentos
son el par neutro-A (un medio-nudo por electricidad), que a orden log no
interactúa ⟹ **la molécula es marginalmente ligada en el modelo mínimo: se parte
(la tensión ∝ w² lo paga: ¼+¼ < 1, textual en Masuda-Nitta) y el tamaño queda
fijado por los residuos de corto alcance, no por un potencial log**. El splitting
del vórtice entero de ³P₂ (Masuda-Nitta PTEP 2020) queda REPRODUCIDO
cualitativamente con maquinaria independiente; el tamaño de equilibrio con
resolución de red gruesa (celda = ξ/2) es indicativo, no cuantitativo.

### D) La pregunta del 1/d² — dónde NO vive el Coulomb de verdad (análisis honesto)

Nuestro mundo tiene Coulomb 1/d² entre partículas puntuales. Lo que el bulk del mar
da entre nudos es otra cosa, y hay que decirlo sin maquillaje:

1. **Entre cuerdas (vórtices de línea)**: F/L ∝ 1/d — el Coulomb de 2D. Calculado hoy.
2. **Entre anillos cerrados (nuestras partículas candidatas, §21)**: a distancia
   d ≫ R el campo lejano de un anillo de vórtice es DIPOLAR (impulso fluido
   p = ρκπR², como una espira de corriente) → interacción anillo-anillo tipo
   dipolo-dipolo ~1/d³ (fuerza ~1/d⁴), dependiente de orientación. **No hay monopolo
   coulombiano 1/d² del winding de fase para un anillo cerrado** — el monopolo
   exigiría π₂ ≠ 0, y nuestro π₂ = 0 exacto (§20). VERIFICADO en fuentes: Biot-Savart
   para filamentos (Lamb; Saffman CUP 1992), impulso p = ρκπR² (Barenghi-Donnelly
   Fluid Dyn. Res. 41:051401), e interacción anillo-anillo dipolar usada textualmente
   en el modelo de la transición λ de Williams (PRL 59:1926 (1987): "the interaction
   between closed loops … is that of two dipoles").
3. Contraste con la gravedad: el canal ESCALAR (la huella, el déficit de densidad)
   sí da 1/d² entre nudos — eso es TCI 1.0 y sale gratis. **La asimetría
   gravedad-fácil / EM-difícil del programa es real y queda documentada.**
4. Las rutas vivas al 1/d² electromagnético genuino son las que ya teníamos
   señaladas y esto las refuerza: **la luz de la red** (string-net §27: el U(1)
   emergente de la RED de nudos, con cargas en las uniones) y **el sector de
   defectos** (Weyl+tétrada en los cores, §24). El Coulomb de dos monedas calculado
   hoy no es el EM final — es LA QUÍMICA DE LA RED: la fuerza que arma y sostiene
   las moléculas/rungs cuya dinámica colectiva tendría que ser el fotón.

### E) Veredicto bibliográfico (agente verificador, fuentes primarias — mismo día)

1. **HQV = vórtice en una sola componente: CONFIRMADO** (Seo et al. PRL 115:015301,
   textual: la componente sin vorticidad llena el core). **Dos sectores log
   desacoplados: CONFIRMADO** en la teoría de dos componentes (Eto-Kasamatsu-Nitta-
   Takeuchi-Tsubota PRA 83:063603 (2011), arXiv:1103.6144): misma componente →
   fuerza ~1/R (log); componentes distintas → ~(ln(R/ξ)−½)/R³, **sin término log
   cruzado**. MATIZ IMPORTANTE para nosotros: la neutralidad de los pares cruzados
   es exacta SOLO a orden logarítmico — queda una fuerza residual de potencia ~1/R³
   incluso en London. "Exactamente neutro" → "neutro a orden log, con residuo 1/R³".
   Los experimentos de Shin (PRL 116:185301) midieron la parte de corto alcance por
   cores magnetizados, no la ley log de dos cargas.
2. **La molécula de HQVs en ³P₂: mecanismo CONFIRMADO, nuestro número NO**: el
   splitting del vórtice entero está textual en Masuda-Nitta (PTEP 2020 013D01,
   tensión ∝ w²: ¼+¼ < 1), y lo que LIGA la molécula son **solitones lineales**
   entre los dos HQVs (Kobayashi-Nitta PRC 105:035807: confinamiento lineal por
   tensión de solitón contra la repulsión intervórtice; la distancia depende del
   campo externo, no es universal). **ERRATA PROPIA #8**: el "10.7ξ₀" que venimos
   arrastrando desde §20 NO pudo anclarse a ninguna fuente — queda DEGRADADO a no
   verificado; no citarlo más hasta encontrarle origen.
3. **Anillos dipolares sin monopolo: CONFIRMADO** (ver D.2).
4. **Chequeo de novedad: la lectura "dos electricidades" (dos gases de Coulomb
   independientes con carga fase+orientación en condensado tensorial, framing EM)
   NO ENCONTRADA en ~8 búsquedas.** Vecinos a citar siempre: Babaev PRL 89:067001
   (2002) — vórtices fraccionarios en superconductores de dos gaps, compuestos
   neutros, el pariente estructural más cercano; Eto 2011 (la matemática sin el
   framing); Kobayashi 1802.08763 (gases de Coulomb acoplados por Josephson);
   la dualidad vórtice↔carga 2D clásica (BKT). Deuda estándar antes de reclamar
   en público: barrido full-text INSPIRE.
   **BARRIDO A FONDO EJECUTADO (mismo día, 2º agente, 14 búsquedas + 6 lecturas):
   veredicto ENCONTRADO PARCIAL.** El paquete completo (J=2 tensorial + 4:1 exacto
   por simetría + desacople χ±=φ±2α + dos electricidades + canales oscuros) NO
   apareció; el framing EM con radiación oscura: cero resultados. Pero: (a) la
   versión VECTORIAL es física publicada/folklore — Rubo PRL 99:106401 (polaritones,
   4 especies (±½,±½), χ±=φ±α), ³He-A (Volovik, libro de texto), Zhou
   cond-mat/0108473 (spin-1, gases acoplados); (b) el vecino más peligroso: How-Yip
   PRR 2:043192 — London de HQV con cargas (fase, orientación) en superconductor
   nemático, PERO acopladas por parámetro GL (sin 4:1 de simetría, sin desacople);
   (c) **riesgo de trivialidad relativa declarado**: el BN de spin-2 ES literalmente
   dos componentes m=±2 → el 4:1 y el desacople son cuenta corta para la comunidad
   spinor-BEC — el valor está en escribirla y explotarla (nadie lo hizo), no en la
   dificultad; presentar como "observación estructural + consecuencias".
   (d) **DECLARACIÓN OBLIGATORIA**: el régimen dos-Coulomb-log requiere simetría
   orientacional exacta; en el ³P₂ real B y spin-órbita la rompen → confinamiento
   por solitones (Kobayashi-Nitta) — nuestro mar la tiene libre por hipótesis.
   Deudas del barrido: literatura rusa vieja de ³He; full-texts 2107.02448 y
   2510.26720 no accedidos.

**Bonus estructural que el veredicto regala**: si en nuestro D₄ los dos medios-nudos
de la molécula quedan unidos por solitones (Kobayashi-Nitta lo da para las fases BN),
el confinamiento es LINEAL — la molécula tiene tamaño de equilibrio donde la tensión
del solitón compensa la repulsión residual. Eso es exactamente lo que la Parte C
puede mostrar o refutar en nuestro modelo mínimo.

### Estado de la batalla del acople tras esta jornada

Hecha la mitad estática (cargas de los nudos bajo los canales de textura: fase y
marco). Falta la mitad DINÁMICA — el acople a los canales propagantes (TT ×2,
vectoriales ×2, fonón) para radiación: G_rad, dipolo vectorial, control
Kozik-Svistunov. Esa sigue siendo la cuenta con tres tronos (§29).

## 31. LA BINARIA DEL MAR (2026-07-18) — la mitad dinámica, primer asalto:
## dos medios-nudos orbitándose y radiando en tiempo real

**El experimento** (`binaria_del_mar.py`): el anti-par del sector q₊ — un medio-nudo
(½,¼) y su antinudo (−½,−¼), que por §30 se ATRAEN con Coulomb log — puesto en
órbita con velocidad tangencial inicial, evolucionado con la dinámica REAL del campo
de 10 componentes (leapfrog, borde esponja absorbente, red 200²). Se mide: (1) la
órbita d(t) — ¿decae? (mini-Hulse-Taylor); (2) la radiación descompuesta POR CANAL
en un anillo de medición (fase / rot-z [juntas = sectores q±] / rot-x, rot-y
[vectoriales] / amplitud) — la pregunta del dipolo §28.3 en miniatura; (3) el
espectro temporal — ¿radia a Ω (dipolo) o 2Ω (cuadrupolo)?

**Elección de dinámica DECLARADA**: segundo orden (L = ½ẋ² − E[x]), consistente con
todos los espectros §14-16 — el medio TCI es lorentziano de fábrica, no
Gross-Pitaevskii. Por eso el control Kozik-Svistunov (dinámica GP/Magnus de primer
orden, donde los vórtices no tienen inercia) NO aplica directo: en nuestra clase,
los vórtices globales tienen inercia y una binaria ± ligada es legítima (como
cuerdas globales relativistas). El control KS queda pendiente para cuando toque la
versión GP. Controles internos de hoy: gradiente analítico autotesteado,
conservación de energía en piloto sin esponja (drift ~4% en 800 pasos, integrador +
borde), pureza sectorial de la radiación como control de consistencia.

**Lección del piloto**: la estimación ingenua de la masa inercial del medio-nudo
(μ ~ E_total ~ 8) sobreestima — el piloto con Ω₀=0.059 dio órbita casi no ligada
(apoapsis ~27 desde d₀=14; la inercia efectiva del vórtice global es menor, del
orden del log local, no de la energía total con colas). Corrida definitiva:
Ω₀=0.045, órbita excéntrica contenida (Hulse-Taylor real también es excéntrico,
e=0.6 — no es defecto, es fenomenología).

### A) La caza del rastreador (dos rastreadores muertos, uno bueno)

1. Rastreador de mínimos de amplitud crudo: confundido por las ondas (d espurios).
2. Rastreador con umbral: ciego — **el core del HQV no baja a cero: la otra
   componente lo rellena** (exactamente la física de Seo confirmada en §30.E) y en
   movimiento el dip queda arriba de cualquier umbral fijo.
3. **El bueno: rastreador TOPOLÓGICO** — winding de fase de ψ_{q₊} = z₀+iz₁ por
   plaqueta: +1 en el nudo, −1 en el antinudo, inmune a ondas de amplitud, detecta
   la aniquilación por definición (los windings se cancelan). Control: d inicial
   14.04 con nudos puestos a 14.00. Lección de método para TODA futura dinámica de
   defectos: rastrear carga topológica, no amplitud.

### B) EL TEOREMA DEL PLUNGE (resultado principal — negativo y con causa)

**La binaria anti (q₊, −q₊) NO orbita: toda captura es plunge + aniquilación en
~¼ de vuelta.** Barrido de lanzamiento Ω₀ = 0.045 / 0.054 / 0.09 / 0.10 / 0.115
(energía cinética hasta 2.9, velocidades tangenciales hasta ~0.8): la trayectoria
radial d(t) es IDÉNTICA punto a punto en todos los casos (14 → 11.4 → 7.6 → 4.2 →
1.4 → 0 en t ≈ 13 u.t.), con la pareja rotando a la Ω impresa (el kick funciona:
θ(t) sigue a Ω₀ — verificado). Pre-relajar con cores anclados (protocolo §30) no
cambia nada (el ansatz solo tenía 0.14 de exceso): **el plunge es física, no
artefacto.**

**Anatomía de la muerte orbital (dos verdugos, los dos con nombre):**
1. **El potencial log es confinante**: E_int ∝ ln(d) ⟹ v_circ² = F·r/μ_eff con
   μ_eff ≈ πρ ln(d/ξ) (la inercia del vórtice global crece con el log) ⟹
   **v_circ²/c_s² ~ 1/ln(d/ξ)**: la binaria es semi-relativista salvo a
   separaciones exponencialmente grandes. Curva de rotación plana — el mismo log
   que hace galaxias hace binarias imposibles.
2. **El magnetismo de los vórtices**: la caída observada es ~7× el Coulomb
   estático (F_est = λ/d = 0.198 vs aceleración medida ~0.29·μ). En la
   electrodinámica 2D de vórtices (dualidad vórtice↔carga), nudo y antinudo
   girando llevan corrientes I = q·v PARALELAS (carga opuesta × velocidad
   opuesta) → **atracción tipo Ampère ∝ Ω²** — subir la velocidad de lanzamiento
   la aprieta más fuerte. El cociente centrífuga/Ampère ~ ln(d/ξ)/2: de nuevo el
   log, de nuevo marginal a toda separación práctica.

**Consecuencia honesta para el examen Hulse-Taylor**: el juguete 2D NO puede
rendir ese examen — su potencial confinante y su magnetismo matan la órbita antes
del régimen adiabático. El examen real vive en 3D con ANILLOS (interacción ~1/d³
dipolar + gravedad escalar 1/d², masas finitas → órbitas newtonianas legítimas).
Lo que el juguete SÍ responde (y era la pregunta §23/§28.3): qué canales cargan
la energía radiada del evento. Paralelo exacto en la literatura: las binarias de
cuerdas globales/cósmicas también son relativistas y se fusionan — el análogo
correcto del juguete es un evento de captura de cuerdas, no un púlsar binario.

### C) El evento completo: captura, fusión y estallido (canales y espectro)

Corrida definitiva (Ω₀=0.09, pre-relajada, 2500 pasos, datos crudos en
`binaria_datos.npz` local + análisis post-hoc `analiza_binaria.py`): fusión al
paso 125 (t=15, 0.42 vueltas), **91% de la energía interna convertida en ondas**
(13.1 → 1.2 — la aniquilación del cap. 8 del libro, ahora con contabilidad).

**Tabla de canales en el anillo r=70** (fracción de ⟨v̇²⟩ por ventana temporal):

| canal | lanzamiento (8-120) | ESTALLIDO (480-1600) | cola (1600-2500) |
|-------|--------------------:|---------------------:|-----------------:|
| fase  | 48.7% | 29.5% | 4.5% |
| rot-z | 48.7% | 29.5% | 4.5% |
| **rot-x** | **0.00%** | **0.00%** | **0.00%** |
| **rot-y** | **0.00%** | **0.00%** | **0.00%** |
| amp (masivo) | 1.3% | 17.2% | 44.0% |
| resto (masivos) | 1.3% | 23.8% | 47.0% |

- **LOS VECTORIALES SON OSCUROS EN ESTE EVENTO: 0.00% exacto en las tres
  ventanas** — primer test DINÁMICO de la pregunta §23. Lectura honesta: la
  oscuridad acá está protegida por simetría (el evento solo excita φ y α_z; las
  rotaciones x,y nunca se acoplan) — un evento genérico 3D podría romperla, pero
  el juguete muestra que el acople NO se genera dinámicamente donde la simetría
  no lo obliga. Para J1738 (dipolo §28.3): alentador, no concluyente.
- **fase y rot-z con correlación MÁXIMA en las tres ventanas: radiación q₊ PURA**
  — los dos sectores no se hablan ni en el régimen no lineal violento de la
  fusión. El teorema de las dos monedas (§30) sobrevive su primer test dinámico.
- **La cola es masiva**: el ringdown tardío vive en los canales de amplitud
  (44%+47%), oscilando en ω ≈ 2.6-2.8 = la frecuencia del gap (los modos masivos
  tienen velocidad de grupo → 0 y se quedan sonando cerca del origen — un
  "ringdown masivo" característico del medio, sin análogo en RG pura). El
  estallido q₊ propagante tiene banda dominante ω ≈ 0.9-1.1 ~ c_s/ξ·O(½): la
  frecuencia característica la fija el tamaño del núcleo — como en RG el
  ringdown lo fija el tamaño del horizonte (cualitativo, anotado).

**Marcador §31**: 1 teorema con causa doble (plunge: log confinante + Ampère de
vórtices), 1 respuesta dinámica (vectoriales oscuros por simetría, sectores
incomunicados), 1 contabilidad (91% radiado), 1 lección de método (rastreador
topológico), 1 límite declarado (el examen Hulse-Taylor NO se rinde en el juguete
2D — vive en anillos 3D). Scripts: `binaria_del_mar.py` (piloto/scan/full) +
`analiza_binaria.py`; 5 lanzamientos fallidos documentados en el camino.

## 6-bis. Estado de las verificaciones pendientes de §6 (cerradas esta noche)

- [x] Zoología NPPR: el medio SL(3) figura (caso 7) y NO da quinteto — Familia F muerta.
- [x] Inverse Higgs: confirmado el peligro; regla de diseño: traslaciones intactas.
- [x] ¿El quinteto propaga?: NO (IR fluido; sector transverso patológico).
- [x] Ghosts por no-compacidad: benigno (coset riemanniano).
- [x] Shear Goldstones / graviton-as-Goldstone: existe linaje (1966/1974/2002); la
      variante nuestra no está construida; 4 obstrucciones con nombre mapeadas.
- [x] Homotopías nemáticas: confirmadas (Mermin RMP 51:591; ℝP²/ℤ₂; biaxial/Q₈).

## 6. Verificaciones pendientes ANTES de creer nada de esto

- [ ] ¿La zoología NPPR (1501.03845) ya clasifica el medio SL(3)-invariante? ¿Lo
      permite o lo prohíbe? (Sospecho que su "fluido" es el caso de simetría aún mayor
      — difeos que preservan volumen — y esto sería un punto intermedio fluido/sólido.)
- [ ] Inverse Higgs: conteo real de Goldstones para cizallas internas + rotaciones.
- [ ] ¿El quinteto propaga? ¿Con qué velocidad? (paso B).
- [ ] ¿SL(3,ℝ) no-compacto genera inestabilidades/ghosts?
- [ ] Literatura de "shear Goldstones" / supersólidos / graviton-as-Goldstone: ¿alguien
      ya construyó esto? (El territorio virgen de la nota 10 era específicamente el
      orden tensorial → fase m₂=0; esta construcción podría existir con otro nombre.)
- [ ] π₁ de espacios de orden nemáticos: confirmar ℝP²/ℤ₂ y biaxial/Q₈ (recuerdo
      textbook, verificar igual).

## 32. LA LUZ DE LA RED, PRIMER ASALTO (2026-07-19) — el fotón de la circulación
## cuesta una polarización de la gravedad, y nadie tendría carga para verlo

**Contexto de sesión**: Nico levantó la pausa ("encaminá por donde decidas") y quitó
el freno de gasto. Antes de esta sección hubo que revertir una nota redundante que
re-derivaba la Familia F ya falsada (commits e05a7c3 → e997017 en notas/; error de
proceso documentado en la memoria: arrancar del CLAUDE.md viejo sin releer memoria
completa). Único rescate de ese desvío: verificación sympy independiente de POR QUÉ
muere SL(3) — el invariante mixto Tr(Q⁻¹B) con el fondo fluido regenera masa
½Tr(π²) para el quinteto: el mecanismo concreto detrás del "solo 3 Goldstones" de
NPPR caso 7.

### A) El marco exacto para "la luz de la red" existe y está verificado (web, hoy)

- **El fotón ES un Goldstone**: en teoría de gauge U(1) pura, la fase de Coulomb =
  ruptura espontánea de la simetría global 1-forma magnética; el fotón sin masa es
  su bosón de Goldstone (Gaiotto-Kapustin-Seiberg-Willett, arXiv:1412.5148;
  Lake, arXiv:1802.07747; el precursor con este título literal: Kovner-Rosenstein,
  "New look at QED₄: the photon as a Goldstone boson and the topological
  interpretation of electric charge", PRD 49:5571 (1994) + hep-th/9210154).
- **El parámetro de orden es una cuerda**: el operador que crea un vórtice/cuerda
  magnética infinita toma valor de expectación no nulo en la fase de Coulomb — 
  "fase de Coulomb = condensado de cuerdas" es literal, no metáfora.
- **Lo único que rompe la protección**: monopolos DINÁMICOS (extremos de cuerda)
  rompen explícitamente la simetría 1-forma → fotón sin protección.

### B) El regalo estructural: π₂ = 0 cambia de bando (segunda vez en el programa)

En §30.D, π₂ = 0 fue maldición: sin monopolos no hay Coulomb 1/d² del winding para
anillos. Acá es EXACTAMENTE la protección del fotón emergente: nuestras cuerdas no
pueden terminar (π₂ = 0 exacto, §20) ⟹ si un sector de cuerdas condensa, su simetría
1-forma es EXACTA y el Goldstone-fotón sin masa es obligatorio por teorema, no por
ajuste. El patrón "el bug es la feature" (nota 10) reaparece. Anotado para el futuro:
esta protección sirve para CUALQUIER U(1) emergente del programa, incluido el del
sector de defectos.

### C) La contabilidad de monedas (el resultado central — negativo y con causa)

π₁ = ℤ×_h D₄* (§20). Los sectores continuos disponibles para un fotón U(1) son las
dos monedas χ± = φ ± 2α (§30: k₊₋ = 0 exacto, rigideces iguales). La cadena, a nivel
de estructura de fases:

1. Fotón de la red ⟸ fase de Coulomb del sector de cuerdas con winding χᵢ
   ⟸ esas cuerdas condensadas (proliferadas, tensión efectiva → 0).
2. Cuerdas de winding χᵢ condensadas = orden χᵢ DESTRUIDO (eso ES la fase
   desordenada del sector) = su Goldstone muerto.
3. Pero los dos TT del D₄ sobre el eje especial SON los dos Goldstones de ese
   par degenerado (§15-16: uno 100% fase U(1), otro 100% rotacional; χ± generan
   exactamente ese espacio 2D). Matar un χ = matar una polarización.

**⟹ el fotón del sector de circulación cuesta una de las dos polarizaciones TT.**
El balance es inescapable en fases: orden (fonón/TT) y Coulomb (fotón) son fases
DISTINTAS del mismo sector — no se pueden tener ambas a la vez. Y la segunda
polarización era el hallazgo estrella de la campaña (§15, mecanismo candidato a
original). Costo: inaceptable. [Deuda declarada: buscar el test observacional
exacto de "una sola polarización tensorial" en la red LIGO-Virgo-KAGRA — el
contenido tensor-puro está testeado (GWTC-3), el sub-test de 1-vs-2 polarizaciones
TT hay que citarlo con precisión antes de llamar a esto "muerte por GW170817".]

### D) La segunda herida, independiente: electrodinámica sin electrones

En la construcción string-net del U(1) (cuerdas = líneas de campo eléctrico), las
cargas eléctricas son EXTREMOS de cuerda (Levin-Wen cond-mat/0407140; Kovner-
Rosenstein: la carga es topológica, el extremo de la línea). Nuestro π₂ = 0
prohíbe extremos; las uniones (rungs) CONSERVAN el winding (suman, no crean) ⟹
**el fotón de la circulación no tendría fuentes: campo de Coulomb sin cargas que
lo emitan o lo sientan**. Lo que sí puede vivir en uniones: cargas del sector
DISCRETO (irreps de D₄, Majoranas — §20), pero gauge discreto = gapped, sin
Coulomb 1/d². Dos causas de muerte independientes.

### E) Veredicto y lo que sobrevive

**6ª lápida: "el fotón U(1) emerge de condensar las cuerdas de circulación de la
red" queda FALSADA a nivel de estructura de fases, con doble causa (C: cuesta una
polarización TT; D: sin cargas).** Es argumento de simetrías y fases con citas,
no cálculo dinámico — los escapes lógicos quedan declarados:
- Condensar SOLO cuerdas de flujo D₄ puro con winding cero (existen en ℤ×_h D₄*
  para el subgrupo no mezclado por el entrelazado): no toca los Goldstones ⟹
  orden topológico D(D₄)-like COEXISTIENDO con el orden roto. No da fotón (gauge
  discreto), pero es la respuesta constructiva a la "pregunta afilada" de §27
  (qué subconjunto de las 45 especies condensa sin matar el D₄) — anotado como
  frente de materia, no de luz.
- El Coulomb de dos monedas (§30) NO se toca: es la química de la red en la fase
  ORDENADA (la nuestra). Todo lo calculado sobrevive.

**Consecuencia mayor: por eliminación, la luz queda en el sector de defectos** — 
tercera convergencia independiente al mismo lugar (§23 monometricidad falsada en
el bulk; §24 tétrada de Weyl en los cores cíclicos; ahora §32 la red no da fotón
con cargas). **La próxima batalla del frente luz queda definida y ya no es
opcional: BdG del core cíclico confinado (¿qué sobrevive de los 8 Weyl + tétrada
en un tubo?, §25 la dejó abierta) y si su U(1) nodal emergente hereda la
protección de π₂ = 0 (B).** El programa tiene ahora UNA sola puerta para la luz;
si el core no la da, se declara.

**Marcador §32**: 1 falsación estructural con doble causa citada, 1 regalo (π₂=0
protege fotones emergentes — reutilizable), 1 pregunta de §27 respondida
constructivamente (condensación parcial discreta), 1 deuda observacional
declarada (test 1-vs-2 polarizaciones TT), 0 scripts (argumento de fases; toda
pieza con fuente). Próxima batalla: el core cíclico.

## 33. LA BATALLA DEL CORE, PRIMER ASALTO (2026-07-19) — la materia del tubo
## depende de su orientación: el tetraedro decide qué nudos hablan

**Régimen de sesión**: desarrollo libre SIN push (pedido de Nico del día: nada se
publica, ni siquiera backup, hasta que él tenga certeza de lo que hay; commits
locales solamente).

### A) Reformulación de la batalla tras §25 y §32

La §25 estableció que el Weyl 3D + tétrada NO sobrevive tal cual en un tubo
delgado (queda un mundo 1D: escalera CdGM + rama Majorana); la §32 cerró el fotón
del bulk. La batalla del core se desarma entonces en tres preguntas, dos de las
cuales se atacan hoy:

1. **¿CUÁNTA materia 1D lleva cada tubo?** — calculable ya: conteo topológico
   (flujo espectral: ramas quirales = winding × número de Chern por rebanada).
   ESTE es el cálculo de hoy.
2. **¿La red de tubos con fermiones 1D da el fotón a nivel colectivo?** — las
   piezas de precedente existen por separado: construcciones de cables acoplados
   3D desde semimetales de Dirac (PRX 9:011039), redes de cables con CFT y reglas
   de ramificación (arXiv:1901.05918), "fotón artificial" en modelos bosónicos 3D
   (Motrunich-Senthil cond-mat/0407368). La versión sobre red de vórtices de un
   superfluido tensorial: sin construir (virgen). Queda scopeada, no atacada.
3. **¿El U(1) nodal hereda la protección π₂=0 de §32.B?** — pendiente, depende
   de cómo se realice (2).

### B) La fuente, verificada textual (ar5iv 1607.07266)

Los 8 nodos de Weyl de la fase cíclica: "The nodal points are identified as
q·k_α (α=1,…,4 and q=±1), where α denotes each vertex of the tetrahedron", con
carga de monopolo q_m = q. O sea: ±k_F sobre las 4 direcciones tetraédricas —
los 8 vértices del cubo, con el tetraedro A cargado +1 y el B (= −A) cargado −1.
El paper NO trata estados de core de vórtices (el hueco sigue siendo nuestro).

### C) El conteo (script `core_indice_toy.py`, todos los chequeos PASS)

**Mecanismo**: para un tubo con eje ĝ, el número de Chern C(k∥) de cada rebanada
perpendicular suma las cargas de Weyl cruzadas; una línea de vórtice de winding n
lleva n·C(k∥) ramas fermiónicas quirales (flujo espectral estándar — el mismo
argumento de Callan-Harvey/Volovik). Control del mecanismo en red: Jackiw-Rossi
(Dirac 2D de Wilson + vórtice s-wave a μ=0, geometría disco + pared de masa):
peso de core acumulado 0 / 1 / 2 para winding 0 / 1 / 2 ✓, con dos regalos de
física de libro como control gratis: la pared interior-SC/exterior-masivo es la
frontera de Fu-Kane con su anillo Majorana quiral (escalera ±0.081·m medida) y
el vórtice le voltea la condición de contorno (el cero de la escalera aparece
con n=1 y se hibridiza con el Majorana del core: par a E=±0.004 con el peso
repartido 0.47/0.44 — un fermión partido en dos mitades, textual).

**Resultados del conteo cíclico (combinatoria exacta + barridos):**
- **Eje (001): tubo MUDO** — cancelación exacta rebanada a rebanada, C = 0 en
  todas. Ídem (110).
- **Teorema chico (verificado 300/300 + 300/300): mudo ⟺ el eje es
  perpendicular a alguno de los tres ejes del cubo** (cada vértice + se aparea
  con el − que difiere en un solo signo: a−b = 2ê_i; si ĝ·ê_i = 0 proyectan
  iguales y se cancelan). Los mudos son exactamente TRES CÍRCULOS MÁXIMOS del
  cielo de orientaciones — medida cero.
- **Eje (111): perfil C = (1, −2, 1, 0)** — hasta 2 ramas quirales por unidad
  de winding, con el signo alternando a lo largo de k∥.
- **Genérico (2000 ejes aleatorios): NINGUNO mudo; |C| ≤ 2 siempre.**

### D) La lectura física y la bisagra nueva

**Un tubo de fase cíclica genérico viene poblado de fermiones quirales de
fábrica; solo una familia de medida cero de orientaciones da tubos estériles.**
Pero la orientación relevante NO es la del laboratorio: el orden cíclico del
core elige su propia orientación interna. La pregunta bisagra que esto define:

> **¿El funcional GL del core cíclico alinea el tetraedro con el eje del tubo
> (y cómo)?** Si el mínimo de energía es tipo (111): todo nudo lleva materia
> quiral de serie (Arquitectura A completa su sector de materia con conteo
> concreto). Si el mínimo cae en un círculo mudo: los nudos son estériles y la
> arquitectura pierde su materia. Es UN cálculo de energética de texturas con
> la maquinaria GL que ya tenemos (§16/§26) en geometría cilíndrica.

Para ANILLOS (nuestras partículas): la orientación del eje varía a lo largo del
anillo salvo que el tetraedro co-rote con la tangente — el conteo sobre un anillo
cerrado necesita tratamiento propio (¿el twist del tetraedro a lo largo del lazo
es otro número cuántico? — anotado, no resuelto).

### E) Erratas y método (3 intentos de JR, documentados en el script)

(a) borde abierto con Wilson m0=0: el borde queda crítico y contamina E≈0 —
FALLA; (b) toro con par vórtice/antivórtice por imagen mínima: la fase tiene
costuras discontinuas — FALLA; (c) disco + pared de masa: limpio, pero la
clasificación por radio medio pierde los pares hibridizados — corregida a conteo
por PESO de core acumulado. Lección de método para todos los BdG futuros del
programa: contar por peso, no por posición del centroide; y presupuestar la
física de la frontera (la pared de Fu-Kane no es ruido, es parte del sistema).

### F) Marcador honesto §33

**Qué es**: el conteo topológico de la materia 1D de un tubo cíclico, exacto y
verificado (combinatoria + control JR en red); el teorema chico de los mudos;
la bisagra energética identificada como próximo cálculo con maquinaria ya hecha.
**Qué NO es**: no dice nada todavía del fotón colectivo (frente 2 scopeado);
no resuelve la luz 3D; los números del juguete no son los del core real (HQV
con winding fraccionario + orden cíclico confinado: el winding fraccionario
puede partir el conteo a la Majorana — refinamiento declarado); y el examen de
Carlip (tétrada nodal vs métrica TT del bulk) sigue intacto en la cola.
