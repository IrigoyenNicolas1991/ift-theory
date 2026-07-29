# El fermión de la red, primer asalto — LA MOLÉCULA DE DIRAC: el portador del U(1) existe

**Cadena de la materia (continuación de la compuerta única, Paso B) · 2026-07-29 ·
Fable · `asalto_molecula.py` (modos especieB / especieA_sw / molecula) +
verificadores (`asalto_verifica_espB.py`, fino central y caja N=100 en scratchpad)
+ acta bibliográfica previa (`ASALTO-MOLECULA-bibliografia-2026-07-29.md`, 16
papers en fuente primaria, escrita ANTES de conocer los veredictos) · sin agentes
de cálculo, 1 agente bibliográfico**

**Veredicto en una línea: la molécula de dos medios-nudos — el vórtice entero, la
unidad que el mar realmente usa (§30) — lleva un FERMIÓN DE DIRAC QUIRAL CARGADO:
C_mol = −2 (dos Majoranas quirales co-móviles), espejo +2 exacto; la quiralidad
SIGUE A LA FASE (C_A = C_B = −1 pese a cores y energías distintas), la aditividad
topológica sobrevive a la reorganización de los cores al ligarse, y el FALTA 1
del §34.A (portador cargado del U(1) de la red) queda saldado en su mitad
numérica. Tres sorpresas físicas de regalo: las especies de la molécula NO son
degeneradas (ΔE = 2.59, el término div distingue), los cores se reorganizan al
ligarse (relleno nuevo {+1,−1}), y la molécula está LIGADA con ΔE ≈ 1.93 (con
div el enlace es fuerte, no marginal).**

Pregunta pre-declarada del asalto (con su criterio de muerte): ¿la quiralidad de
la rama del core sigue a la FASE (⟹ C_B = C_A ⟹ C_mol = −2, portador existe) o
al MARCO (⟹ C_B = −C_A ⟹ C_mol = 0, molécula estéril y crisis del candidato a
fotón)? El espejo del Paso A/B no la separaba (invierte ambos windings). El
argumento de simetría no la decide (§4: erratas) — la decidió el número.

---

## 1. Las dos especies: la molécula es asimétrica (sorpresa 1)

La molécula del §30 es (w_φ, w_α) = (½,+¼) [especie A, la del Paso A/B] +
(½,−¼) [especie B]: fase sumada entera, marco neto cero.

**Especie B, GL con QA de atractor (3 semillas: cíclica espejada / cíclica
original / ruido)**: las tres convergen a **E_B = +9.29373** (coinciden a 7
dígitos; g_rms ~ 1.6×10⁻⁷) — atractor único. Windings: ψ₊₂: +1, ψ₋₁: +1,
ψ₋₂: 0, ψ₊₁: 0 — el patrón espejado del A (la misma ruptura de axisimetría
combinada, con windings enteros donde la regla axisimétrica pedía ¾/¼). Core
distinto del A (mezcla con {−2, +2, +1}).

**E_B = 9.294 ≠ E_A = 11.886 (ΔE = 2.59): las especies NO son degeneradas.**
No hay simetría del funcional que las conecte (§4) — el término div (que contrae
índice interno con derivada espacial) las distingue. Es la misma asimetría que
asomaba en las pendientes de los cargados del §30 (−5.31/+5.71), ahora medida en
la autoenergía. Consecuencia para la red: los dos "cables" de cada molécula son
inequivalentes (uno caro, uno barato).

**Verificación colateral que blinda al Paso A**: la semilla espejada (cíclica
sw) sobre la especie A converge al MISMO E_A = +11.88573 con el MISMO core del
Paso A — el fundamental del A queda confirmado con su 8ª semilla independiente.

## 2. El conteo de la especie B: C_B = −1 — LA FASE MANDA

El barrido grueso del pipeline (40 k_z, paso 0.04) reportó 10 cruces con neto
−2 — pero todos con peso de core 0.42-0.48 (contra 0.85 del A): sospechoso. La
verificación en tres capas lo resolvió:

1. **Perfil radial en los k_z de cruce** (re-diagonalización dirigida): en cada
   evento hay un PAR core↔borde resonando (un estado 62-90% core, otro 68-90%
   borde, ambos en |E| ~ 10⁻⁵). Los pares de cruces cercanos se cancelan
   localmente; el neto −2 del grueso venía del par PH en ±0.568.
