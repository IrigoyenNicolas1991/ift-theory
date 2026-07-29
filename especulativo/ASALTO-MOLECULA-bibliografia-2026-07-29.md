# El fermión de la red, primer asalto — acta bibliográfica (previa al veredicto numérico)

**2026-07-29 · Fable · 1 agente bibliográfico (~198k tokens, 79 operaciones, 16
papers leídos en fuente primaria — ar5iv/TeX completos, no abstracts). Regla
aplicada: cada afirmación con cita textual leída; lo no verificado, declarado.
Este documento fija el marco teórico y la vara de novedad ANTES de conocer el
resultado del cálculo de la molécula (corriendo al momento de escribir esto —
el orden importa: la biblioteca no puede contaminar al juez).**

---

## 1. Callan-Harvey aplica a nuestro caso, verificado ecuación por ecuación

- Original: Callan & Harvey, Nucl. Phys. B 250, 427 (1985) (pre-arXiv; título y
  journal verificados en la ref. [39] de hep-th/0509097). Exposición detallada
  leída: **Harvey, "TASI lectures on anomalies", hep-th/0509097, §4.1-4.2**
  (ecs. 105-133): rama quiral ligada al core de una cuerda (Φ = f(ρ)e^{iθ},
  zero mode con γ^int η = −η), corriente de inflow radial tipo Hall desde el
  término axiónico, y cancelación exacta vía **d²a = 2π δ₂(Σ²)** (ec. 124) —
  "a is not a smooth function. It has winding number one around the origin".
- **La condición sobre el bulk es solo esta**: fermiones de bulk MASIVOS
  (gapeados) cuya fase de masa winde alrededor del defecto. NO exige Chern por
  rebanada del bulk — el σ_H efectivo local viene de ∇a. **Nuestro caso (bulk
  D₄ mudo, C=0 por rebanada, toda la quiralidad del winding del defecto) ES el
  caso Callan-Harvey**, no una variante exótica.
- Precedente condensed-matter explícito de "bulk trivial + quiralidad del
  defecto": **Chan-Liu, arXiv:1611.08516** (PRL 118, 207002): "While the 3D
  gapped PDW phase is topologically trivial, a vortex line generated in such
  phase can host chiral Majorana modes… protected by an emergent second Chern
  number of a synthetic 4D space".
- Clasificación general: **Teo-Kane, arXiv:1006.0690** (PRB 82, 115120), §III:
  el invariante del defecto de línea es el second Chern number en (k,s),
  reescrito como winding de θ(s); clase D → **Z, "Chiral Majorana"**. Nuestro
  C=−1 cae exactamente ahí.
- Puente a superfluidos: **Kopnin-Volovik-Parts, cond-mat/9509157**: "The
  spectral flow of the fermion zero modes within the vortex core is a
  realization of the Callan-Harvey mechanism" (con Volovik JETP Lett. 57, 244
  (1993), verificado por doble referencia — pre-arXiv, no leído directo).

## 2. La vara de novedad: qué existe y qué NO (buscado con intención de refutar)

**Existe** (y se cita como pariente):
- Ramas quirales Majorana dispersando en k_z en líneas de vórtice: **Wang-Fu,
  arXiv:1703.06880** (PRL 119, 187003) — HQV en s+ip con U(1)×U(1), "the half
  quantum vortex line binds a propagating chiral Majorana mode", ε(k_z)=v_M k_z;
  la quiralidad la fija CUÁL componente del doblete windea ("For the opposite
  half vortices (−1,0) and (0,1)… opposite chirality"). Mecanismo: la Weyl FS
  del bulk — pairing QUIRAL, distinto del nuestro.
- Flat bands de core acotadas por proyecciones de nodos: **Volovik,
  arXiv:1011.4665** (JETP Lett. 93, 66) — el método de rebanadas en k_z, para
  bulk con Fermi points (³He-A, quiral).
- El espectro clásico de vórtices: **Volovik, cond-mat/9909426** — E(L_z) =
  −m L_z ω₀ (la pendiente en L_z la fija el winding de FASE m; índice −2m);
  clases n vs n+½ por paridad de m+N. Flujo espectral clásico: en Q (momento
  angular), NO en k_z.
- **Nuestro sistema exacto, la serie Masaki-Mizushima-Nitta**: arXiv:2107.02448
  (PRB 105 L220503, HQV no abelianos (½,±¼) en D₄-BN, molécula estabilizada por
  la componente UN, un zero mode por HQV con protección mirror), arXiv:1908.06215
  (PRR 2 013193, vórtices axisimétricos, ramas quirales en ℓ y efecto del core
  relleno γ_{M=±1} — "gap out a pair of chiral branches… crossing at ℓ=0"), y
  el review arXiv:2301.11614 (2024). **TODO a k_z = 0.** Hasta el review más
  reciente del grupo no hay ε(k_z) del HQV ni flujo espectral en k_z.

**NO existe (huecos reclamables, 6):**
1. Flujo espectral en k_z de un HQV en fase NEMÁTICA (no quiral, Chern por
   rebanada cero) — los precedentes exigen pairing quiral o Weyl FS.
2. El mecanismo "relleno del core rompe una PH de rebanada y genera la rama
   quiral neta" — inédito (lo más cercano: el gapeo de ramas en ℓ de 1908.06215;
   nadie conectó orden del core con quiralidad en k_z).
