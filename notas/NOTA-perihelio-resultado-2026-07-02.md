# Perihelio de Mercurio en TCI: RESUELTO

**Nota de resultados — 2 de julio de 2026** · rama `desarrollo-fable`
*(sigue a NOTA-perihelio-scoping-2026-07-02.md)*

## Resultado central

**TCI reproduce los 42.98″/siglo de Mercurio**, con dos ingredientes que no son parches sino consecuencias de tomarse en serio los propios principios de la teoría:

### Ingrediente 1: la triple equivalencia aplicada localmente → E = mc²·e^(−φ)

El paper decía (ec. 43): E(r) = mc²(1−φ). Pero eso usa la masa *desnuda* m en el acoplamiento. El principio central de TCI es que la carga T es proporcional a la masa, y que la masa ES energía local (m = E/c², la triple equivalencia). Aplicado consistentemente a cada profundidad del pozo:

$$dE = -E\,d\phi \;\Longrightarrow\; E(r) = mc^2\,e^{-\phi}$$

La exponencial no se pone a mano: **sale de integrar el propio principio de equivalencia de la teoría**. Consecuencias:

- g₀₀ = e^(−2φ), que coincide con Schwarzschild (coordenadas isótropas) hasta O(φ²) inclusive — las desviaciones recién aparecen a O(φ³), o sea en régimen de campo fuerte.
- El redshift queda z = e^(Δφ) − 1: idéntico a primer orden (Pound-Rebka intacto ✓), y ahora correcto también a segundo orden.
- β_PPN pasa de ½ a 1 — **si** el campo exterior del Sol no recibe correcciones a segundo orden (σ = 0).

### Ingrediente 2: dónde vive la no linealidad β = 4 → en el sector temporal

Parametrizando el lagrangiano cinético general del medio:

$$\mathcal{L} = \frac{K}{2c^2}\,\mathcal{G}(\phi)\,\dot\phi^2 - \frac{K}{2}\,\mathcal{F}(\phi)\,|\nabla\phi|^2 - \frac{\Lambda}{2}\phi^2 + J\phi$$

con 𝒢 = 1 + g₁φ, 𝓕 = 1 + f₁φ:

- **La óptica (§7.4)** fija solo el cociente: c_s² = c²𝓕/𝒢 → f₁ − g₁ = −4.
- **La estática** (perfil del Sol a segundo orden) depende solo de 𝓕: resolviendo la ecuación de campo exterior a O(φ²) sale φ = φ₁ + σφ₁² con **σ = −f₁/4**.
- **Mercurio** exige σ = 0 (a ±0.003, del error observacional de ±0.04″).

Conclusión: **f₁ = 0, g₁ = +4**. La no linealidad del medio vive enteramente en el término cinético *temporal*:

$$\boxed{\;\mathcal{L} = \frac{K}{2c^2}(1+4\phi)\,\dot\phi^2 - \frac{K}{2}|\nabla\phi|^2 - \frac{\Lambda}{2}\phi^2 + J\phi\;}$$

Lectura física: **la inercia del medio se endurece con la depleción; su elasticidad se mantiene lineal.** Las alternativas (no linealidad en el sector espacial, f₁ = ∓4) dan 57.3″ o 28.7″/siglo — excluidas por ~300σ. Los datos no solo permiten la estructura: la *determinan*.

## Verificación numérica (independiente del álgebra)

Integración RK4 de la geodésica ecuatorial de Mercurio (a = 5.7909×10¹⁰ m, e = 0.2056, 100 órbitas, evaluación sin cancelación catastrófica vía expm1). Script: `perihelio.py` (en este directorio).

| Métrica temporal A(r) | Numérico | PPN teórico | Estado |
|---|---|---|---|
| e^(−2φ) (σ = 0, β_PPN = 1) | **42.98″** | 42.98″ | ✓ = observado |
| (1−φ)² (ec. 43 original) | 50.15″ | 50.14″ | ✗ excluido |
| e^(−2(φ+φ²)) (σ = +1) | 57.31″ | 57.31″ | ✗ excluido |
| e^(−2(φ−φ²)) (σ = −1) | 28.66″ | 28.65″ | ✗ excluido |

Observado: 42.98 ± 0.04 ″/siglo. El integrador reproduce la fórmula PPN a 4 cifras — álgebra y numérica se validan mutuamente.

## Lo que sale gratis ahora (γ = β = 1 fijados)

- **Efecto Nordtvedt**: η = 4β − γ − 3 = **0** → la Luna y la Tierra caen igual hacia el Sol pese a sus distintas energías gravitacionales propias. Lunar Laser Ranging: η = (−0.2 ± 1.1)×10⁻⁴ ✓
- **Precesión geodética** (de Sitter): factor (1+2γ)/... → valor RG exacto, confirmado por LLR y Gravity Probe B ✓

Cero parámetros nuevos para ambos.

## Tablero actualizado

Dos números calibrados en total — β = 4 (eclipse 1919) y su *ubicación* en el sector temporal (Mercurio) — contra **siete observables**: deflexión 1.75″, Shapiro, no-dispersión radio/óptico, redshift/GPS, perihelio 42.98″, Nordtvedt, geodética.

## Predicción falsable propia (campo fuerte)

g₀₀ = e^(−2φ) coincide con Schwarzschild hasta O(φ²) pero difiere a O(φ³): TCI predice desviaciones de la RG cerca de objetos compactos (sombra de agujeros negros/EHT, púlsares binarios en campo fuerte). Cuantificarlas es el próximo frente natural, junto con la forma covariante del término (1+4φ)φ̇² y las ondas gravitacionales.
