# Briefing — ¿Tiene la espuma de vortones una fase hielo? (el EM del sótano)

**Preparado 2026-07-21 (sesión campana-m2), a pedido de Nico, para ser retomado por
cualquier sesión futura. Es un PASO 0: papel antes que cómputo, criterios de muerte
declarados. La sesión que lo tome escribe su propia acta (protocolo de sesiones
paralelas: archivos propios).**

## La pregunta en una frase

¿Existe un régimen de la espuma de vortones con **degeneración extensiva tipo ice rule**
— el combustible de una fase Coulomb emergente (cargas 1/r genuinas, mecanismo
Castelnovo-Moessner-Sondhi) — en algún grado de libertad **compatible con (o desacoplado
de) el orden laminar J=2** que la gravedad necesita?

## Por qué importa

- El frente de la luz está trabado arriba: la 6ª lápida (condensar cuerdas cuesta una
  polarización TT) y π₂=0 (sin extremos = sin electrones) dejaron al fotón solo la
  rendija fermiónica de los tubos (compuerta única, §34 bitácora madre).
- El censo estático del sótano (acta `SOTANO-PASO0-censo-estatico-2026-07-21.md`, canal
  14) mostró que el argumento "div ω=0 ⟹ sin cargas" era insuficiente: **el hielo de
  espín es el contraejemplo publicado** — cadenas de dipolos con div B=0 exacto
  telescopean a monopolos 1/r genuinos (verificado con sympy) cuando el fundamental es
  extensivamente degenerado. Nuestro laminar antialineado NO lo es — por eso la lápida de
  gravedad se sostiene — pero la puerta EM quedó anotada.
- El signo funciona: gauge emergente spin-1 ⟹ cargas iguales se REPELEN — inservible
  para gravedad, **correcto para electromagnetismo**.

## La sospecha estructural (declararla antes de empezar)

En el hielo de espín la fase Coulomb vive en el régimen desordenado: la degeneración
extensiva ES el combustible. Si la ice rule tuviera que vivir en las MISMAS orientaciones
n̂ que portan el orden J=2 laminar, esto sería la 6ª lápida repetida un piso más abajo
(o moneda o gravedad). La única salida elegante: que el sector hielo viva en **otro**
grado de libertad. Ojo técnico: para la interacción dipolar lo que importa es
p̂ = Γ·n̂ (signo de circulación y orientación NO son independientes — flipear Γ equivale
a flipear n̂); el "pseudo-espín" candidato es el dipolo completo.

## Grados de libertad candidatos (examinarlos en este orden)

1. **Geometría de red no-bipartita** (la ruta dipolar spin ice): ¿hay una red (pirocloro
   de anillos, kagome apilado…) y un régimen de densidad donde el fundamental dipolar con
   el SIGNO VÓRTICE sea extensivamente degenerado en vez de laminar? Herramienta lista:
   nuestro Luttinger-Tisza + Ewald certificado (`sotano_bulk_veredicto.py`). OJO: en el
   spin ice magnético la degeneración necesita ejes de Ising LOCALES (anclaje); dipolos
   libres sobre pirocloro ORDENAN. ¿Qué anclaría los n̂ acá? (¿anisotropía local de la
   red misma? ¿el D₄ del piso de arriba?) — esta es la subpregunta que probablemente
   decida todo.
2. **El apilado de politipos** (rama 1: gaps 0.0008–0.005, cuasi-degenerado): ¿la
   degeneración de registro es extensiva (∝N) o subextensiva (∝capas)? Sospecha
   declarada: subextensiva ⟹ no alcanza para fase Coulomb. Verificar y cerrar.
3. **El sector del núcleo** (segunda componente: fases/corrientes internas de cada
   vortón): ¿frustración propia, desacoplada del orden orientacional? Virgen.
4. **La variante líquido-nemática (sinergia con rama 8 / dragón 9)**: si el lema de
   exclusión fuerza a fundir las posiciones de todos modos, la pregunta se vuelve: ¿el
   fundido es un líquido trivial o un **líquido Coulomb**? (la fase Coulomb ES un
   líquido correlacionado). Si dragón 9 y puerta-hielo se resuelven JUNTOS, sería la
   convergencia más elegante del sótano. Idealmente examinar después (o junto con) el
   examen de la rama 8.

## Criterios de muerte (pre-declarados)

- **M1**: ningún grado de libertad admite degeneración extensiva compatible con (o
  desacoplada de) el orden J=2 ⟹ lápida barata, el EM del sótano muere, la ceca vuelve
  al piso de arriba (compuerta única).
- **M2**: la degeneración existe SOLO destruyendo el orden laminar ⟹ documentar como
  "6ª lápida bis": la disyuntiva moneda-vs-gravedad es estructural en ambos pisos (eso
  también es un resultado).
- **Si sobrevive**: siguientes pasos en orden — (a) ¿qué defecto viola la ice rule? (esas
  son las cargas; ¿son vortones especiales, o excitaciones nuevas?); (b) confrontar con
  las dos monedas χ± del piso de arriba (§30): ¿es el mismo U(1) visto desde abajo o uno
  nuevo?; (c) el conteo de polarizaciones TT del piso de arriba NO debe pagar el costo
  (verificar que la moneda de abajo no repita la 6ª lápida arriba).

## Literatura de arranque (verificar identificadores antes de citar — varios van de memoria)

- Castelnovo-Moessner-Sondhi, "Magnetic monopoles in spin ice", Nature 451:42 (2008) —
  VERIFICADO en el censo del paso 0.
- Henley, "The Coulomb phase in frustrated systems", Annu. Rev. Condens. Matter Phys. 1
  (2010) — el marco general [de memoria].
- den Hertog & Gingras (dipolar spin ice, PRL 84:3430 (2000)) [de memoria].
- **Vortex ice**: Libál-Olson Reichhardt-Reichhardt, "Creating artificial ice states
  using vortices in nanostructured superconductors", PRL 102:237004 (2009) [de memoria]
  + realización experimental posterior (Latimer et al. PRL ~2013) [de memoria] — el
  precedente de que los vórtices SÍ hacen hielo con la geometría correcta.
- Artificial spin ice reviews (Nisoli-Moessner-Schiffer RMP 85:1473) [de memoria].
- Del proyecto: acta del paso 0 (canal 14 + falla 2 del verdugo), tronco del sótano §5
  (maquinaria LT/Ewald certificada), bitácora madre §30 (dos monedas) y §32/§34 (6ª
  lápida y compuerta única — el costo que la moneda NO debe repetir).

*Estado: pregunta bien planteada, sin tocar. Costo estimado del paso 0: una sesión de
papel + a lo sumo corridas LT sobre 2-3 redes con la maquinaria ya certificada.*
