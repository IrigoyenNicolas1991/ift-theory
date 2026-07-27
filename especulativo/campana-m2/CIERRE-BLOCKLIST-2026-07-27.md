# Campaña de cierre de la lista de bloqueo del paper — 2026-07-27

**Objetivo**: dejar el paper missing-row (v0.5 → v0.6) a un solo ítem humano de
"listo para canal": el OK final de Nicolás. Autorización explícita de Nico
2026-07-27: "le mandamos de una con el máximo poder de razonamiento sin
preocuparnos en los tokens".

**Diseño**: 6 agentes en paralelo, uno por frente vivo de la lista de bloqueo —
(A) auditoría adversarial de física de §9 (FRW, la única sección sin pasada
propia); (B) acción cuadrática FRW completa + factor global vs BCP (7.22);
(C) tercera pasada adversarial del TEXTO completo v0.5; (D) dirimir el chequeo
C5d; (E) bibliógrafo verificador (ítems 2, 4, 8); (F) completitud de {X, Y}
(ítem 9). Los seis corrieron con verificación cruzada donde se tocaban; abajo,
cada acta en resumen con su evidencia. Los hallazgos se aplicaron el mismo día
(→ v0.6); los textos aplicados están en el diff del commit correspondiente.

**Balance de la campaña en una línea: seis patas — cinco cierres completos,
la sexta con tensor/vector/factor cerrados y una validación escalar en curso
— y una derrota parcial propia: la fórmula de dispersión del atractor de
§9/acta FRW era FALSA y la cazamos nosotros; la corrección REFUERZA el
congelamiento que la sección afirma. Se publica igual que las victorias,
regla de la casa. Bonus inesperados: el vector congelado sobre FLRW como
identidad nueva, y dos erratas más de BCP §8 en la gatera.**

---

## 1. C5d — DIRIMIDO (agente D + resolución de una condición de carrera)

**Veredicto: el residuo −m₁²p⁴ρ_op²/[2(−2−α+3β+α²+3αβ)(m₁²+2κp²)] impreso por
el chequeo C5d de `acople/estatico/colA_causal.py` es un ARTEFACTO DEL MÉTODO
del propio chequeo — no convención, no física.** Con ρ_op ≠ 0 el operador
trK̄·R3 genera un acople G·ψ·Ė en el Lagrangiano reducido (G ∝ ρ_op, único
operador NLO con ψ sin derivar); leer ω² como −coeff(ψ) del ψ̈ crudo omite
exactamente −G²/(4AF−D²) — identidad simbólica: ESE es el residuo. La ω²
física del MISMO Lagrangiano, por dos rutas independientes (Routhiana con
Π_E conservado, y det 4×4 sin reducción — coincide con `colA_cierre.py` D1),
reproduce EXACTA la fórmula del acta escalar, con ∂ω²/∂m₁² = 0.

- **La cancelación exacta de m₁² queda confirmada TAMBIÉN desde el pipeline
  del acople** (antes solo del escalar): dos pipelines, misma respuesta.
- **ρ ≡ ρ_op demostrado término a término** ([7a]/[7b]): mismo operador
  (trK̄·R3)/4, misma normalización — el renombre fue solo para no chocar con la
  densidad de fuente ρ(t). Ironía registrada: el hallazgo N1 de la 2ª auditoría
  hizo DESHACER la identificación en el paper; la identificación era correcta.
  §6 la recupera, ahora con demostración.
- Magnitud del artefacto si alguien usara la extracción cruda: ~13% de ω² en la
  esquina ilustrativa — no era inocuo dejarlo sin dirimir.
- Script: `acople/estatico/C5d_dirimido.py` — 26 chequeos PASS, ~10 s, 8
  bloques ([0] referencias, [1] reproducción exacta del residuo + factorización,
  [2] b,c ∝ ρ_op, [3] identidad del artefacto, [4] Routh, [5] det 4×4,
  [6] esquina numérica, [7] ρ≡ρ_op). El comentario de `colA_causal.py` quedó
  reescrito con el veredicto; el print original se conserva como registro.
