# Sector escalar de U(X,Y) con mezcla gravitatoria — tarea 2 SALDADA

**Campaña m₂=0 · 2026-07-21 · campaña orquestada: derivador + control textual +
fenomenólogo + verificador adversarial (4 agentes, ~559k tokens; el verificador rehizo
TODO desde √−g R con pipeline propio y no refutó — cuatro fallas menores, corregidas acá)**

## Resultado en tres líneas

1. **Al orden dominante estricto (U(X,Y)+EH cuadrático), el sector escalar NO propaga**:
   det = −(M_Pl⁴m₀²m₁²/2)·ω⁴p⁶ — cero DOBLE en ω²=0 para todo p. Coincide textual con la
   ec. (99) de Dubovsky ("mixing with gravity does not introduce new propagating modes").
2. **El famoso ω²∝p⁴ requiere los operadores NLO del medio** (derivadas superiores
   compatibles con la simetría residual ξⁱ(x⃗): K̄ᵢⱼK̄ᵢⱼ, (trK̄)², …): con ellos aparece
   UN modo, con coeficiente **UV-sensible** c₄ ≈ −(α+β)/m₀² — NO expresable solo en
   m₀²,m₁². Dubovsky nunca lo calculó (su "a" es genérico, verificado en fuente):
   **nuestra fórmula exacta de ω²(p) es la primera escritura explícita para este medio.**
3. **Con gravedad, el término dominante en p→0 no es p⁴ sino un p² tipo Jeans**,
   ω² ≈ (κ/2M_Pl²)p² con κ=α+β<0 en la rama sana — la inestabilidad IR lentísima del
   ghost condensate, inofensiva (ver cotas). El p⁴ domina para p² > m₀²/(2M_Pl²).

## Corrección a la Nota 12 / bitácora (obligatoria)

Donde el handoff decía *"Sector escalar: 1 modo ω²∝p⁴ (Dubovsky ec. 74, citado, no
rederivado)"* debe decir: **al orden de dos derivadas el escalar está congelado (cero
doble); el modo p⁴ existe solo al encender los NLO del medio, y su coeficiente es de los
NLO, no de las masas.** No es un problema — es exactamente lo que Dubovsky describe (el
cero doble que se parte, su Fig. 1) y la física del ghost condensate — pero la nota debe
decirlo bien. También corregir: la cota del handoff "M < 10 MeV-ish" es la lineal de
ACLM; la cota dura publicada es M ≲ 100 GeV (twinkling del CMB, hep-ph/0507120).

## La dispersión exacta (M_Pl=1; κ≡α+β; verificada por dos rutas + verificador independiente)

    ω²(p) = p²·[κ(2p² − m₀²) + p²m₀²(ρ²/2 − 2κσ)] / [m₀²(−2 − α + 3β + α² + 3αβ)]

- Límite EFT (|α|,|β|≪1): ω² ≈ (κ/2)p² − [κ/m₀² + (ρ²−4σκ)/4]p⁴.
- Límite de desacople M_Pl→∞: ω² → −κp⁴/m₀² (puro p⁴, la forma de Dubovsky).
- La otra raíz es ω²=0 EXACTA a todo orden (protegida por la simetría residual;
  sobrevive con NLO — el "cero simple" que queda tras partirse el doble).
- **m₁² se cancela EXACTAMENTE en ω² y en el término cinético K del modo escalar** —
  solo vive en el sector vectorial.
- No-fantasma, desglosado (refina el m₀²m₁²>0 de Dubovsky ec. 75): **κ<0** (signo tipo
  ghost condensate del NLO) + **m₀²>0** (sin inestabilidad de gradiente p⁴) + **m₁²>0**
  (vector sano). Esquina (m₀²,m₁²)=(1,2) con β=−ε: K=3+2/ε>0 ✓, ω²=εp²(2p²−1)/(2+3ε)
  (Jeans suave bajo p²=½, estable arriba).
- Sectores restantes con gravedad, verificados: vector NO propaga (det=(m₁²/4)ω²p²(M_Pl²+α));
  tensor sin masa exacto, c_T²=M_Pl²/(M_Pl²+α) (con α=0, intocado). Conteo: 2 g.d.l. (LO),
  2+1 (NLO) — coincide con Dubovsky.

