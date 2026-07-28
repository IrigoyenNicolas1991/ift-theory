# Selección de estado — acta bibliográfica de fuentes primarias (columna C)

**Campaña m₂=0 · frente selección de estado · 2026-07-27 · bibliógrafo: 1 agente
(~215k tokens, 57 usos). Método: fuentes LaTeX bajadas de arXiv y LEÍDAS del .tex
(no abstracts) salvo donde se declara; barridos INSPIRE con queries declaradas.
Fuentes guardadas en el scratchpad de la sesión (`seleccion-biblio/`).**

## Blanco 1 — Fuentes en movimiento en el ghost condensate: YA RESUELTO (2004-2007)

Corrección a la premisa de la apertura: ACLM 0312099 NO trae moving sources; el
cuerpo del cálculo está en **Dubovsky hep-ph/0403308 ("Star tracks in the ghost
condensate")**, **Peloso–Sorbo hep-th/0404005 ("Moving sources in a ghost
condensate")** y la TASA en **ACLM+Thaler hep-ph/0507120 §Nonlinear Energy Loss**:

- Dispersión con gravedad (0312099): ω² = α²k⁴/M² − α²(m²/M²)k², m ≡ M²/(√2M_Pl);
  Jeans para k<m con Γ_max = αM³/(4M_Pl²). Velocidad del sector: v_s ~ M/M_Pl
  (≈10⁻¹² m/s a M~10 MeV) ⟹ toda fuente real es hiper-supersónica; v_Landau = 0
  (sin umbral: toda fuente radia — la pregunta es la tasa).
- La estela (0403308): cono α = r_c/(vt_c) con oscilaciones que crecen e^{T/2}
  (la Jeans, apagada por Hubble si H > 1/t_c); supresiones de fuente extensa
  (r_c/L)^{3/2}, (r_c²√T/L²). El observador CO-MÓVIL no ve crecimiento
  (Peloso-Sorbo): Newton se recupera; el drama queda en la estela.
- **LA TASA (0507120, ec. finalEdot): Ė ~ αM²v³** (independiente de la masa del
  objeto y de M_Pl; textual: "completely negligible for macroscopic objects");
  con gravedad superficial débil, supresión extra (R_S/(v²R))². Números de
  ellos: Sol a v=10⁻³, M=10 MeV: Ė ~ 20 W; frenado ≳ 10²⁴ años.
- **El regalo estructural (0507120, §Fluid Picture, textual): el flujo del
  condensado es IRROTACIONAL (u_μ = ∂_μφ ⟹ ∇×u = 0) y el medio se arrastra
  geodésicamente (r_drag ~ R_S/v²)** ⟹ el sector escalar NO puede co-rotar:
  la co-rotación exige vórtices o un sector vectorial — nuestro m₁²≠0 es
  exactamente el ingrediente que la habilita. Explica por qué el ghost
  condensate puro nunca tuvo este problema y delimita qué es nuestro.
- Canal UV: "holes" de Krotov et al (hep-ph/0407081) — tunelación del
  condensado, tasa "exponentially sensitive to the UV completion": se declara
  como incerteza, no se calcula en la EFT.

**Veredicto: DIRECTO-POR-DICCIONARIO — el canal Cherenkov escalar tiene tasa
conocida, ajena (2004-2007) y despreciable. Nuestro aporte posible es solo la
versión ROTACIONAL con sector vectorial gapeado (blanco 4 confirma que está
vacante).**

## Blanco 2 — Corrientes persistentes reales: el marco y los números

Fuente primaria del marco: **Varoquaux 1406.5629 (RMP 87, 803)** — Kramers
Γ = (ω₀/2π)e^{−E_b/k_BT}; MQT Γ₀ = (ω₀/2π)(120πS₀/ħ)^½e^{−S₀/ħ}, S₀=36E_b/5ω₀,
crossover ħω₀ = 2πk_BT_q (⁴He: T_q≈0.147 K). **La barrera del half-ring:
E_v = E_R − P_R·v con E_R = ½ρκ²R ln(8R/a₀), P_R = πρκR² ⟹ E_b ∝ ρκ³/v: DIVERGE
cuando v→0** — sin "casi-decaimiento" a velocidad chica. Mediciones: He-II
decae solo cerca de v_c (Kukich-Henkel-Reppy 1968, secundario); BEC anular NIST
40 s limitado por el trap, no por el flujo (1101.0019); Cambridge: "for v_s ≪
v_c the decay is strongly suppressed… almost perfectly stable, as… in bulk
superconductors" (1112.0334); superconductores ≳10⁵ años (File-Mills 1963,
secundario). Caveat honesto (Kumar 1608.02894): cerca del umbral ni Arrhenius
ni MQT ajustan (T_esc ≫ T) — el marco tiene grietas EN v≈v_c (no nos afecta:
estamos a v/v_c ~ 0, pero no vender el marco como cerrado).

**Veredicto: ANÁLOGO-ÚTIL. Protege contra decaimiento CON umbral (v_c>0) — se
aplica al sector vectorial gapeado; NO aplica al canal escalar sin gap (que es
el del blanco 1).**

## Blanco 3 — Fricción/superradiancia de cuerpos rotantes en medios

