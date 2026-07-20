# BITÁCORA DEL NÚCLEO — ¿el mar sabe contar hasta 4?

**Campaña del núcleo TCI — iniciada 2026-07-19, con OK explícito de Nico**
*("demosle un poco al núcleo ahora"). Archivo separado de la bitácora de la
campaña del condensado para no pisar la sesión paralela. Política vigente:
CERO PUSH — todo local.*

---

## §N1. La pregunta del núcleo

TCI 1.0 y TCI 2.0 son hoy **dos teorías sin puente**. TCI 1.0 tiene un
lagrangiano concreto y exitoso:

    L = (K/2c²)(1+4φ) φ̇² − (K/2)|∇φ|² − (Λ/2)φ² + Jφ

con **dos números calibrados**: β=4 (eclipse 1919) y su *ubicación* en el
término temporal (Mercurio: f₁=0, g₁=4, alternativas excluidas a ~300σ).
TCI 2.0 dice que el mar es un condensado J=2 (³P₂, fase D₄-BN) con funcional
GL conocido (bitácora del condensado, §16).

**La observación que abre el frente**: un condensado a potencial químico μ
tiene ecuación de estado *derivable*, no calibrable. P(μ), ρ(μ) y las
velocidades de todos sus modos salen del funcional GL. Entonces, por primera
vez en el proyecto, se le puede **preguntar al mar cuánto vale β** en vez de
calibrarlo con el eclipse. Si contesta 4, las calibraciones de 1.0 se vuelven
derivaciones y el puente existe. Si contesta otra cosa, sabemos con precisión
qué le falta al puente.

Definición operativa: para cada modo M del condensado,

    β_M := − d ln v_M² / dφ

con φ = déficit fraccional de densidad del fondo (la vacancia = materia).
TCI 1.0 exige β_luz = 4 (⟺ n = 1 + 2GM/c²r).

## §N2. El examen sorpresa: β_TT y el Shapiro de GW170817

Al plantear la pregunta apareció un examen que no habíamos visto: los modos
TT del D₄-BN son *las polarizaciones gravitacionales*. GW170817/GRB170817A
atravesaron el mismo pozo galáctico y llegaron con Δt = 1.7 s tras ~10⁸ años
de viaje: el retardo de Shapiro de la GW y el de la luz coinciden a nivel
fino (Abbott et al. 2017, test de γ_GW; **deuda: citar el número exacto del
bound antes de usarlo como verdugo**). El retardo de Shapiro es la integral
de (n−1): si la luz ve n = 1+2φ, **los TT del bulk también tienen que ver
n ≈ 1+2φ, es decir β_TT ≈ 4**. Un β_TT ≈ 0, o de signo contrario, mata el
cuadro "TT del bulk = gravedad" por sí solo, independientemente de cómo se
resuelva el sector de la luz. El núcleo tiene su propio verdugo.

## §N3. Resultado analítico 1: dónde vive la no-linealidad (gratis)

EFT estándar de superfluido (Son 2002; misma álgebra que usa Dubovsky):
integrar la amplitud deja L_eff = P(X) con X = ∂_μθ∂^μθ. Sobre el fondo
θ = μt, la expansión cuadrática es

    L₂ = P'(μ²) [θ̇² − |∇θ|²] + 2μ² P''(μ²) θ̇²

**Toda la no-linealidad de la EOS (P'') cae en el término temporal.** La
rigidez espacial es P' a secas. Esto es exactamente la estructura que TCI 1.0
tuvo que *calibrar* contra Mercurio (la no-linealidad vive en 𝒢(φ)φ̇², no en
𝓕(φ)|∇φ|²): en un superfluido a μ finito es **automático** — el fondo que
rompe Lorentz es temporal (θ̇=μ), así que la curvatura de la EOS solo puede
vestir al sector temporal. Primer ladrillo del puente, sin costo.

*Letra chica declarada*: el φ de TCI 1.0 es la vacancia (sector de amplitud),
no la fase θ; el enunciado sólido es sobre la estructura del cociente 𝒢/𝓕
que gobierna c_s²(fondo). El análogo exacto de σ=0 (estática a segundo orden)
requiere el cálculo del perfil de vacancia alrededor de un nudo — pendiente,
es el paso 2 del frente.

## §N4. Resultado analítico 2: el fonón de sombrero mexicano refracta AL REVÉS

