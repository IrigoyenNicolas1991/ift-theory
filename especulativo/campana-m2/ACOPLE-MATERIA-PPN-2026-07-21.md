# Acople a materia de la fase U(X,Y): potenciales, PPN y el frame dragging — tarea 3 SALDADA

**Campaña m₂=0 · 2026-07-21 · campaña orquestada: estático/PPN + frame dragging + literatura
+ verificador adversarial (4 agentes, ~868k tokens en dos corridas — la primera murió por
límite de créditos en el verificador y se resumió de caché sin pérdida). El verificador
rehizo TODO con pipeline propio desde √−g R y NO refutó: una sola falla real, menor,
incorporada acá.**

## Resultado en cuatro líneas

1. **La masa quieta: el medio imita a Einstein por teorema, no por calibración.** La
   solución causal (cualquier fuente conservada que se enciende) del sistema masivo LO
   satisface las cuatro ecuaciones de RG pura con residuo [0,0,0,0]: el término de masa
   solo SELECCIONA el gauge síncrono y cuesta cero acción on-shell. **γ_PPN = 1 exacta**
   en todos los regímenes principales; G_N estándar sin renormalización; la modificación
   (modulación cos(μr)/r, NO Yukawa) vive a r ≳ r_c = M̄_Pl/Λ² y recién tras t_c ~ 18
   edades del universo — el punto fijo "estático eterno" es inalcanzable, idéntico al
   ghost condensate (diccionario aritmético cerrado: μ² = m²_ACLM exacto).
