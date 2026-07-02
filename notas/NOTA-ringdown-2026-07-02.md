# Ringdown: la campanada del agujero negro en TCI

**Nota de resultados — 2 de julio de 2026** · rama `desarrollo-fable`

## Qué es el ringdown (para leer tranquilo)

Cuando dos agujeros negros chocan y se funden, el agujero resultante queda "abollado" por un instante — y como una campana golpeada, vibra hasta calmarse, emitiendo ondas gravitacionales con un tono y una duración característicos. Eso es el *ringdown*. LIGO lo escucha. El tono y el amortiguamiento dependen solo de la geometría del agujero final → son un test directo de la métrica en campo fuerte.

## El cálculo (aproximación eikonal, correspondencia con el anillo de luz)

Resultado estándar (Cardoso et al. 2009): las frecuencias cuasinormales de una métrica estática se leen del anillo de fotones:

$$\omega \approx \ell\,\Omega_c - i\,(n+\tfrac12)\,\lambda_L, \qquad \Omega_c = \frac{c}{b_c}, \quad \lambda_L = \kappa\,\Omega_c$$

donde κ² = H″/2 mide la inestabilidad del anillo de luz. Resultado numérico (script `ringdown.py`, con control RG exacto):

| | RG | TCI | Δ |
|---|---|---|---|
| Ω_c (tono) | 0.19245 | 0.18394 | **−4.42%** |
| κ (forma del decaimiento) | 1.000000 | 1.000000 | 0 |
| λ_L (amortiguamiento) | 0.19245 | 0.18394 | **−4.42%** |

Dato lindo: **κ = 1 exacto en las dos métricas** — la relación λ_L = Ω_c de Schwarzschild sobrevive intacta en la métrica exponencial. Todo el corrimiento viene de b_c.

## La firma correlacionada (esto es lo potente)

$$\frac{f_{ring}^{TCI}}{f_{ring}^{RG}} = \left(\frac{b_c^{TCI}}{b_c^{RG}}\right)^{-1} = \frac{3\sqrt3}{2e} = 0.9558$$

TCI no predice dos números sueltos: predice que **sombra y ringdown se mueven juntos, con cocientes inversos**. Sombra +4.63% ⟺ tono −4.42% ⟺ amortiguamiento −4.42%. Si EHT ve la sombra grande pero LIGO no ve el tono bajo (o viceversa), TCI muere. Un solo parámetro geométrico, tres observables de campo fuerte.

Ejemplo físico (remanente tipo GW150914, 62 M☉): RG ~201 Hz / 1.59 ms; TCI ~192 Hz / 1.66 ms (eikonal ℓ=2; el valor absoluto tiene ~15% de error sistemático, pero el *cociente* entre teorías es robusto).

## Estado observacional y caveats honestos

- Los tests actuales de consistencia inspiral-vs-ringdown de LIGO/Virgo tienen precisión ~10-20% → **−4.4% está vivo, pero presionado**. Detectores futuros (Einstein Telescope, Cosmic Explorer) llegan a ~1%.
- El cálculo usa la métrica estática sin rotación; los remanentes reales rotan (Kerr) — la extensión rotante de la métrica exponencial es trabajo pendiente.
- Confrontar de verdad con LIGO exige la forma de onda completa (inspiral + fusión + ringdown), no solo el ringdown.

## El riesgo estructural más grande de TCI (que quede escrito)

Las ondas gravitacionales observadas son **tensoriales** (patrón cuadrupolar, 2 polarizaciones tipo spin-2) y el púlsar de Hulse-Taylor confirma la pérdida de energía cuadrupolar de la RG al 0.3%. Un medio **fluido** solo soporta ondas longitudinales (escalares) → sería fatal. La salida estructural: el medio I debe ser un **sólido elástico** — los sólidos soportan ondas de corte *transversales* (2 polarizaciones), y GW170817 (velocidad de OG = c a 10⁻¹⁵) fija su módulo de corte en ρ₀c². Que los patrones de antena de esas ondas de corte reproduzcan los observados es LA pregunta abierta decisiva de la teoría. El acoplamiento universal (T ∝ E/c²) suprime la radiación dipolar — necesario para Hulse-Taylor — pero la normalización cuadrupolar hay que calcularla.
