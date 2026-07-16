# Nota 11 — Scoping: el lagrangiano del condensado cuadrupolar (un cálculo, tres frutos)

**Fecha:** 2026-07-16
**Pregunta:** ¿cómo se construye, concretamente, TCI 2.0? La nota 10 dejó el cálculo
definido ("lagrangiano del condensado cuadrupolar en lenguaje Ballesteros-Comelli-Pilo →
identificar fase de Dubovsky → imponer m₂ = 0"). Esta nota lo desarma en pasos con
checkpoints y criterios de muerte, como hicimos con el perihelio (nota 2).
**Estado:** scoping — acá no se deriva nada; se declara el plan, las apuestas y lo que
puede matarlas.

---

## 1. Por qué este cálculo y no otro: un tronco, tres frutos

Los tres frentes vivos de TCI 2.0 cuelgan del mismo objeto matemático — el **espacio de
orden** del condensado (qué configuraciones puede tener el "peinado" del mar y qué cuesta
deformarlas):

1. **Gravedad (fase m₂ = 0):** del espectro de fluctuaciones del orden salen las
   helicidades y sus masas → hay que aterrizar en la fase de Dubovsky con ±2 sin masa a
   velocidad c y el resto silenciado (nota 10).
2. **Materia (taxonomía de defectos):** del mismo espacio de orden salen los defectos
   topológicos posibles (grupos de homotopía del vacío). Conjetura a explorar: las
   partículas son esos defectos — "nudos del peinado". Pagaría de una:
   cuantización de la carga (números de vuelta son enteros), identidad exacta de las
   partículas de una especie (misma clase topológica = mismo objeto), antipartícula =
   nudo espejo, aniquilación = par nudo/antinudo desanudándose (la imagen del cap. 11
   del libro, ahora con mecanismo), estabilidad topológica en vez de dinámica.
3. **Radiación (Hulse-Taylor):** con el lagrangiano en mano se rehace el pipeline de
   antenas (notas 6-7) para el campo Q_ij: binaria de defectos → luminosidad radiada →
   contra el decaimiento orbital de PSR B1913+16, medido al 0.16% (Weisberg & Huang,
   arXiv:1606.02744). **Este es el examen final: o da el número o no da.**

## 2. La apuesta física central (conjetura declarada)

**La simetría que protege m₂ = 0 es rotacional, no traslacional.** En criollo: "gotas,
no flechas" llevado hasta el final.

- La lección de solid inflation (Endlich-Nicolis-Wang, arXiv:1210.0569) es que un medio
  que rompe **traslaciones** con rigidez de corte (un sólido) genera m₂ ≠ 0
  inevitablemente. Eso mató a TCI 1.0 por el lado de radiación.
- La apuesta: un condensado cuya rigidez es **orientacional** (rompe rotaciones — o un
  combo interno×espacial de rotaciones — pero NO traslaciones: fluido en desplazamientos,
  rígido en orientación). Los modos ±2 serían **Goldstones de rotaciones rotas**: masa
  cero por teorema, no por ajuste.
- Si la apuesta cierra, la fase m₂ = 0 deja de ser una elección de parámetros y pasa a
  ser la fase natural de esta clase de medio. Si no cierra, se publica que no cierra.

## 3. Las piedras en el zapato, declaradas ANTES de empezar

1. **Los modos J=2 de laboratorio son masivos.** En ³He-B (nota 9) los modos spin-2
   observados son modos de *amplitud* del parámetro de orden, no Goldstones — por eso
   tienen gap. TCI 2.0 necesita un patrón de ruptura donde las helicidades ±2 sean los
   Goldstones *mismos*. No hay precedente directo; es exactamente el territorio virgen
   de la nota 10 §5, y también exactamente donde puede fallar.
2. **Inverse Higgs / Goldstones de simetrías espacio-temporales.** Cuando lo roto son
   simetrías del espacio-tiempo (rotaciones, boosts), el conteo de Goldstones no es el
   de Wigner: hay constraints (inverse Higgs) que pueden comerse los modos que
   necesitamos o cambiarles la dispersión. Hay que hacer el conteo con la maquinaria
   correcta (coset construction; la "zoología" de Nicolis-Penco-Piazza-Rattazzi,
   arXiv:1501.03845, es el mapa donde ubicar nuestro medio).
3. **Isotropía del universo.** Un orden cuadrupolar que elija una dirección fija del
   espacio está muerto de entrada (CMB isótropo a 10⁻⁵). El precedente de escape es
   ³He-B: el parámetro de orden rompe rotaciones de spin y orbitales por separado pero
   preserva la rotación combinada — orden sin dirección observable. Nuestro patrón debe
   tener esa propiedad o equivalente.
4. **El acople de corte residual.** Aunque el medio sea fluido en desplazamientos, el
   sector Q_ij podría inducir rigidez de corte efectiva a algún orden (y resucitar el
   problema de solid inflation por la ventana). Hay que chequearlo explícitamente.
5. **Las de siempre (notas 9-10, siguen abiertas):** Weinberg-Witten (grietas: Lorentz
   emergente, gravitón-Goldstone), dinámica de Einstein completa más allá del sector TT
   (dato fresco arXiv:2512.08435), monometricidad (Carlip) — donde TCI apuesta su
   ventaja estructural: materia = defectos del mismo medio → una sola velocidad límite
   de fábrica. Nótese que la conjetura de defectos (fruto 2) es la que *realiza* esa
   ventaja: si las partículas son nudos del mismo campo cuyas ondas son la luz y la
   gravedad, la monometricidad no se impone — se hereda.

## 4. Lecciones del triaje micro (feb 2026) que esta vez NO se repiten

- **No fijar escalas temprano.** El "electrón de 3 mm" y la "red de 0.17 mm que no
  transmite luz" nacieron de fijar ℓ_I con h antes de tener la dinámica. Acá las escalas
  quedan libres hasta que un cálculo las exija.
- **Nada de numerología.** α no se toca. Si algún número sale, sale de un lagrangiano
  con simetrías declaradas o no sale.
- **Bell queda donde está.** Un medio clásico local 3D no reproduce entrelazamiento
  (teorema, no opinión). El programa no es "cuántica desde mecánica clásica": es
  relocalizar la rareza — las propiedades cuánticas de las cuasipartículas y defectos
  vivirían en la naturaleza cuántica del condensado, como en el helio real. Qué es la
  función de onda en este cuadro: problema abierto, declarado.
- **Se rescata solo lo que sobrevivió al triaje:** EM = ondas transversales (spin-1,
  MacCullagh 1839) y carga = quiralidad. Ambas encajan naturalmente en el cuadro de
  defectos (quiralidad del nudo = signo de la carga).

## 5. El plan por pasos (cada uno con salida publicable, buena o mala)

**Paso A — Ubicar el medio en el mapa.** Elegir el patrón de ruptura: qué grupo G tiene
el condensado y a qué subgrupo H rompe (candidatos: tipo ³He-B con rotación combinada
preservada; fase m₁=0 de Dubovsky con su invariancia xⁱ→xⁱ+ξⁱ(t); revisar dónde cae en
la zoología NPPR). Checkpoint: el patrón debe (i) no romper traslaciones, (ii) no dejar
dirección observable, (iii) tener espacio de orden G/H no trivial.
*Muerte en A:* no existe patrón que cumpla (i)-(iii) con componentes J=2.

**Paso B — El lagrangiano.** Escribir la teoría efectiva de fluctuaciones alrededor del
condensado (coset construction o expansión directa de Q_ij), en el lenguaje de
Ballesteros-Comelli-Pilo para poder leerla como gravedad masiva LV.
Checkpoint: reproducir como caso límite algún medio conocido de BCP (control de calidad,
como los controles RG de los scripts).

**Paso C — El espectro.** Diagonalizar por helicidades → leer m₀…m₄ de Rubakov →
identificar la fase de Dubovsky. Checkpoint decisivo: **¿m₂ = 0 sale protegido por la
simetría del paso A o hay que ajustarlo a mano?** Protegido = victoria grande y
publicable; ajustado = se declara y se evalúa si el ajuste es estable; imposible
(m₂ ≠ 0 forzado) = TCI 2.0 falsada en su forma actual, se publica el mismo día.

**Paso D — Los nudos.** Homotopía del espacio de orden G/H del paso A (π₀, π₁, π₂, π₃)
→ tabla de defectos posibles con sus cargas topológicas y quiralidades. Confrontar la
taxonomía contra la estructura gruesa de la tabla de partículas (¿hay cargas enteras?
¿pares partícula/antipartícula? ¿familias?). Sin promesas: si la tabla no se parece en
nada, se publica que no se parece.

**Paso E — Las antenas y Hulse-Taylor.** Pipeline de las notas 6-7 con el campo nuevo:
patrones de antena de los modos ±2 (¿spin-2 genuino esta vez?) y luminosidad de una
binaria de defectos vs la fórmula del cuadrupolo. Contraste: GWTC-3 (polarizaciones) y
PSR B1913+16 (0.16%).
*Este paso hereda además una intuición de las simulaciones del libro (2026-07-16): en el
mar disipativo de juguete las órbitas decaen por fricción de onda — brutalmente
exagerado, pero es cualitativamente el fenómeno de Hulse-Taylor. La pregunta afilada:
¿qué propiedad del medio fija la tasa de decaimiento? En RG la fija G/c⁵; acá deben
fijarla los módulos del condensado. Si el número sale de la física del medio, se acabó
la discusión.*

## 6. Marcador honesto de largada

**Qué hay hoy:** un plan con checkpoints, una conjetura declarada (protección rotacional
de m₂=0), literatura de soporte verificada (notas 9-10) y un territorio virgen
confirmado por búsqueda.
**Qué NO hay:** ningún lagrangiano, ningún espectro, ninguna tabla de defectos, ningún
número contra Hulse-Taylor. Todo lo de arriba puede morir en el paso A.
**Regla de la casa:** cada paso publica su resultado el mismo día, victoria o derrota.