2. **El frame dragging tiene DOS ramas** — el descubrimiento de la campaña: la ley de
   conservación exacta del sector vectorial (la misma simetría ξⁱ(x⃗) que protege m₂=0)
   deja una dirección plana. Rama fundamental (medio relajado): **apantallamiento Yukawa
   derivado, (∇²−μ²)Sᵢ = 16πG̃τᵢ con μ² = m₁²/(M_Pl²+α)** — un Meissner gravitomagnético.
   Rama retardada (medio recién agitado, sin disipación): **RG exacto disfrazado** (el
   medio co-rota con los marcos). La frase de Dubovsky ("gauge fixing... higher order
   terms needed") describe la rama retardada; nuestra predicción vive en la relajada.
   El estado co-rotante es genuinamente excitado (H mayor, robusto a términos de borde —
   chequeo Ostrogradsky del verificador) y decae al Yukawa con cualquier disipación.
3. **La cota previa estaba mal y se corrige**: la precesión nodal lleva
   𝒮 = (1+μa)e^(−μa) — **sin término lineal en μ** (el dipolo Yukawa lo cancela). La
   cota se debilita 2.7× en Λ: lo defendible hoy es **Λ ≲ 2.0–2.6 MeV** (LAGEOS/LARES
   2–5%); **LARES-2 (0.2%) llegaría a Λ < 1.12 MeV** (ℓ₁ > 30 R⊕). A Λ=1 MeV la
   desviación nodal actual es 0.13%: la ventana está abierta y el test es real.
4. **La firma es VIRGEN — confirmado con búsquedas declaradas**: TODA la literatura de
   campos de fuentes en gravedad masiva LV (DTT, Bebronne-Tinyakov, Comelli-Nesti-Pilo,
   DTZ "bumpy black holes") vive en la familia espejo m₁²=0 (tensor masivo, vector = RG
   exacto — DTZ lo dice verbatim). Nadie calculó jamás el campo gravitomagnético de una
   fuente rotante en una fase con m₁²≠0, ni apantallamiento de Lense-Thirring en ninguna
   gravedad masiva o LV. Los α₁,α₂ de PPN tampoco existen para ninguna fase de Dubovsky
   (grep: cero ocurrencias en el review canónico) — y nuestro "α₁ dependiente de escala"
   está fuera del formalismo PPN estándar: terreno nuestro.

## El caveat central (declarado, es LA pregunta abierta del paper)

La predicción del apantallamiento es **condicional a que el medio relaje al estado
fundamental**. Si el superfluido sostiene la corriente co-rotante como corriente
persistente (metastabilidad tipo superfluido — ironía: la física de nuestro propio
sótano), no hay señal ni cota: la Tierra vería RG exacto. Decidir la relajación excede
el orden cuadrático (disipación no lineal / vórtices en la historia de formación de la
fuente). El paper debe presentar las dos ramas y la condición — es física nueva
igualmente: nadie había notado que la fase tiene esta estructura de dos estados.

## Fórmulas centrales (verificadas doble vía + verificador independiente)

- Estática escalar eterna: Φ̃=Ψ̃=(M/4M_Pl²)/(p²−μ_s²), μ_s²=m₀²/(2M_Pl²) ⟹
  Φ(r)=−GM[cos(μ_s r)+C sin(μ_s r)]/r (familia 1-paramétrica; solo la historia causal
  fija C — y la historia causal da Newton exacto hasta t_c).
- IVP causal NLO cerrado: ΔΨ(t,p)=A(p)[1−cos(Ω(p)t)], A=Φ̃_N μ_s²/(p²−μ_s²); banda de
  Jeans p<μ_s: cos→cosh. Verificado simbólicamente contra las 4 EOM (residuos 0).
- γ(p) estática con σ,ρ_op (falla del verificador incorporada):
  γ = 1 − 2σp²/M_Pl² + p⁴[ρ_op²/(M_Pl²m₁²) + 4σ²/M_Pl⁴] + O(p⁶).
- Exterior de esfera rígida rotante (rama relajada):
  h₀ᵢ = 2G̃(x⃗×J⃗)ᵢ(1+μr)e^(−μr)/r³·𝔉(μR), G̃=G·M_Pl²/(M_Pl²+α),
  𝔉(y)=15[(y²+3)sinh y−3y cosh y]/y⁵; límite μ→0 = Kerr linealizado exacto.
- Precesiones: Ω_nodo ∝ (1+x)e^(−x), giroscopio GP-B ∝ (1+x−x²)e^(−x), x=μa;
  Ω⃗_nodo = f(a)J⃗ demostrado para f genérica e inclinación arbitraria.
- Escala física: μ = 2Λ²/M̄_Pl ⟹ ℓ₁ = 2.40×10⁸ m·(MeV/Λ)² — a Λ=1 MeV, ~la distancia
  Tierra-Luna. Control dimensional SI: μ²=32πGΛ⁴/(ħ³c⁷) (acuerdo 10⁻³ con la ruta natural).

## Mapa de literatura (columna C, fuente primaria local, rutas en scratchpad declaradas)

| Familia | Qué calcularon | Nuestra fase |
|---|---|---|
| DTT hep-th/0504067 / Bebronne-Tinyakov 0705.1301, 0902.3899 / CNP 1010.4773 | fuentes estáticas en fases m₁²=0: Newton+μ²r, hair no lineal, Yukawa del tensor | NO aplica (fase espejo) |
| DTZ 0706.0288 (bumpy BHs) | rotación en fase m₁²=0: arrastre lineal en J = RG puro (verbatim); obstrucción a Kerr es O(J²) tensorial | NO aplica — y su "RG puro" es exactamente lo que nuestra fase NO da en la rama relajada |
| ACLM 0312099 + 0507120 (ghost condensate) | escalar p⁴, sin(mr)/r, r_c, t_c, cotas M≲10 MeV/100 GeV | aplica VÍA DICCIONARIO al escalar (verificado aritmético) |
| Einstein-aether (Foster-Jacobson) / khronometric / SME (Bailey) | frame dragging modificado FRACCIONAL, sin escala; cotas α₁≲10⁻⁴…α̂₂<1.6×10⁻⁹ | distinto en especie: lo nuestro es apantallamiento CON escala (gap) |

## Reproducibilidad

`acople/estatico/` (columna A: estática, teorema causal, IVP cerrado) ·
`acople/frame-dragging/` (columna B: derivación con fuente, dos ramas, Hamiltoniano,
matching, precesiones, cotas) · `acople/verificador/` (pipeline independiente: v1a-v3).
Todos corridos con Python 3.14 + sympy en esta máquina, 2026-07-21.

## Estado de la campaña

| Tarea | Estado |
|---|---|
| 1. Errata BCP | ✅ |
| 2. Sector escalar | ✅ |
| 3. Acople a materia / PPN / frame dragging | ✅ (esta acta) — caveat central declarado |
| Nuevo: selección de estado del medio (relajado vs corriente persistente) | ABIERTO — la pregunta que esta campaña descubrió |
| 4. FRW · 5. mapeo nota 10 · INSPIRE full-text | pendientes |
| 6. Paper corto | **las tres patas técnicas están**: errata + escalar + acople con firma virgen; falta armar el esqueleto y decidir canal (OK de Nico) |

*Escrita el mismo día, como manda la casa. El medio pasó su tercer examen: imita a
Einstein donde Einstein está medido, y se delata exactamente en un lugar — el arrastre
de marcos — donde nadie miró nunca y un satélite ya en órbita podría mirar.*
