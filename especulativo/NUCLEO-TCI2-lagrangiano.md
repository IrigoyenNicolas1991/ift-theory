# EL TRONCO — Lagrangiano maestro de TCI 2.0 y caja de herramientas
# [ETAPA ESPECULATIVA — documento de trabajo interno, v1 2026-07-19]

**Propósito**: TODO lo calculado de TCI 2.0 sale de UN solo objeto. Este documento
lo escribe una vez, con una sola notación, para que cada rama futura sea un
trámite ("bajar del tronco, calcular, volver") y no una expedición. Si una sesión
futura arranca de cero: leer esto primero; la historia y las justificaciones
viven en `BITACORA-campana-condensado-2026-07-16.md` (§§ citadas acá).

---

## 1. El objeto

Campo **A(x,t)**: matriz 3×3 compleja, simétrica, sin traza (parámetro de orden
J=2 — "las almendras del mar": condensado cuadrupolar). 10 componentes reales.

**Base ortonormal** E_a (tr E_aE_b = δ_ab), la de todos los scripts:

    E0 = diag(1,−1,0)/√2        E1 = (xy+yx)/√2       E2 = (xz+zx)/√2
    E3 = (yz+zy)/√2             E4 = diag(−1,−1,2)/√6

    A = Σ_a (x_a + i·x_{a+5}) E_a   →   vector real x ∈ ℝ¹⁰

Componentes esféricas útiles: ψ±2 ∝ (z0 ∓ i z1)/√2 con z0 = x0+ix5, z1 = x1+ix6.
En el vacío D₄ (abajo), TODO el condensado vive en ψ±2 — el mar es, en secreto,
un superfluido de dos componentes (§30).

## 2. La dinámica (elección DECLARADA)

    L = ½ |∂_t x|² − F[x]          (segundo orden, lorentziano de fábrica)

Consistente con todos los espectros (§14-16): ω² = autovalores de (Hess V + K(k)).
NO es Gross-Pitaevskii (1er orden): los vórtices acá tienen inercia; el control
Kozik-Svistunov (dinámica GP/Magnus) NO aplica directo — pendiente si algún día
se explora la variante GP (§31).

## 3. La energía F[A] = gradientes + potencial

### 3a. Gradientes (weak coupling K1=K2=K3=K, textual 1810.04901)

    F_grad = K ∂_iA*_jk ∂_iA_jk + 2K (∂_jA*_jk)(∂_lA_lk)
    (en Fourier, forma real: K5(k) = K k² 𝟙 + 2K (k·E_a)(k·E_b))

El término div (2K) DUPLICA las rigideces de London pero NO cambia la estructura
de sectores (verificado §30: k+− = 0 exacto con y sin div; pendientes no lineales
duplicadas confirmadas al 2-5% en modo `div`). Para relajaciones rápidas se
puede usar solo K1 (declararlo siempre).

### 3b. Potencial (textual ³P₂, Yasui-Chatterjee-Nitta 1810.04901 ecs. 17-19)

    V = α t + β q4 + γ s6 + ε t⁴
    t  = tr(A A†)                      (norma²)
    q4 = t² − tr(A†A†AA)               (cuártico weak coupling)
    s6 = −3t|u|² + 4t³ + 6t·tr(A†²A²) + 12t·tr((A†A)²)
         − 6Re[ū·tr(A†A³)] − 6Re[u·tr(A†³A)] − 12Re tr(A†³A³)
         + 12Re tr(A†²A²A†A) + 8Re tr((A†A)³)      con u = tr(A²)
    ε t⁴ = regularizador declarado (no rompe la degeneración nemática)

**Parámetros de la casa (caso C)**: α=−1, β=1, **γ=+0.15** (signo HIPÓTESIS TCI,
declarado — en materia de neutrones real γ<0 → fase UN), ε=0.05, K=1.

## 4. Los vacíos (diagrama completo, §16 y §26)

