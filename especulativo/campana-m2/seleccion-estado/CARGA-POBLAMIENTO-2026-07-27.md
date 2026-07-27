# Selección de estado — carga y poblamiento (columna B)

**Campaña m₂=0 · frente selección de estado · 2026-07-27 · columna B: 1 agente
(~175k tokens), scripts en `colB/` (t1-t4, corren en <2 s c/u, control B1 contra
la forma canónica verificada de `acople/verificador/`).**

## ⚠️ ESTADO: RESULTADO DE UNA COLUMNA, PENDIENTE DE VERIFICACIÓN ADVERSARIAL

Este hallazgo INVIERTE la expectativa de la apertura Y CORRIGE una frase del
acta ACOPLE ("cualquier disipación la decae a la relajada"). Por su peso, NO
entra al paper ni a ninguna sede hasta pasar el verificador independiente.

## El hallazgo central (dicho fuerte, como lo dijo la columna)

**La conservación cortocircuita la campaña — pero a favor de la CO-ROTANTE.**

1. **Teorema del congelamiento (exacto, no perturbativo)**: para √−g·U(X,Y)+EH,
   la invariancia interna GL(3) da la identidad off-shell P_aᵘ∂_μΦᵇ = 0 con
   P_aᵘ = ∂(√−g U)/∂(∂_μΦᵃ) ⟹ en gauge unitario **P_aⁱ = 0 idénticamente: la
   carga interna NO TIENE corriente espacial** ⟹ on-shell ∂_t P_a⁰ = 0 punto a
   punto, con gravedad no lineal completa. Fórmula cerrada:
   P_a⁰ = √−g·U_Y·g₀ₐ/(g₀₀√(−g₀₀)) = −m₁²h₀ₐ + O(h²).
2. **Las dos ramas viven en sectores de superselección distintos**: en el modo
   verificado, C = −m₁²S; C_co-rotante = 0 exacto (el medio co-rota: en SUS
   coordenadas no hay shift), C_relajada = m₁²τ_c/(Ap²+m₁²) ≠ 0 modo a modo
   (distribución dipolar, carga neta 0). Pasar de una a otra exige transportar
   carga entre puntos — **y la corriente que lo haría no existe**. Prohibido a
   orden dominante.
3. **El IVP adiabático es universal**: S = 0, F = ∫τ/(Ap²) es solución EXACTA
   para τ(t) arbitraria (identidad, ni siquiera límite adiabático); el modo
   plano es holonómico de primer orden (cero frecuencias propias): el estado
   queda etiquetado solo por la carga. RK4 con 4 historias × T ∈ {1…10⁶}:
   S_final ~ 10⁻¹³ contra S_relajada = −0.909. **El encendido de la fuente —
   rápido, lento, no monótono — deja SIEMPRE al medio en la co-rotante.**
4. **Condiciones iniciales cosmológicas**: sobre FRW, P_a⁰ ∝ g₀ₐ = 0 exacto en
   toda época; carga primordial diluye a⁻³ (consistente con el acta FRW). El
   universo llega con carga cero en todas partes — el sector del co-rotante.
5. **Reinterpretación energética**: E_ret > E_fund (verificado en v2b) compara
   estados de SECTORES DISTINTOS. Dentro del sector C = 0 (el poblado), el
   co-rotante es el único estado estacionario — **su fundamental**. "Liberar la
   energía extra" exige cambiar C: sin canal.
6. **Robustez verificada por la columna**: gauge residual (no artefacto),
   Ostrogradsky/bordes (Q_raw − Q_can = 0 como expresión), Tierra no
   axisimétrica (τ(1+ε sin Ωt): S = 0 exacto simbólico, sin resonancia posible
   — la transferencia no tiene polos; RK4 200 vueltas: max|S| ~ 3×10⁻¹¹).

## Los escapes que el teorema DEJA VIVOS (declarados por la columna)

- **Vórtices/phase slips de Φᵃ** (Φ no suave): evaden el teorema; tasa ~e^(−S)
  — y la columna C ya estableció que esas barreras DIVERGEN a v→0 (E_b ∝ 1/v).
- **NLO con derivadas superiores**: agregan a la corriente el término
  ∂L/∂(∂∂Φ)·∂ξ que SÍ permite flujo de carga — suprimido por Λ; cuantificarlo
  es de la columna A / verificador.
- Estados "relajada + nube compensante" no excluidos por carga — pero no son
  la rama Yukawa limpia ni resultan de ningún decaimiento suave.

## Implicación si sobrevive al verificador (D2 de la apertura)

La fase predice **RG exacto en gravitomagnetismo** — la firma del frame
dragging apantallado queda SUPRIMIDA por teorema de superselección, y el paper
lo declara con la misma prominencia con que declaró la firma (regla de la
casa). A cambio, el resultado teórico es más limpio que el que perdemos: el
medio es indistinguible de Einstein en TODO el régimen medido *como
predicción*, no como ajuste — y el teorema del congelamiento (carga sin
corriente) es una estructura nueva y publicable por derecho propio.
Consistencia con la columna C: el único canal sin umbral (Cherenkov escalar)
lleva energía pero no carga — y su tasa importada ya era despreciable.

## Blancos para el verificador adversarial (prioridad máxima)

1. La identidad P_aᵘ∂_μΦᵇ = 0 y su corolario P_aⁱ = 0 (¿la parte EH de la
   corriente de Noether está bien tratada? ¿el vínculo de Einstein 0i se usó
   legítimamente para C = −m₁²S?).
2. La universalidad del IVP (¿el modo de juguete de un solo modo transversal
   captura el sistema completo? ¿qué pasa con la retroacción de la métrica?).
3. La evaluación de carga en las dos ramas fuera del régimen lineal.
4. La reinterpretación de E_ret > E_fund como comparación entre sectores.

*Acta escrita el mismo día del cálculo. El teorema es de la columna B y queda
en cuarentena adversarial hasta el veredicto del verificador.*