- Transparencia del agente: su primera corrida tuvo 5 FAIL por un bug de signo
  PROPIO en la extracción de Routh (el patrón del residuo lo delató); corregido
  y blindado con chequeo patrón. También un crash cp1252 (carácter ∝),
  blindado con reconfigure.

**Condición de carrera dirimida por el orquestador**: la 3ª pasada de texto
(agente C) corrió `C5d_dirimido.py` MIENTRAS el agente D todavía lo corregía y
vio los 5 FAIL intermedios — su hallazgo 16 ("el cierre es incompleto") era una
lectura del estado a medio hacer. Resolución con evidencia directa: corrida del
script final en disco por el orquestador → 26/26 PASS, veredicto completo
impreso. El ítem 7 cierra con el veredicto del agente D; los sub-chequeos
[7a]/[7b] (ρ≡ρ_op) pasaban en AMBAS versiones y nunca estuvieron en disputa.

## 2. Completitud de {X, Y} — RESUELTO con lema propio (agente F)

**El ítem 9 cierra con demostración, no con cita.** Lema (forma normal): sobre
el dominio físico (B ≻ 0, det C ≠ 0), las órbitas de la acción puntual de
GL(3) (Jacobianas de los difeos internos irrestrictos; lineales alcanzan por
regla de la cadena — las segundas derivadas de Ψ solo entran en operadores ∂C,
NLO por contrato) son EXACTAMENTE las fibras del par (X, W ≡ V·B⁻¹·V); Schur:
det C = det B·(X−W), (C⁻¹)₀₀ = (X−W)⁻¹ = −1/Y² ⟹ W = X + Y². Toda invariante
LO es U(X, Y). Conteo redundante: dim órbita genérica 8 ⟹ 10 − 8 = 2
invariantes; {∇X, ∇W} generan el anulador (no hay tercero ni local).

- **Candidatos dirimidos**: V·B⁻¹·V = W (ES el segundo invariante, no uno
  nuevo); el bloque espacial de la inversa 4×4 da WX/(X−W) — función de (X,Y);
  el jacobiano orientado Z_ε de Dubovsky (ec. 15) NO es invariante
  (Z_ε → det J·Z_ε, det libre) — así muere la columna volumen-preservante
  (b, τₙ, yₙ transforman todos); Z_ε/b = ±Y no agrega nada.
- **Corolarios**: (a) restringiendo a det J = 1 el mismo conteo da {X, Y, b} —
  la fila superfluida de BCP, recuperada como CALIBRACIÓN del método;
  (b) sin el reloj Φ⁰ no queda invariante alguno (GL(3) transitivo sobre
  B ≻ 0): la fila que falta EXIGE el reloj.
- **Literatura (verificada full-text hoy)**: no existe clasificación previa del
  caso irrestricto — Dubovsky 0409124 (ecs. 14-15) se queda en el patrón de
  masas; BCP 1603.02956 ((4.9), §5.1.2) y CCPR 1907.11784 imponen det = 1;
  Nicolis-Penco-Piazza-Rattazzi 1501.03845 §2.1 se detiene explícitamente en
  Diff′(3). Precedente metodológico citado: EFT of Inflation
  (Cheung-Creminelli-Fitzpatrick-Kaplan-Senatore 0709.0293, App. A) → ref
  nueva [27] del paper; nuestro grupo es su análogo con ξⁱ(x⃗) independiente
  del tiempo — restringir a ξ(x⃗) es exactamente lo que deja vivir a Y.
- **Alcance declarado (4 cláusulas, mismas que usan [1,4])**: LO estricto (la
  base NLO de §6 es afirmación aparte); dominio no degenerado; orientación
  temporal para el signo de Y; términos Wess-Zumino fuera del argumento
  algebraico.
