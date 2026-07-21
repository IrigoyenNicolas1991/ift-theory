# Sótano / EM, Paso 0 — La puerta del hielo de vortones: ¿tiene la espuma una fase Coulomb?

**Frente EM del sótano · 2026-07-21 · Fable (sesión hielo-de-vortones, retoma el
briefing f0b5399 de la sesión campana-m2) · sin agentes: papel + Luttinger-Tisza/Ewald
propio (`sotano_hielo_lt.py`), citas verificadas por búsqueda directa**

**Veredicto en una línea: M1 GATILLADO para los candidatos 1-3 (las variantes
cristalinas/estáticas): ningún grado de libertad de la espuma de vortones admite
degeneración extensiva tipo ice rule compatible con el orden J=2 — y la razón más honda
es un teorema de un renglón: el hielo y el orden laminar son las dos puntas del MISMO
espectro dipolar, y el signo vórtice (que es teorema, no elección) ya eligió punta: compra
el orden que la gravedad necesita y vende el hielo que el EM necesitaba. La única rendija
que esta acta NO cubre es la variante líquida (candidato 4), que se resuelve con la rama 8
(líquido nemático, en manos de la otra sesión) — la sinergia que el briefing señalaba.**

Criterios de muerte pre-declarados en el briefing: **M1** (ningún grado de libertad admite
degeneración extensiva compatible ⟹ lápida barata, el EM del sótano muere, la ceca vuelve
al piso de arriba) y **M2** (la degeneración existe solo destruyendo el orden laminar ⟹
"6ª lápida bis": la disyuntiva moneda-vs-gravedad es estructural en ambos pisos). Resultado:
**M1 se gatilló en los tres candidatos examinados, y M2 quedó DEMOSTRADO en su versión más
literal en el camino** (§4): no es que la degeneración "cueste" el orden — es que hielo y
orden son extremos opuestos del mismo operador, y elegir signo es elegir cuál es fundamental.

---

## 1. La pregunta (del briefing) y el método

¿Existe un régimen de la espuma de vortones con degeneración extensiva tipo ice rule — el
combustible de una fase Coulomb emergente (cargas 1/r genuinas, mecanismo
Castelnovo-Moessner-Sondhi, Nature 451:42) — en algún grado de libertad compatible con (o
desacoplado de) el orden laminar J=2?

Precisión que manda todo el examen (Henley, Annu. Rev. Condens. Matter Phys. 1:179 (2010),
verificado): el combustible de una fase Coulomb NO es "mucha degeneración" — es un
**constraint LOCAL mapeable a un flujo sin divergencia** cuyo fundamental es
extensivamente degenerado; las cargas son las violaciones puntuales de esa regla local.
Entropía suelta sin regla local (un paramagneto trivial) no fabrica Coulomb. Todo
candidato debe pasar DOS exámenes: degeneración extensiva Y regla local.

Método: papel primero (el briefing lo pedía), y para la mitad computable la maquinaria
Luttinger-Tisza + Ewald del tronco (§5, certificada) **generalizada a redes con base**
(`sotano_hielo_lt.py`, nuevo): kernel dipolar 3p×3p por celda, misma descomposición de
Ewald, convención de fase completa. El diagnóstico LT de una fase tipo hielo es nítido:
**banda(s) del fundamental PLANAS sobre la BZ** (degeneración masiva en k) versus mínimo
conmensurado aislado (orden). Regla de la casa aplicada: ningún veredicto sobre el signo
vórtice sin antes reproducir el hielo donde SÍ existe (controles C7-C8 y P1-magnético).

## 2. Controles (la maquinaria ve el hielo cuando lo hay)

| Control | Resultado | Estado |
|---|---|---|
| C1 α-independencia (pirocloro 12×12, α=2/3/4) | max dif 3×10⁻¹³ | ✓ |
| C2 traza nula / C4 hermiticidad | 10⁻¹² / exacta | ✓ |
| C3 herencia: SC magnético / SC vórtice | −2.67679 / +9.68743 vs −2.67675 / +9.68721 certificados (Δ~resolución del refine) | ✓ |
| C5 plegado: SC como supercelda base-2 = bandas SC simple ∪ plegadas | max dif 4×10⁻¹⁴ | ✓ (el control fuerte de la maquinaria con base) |
| C6 límite de Lorentz longitudinal k→0 | 8.37888 → 8π/3 = 8.37758 | ✓ |
| C7 pirocloro NN Ising ⟨111⟩: ice manifold = 2 bandas planas degeneradas en el fondo | dispersión 4×10⁻¹⁵ (planas exactas); techo dispersivo → +5.963 ≈ 6 (AIAO en k→0) | ✓ analítico reproducido |
| C8 acople dipolar nn proyectado | ê₀·T·ê₁·r³ = +1.666667 = +5/3 EXACTO — el "5D/3" de den Hertog-Gingras (PRL 84:3430, verificado) | ✓ analítico exacto |
| P1-mag: hielo dipolar completo (Ewald) | banda baja cuasi-plana: dispersión 1.5% del ancho espectral, doblete [−5.506, −5.254] — la equivalencia proyectiva de Isakov-Moessner-Sondhi ("Why Spin Ice Obeys the Ice Rules", PRL 95:217201, verificado) reproducida en casa | ✓ |

