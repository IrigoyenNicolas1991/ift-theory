# 4ª auditoría de texto del paper missing-row — v0.7 (la reescritura del teorema de superselección)

**2026-07-28, mismo día de la integración v0.7. Dos agentes independientes en
paralelo sobre el texto integrado (commit 7496779): (A) auditor adversarial de
TEXTO del paper completo con foco en lo reescrito; (B) verificador de
FIDELIDAD de cada número, fórmula, atribución e hipótesis del texto nuevo
contra las 7 actas de la campaña selección-estado, los scripts en disco y
arXiv. Los hallazgos se aplicaron el mismo día (commit de esta acta). El
título nuevo del paper quedó además RATIFICADO por Nicolás en persona ese día
("me gusta el que propusiste vos… podría quedar ese") — el flag de proceso del
auditor B sobre la decisión de título estaba ya saldado al momento de
reportarse.**

## Agente B — cotejo de fidelidad (informe completo en la bitácora de sesión)

Veredicto: **fidelidad muy alta** — los ~20 números, las 8 fórmulas y las 5
hipótesis del texto nuevo transcriptos sin un solo error numérico; varias
frases traducción casi literal del acta del verificador; las 10 frases que el
verificador de la campaña exigió corregir están las 10 aplicadas; las
referencias [29]–[32] verificadas contra arXiv, correctas.

Hallazgos aplicados:
1. **Atribución de las 4 rutas del teorema** (el más serio): el paper colgaba
   el vértice-a-vértice explícito (a2, 36 componentes) "in the adversarial
   pass" — es de la **columna A**; el verificador aportó la parametrización de
   Gram (+ nullspace) y COTEJÓ a2. Corregido con atribución por columna
   (charge column / vertex column / adversarial verifier) y, por pedido
   concurrente del agente A, con el matiz de que la vía de vértices corre al
   orden cúbico ("where the first backdoor would live").
2. **Convención m₁²**: §8-Numbers decía "as in the campaign scripts…
   m₁² = 2Λ⁴"; los scripts de selección declaran m₁² = 4Λ⁴ (los de acople,
   2Λ⁴). El O(1) se absorbe en ĉ y no cambia ningún número citado (verificado
   por B). El paper ahora declara ambas convenciones y la equivalencia.
3. **"Cosmological times" para superfluidos reales**: sobreafirmación — lo
   medido es ≳10⁵ años (superconductores, File–Mills) y "almost perfectly
   stable" lejos de v_c. Reescrito con lo medido.
4. **"Per Hubble time"** → "over the age of the universe" (las actas y el
   script usan t_edad) — abstract, scoreboard y §8.
5. **Barrera del half-ring**: E_b es el MÁXIMO de E_R − P_R·v sobre el tamaño
   del anillo (el acta distingue E_v de E_b). Reformulado.
6. **Canal de tunelación UV (Krotov)**: el acta C lo declara como incerteza
   heredada; el §8 lo omitía. Añadido como canal (iv) con ref nueva [33]
   (Krotov–Rebbi–Rubakov–Zakharov, PRD 71 (2005) 045014, verificada contra
   arXiv).
7. **ERRATA DE LAS ACTAS cazada por B**: "ACLM+Thaler hep-ph/0507120" — el
   quinto autor es **WISEMAN**, no Thaler (verificado contra arXiv). El paper
   ya citaba bien; el acta C lleva adenda de errata fechada; el comentario del
   script a4 queda intacto como registro.

Menores aplicados: §1 "(up to δ ≲ 10⁻⁴¹)"; co-rotante "GR in disguise **at
leading order**"; "no **known** thermal bath"; leak del scoreboard al número
real (era "≤ 10⁻¹⁴", redondeo a favor — ver también ALTA-2 de A); changelog
completado; Novelty "exceptions declared in the record". Verificados sin
cambio: [24] (el arXiv 1910.13818 del paper I de LARES-2 es real — subido
tardío, título y journal coinciden), la procedencia del margen de spin-down
(10% del presupuesto de disipación mareal, "mandato" declarado en
`a4_numeros.py` — ahora citado en §8), y el ancla del "< 10⁻²¹" (todo el
barrido, p = 1/R⊕ o 1/a_LARES-2).

## Agente A — auditoría adversarial de texto: 31 hallazgos (4 ALTA, 11 MEDIA, 16 BAJA)

Las 4 ALTAS (contradicciones internas objetivas), todas aplicadas:
1. §1 decía "four technical blocks" contra los "five legs" del preámbulo (el
   leg nuevo — selección de estado — faltaba justo donde se lista la cadena de
   verificación). → cinco bloques + el verificador de 5 flancos + las 2
   manchas de la campaña añadidas a la lista de slips declarados.