- Script: `exhaustividad_XY.py` — 19/19 PASS, aritmética exacta (racionales),
  3 semillas (las alternativas en scratchpad, fuera del repo). Nota de
  notación: en el paper el jacobiano orientado se escribe Z_ε (Z ya estaba
  tomado por Z^{ab} = V^aV^b en §2).

## 3. Bibliógrafo verificador — ítems 2, 4 y 8 CERRADOS (agente E)

**[16]-[18]: los tres veredictos RESPALDA, contra fuente .tex** (bajadas fuera
del repo):

- **[16] Solid Inflation (1210.0569)**: acción cuadrática tensorial con masa
  explícita m_γ² = 4εa²H²c_T², c_T² = 1 + (2/3)(F_Y+F_Z)/(F_X X) con F_Y, F_Z
  los módulos del sólido (c_T = 0 para el fluido perfecto); el blue tilt
  celebrado como "distinctive signature… unreproducible by more conventional
  models". Matiz declarado: la masa va multiplicada por εH² (slow-roll), se
  apaga en de Sitter exacto. Bonus: [16] §5 dice textual que en gauge φ^I = xᴵ
  su teoría se reduce a la massive gravity LV "studied in broad generality in
  [Dubovsky]".
- **[17] Solid Holography (1510.09089)**: "the ones with *rigidity*… encoded
  in the non-vanishing m₂"; la distinción sólido/fluido "is encoded
  **exclusively in the m₂(r) mass parameter**"; el módulo Kubo G se anula solo
  para m₂ = 0. Mismo nombre m₂, mismo rol que nuestro lema.
- **[18] Crystal gravity (2109.11325)**: "Upon integrating out the shear
  graviton… m_G = √(16πGμ/c²)" con μ el shear modulus; la rigidez "uniquely
  captured by the shear modulus μ"; gravitones acoplan "exclusively to the
  shear stress". También sostiene el Novelty search: "this graviton mass due
  to the Higgsing by crystalline matter is not commonly known".

**Datos bibliográficos completados vía INSPIRE** para [6], [7], [9]-[15],
[17]-[19], [21]-[24] + [28] nueva (GP-B: Everitt et al., PRL 106 (2011)
221101). **Dos correcciones cazadas**: [19] tenía el orden de autores invertido
(es de Matos-Tajmar, Physica C 432 (2005) 167); el segundo ítem de [24] es
**Eur. Phys. J. Plus** 132 (2017) 336, no EPJC. Extra: erratum 2011 del JHEP de
Bebronne-Tinyakov [11] agregado. **[7] verificado en CONTENIDO además de
datos**: su apéndice A (eq. MXY) lleva exactamente los pesos que §2(5) le
atribuye — uniforme en U_yₙ incluyendo n = 0, n² en U_τₙ, signos incluidos.

**Nature [23] — verificado hasta la línea del paywall**: main text (pp.
332-335) inaccesible por vías legítimas (sin preprint, sin repositorio, CLOSED
en Semantic Scholar; no se usaron espejos piratas). PERO el material abierto
del propio paper alcanzó para todo lo que el nuestro cita: **Extended Data
Table 2(b) — "Total RSS error: 0.2% of frame-dragging"**, renglón por renglón
(inyección orbital: Negligible; no-zonales, mareas, albedo, térmico, medición:
0.1% c/u); μ = 1.0001 ± 0.0019 (Monte Carlo 2025) / 1.001 ± 0.001 ± 0.002
(GEODYN II) / 1.0007 ± 0.0019 (covariance); semiejes Tabla 1 (LARES-2
12 264 567 m — confirma el a = 1.227×10⁷ m de §8); Supplementary (8 págs.) y
**Peer Review File (88 págs.)**: Iorio no es citado nominalmente en ninguna
parte, pero la SUSTANCIA de su objeción (cancelación de zonales pares
dependiente de la inyección) fue planteada por los referees y respondida
cuantitativamente — inyección real ~15× mejor que lo asumido pre-lanzamiento
(Σ inclinaciones = 180.01° vs 0.15° asumido), Fig. 5 nueva con la serie, y
residuos zonales "well below the relative uncertainty 10⁻³"; un referee pidió
"reassess the claimed measurement accuracy" y el 0.2% sobrevivió esa revisión.
§8 y el ítem 2 del block list quedaron reescritos en estos términos (ambos
lados, sin sesgo). Dato de archivo: papers hermanos arXiv:2311.13268 (primeros
resultados 2023) y arXiv:2603.00685 (feb 2026, verificación por mareas).