## Fenomenología (cotas con fuente primaria leída)

- **Diccionario exacto con el ghost condensate** (ACLM hep-th/0312099; residuo sympy=0
  por dos vías): M⁴=2m₀², κ=−M̄²/2. En el sector escalar el medio es **indistinguible**
  del ghost condensate (porque m₁² se cancela ahí).
- **Jeans inofensiva**: τ ≈ 18–21 edades del universo a Λ=10 MeV (∝Λ⁻³); para Λ≲30 MeV
  la fricción de Hubble la elimina por completo; arriba, el no-lineal la satura en
  grumos ~1-2% de la energía oscura (invisibles hasta M~100 GeV).
- **La esquina sana sobrevive como forma, no como números**: reescalando U=Λ⁴Û, ventana
  amplia Λ ≲ 10 MeV (conservadora) hasta ~100 GeV (aceptando grumos), y por abajo hasta
  Λ~10⁻³ eV (donde haría de energía oscura). Jerarquía Λ≪M_Pl declarada sin explicar
  (el mismo fine-tuning de escala de todo ghost condensate).
- **LA FIRMA DISTINTIVA DEL MEDIO ES m₁²≠0** (el ghost condensate lo tiene prohibido
  por su simetría residual — verificado textual): apantallamiento Yukawa del **frame
  dragging** a r ≳ ℓ₁ = M_Pl,red/(2Λ²) — sin el retardo t_c que protege al escalar.
  LARES (~5%) daría Λ ≲ 1.0 MeV; **LARES-2 (0.2%) sería el test**. ESTADO: deducción
  propia del límite estático de la ec. (85) de Dubovsky, con el factor √2 ya corregido
  por el verificador — **falta la derivación prolija con fuente rotante y gauge residual
  antes de escribirla como resultado** (tarea nueva, prioridad alta: es la predicción
  falsable propia del paper).

## Erratas ajenas encontradas (para la carta a los autores, si va)

En el fuente LaTeX de hep-th/0409124: ec. (73) trae Λ⁴ donde dimensionalmente va Λ²
(y omite "=0"); ec. (99) trae +6(∂₀τ)² donde la rederivación desde su propia (86)-(88)
da −6(∂₀τ)² (verificado simbólicamente; no cambia su conclusión). Su EH de la sección 5
es 2× el canónico ⟹ el factor de conversión absoluto de masas es 2M_Pl² frente a sus
ecs. (2)/(22) pero M_Pl² frente a la sección 5 — ninguna condición adimensional cambia.
Rubakov-Tinyakov 0802.4379 NO analiza esta fase (verificado: remiten a Dubovsky).

## Reproducibilidad

- `escalar/derivador/` — pipeline del derivador (EH desde cero, reducción por dos rutas,
  NLO, vector, tensor).
- `escalar/verificador/` — pipeline INDEPENDIENTE del verificador (no comparte código);
  incluye el cotejo simbólico contra las ecs. (22), (86)-(88), (99) de Dubovsky y la
  auditoría numérica de todas las cotas.
- `escalar/cotas_fenomenologicas.py` — el diccionario ACLM y los números de las cotas.

## Estado de la campaña tras esta acta

| Tarea del handoff | Estado |
|---|---|
| 1. Verificación independiente + errata BCP | ✅ SALDADA (VERIFICACION-BCP-2026-07-21.md) |
| 2. Sector escalar completo | ✅ SALDADA (esta acta) — con corrección a la Nota 12 |
| 3. Acople a materia y PPN | ⏳ siguiente |
| 4. Cosmología FRW | pendiente |
| 5. Mapeo con nota 10 | pendiente |
| 6. Paper corto | las piezas 1-2 ya aguantan referato; falta 3 + frame dragging prolijo + INSPIRE |

*Escrita el mismo día del cálculo, como manda la casa. El medio pasó su segundo examen:
el escalar no es un problema — es el mismo escalar del ghost condensate, con la novedad
honesta de que ahora sabemos exactamente qué operadores lo encienden y qué firma (m₁≠0,
frame dragging) lo distingue.*
