# Selección de estado — VERIFICADOR ADVERSARIAL FINAL

**Campaña m₂=0 · frente selección de estado · 2026-07-28 · verificador
independiente (relanzado tras corte externo; esta vez los archivos quedaron).
Pipeline PROPIO en `verificador/` (va1–va4 + cotejo), tercera parametrización
de Y (determinantes de la matriz de Gram; ni el solve-u de colB ni la forma
Levi-Civita de colA) y EH propio (acción ΓΓ de primer orden; lib_eh de las
columnas usa el Ricci con segundas derivadas). Todos los scripts corren en
esta máquina: va1 50 s · va2 4 s · va3 7 s · va4 2 s.**

## VEREDICTO FINAL: **D2 CONFIRMADO** (condicionado a las hipótesis declaradas abajo)

El teorema del congelamiento y sus consecuencias (superselección, poblamiento
co-rotante, IVP universal, fuga nula/despreciable, δ_ret ~ −c_σ/A) RESISTEN
los cinco ataques. No encontré ninguna grieta que cambie el veredicto. Cacé
dos erratas menores de redacción (una en el script a4 de colA, una mía propia
durante la auditoría, retirada) y una inconsistencia de coherencia interna en
el acta de colA (la cota nodal) que la integración debe limpiar.

---

## Ataque 1 — el teorema mismo: **RESISTE**

**Mi pipeline** (`va1_teorema.py`): tercera forma cerrada
**Y² = −det C/det B** con C^{AB} = ∂Φ^A·g⁻¹·∂Φ^B y B su bloque espacial
(equivale a (C⁻¹)₀₀ = det B/det C, cofactores). Validada contra una
construcción por nullspace (mecánicamente distinta de las tres rutas
anteriores), racional exacto (V0).

- **Invariancia GL(3) finita = álgebra lineal pura** (V1): con M = diag(1,E),
  (MCMᵀ)_esp = E·C_esp·Eᵀ (identidad simbólica de bloques) y multiplicatividad
  del determinante ⟹ Y²(MCMᵀ) = Y²(C) **exacto, off-shell, C genérica, todo
  orden**. El corolario infinitesimal es P_aᵘ∂_μΦᵇ = 0; en gauge unitario
  ∂_μΦᵇ = δᵇ_μ ⟹ **P_aᵇ = 0 sin más cálculo**.
- **P_aⁱ = 0 con métrica exacta simbólica** (V2, 9 componentes) y **fórmula
  cerrada de P_a⁰** (V3) verificadas por reducción de Jacobi
  (det(adj g)_esp = g₀₀·det g²) a identidades polinomiales de grado ≤ 9:
  d(detW)/ds − 2δ_{ai}detW₀ = 0 y d(detW)/ds + 2g₀ₐ·det g² = 0. Linealización
  P_a⁰ = −m₁²h₀ₐ + O(h²): coincide con ambas columnas.
- **(1a) La corriente de Noether COMPLETA no tiene pieza EH ni de borde** (V4):
  la transformación interna Φᵃ→Φᵃ+ξᵃ(Φ⃗) deja g y materia FIJAS ⟹ δL_EH = 0 y
  δL_mat = 0 idénticamente; δU = 0 **puntual** (V1 es identidad, no
  cuasi-invariancia) ⟹ K^μ = 0. X e Y contienen Φᵃ solo derivado ⟹
  EOM(Φᵃ) ≡ ∂_μP_aᵘ = 0. Nada omitido.
- **(1b) ¿La carga que distingue ramas es otra que sí fluye?** Atacado con la
  corriente LOCAL de campo de la realización unitaria (va2-G4, difeo
  compensador ξˣ = ε·cos(pz), mi ΓΓ de primer orden ⟹ Noether estándar sin
  Ostrogradsky): el K^μ completo resultó ser SOLO la pieza de la fuente
  externa; **J^z = 0 sobre el modo** (ni flujo gravitatorio local hay en este
  sector) y la carga modal promediada es exactamente −C/2 = la interna vía el
  vínculo. Las dos leyes (interna punto a punto / residual modal con pieza EH)
  dan la MISMA superselección. Las traslaciones reales llevan el momento total
  (igual en ambas ramas: la diferencia es dipolar con neta cero, t1[B6] de
  colB, verificado en su corrida): no distinguen las ramas y su flujo es
  irrelevante para la etiqueta de sector.
