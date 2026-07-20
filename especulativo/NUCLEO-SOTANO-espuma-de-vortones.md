# NÚCLEO SÓTANO — La espuma de vortones (formalización v1)

**[ETAPA ESPECULATIVA — modelo en formalización, NO es corpus TCI]**
Fecha: 2026-07-20. Este documento es el TRONCO del frente sótano: la
formalización de la hipótesis "el mar I subyace en un fluido perfecto más
profundo". Todo cálculo futuro del sótano arranca acá y todo resultado vuelve
acá. La historia y el día a día viven en `HIPOTESIS-SOTANO-fluido-continuo.md`;
el tronco del piso de arriba es `NUCLEO-TCI2-lagrangiano.md`.

**Etiquetas**: [CALCULADO] = cálculo propio con controles; [VERIFICADO-LIT] =
verificado en fuente primaria (cita al lado); [POSTULADO] = supuesto declarado;
[ABIERTO] = sin resolver. Regla de la casa: ningún "exactamente" sin ecuación.

---

## §0. El objeto en una frase

> **El mar I de TCI no es fundamental: es la fase ordenada de una espuma de
> vortones — anillos de vórtice con carga en el núcleo — de un fluido perfecto
> más profundo.** TCI 1.0/2.0 quedan intactas como teoría efectiva (relación
> termodinámica ↔ teoría atómica); el sótano es su microfundación candidata.

Jerarquía de pisos: fluido profundo → vortones (almendras) → espuma ordenada
(mar I, orden J=2) → TCI 2.0 (condensado cuadrupolar efectivo) → gravedad
(2 TT) + defectos (materia/luz).

## §1. El piso cero: el fluido (axiomas)

El fluido de Nico (charla 2026-07-19): un continuo con **densidad ρ, presión
P(ρ), flujo v, y velocidad de sonido** c_s² = dP/dρ — es decir, un **fluido
perfecto barotrópico** (ecuaciones de Euler). Nada actúa a distancia: toda
influencia es contacto hidrodinámico (**localidad dominó por construcción** —
el principio fundacional de TCI llevado al último subsuelo).

- **Ingrediente cuántico 1 [POSTULADO, declarado]**: el fluido porta una
  fase U(1) (superfluido: v = (ħ/m)∇θ fuera de los núcleos). Consecuencias:
  (i) circulación cuantizada Γ = nκ ⟹ **todas las almendras idénticas sin
  control de calidad** (el mismo argumento que la carga, un piso más abajo);
  (ii) T=0 sin viscosidad ⟹ los vórtices no se difunden. Un fluido clásico
  puro admite remolinos de cualquier Γ — la identidad EXIGE este ingrediente.
- **Ingrediente cuántico 2 [POSTULADO, agregado tras auditoría adversarial
  2026-07-20]**: una **segunda componente** (otro U(1) aproximado, o un grado
  de libertad interno) capaz de condensar en los núcleos de los vórtices. Sin
  ella NO existen vortones (el mecanismo de Metlitski-Zhitnitsky es
  explícitamente de dos componentes; en ⁴He de una componente los anillos
  solo son estables en movimiento) y la espuma estática es imposible. **"La
  ayuda de los núcleos" no es metáfora: es un axioma.** Rima estructural
  fuerte: el parámetro de orden del piso de arriba (³P₂, spin-2, 10
  componentes) tiene de sobra componentes para llenar núcleos — y sus HQV ya
  los llenan (fase FM/cíclica en el core, §21-bis/§24 de la bitácora madre).
  [ABIERTO: derivar N y Q desde el fluido profundo concreto.]
- Toda la estática de vórtices de abajo es el límite incompresible (Mach→0);
  c_s entra en (a) la radiación de sonido por vórtices (canal disipativo,
  Kozik-Svistunov cond-mat/0505020 — ya control obligatorio del §29 de la
  bitácora madre) y (b) la EOS del medio efectivo [ABIERTO §6].

