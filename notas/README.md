# Notas de trabajo — TCI / Intangible Field Theory

Bitácora del desarrollo en la rama `desarrollo-fable`. Cada nota está escrita en español,
en orden de lectura, con la honestidad como regla: qué se derivó, qué se calibró con datos,
qué queda abierto y qué podría matar la teoría.

| # | Nota | Qué resuelve | Resultado en una línea |
|---|------|--------------|------------------------|
| 1 | [Deflexión de la luz](NOTA-deflexion-luz-2026-07-02.md) | El problema Nordström: la teoría lineal no curva la luz | β = 4 (calibrado con el eclipse de 1919) → 1.75″ ✓ y el retardo de Shapiro sale gratis |
| 2 | [Perihelio: scoping](NOTA-perihelio-scoping-2026-07-02.md) | Plantea el peligro: la fórmula original daba 50″/siglo (excluido) | La condición de supervivencia era exacta: +½φ² en g₀₀ |
| 3 | [Perihelio: resultado](NOTA-perihelio-resultado-2026-07-02.md) | Mercurio, 42.98″/siglo | La equivalencia aplicada localmente da E = mc²·e^(−φ); la no linealidad vive en el sector temporal |
| 4 | [Campo fuerte](NOTA-campo-fuerte-2026-07-02.md) | Dónde TCI se separa de Einstein | Sombras de agujeros negros **+4.63%**, ISCO −6.9%; sin horizonte de eventos |
| 5 | [Ringdown](NOTA-ringdown-2026-07-02.md) | La "campanada" del agujero negro fusionado | Tono y amortiguamiento **−4.42%**, anticorrelados con la sombra; y el riesgo Hulse-Taylor documentado |
| 6 | [Polarización](NOTA-polarizacion-2026-07-02.md) | ¿TCI radia el tipo de onda que LIGO observa? | **Teorema no-go** para el acoplamiento de densidad; la salida: el mecanismo de la inercia (masa añadida) radia ondas de corte cuadrupolares a 2Ω |
| 7 | [Antenas: la falsación](NOTA-antenas-falsacion-2026-07-02.md) | El cálculo decisivo de los patrones de antena | **Resultado adverso**: las ondas de corte son modos vectoriales (spin-1); LIGO midió spin-2 con Bayes >10²⁰ → el sector de radiación elástico-lineal queda falsado. Lo que sobrevive y la cirugía necesaria, documentados |
| 8 | [Galaxias: test RAR honesto](NOTA-galaxias-RAR-2026-07-02.md) | El sector galáctico con datos SPARC reales (2681 puntos, 144 galaxias) | Se retira un paper previo con datos fabricados; la RAR real se reproduce (a₀=1.17×10⁻¹⁰, 0.13 dex); **TCI lineal falla 5× en baja aceleración** (declarado); a₀ = c√(Gρ₀) queda como coincidencia calibrada, no predicción; camino: elasticidad sub-lineal del medio |
| 9 | [TCI 2.0: sustrato tensorial](NOTA-tci2-sustrato-tensorial-2026-07-11.md) | ¿Hay salida a la falsación de la nota 7? Buceo bibliográfico verificado en tres frentes | **Sí, documentada**: el no-go vale para medios de *desplazamientos*; medios con orden tensorial tienen modos spin-2 reales y medidos (³He-B desde 1980; helicidad ±2 en Hall cuántico, *Nature* 2024). Reformulación propuesta: condensado con orden tensorial; el sector escalar φ sobrevive entero. Obstáculos con nombre: masa cero (ruta Goldstone) y monometricidad (objeción de Carlip — donde TCI tiene una ventaja estructural a probar) |
| 10 | [TCI 2.0: el bug es la feature](NOTA-tci2-bug-es-feature-2026-07-11.md) | Los 3 modos sobrantes del quinteto spin-2 (helicidades 0, ±1) vs los 2 que LIGO ve | **Resuelto en principio, con literatura sana**: en gravedad masiva con marco privilegiado existe la fase m₂=0 (Dubovsky 2004) — helicidad ±2 exactamente sin masa a velocidad c, sobrantes no-dinámicos, sin ghosts. El marco propio del medio —el "defecto" histórico de TCI— es la licencia que lo permite. El diccionario medio↔gravedad-masiva ya existe (Ballesteros-Comelli-Pilo 2016). **Territorio virgen verificado**: nadie construyó la fase m₂=0 desde un parámetro de orden tensorial |
| 11 | [TCI 2.0: scoping del condensado](NOTA-tci2-condensado-scoping-2026-07-16.md) | El plan de construcción de TCI 2.0, con checkpoints y criterios de muerte | **Un cálculo, tres frutos**: del espacio de orden del condensado cuadrupolar salen (1) la fase m₂=0 (gravedad), (2) la taxonomía de defectos topológicos (conjetura: partículas = "nudos" — cuantización de carga, antipartículas e identidad, gratis), (3) la radiación de una binaria de defectos contra Hulse-Taylor (0.16%) como examen final. Apuesta declarada: la simetría protectora de m₂=0 es rotacional, no traslacional ("gotas, no flechas"). Piedras declaradas antes de empezar: los J=2 de laboratorio son masivos, inverse Higgs, isotropía del CMB, Bell queda donde está |
| 12 | [TCI 2.0: Paso A ejecutado](NOTA-tci2-paso-A-2026-07-19.md) | Elegir el patrón de ruptura del condensado (checkpoints i-iii de la nota 11) | **SL(3)×SO(3) → SO(3) diagonal**: el cuadrupolo sale como Goldstone (5 = J=2 irreducible, verificado con Schur) y hay candidato a teorema de protección — la fluidez interna SL(3) prohíbe todo potencial del sector de forma ⇒ m₂=0 por simetría [13/13 chequeos sympy]. Mina calculada antes de pisarla: el invariante mixto Tr(Q⁻¹B) con el sector fluido regenera la masa — el Paso B queda afilado en esa sola pregunta, con 3 rutas declaradas. Precedentes honestos que matizan el "territorio virgen": Borisov-Ogievetsky 1974 (métrica como Goldstone afín), Gromov-Son 2017 (Q unimodular en Hall cuántico, spin-2 masivo) |