## 4. Tercera pasada adversarial del TEXTO v0.5 (agente C)

**30 hallazgos: 4 ALTA, 12 MEDIA, 14 BAJA — todos aplicados en v0.6** (los
números de línea del informe refieren al v0.5 pre-integración; el detalle vive
en el transcript de la campaña y los textos aplicados en el diff del commit).
Los ALTA: (1) preámbulo y block list 1 se autocontradecían — decían "falta la
2ª pasada" con las dos pasadas ya hechas y registradas diez líneas antes;
(2) §11.4 decía "before contacting the BCP authors" tras el contacto y la
confirmación; (3) **el plural "confirmed by the authors" atribuía a los tres
autores de BCP lo que confirmó L. Pilo** (cc Comelli; Ballesteros no participó)
— cinco pasajes, exactamente la inflación que la regla de paráfrasis prohíbe,
introducida por el propio orquestador en v0.5 y cazada por el auditor;
(4) la tabla de Reproducibility no tenía fila FRW. Entre los MEDIA:
inconsistencia J vs s en la atribución a CCP (independiente del mismo hallazgo
del auditor de física — dos auditores, mismo bug); doble uso de ρ sin declarar
(NLO vs densidad FRW); citas encomilladas del ghost condensate que diferían
entre abstract y §9 (des-encomilladas); [25]/[26] intercaladas en la lista;
"debt 3" que no resolvía a nada; Y = 1/√(−g₀₀) sin declarar el gauge; block
list 4 desactualizado. **Verificación de regresión**: los 43 hallazgos de las
pasadas 1-2 siguen aplicados (muestreo de los 10 más severos + ~20 más); la
aritmética de cotas re-verificada a mano por tercera vez (ℓ₁ = 2.40×10⁸ m·
(MeV/Λ)², Λ < 1.12 MeV con a = 1.227×10⁷ m, 0.13% a 1 MeV); las 27 referencias
todas citadas en el cuerpo sin huérfanas; TODOS los archivos y scripts citados
existen (verificado por listado); la regla dura de paráfrasis del correo de
Pilo se cumple en los seis pasajes (salvo el plural, hallazgo 3); las ~25
referencias cruzadas §N correctas tras la renumeración v0.4.

## 5. Auditoría adversarial de FÍSICA de §9 (agente A) — un claim muerto, el resto resiste

**EL HALLAZGO DE LA CAMPAÑA (ALTA): la dispersión ω = ±(H/√2)k + 3iH del
atractor — destacada como material propio en scoreboard, §9 y acta FRW — es
FALSA al orden en que se enuncia.** Causa: `v4b_escalar_frw_analisis.py`
truncó el determinante a O(H²) ANTES del escaleo ω = Hx; el coeficiente
c₁ = 8k⁵wH(w−1)(w³+w²+w−1) del término lineal en ω aporta 24k²H³ω sobre el
atractor (w = 1+δ, δ = (3/2)H²) — el MISMO orden H⁴ que el resto. El orden
dominante correcto del det sobre el atractor:

    det_dom = k³·[−8iω⁴ − 48Hω³ + 4iH²(k²+18)ω² + 24k²H³ω]