Para V = a·t + (g/2)t² (t = tr AA*, cuártico genérico) a potencial químico μ
(u ≡ μ²), con la rama del mar (a < 0: condensado aun a μ=0, sombrero
mexicano):

    t₀ = (u−a)/g,   c_s² = (u−a)/(3u−a),   ρ = 2μt₀

    d ln c_s² / d ln ρ = 4au/(3u−a)²  →  con a<0:  **negativo**

*(errata propia cazada por el control C1 del script: la primera versión tenía
este signo dado vuelta en el código; la fórmula de acá es la verificada.)*

Es decir: **más densidad = sonido más lento; una vacancia = sonido más
rápido = la luz-fonón se curva ALEJÁNDOSE de la masa.** Signo contrario al
observado. Y la magnitud está acotada: |d ln c_s²/d ln ρ| ≤ 1/3 (máximo en
u = −a/3). El fonón del sombrero mexicano no cuenta hasta 4: cuenta hasta
−1/3.

(La rama opuesta a > 0 — condensado solo por μ, tipo BEC no relativista —
da el signo correcto y β→1 en el límite Bogoliubov, el famoso c_s² ∝ ρ del
contacto; con séxtico llega a 2; para β=4 haría falta EOS efectiva P ∝ ρ⁵.
Pero esa rama tiene c_s ≪ c y no es la ontología del mar.)

Conclusión parcial analítica: **si el mar es sombrero mexicano, el fonón del
bulk NO puede ser lo que refracta con β=4.** Converge —por tercera vía
independiente— con §23 y §32 de la campaña del condensado: la luz no es del
bulk. Lo nuevo: ahora la pregunta filosa es β_TT (§N2), que no tiene escape
por el sector de defectos.

## §N5. Cálculo numérico (nucleo_beta4.py)

Maquinaria: pencil cuadrático (−ω² − 2iμωJ + W(k))u = 0 con
W = Ĝ(k) + ½Hess V − μ², companion 20×20; fondo D₄-BN del funcional ³P₂
textual (caso C: α=−1, β₄=1, γ=+0.15, ε=0.05, K=1), dinámica 2º orden
declarada. Cadena de verificación: [C1] juguete U(1) vs fórmula analítica
exacta; [C2] μ=0 reproduce la clasificación del espectro del caso C
(2TT+2V sobre el eje; factor global de convención declarado); [C3]
linealidad ω(k) en dos k.

Dos parametrizaciones de la vacancia:
(I) on-shell (variar μ, fondo en su mínimo; φ = −δln ρ) y
(II) off-shell a μ fijo (fondo s·x₀ sostenido por la fuente; φ = 1−s²) —
la fiel a TCI (materia = déficit local con μ global uniforme).

### Resultados (corridas del 2026-07-19, tres iteraciones)

**Controles**: C1 exacto (pendiente numérica = fórmula analítica a 5
decimales, 3 valores de μ). C2: el D₄-BN a μ=0 da sobre su eje TT(v=1.0000),
TT(v=1.0001), V(v=1.4142=√2), V — limpio. C3: drift de pendiente entre
ventanas 0.00%.

**(I) on-shell**: β < 0 (signo CONTRARIO) para TODOS los modos en todo el
rango μ=0.15–0.90 (TT: −0.08…−0.27; V: −0.16…−0.42). Confirma §N4
numéricamente en el funcional completo.

**(II) vacancia a μ fijo — signo CORRECTO, y la ley**:

| μ | v_TT(eq) | β_TT medido | ley 2(1−v_TT²) |
|---|---|---|---|
| 0.25 | 0.964 | +0.129 (k→0 extrap.) | +0.143 |
| 0.60 | 0.864 | +0.504 (ventana W2) | +0.507 |
| 0.90 | 0.800 | +0.770 (ventana W2) | +0.720 |

**LA LEY: β_TT ≈ 2(1 − v_TT²/c_cin²)**, derivada EXACTA en el juguete U(1)
con la raíz cerrada del pencil (c² = 1 − 4μ²/B, B = δ+4μ²−ε ⟹
β(k→0) = 2(1−c²)) y verificada en el ³P₂ D₄-BN al 3–8%. Los vectoriales no
la siguen (β_V ≈ +0.27 con v>c_cin: estructura distinta, K₂₃-dominada) —
anotado, no crítico (son los canales oscuros).

