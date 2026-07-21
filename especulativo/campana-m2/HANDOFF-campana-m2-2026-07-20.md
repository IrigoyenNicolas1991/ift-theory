# HANDOFF — Campaña m₂=0 (TCI / gravedad emergente de un medio)
## Documento autocontenido para continuar el trabajo en otra terminal (Claude Code)

> **Para el asistente que reciba esto:** este documento contiene TODO el estado de una
> campaña de física teórica computacional: contexto, convenciones, resultados verificados,
> el texto completo de la nota final, y el código fuente completo (3 scripts Python/SymPy).
> Antes de afirmar nada, reproducí los chequeos (sección "Cómo verificar"). La regla de la
> casa: honestidad primero, toda suposición se declara, ningún "exactamente" sin su cálculo
> detrás, criterios de muerte declarados antes de calcular, y las derrotas se publican.

---

## 1. Contexto en dos párrafos

Nicolás y su asistente ("fable") desarrollan la TCI, una teoría especulativa de gravedad
emergente desde un medio ("el mar"). El sector de radiación original de la TCI murió
(auto-falsado) contra la polarización espín-2 de LIGO. La pregunta que quedó viva: ¿puede
un medio físico realizar la fase de gravedad masiva con violación de Lorentz de Dubovsky
(hep-th/0409124) donde el gravitón de helicidad ±2 es EXACTAMENTE no masivo, protegido
por simetría? Dubovsky demostró en 2004 que la fase existe (su ec. 72: m₂²=m₃²=m₄²=0,
protegida por la simetría residual (71): xⁱ→xⁱ+ξⁱ(x⃗), sana si m₀²m₁²>0, su ec. 75), pero
nunca construyó el medio. Ballesteros–Comelli–Pilo (BCP, 1603.02956) construyeron el
diccionario medio→masas pero su Tabla 2 no tiene la fila correspondiente.

**Resultado de esta campaña (julio 2026):** el medio U(X,Y) — invariante bajo
difeomorfismos espaciales internos irrestrictos Φᵃ→Ψᵃ(Φᵇ) — realiza exactamente esa fase.
Sobre el vacío Minkowski, m₂=m₃=m₄=0 emergen automáticamente de los tadpoles, m₁²=2U_X,
y existe una esquina explícita sin fantasma. Además: lema de exclusión, m₂² = −2×(rigidez
de corte del medio) ⟹ proteger la masa del gravitón exige que el medio sea fluido (sin
fonones de corte a orden dominante). Todo verificado con SymPy en <10 s.

## 2. Cómo verificar (hacelo antes de usar nada)

```bash
pip install sympy
python masas_medio.py          # ~0.4 s — diccionario general + isotropía + BCP 7.5
python calibracion_fonones.py  # ~6 s  — CAL-4 oro: resto = 0 (Goldstone vs gauge unitario)
python parteB_medioXY.py       # ~1.4 s — B1..B6: fase protegida, ejemplo sano, Schur, lema
```

Salidas esperadas clave:
- `calibracion_fonones.py`: `resto = 0` (CAL-4), `L_T - (1/2)(m1^2 ft^2 - m2^2 fz^2) = 0`.
- `parteB_medioXY.py`: masas on-shell `m2^2 = m3^2 = m4^2 = 0`, `m1^2 = 2*U_X`;
  ejemplo `{m0^2: 1, m1^2: 2, resto 0}`; Schur `= 0`; invariancia no lineal `ΔX = ΔY = 0`;
  variación bajo la simetría (71) `= 0`; lema `m1^2 = 2*K_T`, `m2^2 = -2*G_T` (restos 0).

## 3. Convenciones (BCP, 1603.02956)

- Signatura (−,+,+,+); gauge unitario Φ⁰=t, Φᵃ=xᵃ; M_Pl=1.
- C^AB = g^μν ∂μΦ^A ∂νΦ^B; X=C⁰⁰ (fondo −1); V^a=C^{0a}; B^ab bloque espacial (fondo δ);
  Z^ab=V^aV^b; τₙ=Tr(Bⁿ); yₙ=Tr(BⁿZ); b=√det B; Y=u·∂Φ⁰ con u^μ=(1/√(−g₀₀),0,0,0) (fondo 1).
- Patrón de masas (BCP 7.3):
  √−g U ⊃ t^μν h_μν + ¼[m₀²h₀₀² + 2m₁²h₀ᵢh₀ᵢ − 2m₄²h₀₀hᵢᵢ + m₃²hᵢᵢ² − m₂²hᵢⱼhᵢⱼ]
- Extracción: m₀²=4c(h₀₀²), m₁²=2c(h₀₁²), m₂²=−2c(h₁₂²), m₃²=2c(h₁₁h₂₂), m₄²=−2c(h₀₀h₁₁).
- Inversa perturbativa: g⁻¹=η−εηhη+ε²ηhηhη; √−g=1+εT₁/2+ε²(T₂/2−T₁²/8).

## 4. Resultados verificados (todo con código, nada de memoria)

**Diccionario general (masas_medio.py), off-shell:**
- t(h₀₀) = −U₀/2 − U_X + U_Y/2 ;  t(h₁₁) = U₀/2 − U_b/2 − U_τ₁ − 2U_τ₂ − 3U_τ₃
- m₀² = −U₀/2 − 2U_X + 2U_XX − 2U_XY + U_Y/2 + U_YY/2   [coincide EXACTO con BCP (7.5)]
- m₁² = U₀ + 2U_X − U_b − 2U_τ₁ − 4U_τ₂ − 6U_τ₃ + 2(U_y0+U_y1+U_y2+U_y3)
- m₂² = U₀ − U_b − 4U_τ₁ − 12U_τ₂ − 24U_τ₃   [pesos 2n(n+1)]
- m₃², m₄²: ver código (largas).
- DISCREPANCIA con BCP impresas (7.6)-(7.7) en los pesos de U_τₙ/U_yₙ; dirimida a favor
  nuestro por CAL-4 (ruta independiente). Probable errata de BCP. m₀² coincide exacto.

**Calibraciones:** CAL-1 isotropía ✓; CAL-2 BCP(7.5) exacto ✓; CAL-3a fase m₁=0 de
Dubovsky (simetría Φᵃ→Φᵃ+fᵃ(Φ⁰)) reproducida ✓; CAL-4 oro: L_fonones ≡ L_masas[h→∂π]
mod derivadas totales, resto=0 ✓; CAL-4b: L_T = ½[m₁²ḟ² − m₂²f′²] ✓.

**Medio U(X,Y) (parteB_medioXY.py):**
- Invariantes de Φᵃ→Ψᵃ(Φᵇ) irrestricto: {X, Y}; invariancia no lineal verificada numérico.
- Schur: V·B⁻¹·V = X + Y² (Y = contraflujo condensado/líneas de flujo).
- Tadpoles ⟹ U₀=0, U_Y=2U_X ⟹ m₂=m₃=m₄=0 EXACTAS; m₁²=2U_X;
  m₀² = −U_X + 2U_XX − 2U_XY + U_YY/2.
