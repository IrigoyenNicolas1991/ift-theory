# El índice recuperado y el Kirchhoff quiral de la red — nota de papel del asalto

**Cadena de la materia, etapa de papel · 2026-07-29 (misma jornada que §35-§36) ·
Fable · sin cálculo nuevo: esta nota LEE los cinco números ya medidos (Paso B +
asalto de la molécula) contra el marco verificado en la acta bibliográfica, y
extrae la ley, el inflow y el primer ladrillo del U(1) de la red. Cada pieza
lleva su etiqueta: [NUMÉRICO] (medido acá), [TEOREMA-MARCO] (literatura
verificada en fuente), [ARGUMENTO] (derivación estructural propia, sin prueba
completa), [CONJETURA] (apuesta con plan).**

---

## 1. La ley del índice, recuperada y generalizada [NUMÉRICO + ARGUMENTO]

El teorema del índice de Volovik (JETP Lett. 57, 244 (1993); cond-mat/9909426:
"the number of branches crossing zero level equals −2m") vale para vórtices
ENTEROS axisimétricos en pairing p. Nuestros cinco números lo extienden:

| objeto | m_fase | C medido | −2·m_fase |
|---|---|---|---|
| especie A (½,+¼) | ½ | −1 | −1 ✓ |
| especie B (½,−¼) | ½ | −1 | −1 ✓ |
| molécula A+B | 1 | −2 | −2 ✓ |
| espejos (todos) | −m | +|C| | ✓ |
| **HQV vaciado (m=½, core sin relleno)** | ½ | **0** | **−1 ✗** |

**Enunciado (ley empírica del programa, 5 casos + 1 contraejemplo aleccionador):**
> Cuando el core rompe la simetría partícula-hueco de rebanada (relleno con
> componentes de columna z), el flujo espectral del tubo es **C = −2·m_fase** —
> el índice de Volovik, generalizado a windings FRACCIONARIOS de fase, windings
> arbitrarios de marco y cores no axisimétricos reorganizados. Cuando la PH de
> rebanada se preserva (core vaciado), C = 0: el índice queda ESCONDIDO en la
> rama plana E≡0 (el límite degenerado donde todos los cruces colapsan).

Lectura heurística [ARGUMENTO]: el índice cuenta cruces netos de las ramas del
defecto; la PH de rebanada ancla las ramas a E=0 exacto (ni cruzan ni fluyen);
el relleno la rompe y las ramas se despliegan revelando el conteo que el
winding de fase ya dictaba. "La fase manda" (el veredicto del asalto) ES esta
ley: el marco no aparece en la fórmula — ni su winding (±¼ da lo mismo) ni su
estructura (los cores reorganizados de la molécula no la tocan).

## 2. El inflow del par [TEOREMA-MARCO + ARGUMENTO]