## §2. Las almendras: vortones (anillos con carga en el núcleo)

- **Anillo desnudo: jamás quieto.** Autopropulsión de Kelvin
  U = (Γ/4πR)[ln(8R/a) − ¼] [VERIFICADO-LIT: Lamb §163; constante −¼ para
  núcleo uniforme, −½ hueco — depende del núcleo]. Una espuma estática de
  anillos desnudos es ficción.
- **Vortón: anillo estable EN REPOSO** [VERIFICADO-LIT: Metlitski-Zhitnitsky,
  cond-mat/0307559 — BEC de DOS componentes, la segunda condensada en el
  núcleo]: E(R) = 2πμR + N²Q/R² (tensión vs energía del modo de fase
  atrapado; unidades ħ²/2m=1) ⟹ radio de equilibrio **R₀ = (N²Q/πμ)^(1/3)**,
  E(R₀) = 3πμR₀; estabilización mecánica por conservación de (N, Q), momento
  angular M = NQ, sin Magnus.
- **El vortón tapa el desagüe disipativo (H1 del §4)**: el canal estándar a
  T=0 (Kozik-Svistunov) drena energía ENCOGIENDO anillos hasta aniquilarlos
  (Leadbeater et al. cond-mat/0009060; colisionador de vórtices, Nature
  598:2021) — para un anillo desnudo, "bajar E a Γ fija" = el vacío sin
  anillos. El término N²Q/R² del vortón lo prohíbe: encoger por debajo de R₀
  CUESTA energía divergente. Sin vortón, el criterio del §4 es falso.
- **Ventana de estabilidad, honesta [VERIFICADO-LIT]**: la MAYORÍA de los
  vortones de teoría de campos son inestables; sobreviven los "gordos" (R ~
  pocas veces el grosor del núcleo): Garaud-Radu-Volkov arXiv:1303.3044;
  Battye-Cotterill PRL 127:241601 (2021) + Battye-Cotterill-Pearson JHEP
  04(2022)005 (catálogo de modos inestables); disipación cuántica de la
  corriente: JHEP 02(2023)004. **La espuma debe vivir en el régimen de
  anillos gordos** — lo que además mata el logaritmo de la autopropulsión
  (ln(8R/a) → 0 cuando a ~ R) y hace creíble el reposo. [ABIERTO: la ventana
  (N, Q) concreta del fluido profundo.]
- **La almendra ≔ vortón gordo.** Identidad: (Γ, N, Q) topológicos ⟹ familia
  discreta de almendras idénticas. El teorema del §5 exige monodispersidad
  (una sola especie presente) — condición (0), declarada.

## §3. La voz lejana: la interacción (teoremas del signo y del monopolo)

- **Fórmula de Neumann** [VERIFICADO-LIT por triple vía independiente:
  Talalov 2112.04859 §3 (citando Saffman 1992); Ruban physics/0001070 (nota 1
  + ec. 25); Dyson vía Meleshko, Theor. Comput. Fluid Dyn. 2010, ecs. 13-22,
  con identidad integral↔elíptica verificada a 6 decimales]:
  **E_int = (ρΓ₁Γ₂/4π) ∮∮ dl₁·dl₂/|r₁₂|** — la energía cinética cruzada
  ρ∫v₁·v₂dV de una forma cuadrática definida positiva: el signo no es
  convención.
- **Límite dipolar** [VERIFICADO-LIT, Ruban ec. 25 + asíntota elíptica
  coincidente]: con impulso P = ρΓπR² n̂,
  **E_int = (1/4πρ)[3(n̂·P₁)(n̂·P₂) − P₁·P₂]/d³**.