- **Refuerzo no perturbativo nuevo (respuesta al ataque 2): el corolario de
  inversión** (V5): P_a⁰ = √−g·U_Y·g₀ₐ/(g₀₀√(−g₀₀)) con factor no nulo ⟹
  **P_a⁰(x) = 0 ⟺ g₀ₐ(x) = 0, punto a punto, exacto en h**. La etiqueta de
  sector equivale al perfil completo del shift en comóviles: la separación
  co-rotante/relajada es de campo completo y no perturbativa, no un artefacto
  del modo único ni del orden lineal.

## Ataque 2 — el vínculo y las ramas fuera del modo de juguete: **RESISTE**

- Vínculo C = −m₁²S rederivado desde MI ΓΓ (va2-G1/G2: mi L modal ≡ forma
  canónica mod derivada total; 2eqS = Ap²σ + m₁²S + τ; C conservada con τ(t)
  arbitraria). Ramas y ΔC modo a modo reproducidas (G3).
- **Dos modos (p y 2p) con NLO c_σ, c_ω** (va3-X2): el L modal SEPARA
  (las 9 derivadas cruzadas = 0) y C̃(p), C̃(2p) se conservan POR SEPARADO.
  Sin fuga inter-modo a orden cuadrático. El acople inter-modo empieza en
  cúbicos, y para la CARGA los cubre el teorema exacto (P_aⁱ = 0 con g exacta,
  todo orden). **Blanco 2 de colA: cerrado.**
- **El escape "relajada + nube compensante"** (va2-G5): el sistema
  {vínculo = 0, C = 0, σ = σ_rel} NO tiene solución; el único estacionario del
  sector C = 0 es el co-rotante. "Su fundamental" es literal (y único).
- Reinterpretación energética de colB (blanco 4): verificada por mi Legendre
  (va2-G6): H(C;τ) = C²/(4m₁²) + (τ−C)²/(4Ap²), mínimo global en C_rel,
  pero C congelada.

## Ataque 3 — el IVP universal: **RESISTE**

- **Solución general cerrada** (va2-G7, más fuerte que el RK4 de colB):
  S = −C₀/m₁², Ḟ = S − (C₀−τ)/(Ap²) resuelve EXACTO con τ(t) arbitraria;
  el estado queda etiquetado solo por C₀. C₀ = 0 (FRW) ⟹ S ≡ 0.
- **Fuente que se DESPLAZA** (va3-X1, el caso que ninguna columna probó):
  T⁰ˣ = τ(t)cos(p(z−z₀(t))) con τ(t) y z₀(t) arbitrarias, T^zx fijado por
  conservación, dos cuadraturas: **S₁ = S₂ = 0 es solución exacta** (residuos
  0 en las cuatro EOM) con cargas constructivas Q₁ = Q₂ = 0 conservadas.
  La acreción con movimiento tampoco puebla la relajada: la materia transporta
  SU momento; el medio queda en carga cero.
- Retroacción métrica: el juguete YA contiene el EH dinámico y su vínculo;
  el carácter de vínculo de eqS sobrevive a c_σ/c_ω (va3-X3); y el corolario
  de inversión (va1-V5) cubre el régimen no perturbativo: con P ≡ 0 congelado,
  g₀ₐ comóvil = 0 exacto para todo t; la evolución no lineal de h_ij/h₀₀ no
  puede regenerar shift comóvil sin violar la EOM exacta de Φᵃ. Punto de
  prolijidad para la integración: el crecimiento lineal de h_xz ∝ t del
  co-rotante en gauge unitario es puro enrollamiento de etiquetas (deformación
  de corte que U(X,Y) no ve, σ constante); la descripción a t grande debe
  darse en coordenadas físicas (donde el estado es Kerr linealizado exacto).

## Ataque 4 — los números de colA: **RESISTE** (con dos manchas menores)

- **δ_ret con c_a GENÉRICO, sin reducción de orden** (va4-N1): c_a no entra en
  la carga ni en las estacionarias (a = V̇ = 0 sobre ellas) ⟹ σ_ret, σ_rel y
  ambas δ NO contienen c_a. δ_ret = −c_σ/A a O(c), factor exacto igual al de
  a4. **La reducción de orden de colA era innecesaria para el veredicto: el
  fantasma espurio (polo en |ω| ~ corte) no toca ninguna rama estacionaria.
  Blanco 3 de colA: cerrado, y más fuerte que como lo dejó A.**
- **"Sin polos ⟹ δu ≤ J₂₂v_drag" es legítimo** (va4-N2): función de
  transferencia σ̂/τ̂ derivada exacta: denominador sin raíces reales (c_a = 0)
  ⟹ sin resonancia a ω = 2Ω⊕ y sin secularidad no resonante (solución
  particular periódica); respuesta acotada por la estática 1/(Ap²).
