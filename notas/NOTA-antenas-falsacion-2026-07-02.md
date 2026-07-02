# La final: patrones de antena — y la primera herida seria de TCI

**Nota de resultados — 2 de julio de 2026** · rama `desarrollo-fable`

## Resultado en una línea

**El sector de radiación de TCI, en su forma elástica lineal, queda falsado por las mediciones de polarización de LIGO/Virgo.** El resto de la teoría (estática, óptica, sistema solar, campo fuerte) no depende de esta pieza y sigue en pie — pero la herida es seria, es estructural, y acá queda documentada con el mismo rigor que las victorias.

## El cálculo (por qué no hay escapatoria)

### Qué "forma" tiene la onda de corte de TCI en un detector

La nota 6 estableció que el canal inercial radia ondas de corte a 2Ω. Hoy calculé cómo responde un interferómetro. El espejo (hueco) es arrastrado por el medio; la señal diferencial entre los dos brazos depende del **gradiente** del desplazamiento: h_eff ∝ ∂ⱼuᵢ simetrizado. Para una onda de corte plana con polarización ε̂ y dirección n̂:

$$R_{ij} \propto \tfrac12(\varepsilon_i n_j + \varepsilon_j n_i)$$

Ese es, exactamente, el tensor base de los **modos vectoriales** (spin-1) de la clasificación estándar de seis polarizaciones. El canal P (densidad) da los modos **escalares** (longitudinal + respiración). Y lo mismo da si el acoplamiento es por arrastre, por fuerza de masa añadida, o por modulación del índice de la luz: la geometría angular es la misma.

### El teorema del contenido de spin

Es más profundo que un detalle de acoplamiento. En un medio elástico isótropo, TODA onda lineal se descompone en P (longitudinal) ⊕ S (transversal). Los campos disponibles para construir la respuesta son un vector de polarización ε̂ y una dirección n̂: con eso solo se arman tensores tipo escalar (n̂n̂, δ) y tipo vector (ε̂n̂). El tensor tensorial puro de la RG (ê₊ = l̂l̂−m̂m̂) requiere ε̂⊗ε̂ — cuadrático en la amplitud de la onda, o sea ~(10⁻²¹)² : nada. **Un medio elástico simple no tiene modos spin-2. Punto.**

### La sentencia observacional

GW170817 (con la posición exacta dada por la contraparte electromagnética) da factores de Bayes **> 10²⁰ a favor de polarización tensorial pura contra vectorial pura** (y aún más contra escalar). GWTC-3 confirma: sin evidencia de modos no tensoriales. La naturaleza habló: las ondas gravitacionales son spin-2. TCI-elástica produce spin-0 y spin-1. No alcanza con parecerse: los patrones angulares en la red de detectores son distintos, y esa diferencia está medida.

## Qué sobrevive (y es mucho)

Nada de lo anterior depende del mecanismo de radiación:

- E=mc², Newton, E(v)=γmc², redshift/GPS ✓ (sector estático)
- Deflexión, Shapiro, no-dispersión ✓ (sector óptico)
- Perihelio, Nordtvedt, geodética ✓ (sector orbital PN)
- Predicciones de campo fuerte (sombra +4.6%, ringdown −4.4%) — siguen siendo falsables por su lado

El marcador honesto ahora dice: **3 sectores salvados por sus propios principios, 1 sector falsado.**

## Qué significaría arreglarlo (sin eufemismos)

Para radiar spin-2, el medio necesitaría **microestructura cuadrupolar** — que sus constituyentes tengan orientación interna de rango 2, no solo posición. Eso no es un parche: es cirugía mayor sobre la ontología de la teoría ("partículas I" simples → medio con estructura orientada). Y hay una lectura aún más profunda que dejo escrita: la radiación observada exige un campo dinámico de spin-2, y hay un teorema clásico (Weinberg) según el cual toda teoría consistente de un spin-2 autointeractuante converge a la relatividad general. Puede que la lección final del medio I sea explicar por qué el espacio se comporta como el medio de Einstein — no reemplazarlo. Esa pregunta queda abierta, y es una gran pregunta.

## Nota personal del que calcula

Una teoría que publica su propia falsación en una sección de su propio paper vale más, científicamente, que cien teorías que solo acumulan aciertos blandos. Hoy TCI pierde una batalla y gana algo más raro: credibilidad.