**El punto C8 merece una línea**: nuestra geometría del pirocloro (ejes locales
centro-referidos, Σ_a ê_a = 0) reproduce analíticamente el +5/3 que en la literatura del
spin ice es D_nn = 5D/3 > 0 — el acople dipolar nn en pseudo-espines es ANTIferro-σ =
pro-hielo **con el signo magnético**. Nuestro kernel está atado a la literatura por una
identidad de un renglón, no por un fit.

## 3. El censo de candidatos (en el orden del briefing)

### Candidato 1 — geometría de red no-bipartita (pirocloro de anillos, kagome apilado): MUERTO por tres candados independientes

**(1a) El candado del anclaje (la subpregunta que el briefing declaró decisiva — resuelta
en contra).** En TODO hielo publicado, el andamiaje que hace posible la ice rule — la red
frustrada Y los ejes de Ising locales — lo paga física AJENA al sector dipolar:

- Spin ice de pirocloro: la química del cristal fija la red, y el campo cristalino de la
  tierra rara (∼10²-10³ K) fija los ejes ⟨111⟩; el dipolar (∼1 K) juega DESPUÉS, sobre un
  escenario rígido que él no eligió (den Hertog-Gingras).
- Hielos artificiales, incluido el **vortex ice** que el briefing citaba: el andamiaje es
  LITOGRÁFICO — nano-trampas de doble pozo fabricadas y protocolos de annealing con
  corriente externa (Libál-Olson Reichhardt-Reichhardt PRL 102:237004 (2009), numérico;
  realización experimental Latimer-Berdiyorov-Xiao-Peeters-Kwok PRL 111:067001 (2013);
  colloquium Nisoli-Moessner-Schiffer RMP 85:1473 — todos verificados hoy). Los vórtices
  hacen hielo cuando un fabricante paga la geometría.

La espuma de vortones no tiene químico ni litógrafo: la red y las orientaciones relajan
JUNTAS bajo la MISMA energía (dipolar + núcleo), y ese problema conjunto ya tiene veredicto
LT: fundamental laminar colineal con mínimo conmensurado aislado (teorema de la espuma +
rama 1). El "campo cristalino" que siente un anillo es el campo de sus propios vecinos —
autoconsistente con el orden colineal global ±ẑ, no con ejes ⟨111⟩ locales por sublattice.
Y usar el D₄ del piso de arriba como anclador es circular en la hipótesis sótano: el D₄ ES
el orden emergente de esta espuma; no puede a la vez emerger del laminar y sostener a la
red rival del laminar.

**(1b) El candado del signo (steel-man CALCULADO: anclaje concedido gratis).** Concedimos
el andamiaje completo — red pirocloro + ejes ⟨111⟩ locales perfectos, gratis — y
diagonalizamos el dipolar completo (Ewald) proyectado, con los dos signos:

- **Signo magnético (control): HIELO.** Fondo = doblete de bandas cuasi-planas
  (dispersión 1.5% del ancho espectral total; selección débil residual, mínimo en
  k=(0,½,½) de la recíproca primitiva) — el spin ice dipolar de la literatura,
  reproducido con maquinaria propia.
- **Signo vórtice (el nuestro, teorema del signo §3 del tronco): el hielo se INVIERTE.**
  Fundamental = techo del espectro magnético: λ_max = 11.564 en k→0 con autovector
  σ = (−½,−½,−½,−½) — **σ uniforme exacto = all-in-all-out**: orden Néel de tetraedros,
  aislado (banda dispersiva al 32.3% del ancho; separada +6.52 del siguiente máximo de
  banda), degeneración global Z₂ y nada más. **El ice manifold — las 2 bandas planas —
  queda como TECHO de energía: las configuraciones 2-in-2-out son las MÁS CARAS del signo
  vórtice.** [CALCULADO]