3. El espectro ε(k_z) del HQV (½,±¼) del ³P₂/D₄-BN — la serie MMN se detiene
   en k_z=0.
4. La regla "fase vs marco" para windings FRACCIONARIOS de marco (±¼) — existen
   la versión entera (Volovik: pendiente = −m·ω₀) y la de doblete U(1)×U(1)
   (Wang-Fu); la no-abeliana, no.
5. Molécula de dos tubos HQV cuyos Majoranas quirales componen un Dirac quiral
   CARGADO bajo un U(1) colectivo — Ivanov (cond-mat/0005069) lo hace con zero
   modes 2D ("the two Majorana fermions may be combined into a single complex
   fermion"); QHZ (arXiv:1003.5448) y Teo-Kane con dos Majoranas en el MISMO
   borde/defecto ("a chiral Dirac fermion can be split into a pair of chiral
   Majorana fermions"). La versión dos-tubos-separados + carga U(1): virgen.
6. **El teorema "conservación en las uniones + cables quirales ⟹ U(1) gauge
   emergente": NO EXISTE.** Las redes de cables publicadas dan semimetal o
   topological order gapeada — Raza-Sirota-Teo arXiv:1711.05746 (PRX 9, 011039:
   los cables son vórtices de masa a la Jackiw-Rossi; single-body → Dirac
   semimetal, many-body → topological order/Pfaffian; SIN fotón), Fuji-Furusaki
   arXiv:1901.05918 (→ Z₂ gauge gapeada). El único fotón 3D emergente verificado
   es bosónico: **Motrunich-Senthil, cond-mat/0407368** — constraint local
   N_r=0 ⟹ "the ground state sector constraint N_r=0 is simply the Gauss law",
   fase Coulomb deconfinada con fotón. Ese es el pariente a imitar con
   fermiones: si la red de tubos del mar produce el U(1) con ley de Gauss
   fermiónica en las uniones, es enunciado NUEVO.

## 3. Lectura para el asalto en curso

- El marco Callan-Harvey ampara la rama del Paso B tal como salió (bulk mudo +
  defecto que winde) — el inflow existe y se puede calcular (siguiente etapa de
  papel: la corriente radial del bulk D₄ hacia el core).
- Para la pregunta fase-vs-marco: el pariente más cercano (Wang-Fu) sugiere que
  el par análogo a (1,0)+(0,1) lleva quiralidades IGUALES (⟹ C_mol=−2), pero su
  mecanismo (Weyl FS de bulk quiral) NO es el nuestro (relleno del core en bulk
  mudo) — sugiere, no decide. El juez es el cálculo corriendo.
- Citas obligadas del asalto (lista completa con quotes en este archivo y los
  .txt del agente en el scratchpad de sesión): CH85 + Harvey TASI; Volovik 93/99
  + KVP; Teo-Kane; Volovik flat band; Wang-Fu (+ Qi-Witten-Zhang PRB 87 134519
  y Stone-Lopes PRB 93 174501, verificados solo como citas); Chan-Liu; la serie
  MMN completa; Ivanov; QHZ; Motrunich-Senthil; Raza-Sirota-Teo y Fuji-Furusaki
  (por contraste).
- Advertencias de honestidad del agente, heredadas: el libro de Volovik no se
  leyó directo (cubierto por sus papers); Stone-Gaitan 87, Volovik 93,
  Thuneberg/Salomaa-Volovik 86, QWZ 2013 y Stone-Lopes 2016 verificados solo
  como referencias citadas en papers leídos; la correspondencia
  2107.02448 ↔ PRB 105 L220503 vista en metadata, no en fuente primaria.
