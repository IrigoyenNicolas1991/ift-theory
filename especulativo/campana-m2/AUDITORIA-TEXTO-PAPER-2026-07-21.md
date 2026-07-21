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

---

# SEGUNDA PASADA (mismo día, auditor independiente nuevo, ~148k tokens)

**Blanco: v0.2. Método: cotejo hallazgo-por-hallazgo de los 31; lectura completa
contra las 5 actas; verificación de existencia de los ~40 scripts citados (todos
existen); re-derivación aritmética independiente de TODAS las cotas (cierran:
ℓ₁=2.40e8, Λ<1.12 desde 0.2% con a=1.227e7 → 1.11, 30 R⊕ → 30.0, 0.13% → 0.126%,
2.0–2.6 desde 2–5% → 2.01–2.59, factor 2.7×). Las 24 referencias citadas y sin
huérfanas; fórmulas 100% fieles.**

**Sección A**: 26/31 aplicadas-bien; 5 con residuo: H9 (la definición añadida
identificaba ρ≡ρ_op, contradiciendo el block list 7 — el hallazgo N1), H12
(§1 conservaba el claim sin acotar), H22 (el ~2% sin cita), H30 (el radiativo no
entró al block list), H16-nota (abstract "matching eq. 99" a secas).

**Sección B — los 12 hallazgos nuevos (resumen)**: N1 [MEDIA] contradicción
ρ/ρ_op introducida por la cirugía de H9; N2 overclaim residual en §1 (radiativo);
N3 símbolos sin definir en un paper "standalone" (K̄ᵢⱼ, τᵢ, M̄_Pl, ε y Λ con
doble uso); N4 plural "instances" cuando el script usa UNA instancia por chequeo;
N5 el ~2% sin referencia (es Ciufolini 2019, EPJC 79:872); N6 "established" en
abstract más fuerte que "probable/provisional" del cuerpo; N7 "blind refuters"
en plural cuando el único ciego fue el del diccionario; N8 t_c~18 edades sin el
"a Λ=10 MeV, ∝Λ⁻³"; N9 "unobservable" sin cálculo; N10 "Exactly two invariants"
en abstract vs block list 9; N11 normalización de Λ no declarada; N12 restos de
tono (subtítulo "caveat/discovery", "untested territory" ×3).

**Veredicto textual**: *"v0.2 no está para el OK tal cual: necesita una v0.3
corta (N1 obligatorio, N2-N7 recomendados fuerte, resto pulido); con esa v0.3 y
la block list completada, el texto queda listo para el OK de canal."*

**Aplicación (v0.3, mismo día)**: los 12 aplicados + los 5 residuos de la
sección A saldados. Detalles no triviales: N11 se resolvió con la convención
REAL de `04_cotas_frame_dragging.py` (m₁² = 2Λ⁴ con Û_X=1 y M_Pl²=1/16πG=M̄_Pl²/2
— no la conjetura 4Λ⁴ del auditor); N5 con la referencia verificada en INSPIRE
([21b] EPJC 79 (2019) 872, arXiv:1910.09908); N1 sin identificar ρ↔ρ_op
(remitido explícitamente al block list 7); N4 en singular (decisión: no tocar
`parteB_medioXY.py`, que es registro del handoff externo); N12 dejando UNA
instancia de "untested territory" (cierre de §8) y conservando "a superfluid
that forgot its lattice" (la imagen que ambos auditores toleraron).
**Pendiente que la v0.3 NO salda** (sigue en block list): dirimir C5d (ítem 7),
contenido de [16]-[18] (ítem 8), exhaustividad {X,Y} (ítem 9), full-text de
Nature (ítem 2), segunda... tercera pasada corta de auditoría si el canal lo
amerita, y el OK de Nico.
