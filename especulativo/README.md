# ⚠️ Carpeta especulativa — investigación en desarrollo, NO es parte del corpus TCI

**Leé esto antes que nada.** Esta carpeta contiene trabajo exploratorio **en curso** de
la línea "TCI 2.0" (gravedad y materia emergentes de un condensado con orden tensorial).
Se guarda acá como respaldo y bitácora de trabajo, con separación deliberada del resto
del repositorio:

- **NO está validado.** Hay hipótesis vivas, conjeturas declaradas, cálculos
  preliminares con parámetros de prueba, e ideas que ya fueron falsadas y se conservan
  documentadas (la bitácora registra el proceso completo, muertes incluidas).
- **NO es lo que TCI afirma públicamente.** El corpus publicado (paper, sitios, Zenodo)
  vive en la raíz del repo y en las ramas publicadas; nada de esta carpeta se mergea a
  `main` ni aparece en los sitios.
- **Es la parte más especulativa del proyecto**, y se presenta como tal. Si llegaste
  acá navegando: bienvenido, pero calibrá expectativas — esto es un cuaderno de
  laboratorio, no un resultado.

**Política de autoría (2026-07-21).** En toda pieza con formato de publicación (papers,
notas promovidas), el autor es **Nicolás Irigoyen**, único responsable del contenido; la
asistencia de IA (Fable — Claude, de Anthropic: derivaciones, código, bibliografía y
redacción, bajo su dirección) se declara en los agradecimientos/metodología — nunca en la
línea de autoría, que ninguna editorial científica admite para una IA. En las bitácoras y
actas de esta carpeta, "Nicolás & fable" describe el proceso de trabajo (quién hizo qué),
no una autoría formal; los registros históricos no se reescriben.

## Las páginas divulgativas (las caras visuales de esta carpeta)

Todo lo de acá tiene su versión contada para no-físicos, con simulaciones jugables:

- **«El mar y sus nudos»** (la materia): https://irigoyennicolas1991.github.io/ift-theory/mar-y-nudos/
- **«El taller electromagnético del mar»** (el EM): https://irigoyennicolas1991.github.io/ift-theory/taller-electromagnetico/

Ambas llevan el aviso de etapa especulativa y enlazan de vuelta a esta carpeta como
respaldo formal. No están enlazadas desde las sedes públicas de TCI (decisión
deliberada: se comparten en persona).

## Cómo leer esta carpeta (jerarquía — de la raíz a las hojas)

**1. EL TRONCO — `NUCLEO-TCI2-lagrangiano.md`** ⭐ *empezá acá si vas a calcular.*
El lagrangiano maestro de TCI 2.0: el objeto, el funcional con los parámetros de la
casa, los vacíos, el espectro, las fuerzas medidas, la taxonomía de defectos, las
convenciones y los controles obligatorios. Todo cálculo nuevo arranca de este
documento; todo resultado nuevo vuelve a él.

**2. LA BITÁCORA MADRE — `BITACORA-campana-condensado-2026-07-16.md`** ⭐ *empezá acá
si querés la historia.* El registro completo de la campaña (§1–§33): verificaciones
bibliográficas, rutas falsadas con causa citada (el cementerio, con orgullo), erratas
propias documentadas, cálculos y convergencias. Las secciones finales (§29–§33) son
el frente actual.

**3. LOS FRENTES VIVOS** (cada uno con su documento y sus scripts):