- **Números reproducidos con mis constantes** (va4-N3/N4/N5): δ_ret 1.69e−61
  … 1.69e−43; ĉ_nec ~ 1.2e40; v_drag = 7.15e−16; **Γ_burda·t_edad = 2.74e−14 y
  Γ_estr·t_edad = 3.52e−35** (= acta); spin-down Ė(1 MeV) = 2.789e−15 W, 26.1
  órdenes bajo el margen, Sol 24.3 W (= acta). La cota de fuga es dimensional
  (no un cálculo de vértices): débil como número, robusta como veredicto
  (habría que errar 14 órdenes la cadena rota a propósito; sin polos ni
  secularidad no hay enhancement paramétrico que lo haga).
- Mancha 1 (colA): el párrafo final de `a4_numeros.py` dice "6e-14 / 7e-36";
  su PROPIA tabla (y mi recálculo) da 2.7e−14 / 3.5e−35. El acta transcribió
  la tabla (bien). Errata de redacción del script: corregir al integrar.
- Mancha 2 (mía, retirada): mi primera cuenta a mano del spin-down acusó un
  typo de 10³ en el acta; el error era MÍO (v_ec = 1.55e−6, no 1.55e−3).
  Mi propio script me corrigió. El acta estaba bien. Queda registrado por
  honestidad y como evidencia de que el cotejo funciona en ambas direcciones.

## Ataque 5 — coherencia global: **CONSISTENTE**, con UNA inconsistencia interna a limpiar

- **Teorema causal del acta ACOPLE** ("la solución causal es la co-rotante"):
  D2 lo CONFIRMA y lo extiende (la causal es además la final: sin canal de
  decaimiento). Sin contradicción.
- **§9 FRW del paper / atractor**: el atractor entrega el vacío protegido con
  carga del reloj diluida y carga vectorial idénticamente nula (F1/F2 de colB;
  mi V6). D2 USA exactamente esas CI. La "vector-freezing identity" de §9 es
  la misma estructura. Consistente.
- **Columna C**: jerarquía de canales consistente con D2 (Cherenkov escalar
  lleva energía, no carga; phase slips con barrera ∝ 1/v divergente; ³He-A:
  nuestro modo blando solo acopla gravitacionalmente). Consistente.
- **INCONSISTENCIA INTERNA (a limpiar en la integración)**: a4/P4 de colA
  declara "manda la nodal Λ ≲ 2.0–2.6 MeV". Si D2 vale — el propio veredicto
  de A — la cota nodal DEJA DE SER una cota sobre la fase (es de la rama no
  poblada): la ventana de Λ vuelve a estar regida por el sector escalar
  (ACLM-like) y las consistencias internas. No cambia ningún número de la
  campaña (la fuga empeora hacia Λ chico, no grande), pero la frase es
  incoherente con D2 y el paper no debe heredarla.

## Hipótesis de las que D2 queda condicionado (declaradas, ninguna nueva)

1. L = √−g U(X,Y) + EH a LO; NLO = invariantes del flujo u (la exhaustividad
   de la base {θ,σ,ω,a} queda como argumento estructural: todo operador
   GL(3)-invariante toca ∂Φᵃ solo vía u, y u depende de π solo vía π̇ ⟹ toda
   corriente espacial interna lleva ∂_t delante — argumento de a3/N2,
   consistente con mi V1; no es teorema formal).
2. Acople universal: la materia no toca Φᵃ directamente.
3. Φᵃ suave global (sin vórtices/phase slips) — el único escape no
   perturbativo, con barrera E_b ∝ 1/v divergente (columna C) y sin baño
   térmico conocido.
4. U_Y ≠ 0 (fase m₁² ≠ 0) y métrica regular (para el corolario de inversión).
5. Perturbaciones vectoriales primordiales ~ 0 (FRW exacto da carga
   idénticamente nula; ruido primordial diluye a⁻³ y no puede conspirar el
   perfil dipolar correlacionado con la fuente).

## Frases del acta ACOPLE que quedan corregidas por D2 (para la integración — NO editadas acá)

1. «El estado co-rotante … **decae al Yukawa con cualquier disipación**» —
   REFUTADA (no existe canal que respete la simetría; el co-rotante es el
   fundamental de su sector).
2. «(medio en su fundamental)» para la relajada / «estado genuinamente
   EXCITADO» para la co-rotante — REINTERPRETAR: fundamental global de OTRO
   sector de superselección vs fundamental (y único estacionario) del sector
   poblado C = 0.