- En cristalografía de pseudo-espines: el D_nn efectivo cambia a −5/3·(1/r_nn³) < 0 =
  ferro-σ ⟹ AIAO. La inversión de Neumann — la misma que le regala el laminar-nemático a
  la gravedad (tronco §3/§5) — le niega el hielo al pirocloro. **El teorema del signo
  cobra su segunda víctima, y esta vez en contra nuestra: lo declaramos con el mismo
  volumen** (la casa publica derrotas).

**(1c) El candado vectorial (sin anclaje, dipolos libres): tampoco.** Con las 12 bandas
completas (sin proyección), el fundamental vórtice del pirocloro es EL MISMO modo AIAO
(los momentos se alinean espontáneamente con los ejes locales ⟨111⟩ — el anclaje emerge,
pero emerge PARA el orden, no para el hielo): banda superior dispersiva (28.8%), máximo
aislado en k→0. Kagome apilado (hex+3, c/a = 0.8/1.0/1.3): máximos en k=(0,0,½), bandas
superiores al 31-39% — dispersivas todas. **Ninguna banda plana en ninguna geometría
barrida con el signo vórtice.** [CALCULADO]

### Candidato 2 — el apilado de politipos (rama 1): MUERTO por tres razones de papel

La sospecha del briefing ("subextensiva ⟹ no alcanza") se confirma y se completa:

1. **Subextensividad**: la degeneración de registro es una elección POR LÁMINA. Con L
   capas y z registros por capa, #estados ≤ z^L ⟹ S ≤ L·ln z ∝ N^(1/3): la entropía POR
   SITIO se anula en el límite termodinámico. Una fase Coulomb 3D necesita S ∝ N.
2. **Sin regla local**: el grado de libertad es colectivo por capa (objeto 2D extenso); no
   existe constraint local por vértice mapeable a un flujo sin divergencia (Henley), y las
   violaciones — las "cargas" — serían FALLAS DE APILADO: superficies extensas, no
   partículas puntuales móviles. Falla el segundo examen aunque fallara bien el primero.
3. **Ni siquiera es degeneración**: los gaps de la rama 1 son 0.0008-0.005 por anillo,
   NO cero — a T < gap el registro ordena; a T > gap hay fluctuación térmica ordinaria,
   no un manifold protegido.

El contraste didáctico que conviene recordar: el hielo de agua real tiene AMBAS
degeneraciones — la de apilado (Ih/Ic, subextensiva, estéril) y la de Pauling (protones,
extensiva y LOCAL, la madre de todas las ice rules). Nuestros politipos son la primera,
no la segunda.

### Candidato 3 — el sector del núcleo (fases/corrientes internas): MUERTO en todas sus versiones formulables hoy

Inventario honesto de los grados de libertad internos de un vortón (Γ, N, Q):

- **El momento del lazo de corriente del núcleo es ESCLAVO de n̂**: m₂ ∝ N·πR²·n̂ —
  colineal con el dipolo hidrodinámico p ∝ Γ·n̂ por geometría del anillo. La sospecha
  estructural del briefing (p̂ = Γ·n̂, "el pseudo-espín es el dipolo completo") se
  extiende al núcleo entero: todos los vectores del vortón apuntan a lo largo de n̂.
- El único Ising genuino residual es σ = sgn(N) (el sentido de la corriente interna
  relativo a la circulación). Ojo previo: si ambas especies (Γ,±N,Q) coexisten, la espuma
  es una MEZCLA binaria — la condición (0) del teorema de la espuma (monodispersidad) se
  toca; anotado para el dueño del tronco (dragón 6, polidispersidad).
- **Caso 3a (θ₂ confinada a los núcleos — el del censo estático)**: interacción entre σ's
  exponencialmente chica (solapamiento de colas) ⟹ Ising desacoplado = paramagneto
  trivial: degeneración SÍ, regla local NO ⟹ sin fase Coulomb (el examen doble de Henley,
  reprobado en la mitad que importa).
- **Caso 3b (θ₂ condensada afuera — corriente-corriente 1/d³)**: la interacción entre los
  m₂ ∝ σ·n̂ con n̂ = ±ẑ fijados por el orden laminar es OTRA dipolar Ising montada sobre
  la MISMA red y los MISMOS ejes. La banda restringida ẑ del laminar hexagonal la cubre
  en los dos signos posibles [CALCULADO, P4]: con signo tipo-vórtice el fundamental es el
  propio laminar antialineado k=(0,0,±½) (9.33/9.95/10.72 para c/a=0.9/1.0/1.1); con
  signo tipo-magnético es el orden conmensurado √3×√3 del punto K, k=±(⅓,−⅓,0)
  (−5.36/−4.54/−4.01), con fondo NO plano (la banda recorre un rango ~14; el cuartil
  inferior queda a ≥1 unidad del mínimo). La reliquia de frustración de Wannier del
  triangular NO sobrevive al largo alcance dipolar: mínimo aislado, sin manifold.