| Frente | Documento | Scripts | Estado |
|---|---|---|---|
| **El núcleo** (el lagrangiano borrador y el puente 1.0↔2.0) | `BITACORA-NUCLEO-2026-07-19.md` (§N1-N9) | `nucleo_beta4.py` | 2 calibraciones de 1.0 derivadas (ubicación temporal + σ_Mercurio=0 por Z₂); leyes β=2(1−v²) y m²_r=32γa₀⁴; PE emerge del nudo (p≈1); 7ª y 8ª lápidas + teorema del censo: ni luz ni Newton salen del bulk → todo converge al sector de defectos |
| **La luz del core / la compuerta única** (¿el nudo lleva materia quiral?) | bitácora madre §33-§35 + actas `PASO-A-bisagra-core-2026-07-21.md` y `PASO-B-bdg-core-2026-07-29.md` | `core_indice_toy.py`, `paso_a_bisagra_core.py`, `paso_b_core_input.py`, `paso_b_bdg_core.py` | **COMPUERTA CERRADA DEL LADO VIVO 2026-07-29**: Paso A — core FM+cíclica alineado, pinning duro (ΔE ×40 el número refutado, QA completo); Paso B — BdG del tubo con el campo real: **C_neto = −1** (una rama Majorana quiral por nudo, cuasi-plana, v/v_F≈0.006, quiralidad esclava del winding — espejo +1 exacto, estable en 4 deformaciones, controles §33 todos PASS); mecanismo probado por vaciado (sin relleno cíclico C_neto=0); NO hay 10ª lápida; siguen: fermión de la red (anomaly inflow + Gauss en uniones), tubo→anillo |
| **El sótano** (¿el mar subyace en un fluido más profundo?) | **`NUCLEO-SOTANO-espuma-de-vortones.md`** (tronco) + `HIPOTESIS-SOTANO-fluido-continuo.md` (bitácora) | `sotano_tkachenko.py`, `sotano_anillos_nematica.py`, `sotano_espuma_viva.py`, `sotano_bulk_veredicto.py`, `sotano_bulk_cierre.py` | FORMALIZADO 2026-07-20 con auditoría adversarial (3 escépticos, §10 del tronco): teorema del modelo dipolar (fundamental = laminar nemático uniforme, sin flecha; LT + Ewald certificado contra 3 fuentes a 4-5 cifras) + condiciones H1-H3 declaradas; vortones gordos = almendras (2ª componente elevada a axioma); estructura fina a empaquetamiento denso ABIERTA (rama 1) |
| **EM estático** (dos electricidades) | bitácora madre §30 + `PAPER-borrador-dos-electricidades.md` | `coulomb_del_mar.py` | saldado (teorema de las dos monedas + molécula 1/d³); paper bloqueado hasta el fotón |
| **Campaña m₂=0** (el medio U(X,Y) realiza la fase protegida de Dubovsky) | `campana-m2/` (handoff 2026-07-20 + actas con paneles adversariales; cronología completa en su README) | `campana-m2/**/*.py` (SymPy) | errata BCP (7.6)-(7.7) verificada 5 vías y **CONFIRMADA por L. Pilo (mail 22/7)**; escalar congelado a LO (ω²(p) exacta propia, diccionario ghost condensate); γ=1 exacta por teorema causal; FRW: atractor + identidades tensor/vector; completitud {X,Y} probada; **SELECCIÓN DE ESTADO CERRADA 2026-07-28: TEOREMA DE SUPERSELECCIÓN** (P_aⁱ=0, 4 rutas + verificador adversarial) — la fase predice RG en gravitomagnetismo, la firma apantallada queda suprimida (contrafáctica), cotas LARES a contrafácticas, ventana de Λ al sector escalar; pendiente: mapeo nota 10, sector radiativo |
| **Sótano, paso 0: censo estático (Newton del hueco)** | `SOTANO-PASO0-censo-estatico-2026-07-21.md` (acta) | `verdugo_checks.py`, `verdugo_bjerknes.py` | **LÁPIDA 2026-07-21** (criterio pre-declarado, gatillado): 20 canales censados — ningún canal de la espuma, estático NI Bjerknes, media 1/r universal atractivo; la conservación que estabiliza la espuma prohíbe la carga monopolar; Bjerknes muerta por la pinza espacio-temporal (retardación vs LLR/BBN, teorema propio); la espuma queda como microfundación de las gotas J=2; la gravedad converge (4ª vez) al piso de arriba |

**4. LOS PAPERS EN GESTACIÓN** (borradores técnicos en inglés; NINGUNO sometido a
ningún lado; política de la casa: nada sale de esta carpeta sin OK explícito + las
auditorías que cada uno declara adentro):