- **Brito-Cardoso-Pani 1501.06570 (review)**: "rotation AND a dissipation
  channel are enough to trigger superradiance" — y su recíproco: sin canal
  absorptivo a ω = mΩ, no hay torque de frenado (correspondencia
  superradiancia↔fricción de marea, Glampedakis et al). Tasas con campos
  masivos: ω_I ∝ (Mμ)^{4l+5} (Detweiler) — los canales gapeados mueren con
  potencias altísimas del acople.
- **Fricción dinámica con ω∝k²** (Hui et al 1610.08297 apéndice cuántico;
  Lancaster et al 1909.06381): F = 4πG²m²ρ/v²·C con C ≈ (kr)²/3 para kr≪1 —
  supresión del wake cuando la escala del sistema entra; validado contra
  simulaciones. Prior art de "cuerpo rotante que no se frena" (barras
  galácticas en FDM).
- **Berezhiani-Khoury 1507.01019**: halos superfluidos rotantes → red de
  vórtices carga el momento angular; sin frame dragging computado.
- **Oshita et al 2102.01741**: superradiancia sin rotación con dispersión
  Lifshitz z=2 — necesita horizonte; no aplica a la Tierra.

**Veredicto: ANÁLOGO-ÚTIL — las dos piezas (canal a ω=mΩ obligatorio; drag
suprimido del sector blando) encajan. El spin-down de un cuerpo rotante en un
ghost condensate NO está calculado: pieza genuinamente nueva con partes listas.**

## Blanco 4 — Metaestabilidad en LV massive gravity: VACANTE (confirmado)

Barrido INSPIRE (7 queries declaradas en el informe, 0-92 hits todos
irrelevantes): nadie discutió metaestabilidad de configuraciones del medio de
Stückelberg alrededor de fuentes rotantes en fases m₁²≠0. **ALERTA de cita
obligada: Kiselev gr-qc/0406086 tituló "ghost condensate ⟹ flat rotation
curves" en 2004** — mecanismo totalmente distinto (gradiente espacial estático
+ monopolo; sin rotación ni sector vectorial), pero el titular no es virgen:
citar. AeST 2505.03527 (frame dragging en éter escalar-tensor, sin gap ni
metaestabilidad) como vecino.

## Blanco 5 — ³He-A y espinores: EL control conceptual

Varoquaux (secciones ³He): en ³He-A la circulación NO está cuantizada
(Mermin-Ho) y "the A-phase persistent superflow can be relaxed by textural
motion alone without… vortices. However, if large-scale motion of the texture
is suppressed, dissipation can be quenched and persistent currents stabilised"
(polvo de SiC inmoviliza l̂ — Gammel-Hall-Reppy 1985). Espinores (Beattie
1210.4834): corriente estable con polarización alta, inestable bajo un umbral.
**Moraleja doble: un modo interno blando sin gap mata la persistencia sin
barrera topológica; gapear/pinnear el modo la restaura. Nuestro medio tiene
AMBOS: vector gapeado (protegido) + escalar blando (canal siempre abierto —
pero acoplado solo gravitacionalmente, con la tasa del blanco 1).**

## Síntesis de la columna C (jerarquía a v minúscula)

1. Phase slips/nucleación: MUERTO (barrera ∝ 1/v diverge; sin baño térmico).
2. **Cherenkov escalar: el único canal sin umbral — tasa importada Ė ~ αM²v³:
   "decae en principio, persiste en la práctica"** (tiempos ≫ 10²⁰ edades).
3. Superradiancia del sector gapeado: prohibida bajo el gap (sin modos a
   ω=mΩ<m₁); si hubiera solape, (acople)^{4l+5}.
4. Tunelación UV (Krotov): incerteza declarada, no tasa.

**Lectura bibliográfica: el co-rotante, SI SE PUEBLA, es metaestable con vida
cosmológicamente absurda. La decisión de rama pasa a depender enteramente del
POBLAMIENTO (columna B: carga de Noether + IVP adiabático + condiciones
iniciales FRW).** Fórmulas concretas transferidas a las columnas A y B en el
informe completo (transcripto en la bitácora de sesión).

*Acta escrita el mismo día del barrido. Citas textuales re-verificables contra
los .tex guardados antes de transcribir a cualquier paper.*

---

## ERRATA DE ESTA ACTA — 2026-07-28 (cazada por el cotejo de fidelidad de la 4ª auditoría del paper)

Esta acta (y la síntesis y el comentario del script `colA/a4_numeros.py`, que
la heredaron) dice **"ACLM+Thaler hep-ph/0507120"**: el quinto autor de
"Dynamics of Gravity in a Higgs Phase" (JHEP 01 (2007) 036) es **Toby
WISEMAN**, no Thaler — verificado contra arXiv el 2026-07-28. El contenido
citado (§Nonlinear Energy Loss, §Fluid Picture, la tasa Ė ~ αM²v³ y la
irrotacionalidad) es correcto y no cambia. El paper missing-row cita [9] con
los autores correctos desde antes de esta errata. Registro intacto arriba;
esta adenda es la corrección fechada (regla de la casa: las actas no se
reescriben).