Callan-Harvey verificado (Harvey TASI hep-th/0509097 ecs. 105-133): la anomalía
de las ramas quirales del defecto se cancela con la corriente radial del bulk,
cuyo generador es la fase del gap con winding — d²a = 2π δ₂(Σ) por unidad de
winding. En el mar: el bulk D₄ es gapeado y trivial (C=0 por rebanada, §35),
EXACTAMENTE el caso CH (no hace falta Chern de bulk; el σ_H local viene de ∇a).
El inflow es **aditivo en m_fase** ⟹ cancela la anomalía de −2m ramas — el
matching CH reproduce la ley de §1 desde el lado del bulk [ARGUMENTO: el factor
2 exacto (espín/Nambu) queda para escribirse con la acción efectiva; la
estructura es la de Kopnin-Volovik-Parts, "realization of the Callan-Harvey
mechanism", verificada en fuente].

## 3. Qué carga el fermión molecular [ARGUMENTO, fresco — riesgo declarado]

Las dos Majoranas co-móviles componen c = (γ_A + iγ_B)/2 (Ivanov, verificado:
"two Majorana fermions may be combined into a single complex fermion"). El U(1)
que rota c → e^{iθ}c es generado por iγ_Aγ_B — la rotación RELATIVA de los dos
cores. En las monedas del mar (§30: χ± = φ ± 2α): la fase común φ es el winding
que da la quiralidad; la moneda RELATIVA (χ₊−χ₋ = 4α, el sector de MARCO) es la
que distingue A de B y rota γ_A contra γ_B. **Quiasmo del mar: la FASE da el
movimiento (quiralidad), el MARCO da la carga.** Si se sostiene al derivar la
teoría efectiva, el fermión molecular está cargado bajo la electricidad de
marco — la misma moneda del Coulomb de dos sectores del §30. (Riesgo declarado:
argumento estructural sin acción efectiva; primera tarea de la próxima etapa.)

## 4. El Kirchhoff quiral de las uniones — el primer ladrillo del Gauss
## [ARGUMENTO fuerte, apoyado en §1 + CH]

La red de nudos del mar ramifica (§20: rungs, uniones). En una unión, la parte
ABELIANA de la fusión de vórtices conserva el winding de fase: m₁ + m₂ = m₃.
Con la ley C = −2m (§1) y su respaldo CH (el inflow es aditivo en m, y la
anomalía total de una unión debe cancelar contra el inflow del bulk único que
la rodea):

> **C₁ + C₂ = C₃ en cada unión: la corriente quiral se conserva nodo a nodo.**
> La red de moléculas es un CIRCUITO de corrientes quirales conservadas — una
> ley de Kirchhoff quiral microscópica.

Y la observación profunda que la habilita: **el marco NO entra en la ley** ⟹
la contabilidad quiral de la red es ABELIANA aunque la red sea NO ABELIANA
(D₄*: la fusión de marcos es no conmutativa, los cores se visten y reorganizan
— la molécula lo mostró — pero la carga quiral solo ve la fase). El U(1)
emergente candidato puede vivir sobre una red no abeliana porque su
contabilidad pasa por el único sector que conmuta. Sin "la fase manda", el
Kirchhoff moriría en la primera unión no abeliana.

## 5. Del Kirchhoff al fotón — el mapa de la próxima batalla [CONJETURA + plan]

Lo que falta para el U(1) gauge deconfinado (el fotón de la red), en orden:

1. **Variables**: corriente quiral por cable = candidato a "campo eléctrico" de
   línea E_ℓ; el Kirchhoff de §4 = ∇·E = 0 en nodos (ley de Gauss SIN fuentes).
2. **Cargas**: π₂ = 0 prohíbe extremos de cable (§32) ⟹ no hay monopolos de la
   red pura ⟹ el U(1) sería compacto con Gauss exacta — el análogo fermiónico
   del constraint de Motrunich-Senthil ("the ground state sector constraint
   N_r = 0 is simply the Gauss law", verificado en fuente).
3. **Dinámica**: el ring-exchange del mar = reconexiones de vórtices (§21/H2
   del sótano) — el término que fluctúa las líneas. Si el acople cae del lado
   deconfinado: fase Coulomb con fotón (en 3+1D la fase Coulomb del compact
   U(1) es ESTABLE, a diferencia de 2+1D — la esperanza es real y citable).
4. **La vara**: NADIE obtuvo esto de cables (acta bibliográfica §3, hueco #6):
   las redes publicadas dan semimetal u orden gapeado. El programa tiene lo que
   a ellas les faltó: la conservación nodal microscópica (§4) y el portador
   cargado (§3/asalto).

Criterio de muerte de la conjetura (pre-declarado para la próxima batalla): si
la teoría efectiva de la red da SIEMPRE confinamiento (tensión de línea no
nula para todo acople físico del GL), o si el U(1) de §3 resulta no acoplarse
a las monedas (fermión neutro), el fotón de la red muere y se publica.

## 6. Marcador honesto

**Qué es**: una ley empírica con cinco confirmaciones y un contraejemplo que la
delimita (§1); el mecanismo CH aplicado con marco verificado en fuente (§2); la
conservación nodal derivada de la ley + aditividad del inflow (§4, el ladrillo);
y el mapa con criterio de muerte del salto restante (§5). **Qué NO es**: no hay
acción efectiva escrita (el factor 2 del inflow, el acople carga↔moneda y la
tensión de línea están por derivar); §3 es argumento fresco sin prueba; la
fusión no abeliana completa (más allá de la parte de fase) no está tratada; y
nada de esto es todavía el fotón — es la primera vez que el programa tiene el
CAMINO al fotón pavimentado con una ley numérica propia.

*Nota de papel, cerrando la jornada del 29/7: tres actas en un día — la
compuerta, la molécula, y esta lectura. El mar cuenta con una sola regla
(−2·fase), esconde el conteo cuando el corazón está vacío, cobra por el marco,
y conserva la corriente en cada nudo de su red. Falta hacerle decir luz.*