| γ | vacío | forma | modos sin masa |
|---|-------|-------|----------------|
| γ<0 | UN (uniaxial) | a·diag(1,1,−2)-clase | 3 (control: Bedaque-Nicholson ✓) |
| γ>0 | **D₄-BN (la casa)** | **A₀ = a·diag(1,−1,0)**, a=0.47211, V₀=−0.264719 | 4 = 2 TT + 2 vec |
| β solo | degeneración SO(5) | familia continua | (control UKU ✓) |
| — | cíclica | autovalores (1,ω,ω²)·a | 4, TT mediocre (§26) |

**El vacío D₄**: eje especial z (autovalor 0). Grupo residual: D₄ mezclando fase
y rotación ((−1, R_{π/2}): rotar 90° = fase π). ψ+2 y ψ−2 con |ψ±2| = a.

## 5. Espectro sobre D₄ (§16, §22)

Sobre el eje especial: **2 TT sin masa** (v≈1.078 = fonón U(1) "vestido" y
v≈1.083 = rotacional — LAS DOS POLARIZACIONES GW, mecanismo propio: el sonido
del superfluido vestido de biaxial ES la segunda polarización, novedad verificada
§17) + 2 vectoriales (v≈1.46) + masivos (modo-r gap 0.24; amplitud ω≈2.6-2.8 —
la "campana" del ringdown masivo §31). Fuera del eje: 1 modo casi-TT en todo el
cielo (media 0.951), anisotropía v_TT ~12.6% con parámetros de juguete (§22 —
EL DRAGÓN CMB, deuda mayor del programa).

## 6. London / los sectores (el teorema de las dos monedas, §30)

Textura A = e^{iφ} R(α) A₀ Rᵀ(α) (α = rotación alrededor del eje especial):

    ρ_marco/ρ_fase = 4 EXACTO  (el cuadrupolo acopla rotación con carga 2)
    cruce fase-marco = 0;  isotropía en el plano (aun con div)
    base que diagonaliza: χ± = φ ± 2α  (= fases de ψ∓2)
    ⟹ DOS gases de Coulomb U(1) independientes con k++ = k−− (= Ka² con K1 solo)

**Especies fundamentales de HQV** (w_fase, w_marco) → (q+, q−):
(½,¼)→(1,0); (½,−¼)→(0,1); (−½,¼)→(0,−1); (−½,−¼)→(−1,0).

## 7. Fuerzas entre nudos (todo MEDIDO, §30 + nightcap)

| par | fuerza | valor |
|---|---|---|
| mismo sector, mismo signo | repulsión log (F ∝ 1/d) | pendiente −2.80 (K1) / −5.60 (full), verif. 1-5% |
| mismo sector, signo opuesto | atracción log | ídem, + aniquilación (91% radiado, §31) |
| sectores cruzados | **neutro a orden log** | < 0.5%; residuo **atractivo ~1/d^3.19** (vdW del mar) |
| molécula (uno de cada) | ligada | tamaño ~3ξ = balance vdW ↔ repulsión de core |
| corrientes (dinámico) | Ampère ∝ Ω² | mató la binaria (teorema del plunge §31) |

Radiación de eventos: sectores NO se mezclan ni en fusión; vectoriales
EXACTAMENTE oscuros (0.00%, por simetría del evento); cola masiva en el gap.

## 8. Defectos (taxonomía §20-21)

    π₁ = ℤ ×_h D₄*  (NO abeliano: 7 familias; fundamentales = HQV)
    π₂ = 0 (sin monopolos — por eso no hay Coulomb 1/d² del bulk)
    π₃ = ℤ (candidato a partículas-anillo: Hopfions/vortones)

Anillos: twist estabiliza contra Derrick (torre superlineal ⟹ solo k=±1
absolutamente estable — "mar tacaño"); cores con orden FM/cíclico (ingrediente
vortón); niveles internos discretos del anillo = candidato familias (§25,
especulativo³).

## 9. Caja de herramientas numérica (todo con autotest — REGLA DE ORO)

