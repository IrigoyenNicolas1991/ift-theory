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

## Scripts de verificación numérica

Todos con controles de calidad: el mismo código reproduce los valores exactos de la
relatividad general antes de calcular los de TCI.

- [`perihelio.py`](perihelio.py) — integra la órbita de Mercurio en cuatro métricas candidatas (RK4, 100 órbitas)
- [`campo_fuerte.py`](campo_fuerte.py) — sombra (rayos nulos + bisección de captura) e ISCO
- [`ringdown.py`](ringdown.py) — modos cuasinormales por correspondencia con el anillo de luz

## Marcador honesto

**Calibrado (2 números):** β = 4 (eclipse 1919) y su ubicación temporal (Mercurio).
**Reproducido/predicho (10 observables):** E=mc², Newton, E(v)=γmc², redshift/GPS, deflexión 1.75″, Shapiro, no-dispersión, perihelio, Nordtvedt, geodética.
**Predicción propia falsable:** sombras +4.6% / ringdown −4.4% (ngEHT y detectores de 3ª generación deciden).
**Mayor riesgo abierto:** el sector de radiación gravitacional. Estado: teorema no-go probado para el acoplamiento ingenuo; canal de corte identificado (la reacción inercial de masa añadida, que radia a 2Ω con estructura cuadrupolar). Quedan los dos cálculos decisivos: patrones de antena vs spin-2 observado, y luminosidad total vs el decaimiento orbital de Hulse-Taylor (~0.2%).
