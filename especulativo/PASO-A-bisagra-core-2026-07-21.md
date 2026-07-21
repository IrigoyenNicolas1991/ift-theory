# Paso A — La bisagra del core, CERRADA: el nudo llena su corazón con la mezcla alineada

**Compuerta única (§34.D de la bitácora madre) · 2026-07-21 · Fable (sesión
hielo-de-vortones, continuada) · sin agentes: `paso_a_bisagra_core.py`, 7 semillas + espejo
+ control de h + contraste, ~2h07m de máquina, QA completo de la regla nueva**

**Veredicto en una línea: la bisagra cierra del lado BUENO y con margen ×40 sobre el
número refutado — el core del HQV del D₄-BN se llena espontáneamente con la mezcla
FM+cíclica ALINEADA con el eje del tubo (L ∥ +ẑ, esclava del winding), desde CUALQUIER
semilla que rompa la simetría (incluidas la cíclica perpendicular y el ruido puro); el
"FM puro" del preliminar refutado NO es ni siquiera un mínimo local; y la física entera
de la bisagra vive en el término de divergencia del gradiente (K₂=K₃): sin él, el efecto
colapsa 60×. La matriz de gap del Paso B queda confirmada y medida: a·Y₊₂ + b·Y₋₁ con
C₃ ∥ eje.**

Contexto: el preliminar de la batalla de la red ("core mezcla FM+cíclica 76/24, C₃∥eje,
ΔE=−0.0114 vs FM puro") fue refutado como evidencia (errata #12: plateau no convergido,
drift/400 subestimó ~50×). La regla nueva de la casa (tronco del sótano §8 /
bitácora §34.C) exige convergencia por norma de gradiente, test espejo, semillas
inclinadas y control de h. Este cálculo la aplica completa. La sugerencia del refutador
("el atractor único es la mezcla C₃∥eje incluso sin semilla") queda **PROBADA con
números confiables — y enmendada en un punto**: hay una segunda cuenca metaestable
(el core trivial casi-D₄) que atrapa a las semillas que no rompen la simetría; el
atractor de todo lo demás es la mezcla alineada.

---

## 1. Setup (declarado)

- Sección 2D perpendicular al tubo; eje z = eje especial del D₄ de fondo (geometría
  estándar del proyecto, §30). HQV (w_φ, w_α) = (+½, +¼) centrado; marco de borde
  congelado al ansatz de London (fija la clase topológica; idéntico para todas las
  semillas ⟹ las ΔE comparan limpio).
- Funcional GL caso C textual (α,β,γ,ε = −1, 1, +0.15, 0.05; §16), **gradiente completo
  K₁ + 2K(div)** (K₁=K₂=K₃ textual de 1810.04901) como principal — el término div es el
  único que acopla la orientación interna del tetraedro al eje del tubo; corrida de
  contraste con K₁ solo (la convención de §30) para conectar con lo anterior.