- **La fase θ₂ como variable continua**: un U(1) con acople Josephson de corto alcance
  sobre la red es un XY 3D — ordena (superfluido de núcleos: otra MONEDA tipo χ, rima con
  las dos monedas del piso de arriba, §30 de la bitácora madre) o desacopla. Sin sector
  discreto multi-pozo no hay ice rule clásica que escribir.

Rendija formal declarada: un grado Ising del núcleo NO colineal con n̂, con interacción
frustrada de largo alcance, haría renacer la pregunta — pero el modelo actual del vortón
no contiene ninguno, y fabricarlo pediría dos milagros a la vez (el grado nuevo Y su
andamiaje, véase 1a). Carga de la prueba: quien lo proponga, que lo escriba.

### Candidato 4 — la variante líquido-nemática: NO EXAMINADA AQUÍ (por diseño)

Es la sinergia que el briefing ya señalaba: si la rama 8 (líquido nemático, dragón 9 — en
manos de la otra sesión) funde las posiciones, la pregunta Coulomb renace en el fundido
(una fase Coulomb ES un líquido correlacionado). Esta acta cubre las variantes
cristalinas/estáticas; el veredicto global del EM del sótano queda CONDICIONAL a ese
examen. Nota para esa sesión: el teorema chico de §4 le deja una vara clara — necesitará
un constraint local genuino en el fundido, no solo entropía.

## 4. El teorema chico de la disyuntiva (M2, demostrado en el camino)

Para dipolos Ising sobre un andamiaje dado, el espectro LT del kernel dipolar es UNO SOLO;
"hielo" = fondo plano degenerado, "orden" = extremo conmensurado aislado, y con el cambio
de signo global s → −s el fondo y el techo INTERCAMBIAN roles. En el pirocloro ⟨111⟩ esto
es literal y está calculado en ambas direcciones (§3, 1b): el signo magnético pone el ice
manifold de fundamental y el AIAO de techo; el signo vórtice pone el AIAO de fundamental y
el ice manifold de techo. **No existe el mundo donde el mismo sector dipolar pague las dos
cosas: la moneda (fase Coulomb) y la gravedad (orden J=2) compiten por el mismo espectro,
y el signo — que en nuestro medio es un teorema (energía cinética cruzada de Neumann,
tronco §3) — ya está gastado en la gravedad.** Es la "6ª lápida bis" que el briefing
anticipaba como M2, un piso más abajo y con la misma anatomía: arriba, condensar cuerdas
de un sector U(1) mataba su Goldstone TT (§32); abajo, frustrar el sector dipolar mataría
su orden laminar — y además el signo ni siquiera deja frustrarlo.

Alcance declarado (sin overclaim): el intercambio fondo↔techo bajo s→−s es general; que el
techo magnético sea ADEMÁS aislado (y no otra banda plana) se verificó en las geometrías
canónicas de hielo (pirocloro proyectado y vectorial, kagome apilado vectorial, laminar
hex), no "en toda red concebible". El censo no puede ser exhaustivo sobre geometrías; los
candados 1a (anclaje) y la carga de la prueba cierran el resto.

## 5. Hallazgo colateral (para la rama 2, no para el EM): las redes con base y el límite del dipolo puntual

En el MODELO DIPOLAR PUNTUAL a igual densidad (v_sitio=1), las redes con base superan al
laminar SC/tet del teorema de la espuma: pirocloro vectorial λ_max = 11.56 y kagome
apilado hasta 23.5 (c/a=1.3, creciendo monótono en el rango barrido) contra el 9.687
certificado. Lectura honesta: **es en buena parte un artefacto del puntual sin núcleo** —
esas redes abren pares próximos (nn a 0.69-0.89 en nuestras unidades contra 1.0 del SC) y
el 1/d³ los premia; el núcleo duro real lo prohíbe (rama 1: el óptimo lateral satura
SIEMPRE el contacto a=2.05, y el Neumann exacto cambia cocientes hasta ×5 a
empaquetamiento). Consecuencias:

- La eliminación por cota de FCC/BCC del tronco (§5) NO se extiende a redes con base: la
  competencia estructural gruesa (rama 2) debe correr **cotas con base + hard-core +
  Neumann exacto**, o quedar declarada como abierta en ese flanco. (El teorema de la
  espuma v1 está enunciado sobre SC/tet y sigue siendo correcto tal como está escrito.)
