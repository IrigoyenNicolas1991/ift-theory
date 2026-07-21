# Bibliografía FRW de medios auto-gravitantes — acta de fuentes primarias

**Campaña m₂=0 · tarea 4 (FRW) · 2026-07-21 · bibliógrafo: 1 agente (~263k tokens,
55 usos de herramientas). Método: fuentes LaTeX bajadas de arxiv.org/e-print y
LEÍDAS del .tex (no abstracts), metadatos verificados contra las APIs de arXiv e
INSPIRE. Fuentes descargadas en el scratchpad de la sesión (frw-biblio/) para
re-verificación de citas.**

Contexto: nuestro cálculo de fondo (`fondo_frw.py`) da: corriente conservada
J = a³(U_Y−2φ̇U_X); atractor J→0 cuyo cero coincide con los tadpoles de Minkowski
(la protección m₂=m₃=m₄=0 como atractor cosmológico); w=−1 exacto sobre el
atractor; desviaciones diluyen como polvo (a⁻³); la isentrópica U(X+Y²) degenerada
sobre FRW. Este acta establece qué de eso ya existe.

## Lo leído, paper por paper

1. **CCP 1704.00322** — título real "Fluids, Superfluids and Supersolids:
   Dynamics and Cosmology of Self-Gravitating Media", JCAP 09 (2017) 036.
   (La confusión del encargo: "Adiabatic Media Inflation" es 1907.11784, otro
   paper — inflación con fluidos/sólidos, superfluidos explícitamente afuera.)
   - **La corriente YA ESTÁ, como termodinámica**: definen s = U_Y − 2Y·U_X como
     densidad de ENTROPÍA (§3, corriente de Noether del shift Φ⁰→Φ⁰+c) y sobre
     FRW derivan s̄′+3ℋs̄=0 — exactamente nuestra J. PERO: cero "attractor", cero
     "tadpole" (grep), no analizan los puntos fijos, no notan a³s→0 como
     dinámica, no derivan w=−1 asintótico, no conectan con Minkowski.
   - **U(X+Y²) identificada** (§6, clase isentrópica M₀=0; ξ̄=√(X+Y²)=0 sobre
     FRW; "para M₀=0, φ es gauge artefact") — pero el corolario "sobre FRW es
     EXACTAMENTE una CC, sin dinámica de fondo" no está escrito.
   - Masas cosmológicas (ap. B): M₂ ∝ Σn²a^{2(2−n)}U_τₙ — solo U_τₙ. §3.2:
     "For fluids and superfluids where M₂=0, the dynamics of spin 2 modes is
     standard."
2. **BCP 1603.02956, §7-§8 + ap. A**: M₂²M_pl² = Σn²a^{−2(n−1)}U_τₙ y la Tabla
   T3 con M₂²=0 para TODOS los fluidos y superfluidos (la fila U(X,Y) exacta no
   está, pero es subcaso trivial). Sin conexión con la fase protegida de
   Dubovsky (el término "protected phase" no aparece). §8: dark matter entrópico
   δ∝a^{−3c_b²} para U(b,Y) y el ejemplo U=−λb+V(bY) con w: 0→−1 (clase fluido,
   sin X). El germen estructural de la degeneración está en su caso "F₁ y F₂
   idénticamente cero ⟹ N no fijado por el fondo" — sin ejemplos.
3. **CCP 1712.04827 "Self-gravitating Λ-media"**, JCAP 01 (2019) 057: p+ρ=0
   NO-perturbativo impuesto por simetría (mecanismo opuesto al nuestro:
   restricción vs punto fijo dinámico). Los superfluidos con w=−1 los declaran
   INESTABLES a LO (Φ″−k²Φ=0, crecimiento exponencial) — sin considerar la cura
   k⁴ tipo ghost condensate. La solución superfluida de su propia PDE
   (U_Y−2YU_X=0 ⟺ U(X+Y²)) no aparece.