3. «la cota se debilita 2.7×: lo defendible hoy es **Λ ≲ 2.0–2.6 MeV** …
   LARES-2 … llegaría a Λ < 1.12 MeV … **la ventana está abierta y el test es
   real**» — pasa a CONDICIONAL-CONTRAFÁCTICO: cota de la rama relajada, que
   la superselección deja sin poblar; el test no distingue la fase de RG.
4. «La predicción del apantallamiento es **condicional a que el medio
   relaje** … Decidir la relajación **excede el orden cuadrático**» — el
   problema quedó DECIDIDO y no excedía el orden cuadrático: lo decidió una
   ley de conservación exacta ya presente en el orden cuadrático + CI FRW.
5. Tabla de estado: «Nuevo: selección de estado … ABIERTO» → CERRADO (D2).

## Frases del paper v0.6 que quedan tocadas (para la integración — NO editadas acá)

1. **Título**: «…and a screened frame-dragging signature» — la firma queda
   suprimida por superselección; retitular o recalificar (p.ej. "and the
   superselection of its gravitomagnetic state").
2. Tabla de contribuciones: «Screened Lense–Thirring as **the falsifiable
   signature**; … LARES-2 … gives Λ < 1.12 MeV on the relaxed branch» —
   recalificar: la fase PREDICE RG en gravitomagnetismo (hasta ~1e−43); la
   cota Λ < 1.12 MeV es de la rama no poblada.
3. §1: «Which branch nature picks is a genuine **open problem** of the phase
   (**it exceeds quadratic order**), and we state it as such» — reemplazar por
   el teorema del congelamiento (no excedía el orden cuadrático).
4. §8: «Co-rotating branch (medium recently stirred, **no dissipation**)…
   **any dissipation relaxes it** toward the screened branch — but a
   superfluid medium **could in principle** sustain it» — "any dissipation"
   REFUTADA; "could in principle" → lo hace, por superselección; y el estado
   ya no es "GR in disguise" exacto: gana δ_ret = −ĉ(Λ/M̄_Pl)² ≤ 1.7e−43.
5. §8: «**The caveat, stated as a result.** Which branch describes the Earth
   is **not decidable at quadratic order**…» — reescribir entera: es
   decidable y está decidida (congelamiento + IVP + CI FRW ⟹ co-rotante).
6. §8: «any sharpening of the error-budget dispute or of the state-selection
   problem now **converts directly into MeV-scale physics**» — ya no para la
   nodal: la medición LARES-2 pasa a ser consistencia (predicción RG), no cota.
7. §8 Numbers: «gives **Λ ≲ 2.0–2.6 MeV** on the relaxed branch … pushes the
   relaxed-branch bound to **Λ < 1.12 MeV**» y «the predicted nodal deviation
   is 0.13%» — condicionalizar a la rama no poblada (contrafáctico útil).
8. §9: «the **frame-dragging signature** of §8 … rides on a tensor sector…» —
   "signature" → "gravitomagnetic structure" (la firma está suprimida).
9. §10 Declared limits: «**The frame-dragging signature is conditional** on
   the medium relaxing … Deciding the branch **exceeds this paper's order of
   computation** — stated as the open problem it is» — reemplazar por las
   hipótesis del teorema (acople universal, suavidad de Φ, base NLO).
10. §11 Open problems: item 1 (state selection: «This is now *the* question
    of the phase») — RESUELTO, sale; item 5 (NLO frame dragging co-rotante:
    «the first observable … **if any exists**») — RESPONDIDO: existe,
    δ = −ĉ(Λ/M̄_Pl)², inobservable por ~40 órdenes.

## Scripts propios (todos corren; cada chequeo imprime su residuo)

| Script | Qué ataca | Tiempo |
|---|---|---|
| `va1_teorema.py` | teorema (dets de Gram, Jacobi), Noether completo, inversión, FRW | 50 s |
| `va2_juguete_campo.py` | juguete desde ΓΓ propio; vínculo; corriente local 1b; nube compensante; energía; IVP general | 4 s |
| `va3_extensiones.py` | fuente móvil (2 cuadraturas); dos modos NLO; carácter de vínculo | 7 s |
| `va4_numeros.py` | δ_ret con c_a genérico; transferencia/secularidad; fuga; spin-down | 2 s |
| `cotejo_columnas_out.txt` / `cotejo_a2_out.txt` | corridas de t1–t4, a1, a3, a4 (y a2) cotejadas contra sus actas | — |

*Acta escrita el mismo día del cierre de los ataques. El teorema no es mío y
me habría gustado romperlo: no pude. Donde el pipeline me corrigió a mí, quedó
escrito. D2 entra al paper cuando Nico dé el OK, con las frases de arriba
corregidas y las hipótesis a la vista.*
