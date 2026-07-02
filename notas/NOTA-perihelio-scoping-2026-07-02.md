# Perihelio de Mercurio en TCI: scoping honesto del problema

**Nota de trabajo — 2 de julio de 2026** · rama `desarrollo-fable`

## Qué hay que calcular

La precesión anómala del perihelio de Mercurio: **42.98 ± 0.04 ″/siglo** (observado). En lenguaje PPN, la precesión por órbita es

$$\Delta\omega = \frac{6\pi GM}{c^2 a(1-e^2)}\cdot\frac{2+2\gamma-\beta_{\rm PPN}}{3}$$

La RG tiene γ = 1, β_PPN = 1 → factor 1 → 43″/siglo. TCI ya fijó **γ = 1** (§7.4, deflexión/Shapiro). Falta β_PPN, que vive en el término de segundo orden de g₀₀:

$$g_{00} = 1 - 2\phi + 2\beta_{\rm PPN}\,\phi^2 + \ldots$$

## El estado actual de TCI (y la tensión)

El paper identifica g₀₀ = (1−φ)² = 1 − 2φ + **1·φ²** (ec. 48). Comparando: 2β_PPN = 1 → **β_PPN = 1/2**.

Si eso fuera la historia completa, la precesión sería (2+2−½)/3 = 7/6 del valor de la RG ≈ **50.1″/siglo — un 17% de más, excluido por ~180σ**. Este es el número que hay que mirar de frente.

## Por qué NO es (todavía) una falsación

El cálculo anterior asume dos cosas que la teoría aún no fijó:

1. **φ lineal hasta segundo orden.** La identificación φ = GM/(c²r) se derivó del sector lineal. Pero la §7.4 ya estableció que el medio ES no lineal (β = 4 en el sector derivativo). Esa misma no linealidad corrige el perfil del campo del Sol a O(φ²) y la energía de interacción del hueco de prueba a O(φ²). Ambas correcciones alimentan el coeficiente de φ² en g₀₀ efectivo.
2. **Que la partícula sigue geodésicas de la métrica efectiva (44)+(53).** La dinámica de un hueco a segundo orden hay que derivarla del lagrangiano, no asumirla.

**La condición de supervivencia es precisa:** el sector de segundo orden (la no linealidad derivativa con β = 4 + el coeficiente cúbico de la EOS) debe aportar exactamente **+½·φ²** adicional a g₀₀, llevando β_PPN de ½ a 1. Ni más ni menos.

## Lo interesante (y lo peligroso)

- **Interesante:** la no linealidad ya no es libre — β = 4 quedó fijada por la luz. Si ESA MISMA no linealidad, sin parámetros nuevos, empuja β_PPN → 1, sería un resultado espectacular: el eclipse de 1919 prediciendo el perihelio de Mercurio dentro de TCI.
- **Peligroso:** si la corrección da otro número, la teoría queda falsada en el sistema solar (salvo que el coeficiente cúbico de la EOS, aún libre, pueda absorberlo — en cuyo caso Mercurio *calibra* el cúbico y hay que buscar un cuarto observable post-newtoniano para testearlo: Nordtvedt/LLR, por ejemplo).

## Plan de ataque

1. Escribir el lagrangiano con la no linealidad derivativa explícita (forma mínima compatible con β = 4 y con la covariancia local del sector lineal).
2. Resolver el campo del Sol a O(φ²) con esa no linealidad (corrección al perfil de Yukawa/Coulomb).
3. Derivar la energía de un hueco de prueba en ese fondo a O(φ², v²φ) → lagrangiano efectivo de la órbita.
4. Extraer β_PPN y comparar con 1. Publicar el resultado **sea cual sea** — si falsifica, se documenta la falsación y qué la salvaría.

## Verificación numérica pendiente

Cuando exista el resultado analítico: integrar numéricamente la órbita de Mercurio con el potencial efectivo TCI (a = 5.79×10¹⁰ m, e = 0.2056) y medir la precesión directamente, como chequeo independiente del álgebra.