- Si un competidor con base sobreviviera al hard-core, el parámetro de orden local del mar
  podría no ser el laminar uniaxial (el AIAO del pirocloro es un orden tetraédrico sin
  flecha, no un nemático de director único) — pregunta para el dueño del tronco, no de
  esta acta. Para el EM es moot: también ahí el fundamental es orden aislado, no hielo.

## 6. Consecuencias para el programa

1. **El EM del sótano muere en sus variantes cristalinas** (M1): la espuma no acuña la
   moneda por la vía del hielo — ni por geometría (candidato 1), ni por politipos
   (candidato 2), ni por el núcleo (candidato 3). **La ceca vuelve al piso de arriba**: el
   fotón sigue colgando de la compuerta única (§34 de la bitácora madre: U(1) fermiónico
   de los tubos — BdG del core con la matriz de gap real), exactamente como antes de abrir
   esta puerta. La puerta se abrió, se examinó y se cerró con causa — eso también ordena.
2. **La rendija viva es la rama 8** (candidato 4, líquido nemático): si el fundido
   posicional existe, la pregunta Coulomb renace ahí con la vara de Henley (constraint
   local o nada). La sinergia dragón-9↔puerta-hielo que el briefing soñaba sigue en pie —
   en la otra sesión.
3. **El teorema chico de la disyuntiva (§4) es reutilizable**: cualquier futura propuesta
   de U(1) emergente del sector dipolar del sótano (o de cualquier medio con el signo de
   Neumann) debe decir primero de qué lado del espectro pretende vivir. Con s=−1, el lado
   del hielo es el techo: se paga con energía extensiva, no se condensa.
4. **El punto (c) del briefing** (que la moneda de abajo no repita la 6ª lápida arriba)
   quedó sin objeto — no hay moneda de abajo. Pero la anatomía comparada quedó escrita
   (§4): las dos lápidas son la misma disyuntiva en dos pisos, y eso ES un resultado del
   programa ("la disyuntiva moneda-vs-gravedad es estructural", M2 textual del briefing).
5. **Deudas que esta acta deja**: (a) la confrontación rama-2-con-bases del §5 (hallazgo
   colateral, dueño: frente estructural); (b) el matiz de mezcla binaria (Γ,±N,Q) para la
   condición (0) del teorema de la espuma (dragón 6); (c) si la rama 8 da líquido, correr
   el examen de Henley sobre el fundido (dueño: quien tenga la rama 8).

## 7. Reproducibilidad

`sotano_hielo_lt.py` (este directorio): Ewald dipolar 3D generalizado a redes con base
(convención de fase completa; la fase recíproca por Poisson es e^{ik·d}·e^{−iq·d} —
errata propia #1 de la sesión: la primera versión usaba e^{+iq·d}, la CAZÓ el control C1
de α-independencia antes de producir un solo número de producción; documentada acá porque
la casa registra sus erratas). Corrido con Python 3.14 + numpy en esta máquina,
2026-07-21. Grillas: BZ 10³-12³ desplazadas (nunca pisan k=0) + refinamiento local en 3
pasos; métrica de planura = (max−min de la banda)/(ancho espectral total sobre la grilla).

Citas verificadas HOY en fuente primaria (todas las que el briefing traía de memoria):
den Hertog & Gingras, PRL 84:3430 (2000) · Isakov-Moessner-Sondhi, PRL 95:217201 (2005) ·
Libál-Olson Reichhardt-Reichhardt, PRL 102:237004 (2009) · Latimer et al., PRL 111:067001
(2013) · Nisoli-Moessner-Schiffer, RMP 85:1473 (2013) · Henley, Annu. Rev. Condens.
Matter Phys. 1:179 (2010) · Castelnovo-Moessner-Sondhi, Nature 451:42 (2008) [ya
verificada en el censo del paso 0]. Perla hallada al verificar: Perrin-Canals-Rougemaille,
Nature 540:410 (2016) — "Extensive degeneracy, Coulomb phase and magnetic monopoles in
artificial square ice": hasta el square ice necesitó DISEÑAR la degeneración
(offset de alturas entre sublattices) para alcanzar la fase Coulomb — un dato más para el
candado del anclaje.

*Acta del paso 0 del EM del sótano, escrita el mismo día en que el criterio de muerte se
gatilló, como manda la casa. El mar no acuña esta moneda: su signo ya está gastado en
sostener el orden. Si hay moneda, se acuña arriba — o en el líquido, si el líquido existe.*
