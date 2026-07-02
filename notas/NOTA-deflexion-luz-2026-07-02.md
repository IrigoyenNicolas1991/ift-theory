# Deflexión de la luz en TCI: diagnóstico y derivación

**Nota de trabajo — 2 de julio de 2026**
*(preparada por Claude Fable 5 sobre el material de Nicolás Irigoyen)*

## 1. El problema (honesto y sin anestesia)

El sitio conceptual afirmaba: *"El cálculo da exactamente 1.75 segundos de arco"*. Ese cálculo **no existía** — el paper técnico lo listaba correctamente como problema abierto (§7.5, ítem 3). Peor: el mecanismo descripto ("diferentes partes del frente de onda viajan a velocidades ligeramente diferentes") **contradice la propia ecuación de estado de la teoría**.

La razón: el Postulado 1 dice P = ρc² (fluido rígido, *lineal* en ρ). La velocidad de propagación de perturbaciones es

$$c_s^2 = \frac{dP}{d\rho} = c^2 = \text{constante, independiente de la densidad local.}$$

Si la ecuación de estado es exactamente lineal, la luz viaja a c en todas partes — **el gradiente de densidad alrededor del Sol no refracta nada**. La teoría lineal predice deflexión **cero**, igual que la gravedad escalar de Nordström (1913), que murió justamente por el eclipse de 1919. Este era EL punto donde la teoría se jugaba la vida.

*(Detalle menor pero real: la Remark 2.1 del paper dice c_s = √(P/ρ); la fórmula correcta es c_s = √(dP/dρ). Coinciden solo porque la EOS es lineal — y esa linealidad es exactamente lo que mata la refracción.)*

## 2. La solución: curvatura de la ecuación de estado

El Postulado 1 fija la presión y la rigidez del medio **en el equilibrio**, pero no dice nada sobre su respuesta a segundo orden. Escribimos la EOS como desarrollo de Taylor alrededor de ρ₀, con Δ ≡ (ρ−ρ₀)/ρ₀:

$$P(\rho) = \rho_0 c^2\left[1 + \Delta + \tfrac{\beta}{2}\Delta^2 + \mathcal{O}(\Delta^3)\right]$$

donde β es un parámetro adimensional nuevo (la "curvatura" del medio). Los dos primeros coeficientes ya estaban fijados por resultados existentes:

- **P(ρ₀) = ρ₀c²** → preserva la derivación de E = mc² (§3 del paper: W = P₀V usa la presión de equilibrio).
- **dP/dρ|ρ₀ = c²** → preserva la propagación a c en el medio no perturbado.

La velocidad local de propagación sobre un fondo estático con déficit Δ = −φ(r):

$$c_s^2(r) = c^2\left[1 - \beta\,\phi(r)\right] \;\Longrightarrow\; c_s(r) \approx c\left(1 - \tfrac{\beta}{2}\phi(r)\right)$$

Cerca de una masa el medio está deprimido (φ > 0) → la luz viaja **más lento** → se curva **hacia** la masa. Dirección correcta. ✓

## 3. Índice de refracción efectivo y deflexión

Con la identificación ya establecida por la derivación del redshift (ec. 42 del paper, anclada por Pound–Rebka): φ(r) = GM/(c²r). El medio actúa como lente de índice gradual:

$$n(r) = \frac{c}{c_s(r)} \approx 1 + \frac{\beta}{2}\frac{GM}{c^2 r}$$

Deflexión de un rayo con parámetro de impacto b (eikonal, camino recto a primer orden). Para n − 1 = A/r el resultado estándar es α = 2A/b:

$$\alpha = \frac{\beta\, GM}{c^2 b}$$

La observación (eclipse de 1919, hoy VLBI) da α = 4GM/(c²b) ⟹ **β = 4**, y entonces

$$n(r) = 1 + \frac{2GM}{c^2 r}$$

— exactamente el índice efectivo del campo débil de la RG (PPN γ = 1). Para luz rasante al Sol: α = 4GM☉/(c²R☉) = 8.49×10⁻⁶ rad = **1.75″**. ✓