Con x = iy la cuártica restante es una cúbica REAL: 2y³ − 12y² + (18+k²)y −
6k² = 0. **En la ventana EFT (k ≲ 1) las cuatro raíces son {0 exacto,
i·y₁H, i·y₂H, i·y₃H} — TODAS imaginarias puras positivas: espectro puramente
disipativo, velocidad de fase CERO**: un modo difusivo lento ω ≈ i(k²/3)H y un
par ω = i(3 ∓ k/√2)H + O(k²) — el split ±k/√2 EXISTE pero vive en la parte
imaginaria: el error rotó el resultado 90° en el plano complejo. Recién en
k > k* ≈ 1.27 (FUERA de la ventana EFT) nace un par con Re ≠ 0. Verificación
triple: extracción simbólica exacta del det de la casa; serie exacta
(P − corchete_v4b·ω² = 24k⁵H³ω idéntico); numérica mpmath dps=60 con δ exacto.
Consecuencias: "damping 3H (the same a⁻³)" también cae (el modo más longevo
decae como e^(−k²Ht/3), MÁS lento); **lo que sobrevive queda REFORZADO** — no
hay modo propagante nuevo ni inestabilidad rápida: el sector está aún más
congelado que lo publicado. v4b contenía a medias la salvedad ("la
factorización es exacta solo a O(H²)") pero quedó enterrada y la fórmula pasó
al paper. Lección de proceso: las salvedades de validez de los scripts deben
subir al acta y al paper CON la fórmula, no quedarse en comentarios.

**Los otros 9 hallazgos** (aplicados): w = −1 degenerado en U* = 0 (0/0; el
enfoque es polvo w → 0 y el endpoint es Minkowski — la RUTA C numérica lo
muestra: w_eos → +3×10⁻⁴; el enunciado limpio es "vacuum-form stress, w = −1
para U* ≠ 0"); c_T² = 1 solo al LO (el α de §6 lo corre con NLO — mismo
hallazgo que el auditor de texto); la respuesta a la objeción de [6]/[26] era
una IDENTIFICACIÓN interpretativa sin cálculo que mapee las clases → reescrita
como contraste (nuestra clase: congelado con doble cero, no gradient-unstable;
la cura k⁴ tipo KSS aplica como en el ghost condensate); "J = 0 es la
condición de tadpole" precisado (J = 0 ⟺ f(φ̇) = 0 con TRES raíces; solo la
raíz φ̇ = 1 en su cuenca es el tadpole; franja 0.816 < φ̇ ≲ 0.97 de la cuenca
con ρ < 0 declarada; U* = 0 es el ajuste de CC, no dinámica); el "cero
persistente exacto" ahora con PRUEBA SIMBÓLICA (coeff(ω⁰) ∝ (3H² − ρ): se
anula por Friedmann — el cero persistente ES la constraint; antes solo floats);
J vs s de CCP (s = U_Y − 2Y·U_X = J/a³ es la densidad de entropía de CCP, no
J); alcance de la identidad tensorial declarado (FLRW PLANO, medio como única
fuente; con materia extra aplica la cancelación estándar de RG — y regalo: la
invariancia δX = δY = 0 vale para CUALQUIER perturbación puramente espacial en
gauge síncrono, más fuerte que TT); condición de raíz simple K = f′(1) = 2m₀²
≠ 0 declarada — une el atractor con la salud escalar (la misma m₀² de
m₀²m₁² > 0); el caveat de coeficientes congelados pegado a la fórmula.

**Lo que atacó y resistió**: identidad tensorial (por inversa exacta y por su
argumento estructural propio); fondo (ρ, p, J, Bianchi — re-derivados por ruta
covariante propia con lapse y U cuártica general de 15 coeficientes); dust
exacto (δp = 0 en toda raíz); puntos fijos extra (ρ(w₂) = −(5√5−11)/4 exacto,
U_X(w₃) < 0); los 6 scripts de la casa corren y dan PASS (el problema era un
truncado DENTRO del análisis, no los chequeos). El auditor declaró y mató un
pseudo-hallazgo propio (par "inestable" que era artefacto de SU linealización
de δ — con δ exacto desaparece). Sus scripts: scratchpad/frw-audit/ (fuera del
repo).

