# Auditoría adversarial del TEXTO del paper "The missing row" — informe completo

**2026-07-21 · auditor: 1 agente adversarial independiente (~169k tokens, 16 usos de
herramientas, ~18 min) · blanco: `../PAPER-borrador-missing-row-UXY.md` v0.1 · fuentes
de contraste: las 3 actas + handoff + scripts (corrió `colA_causal.py` completo y
verificó aritmética de cotas de forma independiente).**

**Veredicto del auditor**: *"No está listo para pulido final: necesita cirugía menor —
un día de trabajo, ninguna amputación. Las tres patas técnicas se sostienen; lo que
falla es la costura."*

**Estado**: los 31 hallazgos fueron aplicados EL MISMO DÍA (v0.2 del paper, mismo
commit que este archivo). Detalle de aplicación al final. Lo que el auditor validó
positivamente: fórmulas y números transcritos de las actas fieles al 100% en ~40 ítems
cotejados (incluida la aritmética de ℓ₁, cotas Λ, series de supresión y el límite Kerr);
deudas duras declaradas con la prominencia debida; política de autoría cumplida.

---

## Los 31 hallazgos (verbatim del auditor)

1. **[ALTA][transcripción/consistencia]** §7: "verified to residues [0,0,0,0] in the
   eight field equations" — el acta y los scripts muestran 4 EOM del sistema masivo +
   4 de RG pura (C3/C4; v1a imprime 4+4). "Eight" no corresponde a ninguna salida y
   choca con el "[0,0,0,0]" de la misma frase.
2. **[ALTA][overclaim/reproducibilidad]** "run in seconds"/"under a minute" era falso
   (`colA_causal.py`: 129 s) y 5 scripts de `acople/verificador/` no corrían desde el
   repo (import de `../verificador-m2/` inexistente) + ruta absoluta hardcodeada en
   `frame-dragging/01_derivacion_vector_fuente.py` — el pipeline verificador de la
   firma estrella era irreproducible por terceros.
3. **[ALTA][novedad/omisión de registro]** La sección Novelty search citaba queries,
   conteos y "all 19 papers listed" sin acta formal del barrido.
4. **[MEDIA][overclaim]** §1 "nobody has ever computed anything in any phase of this
   class" contradice §8/acta: DTZ computaron fuentes rotantes en la fase espejo m₁²=0.
5. **[MEDIA][consistencia]** El sector vectorial descrito 3 veces sin reconciliar
   (gapped (73) / healthy / no propaga a LO con gravedad).
6. **[MEDIA][overclaim]** "phases with m₁²≠0 have a two-state structure" (plural) —
   el acta lo dice de ESTA fase.
7. **[MEDIA][consistencia interna]** §4 "any quantum counterterm… is again U(X,Y)"
   choca con los NLO de §6 (respetan la simetría y no son U(X,Y)).
8. **[MEDIA][respaldo condicional]** La pata Nature/LARES-2 presentada en abstract y
   scoreboard con la salvedad (solo abstract+prensa verificados) recién al final de §8.
9. **[MEDIA][omisión]** σ, ρ, ρ_op nunca definidos; α, β solo genéricos — "stand
   alone" incumplido.
10. **[MEDIA][reproducibilidad]** El chequeo C5d de `colA_causal.py` imprime "esperado
    0" con residuo NO nulo ∝ m₁²p⁴ρ_op² — visible para cualquiera que reproduzca.
11. **[MEDIA][novedad/respaldo]** Caracterizaciones de [16]-[18] (solid inflation,
    holografía, crystal gravity) sin verificación de contenido citada.
12. **[MEDIA][overclaim/omisión]** "Everywhere Einstein is well measured, this phase
    is Einstein" — el sector radiativo (Hulse–Taylor) ni calculado ni declarado.
13. **[BAJA-MEDIA][overclaim]** "PPN α₁, α₂ have never been computed" — evidencia: un
    grep en un solo review.
14. **[BAJA-MEDIA][precisión]** B4/B3 son instancias exactas aleatorias, no
    identidades simbólicas: "identically"/"generic" excedían.
15. **[BAJA][overclaim]** Abstract "was never constructed" sin acotamiento.
16. **[BAJA][consistencia]** "matches eq. (99) verbatim" cuando §2 declara el signo
    impreso mal — coincide con la (99) corregida.
17. **[BAJA][precisión+PLAUSIBLE]** c_T "untouched": vale para la masa, no la
    velocidad; falta flag de |c_T−1|≲10⁻¹⁵ (GW170817) sobre α.
18. **[BAJA][tono]** Melodrama LARES-2 repetido 4 veces.
19. **[BAJA][tono]** Inventario de dialecto vendedor (10 frases listadas).
20. **[BAJA][gramática]** "Every row says whose each piece is"; "(they define, not
    embarrass, the program)".
21. **[BAJA][bibliografía]** [2] y [14] huérfanas (no citadas en el cuerpo).
22. **[BAJA][respaldo]** "claimed accuracy 2–5% [21]" — [21] reclama ~5%; el 2% es de
    análisis posteriores no citados.
23. **[BAJA][precisión]** "[22, 24] dispute" — [22] disputa, [24] DEFIENDE.
24. **[BAJA][omisión]** El semieje orbital de las cotas nunca declarado (a≈1.227×10⁷ m).
25. **[BAJA][claridad]** BD ghost vía m₀=0 como contexto sin aclarar que es OTRA fase.
26. **[BAJA][novedad]** "its first phenomenology with matter" sin "to our searches".
27. **[BAJA][observación]** Exhaustividad de {X,Y}: los scripts verifican invariancia,
    no unicidad — nota recomendada.
28. **[BAJA][consistencia]** La remark "gauge fixing" usada con dos significados
    (§7 teorema / §8 rama co-rotante); el acta la asigna a la rama.
29. **[BAJA][transcripción menor]** (7.21) sin "at a=1" en línea; "none refuted" sin
    mencionar las 4+1 fallas menores que los verificadores sí encontraron (suma
    credibilidad decirlo).
30. **[BAJA][omisión]** Block list sin los ítems: scripts rotos, C5d, contenido
    [16]-[18], radiativo, acta INSPIRE.
31. **[PLAUSIBLE][bajo]** Tajmar–de Matos citado sin calificativo (claims de
    laboratorio no replicados).

## Aplicación (v0.2, mismo día)

- **Scripts (H2, H10)**: imports de los 5 verificadores redirigidos a
  `escalar/verificador/` (la lib es la misma; en la sesión original vivía en una
  carpeta `verificador-m2/` que no entró al repo); ruta absoluta de
  `01_derivacion_vector_fuente.py` relativizada; DOS bugs reales adicionales
  reparados en `v2_vector_fuente.py` (dict de sustitución con la expresión A como
  clave; `Derivative` respecto de expresión compuesta) — **la suite completa del
  acople corre ahora desde el repo** (v1a 6s, v1b 4s, v1c 4s, v2 16s, v2b 4s,
  01 8s; `colA_causal.py` ~2 min) y reproduce los chequeos citados en el paper
  ([0,0,0,0], series (1+x)e⁻ˣ y (1+x−x²)e⁻ˣ, B−Bclaim=[0,0,0]). C5d: comentario
  de estado en el script + ítem de block list (pendiente de dirimir, no se toca
  la lógica).
- **Acta del barrido (H3)**: escrita — `BARRIDO-INSPIRE-2026-07-21.md` (queries
  textuales, hits, los 19 papers, limitaciones declaradas).
- **Texto (todos los demás)**: aplicados en v0.2; el preámbulo del paper registra
  la versión y remite a este informe.