4. **Ghost condensate**: (a) ACLM hep-th/0312099 §2.3-§3: TODO el patrón para su
   clase — corriente ∂_t[a³P′φ̇]=0, atractor P′→0, "T_μν → −g_μν M⁴P: precisely
   the form of a cosmological constant!", y P′~1/a³ gravitando como materia no
   relativista. (b) El "GC dark matter" correcto es **hep-ph/0507120** (ACLM+
   Wiseman, "Dynamics of gravity in a Higgs phase", JHEP 01 (2007) 036), sección
   "Ghost Dark Matter": ρ~Σ~a⁻³, p=ρ²/2M⁴, Σ = carga conservada ("ghostogenesis").
   La sugerencia hep-th/0502189 del encargo era incorrecta (eso es "Black Holes
   in the Ghost Condensate"). (c) Mukohyama hep-th/0607181: "CC + CDM" para el
   GC exacto, y NEC-violation con shift roto.
5. **DTT hep-th/0504067 "Cosmological attractors in massive gravity"**, PRD 72,
   084011 (2005) — EL antecedente crítico (no estaba en el encargo; hallado por
   barrido de autor): en la fase espejo F(X,Wⁱʲ) (m₁²=0, m₂≠0): corriente
   ∂_t(a³√X F_X)=0, atractor F_Z=0 "corresponds to the restoration of an
   additional dilatation symmetry" (usan "attractor" textual), dilución
   generalizada ρ₁∝a^{−(3−1/γ)} ("generalizes the ghost condensate"), y para
   γ=1/3 el de Sitter tardío con la CC como constante de integración (analogía
   unimodular explícita). **Clave: en SU clase el atractor NO coincide con los
   tadpoles de Minkowski** ("solutions which asymptotically approach these
   points correspond to the scale factor going to a finite limit").
6. **KSS 1805.05937 (Khoury–Sakstein–Solomon, "Superfluids and the Cosmological
   Constant Problem", JCAP 2018)**: superfluido U(X,Yb) que degravita una CC;
   m₁²=0 idéntico para toda la clase (fase "hitherto unidentified" de massive
   gravity, UV-insensible, GC-like con ω²=0 a LO → k⁴ a NLO). **Cita textual:
   "it remains to be shown that the Minkowski solution is a dynamical attractor
   for generic initial conditions... which we leave for future work" — y el
   barrido de sus 21 citas muestra que NADIE lo hizo (2018→2026).** Además: KSS
   es pariente directo del paper principal (fila de tabla no identificada,
   m₁²=0 espejo del nuestro m₁²≠0) — DEBE citarse en "The missing row".
7. **di Donato–Pilo 2503.03589 (PRD 2025)**: mantienen la línea "sin componente
   sólida hay inestabilidad exponencial" (lim M₂→0: ω²=−k²) — a LO, sin la cura
   k⁴. Es LA objeción publicada que nuestra sección FRW debe responder
   explícitamente vía el diccionario GC.
8. Barridos INSPIRE declarados: citas de 1704.00322 (34, listadas — ninguna hace
   la cosmología de U(X,Y)); citas de KSS (21 — el future work no se hizo);
   "ghost condensation/condensate" en título (53, 30 revisados); "cosmological
   attractor"+"massive gravity"+"Lorentz" full-text (34, ajenos).

## Veredictos por claim

| Claim nuestro | Veredicto | Detalle |
|---|---|---|
| (i) J y atractor J→0 ⟺ tadpoles | **PARIENTE-CERCANO** | la corriente está en CCP (como entropía, sin dinámica); el patrón atractor está en ACLM y DTT (citar como precedentes directos); **la identificación atractor ⟺ tadpoles-de-Minkowski no está en ningún lado — y en DTT explícitamente NO vale** (esa es nuestra frase) |
| (ii) w=−1 exacto sobre el atractor | **PARIENTE-CERCANO** (frontera) | textual para U(X) en ACLM; γ=1/3 en DTT; para U(X,Y) es extensión de una línea — lo defendible es el PAQUETE (U(X,Y) + tensor sin masa + w=−1 dinámico) |
| (iii) dilución dust a⁻³ | **YA-EXISTE** | GC dark matter (0312099, 0507120 "ghostogenesis", 0607181, DTT generalizado) — citar, no reclamar |
| (iv) U(X+Y²) degenerada en FRW | **PARIENTE-CERCANO** | CCP tienen la clase y ξ̄=0; el corolario cosmológico explícito no está escrito en ninguno de los 4 papers donde brillaría — novedad chica pero real |
| (v) M₂²=0 idéntico sobre FLRW | **YA-EXISTE** | BCP Tabla T3 + CCP §3.2 + Λ-media §5.1 (tres veces, del mismo grupo) — nuestro único ángulo es el énfasis "robustez de la firma a lo largo de la historia FRW", como lectura, no como resultado |

**El hueco citable de oro**: la pregunta "¿el vacío es atractor dinámico?" está
PLANTEADA Y DECLARADA ABIERTA por KSS (2018) para la clase hermana — nuestra
sección FRW la responde para U(X,Y).

**Deber adquirido**: responder explícitamente la objeción de inestabilidad
superfluida de Λ-media/di Donato–Pilo (vía diccionario ghost condensate: el LO
congelado se cura con k⁴, exactamente como en ACLM — y a diferencia de Λ-media,
nuestro w=−1 no es una restricción de simetría sino un punto fijo).

*Acta escrita el mismo día del barrido. Las citas textuales de arriba salen de
los fuentes .tex descargados; re-verificar contra los archivos guardados antes
de transcribirlas a cualquier paper.*