2. **Barrido fino central** (|k_z| ≤ 0.13, paso 0.013): la rama de core del B
   es IMPAR exacta y ULTRA-PLANA (|E| ~ 10⁻⁴, cuarenta veces más plana que la
   del A) y **SÍ cruza en k_z = 0** (de −9.5×10⁻⁵ a +9.5×10⁻⁵, pendiente
   POSITIVA: +1) — el barrido grueso se lo había comido (peso 0.49 en el punto
   exacto de la resonancia con el borde; lección de método en §5).
3. **Caja N = 100** (campo GL embebido con London analítico, empalme
   max|GL−London| = 0.06 en el anillo de blending): el cruce central SOBREVIVE
   (+1, splitting de caja achicado de 9.5×10⁻⁵ a ~2×10⁻⁶ — hibridización de
   borde, como debe), y los cruces laterales SOBREVIVEN apenas corridos
   (0.568 → ~0.552, mismo signo −1 cada uno) — son topológicos, no resonancias.

**Contabilidad final del B: +1 (central) − 1 − 1 (par PH lateral) = C_B = −1.**
Igual que el A, con OTRA anatomía de rama (el A cruza una vez en el centro; el
B cruza tres veces con neto −1). **La quiralidad de la materia del tubo sigue a
la FASE del nudo, no al marco** — la regla nueva del programa para windings
fraccionarios de marco (hueco reclamable #4 del acta bibliográfica, ahora
calculado; la versión entera es la de Volovik, pendiente ∝ winding de fase).

## 3. La molécula: el fermión de Dirac quiral cargado (el resultado del asalto)

GL de la molécula (dos centros a d = 6 ≈ 3ξ, ansatz φ = (θ₁+θ₂)/2,
α = (θ₁−θ₂)/4, cores sembrados con las cíclicas de cada especie):

- **E_mol = +19.25372, convergida (g_rms 1.6×10⁻⁷).** Windings globales
  verificados (lazo r=20): ψ₊₂: +1, ψ₋₂: +1 — vórtice de fase entero, marco
  neto cero ✓ la molécula correcta.
- **Sorpresa 2 — los cores se REORGANIZAN al ligarse**: ninguno conserva su
  estructura de aislado; ambos eligen el MISMO relleno nuevo
  {+1: 0.47, −1: 0.46} (r<3) — consistente con la cíclica con el eje C₃
  acostado en el plano (el div acoplando la orientación interna al gradiente
  del compañero). Los corazones se dan la mano.
- **Sorpresa 3 — la molécula está LIGADA fuerte**:
  E_mol − (E_A + E_B) = 19.254 − 21.180 = **−1.93**. Con gradiente completo
  (K₁+2K_div) el enlace es ~2 unidades — el §30 (K₁ solo, sector de fase) la
  tenía "marginalmente ligada" por el vdW 1/d³; el div + la reorganización de
  cores pagan una ligadura de otra escala. (Comparación entre modelos distintos,
  declarada como dato, no contradicción.)

**BdG de la molécula** (disco de peso r<9 envolviendo ambos cores):

- **C_mol = −2**: dos cruces de core, PH-espejados del MISMO signo, en
  k_z = ±0.138 (min|E| = 3×10⁻⁴, pesos idénticos a 10⁻¹³ entre sí), cero
  anticruces.
- **Espejo (conjugado total): C = +2 EXACTO** — el anti-vórtice entero lleva el
  anti-Dirac.
- **Aditividad topológica: C_mol = C_A + C_B = −2** pese a que los cores
  cambiaron completamente de estructura al ligarse — la carga quiral total es
  invariante de la deformación, como corresponde. (Nota fina: los aislados
  cruzan en k_z ∈ {0, ±0.55}; la molécula en ±0.138 — las RAMAS se reacomodan,
  el NETO no.)