- **Teorema del signo (la inversión)**: E_int es la **energía cinética
  cruzada verdadera del flujo** (ρ∫v₁·v₂dV — término cruzado de una forma
  definida positiva), que coincide con la forma +M·I₁I₂ de espiras (ρ↔μ₀,
  Γ↔I) y es **término a término OPUESTA** al potencial de imanes permanentes
  U = −m·B. Razón física: el teorema de Kelvin fija Γ automáticamente. NOTA
  DE VOCABULARIO (auditoría adversarial): NO llamarla "co-energía" en
  enunciados públicos — ese término invita la objeción termodinámica de la
  batería (teorema de fuerza a corriente constante), que acá NO aplica: no
  hay batería, se minimiza la energía verdadera del fluido a Γ fija con
  disipación por sonido. Consecuencias por par (límite dipolar): coaxial
  antiparalelo −2C/d³ (óptimo), coplanar paralelo −C/d³, coaxial paralelo
  +2C/d³ — el revés del imán. [Observación posiblemente original: en ~12
  búsquedas nadie discute esta inversión en contexto vórtice↔magnetismo;
  Ruban ec. 25 la exhibe sin comentarla. Barrido INSPIRE pendiente antes de
  reclamar novedad en público.]
- **Teorema del monopolo**: ∇·ω = 0 ⟹ toda estructura de vorticidad
  localizada tiene ∫ω dV = 0 ⟹ el campo lejano ARRANCA en el dipolo ⟹
  **no existe Coulomb 1/d² entre anillos desnudos** (7ª… es la lápida del
  sótano #1, ya documentada en HIPOTESIS-SOTANO Fase A). El 1/d² del juguete
  de las sims no puede fundarse acá; la EOS efectiva es otra pregunta [§6].
- Trampa declarada [VERIFICADO-LIT, Fukumoto-Moffatt Physica D 237:271]:
  los vórtices NO obedecen F = −∇E en dinámica ideal (estructura simpléctica;
  leapfrogging, no repulsión). El uso de E como paisaje exige el §4.

## §4. El criterio estático (CONDICIONAL, con hipótesis numeradas)

Pregunta que respondemos: *¿qué configuración de orientaciones/posiciones
prefiere la energía?* **El criterio "los mínimos de E_int son los atractores"
es CONDICIONAL a tres hipótesis, ninguna demostrada todavía en este medio**
(forma exigida por la auditoría adversarial 2026-07-20):

- **(H1) Radios congelados**: el radio de cada anillo está protegido por el
  gap del vortón (E(R) diverge al encoger, §2) frente al canal fonónico de
  encogimiento. Sin H1, el mínimo de E a Γ fija es EL VACÍO SIN ANILLOS: el
  canal estándar encoge anillos hasta aniquilarlos (Kozik-Svistunov
  cond-mat/0308193; Leadbeater cond-mat/0009060; Nature 598, 2021). El
  vortón provee el mecanismo; el gap en NUESTRO fluido está [ABIERTO].
- **(H2) N conservado**: las reconexiones (que en espumas densas cambian el
  número de anillos y disparan cascadas — arXiv:1009.0823) están suprimidas
  porque cortar un núcleo cargado no conserva Q. AFIRMADO, NO DEMOSTRADO
  [ABIERTO]. Agravante geométrico (letra chica v del §5): los vecinos
  coplanares co-orientados del laminar tienen segmentos de núcleo
  ANTIPARALELOS — la configuración canónica de reconexión. La barrera es
  cálculo obligatorio.
- **(H3) Reposo**: la autopropulsión de cada anillo queda anulada. Mecanismos
  candidatos: anillos gordos (ln(8R/a) → 0, §2) y/o cancelación por
  inducción mutua de la red. [ABIERTO — condición dinámica extra que la
  minimización de E no provee sola.]

**Forma honesta de la dinámica**: dq/dt = (J − γD)∇E, con J la estructura
simpléctica de Kirchhoff (posiciones conjugadas entre sí; la orientación
atada al impulso P = ρΓπR²n̂ — un torque hace PRECESAR, no alinear) y D el
tensor disipativo. Plausibilidad de precesión + disipación = descenso en
espiral: análogo Landau-Lifshitz-Gilbert y spiral-out documentado de
vórtices (Fedichev-Shlyapnikov PRA 60:R1779; cond-mat/0312520). PERO D no
está derivado para el modo de tilt (modo cero del anillo aislado, que solo
adquiere dinámica por interacción), y el vortón precesa por su momento
angular interno M = NQ ⟹ la interacción efectiva promediada puede diferir de
la estática [ABIERTO — rama 3 del §9: espectro de tilt con Biot-Savart
linealizado].

**Cargas residuales**: la radiación fonónica se lleva E, P y L a infinito,
pero si L o la HELICIDAD total decaen más lento que la relajación
orientacional, el atractor es un equilibrio relativo (mínimo de
E − Ω·L − V·P), no un mínimo desnudo. El candidato laminar vive en el sector
limpio (P_total = 0 y Σn̂ = 0 exactos); helicidad total como ligadura: NO
chequeada [ABIERTO].

**Kelvin-Benjamin, con su boomerang declarado** [Fukumoto-Moffatt 2008]: los
anillos estacionarios ideales son MÁXIMOS de E a impulso fijo — pregunta
distinta (forma de UN anillo, dinámica ideal). Pero su contracara es
exactamente H1: que el anillo ideal sea máximo a P fijo es lo que hace que
la disipación a Γ fija lo DESTRUYA. Nuestro criterio solo es consistente
porque H1-H3 desacoplan el sector de tamaños. Precedente del método:
cristales de vórtices (Campbell-Ziff PRB 20:1886 — bajar por el gradiente
CON la ligadura declarada; allá F − Ω·J, acá H1-H3).

## §5. Los cálculos y el TEOREMA DE LA ESPUMA

Scripts en este directorio; todos numpy puro, con autotest y controles.

| # | Cálculo | Script | Resultado | Controles |
|---|---|---|---|---|
| 1 | Dispersión de Tkachenko desde la dinámica microscópica (Ewald 2D) | `sotano_tkachenko.py` | ω/k = 0.151573 vs c_T = √(κΩ/8π) = 0.151565 (0.005%) | α-independencia 6 díg.; isotropía 0.2%; red cuadrada inestable (Tkachenko 1966) ✓ |
| 2 | Orientaciones en cluster abierto (posiciones fijas) | `sotano_anillos_nematica.py` | J=2 local (S_loc 0.5-0.7), P≤0.12, mosaico global | pares exactos 5/5; LT-SC magnético ✓ |
| 3 | Espuma viva (posiciones libres, gota abierta) | `sotano_espuma_viva.py` | mosaico persiste; láminas (d_perp<d_par); sin flecha | autotest gradientes; par exacto −4/3 ✓ |
| 4 | **VEREDICTO DE BULK: Luttinger-Tisza en k + Ewald 3D** | `sotano_bulk_veredicto.py` + `sotano_bulk_cierre.py` | **teorema abajo** | tabla de certificación abajo |

**Certificación del cálculo 4 contra literatura** (todas las constantes en
μ²/a³, v_c=1; fuentes: Johnston PRB 93:014421 (=LT 1946 certificado),
Schönke et al. Sci. Rep. 10:19153 (2020), Nature Sci. Rep. 10:18781 (2020)):

| Cantidad | Nuestro código | Publicado | Δ |
|---|---|---|---|
| SC magnético, fundamental (AFM columnar, k=(½,½,0)-tipo) | −2.67675 | −2.67675 (Johnston/LT); −2.67679±2e-7 (Schönke) | <1e-5 |
| SC vórtice, fundamental (= "máximo" del problema estándar, tipo-A) | λ = 9.68721 | λ = 9.6874 (Johnston); 9.6895 (Nature 2020 ×2) | ~2e-4 |
| Límite longitudinal k→0 (Lorentz) | 8.37750-57 | 8π/3 = 8.37758 | <1e-4 |
| Independencia de α / traza nula / hermiticidad | 6 dígitos / 1e-13 / exacta | — | — |

**TEOREMA DE LA ESPUMA (v1, del MODELO DIPOLAR) [CALCULADO]**: *para dipolos
puntuales IDÉNTICOS con el signo de Neumann sobre las redes SC y
tetragonales (v_c fijo), el estado fundamental es el modo conmensurado
k\* = (0,0,½) (fracciones de la recíproca) con polarización ε ∥ k\*: láminas
de dipolos co-orientados apiladas antialineadas. El modo satisface la
restricción fuerte de Luttinger-Tisza (|n_i| = 1 exacto; toda configuración
sobre la red admite descomposición de Fourier ⟹ la cota débil es universal y
este modo la satura), de modo que* **ninguna configuración de orientaciones
sobre esas redes — mosaico, vidrio, multi-k, no-colineal — puede superarlo**
*(Lyons-Kaplan PR 120:1580). Es un nemático uniforme: director único ±ẑ,
S = 1, flecha P = 0.*

**Condiciones del teorema (declaradas)**: (0) monodispersidad — todas las
almendras con |P_i| idéntico (una sola especie (Γ,N,Q); mezclas requieren LK
generalizado); (1) posiciones en la red dada, densidad fija; (2) interacción
dipolar puntual pura.

- **Cierre riguroso de k≈0** (fortalecido por la auditoría): en el toro,
  J(0) es finito (tin-foil) y pierde; para muestras físicas, TODO modo
  uniforme tiene autovalor 8π/3 − N_α con N_α ∈ [0, 4π] ⟹ **cota 8π/3 =
  8.3776 < 9.6872 para CUALQUIER forma de muestra y condición de contorno**
  (margen 1.31); dominios macroscópicos y ferro modulado de onda larga son
  superposiciones de k chicos, cubiertas por el mismo Parseval. OJO: con el
  signo magnético estándar esta exclusión sería ILEGÍTIMA (el ferro compite
  vía término de forma) — es rigurosa específicamente para el signo vórtice.
- **Eliminación de FCC/BCC, reformulada como cota** (más fuerte de lo que
  parecía): sup_k λ_max^FCC ≤ 8.378 < 9.687 ⟹ NINGUNA configuración sobre
  FCC a igual densidad alcanza al laminar SC/tet, aunque FCC no sature su
  propia cota (ídem BCC). El mismo método de cota sirve para liquidar HCP y
  el resto de las 14 de Bravais sin necesidad de saturación [ABIERTO — rama
  2, cálculo barato].
- Resolución del barrido, declarada: grillas 14³ (SC/FCC/BCC) y 12³ (tet)
  desplazadas (evitan k=0) + refinamiento en 3 pasos (~0.005 finales);
  aislamiento verificado con caída cuadrática en 5 direcciones × 2 escalas ×
  3 c/a. J(k) es suave fuera de k=0 (interacción 1/r³) — riesgo residual de
  cruce de niveles entre puntos de grilla: menor, no nulo [declarado].
- Correspondencia con literatura [VERIFICADO-LIT]: nuestro fundamental
  vórtice ≡ el estado "de energía MÁXIMA laminar tipo-A" del problema
  dipolar estándar (Nature Sci. Rep. 10:18781 calcula ambos extremos; la
  inversión del §3 lo convierte en fundamental). El mapa columnar↔laminar
  bajo inversión de signo queda con las dos puntas publicadas y el puente
  nuestro.

**LETRA CHICA GRANDE (v) — el límite del modelo dipolar [auditoría
adversarial, CALCULADO-ADV pendiente de réplica propia]**: a distancia de
empaquetamiento (d ~ 2-3R) el dipolo puntual NO decide la estructura física:
con la integral de Neumann EXACTA (Maxwell elíptica, verificada a 6
decimales por el auditor) los cocientes exacto/dipolo varían ~5× según la
geometría del par (coaxial d=2R: 0.575; coplanar d=2.2R: 2.16; diagonal 45°:
1.62), el gap entre el laminar y su competidor con offset (tipo bct) colapsa
~97% (de ~0.5-0.7 a 0.011-0.060 por anillo) y puede invertirse con
relajación axial. Además, al contacto, los segmentos de núcleo de vecinos
coplanares co-orientados son ANTIPARALELOS = canal de reconexión (física del
núcleo, invisible para todo desarrollo multipolar). **Lectura honesta: el
teorema fija la FAMILIA ganadora (laminar-nemática, sin flecha — ningún
competidor de otra familia se acerca) en el régimen diluido-a-moderado; la
ESTRUCTURA fina a empaquetamiento denso (laminar simple vs offset-bct vs
variantes) queda ABIERTA y es la rama 1 del §9.**

- **Consecuencia (forma condicional)**: dentro del modelo dipolar sobre las
  familias barridas, con almendras idénticas, el fundamental de
  orientaciones es el laminar uniforme — y por lo tanto **el mosaico de los
  cálculos 2-3 era efecto de superficie, no frustración intrínseca del
  material**. Para promover esto a "océano físico" faltan: H1-H3 del §4, la
  EOS que fije la densidad (el dipolar solo, con este signo, favorece
  comprimir — la estabilización es física de corto alcance fuera del
  modelo), la competencia estructural fina de la letra chica (v), y las
  redes restantes como cotas. Lo que SÍ queda establecido sin condición
  dentro del modelo: **sin flecha (P=0) y orden J=2 por láminas en toda la
  familia ganadora** — la gota macroscópica no depende de cuál variante
  laminar gane.

## §6. El puente al piso de arriba (qué compra TCI con esto)

| El piso de arriba postula | El sótano ofrece | Estado |
|---|---|---|
| Repulsión entre almendras | Derivada (Neumann; co-rotantes 2D ~1/d, anillos ~1/d³) | [CALCULADO/VERIFICADO-LIT] |
| Identidad exacta de almendras | Γ=nκ + (N,Q) topológicos | [VERIFICADO-LIT] |
| Localidad (pregunta fundacional) | Dominó por construcción (Euler) | axioma |
| Parámetro de orden J=2 (la gota) | **Teorema de la espuma: nemático uniforme sin flecha** | [CALCULADO] |
| Signo γ>0 del GL (D₄-BN) | ¿empaquetamiento de la fase laminar? | [ABIERTO] |
| EOS P=ρc² del mar | energía/compresibilidad de la espuma ordenada | [ABIERTO] |
| Van der Waals del mar ~1/d^3.19 (§30) | dipolar 1/d³ genérico; además Eto PRA 83:063603: fuerza intercomponente [ln(R/ξ)−½]/R³ — ¿mismo mecanismo? | [ABIERTO — rima anotada] |
| Cores con estructura (luz/materia §24-§33) | vortones = anillos CON carga nuclear de fábrica | rima estructural — dos pisos piden el mismo órgano |

## §7. Dragones vivos (por peso, actualizado tras la auditoría)

1. **El canal de reconexión del laminar (H2)**: los vecinos coplanares
   co-orientados tienen segmentos de núcleo antiparalelos — la configuración
   canónica de reconexión, agravada porque la carga Q ENGORDA los núcleos.
   Si la barrera no existe, la red se come a sí misma. Cálculo obligatorio.
2. **La estructura fina a empaquetamiento denso**: el dipolo puntual no
   decide entre laminar simple y offset-bct (letra chica v del §5) — Neumann
   exacto o nada.
3. **Interacción vortón-vortón: NUNCA calculada** (verificado; los gases
   cosmológicos de vortones se tratan como polvo). Riesgo: canales nuevos
   del núcleo (Eto intercomponente ~1/R³; Biot-Savart corriente-corriente si
   la segunda componente vive también afuera — declarar en cuál caso
   estamos). Oportunidad: publicable por derecho propio.
4. **Precesión vs relajación (tilt)**: el vortón tiene momento angular
   interno M=NQ; bajo torque precesa. Sin el espectro de tilt (Biot-Savart
   linealizado + corriente de núcleo) el fundamental estático no está
   dinámicamente certificado. Además: helicidad total como posible ligadura
   de la relajación, no chequeada.
5. **El problema del exceso, invertido**: los vortones cosmológicos
   sobrecierran el universo de puro estables (Brandenberger PRD 54:6059);
   nuestra pregunta es por qué la espuma no es dominada por una población
   térmica de anillos chicos [ABIERTO].
6. **Polidispersidad**: el teorema exige una sola especie (Γ,N,Q); una
   espuma real puede mezclar especies ⟹ LK generalizado o desorden.
7. **El eje del monocristal**: ya no hace falta rotación global, pero un
   monocristal cósmico laminar tiene ejes ⟹ el mismo dragón de anisotropía
   del D₄ de arriba (§22). ¿Son EL MISMO dragón? (Si el D₄ de arriba ES la
   espuma de abajo, sí — y la salida monometricidad-por-defectos ya está en
   juego arriba.) [ABIERTO]
8. **Kelvin-Benjamin residual**: subsistemas con impulso neto pueden
   invertir el extremo relevante localmente [vigilar].

## §8. Caja de herramientas (para el próximo que calcule)

- **Ewald dipolar certificado**: fórmulas B(r), C(r), recíproco, auto,
  superficie verificadas verbatim contra Wang-Holm (cond-mat/0107064, ecs.
  2-8; ojo: página correcta JCP 115:6351) y Cerdà et al. (0805.4783, ecs.
  9-13). Fuerzas: D(r) = −C′/r (ec. 12 W-H). Término de superficie DPS:
  2π|Σμ|²/((2ε′+1)V); tin-foil ε′=∞ lo anula; para estados Σμ=0 es neutral
  en toda convención.
- **Controles obligatorios de cualquier Ewald nuevo**: (1) dipolo único en
  caja = 0 exacto (Cerdà ec. 33); (2) SC magnético −2.67675; (3) SC vórtice
  +9.6874; (4) límite Lorentz 8π/3; (5) α-independencia; (6) FM cúbico bajo
  tin-foil = 0 exacto.
- **Convenciones**: v_c = 1 (volumen por sitio); Johnston usa a = arista de
  celda CONVENCIONAL (FCC: 4 sitios/a³ — dividir λ por 4 para comparar);
  nuestro λ tiene signo opuesto al de Johnston (E_mag/N = +λ_min/2 nuestro
  = −λ_max/2 de Johnston).
- **Lecciones de método** (acumuladas, 4 erratas propias del sótano): ventana
  radial simple NO alcanza para sumas dipolares (usar Ewald); autotest de
  gradientes SIEMPRE; python con `-u` en background; el test de
  conmensurabilidad con abs() (errata del flag, corregida en
  `sotano_bulk_cierre.py`).
- **El criterio del extremo**: antes de minimizar nada, declarar la ligadura
  (§4). Es exactamente donde un signo invierte conclusiones.

## §9. Ramas abiertas (priorizadas tras la auditoría) y criterios de muerte

1. **Neumann exacto sobre la familia laminar** (laminar simple vs offset-bct
   vs variantes, con relajación c/a a densidad fija; réplica propia de los
   números del auditor): decide la estructura fina. Muerte parcial: si gana
   una fase NO laminar, el teorema v1 queda como límite diluido.
2. **Cotas para HCP + las 14 de Bravais** (método de la cota sin saturación,
   §5): cierra la competencia estructural gruesa. Barato.
3. **Espectro dinámico del cristal** (tilt/precesión + fonones, Biot-Savart
   de primer orden + corriente de núcleo): certifica (o mata) el fundamental
   como atractor; de paso responde qué MEDIO EFECTIVO es la espuma (módulos,
   EOS → puente §6). Muerte: modos blandos inestables.
4. **La barrera de reconexión (H2)** con núcleos cargados: ¿cortar cuesta Q?
   Muerte: sin barrera, la red laminar se autodestruye.
5. **El vortón del fluido profundo**: derivar la segunda componente, N, Q,
   el gap de R (H1) y la ventana de estabilidad "gorda". Conecta con el
   D₄-BN de arriba (¿la segunda componente ES otra componente del parámetro
   de orden spin-2?).
6. **Vortón-vortón** (canales del núcleo): el hueco publicable. Control: Eto
   2D (PRA 83:063603).
7. **La población térmica** (dragón 5). Muerte: si los anillos chicos
   dominan a toda T, la espuma no es EL vacío.

## §10. Registro de auditoría adversarial (2026-07-20)

Tres escépticos independientes con mandato de refutar, ANTES de sellar v1:
(a) **criterio estático**: sobrevive GRAVE ⟹ §4 reescrito condicional
(H1-H3, forma (J−γD)∇E, cargas residuales, boomerang K-B, ventana de
vortones gordos); (b) **teorema LT**: sobrevive GRAVE ⟹ condición (0)
monodispersa, cierre riguroso de k≈0 (regalo: la exclusión es una COTA
válida para toda forma), FCC/BCC reformulados como eliminación por cota,
"co-energía" desterrada del vocabulario público, Consecuencia rebajada a
condicional; (c) **dipolo/vortón**: NO sobrevive como estaba ⟹ segunda
componente elevada a AXIOMA (§1), letra chica (v) del campo cercano
(cuasi-degeneración laminar/offset, canal de reconexión), "orientación
fija" reemplazada por la deuda del espectro de tilt. Los números del
auditor (c) son [CALCULADO-ADV]: réplica propia pendiente en rama 1.

## Bibliografía del tronco

Saffman, *Vortex Dynamics*, CUP 1992 (vía Talalov arXiv:2112.04859) ·
Ruban, arXiv:physics/0001070 · Meleshko, Theor. Comput. Fluid Dyn. 24:403
(2010) · Fukumoto-Moffatt, Physica D 237:271 (2008) · Campbell-Ziff, PRB
20:1886 (1979) · Luttinger-Tisza, PR 70:954 (1946) + errata PR 72:257 ·
Lyons-Kaplan, PR 120:1580 (1960) · Johnston, PRB 93:014421 (2016) /
arXiv:1505.00498 · Schönke et al., Sci. Rep. 10:19153 (2020) · *Minimum and
maximum energy for crystals of magnetic dipoles*, Sci. Rep. 10:18781 (2020) ·
Groh-Dietrich, PRE 63:021203 (2001) · de Leeuw-Perram-Smith, Proc. R. Soc. A
373:27,57 (1980) · Wang-Holm, JCP 115:6351 (2001) / cond-mat/0107064 · Cerdà
et al., JCP 129:234104 (2008) / arXiv:0805.4783 · Metlitski-Zhitnitsky,
cond-mat/0307559 · Radu-Volkov, Phys. Rept. 468:101 (2008) · Battye-Cotterill,
PRL 127:241601 (2021) + JHEP 04(2022)005 · Eto et al., PRA 83:063603 (2011) ·
Brandenberger-Carter-Davis-Trodden, PRD 54:6059 (1996) · Kozik-Svistunov,
cond-mat/0505020 · Tkachenko, JETP 22:1282, 23:1049 (1966), 29:945 (1969) ·
Coddington et al., PRL 91:100402 (2003) · Fetter, RMP 81:647 (2009) ·
Saadeh et al., PRL 117:131302 (2016) · Huang-Low-Tung, arXiv:1106.5283 ·
Nguyen-Moroz, arXiv:2310.13741 · Moroz-Hoyos et al., SciPost Phys. 5:039
(2018).
