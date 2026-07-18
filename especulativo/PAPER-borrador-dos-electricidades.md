# [BORRADOR — ETAPA ESPECULATIVA, NO PUBLICAR SIN OK EXPLÍCITO DE NICO]
# Esqueleto del paper chico: "Two decoupled Coulomb sectors and dark channels
# in the vortex electrodynamics of a tensorial superfluid"

**Estado**: esqueleto (2026-07-18). Género: física de análogos / materia condensada
(NO es "TCI deriva el EM" — el alcance está acotado a lo calculado).
**Condiciones previas a cualquier publicación** (lista de bloqueo):
1. [x] Barrido de novedad (2026-07-18, 14 búsquedas + 6 lecturas): **encontrado
       PARCIAL** — el paquete completo (tensorial J=2 + 4:1 exacto por simetría +
       desacople χ± + framing dos electricidades + canales oscuros) NO está
       publicado; el framing EM con radiación oscura: cero resultados. PERO la
       versión VECTORIAL existe (Rubo PRL 99:106401 polaritones (±½,±½); ³He-A
       folklore Volovik; Babaev; Eto) y el vecino más cercano en London con cargas
       (fase, orientación) es How-Yip PRR 2:043192 (acopladas, sin 4:1, sin
       desacople). CONSECUENCIA DE FRAMING: presentar como "observación
       estructural + consecuencias" — en el BN spin-2 el estado ES dos componentes
       m=±2 y el desacople es cuenta corta; el valor está en explotarla (tabla de
       especies, tests no lineales/dinámicos, canales oscuros), no en la
       dificultad. Deuda residual: literatura rusa vieja de ³He y 2 full-texts
       inaccesibles (2107.02448, 2510.26720) — revisar antes de mandar a nadie.
2. [x] Robustez con gradiente completo (K₂+K₃): HECHA (2026-07-18, modo `div`):
       cargados −5.31/+5.71 vs ∓5.60 London (2-5%), neutros ±0.03 ≈ 0. El
       teorema sobrevive el funcional completo. (Bonus: con div las E absolutas
       de los neutros difieren pero la fuerza sigue neutra — como debe.)
3. [x] Residuo entre sectores MEDIDO (2026-07-18, modo `residuo`, fuerza directa
       sobre el anclaje con doble control: Coulomb F·d=+2.79/+2.73 vs +2.77 y
       fuerza de borde del nudo solo = 0.000000): **atractiva, |F| ~ 1/d^3.19**
       (4 puntos d=10-28) — potencia dipolar ~d⁻³ confirmada; el log de Eto
       (efectivo ~2.5 en este rango) no preferido por los datos — pregunta
       abierta declarable (¿acople tensorial ≠ dos componentes?). Bonus: explica
       el tamaño ~3ξ de la molécula (atracción d⁻³ + repulsión de core).
4. [ ] OK explícito de Nico (política de la casa para la línea TCI 2.0).
5. [ ] Decidir canal: Zenodo (tenemos DOI concepto) vs arXiv (requiere endorsement).
6. [ ] DECLARACIÓN OBLIGATORIA (del barrido): el régimen dos-Coulomb-log vale solo
       con la simetría orientacional exacta (gapless); en el ³P₂ REAL el campo
       magnético y el spin-órbita la rompen y los HQV quedan confinados por
       solitones (Kobayashi-Nitta PRC 105/107) — nuestro mar la tiene libre por
       HIPÓTESIS del modelo TCI. Decirlo en el abstract, no en un pie de página.

## Título tentativo
Two decoupled Coulomb sectors in the vortex electrodynamics of a biaxial-nematic
(³P₂-like) condensate: exact 4:1 stiffness ratio, neutral molecules, and dark
radiation channels

## Claims (exactamente estos, ni uno más)
1. En la fase D₄-BN de un condensado J=2 (funcional GL textual de la literatura
   ³P₂, Yasui-Chatterjee-Nitta), el límite de London de los HQV tiene matriz de
   rigideces diagonal (sin cruce fase-orientación), cociente EXACTO 4:1, e
   isotropía en el plano — de donde: dos gases de Coulomb logarítmicos
   independientes de igual constante (base χ± = φ ± 2α ↔ componentes ψ∓₂).
2. Las 4 especies de HQV llevan carga (±1,0)/(0,±1); la mitad de los pares es
   neutra a orden log. Verificación no lineal completa (campo de 10 componentes):
   pendientes log al 1-3.5% de London, neutralidad < 0.5%.
3. El vórtice entero se parte en la molécula neutra (reproduce Masuda-Nitta con
   maquinaria independiente); en el modelo mínimo la molécula es marginalmente
   ligada (sin solitón confinante — contraste declarado con Kobayashi-Nitta, que
   tienen campo externo).
4. Dinámica (2º orden, declarada): el anti-par no orbita (potencial log
   confinante: v_circ²/c² ~ 1/ln(d/ξ); + atracción Ampère de corrientes ∝ Ω²) —
   captura = fusión en ~¼ vuelta; el estallido radia ~91% de la energía interna,
   con sectores INCOMUNICADOS (correlación fase-rotación máxima) y canales
   vectoriales EXACTAMENTE oscuros (protegidos por simetría del evento); cola
   masiva sonando en el gap.

## No-claims (sección explícita de límites — estilo de la casa)
- NO derivamos Maxwell ni el fotón: las ondas de los sectores no son la luz del
  modelo mayor (velocidades/anisotropía, bitácora §23); el U(1) de largo alcance
  para defectos puntuales (anillos: campo lejano dipolar, sin monopolo con π₂=0)
  requiere red (string-net) o sector de defectos — fuera de alcance acá.
- NO es el examen Hulse-Taylor: el juguete 2D no puede rendirlo (log confinante).
- La dinámica GP (Magnus, Kozik-Svistunov) es una clase distinta — no comparable
  directo; declarado.
- Vecinos a citar SIEMPRE: Babaev PRL 89:067001 (compuestos neutros en two-gap);
  Eto et al. PRA 83:063603 (dos sectores log en 2-comp BEC); Seo PRL 115:015301;
  Masuda-Nitta PTEP 2020; Kobayashi-Nitta PRC 105:035807; dualidad vórtice↔carga
  2D clásica; Chojnacki et al. PRB 109 L220407 (contexto spin-2 análogo).

## Estructura tentativa (6-8 páginas)
1. Intro: HQVs en condensados tensoriales; qué agrega esto a Eto/Babaev
   (orientación como segunda moneda con 4:1 exacto; el framing de dos
   electricidades; el test dinámico).
2. Modelo: GL textual ³P₂, fase D₄-BN (γ>0 declarado como elección), London.
3. Teorema de las dos monedas (analítico) + tabla de especies.
4. Verificación no lineal (métodos: gradiente Wirtinger, autotests; resultados).
5. La molécula y su marginalidad.
6. Dinámica: plunge, Ampère, canales oscuros, cola masiva.
7. Discusión: qué haría falta para un U(1) de largo alcance genuino (red /
   defectos); relación con materia de neutrones (³P₂ real: γ<0 → UN; nuestro
   régimen es hipotético declarado).
8. Reproducibilidad: scripts públicos (coulomb_del_mar.py, binaria_del_mar.py,
   analiza_binaria.py) + datos.

## Datos que ya existen para las figuras
- Tabla de pendientes log (4 pares × 3 distancias) — §30.
- d(t) del plunge (5 lanzamientos superpuestos: la universalidad del colapso).
- Tabla de canales en 3 ventanas + espectros (binaria_datos.npz local).
- Falta generar: mapa 2D del campo en la fusión (bonito para figura, opcional).