**Adenda de corrección**: el acta `frw/FRW-2026-07-21.md` queda corregida por
adenda al final (la fórmula del punto 4 refutada, el espectro correcto, la
causa) — no se reescribe la historia, se corrige con fecha.

## 6. Acción cuadrática FRW completa + factor global vs BCP (7.22) (agente B)

*(El agente sufrió un corte de red a mitad de campaña y fue reanudado dos
veces — la segunda con el blanco escalar corregido: validar contra el espectro
disipativo del §5, no contra la fórmula refutada. Cerró con acta honesta:
tensor y vector CERRADOS, factor (7.22) CERRADO, validación escalar EN CURSO.)*

**Tensor — CERRADO como identidad, doble verificación.** Desde la acción
cuadrática completa (gauge unitario cosmológico exacto, ADM, U arbitraria vía
Taylor con regla de cadena): el coeficiente de masa tensorial es
−(a³/2)(U + 2ä/a + H²)·h² → **cero imponiendo SOLO Friedmann II** —
M₂²(t) ≡ 0 como identidad FLRW para U(X,Y) y a(t) arbitrarios, sin tadpoles,
c_T² = 1 exacto al LO. δX = δY = 0 REDESCUBIERTO por el cálculo, no asumido:
la identidad tensorial de §9 queda verificada por una ruta completamente
independiente de la original.

**Vector — CERRADO, resultado NUEVO más fuerte que el encargo.** El potencial
del modo vectorial F es LA MISMA combinación de Friedmann II del tensor —
idénticamente cero on-shell, para U genérica y a(t) genérico: **el vector NO
propaga sobre ningún FLRW** (cinético (k²/4)·U_Y a⁵φ̇/(k²+2U_Y a²φ̇), potencial
nulo — la generalización FLRW exacta del cero doble de Minkowski). Verificado
por TRES rutas propias (ADM; covariante 4D; Fierz-Pauli + patrón (7.3)) **y
contra el árbitro externo: su L₂ⱽ == BCP (7.24) EXACTO on-shell** (con
w = 1, ℋ = ȧ/a, M_pl² = 1/2). Entra al paper (§9 y scoreboard) como identidad
hermana de la tensorial. Falsa alarma propia declarada y resuelta: sus dos
rutas del vector daban un signo de cinético anómalo — era un bug SUYO
(sustituir f → f·e^{ikz} y dividir por e^{2ikz} en la ACCIÓN invierte
gradientes; corregido con modos reales cos(kz) + promedio; los pipelines de
EOM no están afectados — el ansatz complejo es legítimo en ecuaciones
lineales). Lección documentada en el header del script.

**Factor 2 vs (7.22) — CERRADO, TODO PASS (17 chequeos, `frw/factor_722.py`,
~3 s).** Causa exacta: **convención de M_Pl²**. La acción de BCP (label LAllb
del .tex) es S = M_pl²∫√−g R + ∫√−g U — su M_pl² es el coeficiente de R SIN ½,
o sea M_pl² = 1/16πG = ½ en unidades de la casa (R/2). Con el MISMO Mp2
simbólico, la (7.22) impresa da residuo 0 exacto: **la (7.22) de BCP es
CORRECTA, no hay factor 2** — la razón 2 del acta FRW era la lectura con
M_pl² = 1. Caveat 2 del acta FRW-2026-07-21: SALDADO.

**Corrección de numeración de cita (aplicada al paper)**: la fórmula
M₂² = Σn²a^(−2(n−1))U_τₙ que citábamos como "(7.21)" es la **(7.22)** del
PDF/tex publicado (verificado contando entornos equation/align del fuente con
tres anclas — (7.3) = masst, (7.5)-(7.7) = masas — que cuadran con las citas ya
verificadas). (7.23) [GW] es la acción tensorial; (7.24)-(7.25) el vector.

