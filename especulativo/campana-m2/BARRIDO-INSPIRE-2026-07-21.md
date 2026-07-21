# Barrido INSPIRE de novedad — campaña m₂=0 (acta)

**2026-07-21 · Fable · registro de las búsquedas que respaldan la sección
"Novelty search" del paper `../PAPER-borrador-missing-row-UXY.md`.**
Método: API de INSPIRE-HEP (`inspirehep.net/api/literature?q=...`), búsquedas
full-text (`ft "..."`), resultados leídos por título (y por abstract donde se
indica). Complementa —no reemplaza— el barrido de la sesión externa del
2026-07-20 (handoff, sección "Novedad"), que cubrió la identificación U(X,Y) y
la vecindad CCP por otra vía.

## Las queries y sus resultados

**Q1. `ft "unrestricted internal diffeomorphisms"` → 0 hits.**
La frase que nombra la simetría de la fila no existe en el full-text indexado.

**Q2. `ft "unrestricted spatial diffeomorphisms"` → 3 hits:**
1309.1119 (Weyl anomalies in shape dynamics), 1211.5878 (FAQ about Shape
Dynamics), 2505.13548 (Alternative Action for Generalized Unimodular Gravity).
Veredicto: los tres usan la frase para difeomorfismos del ESPACIO FÍSICO
(shape dynamics / unimodular) — otro objeto; ninguno trata difeos del espacio
interno de los Stückelberg de un medio.

**Q3. `ft "shear rigidity" AND ft "graviton mass"` → 2 hits:**
2109.11325 ("Crystal gravity"), 1904.01419 ("Gapped momentum states").
Abstract de 2109.11325 revisado: no enuncia el lema (ni el marco de masas
m₀…m₄ ni la condición de protección). Ambos citados en el paper como parientes.

**Q4. `ft "graviton mass" AND ft "shear modulus"` → 29 hits** (primera página
de 25 revisada por título): casi todos holografía sólida / axion model
(1711.03100, 1903.02859, 1708.08477, 1910.06331, 1808.05391, 2005.06482,
2410.10161, 1905.09164, 1905.09488, 2001.05737, 1910.05281, **1510.09089
"Solid Holography and Massive Gravity"**, 2311.16423, 1801.08627, 1908.02667,
1807.10530, 2108.13124, 2101.01892, 1610.02681, 1708.04997, 2502.01687,
2005.01725, más 2404.03872 y los de Q3). Veredicto: la relación masa del
gravitón (bulk) ↔ elasticidad/fonones (boundary) es un tema ESTABLECIDO en
holografía — por eso el paper la cita como pariente [17] — pero ninguno
enuncia "protección de m₂=0 ⟺ medio fluido" dentro del diccionario
BCP/fases de Dubovsky.

**Q5. `ft "Lense-Thirring" AND ft "massive gravity"` → 103 hits** (primera
página de 25 revisada por título): tests genéricos de gravedad, cotas de m_g
por lensing/S2/púlsares, dRGT-AdS, etc. Ningún título sobre apantallamiento
del frame dragging en fases de gravedad masiva o LV.

**Q6. `ft "gravitomagnetic" AND ft "Meissner"` → 107 hits** (primera página de
25 revisada por título): la línea "superconductores y gravitomagnetismo" de
laboratorio (Tajmar–de Matos y derivados). El eco conceptual más cercano:
**cond-mat/0602591** ("Gravitomagnetic London moment and the graviton mass
inside a superconductor") — claim de laboratorio no replicado, citado en el
paper con ese calificativo [19]. Nada sobre Lense–Thirring astronómico
apantallado en una fase de gravedad masiva.

**Q7. `refersto:recid:659064 AND de > 2023-12-31` → 19 hits** (recid 659064 =
Dubovsky hep-th/0409124; TODOS listados y revisados por título):
2604.02402 (dRGT-AdS termodinámica) · 2603.03433 (COSMIC WISPers white paper) ·
2602.09089 (WISPedia) · [sin arXiv] (Lyapunov/AdS BHs) · 2511.00877 (interiores
de BHs holográficos sólidos) · [sin arXiv] (massive gravitons, atmospheric
turbulence and RATs — interferometría atómica) · 2507.03103 (Open System
Approach to Gravity) · 2412.14282 (massive graviton dark matter, atom
interferometers) · 2411.12528 (imágenes holográficas, LSB massive gravity) ·
2411.11118 y 2410.15056 (Degrees of Freedom of New General Relativity) ·
2410.04848 (STEGR internal-space) · 2409.03104 (Very Special Relativity) ·
2407.20688 (Hamiltoniano, violación espontánea de simetría) · [sin arXiv]
(pseudo-SUSY Dirac en Schwarzschild) · 2407.06572 (spin-2 masivo efectivo por
SSB de escalar) · 2404.06584 (Khronon relativista / MOND) · 2404.02095
(Lyapunov/AdS) · [sin arXiv] (dinámica cuántica no perturbativa en de Sitter).
**Veredicto: ninguno construye un medio que realice la fase (72) ni toca la
fila U(X,Y).**

## Limitaciones declaradas (deber de honestidad)

1. En Q4–Q6 (29/103/107 hits) se revisó por título la primera página (25) de
   cada query, no el full-read de todos los hits — suficiente para "no hay un
   cuerpo de literatura sobre esto", insuficiente para un negativo absoluto.
2. Las lecturas de resultados pasaron por resumen automático del contenido de
   cada página de la API (mismo método en todas).
3. Quedan variantes léxicas por barrer si el paper avanza a submission:
   "volume-preserving internal diffeomorphisms" (contraste), "protected phase"
   + massive gravity, sinónimos de counterflow, y el barrido de citas de BCP
   1603.02956 análogo al Q7.
4. El barrido de la errata BCP (2026-07-21, acta propia) y el de la sesión
   externa (2026-07-20) son registros separados que este acta complementa.

*Escrita el mismo día de las búsquedas, como manda la casa. Si alguien
encuentra prior art que estas queries no vieron, la sección de novedad del
paper se corrige y este acta se enmienda diciéndolo.*
