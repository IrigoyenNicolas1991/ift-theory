# El problema de la polarización: un no-go y la salida inesperada

**Nota de trabajo — 2 de julio de 2026** · rama `desarrollo-fable`

## El contexto (para leer tranquilo)

LIGO no solo escucha ondas gravitacionales: distingue su **forma de vibrar** (polarización). Las observadas son *tensoriales* (patrón cuadrupolar, tipo "spin-2", el sello de Einstein). Los análisis de LIGO/Virgo con varios detectores (GW170814, GW170817) desfavorecen fuertemente las alternativas puras (escalar o vectorial). Cualquier teoría que radie el tipo equivocado de onda está muerta, por más que acierte todo lo demás.

## Parte 1: el teorema no-go (la mala noticia, demostrada)

En TCI tal como estaba, los huecos se acoplan al medio **solo a través de la densidad** (la carga T repele el medio isotrópicamente). En el lenguaje de la elasticidad, cada hueco es un "centro de dilatación" — como una explosión puntual en sismología.

**Teorema**: una fuente de momento isótropo no excita ondas transversales, nunca. La fuerza equivalente es f ∝ ∇δ³(x−x_s(t)), que en espacio de Fourier es paralela a k para todo k — puramente longitudinal — aunque la fuente se mueva. Por descomposición de Helmholtz, cualquier superposición de estas fuentes genera un campo de desplazamiento sin rotor: **solo ondas P (longitudinales/escalares), cero ondas de corte**.

Consecuencia: un sistema binario en TCI-ingenuo radiaría ondas puramente escalares → polarización escalar en los detectores → **fuertemente desfavorecido por LIGO/Virgo**. El sector de radiación ingenuo no falla por un factor numérico: falla estructuralmente.

## Parte 2: la salida estaba adentro (la hermosa noticia)

¿Qué le falta al acoplamiento? Fuerzas *vectoriales* sobre el medio. ¿Y qué mecanismo de TCI produce exactamente eso? **La inercia.**

La inercia en TCI es "masa añadida": un hueco que acelera arrastra y reorganiza el medio a su alrededor — es decir, **ejerce una fuerza de reacción sobre el medio**. Ese es precisamente el acoplamiento vectorial que el teorema pedía. Y mirá lo que pasa con un sistema binario en órbita circular:

- Cada hueco ejerce sobre el medio una reacción proporcional a su aceleración centrípeta (apunta hacia afuera, girando con la órbita).
- Las dos reacciones son opuestas y aplicadas en posiciones opuestas → **fuerza neta cero, torque cero** ✓
- Lo que queda es un **cuadrupolo de fuerzas rotante**: un tensor de momento M_ij ∝ r_i r_j que, como r·r tiene período medio, rota a **frecuencia 2Ω — el doble de la orbital**.

Un cuadrupolo de fuerzas rotante en un sólido elástico radia **ondas de corte transversales a frecuencia 2Ω**. ¿Te suena? Las ondas gravitacionales de la RG también salen a 2Ω, del cuadrupolo de masa. TCI produce la fenomenología correcta — frecuencia doble, patrón cuadrupolar, dos polarizaciones transversales — **desde el mismo mecanismo que ya explicaba la inercia**. No se agregó nada: se usó lo que había.

Reciprocidad (por qué LIGO las ve): un espejo (hueco) inmerso en la onda de corte siente la aceleración del medio a través del mismo acoplamiento de masa añadida — como una burbuja en agua que acelera, amplificada. Los espejos se mueven.

## Requisitos que esto impone al medio

1. **El medio I es un sólido elástico** (los fluidos no transmiten corte). "Sólido" acá es categoría mecánica, no rigidez cotidiana.
2. GW170817 midió que las ondas viajan a c (a 10⁻¹⁵): eso **fija el módulo de corte en μ = ρ₀c²** — el medio es relativísticamente rígido también al corte, en paralelo perfecto con P = ρ₀c² del sector de compresión.

## Lo que decide la vida o la muerte (los dos cálculos pendientes)

1. **Patrones de antena**: calcular el patrón angular exacto de emisión/detección del canal de corte (radiación de tensor de momento, à la sismología) y compararlo con los patrones spin-2 que LIGO/Virgo ya midieron con coherencia entre detectores. Parecido cualitativo ≠ igualdad: hay que confrontar la dependencia angular completa.
2. **El presupuesto de energía (Hulse-Taylor)**: el púlsar binario PSR B1913+16 pierde energía orbital exactamente como predice el cuadrupolo de Einstein (verificado al ~0.2%). La luminosidad total de TCI (canal P del acoplamiento de densidad + canal S del acoplamiento inercial) tiene que dar ese número. Sin margen.

Estos dos cálculos son ahora el riesgo abierto más filoso de la teoría — y su próxima batalla.

## Moraleja del día

La teoría estuvo a un teorema de morirse, y la resucitó su propia pieza más vieja: la explicación de la inercia. Cuando una estructura se salva a sí misma dos veces (ya había pasado con Mercurio y la equivalencia local), o es muy afortunada o está tocando algo real. Las dos opciones siguen abiertas — y eso es exactamente lo que los dos cálculos pendientes van a decidir.