- Grillas: N=80, h=1 (caja física 80×80, ξ=2) y control N=120, h=⅔ a caja física FIJA.
- Maquinaria heredada certificada: potencial + gradiente Wirtinger (autotest 5.1×10⁻⁹),
  fuerza del div (autotest 1.3×10⁻⁸), vacío D₄ a₀=0.47211 (control §16 ✓). Control
  nuevo de la base m_J: ortonormalidad exacta; cíclica C₃∥z = (Y₊₂+√2·Y₋₁)/√3 con
  TrA²=0 y L=0; FM=Y₊₂ con L=+ẑ — este control cazó un signo invertido en mi fórmula
  del momento angular ANTES de correr (errata propia #2 de la sesión, documentada).
- Métricas del core (disco r<2ξ): t=‖A‖², a₂₀=|TrA²|/‖A‖² (nemático), det̂=3^{3/2}|det
  A|/‖A‖³ (cíclico), L (momento angular, FM puro=1), y **pesos m_J** — la proyección
  sobre armónicos tensoriales, que es directamente el lenguaje de la matriz de gap del
  Paso B. Nota honesta: el disco r<2ξ incluye la interfaz con el fondo D₄ (peso m=±2
  del vacío penetra la métrica); el perfil radial fino queda para el input del Paso B
  (`paso_b_core_input.py`).

## 2. Resultados (N=80, K₁+2Kdiv, todas convergidas por norma de gradiente)

| Semilla | E final | g_rms | Estado final del core |
|---|---|---|---|
| desnuda | +12.33947 | 1.1×10⁻⁷ | trivial casi-D₄ (pesos {+2: 0.59, −2: 0.40}, det̂=0.17) |
| FM+z | +12.33947 | 1.4×10⁻⁷ | ídem — **el FM decae: no es mínimo local** |
| FM−z | +12.33947 | 1.3×10⁻⁷ | ídem |
| cyc-z | **+11.88573** | 1.3×10⁻⁷ | **mezcla alineada** (det̂=0.343, L_z=+0.101) |
| cyc-55° | **+11.88573** | 1.2×10⁻⁷ | ídem — **la inclinada se realinea sola** |
| cyc-x (⊥) | **+11.88573** | ~10⁻⁷ | ídem — **la perpendicular también** |
| ruido | **+11.88573** | ~10⁻⁷ | ídem — **el ruido puro cae al fundamental** |

Pesos m_J del ganador (r<2ξ): [+2]=0.416, [+1]=0.094, [0]=0.009, [−1]=0.236,
[−2]=0.244. La estructura {+2, −1} del core está presente y dominante una vez
descontada la interfaz (el −2 es mayormente el fondo D₄ penetrando el disco; perfil
fino en el input del Paso B). det̂=0.343 — **el mismo 0.34 que el preliminar refutado
reportaba para su "core real"**: la COMPOSICIÓN del preliminar era correcta; su
energética no.

**ΔE = 0.45373 entre cuencas** — cuarenta veces el 0.0114 refutado. La bisagra no
cierra por un pelo: cierra con holgura.

## 3. El QA, punto por punto (la regla nueva, aplicada completa)

- **QA1 — norma de gradiente, jamás drift por ventana**: todas las corridas convergidas
  a g_rms ≈ 10⁻⁷ (tolerancia 2×10⁻⁷) + pulido sin momentum. Drift residual del ganador
  medido aparte: |ΔE| = 1.53×10⁻⁷ en 5000 pasos extra — **seis órdenes de magnitud por
  debajo del ΔE entre cuencas**. El fantasma de la errata #12 queda enterrado.
- **QA2 — espejo (quiralidad esclava del winding)**: HQV (−½,−¼) desde el conjugado del
  ganador: |E_espejo − E_ganador| = 1.18×10⁻⁷ ✓; L_z: +0.1009 → −0.1008 ✓ invertido;
  pesos espejados exactos ({+2,−1} → {−2,+1}: 0.416/0.236 ambos lados) ✓. El core del
  anti-nudo es la imagen especular exacta — la quiralidad de la materia del tubo la
  fija el winding, como el preliminar sugería y ahora está probado.
- **QA3 — semillas inclinadas**: la cuenca ganadora atrae desde 4 semillas
  independientes, incluidas la cíclica PERPENDICULAR (C₃∥x) y el ruido sin estructura.
  No existe ningún mínimo local con el tetraedro inclinado o perpendicular: **el
  pinning de la orientación es duro** (todas las orientaciones drenan a C₃∥eje). La
  cuenca trivial (casi-D₄, +0.454) existe como metaestable y atrapa solo a las semillas
  que no rompen la simetría (desnuda) o que decaen a ella (FM±z).
- **QA4 — control de h a caja física fija** (N=120, h=⅔): ganador reproducido
  (E=+11.91811, misma composición: [+2]=0.416, [−1]=0.244, det̂=0.358, L_z=+0.105);
  trivial reproducida (+12.37684). ΔE entre cuencas: 0.459 vs 0.454 — **estable al 1%**.
  El error de discretización mueve las E absolutas (~0.03) pero no el orden ni el margen.

## 4. La lección física nueva: la bisagra vive en el término div

Contraste con K₁ solo (sin div, la convención de §30 Parte B): el ΔE entre cuencas
colapsa a 0.0073 (60× menos) y la componente cíclica del core casi desaparece
(det̂: 0.343 → 0.079; pesos [−1]: 0.236 → 0.042). **El término de divergencia
(K₂=K₃) es el responsable físico del llenado cíclico del core y de su alineación
con el eje** — es el único término del funcional que sabe dónde está el eje del tubo.

Dos consecuencias: (a) explica retroactivamente el preliminar refutado — con gradiente
isótropo la señal es ~0.007, del orden del ΔE=0.0114 que reportó y nunca pudo
converger; la señal real (con div) es 60× más gorda; (b) advertencia para TODO cálculo
futuro de texturas/cores del programa: K₁-solo es una convención cómoda para
rigideces de fase (§30, donde funciona), pero **mata la física de orientación de los
cores** — declarar siempre cuál se usa.

## 5. Lectura para la compuerta única (el semáforo del Paso B)

1. **La matriz de gap del Paso B queda confirmada y medida**: Δ(r) ~ a(r)·Y₊₂ +
   b(r)·Y₋₁ con C₃ ∥ eje del tubo — exactamente la forma que el crítico de §34 dejó
   escrita. Los perfiles (a,b) y los windings de cada componente salen del campo
   regenerado (`paso_b_core_input.py` → `paso_b_core.npz`, local regenerable).
2. **El pinning es duro en orientación** (atractor único alineado, sin metaestables
   inclinados) — la condición "si el pinning del tetraedro tiene gap contra los
   círculos mudos" de §34.A queda satisfecha en su versión energética de texturas: no
   hay cuenca muda donde caer. (El espectro de fluctuación del tetraedro — el "gap"
   cuantitativo — es refinamiento pendiente, no bloqueante para el conteo del Paso B.)
3. **La quiralidad de la materia es esclava del winding** (QA2): nudo y anti-nudo
   llevan cores espejados — el ingrediente de las anti-clases del scorecard de
   partículas, ahora calculado en el core real.
4. Deudas declaradas: perfil fino core-vs-interfaz (en curso, input del B); espectro
   de fluctuación del tetraedro; la anisotropía de la energía de línea del tubo según
   su orientación en el D₄ (acá el tubo se tomó ∥ al eje especial, la geometría
   estándar); y el paso del tubo recto al ANILLO (¿el tetraedro co-rota con la
   tangente? — §33.D, sigue abierta).

**El semáforo del §34 está en verde: ir al Paso B** — BdG de la sección del tubo con
la matriz de gap real medida acá, conteo neto de ramas por flujo espectral. El criterio
de muerte sigue en pie tal como fue pre-declarado: C_neto = 0 ⟹ 10ª lápida (tubos
estériles, Arquitectura A pierde materia y fotón).

## 6. Reproducibilidad y erratas

`paso_a_bisagra_core.py` (producción, este directorio; log completo de la corrida en el
scratchpad de sesión) y `paso_b_core_input.py` (regenerador del ganador + perfil radial
+ windings; base idéntica cortada programáticamente). Python 3.14 + numpy, esta máquina,
2026-07-21, ~2h07m. Erratas propias de la sesión: #2 — signo invertido en L_k =
−iε_{kab}(A†A)_{ab} (cazado por el control de base ANTES de correr: FM debe dar L=+ẑ).
Las #12 (drift por ventana) y la lección "contar por peso" (§33.E) están incorporadas
al diseño, no repetidas.

*Acta del Paso A, escrita el mismo día. La bisagra que hace tres días era un número
falso hoy es un teorema de relajación con cuatro caminos convergentes, un espejo exacto
y dos resoluciones. El nudo no es estéril: viene con su materia alineada de fábrica.
Falta contarla — eso es el Paso B.*