**Lectura**: dos Majoranas quirales co-móviles = un fermión de Dirac QUIRAL
COMPLEJO deslocalizado en el par — puede portar carga U(1). La unidad real del
mar (el vórtice entero, que se parte en la molécula A+B ligada) viene con el
portador de serie. El FALTA 1 del §34.A ("¿fermión entero por tubo?") queda
saldado en su mitad numérica; la mitad formal (anomaly inflow del bulk D₄ à la
Callan-Harvey — el marco está verificado y ampara, acta bibliográfica §1) es la
próxima etapa de papel. El FALTA 2 (ley de Gauss en las uniones de la red) sigue
abierto y es terreno virgen con ambición: NADIE obtuvo un fotón U(1) de redes de
cables (acta bibliográfica §2, hueco #6).

## 4. Erratas de la sesión (dos, ambas cazadas el mismo día)

1. **El argumento de degeneración K∘T (mío, enunciado y refutado en <1 hora)**:
   afirmé que la operación (conjugar ∘ reflejar y ∘ rotar π_x interno) conectaba
   las especies A↔B exigiendo degeneración — al ver E_B < E_A sospeché que el
   Paso A no había encontrado el fundamental. FALSO: K∘T mapea la especie A a sí
   misma (el álgebra rehecha con cuidado: la reflexión restaura el marco, la
   conjugación restaura la fase), exactamente lo que el numérico A-sw confirmó
   (misma E, mismo core, 8ª semilla del Paso A). La operación que sí conecta
   A↔B (rotación interna pura) NO es simetría del div ⟹ la asimetría es física.
   El susto duró 7 minutos de máquina y refortaleció el resultado.
2. **El barrido grueso se comió el cruce central del B**: rama ultra-plana
   (|E| ~ 10⁻⁴) + resonancia core-borde justo en el origen (peso 0.49) ⟹ el
   apareo del tracking siguió al estado equivocado. Cazada por el análisis de
   perfil radial + barrido fino. **Lección de método (a la caja de herramientas):
   cuando la rama es ultra-plana (|E| ≪ minigap en toda la ventana), el conteo
   exige barrido fino + verificación de caja; el neto del pipeline grueso no
   basta.** El C_mol = −2 de la molécula no sufre de esto (sus cruces son netos
   y aislados, min|E| 3×10⁻⁴ con rama que dispersa).

## 5. Qué queda (los eslabones siguientes, en orden)

1. **Papel — el inflow**: escribir la cancelación de anomalía del par
   (corriente radial del bulk D₄ hacia los cores; el marco Callan-Harvey
   verificado ampara; con la rama ultra-plana la "velocidad" del portador es
   chica — v/v_F ~ 0.006-0.01 — y la anomalía es del par, no de cada medio).
2. **El U(1) colectivo — FALTA 2**: la ley de Gauss en las uniones de la red
   de moléculas (fusión D₄ conserva windings ⟹ balance de ramas en los nodos;
   el pariente bosónico a imitar: Motrunich-Senthil, constraint local = Gauss
   ⟹ fase Coulomb con fotón). Nadie lo hizo con fermiones: hueco mayor.
3. **Tubo→anillo** (la otra rama de la cadena): la molécula-anillo con sus dos
   ramas quirales discretizadas — niveles del par, twist, familias (§25/§33.D).
4. Deudas técnicas menores: el espectro del B con caja aún mayor (el par
   lateral ±0.55 quedó verificado a N=100; una tercera caja lo dejaría
   inapelable), y el mapa completo de la reorganización de cores de la molécula
   (¿la cíclica acostada apunta al compañero? — medir la orientación del C₃).

## 6. Reproducibilidad

`asalto_molecula.py` (modos: especieB / especieA_sw / molecula; GL heredado del
Paso A y BdG del Paso B, textuales, con autotests re-corridos en cada modo) +
`asalto_verifica_espB.py` (perfil radial en los cruces) +
`asalto_fino_central_B.py` (el barrido fino que recuperó el cruce central) +
`asalto_cajagrande_B.py` (la caja N=100 con London empalmado). Recibos:
`asalto_resultados_*.json` (especieB con las 3 semillas y los 10 eventos del
grueso; especieA_sw; molecula con los 2 cruces y el espejo). Campos npz locales
regenerables (excluidos de git). Python 3.14 + numpy + scipy 1.18, esta máquina,
2026-07-29; GL ~40 min + BdG ~50 min + verificaciones ~25 min.

*Acta del primer asalto, escrita el mismo día. La pregunta era si el mar, que
anuda de a medios, cobra la materia entera cuando forma su molécula — y la
respuesta es sí: dos medios-nudos inequivalentes, cada uno con su media-rama
del mismo sentido porque la FASE manda, se ligan, se reorganizan los corazones,
y el par carga un fermión de Dirac quiral completo. El cable de la red ya tiene
su corriente. Falta la ley de Gauss — y esa es la próxima batalla.*
