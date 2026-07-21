# Campaña m₂=0 — el medio U(X,Y) y la fase protegida de Dubovsky

**Trabajo importado.** Esta campaña se corrió en una sesión externa (2026-07-20) y entró
al repo vía el documento de handoff autocontenido `HANDOFF-campana-m2-2026-07-20.md`,
que contiene el contexto completo, las convenciones (BCP 1603.02956), los resultados,
el texto de la nota final y el código fuente.

**Resultado central**: el medio U(X,Y) — invariante bajo difeomorfismos espaciales
internos irrestrictos Φᵃ→Ψᵃ(Φᵇ), la fila que falta en la Tabla 2 de BCP — realiza
exactamente la fase protegida de Dubovsky (hep-th/0409124, ec. 72): sobre el vacío
Minkowski m₂²=m₃²=m₄²=0 emergen de los tadpoles, m₁²=2U_X, y existe esquina explícita
sin fantasma (m₀²m₁²>0). Además, lema de exclusión: m₂² = −2×(rigidez de corte del
medio) ⟹ proteger la masa del gravitón exige mar **fluido** a orden dominante — con
los escapes declarados (orden interno tipo Chojnacki 2310.10078; gravedad inducida),
que son exactamente donde vive la línea D₄-BN de la bitácora madre.

## Verificación (Fable, 2026-07-21, en esta máquina)

Los 3 scripts extraídos del handoff corren con Python 3.14 + SymPy 1.14 y reproducen
**todas** las salidas declaradas:

| Script | Chequeo | Resultado |
|---|---|---|
| `masas_medio.py` | diccionario general, isotropía (5 ceros), m₀² vs BCP (7.5) | ✓ exacto |
| `calibracion_fonones.py` | CAL-4 oro (Goldstone vs gauge unitario) | resto = 0 ✓ |
| `parteB_medioXY.py` | B1–B6 (masas, no-fantasma, Schur, invariancia, simetría 71, lema) | todos 0/✓ |

## Advertencias de la casa

1. **"Nota 12"**: el número ya se usó y se revirtió el 2026-07-19 (incidente Familia F).
   El texto del anexo A queda acá adentro; si se promueve a `notas/`, renumerar **y
   aplicar la política de autoría de la casa (2026-07-21)**: la cabecera "Nicolás
   Irigoyen & fable" del handoff es registro de proceso de un acta externa — en la
   versión promovida el autor es Nicolás Irigoyen y la asistencia de IA se declara al
   pie, no en la línea de autoría.
2. **La errata de BCP (7.6)–(7.7): VERIFICADA 2026-07-21** — ver
   `VERIFICACION-BCP-2026-07-21.md` y `verificacion_independiente.py` (tarea 1 del
   handoff saldada en sustancia; sin xAct en la máquina, la independencia se logró por
   ruta exacta propia + panel adversarial de 3 agentes + los apéndices posteriores de
   los propios autores, que usan nuestros pesos). El contacto con Comelli/Pilo ya es
   defendible pero **requiere OK explícito de Nico**.
3. **El barrido de novedad de la fila U(X,Y) sigue siendo de la sesión externa** —
   antes de cualquier claim público aplica el estándar propio: barrido INSPIRE
   full-text (pendiente; el barrido del 21/7 cubrió solo la errata).
4. Estos scripts usan **sympy** (no numpy como el resto de la carpeta): `pip install sympy`.