| Paper | Archivo | Estado |
|---|---|---|
| **La espuma nemática** — "Inverted dipolar order: the laminar nematic ground state of vortex-ring arrays" | `PAPER-espuma-nematica-DRAFT.md` | **draft v0.9 completo y auditado** (física de condensados standalone — se defiende sin TCI); bloqueos: cotas con redes con base (obligatorio tras el colateral del hielo 2026-07-21), barrido INSPIRE, canal |
| **El censo del spin-2** — "Static long-range forces in a spin-2 condensate: a refraction bound, a symmetry-protected perihelion constraint, and a no-go census" | `PAPER-borrador-censo-nucleo.md` | draft v2 completo (incorpora las 17 correcciones del auditor de overclaims); pendiente v3: auditorías de claims y de citas (declaradas en el propio paper) |
| **El gravitón** — "The phonon as the second graviton polarization: exactly two massless TT modes in the D₄ biaxial-nematic phase of a spin-2 superfluid" | `PAPER-borrador-graviton-dos-polarizaciones.md` | **draft v0.1** (2026-07-21): primera escritura de los resultados §14–§17/§22 — las dos polarizaciones TT sin masa y el mecanismo fonón-U(1), el candidato a aporte original del programa; SIN auditoría todavía (lista de bloqueo adentro) |
| **Las dos electricidades** — "Two decoupled Coulomb sectors in the vortex electrodynamics of a tensorial superfluid" | `PAPER-borrador-dos-electricidades.md` | esqueleto (claims fijados, bloqueos técnicos saldados); en pausa hasta que haya un cálculo del fotón |
| **La fila que falta** — "The missing row: unrestricted internal diffeomorphisms, the protected phase of Lorentz-violating massive gravity, **and a superselection theorem for frame dragging**" (retitulado 2026-07-28; era "…and a screened frame-dragging signature") | `PAPER-borrador-missing-row-UXY.md` | **draft v0.7** (2026-07-28): el paper de la campaña m₂=0 — standalone (se defiende sin TCI); las 5 patas técnicas (diccionario, escalar, acople, FRW, selección de estado) pasaron paneles adversariales (actas en `campana-m2/`); el TEXTO lleva 3 auditorías (31+12+30 hallazgos aplicados); v0.7 integra el TEOREMA DE SUPERSELECCIÓN — la firma apantallada queda suprimida y las cotas LARES pasan a contrafácticas, §8 reescrita; errata BCP confirmada por Pilo (22/7, cita formal pendiente de permiso); incluye la medición Nature jul-2026 de LARES-2 con la disputa citada; falta: 4ª auditoría de texto (sobre la reescritura) + OK de canal; blanco: arXiv hep-th/gr-qc + PRD/JCAP |

**5. LAS CARAS VISIBLES** (divulgación semi-oculta, fuentes acá):
`libro2/` (fuente de /mar-y-nudos/), `em/` (fuente de /taller-electromagnetico/),
`sotano-web/` (fuente de /sotano-del-mar/),
`eter-sin-viento/` (fuente de /eter-sin-viento/ — el teorema de superselección contado
para humanos, 5 sims con física verificada por su `test_fisica.js`; construida 2026-07-28
desde `campana-m2/BRIEFING-DIVULGACION-ETER-SIN-VIENTO-2026-07-28.md`, pendiente OK de
Nico para publicar en main),
`LIBRO2.md` + `LIBRO2-esqueleto.md` (el texto completo del libro 2, en el cajón).

**6. EL RESTO DE LOS SCRIPTS** (cada uno nació de una batalla; la sección de la
bitácora que lo explica va al lado): `espectro_biaxial_real/complejo/_3p2.py` (§14-16,
las dos polarizaciones TT), `espectro_ciclico.py` (§26), `anisotropia_mapa.py` (§22),
`monometricidad_test.py` (§23, 5ª lápida), `anillos_toy.py` (§21),
`scaling_cuadrupolo.py` (§28), `binaria_del_mar.py` + `analiza_binaria.py` (§31),
`coulomb_del_mar.py` (§30), `nucleo_beta4.py` (bitácora del núcleo),
`sotano_*.py` (doc del sótano).

Todos corren con Python 3 + numpy, sin más dependencias (`python <script>.py`).

## El estado en una línea (2026-07-20)

Hipótesis de trabajo: *un superfluido con orden cuadrupolar interno soldado al espacio
(fase D₄-BN del ³P₂) tiene como modos sin masa exactamente las dos polarizaciones
tensoriales de una onda gravitacional — una es el Goldstone rotacional, la otra es el
fonón vestido; la luz y la materia NO viven en ese mar liso sino en los núcleos de sus
nudos (tres falsaciones independientes convergen ahí); y el mar mismo podría subyacer
en un fluido perfecto más profundo cuyos anillos de vórtice fabrican las gotas J=2
localmente (calculado) aunque todavía no el vacío uniforme.* Verificaciones, deudas y
criterios de muerte: en las bitácoras. Reglas de la casa: honestidad brutal, toda
derrota se documenta el mismo día, ningún "exactamente" sin ecuación de respaldo.