### Honestidad primero

β = 4 **se calibra con el eclipse, no se predice** — igual que G se calibra con Cavendish. Decir "TCI predice 1.75″" a secas sería mentir. El contenido físico real es lo que viene ahora.

## 4. Lo que sale gratis: retardo de Shapiro (predicción sin libertad)

Con β ya fijado, la luz viaja a c_s(r) = c(1 − 2φ) y acumula un retardo extra:

$$\Delta t = \frac{1}{c}\int (n-1)\,dl = \frac{2GM}{c^3}\ln\frac{4 r_1 r_2}{b^2}$$

(ida). Para un radar Tierra–Venus en conjunción superior rasante: ida y vuelta ≈ **230–250 μs** — medido por Shapiro (1968) y, en su forma moderna, por Cassini (Bertotti–Iess–Tortora 2003): γ − 1 = (2.1 ± 2.3)×10⁻⁵. Misma β, segundo observable, **cero parámetros nuevos**. Además n(r) no depende de la frecuencia → radio y óptico se curvan igual, como confirma VLBI. Tercer observable gratis.

## 5. Consistencia con el redshift (el clásico asesino de teorías de "c variable")

El peligro típico: si los relojes también corrieran al ritmo de c_s, el redshift daría 2ΔΦ/c² — el doble de Pound–Rebka. Muerte instantánea.

TCI se salva porque los dos efectos viven en lugares distintos:
- **Relojes** (§7.3): su ritmo viene de la energía de interacción, E = mc²(1−φ) — primer orden en φ, **independiente de β** → redshift con factor 1. ✓
- **Luz**: su velocidad viene de dP/dρ — sensible a β → deflexión con factor 2. ✓

Es exactamente la estructura g₀₀ vs g_rr del campo débil de la RG, transplantada al medio: la parte temporal quedó fijada por el redshift, la parte espacial por β = 4.

## 6. Restricción no trivial sobre el lagrangiano microscópico

En lenguaje de campos, β ≠ 0 exige **no linealidad en el sector derivativo** (métrica acústica, à la Unruh 1981 / Visser 1998). Un auto-acoplamiento de potencial tipo gφ³ NO sirve: daría un índice dispersivo n(ω) − 1 ∝ 1/ω² — deflexión dependiente de la frecuencia, excluida por VLBI. Que la observación obligue a poner la no linealidad en las derivadas y no en el potencial es una restricción estructural genuina sobre la teoría. La forma covariante exacta de ese término queda como problema abierto.

## 7. Estado del tablero después de esto

| Observable | Estado |
|---|---|
| E = mc², Newton, E(v) = γmc² | Derivados (paper, §3–5) |
| Redshift gravitacional / GPS | Derivado (§7.3), factor 1 ✓ |
| Deflexión de la luz 1.75″ | **Calibra β = 4** (nueva §7.4) |
| Retardo de Shapiro | **Predicho sin libertad** ✓ |
| Deflexión igual en radio y óptico | **Predicho sin libertad** ✓ |
| Perihelio de Mercurio (43″/siglo) | Abierto — lo gobierna el coeficiente cúbico de la EOS (el análogo de PPN β). Es el próximo frente. |
| Ondas gravitacionales, cuántica, estructura nuclear | Abiertos |

## Cambios aplicados a los sitios

1. **Paper técnico (ift-theory)**: nueva §7.4 con esta derivación completa (ecs. 49–54), renumeración de §7.4→7.5 y §7.5→7.6, deflexión removida de problemas abiertos, perihelio re-encuadrado vía coeficiente cúbico, abstract y conclusión actualizados, referencias agregadas (Shapiro, Bertotti et al., Unruh, Visser).
2. **Sitio conceptual (teoria-campo-intangible)**: el recuadro "el cálculo da exactamente 1.75″" reemplazado por la versión honesta (mecanismo + β calibrada + Shapiro gratis), tabla de verificaciones corregida (deflexión = "calibrada", Shapiro = fila nueva "predicho").
