# Selección de estado — vértices, canal NLO y números (columna A)

**Campaña m₂=0 · frente selección de estado · 2026-07-27 · columna A (3
relanzamientos por cortes externos; scripts sobrevivieron y el tramo final los
completó). Scripts en `colA/`: a1 (5 s) · a2 (193 s) · a3 (1.5 s) · a4 (0.8 s,
dos corridas estables). Todos corren en esta máquina.**

## Resultados

1. **a1 — teorema de B confirmado por ruta funcional independiente**: Y tiene
   forma polinomial cerrada vía el vector dual ε (Y = det(∂Φ)/√(−u_un·g·u_un));
   la identidad P_aᵘ∂_μΦᵇ = 0 es la invariancia GL⁺(3) FINITA manifiesta —
   off-shell, métrica exacta, todo orden (identidad algebraica). P_aⁱ = 0 con
   g exacta; linealización coincide con el acta de B; tres implementaciones de
   Y coinciden en racional exacto.
2. **a2 — vértice a vértice explícito**: los vértices cúbicos h²∂ᵢπ NO existen
   (36 componentes × 3 órdenes: todas cero); la corriente espacial con π
   encendido es advección pura esclava de P_a⁰ (la carga viaja CON el medio,
   nunca a través); los cúbicos existentes (∂₀π) renormalizan densidad;
   C = −m₁²S reproducido.
3. **a3 — el canal NLO**: la base correcta que puede transportar carga son los
   invariantes del FLUJO (θ, σ, ω, a; los K̄ del sector escalar no contienen Φᵃ);
   el término nuevo de corriente es derivada temporal total ⟹ CERO exacto
   sobre estacionarias y CERO exacto de fuga modal-lineal incluso en
   transitorios; la carga corregida C̃ se conserva con τ(t) arbitraria; el IVP
   deja siempre al medio en el co-rotante corregido. **Efecto nuevo: el
   co-rotante corregido no es RG exacto.**
4. **a4 — los números** (supuestos U1-U7 declarados en el script; c = ĉΛ²,
   m₁² = 4Λ⁴, A ≈ M̄_Pl²; todo lineal en ĉ UV-sensible):
   - **La corrección del co-rotante es una renormalización universal del
     acople gravitomagnético**: δ_ret ≈ −c_σ/A, independiente de p a orden
     dominante — sin resurrección del Yukawa. |δ| = ĉ(Λ/M̄_Pl)² =
     1.7×10⁻⁶¹ (Λ=10⁻³ eV) … 1.7×10⁻⁴³ (Λ=1 MeV). LARES-2 (2×10⁻³) queda a
     ≥40 órdenes: **la firma NO revive como efecto NLO** (revivirla exigiría
     ĉ ~ 10⁴⁰ ⟺ corte UV ~10¹⁷ GeV en un medio de corte ≤ MeV). El corrimiento
     NLO de la rama relajada es < 10⁻²¹: las dos ramas quedan nítidas.
   - **Fuga (no lineal)×(NLO)**: cadena dimensional declarada (v_drag =
     7.2×10⁻¹⁶ en superficie; forzante J₂₂ = 1.8×10⁻⁶ a 2Ω⊕; respuesta sin
     polos — teorema de B; rectificación por los cúbicos de a2):
     **Γ·t_edad ≤ 3.5×10⁻³⁵** (estructural) y ≤ 2.7×10⁻¹⁴ (cota
     deliberadamente rota, flujo oscilante contado como drenaje coherente).
     Ambas ≥14 órdenes bajo 1/t_edad: **el co-rotante no se vacía.**
   - **Spin-down terrestre**: canal Cherenkov importado (Ė ~ αM²v³, validado
     contra el número del Sol de 0507120: 24.3 W vs ~20 W), aplicado a la
     no-axisimetría rotante (proxy declarado): Ė ≤ 2.8×10⁻¹⁵ W a Λ=1 MeV vs
     margen libre ~3.6×10¹¹ W — **26 órdenes: sin cota nueva** (manda la
     nodal Λ ≲ 2.0–2.6 MeV). Consistente: este canal lleva energía, no carga.
5. **Patología ("muerte fea"): NO aparece** — H modal positivo en la validez
   EFT para cualquier signo O(1) de ĉ; sin taquiones ni raíces nuevas (la rama
   plana sobrevive como ω²=0, no ω²<0); los cúbicos no generan runaway; el
   fantasma de Ostrogradsky de c_a es espurio del truncamiento (reducción de
   orden estándar, documentado).

## Veredicto preliminar de la columna: D2 uniforme

Gana la CO-ROTANTE en toda la ventana Λ ∈ [10⁻³ eV, 1 MeV] — sin frontera (no
es D3) — **condicional al verificador adversarial del teorema de B**. La fase
predice RG en gravitomagnetismo hasta una parte en 10⁴³; la firma del
apantallamiento queda suprimida por superselección y no revive por NLO; lo que
se gana: predicción limpia por teorema + δ = −c_σ/A como estructura (linda,
inobservable).

## Blancos declarados para el verificador (lo más frágil, en orden)

1. La estimación de fuga es dimensional, no un cálculo de vértices (mitigante:
   14-35 órdenes de colchón).
2. Truncamiento a un solo modo p: ¿los NLO acoplan modos p→p′ (canal
   inter-modo que el juguete no ve)?
3. La reducción de orden de c_a (¿el fantasma era realmente espurio?).
4. Exhaustividad de la base NLO (θ,σ,ω,a) no demostrada formalmente (defensa:
   todo operador GL(3)-invariante sin derivadas superiores cae en el teorema
   de a1).
5. El diccionario Cherenkov traslacional→rotacional es proxy declarado.
6. σ = S − Ḟ como EL observable gauge-invariante (cualquier combinación da
   δ < 10⁻²¹: veredicto robusto, número exacto no).

*Acta escrita el mismo día. El veredicto de la campaña lo da el verificador
adversarial; estos números solo dicen que, si el teorema de B aguanta, no hay
puerta trasera.*