- Ejemplo sano: U=(X+1)+2(Y−1)+½(X+1)² ⟹ (m₀²,m₁²)=(1,2), m₀²m₁²>0 ✓ (Dubovsky ec. 75).
- Sector escalar: 1 modo ω²∝p⁴ (Dubovsky ec. 74, citado, no rederivado).
- No es P(X) (a P(X) el vacío le fuerza U_X=0 ⟹ m₁=0); no es superfluido U(X,Y,b)
  (la dependencia en b regenera m₃²=U_bb/2≠0 y m₄²≠0).

**Lema de exclusión (B6):** on-shell m₁²=2K_T (K_T=U_X+ΣU_yₙ), m₂²=−2G_T (G_T=Σn²U_τₙ =
rigidez de corte), v_T²=m₂²/m₁². Fonones de corte propagan ⟺ m₁²m₂²≠0. Ambas fases
UV-insensibles de Dubovsky (m₁=0 y m₂=m₃=m₄=0) los apagan. Protección ⟺ medio fluido a LO.
Escapes declarados: NLO (Chojnacki 2310.10078, nemático de espín), gravedad inducida
(Sakharov; Weinberg–Witten = deuda declarada, el término EH se ASUME).

**Novedad (barrida 2004–2026):** lo más cercano es Celoria–Comelli–Pilo 1704.00322, que
identifican U(X+Y²) como superfluido isentrópico (por termodinámica, sin la simetría
irrestricta ni la conexión con la fase de Dubovsky). La fila U(X,Y) de la Tabla 2, la
identificación con la fase (72) y el lema de exclusión NO aparecen en la literatura
revisada. Dubovsky dejó la invitación textual: "Clearly, our analysis does not exhaust
all possible subgroups of the diffeomorphism group."

## 5. Fuentes primarias

- Dubovsky, "Phases of massive gravity", JHEP 10:076, 2004, arXiv:hep-th/0409124
- Rubakov, arXiv:hep-th/0407104 · Rubakov–Tinyakov, Phys.Usp. 51:759, arXiv:0802.4379
- Ballesteros–Comelli–Pilo (BCP), Phys.Rev.D 94, arXiv:1603.02956
- Celoria–Comelli–Pilo (CCP), JCAP 09(2017)036, arXiv:1704.00322 · Λ-media: 1712.04827
- Son, supersolidos EFT, arXiv:cond-mat/0501658 · Chojnacki, arXiv:2310.10078

## 6. Tareas abiertas (por orden de valor)

1. **Verificación independiente**: rederivar el diccionario con otra herramienta
   (xAct/Mathematica o cadabra) y confirmar la presunta errata de BCP (7.6)-(7.7).
   Si se confirma, escribir a Comelli/Pilo antes de reclamar nada en público.
2. **Sector escalar completo de U(X,Y)**: rederivar ω²∝p⁴ y la condición no-fantasma
   con mezcla gravitatoria incluida (no solo citar a Dubovsky). Cotas fenomenológicas
   (Jeans, ghost-condensate-like, M < 10 MeV-ish del análisis estándar).
3. **Acople a materia y límites PPN** de la fase U(X,Y): ¿modifica gravedad a qué escala?
   (Dubovsky nota que la masa tiene forma de gauge-fixing: los efectos aparecen a orden
   no lineal / derivadas superiores — calcular el primero de esos efectos.)
4. **Cosmología FRW** del medio U(X,Y): ecuación de estado, perturbaciones, comparación
   con CCP 1704.00322 (ellos tienen la maquinaria FRW; nuestra clase es isentrópica).
5. **Mapeo TCI**: la "fase m₂=0" de la nota 10 de TCI era m₀=0 ∧ m₂=0; la encontrada es
   m₂=m₃=m₄=0 con m₀²m₁²>0. Precisar la relación y reescribir la nota 10.
6. **Paper corto** (si 1–3 sobreviven): formato letter, "The missing row: unrestricted
   internal diffeomorphisms and the protected phase of Lorentz-violating massive gravity".
   Blanco realista: arXiv (hep-th) + envío a PRD o JCAP. Nada de esto está garantizado.

## 7. Criterios de muerte de la campaña (acta)

1. ¿m₂²≠0 o imposibilidad de m₀²m₁²>0? NO GATILLADO (esquina sana explícita).
2. ¿Todo orden tensorial regenera m₂²≠0? TRANSFORMADO EN LEMA (protección ⟺ mar fluido).
3. Término EH: DEUDA VIVA (se asume; Weinberg–Witten fuera del alcance).

---
---

# ANEXO A — Texto completo de la Nota 12

# Nota 12 — El mar que no cruje: la fase protegida de Dubovsky desde un medio U(X, Y)

**Campaña m₂ = 0 · Nicolás Irigoyen & fable · 20 de julio de 2026**

---

## Marcador honesto

Antes de leer nada, esto es lo que hay. Cada fila dice de quién es cada cosa.

