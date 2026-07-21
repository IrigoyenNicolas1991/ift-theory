# Verificación independiente del diccionario de masas y de la errata de BCP (7.6)–(7.7)

**Campaña m₂=0 · tarea 1 del handoff · 2026-07-21 · Fable**

**Veredicto: el diccionario del handoff queda CONFIRMADO por cinco vías independientes,
y la discrepancia con las (7.6)–(7.7) impresas de Ballesteros–Comelli–Pilo
([1603.02956](https://arxiv.org/abs/1603.02956), PRD 94, 124023) queda establecida como
errata de imprenta no corregida y no señalada en la literatura (hasta donde llegó la
búsqueda, 2026-07-21).**

Nota de honestidad: la tarea pedía xAct/Mathematica o cadabra; ninguna está disponible
en esta máquina. La independencia se logró por otra vía (más fuerte al final): ruta
algebraica exacta propia + refutador desde cero + los papers posteriores de los propios
autores. Una corrida xAct sigue siendo deseable antes del contacto con los autores, pero
ya no es la pieza que sostiene el veredicto.

## La disputa

Pesos de las derivadas primeras U_τₙ y U_yₙ sobre el fondo Minkowski (a=N=1, M_Pl=1):

| | m₁²: U_τₙ | m₁²: U_yₙ | m₂²: U_τₙ |
|---|---|---|---|
| **Handoff (masas_medio.py)** | −2n (−2,−4,−6) | +2 plano, incl. n=0 | −2n(n+1) (−4,−12,−24) |
| **BCP impresas (7.6)–(7.7)** | −2 plano | +2n (0,+2,+4,+6) | −4(n+1) (−8,−12,−16) |

(m₀², m₃² y m₄² impresas — ecs. (7.5), (7.8), (7.9) — coinciden **exactamente** con el
diccionario en a=N=1: la discrepancia vive solo en (7.6)–(7.7), y las convenciones
coinciden ecuación por ecuación: B=C^{ab}, Z^{ab}=C^{0a}C^{0b} sin normalizar,
τₙ=Tr(Bⁿ), yₙ=Tr(BⁿZ), b=√det B, Y=u·∂Φ⁰=1/√(−g₀₀), patrón (7.3), g=η+h vía (7.14).)

## Las cinco vías (todas convergen en los pesos del handoff)

1. **CAL-4 del handoff** (heredada): ruta de Goldstone sin gauge unitario, resto = 0.
   Reproducida en esta máquina el 2026-07-21.

2. **`verificacion_independiente.py` (esta carpeta)**: inversa de métrica EXACTA (sin
   serie perturbativa a mano — justo donde viviría un error de pesos), configuraciones
   dirigidas de h, serie en ε recién al final, aritmética racional. Reproduce el
   diccionario completo (las 5 masas) término a término; control global con h genérica
   aleatoria (2 semillas, coeficientes U_k/U_kl simbólicos) cierra en 0.

3. **Refutador ciego** (agente sin acceso a nuestros archivos, prompt solo con las
   convenciones BCP y la disputa): rederivó desde cero por 4 métodos internos (inversa
   exacta, inversa perturbativa, isotropía, h general de 10 componentes) → −2n / +2
   plano / −2n(n+1). Veredicto: CONFIRMA_HANDOFF en los tres puntos disputados.
   Mecanismo aislado: con solo h₀₁, δτₙ = −n·h₀₁² (el n baja de la potencia) mientras
   δyₙ = Tr(Z) + O(h³) es EXACTAMENTE uniforme en n (Z ya es O(h²)) — el peso plano en
   yₙ no es un resultado de cálculo sino una imposibilidad estructural del peso impreso.
   Con solo h₁₂, los autovalores del bloque espacial dan λ₊ⁿ+λ₋ⁿ = 2+n(n+1)h₁₂².

4. **BCP se contradice a sí mismo** (hallazgo del auditor): la EOM de fondo estática
   (7.10b) da a³U − U_b = 2Σn·U_τₙ; con nuestro diccionario, m₂² on-shell =
   −2Σn²·U_τₙ — proporcional a la ec. (7.21) **del propio BCP** (M₂² = Σn²a^{−2(n−1)}U_τₙ,
   el coeficiente que usan de verdad en su Lagrangiano tensorial (7.22)). La (7.7)
   impresa daría on-shell pesos ∝(n+2), incompatible con su propia (7.21). El sector
   autoconsistente del paper coincide con nuestro diccionario.

5. **Los papers posteriores del propio grupo usan nuestros pesos** (bibliógrafo, fuentes
   LaTeX de arXiv descargadas y leídas):
   - [1704.00322](https://arxiv.org/abs/1704.00322) (Celoria–Comelli–Pilo, JCAP 09(2017)036),
     apéndice "Masses": M₁ con Σₙ₌₀³ U_yₙ **plano desde n=0**; M₂ = −2Σn²U_τₙ (**n²**);
     y su M₁^eff lleva −2Σn·a^{4−2n}U_τₙ — **exactamente nuestro peso** −2n.
   - [1712.04827](https://arxiv.org/abs/1712.04827) y [1907.11784](https://arxiv.org/abs/1907.11784):
     misma estructura (plano en yₙ desde n=0, n² en τₙ).
   - Ningún paper citante encontrado reimprime los pesos de las (7.6)–(7.7) impresas.
     Nadie señaló nunca la discrepancia (corrección silenciosa o rederivación aparte).

**Forense**: en el LaTeX de los autores (v1 y v2 idénticas en estas ecuaciones; la v2 es
la aceptada por PRD, el fuente se llama "PRD23Nov.tex"), la suma de yₙ en (7.6) corre
desde n=0 pero el peso impreso 2n aniquila ese término — el rango n=0..3 solo tiene
sentido con el peso plano, que es el nuestro. Forma probable de la errata: los factores
n y 2 intercambiados entre las dos sumas de (7.6), y −2n(n+1) → −4(n+1) en (7.7).
No existe erratum de PRD 94.124023 (INSPIRE récord 1426813, sin entrada); no hay v3.

## Caveats declarados (del auditor adversarial)

- La comparación se hizo en a=N=1 (Minkowski): no arbitra las potencias de a,N de las
  fórmulas FLRW (aunque chequean estructuralmente: a^{2−2n} en yₙ, a^{3−2n} en τₙ).
- El texto publicado en PRD no fue verificable directamente (paywall APS, HTTP 403);
  la identidad v2-arXiv = versión aceptada se infiere del nombre del fuente, del campo
  comments y de la política de copyedición de APS. Verificar el PDF de la revista si
  alguien tiene acceso institucional, antes del contacto.
- Todas las rutas usan SymPy como CAS de base (el refutador con implementación propia);
  una corrida xAct/cadabra en otra máquina sigue anotada como deseable, no bloqueante.

## Consecuencias

1. Para el resultado central de la campaña (U(X,Y) → fase protegida) la errata era
   irrelevante (U(X,Y) no depende de τₙ ni yₙ); lo que queda confirmado de paso es el
   **diccionario general** del handoff, incluido el lema de exclusión (m₁²=2K_T,
   m₂²=−2G_T), que sí usa esos pesos.
2. **El contacto con Comelli/Pilo ya es defendible** (tarea 1 saldada en sustancia).
   El correo diría: (7.6)–(7.7) parecen llevar errata de imprenta; evidencia: cálculo
   reproducible + la incompatibilidad interna con su (7.21) + sus propios apéndices
   posteriores. Tono humilde, pregunta, no acusación. **Requiere OK explícito de Nico**
   (política de la casa: nada público sin OK por pieza).
3. Pendientes que siguen vivos del handoff: barrido INSPIRE de novedad de la fila
   U(X,Y) (tarea de la sesión que corresponda), sector escalar completo (tarea 2),
   PPN (tarea 3), mapeo con la nota 10 (tarea 5).

*Panel adversarial: 3 agentes (refutador ciego, bibliógrafo, auditor de método),
~224k tokens, 2026-07-21. Ningún agente refutó; los tres aportaron evidencia nueva.*
