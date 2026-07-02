# Campo fuerte: la predicción propia de TCI (donde se separa de Einstein)

**Nota de resultados — 2 de julio de 2026** · rama `desarrollo-fable`

## La idea en una línea

Todo el sistema solar prueba la gravedad hasta segundo orden en φ = GM/(c²r), y ahí TCI ≡ RG (lo establecimos en §7.4–7.5). La primera diferencia física aparece a **tercer orden** — es decir, cerca de objetos compactos. Y hay un lugar donde eso se fotografía: **la sombra de un agujero negro**.

## La métrica de campo fuerte de TCI

El sistema solar fijó 𝒢 = 1+4φ y 𝓕 = 1 a primer orden. Para el campo fuerte hace falta la completación de 𝒢, y el principio ya lo tenemos: la misma composición multiplicativa que dio E = mc²e^(−φ) (la equivalencia local, §7.5), aplicada a la inercia del medio, da 𝒢 = e^(4φ). La métrica efectiva resulta:

$$ds^2 = e^{-2\phi}c^2dt^2 - e^{+2\phi}(dr^2 + r^2 d\Omega^2), \qquad \phi = \frac{GM}{c^2 r}$$

Dato de color con historia: esta es la **métrica exponencial de Yilmaz (1958)** — TCI la obtiene desde un mecanismo físico concreto (el medio I), no como postulado. Honestidad: la completación exponencial es la *mínima/natural*, no está forzada por datos del sistema solar; otras completaciones cambiarían los números de campo fuerte (no los del sistema solar). Es una predicción condicional pero nítida y falsable.

**Rasgo estructural fuerte: no hay horizonte de eventos.** g₀₀ = e^(−2φ) nunca se anula. En vez de horizonte hay una superficie de corrimiento al rojo que crece superexponencialmente: la materia que cae se "apaga" — observacionalmente negro, estructuralmente distinto.

## Predicción 1: sombras 4.6% MÁS GRANDES que en RG

Esfera de fotones (condición de Fermat, d/dr[r·n(r)] = 0, con n = e^(2φ)):

- r_fotones = 2GM/c² (coordenada isótropa)
- Parámetro de impacto crítico: **b_c = 2e·GM/c² ≈ 5.4366 GM/c²**
- RG: b_c = 3√3·GM/c² ≈ 5.1962 GM/c²

$$\frac{b_c^{TCI}}{b_c^{RG}} = \frac{2e}{3\sqrt{3}} = 1.0463 \;\Rightarrow\; \textbf{+4.63\%}$$

**Estado observacional:** el Event Horizon Telescope midió las sombras de M87* (2019) y Sgr A* (2022) con precisión de ~±10% respecto al tamaño esperado por RG. TCI (+4.6%) está **viva hoy** — dentro del error — y el **next-generation EHT (~1% proyectado) la decide**: o la confirma o la mata. Eso es una teoría haciendo su trabajo.

## Predicción 2: el ISCO gira 6.9% más lento

La órbita circular estable más interna (borde interno de los discos de acreción):

| | RG | TCI | Δ |
|---|---|---|---|
| b_c (sombra) | 5.19615 | 5.43656 | **+4.63%** |
| GM·Ω_isco/c³ | 0.06804 | 0.06333 | **−6.92%** |

Afecta la temperatura del borde interno del disco y las oscilaciones cuasi-periódicas (QPOs) de binarias de rayos X — segundo discriminador independiente.

## Verificación numérica

`campo_fuerte.py` (en este directorio): (a) minimización de F(r) = n·r, (b) **integración directa de rayos nulos** con bisección del umbral de captura — ambos métodos coinciden a 6 cifras; (c) ISCO por minimización de L²(r). Control de calidad: el mismo código reproduce los valores exactos de RG (3√3 = 5.196152 ✓, r_isco = 6M en Schwarzschild ✓, Ω_isco = 6^(−3/2) ✓).

## Lo que NO cambia (y por eso TCI sigue viva)

- Estrella S2 alrededor de Sgr A* (GRAVITY): órbita a φ ~ 10⁻⁴ → orden post-newtoniano → TCI ≡ RG ✓
- Todos los tests del sistema solar: idénticos hasta O(φ²) ✓

## Pendientes de este frente

Ringdown/ondas gravitacionales de fusiones (requiere teoría de perturbaciones sobre la métrica exponencial), fenomenología de acreción sin horizonte, deflexión de luz a segundo orden (~1 μas, futuro astrométrico).