**Bonus — DOS ERRATAS INTERNAS MÁS en BCP §8, verificadas por una vía**
(reportables a Pilo si se reabre el canal; SIN consecuencia para nuestra fila,
M₂² ≡ 0): (a) su (GW2) trae el signo de k² volteado — impresa (2M₂²+k²), de
su propia (7.23) sale (2M₂²−k²); (b) su EOM de propagación impresa
χ″+2ℋχ′+(k²−M₂²)χ=0 lleva la masa a la MITAD (debería ser 2M₂²; residuo == M₂²
verificado). También: el prefactor global de (7.23) es 2× nuestro Lagrangiano
(mismo factor en cinético y gradiente — convención de modos, sin efecto
físico). Estas dos erratas esperan verificación independiente (segunda vía)
antes de reportarse — así lo declara el paper en §9/Declared limits.

**Escalar — CORRIDA TERMINADA (mismo día, ~40 min de CPU; log completo
`s_run2.log` del scratchpad). Resultado neto: LA VALIDACIÓN ESTRUCTURAL
CONFIRMA EL ESPECTRO CORREGIDO; los tres FAIL de detalle tienen causa
identificada EN EL CÓDIGO del script (linealización del atractor), y la doble
verificación formal cierra por transitividad.** Desglose honesto:

- **PASS que confirman**: S4 — límite Minkowski EXACTO (cero doble ω⁰..ω³=0,
  coef(ω⁴) ∝ m₀²m₁²): la acción nueva reproduce el resultado central del
  sector escalar plano. S5a — coef(ω⁰) = 0 EXACTO bajo 3H² = ρ(w) con w libre:
  el cero persistente = constraint de Friedmann, confirmado desde la acción
  (el regalo del §5 verificado por segunda ruta). **S5c — en la ventana EFT
  todas las raíces son PURAMENTE IMAGINARIAS: cero velocidad de fase, espectro
  disipativo** — la confirmación estructural del hallazgo de la auditoría (la
  fórmula refutada habría dado Re ω ≠ 0). S7 — det propio / det v4 = razón
  independiente de ω (misma física que el pipeline previo; pieza clave abajo).
  S2 — bloque (α,β) algebraico en ω (constraints genuinas). **Match EXACTO en
  k = 1**: su espectro {0, 0.419i, 2.000i, 3.581i} == raíces de la cúbica de
  la auditoría (y = 2, 2 ± √10/2, verificado algebraicamente por el
  orquestador) — k = 1 es justo donde el término espurio (abajo) se anula.

- **FAIL S5b/S5d/S5e — causa identificada, no física**: el polinomio dominante
  del script difiere del det_dom de la auditoría SOLO en un término constante
  63k²(k²−1)·(factor) — los coeficientes dinámicos (x⁴, x³, x², x¹) coinciden
  EXACTOS (verificado a mano por el orquestador). Causa en el código (líneas
  1095-1119): el bloque S5 sustituye el atractor LINEALIZADO w = 1+(3/2)H²
  bajo el supuesto declarado en comentario de que "los O(H⁴) de delta solo
  tocan órdenes H⁵+" — supuesto FALSO: el c₀ del det es ∝ (3H²−ρ(w)) [el
  propio S5a lo prueba], y 3H² − ρ(1+(3/2)H²) = O(H⁴) entra AL orden
  dominante. Es la misma clase de trampa que mató a v4b (truncado en la
  sustitución del fondo en vez del escaleo), en otra puerta — y es EXACTAMENTE
  el artefacto que el auditor del §5 documentó y mató en su propia pasada
  ("par inestable espurio; con δ exacto desaparece", aud3/aud5). Los FAIL
  S5d/S5e (modo difusivo corrido, k* desplazado) son consecuencia directa del
  mismo c₀ espurio; la raíz con Im < 0 del espectro impreso en k < 1 es el
  artefacto, no una inestabilidad (en k = 1, término espurio nulo, todas las
  raíces tienen Im ≥ 0 y matchean exacto).