Tareas abiertas por orden de valor: §6 del handoff — **1 y 2 SALDADAS**
(`VERIFICACION-BCP-2026-07-21.md`, `SECTOR-ESCALAR-2026-07-21.md`). OJO: la tarea 2
CORRIGE al handoff — al orden dominante el escalar está congelado (cero doble ω⁴=0,
coincide con Dubovsky ec. 99); el modo p⁴ requiere los NLO del medio y su coeficiente es
UV-sensible; nuestra ω²(p) exacta con mezcla gravitatoria es la primera escritura
explícita. Firma falsable propia hallada: m₁²≠0 ⟹ apantallamiento Yukawa del frame
dragging (LARES-2 la testearía) — PENDIENTE derivación prolija con fuente rotante.
**TAREA 3 TAMBIÉN SALDADA** (`ACOPLE-MATERIA-PPN-2026-07-21.md` + `acople/`): γ_PPN=1
exacta y Newton por teorema causal (la masa = gauge-fixing, verificado); el frame
dragging derivado prolijo tiene DOS RAMAS (relajada = Yukawa Meissner con
μ²=m₁²/(M_Pl²+α); retardada = RG exacto — reconcilia a Dubovsky) ⟹ predicción
condicional al estado del medio (caveat central declarado); cota corregida (𝒮=(1+x)e^(−x),
sin término lineal): Λ ≲ 2.0–2.6 MeV hoy, LARES-2 → 1.12 MeV; firma VIRGEN confirmada
(toda la literatura vive en la fase espejo m₁²=0; sin PPN α₁,α₂ publicados para ninguna
fase de Dubovsky). **TAREA 6 EN MARCHA (2026-07-21): el paper corto está escrito** —
`../PAPER-borrador-missing-row-UXY.md`, draft v0.1, standalone, con marcador honesto,
las erratas ajenas (BCP + Dubovsky), las dos ramas del frame dragging con su caveat de
selección de estado, y lista de bloqueo pre-publicación adentro (el TEXTO aún no tiene
auditoría adversarial propia; las 3 patas técnicas sí — estas actas). **El barrido
INSPIRE de novedad quedó hecho el mismo día** (método declarado en el paper): "unrestricted
internal diffeomorphisms" 0 hits full-text; la relación masa↔rigidez existe en OTROS
marcos (holografía sólida 1510.09089, crystal gravity 2109.11325 — citados como parientes)
pero el lema en el marco BCP/Dubovsky no aparece; frame dragging apantallado: nada
comparable (eco lejano: Tajmar–de Matos cond-mat/0602591, superconductores de laboratorio);
19 citas de Dubovsky 2024-2026 revisadas, ninguna construye el medio. Siguen: FRW (tarea 4),
mapeo nota 10 (tarea 5, la fase de ahí era m₀=0 ∧ m₂=0, no la misma), selección de estado
del medio (la pregunta nueva), y el envío del correo BCP (SOLO con OK de Nico; **direcciones
verificadas 2026-07-21 en fuente primaria**: comelli@fe.infn.it — INFN Ferrara, no Padova
como decía el borrador — y luigi.pilo@aquila.infn.it; el correo quedó listo-para-enviar).
**DATO NUEVO 2026-07-21: la medición del frame dragging que el paper esperaba YA SE PUBLICÓ**
— Ciufolini et al., Nature (julio 2026, doi:10.1038/s41586-026-10715-0): LARES-2+LAGEOS+GRACE,
acuerdo con RG al 0.2% reclamado (error budget disputado por Iorio, 2503.07264/Universe 9:211).
Si el 0.2% aguanta, la cota de la rama relajada ya es Λ<1.12 MeV hoy. Incorporado al paper
con ambos lados citados (refs [21]-[24]); leer el texto completo de Nature sigue en la
lista de bloqueo (solo abstract+prensa verificados).
**AUDITORÍA DEL TEXTO DEL PAPER — 1ª PASADA HECHA 2026-07-21** (1 agente adversarial,
~169k tokens): 31 hallazgos (3 altos: reproducibilidad rota, "eight" ecuaciones por 4+4,
novedad sin acta), TODOS aplicados el mismo día → paper v0.2. Actas nuevas:
`AUDITORIA-TEXTO-PAPER-2026-07-21.md` (informe completo + aplicación) y
`BARRIDO-INSPIRE-2026-07-21.md` (queries verbatim, hits, los 19 papers citantes).
Colateral valioso: la suite de `acople/` quedó REPARADA y corre entera desde el repo
(imports a `escalar/verificador/`, ruta absoluta relativizada, 2 bugs de runtime en
`v2_vector_fuente.py`; v1a 6s · v1b 4s · v1c 4s · v2 16s · v2b 4s · 01 8s ·
colA_causal ~2 min) y reproduce todos los chequeos citados en el paper. Pendiente
anotado: dirimir el chequeo C5d de `colA_causal.py` (residuo ∝ m₁²p⁴ρ_op², comentario
en el script + block list). Falta: 2ª pasada de auditoría sobre v0.2 antes de someter.