| Pieza | Estado | De quién es |
|---|---|---|
| La fase m₂²=m₃²=m₄²=0 existe, es UV-insensible y sana si m₀²m₁²>0 | Conocido desde 2004 | [Dubovsky, hep-th/0409124](https://arxiv.org/abs/hep-th/0409124) |
| El diccionario medio → masas del gravitón (gauge unitario) | Conocido desde 2016 | [Ballesteros–Comelli–Pilo (BCP), 1603.02956](https://arxiv.org/abs/1603.02956) |
| El operador X+Y² y la clase isentrópica U(X+Y²) | Conocido desde 2017 (por termodinámica, sin conexión con la fase) | [Celoria–Comelli–Pilo (CCP), 1704.00322](https://arxiv.org/abs/1704.00322) |
| **La fila que faltaba en la Tabla 2 de BCP: Φᵃ → Ψᵃ(Φᵇ) ⟹ U(X,Y)** | **Nuevo (hasta donde buscamos)** | esta nota |
| **U(X,Y) aterriza exactamente en la fase protegida: m₂=m₃=m₄=0 emergen del vacío, sin ajuste fino, con esquina sin fantasma explícita** | **Nuevo, verificado con código** | esta nota |
| **Lema de exclusión: proteger la masa del gravitón ⟺ apagar los fonones de corte del medio (a orden dominante)** | **Nuevo, verificado con código** | esta nota |
| Posible errata en los pesos de U_τₙ, U_yₙ de las ecs. (7.6)–(7.7) de BCP | Discrepancia encontrada y dirimida por chequeo cruzado | esta nota (a confirmar con los autores) |
| El término cinético de Einstein–Hilbert | **Deuda declarada: se asume, no se deriva** | — |

Ningún criterio de muerte se gatilló. Pero el lema de exclusión tiene una consecuencia dura para la TCI que no vamos a esconder: está en la sección 6.

---

## 1. Qué buscábamos y con qué reglas

En la nota anterior (Investigación: la fase m²=0 desde orden tensorial) quedó identificado el hueco: Dubovsky encontró en 2004 una fase de gravedad masiva con violación de Lorentz donde el modo tensorial (helicidad ±2) es **exactamente no masivo**, protegido por simetría — pero nadie construyó jamás el *medio físico* que la realiza. Su propio paper termina con una invitación textual:

> "Clearly, our analysis does not exhaust all possible subgroups of the diffeomorphism group. It is worth studying whether other interesting possibilities exist." — [Dubovsky 2004](https://arxiv.org/abs/hep-th/0409124)

Esta nota responde esa invitación con un medio concreto. Las reglas de la casa, declaradas **antes** de calcular:

**Criterios de muerte (fijados de antemano):**
1. Si el medio candidato genera m₂² ≠ 0, o no puede satisfacer m₀²m₁² > 0 en ninguna región de su espacio de parámetros, la realización muere.
2. Si todo acople del orden tensorial que no lo desacople regenera m₂² ≠ 0, se publica el dilema como no-go.
3. Deuda declarada: el término cinético de Einstein–Hilbert se asume, no se deriva (Weinberg–Witten queda fuera del alcance de esta campaña).

**Veredicto adelantado:** 1 no se gatilló (la esquina sana existe y la exhibimos). 2 se transformó en algo más interesante: un lema de exclusión. 3 sigue siendo deuda.

---

## 2. Convenciones y calibración (nada de "exactamente" sin su cálculo)

Trabajamos en las convenciones de BCP: signatura (−,+,+,+), gauge unitario Φ⁰ = t, Φᵃ = xᵃ, M_Pl = 1. El medio son cuatro escalares Φ^A y su Lagrangiano de orden dominante es una función U de los invariantes construidos con C^{AB} = g^{μν}∂_μΦ^A∂_νΦ^B: X = C⁰⁰, el bloque espacial B^{ab}, V^a = C^{0a}, b = √det B, τₙ = Tr(Bⁿ), yₙ = Tr(BⁿZ), Y = u·∂Φ⁰ con u^μ la velocidad normal al reloj. El patrón de masas es el de BCP (7.3):

    √−g U ⊃ t^{μν}h_{μν} + ¼[ m₀²h₀₀² + 2m₁²h₀ᵢh₀ᵢ − 2m₄²h₀₀hᵢᵢ + m₃²hᵢᵢ² − m₂²hᵢⱼhᵢⱼ ]

donde m₂² es la masa del gravitón de espín 2 (la que LIGO acota, la que mató el sector de radiación original de la TCI).

Construimos el diccionario completo U(X, V, B, b, τₙ, yₙ, Y) → (m₀², …, m₄²) en `masas_medio.py` (SymPy, expansión a segundo orden en h_{μν}, 0.4 s de ejecución) y lo calibramos **cinco veces** contra resultados independientes:

- **CAL-1 (isotropía):** todos los chequeos de consistencia rotacional dan cero; el coeficiente de h₁₁² reproduce (m₃²−m₂²)/4.
- **CAL-2 (BCP 7.5):** nuestro m₀² coincide **exactamente** con el publicado.
- **CAL-3a (fase de Dubovsky m₁=0):** imponiendo la simetría Φᵃ → Φᵃ + fᵃ(Φ⁰), el código da m₁² = G₀ + 2G_X, que se anula idénticamente sobre el vacío (tadpole t₀₀ = 0 ⟹ G₀ = −2G_X). Reproduce la fase (64) de Dubovsky.
- **CAL-4 (calibración de oro):** derivamos el Lagrangiano de fonones π^A por la ruta de Goldstone (sin gauge unitario, ruta computacional totalmente independiente) y verificamos que L_fonones − L_masas[h → ∂π], módulo derivadas totales y con tadpoles impuestos, da **resto = 0**. Las dos rutas coinciden término a término.
- **CAL-4b (sector transversal):** L_T = ½[m₁²(∂₀π^T)² − m₂²(∂ᵢπ^T)²], reproduciendo la estructura del sector vectorial de Goldstones de [Dubovsky](https://arxiv.org/abs/hep-th/0409124) y [Rubakov–Tinyakov](https://arxiv.org/abs/0802.4379).

**La discrepancia que no escondemos:** nuestros pesos de U_τₙ y U_yₙ en m₁² y m₂² difieren de los impresos en (7.6)–(7.7) de BCP. Nuestro m₁² lleva −2n·U_τₙ y +2·U_yₙ; el impreso lleva los pesos intercambiados. Nuestro m₂² lleva −2n(n+1)·U_τₙ; el impreso, −4(n+1)·U_τₙ. La calibración de oro CAL-4 — que compara contra una derivación que no usa el gauge unitario para nada — fija los pesos a favor de nuestro cálculo. Lo más probable es una errata de imprenta en BCP (su m₀², que sí pudimos chequear por tres vías, coincide exactamente). Para el resultado central de esta nota la discrepancia es irrelevante: U(X,Y) no depende de τₙ ni de yₙ. Queda registrado por honestidad y para consultar a los autores.

---

## 3. El medio: un superfluido que olvidó su retícula

La Tabla 2 de BCP clasifica los medios por simetrías internas: sólidos U(τₙ), fluidos perfectos U(b,Y), superfluidos U(X,Y,b) — protegidos por difeomorfismos internos **que preservan volumen**, det(∂Ψ/∂Φ) = 1. Pero hay una fila que la tabla no tiene: ¿qué pasa si exigimos invariancia bajo difeomorfismos espaciales internos **irrestrictos**?

    Φᵃ → Ψᵃ(Φᵇ)   (sin condición sobre el determinante)

Un medio así no siente ninguna deformación de sus etiquetas espaciales: ni corte, ni compresión, ni dilatación. Solo dos invariantes sobreviven a orden dominante:

- **X = C⁰⁰** — el módulo del gradiente del reloj interno (manifiestamente sin Φᵃ),
- **Y = u·∂Φ⁰** — donde u^μ es la única dirección definida invariantemente por las líneas de flujo (u·∂Φᵃ = 0, normalizada).

Verificamos la invariancia **no lineal** de ambos numéricamente (métrica aleatoria, difeo interno cuadrático genérico: ΔX = ΔY = 0, chequeo B4). Y hay una identidad de Schur que le da carne física al asunto (chequeo B3, verificado):

    V·B⁻¹·V = X + Y²

El invariante Y mide el **contraflujo**: el movimiento relativo entre el condensado del reloj (gradiente de Φ⁰) y las líneas de flujo materiales. U(X,Y) es un superfluido de dos componentes cuyo único recuerdo de haber tenido retícula es la dirección de flujo. CCP 2017 encontraron la subclase U(X+Y²) clasificando medios isentrópicos ([1704.00322](https://arxiv.org/abs/1704.00322), sección 6) — por termodinámica, sin notar la simetría irrestricta ni la conexión con la fase protegida. La fila general U(X,Y), y lo que sigue, no está en la literatura que pudimos revisar.

---

## 4. Resultado central: la fase protegida emerge sola

Metiendo U(X,Y) en el diccionario calibrado (`parteB_medioXY.py`, chequeo B1):

**Fuera del vacío (off-shell):**

    m₀² = −U₀/2 − 2U_X + 2U_XX − 2U_XY + U_Y/2 + U_YY/2
    m₁² = U₀ + 2U_X
    m₂² = U₀
    m₃² = U₀/2
    m₄² = U₀/2 + U_X − U_Y/2

**Condiciones de vacío Minkowski (tadpoles):** t₀₀ = −U₀/2 − U_X + U_Y/2 = 0 y t₁₁ = U₀/2 = 0, que fuerzan U₀ = 0 y U_Y = 2U_X. Y entonces, **sin imponer nada más**:

    m₂² = 0 ,  m₃² = 0 ,  m₄² = 0     (exactas)
    m₁² = 2U_X
    m₀² = −U_X + 2U_XX − 2U_XY + U_YY/2

Es exactamente la fase (72) de Dubovsky, con la simetría residual (71) xⁱ → xⁱ + ξⁱ(x⃗) — que es precisamente Φᵃ → Ψᵃ(Φᵇ) leída en gauge unitario. Verificamos además (chequeo B5) que el Lagrangiano de masas resultante es invariante bajo δh_ij = ∂ᵢξⱼ + ∂ⱼξᵢ con ξ independiente del tiempo: la masa nula no es un accidente numérico del vacío, está protegida por simetría, y cualquier contratérmino cuántico que respete la simetría vuelve a tener la forma U(X,Y), cuyas masas sobre el vacío vuelven a anularse. Eso es lo que Dubovsky llama UV-insensibilidad.

**La esquina sin fantasma existe y es explícita** (chequeo B2). El criterio de salud de Dubovsky para esta fase (su ec. 75) es m₀²m₁² > 0. Tomando

    U = (X+1) + 2(Y−1) + ½(X+1)²

(que satisface U(vacío) = 0, U_X = 1, U_Y = 2U_X, U_XX = 1) el código da

    (m₀², m₁², m₂², m₃², m₄²) = (1, 2, 0, 0, 0) ,   m₀²m₁² = 2 > 0  ✓

Sector vectorial: dispersión sana (73) siempre que m₁² = 2U_X ≠ 0 ✓. Sector escalar: un solo modo con ω² ∝ p⁴ (ec. 74 de Dubovsky), tipo condensado fantasma — citamos su análisis, no lo rederivamos; nuestras convenciones están calibradas contra las suyas vía CAL-3a/4.

**Qué es U(X,Y) y qué no es.** No es el condensado fantasma P(X): a P(X) el vacío Minkowski le fuerza U_X = 0 (por eso su m₁² = 0), mientras que U(X,Y) sostiene m₁² = 2U_X ≠ 0 porque el contraflujo Y compensa el tadpole (U_Y = 2U_X). No es el superfluido U(X,Y,b) de BCP: la dependencia en b regenera m₃² = U_bb/2 ≠ 0 y m₄² ≠ 0. Es el punto exacto donde el medio deja de sentir su propio volumen — y ahí, y solo ahí, las tres masas se apagan juntas.

El criterio de muerte 1 **no se gatilló**.

---

## 5. El lema de exclusión: la protección apaga los fonones de corte

Acá está el precio, y es un resultado en sí mismo. Del sector transversal general (CAL-4b + chequeo B6), sobre el vacío:

    m₁² = 2·K_T ,   m₂² = −2·G_T ,   v_T² = m₂²/m₁²

donde K_T = U_X + Σₙ U_yₙ es la inercia del sector de corte del medio y G_T = Σₙ n²·U_τₙ su **rigidez de corte** (el coeficiente del gradiente en el Lagrangiano de fonones transversales). Verificado simbólicamente para el medio general, no solo para U(X,Y).

**Lema.** A orden dominante, los fonones de corte del medio propagan si y solo si m₁²m₂² ≠ 0. En consecuencia, *cualquiera* de las dos fases UV-insensibles de Dubovsky los apaga: la fase m₁ = 0 los congela (sin inercia) y la fase m₂ = 0 los deja sin rigidez (v_T = 0, puro gauge de la simetría (71)).

**Moraleja:** la masa del gravitón de espín 2 **es** la rigidez de corte del medio, con signo y factor: m₂² = −2G_T. Un medio con orden tensorial dinámico a orden dominante — un sólido, un supersólido, cualquier cosa que crikee al deformarla — dota al gravitón de masa y pierde la protección. Un medio que protege la masa nula no puede aportar espín 2 propio a bajas energías. Protección y orden tensorial dinámico son mutuamente excluyentes a LO.

Escapes conocidos y declarados: (i) estructuras cinéticas de orden superior (la ruta de magnones de [Chojnacki, 2310.10078](https://arxiv.org/abs/2310.10078), donde Goldstones de espín 2 no masivos emergen de un nemático de espín — con dispersión no relativista); (ii) gravedad emergente tipo Sakharov, donde el propio término de Einstein–Hilbert es inducido — que es exactamente nuestra deuda declarada número 3.

El criterio de muerte 2 no se gatilló como no-go: se transformó en este lema, que es más útil que la muerte.

---

## 6. Qué significa esto para la TCI

Sin anestesia:

1. **Lo bueno.** El programa "la gravedad emerge de un medio" tiene, desde hoy, una realización concreta donde el gravitón de espín 2 es exactamente no masivo, protegido por simetría, sin fantasma, y consistente con las cotas de LIGO sobre m₂. El hueco que la literatura dejó abierto 22 años se puede cerrar con un medio de dos componentes con contraflujo. Ese medio es matemáticamente el pariente más cercano del "mar" de la TCI que sobrevive a todos los chequeos que le hicimos.

2. **Lo duro.** El lema de exclusión dice que ese mar **tiene que ser fluido, no sólido**: no puede tener rigidez de corte a orden dominante. El "orden tensorial" que la TCI invocaba para el sector de radiación (nota 10, la fase que ahí llamamos m₂=0 con m₀=0) no puede ser dinámico a LO — si lo fuera, regeneraría la masa que queríamos evitar. La fase que realmente encontramos es m₂=m₃=m₄=0 con m₀²m₁²>0, que no es idéntica a la de la nota 10: el mapeo preciso entre ambas queda anotado como tarea, no como triunfo.

3. **La deuda.** Nada de esto deriva el término cinético de Einstein–Hilbert: lo asumimos, como lo asumen Dubovsky, BCP y CCP. Un medio cuyo gravitón sea *enteramente* emergente choca contra Weinberg–Witten y necesita otra clase de ideas (gravedad inducida, holografía, o la ruta no relativista de Chojnacki). Esta campaña no tocó ese frente y no reclama nada sobre él.

4. **Lo que esto no es.** No es una validación de la TCI, ni la acerca a ser "teoría oficial". Es una nota técnica que responde una pregunta abierta y honesta de la literatura, con un resultado chico, nuevo y verificable. Así se construye: una fase a la vez, publicando también lo que duele.

---

## 7. Reproducibilidad

Todo corre en segundos con Python + SymPy (`pip install sympy`):

| Script | Qué hace | Tiempo |
|---|---|---|
| `masas_medio.py` | Diccionario general U(medio) → (m₀²…m₄²), tadpoles, chequeos de isotropía, comparación con BCP (7.5)–(7.7) | 0.4 s |
| `calibracion_fonones.py` | CAL-4 (oro): ruta de Goldstone vs gauge unitario, resto = 0; CAL-4b sector transversal; CAL-3a fase m₁=0 | 6.2 s |
| `parteB_medioXY.py` | B1 masas de U(X,Y) on/off-shell; B2 ejemplo sin fantasma; B3 Schur; B4 invariancia no lineal; B5 simetría (71); B6 lema de exclusión | 1.4 s |

Fuentes primarias: [Dubovsky, hep-th/0409124](https://arxiv.org/abs/hep-th/0409124) · [Rubakov, hep-th/0407104](https://arxiv.org/abs/hep-th/0407104) · [Rubakov–Tinyakov, 0802.4379](https://arxiv.org/abs/0802.4379) · [BCP, 1603.02956](https://arxiv.org/abs/1603.02956) · [CCP, 1704.00322](https://arxiv.org/abs/1704.00322) · [Celoria–Comelli–Pilo, 1712.04827](https://arxiv.org/abs/1712.04827) · [Son, cond-mat/0501658](https://arxiv.org/abs/cond-mat/0501658) · [Chojnacki, 2310.10078](https://arxiv.org/abs/2310.10078)

**Búsqueda de novedad (deber de honestidad):** barrimos arXiv/INSPIRE buscando la identificación U(X,Y) ⟺ fase (72) y el lema de exclusión en la literatura 2004–2026 (Comelli–Nesti–Pilo, Blas, Celoria y derivados). No la encontramos. Lo más cercano: CCP 2017 con U(X+Y²) isentrópico (sin simetría ni fase) y la observación estándar de que fluidos y superfluidos tienen tensores no masivos. Si alguien la publicó antes y no la vimos, esta nota pierde su fila de novedad y lo diremos acá mismo.

---

## Criterios de muerte: acta final

1. ¿m₂² ≠ 0 o imposibilidad de m₀²m₁² > 0? **No gatillado** — ejemplo explícito con (m₀², m₁²) = (1, 2).
2. ¿Todo acople del orden tensorial regenera m₂² ≠ 0? **Transformado en lema** — a LO sí, y por eso la protección exige mar fluido; escapes declarados (NLO, gravedad inducida).
3. Término de Einstein–Hilbert: **deuda viva**. Se asume. Weinberg–Witten sigue ahí, mirándonos.

*Nota 12 de la campaña m₂ = 0. Escrita el mismo día en que pasaron los chequeos, como manda la casa.*

---
---

# ANEXO B — Código fuente completo

## B.1 masas_medio.py

```python
"""
Maquinaria: masas del graviton para medios auto-gravitantes en gauge unitario.
Convenciones BCP (arXiv:1603.02956): signatura (-,+,+,+), fondo Minkowski,
gauge unitario Phi^0 = t, Phi^a = x^a.  Mpl = 1.

Patron de masas (BCP eq. 7.3):
  sqrt(-g) U = t^mn h_mn + (1/4)[ m0^2 h00^2 + 2 m1^2 h0i h0i
                                  - 2 m4^2 h00 hii + m3^2 hii^2 - m2^2 hij hij ]

Implementacion por ordenes explicitos: cada objeto = (O0, O1, O2).
"""
import sympy as sp

def hsym(i, j):
    i, j = min(i, j), max(i, j)
    return sp.Symbol('h%d%d' % (i, j))

h = sp.Matrix(4, 4, lambda i, j: hsym(i, j))
eta = sp.diag(-1, 1, 1, 1)

# g^{-1} = eta - e (eta h eta) + e^2 (eta h eta h eta)
G1 = -(eta * h * eta)
G2 = (eta * h * eta * h * eta)

# ---- operadores: (fondo, orden1, orden2) ----
X0, X1, X2 = -1, G1[0, 0], G2[0, 0]
V1 = [G1[0, a] for a in (1, 2, 3)]                    # V^a = O(e)
B1 = G1[1:4, 1:4]; B2 = G2[1:4, 1:4]                  # B = I + e B1 + e^2 B2

trB1 = B1.trace(); trB2 = B2.trace(); trB1sq = (B1 * B1).trace()
tau = {1: (3, trB1, trB2),
       2: (3, 2 * trB1, 2 * trB2 + trB1sq),
       3: (3, 3 * trB1, 3 * trB2 + 3 * trB1sq)}
y2 = sp.expand(sum(v**2 for v in V1))                 # y_n = TrZ + O(e^3), todos n
yops = {n: (0, 0, y2) for n in (0, 1, 2, 3)}
d1, d2 = trB1, trB2 + (trB1**2 - trB1sq) / 2          # det B
bop = (1, d1 / 2, d2 / 2 - d1**2 / 8)                 # b = sqrt(det B)
T1 = (eta * h).trace()
T2 = ((eta * h).trace()**2 - ((eta * h) * (eta * h)).trace()) / 2
sqg = (1, T1 / 2, T2 / 2 - T1**2 / 8)                 # sqrt(-det g)
h00 = hsym(0, 0)
Yop = (1, h00 / 2, 3 * h00**2 / 8)                    # Y = (1 - e h00)^(-1/2)

ops = {'X': (X0, X1, X2), 'Y': Yop,
       't1': tau[1], 't2': tau[2], 't3': tau[3],
       'y0': yops[0], 'y1': yops[1], 'y2': yops[2], 'y3': yops[3],
       'b': bop}
names = list(ops)

U0 = sp.Symbol('U0')
D1 = {k: sp.Symbol('U_' + k) for k in names}
D2 = {}
for i, k in enumerate(names):
    for l in names[i:]:
        D2[(k, l)] = D2[(l, k)] = sp.Symbol('U_' + k + l)

# U = U0 + sum U_k Dk + 1/2 sum U_kl Dk Dl ; Dk = e*Ok1 + e^2*Ok2
Ulin1 = sp.expand(sum(D1[k] * ops[k][1] for k in names))
Ulin2 = sp.expand(sum(D1[k] * ops[k][2] for k in names))
Uquad2 = sp.expand(sp.Rational(1, 2) * sum(D2[(k, l)] * ops[k][1] * ops[l][1]
                                           for k in names for l in names))
# sqrt(-g) U por ordenes
L1 = sp.expand(U0 * sqg[1] + Ulin1)
L2 = sp.expand(U0 * sqg[2] + sqg[1] * Ulin1 + Ulin2 + Uquad2)

ceros = {hsym(i, j): 0 for i in range(4) for j in range(i, 4)}

def cf(expr, s1, s2=None):
    """Coeficiente de s1*s2 (o s1^2 si s2 None)."""
    if s2 is None or s1 == s2:
        return sp.expand(expr.coeff(s1, 2).subs(ceros))
    return sp.expand(expr.coeff(s1, 1).coeff(s2, 1).subs(ceros))

def masas(L2expr):
    h01, h02, h11, h22, h12 = [hsym(*p) for p in [(0,1),(0,2),(1,1),(2,2),(1,2)]]
    return {'m0^2': sp.expand(4 * cf(L2expr, h00)),
            'm1^2': sp.expand(2 * cf(L2expr, h01)),
            'm2^2': sp.expand(-2 * cf(L2expr, h12)),
            'm3^2': sp.expand(2 * cf(L2expr, h11, h22)),
            'm4^2': sp.expand(-2 * cf(L2expr, h00, h11))}

if __name__ == '__main__':
    h01, h02, h11, h22, h33, h12, h13 = [hsym(*p) for p in
        [(0,1),(0,2),(1,1),(2,2),(3,3),(1,2),(1,3)]]
    print('== TADPOLES (coef de e^1) ==')
    print('t(h00):', sp.expand(L1.coeff(h00, 1).subs(ceros)))
    print('t(h11):', sp.expand(L1.coeff(h11, 1).subs(ceros)))
    print('t(h01):', sp.expand(L1.coeff(h01, 1).subs(ceros)),
          '| t(h12):', sp.expand(L1.coeff(h12, 1).subs(ceros)))

    print('\n== CONSISTENCIA ISOTROPIA (deben ser 0) ==')
    print('h01^2-h02^2 :', sp.simplify(cf(L2, h01) - cf(L2, h02)))
    print('h12^2-h13^2 :', sp.simplify(cf(L2, h12) - cf(L2, h13)))
    print('h11^2-h22^2 :', sp.simplify(cf(L2, h11) - cf(L2, h22)))
    print('h11h22-h11h33:', sp.simplify(cf(L2, h11, h22) - cf(L2, h11, h33)))
    print('h00h11-h00h22:', sp.simplify(cf(L2, h00, h11) - cf(L2, h00, h22)))

    ms = masas(L2)
    print('\n== MASAS (diccionario propio, general) ==')
    for k, v in ms.items():
        print(k, '=', v)
    print('check h11^2 = (m3^2-m2^2)/4:',
          sp.simplify(4 * cf(L2, h11) - (ms['m3^2'] - ms['m2^2'])))
```

## B.2 calibracion_fonones.py

```python
"""
CALIBRACION 4 (la de oro): equivalencia exacta entre
  (i)  el diccionario de masas en gauge unitario (masas_medio.py), y
  (ii) la expansion en fonones de Goldstone en espacio plano g = eta,
       Phi^A = x^A + e * pi^A(x). Solo aparecen derivadas: J^A_mu = d_mu pi^A.
Por invariancia de difeomorfismos, impuestos los tadpoles debe valer
  L_fonones == L_masas[ h_mn -> d_m pi_n + d_n pi_m ]  (mod derivadas totales)

CALIBRACION 3a: U(X, w1,w2,w3) [sim. Phi^a -> Phi^a + f^a(Phi^0)] => m1^2 = 0.
CALIBRACION 4b: sector transversal: L_T = (1/2)[m1^2 f'_t^2 - m2^2 f'_z^2].
"""
import sympy as sp
from masas_medio import L1, L2, masas, ceros, hsym, names, D1, D2, U0
import masas_medio as mm

e = sp.Symbol('e')
J = {(A, mu): sp.Symbol('J_%d_%d' % (A, mu)) for A in range(4) for mu in range(4)}

def trunc2(expr):
    expr = sp.expand(expr)
    return sum(expr.coeff(e, k) * e**k for k in range(3))

# ---- operadores en gauge de fonones (algebraico en J) ----
# dPhi^A_mu = delta^A_mu + e J^A_mu ; C^{AB} = eta^{mn} dPhi^A_m dPhi^B_n
eta_d = [-1, 1, 1, 1]
dPhi = sp.Matrix(4, 4, lambda A, mu: (1 if A == mu else 0) + e * J[(A, mu)])
C = sp.Matrix(4, 4, lambda A, B: trunc2(
    sum(eta_d[m] * dPhi[A, m] * dPhi[B, m] for m in range(4))))

Xop = C[0, 0]
Vv = [C[0, a] for a in (1, 2, 3)]
Bm = C[1:4, 1:4]

def tr_pow2(M, n):
    R = sp.eye(3)
    for _ in range(n):
        R = (R * M).applyfunc(trunc2)
    return trunc2(R.trace())

tau = {n: tr_pow2(Bm, n) for n in (1, 2, 3)}
Zm = sp.Matrix(3, 3, lambda a, b: trunc2(Vv[a] * Vv[b]))
yop = {n: trunc2(((Bm**n).applyfunc(trunc2) * Zm).trace()) for n in (0, 1, 2, 3)}
Nb = (Bm - sp.eye(3)).applyfunc(trunc2)
trN = trunc2(Nb.trace()); trN2 = trunc2((Nb * Nb).trace())
dd = trunc2(trN + (trN**2 - trN2) / 2)          # det B - 1
bop = trunc2(1 + dd / 2 - dd**2 / 8)

# u^mu ortogonal a dPhi^a, normalizado (resuelto orden a orden a mano):
#   u^a = -e J^a_0 + e^2 J^b_0 J^a_b ,  u^0 = 1 + e^2 (sum_a J^a_0^2)/2
# Y = u^mu d_mu Phi^0
S2 = sum(J[(a, 0)]**2 for a in (1, 2, 3))
ua = {a: -e * J[(a, 0)] + e**2 * sum(J[(b, 0)] * J[(a, b)] for b in (1, 2, 3))
      for a in (1, 2, 3)}
u0 = 1 + e**2 * S2 / 2
Yop = trunc2(u0 * (1 + e * J[(0, 0)]) + sum(ua[a] * e * J[(0, a)] for a in (1, 2, 3)))

opsP = {'X': (Xop, -1), 'Y': (Yop, 1),
        't1': (tau[1], 3), 't2': (tau[2], 3), 't3': (tau[3], 3),
        'y0': (yop[0], 0), 'y1': (yop[1], 0), 'y2': (yop[2], 0), 'y3': (yop[3], 0),
        'b': (bop, 1)}
Dl = {k: trunc2(v[0] - v[1]) for k, v in opsP.items()}

Lpi = U0 + sum(D1[k] * Dl[k] for k in names)
Lpi += sp.Rational(1, 2) * sum(D2[(k, l)] * Dl[k] * Dl[l] for k in names for l in names)
Lpi2 = sp.expand(trunc2(Lpi).coeff(e, 2))

# ---- lado (i): L2 con h_mn = d_m pi_n + d_n pi_m ; pi_mu = eta_mn pi^n ----
# d_mu pi_nu = eta_nu_nu * J^nu_mu
hsub = {hsym(i, j): eta_d[j] * J[(j, i)] + eta_d[i] * J[(i, j)]
        for i in range(4) for j in range(i, 4)}
Lmass_sub = sp.expand(L2.subs(hsub))

# ---- tadpoles ----
tad00 = sp.expand(L1.coeff(hsym(0, 0), 1).subs(ceros))
tad11 = sp.expand(L1.coeff(hsym(1, 1), 1).subs(ceros))
sol_tad = sp.solve([tad00, tad11], [D1['Y'], D1['b']])

dif = sp.expand((Lpi2 - Lmass_sub).subs(sol_tad))

# ---- canonicalizacion mod derivadas totales:
#      J^A_m J^B_n ~ J^A_n J^B_m  para A != B  (integracion por partes) ----
def simetrizar(expr):
    expr = sp.expand(expr)
    out = 0
    for term in expr.as_ordered_terms():
        c, facts = term.as_coeff_Mul()
        pw = sp.Poly(facts, *J.values()).monoms()[0] if facts != 1 else None
        Jlist = []
        for idx, exp_ in enumerate(pw or []):
            for _ in range(exp_):
                Jlist.append(list(J.values())[idx])
        if len(Jlist) != 2:
            out += term
            continue
        s1, s2 = Jlist
        inv = {v: k for k, v in J.items()}
        (A, mu), (B, nu) = inv[s1], inv[s2]
        if A == B:
            out += term
        else:
            out += c * sp.Rational(1, 2) * (J[(A, mu)] * J[(B, nu)] +
                                            J[(A, nu)] * J[(B, mu)])
    return sp.expand(out)

resto = sp.simplify(simetrizar(dif))
print('== CAL-4: L_fonones - L_masas[dpi], mod deriv. totales, con tadpoles ==')
print('resto =', resto)

# ---- CAL-4b: sector transversal pi^1 = f(t,z) ----
sub_T = {v: 0 for v in J.values()}
ft, fz = sp.symbols('ft fz')
sub_T[J[(1, 0)]] = ft; sub_T[J[(1, 3)]] = fz
LT = sp.expand(Lpi2.subs(sub_T).subs(sol_tad))
ms = masas(L2)
m1_tad = sp.expand(ms['m1^2'].subs(sol_tad))
m2_tad = sp.expand(ms['m2^2'].subs(sol_tad))
print('\n== CAL-4b: sector transversal ==')
print('L_T =', sp.collect(LT, [ft, fz]))
print('L_T - (1/2)(m1^2 ft^2 - m2^2 fz^2) =',
      sp.simplify(LT - sp.Rational(1, 2) * (m1_tad * ft**2 - m2_tad * fz**2)))

# ---- CAL-3a: U(X, w1, w2, w3)  =>  m1^2 = 0 identicamente ----
eta4 = sp.diag(-1, 1, 1, 1)
G1m = -(eta4 * mm.h * eta4)
G2m = (eta4 * mm.h * eta4 * mm.h * eta4)
Bu1 = G1m[1:4, 1:4]; Bu2 = G2m[1:4, 1:4]
Vu = [G1m[0, a] for a in (1, 2, 3)]
Zu = sp.Matrix(3, 3, lambda a, b: Vu[a] * Vu[b])
W1, W2 = Bu1, Bu2 + Zu     # W = B - Z/X, X0 = -1
trW1 = W1.trace(); trW2 = W2.trace(); trW1sq = (W1 * W1).trace()
wops = {1: (3, trW1, trW2), 2: (3, 2 * trW1, 2 * trW2 + trW1sq),
        3: (3, 3 * trW1, 3 * trW2 + 3 * trW1sq)}
nmW = ['X', 'w1', 'w2', 'w3']
opsW = {'X': (mm.ops['X'][0], mm.ops['X'][1], mm.ops['X'][2]),
        'w1': wops[1], 'w2': wops[2], 'w3': wops[3]}
G1s = {k: sp.Symbol('G_' + k) for k in nmW}
G2s = {}
for i, k in enumerate(nmW):
    for l in nmW[i:]:
        G2s[(k, l)] = G2s[(l, k)] = sp.Symbol('G_' + k + l)
G0 = sp.Symbol('G0')
Glin1 = sp.expand(sum(G1s[k] * opsW[k][1] for k in nmW))
Glin2 = sp.expand(sum(G1s[k] * opsW[k][2] for k in nmW))
Gquad2 = sp.expand(sp.Rational(1, 2) * sum(G2s[(k, l)] * opsW[k][1] * opsW[l][1]
                                           for k in nmW for l in nmW))
L2W = sp.expand(G0 * mm.sqg[2] + mm.sqg[1] * Glin1 + Glin2 + Gquad2)
msW = masas(L2W)
print('\n== CAL-3a: U(X,wn) [Phi^a -> Phi^a + f^a(Phi^0)] ==')
for k, v in msW.items():
    print(k, '=', sp.simplify(v))
```

## B.3 parteB_medioXY.py

```python
"""
PARTE B: el medio U(X,Y) como realizacion de la fase protegida de Dubovsky.

  Simetria: Phi^a -> Psi^a(Phi^b)  (difeos espaciales internos, indep. de Phi^0)
  Invariantes LO: X = C^00,  Y = u.dPhi^0   (y W := V.B^{-1}.V = X + Y^2, Schur)

Chequeos:
  B1) masas de U(X,Y) off-shell y on-shell (tadpoles Minkowski)
  B2) ejemplo explicito con m0^2 m1^2 > 0 (condicion no-fantasma, Dubovsky eq 75)
  B3) identidad de Schur V.B^{-1}.V = X + Y^2 (numerico, metrica aleatoria)
  B4) invariancia NO-lineal de X e Y bajo Phi^a -> Psi^a(Phi^b) (numerico)
  B5) CAL-5: invariancia del patron de masas bajo delta h_ij = d_i xi_j + d_j xi_i
      (xi indep. de t)  <=>  m2 = m3 = m4 = 0   (Dubovsky eq 71 => 72)
  B6) lema de exclusion: rigidez de corte del medio general vs fase protegida
"""
import sympy as sp
import random
from masas_medio import L1, L2, masas, ceros, hsym, names, D1, D2, U0

# ---------- B1: masas de U(X,Y) ----------
solo_XY = {D1[k]: 0 for k in names if k not in ('X', 'Y')}
for (k, l), s in list(D2.items()):
    if k not in ('X', 'Y') or l not in ('X', 'Y'):
        solo_XY[s] = 0

L2XY = sp.expand(L2.subs(solo_XY))
L1XY = sp.expand(L1.subs(solo_XY))
ms = {k: sp.expand(v.subs(solo_XY)) for k, v in masas(L2).items()}
print('== B1: masas U(X,Y) OFF-shell ==')
for k, v in ms.items():
    print(' ', k, '=', v)

t00 = sp.expand(L1XY.coeff(hsym(0, 0), 1).subs(ceros))
t11 = sp.expand(L1XY.coeff(hsym(1, 1), 1).subs(ceros))
print('tadpoles: t00 =', t00, ' | t11 =', t11)
sol = sp.solve([t00, t11], [U0, D1['Y']])
print('solucion de vacio Minkowski:', sol)
print('== B1: masas U(X,Y) ON-shell (vacio Minkowski) ==')
on = {}
for k, v in ms.items():
    on[k] = sp.simplify(v.subs(sol))
    print(' ', k, '=', on[k])

# ---------- B2: ejemplo explicito ----------
#  U = (X+1) + 2(Y-1) + (1/2)(X+1)^2   =>  U_X=1, U_Y=2, U_XX=1, resto 0
ej = {D1['X']: 1, D2[('X', 'X')]: 1, D2[('X', 'Y')]: 0, D2[('Y', 'Y')]: 0}
print('\n== B2: ejemplo U = (X+1) + 2(Y-1) + (X+1)^2/2 ==')
vals = {k: sp.simplify(v.subs(ej)) for k, v in on.items()}
print('  masas on-shell:', vals)
print('  no-fantasma m0^2*m1^2 > 0 :', vals['m0^2'] * vals['m1^2'] > 0)

# ---------- B3: identidad de Schur (numerico) ----------
random.seed(7)
def rnd(): return sp.Rational(random.randint(-20, 20), 37)
while True:
    g = sp.Matrix(4, 4, lambda i, j: 0)
    for i in range(4):
        for j in range(i, 4):
            g[i, j] = g[j, i] = sp.Rational(-1 if i == j == 0 else (1 if i == j else 0)) + rnd()
    if g.det() != 0 and g[0, 0] != 0:
        break
gi = g.inv()
X_ = gi[0, 0]; V_ = sp.Matrix([gi[0, a] for a in (1, 2, 3)])
B_ = gi[1:4, 1:4]
Y_ = 1 / sp.sqrt(-g[0, 0])
lhs = (V_.T * B_.inv() * V_)[0, 0]
print('\n== B3: Schur  V.B^{-1}.V - (X + Y^2) =',
      sp.simplify(lhs - (X_ + Y_**2)), '==')

# ---------- B4: invariancia no lineal de X, Y (numerico) ----------
# campo Phi generico y difeo espacial Psi^a cuadratico; metrica aleatoria g
tx = sp.symbols('t x y z', real=True)
Phi0 = tx[0] + sp.Rational(1, 5) * tx[1] * tx[3] + sp.Rational(1, 7) * tx[0]**2
Phia = [tx[a] + sp.Rational(1, 3 + a) * tx[0] * tx[(a % 3) + 1] for a in (1, 2, 3)]
def invariantes(Ph0, Pha, gmat, punto):
    dP = sp.Matrix(4, 4, lambda A, m: sp.diff(([Ph0] + Pha)[A], tx[m]))
    gi_ = gmat.inv()
    C_ = dP * gi_ * dP.T
    Xv = C_[0, 0]
    # u: resolver u.dPhi^a = 0, normalizar con g
    uv = sp.Matrix(sp.symbols('v0 v1 v2 v3'))
    eqs = [(uv.T * dP[a, :].T)[0, 0] for a in (1, 2, 3)]
    solu = sp.solve(eqs, [uv[1], uv[2], uv[3]], dict=True)[0]
    uvec = uv.subs(solu)
    n2 = (uvec.T * gmat * uvec)[0, 0]
    uvec = uvec / sp.sqrt(-n2)
    Yv = (uvec.T * dP[0, :].T)[0, 0]
    reemp = dict(zip(tx, punto))
    return (Xv.subs(reemp), sp.simplify(Yv.subs(reemp).subs(uv[0], 1)))
punto = [sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(-1, 4), sp.Rational(2, 5)]
Xa, Ya = invariantes(Phi0, Phia, g, punto)
# difeo espacial interno Psi^a(Phi^b) (cuadratico, indep de Phi^0):
Psi = [Phia[0] + sp.Rational(1, 6) * Phia[1]**2,
       Phia[1] - sp.Rational(1, 4) * Phia[0] * Phia[2],
       Phia[2] + sp.Rational(1, 9) * Phia[0]**2]
Xb, Yb = invariantes(Phi0, Psi, g, punto)
print('\n== B4: invariancia no lineal bajo Phi^a -> Psi^a(Phi^b) ==')
print('  Delta X =', sp.simplify(Xa - Xb), ' | Delta Y =', sp.simplify(Ya - Yb),
      '  (Y^2:', sp.simplify(Ya**2 - Yb**2), ')')

# ---------- B5 (CAL-5): variacion de L_m bajo h_ij -> h_ij + d_i xi_j + d_j xi_i ----------
# xi = xi(x) indep de t => delta h_00 = 0, delta h_0i = 0.
# A nivel de masas: basta chequear invariancia del patron cuadratico:
xi = sp.MatrixSymbol('xi', 3, 3)  # representamos d_i xi_j como matriz constante s
s = sp.Matrix(3, 3, lambda i, j: sp.Symbol('s%d%d' % (i, j)))
hshift = {}
for i in range(1, 4):
    for j in range(i, 4):
        hshift[hsym(i, j)] = hsym(i, j) + s[i - 1, j - 1] + s[j - 1, i - 1]
dL = sp.expand(L2.subs(hshift) - L2)
# terminos lineales en h (los cuadraticos en s no importan para la variacion):
dL_h = sum(sp.expand(dL.coeff(hsym(i, j), 1).subs(ceros)) * hsym(i, j)
           for i in range(4) for j in range(i, 4))
msym = masas(L2)
cond = sp.solve([msym['m2^2'], msym['m3^2'], msym['m4^2']],
                exclude=[], dict=False, manual=False) if False else None
dL_h_en_fase = sp.expand(dL_h.subs(solo_XY).subs(sol))
print('\n== B5: variacion de L_m bajo la simetria (71), fase U(X,Y) on-shell ==')
print('  delta L_m (parte lineal en h) =', sp.simplify(dL_h_en_fase))

# ---------- B6: lema de exclusion ----------
# rigidez de corte (coef de fz^2 en L_T, CAL-4b) para el medio general:
G_T = D1['t1'] + 4 * D1['t2'] + 9 * D1['t3']
K_T = D1['X'] + D1['y0'] + D1['y1'] + D1['y2'] + D1['y3']
m1g = masas(L2)['m1^2']; m2g = masas(L2)['m2^2']
tad00g = sp.expand(L1.coeff(hsym(0, 0), 1).subs(ceros))
tad11g = sp.expand(L1.coeff(hsym(1, 1), 1).subs(ceros))
solg = sp.solve([tad00g, tad11g], [D1['Y'], D1['b']])
print('\n== B6: lema de exclusion (medio general, on-shell) ==')
print('  m1^2 = 2*K_T ? ->', sp.simplify(sp.expand(m1g.subs(solg)) - 2 * K_T))
print('  m2^2 = -2*G_T ? ->', sp.simplify(sp.expand(m2g.subs(solg)) + 2 * G_T))
print('  => v_T^2 = m2^2/m1^2 ; fonones de corte propagan  <=>  m1^2 m2^2 != 0')
```