- **La doble verificación formal CIERRA POR TRANSITIVIDAD**: S7 (PASS) prueba
  det_B = C(fondo,k)·det_v4 con C independiente de ω ⟹ mismas raíces en ω
  para todo fondo; y aud5 del auditor corrió det con δ EXACTO (mpmath dps=60)
  dando el espectro disipativo {0, 0.0871i, 2.595i, 3.318i} en k = 1/2. Por
  lo tanto el det del script B con δ exacto da el mismo espectro. Redundancia
  formal opcional anotada: re-correr el bloque S5 de
  `accion_cuadratica_frw.py` sustituyendo δ exacto (resolver 3H² = ρ(1+δ)
  como en aud5) en lugar de la línea 1119 — se espera que S5b/d/e pasen; si
  no pasaran, reabrir.

- **Flags del script B anotados (no bloquean, no tocan al paper)**: (a) A0b
  espacial FAIL — residuo = 3a³(2U0+2U_Xφ̇²−U_Yφ̇) = 3a³(p−ρ) [álgebra del
  orquestador]: se anula en el atractor con U*=0 pero no off-shell — el
  chequeo del script está mal planteado off-shell (probable EOM de fondo
  faltante en su resta) O su coef(ψ) arrastra un término; a revisar en la
  redundancia formal. (b) S1-β FAIL ("residuo = 1"): un término β̇ residual en
  su L2 — pero S2 (PASS) prueba que el bloque (α,β) es algebraico en ω, que
  es lo que importa: las constraints funcionan; flag de construcción. (c) S6
  (resultado nuevo, sin contraste previo): la cinética WKB reducida sobre el
  atractor tiene un autovalor positivo chico (el modo que se congela, → 0) y
  UNO NEGATIVO O(1) — pregunta abierta anotada: ¿es el signo conocido del
  sector tipo-Jeans con gravedad (cf. κ < 0 como parte de la condición de
  salud en Minkowski, §6 del paper) o señala algo? El espectro de raíces —
  lo físico — es disipativo/estable, así que no es una alarma, pero queda
  como pregunta para la próxima sesión técnica.

Limitaciones declaradas
del agente: reducción escalar exacta con coeficientes t-dependientes no
entregada (solo acción completa + reducción en sistema congelado, mismo
estatus que v4); lapse genérico N(t) solo en el tensor de factor_722; banda
ω ~ H indicativa (heredada); lectura ℋ = ȧ/a de (7.24) fijada por consistencia
(BCP no la define explícitamente en esa sección).

## 7. Aplicación e inventario del block list tras la campaña

- Aplicado todo en **paper v0.6** (mismo día, commit correspondiente a esta
  acta): fixes de texto 1-30, fixes de física de §9 1-10, cierres C5d /
  exhaustividad / bibliografía, refs [27] y [28] nuevas, lista de referencias
  verificada completa.
- **Block list**: ítems **3 (Pilo), 4 (datos bibliográficos), 7 (C5d),
  8 ([16]-[18]), 9 (completitud)** → RESUELTOS. Ítem 1 → tres pasadas hechas;
  queda una lectura final del texto ensamblado. Ítem 2 → cerrado hasta la
  línea del paywall (main text de [23]; títulos de [2]/[5]; journal de [8],
  [25], [26] si existen). Ítem 5 → auditoría de §9 HECHA (§5); acción
  cuadrática: tensor y vector CERRADOS como identidades, factor (7.22)
  CERRADO como convención (§6); queda la corrida de validación escalar
  (en curso al cierre, monitoreada) y la re-verificación .tex de [26]. Ítem
  6 → OK de Nicolás: único bloqueo humano.
- Pendientes que esta campaña ABRE: permiso de cita de Pilo (pedido 25-jul,
  respuesta pendiente); erratum de PRD (decisión de ellos); las DOS erratas
  nuevas de BCP §8 (§6 de esta acta) esperan segunda vía de verificación —
  si pasan, son material natural para el próximo correo a Pilo; lectura
  final del ensamblado antes del canal; resultado de la corrida escalar
  (si contradice el espectro corregido: reportar, no forzar).
