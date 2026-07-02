# El sector galáctico, esta vez en serio: test RAR con datos SPARC reales

**Nota de resultados — 2 de julio de 2026** · rama `desarrollo-fable`

## Por qué esta nota existe

En el Drive del proyecto había un paper previo ("ley universal v∞ = √2·c_s", oct 2025, generado con un modelo de IA anterior) que afirmaba validar TCI en galaxias con error de 0.036%. Al auditarlo se encontró: **circularidad** (c_s extraído de la curva de rotación con la misma ecuación que luego "predice" v∞ — la relación v = √2·σ es además la identidad textbook de la esfera isoterma singular), **precisión imposible** (0.04% con datos de ±3–8% de error), y **datos fabricados** (valores de SPARC falsos — NGC3198 real ~150 km/s, listada a 100.5; filas duplicadas idénticas; galaxias elípticas en una muestra "de espirales"). Ese paper queda **retirado del corpus de TCI**. Esta nota lo reemplaza con el test que correspondía hacer.

## El test honesto

**Datos**: catálogo SPARC real (Lelli, McGaugh & Schombert 2016), descargado de la fuente (`astroweb.cwru.edu/SPARC/`), 175 galaxias. Cortes estándar de McGaugh-Lelli-Schombert 2016 (MLS16): inclinación > 30°, calidad ≠ 3, error de velocidad < 10%. Resultado: **2681 puntos de 144 galaxias** (MLS16: 2693/153 — muestra esencialmente reproducida). M/L = 0.5 (disco) y 0.7 (bulbo) a 3.6 μm, los valores estándar.

**Test**: la Relación de Aceleración Radial (RAR) — el resultado observacional central de la dinámica galáctica moderna: la aceleración observada g_obs = V²/R contra la aceleración bariónica newtoniana g_bar, punto por punto.

**Script**: [`rar_test.py`](rar_test.py) (en esta carpeta, reproducible de punta a punta).

## Resultados

| Modelo | Dispersión (dex) | Veredicto |
|---|---|---|
| Newton sin materia oscura (= **TCI lineal actual**) | 0.514, con sesgo sistemático de **5.2×** en g < 10⁻¹¹ m/s² | ✗ falla |
| Función RAR con a₀ ajustado | a₀ = 1.17×10⁻¹⁰ m/s², dispersión **0.132** | ✓ (reproduce MLS16: 1.20×10⁻¹⁰, ~0.13 dex) |
| Función RAR con a₀ = c√(Gρ₀) de TCI | dispersión 0.133 | ✓ pero **ρ₀ fue calibrado de esta misma escala: no es predicción** |

## Lo que esto significa, sin maquillaje

1. **TCI, tal como está formulada, NO explica las curvas de rotación.** El campo de vacancia es Yukawa con alcance cosmológico → a escala galáctica es Newton puro → falla por un factor 5 donde la materia oscura domina. Esto queda declarado como límite actual de la teoría.
2. **La RAR es real y la reprodujimos independientemente** desde los datos crudos — así se ve una validación de verdad: 0.13 dex de dispersión (un factor ~1.35 típico), no un 0.036% de fantasía.
3. **La perla sobrevive, pero con su etiqueta correcta**: a₀ = c√(Gρ₀) conecta la escala galáctica con la densidad del medio (y por ella con la energía del vacío y con cH₀). Como ρ₀ se fijó *desde* a₀, hoy es una **coincidencia estructural sugerente**, no una predicción. Se convertiría en física si un mecanismo la derivara.

## El camino para que TCI gane este sector (dirección concreta)

La fenomenología que los datos piden es exactamente la de AQUAL/MOND: la respuesta gravitacional se modifica cuando los *gradientes* de campo caen por debajo de a₀/c². En lenguaje del medio: **el medio I debería tener elasticidad sub-lineal a deformaciones ultra-pequeñas** — su rigidez efectiva K(|∇φ|) ∝ |∇φ| cuando |∇φ| ≪ a₀/c². Esto no es ad hoc en espíritu: los medios granulares y vítreos reales exhiben exactamente ese tipo de elasticidad anómala a micro-deformaciones. El programa: derivar esa respuesta de la discretitud del medio, y entonces (a) la RAR completa emergería de la ecuación de campo, y (b) a₀ = c√(Gρ₀) pasaría de coincidencia a predicción. Ese es el próximo frente galáctico serio.

## Reproducibilidad

```
curl -O https://astroweb.cwru.edu/SPARC/MassModels_Lelli2016c.mrt
curl -O https://astroweb.cwru.edu/SPARC/SPARC_Lelli2016c.mrt
python rar_test.py
```