**Erratas propias de la jornada (2, cazadas por los propios controles)**:
(1) signo de d ln c_s²/d ln ρ invertido en el código del control C1 de la
primera corrida (la fórmula correcta es 4au/(3u−a)², negativa para a<0);
(2) mi primera "confirmación" de la ley comparaba medición en ventana alta
de k contra la ley k→0 — el control C4 la refutó y forzó a derivar el
**sesgo de ventana**: la dispersión off-shell tiene un término cruzado
8μ²·εδ·k²/B³ (ε∝φ) que NO cancela en la pendiente ⟹ la ventana SUBESTIMA β.
Validado: numérico = fórmula cerrada en la misma ventana a 4 decimales.
También declarado: a μ≥0.6 la ventana baja (0.10–0.20) pierde los modos por
el tachión de la vacancia (números tipo +64/+104 = basura de apareo,
descartados); manda la ventana alta + la ley.

## §N6. El veredicto: SÉPTIMA LÁPIDA (de la clase mínima) + la mudanza del 4

**El verdugo citado**: Abbott et al. 2017, ApJL 848 L13 (GW170817/GRB
170817A): test del principio de equivalencia vía Shapiro de la Vía Láctea,
Δγ = γ_GW − γ_EM acotado a **O(10⁻⁶–10⁻⁷)** (trabajos posteriores ~10⁻⁷);
Cassini ya midió γ_EM = 1 (±2.3×10⁻⁵) ⟹ **β_TT = 4 es obligatorio** con
precisión de partes por millón, independientemente de cómo se resuelva el
sector de la luz.

**El teorema dice que la clase mínima no puede**: β_TT = 2(1−v_TT²/c_cin²)
≤ 2 < 4 SIEMPRE, y β_TT → 0 justo cuando v_TT → c_cin. Velocidad GW
correcta y Shapiro GW correcto son incompatibles en la clase
{GL polinómico + cinética canónica |Ȧ|² + gradientes cuadráticos}.
**FALSADA la clase mínima como origen de la gravedad refractiva.**

**Lo constructivo (la mudanza del 4)**: el teorema señala su propia salida —
violar la hipótesis de cinética canónica. El siguiente operador temporal de
la EFT del medio, 𝒢(t)|Ȧ|² con 𝒢 no constante, desbloquea β arbitrario. Y esa
es EXACTAMENTE la forma del término de TCI 1.0: (K/2c²)(1+4φ)φ̇². El puente
queda planteado así:

    ℒ_mar = 𝒢(t)|Ȧ|²/c² − K(t)(gradientes) − V(A)
    V(A): ya la tenemos (GL ³P₂, caso C)
    el eclipse de 1919 MIDE 𝒢′(t₀)  (el "4")
    Mercurio MIDE K′(t₀) = 0

El 4 deja de ser calibración astronómica misteriosa y pasa a ser un
coeficiente de Wilson localizado del lagrangiano del medio. La pregunta del
núcleo se achica a: **¿qué microestructura genera 𝒢′ = −4/t₀ y K′ = 0?**
(candidatos anotados: operadores de gradiente superior del GL; el vestido
de la red de nudos sobre el bulk; integrar out el sector de defectos).

## §N7. Marcador del frente núcleo

| Pieza del puente 1.0↔2.0 | Estado |
|---|---|
| Ubicación temporal de la no-linealidad (Mercurio, σ=0) | **estructural en superfluido a μ finito** (§N3) ✓ regalo |
| β del fonón del bulk (on-shell) | signo contrario, acotado — falsado §N4 ✓ |
| β_TT de la clase GL mínima | **FALSADO por teorema: β=2(1−v²)≤2, →0 con v→c; GW-Shapiro exige 4** (7ª lápida) |
| Dónde vive el 4 | **localizado**: 𝒢(t) no mínima, coeficiente de Wilson medible |
| Micro-origen de 𝒢′=−4/t₀, K′=0 | ABIERTO — el nuevo objetivo del frente |
| Perfil de vacancia a 2º orden (σ=0 real) | pendiente |
| Diccionario exacto vacancia↔φ (energía del nudo vs t local) | pendiente — solo rescala, no cambia el veredicto salvo exponente <1/2 (improbable, declarar) |

**Deudas declaradas**: dinámica de 2º orden postulada (como toda la
campaña); la ley verificada en juguete (exacta) + ³P₂ (3–8%), no probada
como teorema general de la clase (la estructura que la produce — rigidez ∝ t,
inercia constante, vestido μ — sugiere que sí; formalizar si hace falta);
bound exacto de Δγ por confirmar contra el texto del ApJL (verificado en
orden de magnitud por búsqueda, 2026-07-19).