Scripts en `especulativo/` (rama desarrollo-fable):

- `espectro_biaxial_real/complejo/_3p2.py` — espectros k=0 y k≠0; controles
  Bedaque-Nicholson (UN), UKU (SO(5)), FQ@SU(3).
- `coulomb_del_mar.py` — modos: `todo` (London + relajación 2D + molécula),
  `div` (gradiente completo), `residuo` (fuerza directa sobre nudo anclado).
- `binaria_del_mar.py` — dinámica temporal (leapfrog + esponja): `pilot`,
  `scan Ω`, `full`; `analiza_binaria.py` post-hoc de `binaria_datos.npz`.
- `anisotropia_mapa.py`, `monometricidad_test.py`, `scaling_cuadrupolo.py`,
  `anillos_toy.py`, `espectro_ciclico.py` — cada uno con su § en bitácora.

**Convenciones y lecciones ganadas con sangre**:
1. AUTOTEST SIEMPRE: todo gradiente/fuerza analítica se valida contra numérico
   antes de usarse (cazó 2 signos ya). Vectorización se valida contra escalar.
2. Gradiente del potencial: analítico Wirtinger (P = ∂F/∂A; g_re = 2Re⟨P,E⟩,
   g_im = −2Im⟨P,E⟩) — 10× más rápido que numérico.
3. Rastrear defectos por WINDING TOPOLÓGICO por plaqueta (fase de ψ_q), jamás
   por amplitud (el core del HQV se rellena — Seo).
4. Fuerzas: medir DIRECTO sobre el nudo anclado (F = Σ_disco R·∂x/∂c, teorema
   de la envolvente) — mucho más sensible que diferencias de energía. Control
   de imagen de borde: restar el nudo solo.
5. Datos crudos a disco ANTES de analizar (np.savez) — ningún análisis en
   memoria sin respaldo.
6. Python: usar explícito `C:\Users\usuario\AppData\Local\Programs\Python\
   Python314\python.exe` (el del PATH cambia; el 312 no tiene numpy).
7. Relajaciones: borde congelado al ansatz + cores anclados (discos r≤2.5);
   corte por convergencia. Dinámica: dt=0.12, esponja cuadrática de velocidad.
8. El browser de preview NO anima rAF — verificar física con Node/Python.

## 10. Ramas abiertas, con su punto de entrada en el tronco

| rama | entrada | § |
|---|---|---|
| **La luz de la red** (fotón Levin-Wen) | §8 taxonomía + D(D₄*): ¿qué condensa sin matar D₄? | §27 |
| Anillos 3D / Hulse-Taylor real | §8 anillos + §7 fuerzas → órbitas newtonianas 3D | §28-31 |
| Dipolo J1738 (verdugo) | §7 canales oscuros → acople worldsheet (HNP 1507.05635) | §28-29 |
| Dragón CMB / monometricidad | §5 anisotropía + tétrada de cores (Volovik) | §22-24 |
| Familias e/μ/τ | §8 niveles internos del anillo | §25 |
| **Hipótesis del sótano** (fluido continuo bajo el mar) | `HIPOTESIS-SOTANO-fluido-continuo.md` | idea Nico 19/7 |
| Paper "dos electricidades" | `PAPER-borrador-dos-electricidades.md` (bloqueos técnicos saldados; falta OK de Nico + canal) | §30 |

## 11. Controles obligatorios para TODO cálculo futuro

Reproducir antes de creer: (a) UN con 3 gapless (Bedaque-Nicholson 1307.8183);
(b) spin-2 BEC 5 lineales (Uchino-Kobayashi-Ueda 0912.0355); (c) FQ@SU(3): 2
type-B cuadráticos ω≈(3/√8)|J|k² (§11); (d) Coulomb log ±2.80/±5.60 y neutros 0
(§30); (e) splitting del vórtice entero (Masuda-Nitta). Si tu cálculo nuevo no
reproduce el control que le toca, está MAL él, no el control.