## Scripts de verificación numérica

Todos con controles de calidad: el mismo código reproduce los valores exactos de la
relatividad general antes de calcular los de TCI.

- [`perihelio.py`](perihelio.py) — integra la órbita de Mercurio en cuatro métricas candidatas (RK4, 100 órbitas)
- [`campo_fuerte.py`](campo_fuerte.py) — sombra (rayos nulos + bisección de captura) e ISCO
- [`ringdown.py`](ringdown.py) — modos cuasinormales por correspondencia con el anillo de luz
- [`rar_test.py`](rar_test.py) — test de la Relación de Aceleración Radial sobre el catálogo SPARC real (datos públicos, descarga incluida)
- [`paso_a_simetrias.py`](paso_a_simetrias.py) — verificaciones del patrón de ruptura de TCI 2.0: coset J=2 irreducible, teorema de no-potencial, espectro sin masa del sigma model, y la masa regenerada por el acople mixto (la mina del Paso B)

## Marcador honesto

**Calibrado (2 números):** β = 4 (eclipse 1919) y su ubicación temporal (Mercurio).
**Reproducido/predicho (10 observables):** E=mc², Newton, E(v)=γmc², redshift/GPS, deflexión 1.75″, Shapiro, no-dispersión, perihelio, Nordtvedt, geodética.
**Predicción propia falsable:** sombras +4.6% / ringdown −4.4% (ngEHT y detectores de 3ª generación deciden).
**Sector falsado (2026-07-02):** la radiación gravitacional en forma elástico-lineal. Un medio elástico isótropo solo produce ondas escalares (P) y vectoriales (S); LIGO/Virgo midieron spin-2 puro con factores de Bayes >10²⁰ (GW170817). Los sectores exitosos no dependen de esta pieza y siguen en pie. **Problema abierto principal:** la completación spin-2 — el medio necesitaría microestructura cuadrupolar (cirugía mayor, no parche). Lección posible: los datos radiativos exigen un campo spin-2 dinámico, y eso converge a Einstein; el medio I quedaría como explicación del sustrato de los sectores estático, óptico y orbital.
**Dirección abierta (2026-07-11, nota 9):** la cirugía tiene precedente real — medios con parámetro de orden tensorial (helio-3 B, Hall cuántico fraccionario) tienen modos spin-2 observados; la reformulación "TCI 2.0 = condensado con orden tensorial" conserva todo el sector escalar y hereda dos problemas con nombre: masa cero del modo ±2 (ruta Goldstone) y una sola velocidad límite para todo (monometricidad).