2. El scoreboard afirmaba "leak ≤ 10⁻¹⁴" cuando lo demostrado es 2.7×10⁻¹⁴
   (redondeo a favor propio ×2.7), y "≥14 orders" es en rigor 13.6. → "≤
   3×10⁻¹⁴" y "más de trece órdenes" (34 la estructural).
3. **El techo de δ_ret (1.7×10⁻⁴³) estaba anclado a Λ = 1 MeV — resto del
   encuadre v0.6 — mientras el texto declara la ventana hasta 10 MeV/100 GeV**:
   a 10 MeV da 1.7×10⁻⁴¹ y a 100 GeV, 1.7×10⁻³³. La inobservabilidad
   sobrevive holgada (≥38/≥30 órdenes) pero los números no cerraban entre sí.
   → display de δ_ret reescrito con las tres anclas (scan de campaña ≤1 MeV;
   ventana conservadora ≤10 MeV; extremo twinkling 100 GeV), corte UV
   necesario ~10¹⁷ GeV en todas (mismo corte: es √c), y propagado a abstract,
   scoreboard (dos filas), §1, cierre de §8 y preámbulo de §11.
4. §1 "GR everywhere measured" contradecía el sector radiativo abierto
   (Hulse–Taylor ES una medición). → "in every static and orbital regime
   measured, and in gravitomagnetism… (the radiative sector stays open, §11)".

MEDIAS aplicadas: block list 5 citaba §11.6 (renumerado → §11.4); hipótesis a
la vista en abstract (cláusula "under the hypotheses declared in §8") y
scoreboard ("Hypotheses declared, §8/§10") + condición U_Y ≠ 0 junto al
corolario de inversión; atribución de rutas (con B-1); |ĉ| = 1 y signo libre
declarados en el display de δ_ret; colisiones de notación resueltas (μ_LT de
LARES etiquetado; σ ≡ S − Ḟ definida en línea; A ≈ M̄_Pl² definido; α y M "de
[9], no los NLO de §6"); changelog completado (§§3, 6, 7, Reproducibility,
Novelty, refs) y block list 1 con §3/§6; §10 "P_aⁱ = 0 at leading order"
desambiguado ("of the leading-order Lagrangian, exact to all orders in h");
§6 cierre recalificado (la distinción compra una ley de conservación, no una
firma — el único resto vivo del encuadre viejo); "M̄² in ACLM's notation" en
el abstract; margen del spin-down con procedencia (con B); abstract largo →
diferido: nota en block list 1 (destilar ~250 palabras para el canal).

BAJAS aplicadas: Ω_nodo → Ω_node; "seconds to a few minutes"; "no leg was
refuted as a block (the FRW pass did refute and correct one formula)";
"first-order in time" (por "first-order holonomic"); registro coloquial
("declared limitations"); razones adimensionales + etiqueta de integrador en
los números RK4; semieje 12 264 567 m = 1.2265×10⁷ declarado contra el input
1.227×10⁷ de los scripts (0.04%, irrelevante al 0.13%); P_aᵘ → P_a^μ (trampa
tipográfica); "decidable at quadratic order" → "decidable — and decided —";
"< 10⁻²¹" anclado al barrido completo; "argument" → "theorem" unificado (§1,
§9); [24] verificada (sin cambio); hipótesis de suavidad declarada como
explícita nueva ("implicit in any EFT of smooth fields, made explicit here");
superradiancia reformulada por las dos vías (§6-constraint / Goldstone
gapeado, m_az ≠ m₁); definición operativa de "superselection" (sentido
dinámico); Bookkeeping note movida al final de "The two branches" (donde
pertenece narrativamente).

## Estado del paper tras esta pasada

**v0.7 auditado** — las tres capas de la reescritura (física de campaña,
fidelidad de transcripción, texto) tienen cada una su pasada adversarial
aplicada. Queda en el block list: lectura final del ensamblado por Nicolás,
abstract de submission (~250 palabras, junto con la decisión de canal), y el
OK de canal — más los residuos técnicos pre-existentes del ítem 2 y 5
(paywall de Nature, ω ~ H, exact-δ opcional, .tex de [26]).

*Acta escrita el mismo día de la pasada. El auditor A cerró: "el encuadre
v0.7 está bien logrado — la supresión de la firma propia tiene la misma
prominencia que las victorias, ni enterrada ni sobreactuada". Las cuatro
contradicciones internas que encontró eran todas reales y todas quedaron
corregidas el mismo día — así se gana el derecho a esa frase.*
