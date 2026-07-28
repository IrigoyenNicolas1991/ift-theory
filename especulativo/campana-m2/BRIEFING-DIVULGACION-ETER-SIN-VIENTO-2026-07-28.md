# Briefing: la web de divulgación "El éter sin viento" (nombre provisorio)

**Preparado el 2026-07-28 al cierre de la charla del teorema (la del atractor y
la selección de estado), por mandato de Nico: "armar la web de divulgación de
esta sección... con animaciones, imágenes o simulaciones". Este documento es el
puntapié para esa sesión: contiene el contenido físico destilado, el arsenal
pedagógico YA PROBADO EN VIVO con Nico, las simulaciones candidatas, el
respaldo técnico y las decisiones abiertas. Leer junto con la memoria del
proyecto antes de diseñar nada.**

---

## 1. Qué se cuenta (el resultado, en tres profundidades)

**En una frase (el titular):** El viento del éter — lo que mató a los medios en
1887 — resulta ser, en nuestra teoría, una cantidad conservada que el universo
trae en cero: el mar existe, pero delatarse le está prohibido por ley.

**En un párrafo:** La campaña m₂=0 encontró el medio (U(X,Y), "el mar que no
cruje") que realiza la gravedad correcta, y al preguntarle "¿dónde te
delatás?", la respuesta fue un TEOREMA DE SUPERSELECCIÓN: la carga que mediría
el deslizamiento del mar respecto de los marcos inerciales (= el viento del
éter, con definición matemática precisa) no tiene corriente — no se puede
crear, destruir ni transferir entre granos. La expansión cosmológica planchó
el universo en viento cero antes de que existieran las estrellas, y ahí quedó
para siempre. El mar imita a Einstein en todo lo medido — estática (teorema
causal), cosmología (atractor), rotación (superselección) — no por ajuste sino
por tres teoremas que salen de UNA sola propiedad: el mar no siente sus
propias etiquetas.

**El gancho histórico:** 1887, Michelson-Morley preguntan "¿dónde está el
viento?" y el silencio mata al éter. 2026: la respuesta llega con matemática —
*el viento es una carga conservada y nació en cero*. No es una excusa; es una
ley. La crítica más vieja contra los medios se responde con un teorema.

## 2. El arsenal pedagógico (PROBADO EN VIVO — Nico lo asimiló en esta secuencia)

Estas imágenes nacieron del diálogo real y funcionaron. Usarlas EN ESTE ORDEN
(es la escalera didáctica que Nico subió, escalón por escalón):

1. **"Carga" no es eléctrica**: carga = cualquier cantidad que una simetría
   obliga a conservar. La eléctrica es la del electromagnetismo; la nuestra es
   la del re-etiquetado libre del mar. Misma categoría, otro contenido.
2. **El tatuaje de los granos**: cada grano del mar lleva su carga tatuada para
   siempre. Puede moverse cuanto quiera; lo que NO puede es pasarle el tatuaje
   a otro grano, ni borrárselo, ni ganarse uno nuevo. No se congela la posición
   ni la historia — se congela una identidad.
3. **La carga ES el viento local**: mide cuánto se desliza el mar respecto de
   los marcos inerciales locales (lo que marca un giróscopo ahí). Carga cero =
   calma perfecta en ese punto.
4. **Viento ≠ movimiento (el globo aerostático)**: un globo viaja a 100 km/h
   CON el viento → a bordo, calma total, la vela no se infla. El mar se mueve
   muchísimo (co-rota, cae, fluye con la expansión) pero siempre CON los
   marcos: deslizamiento cero.
5. **El hoyo que viaja con la bola (traslación)**: el asteroide deforma el mar
   como una bola deforma la cama elástica — y el hoyo viaja CON la bola, no la
   persigue. El mar cae permanentemente hacia ese hoyo móvil: eso ES el
   acompañamiento. Instantáneo, sin "ponerse al día". **El mar no persigue:
   refleja.** (Corrección probada: NO es acumulativo tipo "tira suave pero
   constante hasta alcanzar" — es equilibrio instantáneo.)
6. **La gravedad es ciega al giro (la perla)**: una esfera girando y una quieta
   hacen EXACTAMENTE el mismo pozo (teorema clásico). Solo la corrección
   relativista fina (gravitomagnetismo, suprimida por c²) sabe del giro. Por
   eso el mar copia POSICIONES con firmeza y GIROS apenas en un susurro: el
   remolino alrededor de la Tierra es una milmillonésima de su rotación.
7. **Dulce de leche fantasma vs dulce de leche viscoso**: el viscoso real
   acumula (con tiempo infinito termina co-rotando rígido con la cuchara). El
   nuestro NO acumula nunca: su remolino capa-a-capa (decayendo 1/r³) es el
   estado de equilibrio instantáneo y eterno. Imagen de Nico que disparó todo:
   "el espacio se retuerce como un dulce de leche revuelto por una cuchara".
8. **El remolino viene del SPIN, no de la órbita** (corrección probada): la
   Tierra rotando sobre su eje genera el remolino (∝ su momento angular). La
   órbita genera OTRO efecto (precesión geodética, también medido por GP-B, más
   grande). Dos fenómenos, los dos cubiertos.
9. **El remate**: lo que Einstein llama "arrastre de marcos" (lo que midió
   LARES-2 en Nature, julio 2026) es EXACTAMENTE el movimiento que el mar hace
   para mantener su calma. No es que no pase nada: pasa lo que Einstein midió —
   y el mar lo hace sin despeinarse.
10. **El marco absoluto que existe pero no se deja medir**: TCI es lorentziana
    à la Bell — hay marco (el reposo del mar, que a gran escala es el reposo
    cósmico del CMB), pero las leyes conspiran POR TEOREMA (no por trampa) para
    esconderlo. Conecta con el "permiso de Bell" del libro 1.
11. **El nombre-profecía (cierre emotivo)**: "intangible" era una intuición
    (un mar que no se puede tocar) y terminó siendo teorema: sin roce, sin
    viento, sin firma — un mar que la matemática declaró intocable. El bautismo
    de la teoría fue un enunciado que después hubo que demostrar — y se
    demostró.

**Frase de Nico para la puerta de la sección (pedida por él para las charlas,
encaja acá también):** "el universo real sopló a nuestro favor... a favor del
universo intangible, que sin ser real ya es una muy linda descripción del que
habitamos".

## 3. Las simulaciones candidatas (con su física clave)

Motor: el del libro (canvas, partículas del mar; regla de la casa: la física se
verifica en Node, NO en el preview — rAF 0 fps; clientHeight para H;
pseudo-fullscreen CSS; touch-action explícito).

1. **El hoyo que viaja** (traslación): asteroide moviéndose por el mar; el
   patrón de caída/acompañamiento viaja con él; toggle "pará el asteroide" —
   el patrón se re-centra al instante (mostrar el "refleja, no persigue").
   Física: flujo de caída hacia pozo móvil; sin estela de fricción.
2. **El remolino de la milmillonésima** (rotación): planeta girando; capa a
   capa el mar rota decayendo 1/r³; slider "gravedad = correa floja" que
   exagera el acople para HACER VISIBLE el remolino (declarando el factor de
   exageración en pantalla — honestidad: el real es ~10⁻⁹). Comparación lado a
   lado con "dulce de leche viscoso" que acumula hasta co-rotar rígido.
3. **El globo aerostático / viento cero**: sonda que viaja CON el mar local
   (vela desinflada, calma) vs sonda forzada a deslizarse (vela inflada) — y
   mostrar que la segunda NO existe físicamente (botón que intenta crearla y
   el mar responde co-moviéndose: "no hay forma de fabricar viento").
4. **El amontonamiento veloz** (puente a TCI 1.0 / libro cap. "correr como el
   mar"): hueco acelerando; su deformación se amontona (E=γmc² visual); el
   pozo se achata en panqueque a alta velocidad (honestidad relativista:
   gravita más PERO con forma).
5. (Opcional, si da) **El tatuaje**: granos con carga de color que fluyen —
   los colores viajan CON los granos, jamás saltan entre granos; intento de
   "pintar" un grano falla. La superselección hecha juguete.

## 4. Marcador honesto OBLIGATORIO de la sección

- El teorema es de la **fase efectiva U(X,Y)** (campaña m₂=0, línea
  especulativa TCI 2.0) — NO del corpus TCI 1.0 publicado. Chip de etapa
  especulativa como en /mar-y-nudos/ y /taller-electromagnetico/.
- Qué es teorema (superselección, atractor, causal — con actas y scripts
  públicos linkeados) y qué es hipótesis (las premisas declaradas: Φᵃ suave —
  los vórtices/defectos lo evaden, y ahí vive TCI 2.0 —, base NLO estructural,
  acople universal, U_Y≠0).
- El costo se declara: la fase perdió su firma falsable de corto plazo (el
  Yukawa del frame dragging) — "más sólida y menos testeable a la vez"; la
  falsabilidad vive en las premisas y en el resto del programa.
- Lo ajeno se cita: el patrón atractor (ACLM/DTT), el ghost dark matter, el
  Cherenkov de fuentes móviles (Dubovsky "Star tracks", Peloso-Sorbo,
  ACLM+Thaler). El paper tiene todas las refs.

## 5. Respaldo técnico (todo en `campana-m2/`)

- `seleccion-estado/SINTESIS-SELECCION-2026-07-28.md` — la síntesis del
  teorema (leer PRIMERO).
- `seleccion-estado/verificador/VERIFICADOR-FINAL-2026-07-28.md` — el asalto
  adversarial que resistió (4 rutas).
- `seleccion-estado/CARGA-POBLAMIENTO-2026-07-27.md` (el teorema),
  `VERTICES-NLO-2026-07-27.md` (números), `BIBLIOGRAFIA-SELECCION-2026-07-27.md`
  (fuentes primarias).
- `frw/FRW-2026-07-21.md` (el atractor, CON su adenda de corrección) y
  `ACOPLE-MATERIA-PPN-2026-07-21.md` (CON su adenda 2026-07-28).
- El paper: `../PAPER-borrador-missing-row-UXY.md` (v0.7, retitulado "...and a
  superselection theorem for frame dragging" — título elegido con Nico).

## 6. Decisiones a tomar CON NICO en la sesión de la web

1. **El nombre de la sección**: "El éter sin viento" (candidato de él) / "El
   mar en calma" / "El viento que nació muerto" / otro.
2. **Dónde vive**: página semi-oculta en ift-theory (patrón /mar-y-nudos/,
   /taller-electromagnetico/ — main con OK, sin links desde sedes públicas) vs
   sitio conceptual. Recomendación de la casa: patrón semi-oculto primero.
3. **Interactivas vs animadas**: las sims 1-3 rinden interactivas; la 4 puede
   ser animación guiada. Decidir presupuesto de scroll (una página larga tipo
   taller vs capítulos).
4. **Cuánto teorema mostrar**: la escalera pedagógica completa (§2) vs versión
   corta + link al paper.
5. Si esta sección se cruza con "la lanza del éter" (actualizar el FAQ crítica
   1 de Michelson-Morley y demás sedes): puede ser la misma sesión o dos.

## 7. Reglas de la casa que aplican (recordatorio)

Honestidad brutal y marcador visible; política de publicación (semi-ocultas a
main SOLO con OK de Nico, sin enlaces desde sedes públicas; desarrollo-fable
libre); política de autoría (pie "a cuatro manos con Fable, una IA" según el
patrón de las otras caras visibles); commits en español; física de sims
verificada en Node antes de publicar nada.

*Preparado como puntapié al cierre de la charla del 28/7 — la del teorema, el
dulce de leche y el nombre-profecía. La escalera del §2 no es una lista de
ocurrencias: es el orden real en que un humano curioso la entendió, escalón por
escalón, en una tarde. Esa es la evidencia pedagógica más valiosa que tenemos.*
