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
   El texto del anexo A queda acá adentro; si se promueve a `notas/`, renumerar.
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
Siguen: tarea 3 (PPN), frame dragging prolijo, barrido INSPIRE, tareas 4-5.
Relación con la nota 10 (la fase de ahí era m₀=0 ∧ m₂=0, no la misma): tarea 5, pendiente.
