# The missing row: unrestricted internal diffeomorphisms, the protected phase of Lorentz-violating massive gravity, and a screened frame-dragging signature

**Nicolás Irigoyen**

*Draft v0.1 — 2026-07-21. First written form of the results of the m₂ = 0 campaign
(2026-07-20/21; campaign records and full verification chain in
`especulativo/campana-m2/`: `HANDOFF-campana-m2-2026-07-20.md`,
`VERIFICACION-BCP-2026-07-21.md`, `SECTOR-ESCALAR-2026-07-21.md`,
`ACOPLE-MATERIA-PPN-2026-07-21.md`). Internal working paper of the speculative stage
of the Intangible Field Theory (TCI) program, written to stand alone: nothing below
depends on any other claim of that program. **Not submitted anywhere.** The three
technical legs each passed an independent adversarial verification pass (blind
refuters and independent re-derivation pipelines; none refuted); **this text itself
has not yet passed the in-house audit** — see the pre-publication block list at the
end. Honesty rules of the house apply: every assumption declared, every "exactly"
backed by a reproducible computation, negative results stated with the same
prominence as positive ones.*

---

## Honest scoreboard

Every row says whose each piece is.

| Piece | Status | Whose |
|---|---|---|
| The phase m₂² = m₃² = m₄² = 0 of Lorentz-violating massive gravity exists, is UV-insensitive, and is healthy if m₀²m₁² > 0 | Known since 2004 | Dubovsky [1], eqs. (71)–(75) |
| The medium → graviton-mass dictionary (unitary gauge, self-gravitating media) | Known since 2016 | Ballesteros–Comelli–Pilo (BCP) [4] |
| The operator X + Y² and the isentropic class U(X + Y²) | Known since 2017 (thermodynamic route, no connection to the protected phase) | Celoria–Comelli–Pilo (CCP) [5] |
| Scalar-sector phenomenology of ω² ∝ p⁴ media (Jeans time, r_c, t_c, bounds) | Known since 2003–2005 | ghost condensate, ACLM [8, 9] |
| **The missing row of BCP's Table 2: Φᵃ → Ψᵃ(Φᵇ) unrestricted ⟹ U(X,Y)** | **New (to the searches declared below)** | this paper |
| **U(X,Y) lands exactly on the protected phase: m₂ = m₃ = m₄ = 0 emerge from the vacuum conditions, no tuning, explicit ghost-free corner** | **New, machine-verified** | this paper |
| **Exclusion lemma: on-shell m₁² = 2K_T, m₂² = −2G_T — protecting the graviton mass ⟺ switching off the medium's shear phonons (at leading order)** | **New in this framework** (the mass ↔ rigidity link is known in other settings [17, 18]) | this paper |
| **The exact scalar dispersion ω²(p) of this phase with gravitational mixing** (Dubovsky's leading-order freeze-out made quantitative; the p⁴ coefficient is NLO and UV-sensitive) | **New (first explicit form)** | this paper |
| **Causal theorem: with conserved sources the leading-order solution is exactly GR; γ_PPN = 1 exact; the mass only selects the gauge** | **New for this phase** (mechanism anticipated qualitatively by Dubovsky's "gauge-fixing" remark [1]) | this paper |
| **Frame dragging has two branches: relaxed medium ⟹ Yukawa-screened (gravitomagnetic Meissner); co-rotating medium ⟹ exact GR. Screened Lense–Thirring as the falsifiable signature; the July-2026 LARES-2 measurement (claimed 0.2% [23]) gives Λ < 1.12 MeV on the relaxed branch if its error budget holds** | **New; no prior computation of rotating sources in any m₁² ≠ 0 phase found** | this paper |
| Probable misprint in BCP eqs. (7.6)–(7.7); two misprints in Dubovsky eqs. (73), (99) | Found and cross-checked five independent ways (BCP case) | this paper (to be confirmed with the authors) |
| The Einstein–Hilbert kinetic term | **Assumed, not derived** (as in [1, 4, 5]; Weinberg–Witten out of scope) | — |

No death criterion of the campaign was triggered. The price of the result — the
exclusion lemma — and the conditionality of the signature — the state-selection
caveat — are stated with the same prominence as the wins.

---

## Abstract

In 2004 Dubovsky classified the phases of Lorentz-violating massive gravity and
found one where the helicity-±2 graviton is **exactly massless, protected by the
residual symmetry xⁱ → xⁱ + ξⁱ(x⃗)**, UV-insensitive, and ghost-free when
m₀²m₁² > 0 — and closed with the remark that his analysis "does not exhaust all
possible subgroups of the diffeomorphism group." The medium realizing that phase
was never constructed. Ballesteros–Comelli–Pilo (BCP) later built the general
dictionary from self-gravitating media (four Stückelberg scalars Φ^A) to the five
graviton mass parameters, classifying media by their internal symmetry — solids,
fluids, superfluids, supersolids — all protected by *volume-preserving* internal
diffeomorphisms. We point out that their Table 2 has a missing row: media invariant
under **unrestricted** internal spatial diffeomorphisms, Φᵃ → Ψᵃ(Φᵇ) with no
condition on the determinant. Exactly two invariants survive at leading order,
X = C⁰⁰ and the counterflow Y = u·∂Φ⁰, and the resulting medium U(X,Y) lands
exactly on the protected phase: the flat-space tadpole conditions force
m₂² = m₃² = m₄² = 0 identically, with m₁² = 2U_X ≠ 0 and an explicit ghost-free
corner. The identification comes with a structural lemma: on-shell, m₁² = 2K_T and
m₂² = −2G_T, where K_T and G_T are the inertia and the rigidity of the medium's
transverse (shear) sector — **the graviton mass is the shear rigidity of the
medium**, so protecting the massless graviton is equivalent to switching off shear
phonons at leading order: the medium must be a fluid. We then compute what this
phase does in the lab. The scalar sector is frozen at leading order (a double zero,
matching Dubovsky's eq. 99); the famous ω² ∝ p⁴ turns on only through
next-to-leading-order operators, with a UV-sensitive coefficient, and with
gravitational mixing the infrared is a slow Jeans instability — in that sector the
medium is exactly a ghost condensate (dictionary M⁴ = 2m₀², κ = −M̄²/2), because
m₁² cancels there. The distinctive signature lives where m₁² does not cancel: with
conserved sources the static and orbital predictions are exactly GR (γ_PPN = 1
exact, by a causal theorem: the mass term only selects the synchronous gauge and
costs zero action on-shell), but **frame dragging is modified**. The vector sector
has two branches: if the medium relaxes to its ground state, the gravitomagnetic
potential obeys (∇² − μ²)Sᵢ = 16πG̃τᵢ — a gravitomagnetic Meissner effect,
Lense–Thirring precession screened by (1 + μa)e^(−μa) with μ = 2Λ²/M̄_Pl; if the
medium co-rotates (a persistent-current state), the prediction is exactly GR. Which
branch nature picks is a genuine open problem of the phase (it exceeds quadratic
order), and we state it as such. Claimed LAGEOS/LARES accuracy (2–5%, error
budget contested) gives Λ ≲ 2.0–2.6 MeV; **the LARES-2 measurement published in
July 2026 — as this draft was being written — reports agreement with GR at its
0.2% design accuracy, which, if its contested error budget holds, already pushes
the relaxed-branch bound to Λ < 1.12 MeV, i.e. screening lengths beyond 30 R⊕**.
To our searches (declared below), no computation of rotating sources exists in
any m₁² ≠ 0 phase: the signature is untested territory. As by-products, we report a probable misprint in
the mass-parameter weights of BCP eqs. (7.6)–(7.7), established five independent
ways, and two minor misprints in Dubovsky's eqs. (73) and (99). All results are
symbolic (SymPy), run in seconds, and are public.

---

## 1. Introduction

Massive gravity with broken Lorentz invariance is less constrained than its
Lorentz-invariant cousin: with separate mass parameters m₀…m₄ for the different
components of h_μν (in the notation of [1, 3]), the Boulware–Deser ghost can be
evaded (m₀ = 0), the vDVZ discontinuity is absent, and — the case of interest
here — there exists a phase where the spin-2 graviton is **exactly massless while
the medium that breaks Lorentz invariance is still there**. Dubovsky exhibited it
in 2004 [1]: if the vacuum preserves the residual symmetry

    xⁱ → xⁱ + ξⁱ(x⃗)        (Dubovsky eq. 71)

then m₂² = m₃² = m₄² = 0 (his eq. 72) — and, unlike generic mass patterns, this
one is stable under radiative corrections, because any counterterm must respect
the residual symmetry (UV-insensitivity). The phase propagates the two GR tensor
polarizations at the full speed of light, plus a vector sector gapped by m₁² and a
scalar sector we discuss at length below. Its health condition is m₀²m₁² > 0 (his
eq. 75). The empirical stakes of *exact* protection are set by the observational
bound on the graviton mass, m_g ≤ 1.27×10⁻²³ eV [20]: a symmetry-protected zero
satisfies it structurally, where any tuned small mass merely survives it.
Twenty-two years of literature cite the phase; to our knowledge, and to
the searches declared at the end, **nobody ever constructed the physical medium
that realizes it**. Dubovsky's own closing line is an open invitation:

> "Clearly, our analysis does not exhaust all possible subgroups of the
> diffeomorphism group. It is worth studying whether other interesting
> possibilities exist." [1]

The natural framework for the question is the self-gravitating-media program of
Ballesteros, Comelli and Pilo (BCP) [4]: four derivatively-coupled scalars Φ⁰, Φᵃ
(the medium's clock and comoving coordinates), a leading-order Lagrangian U built
from the invariants of C^{AB} = g^{μν}∂_μΦ^A∂_νΦ^B, and a dictionary from U to the
five mass parameters in unitary gauge. Their Table 2 classifies media by internal
symmetry: solids U(τₙ), perfect fluids U(b,Y), superfluids U(X,Y,b), supersolids —
every row protected by internal diffeomorphisms that **preserve the volume
element**, det(∂Ψ/∂Φ) = 1.

This paper adds the row that the table is missing — the medium invariant under
internal spatial diffeomorphisms with **no restriction at all** — and shows that
it is precisely the object Dubovsky's invitation asked for. We then push the phase
through its first phenomenology with matter: the result is a theory that imitates
GR by theorem exactly where GR is well measured, and deviates in exactly one
place — the gravitomagnetic sector — where, as far as we could find, nobody has
ever computed anything in any phase of this class.

Everything below is machine-verified symbolic algebra (SymPy; exact rational
arithmetic; no truncations except the declared perturbative orders), reproducible
in seconds from the public scripts (§ Reproducibility). The three technical
blocks (dictionary + misprint; scalar sector; matter coupling) were each
re-derived from scratch by an independent adversarial pipeline that shared no
code with the original derivation, plus blind refutation attempts; none refuted.

## 2. Conventions, the calibrated dictionary, and a misprint in BCP

We work throughout in BCP's conventions [4]: signature (−,+,+,+), unitary gauge
Φ⁰ = t, Φᵃ = xᵃ, M_Pl = 1 unless restored, flat background g = η + h. The medium
invariants are X = C⁰⁰ (background −1), V^a = C^{0a}, the spatial block B^{ab}
(background δ^{ab}), Z^{ab} = V^aV^b, τₙ = Tr(Bⁿ), yₙ = Tr(BⁿZ), b = √det B, and
Y = u·∂Φ⁰ = 1/√(−g₀₀) with u^μ the unit vector normal to constant-Φ⁰ slices. The
mass pattern is BCP's (7.3):

    √−g U ⊃ t^{μν}h_{μν} + ¼[ m₀²h₀₀² + 2m₁²h₀ᵢh₀ᵢ − 2m₄²h₀₀hᵢᵢ + m₃²hᵢᵢ² − m₂²hᵢⱼhᵢⱼ ]

We built the complete dictionary U(X, V, B, b, τₙ, yₙ, Y) → (m₀²,…,m₄²) by direct
second-order expansion (`masas_medio.py`) and calibrated it five independent ways:
(i) all rotational-isotropy identities close; (ii) our m₀² reproduces BCP's (7.5)
**exactly**; (iii) imposing the symmetry Φᵃ → Φᵃ + fᵃ(Φ⁰) reproduces Dubovsky's
m₁ = 0 phase (his eq. 64); (iv) the gold calibration: the phonon Lagrangian
derived by the Goldstone route (flat space, no unitary gauge — a computationally
disjoint path) equals the mass Lagrangian under h_μν → ∂_μπ_ν + ∂_νπ_μ term by
term, with **zero remainder** modulo total derivatives once tadpoles are imposed;
(v) the transverse sector reproduces L_T = ½[m₁²(∂₀π^T)² − m₂²(∂ᵢπ^T)²].

**The misprint.** Our dictionary disagrees with the *printed* BCP eqs.
(7.6)–(7.7) in the weights of U_τₙ and U_yₙ (flat background, a = N = 1):

| | m₁²: U_τₙ weight | m₁²: U_yₙ weight | m₂²: U_τₙ weight |
|---|---|---|---|
| this work | −2n (−2, −4, −6) | +2 flat, including n = 0 | −2n(n+1) (−4, −12, −24) |
| BCP printed | −2 flat | +2n (0, +2, +4, +6) | −4(n+1) (−8, −12, −16) |

Five independent lines of evidence select our weights: (1) the gold calibration
above; (2) an exact-inverse-metric rederivation on directed configurations with
the ε-series taken only at the end (`verificacion_independiente.py`); (3) a blind
refutation attempt (an agent given only BCP's conventions and the dispute, no
access to our files) that rederived the weights four ways and confirmed them —
including the structural observation that δyₙ is *exactly* uniform in n at O(h²)
(Z is already O(h²)), so the printed weight 2n·U_yₙ would annihilate the n = 0
term that BCP's printed sum explicitly includes; (4) internal consistency of BCP
itself: their tensor-sector eq. (7.21), M₂² = Σn²U_τₙ, is compatible with our
weights and not with their printed (7.7); (5) the appendices of the later papers
of the same group [5, 6, 7] use precisely our weights (flat in yₙ from n = 0, n²
in τₙ). No erratum of PRD 94, 124023 exists; the equations are unchanged between
arXiv v1 and v2. We treat this as a probable typographical error, to be confirmed
with the authors before any public claim harder than this paragraph (a draft
query letter exists in the campaign records). Caveats: the comparison was made at
a = N = 1; the journal PDF itself was not accessible to us (paywall).

For the central result of this paper the issue is moot — U(X,Y) depends on
neither τₙ nor yₙ — but the exclusion lemma of §5 does use those weights, so the
verification chain above is part of this paper's evidence base.

**Two minor misprints in Dubovsky [1]** (found while cross-checking our scalar
sector against his; neither affects his conclusions): in eq. (73), dimensional
analysis requires Λ² where Λ⁴ is printed (and an "= 0" is omitted); in eq. (99),
rederiving from his own (86)–(88) gives −6(∂₀τ)² where +6(∂₀τ)² is printed
(verified symbolically). Also for precision: the Einstein–Hilbert normalization
of his section 5 is twice the canonical one, which rescales absolute mass
conversions but no dimensionless condition.

## 3. The missing row: unrestricted internal diffeomorphisms and U(X,Y)

BCP's Table 2 asks of each medium: under which internal transformations of the
comoving labels Φᵃ is U invariant? Every row of the published table imposes
volume preservation. Drop it:

    Φᵃ → Ψᵃ(Φᵇ) ,   det(∂Ψ/∂Φ) unrestricted.

A medium with this symmetry does not feel *any* deformation of its spatial
labels: no shear, no compression, no dilation. At leading order in derivatives
exactly two invariants survive:

- **X = C⁰⁰** — the clock gradient squared (manifestly free of Φᵃ);
- **Y = u·∂Φ⁰** — with u^μ the unique direction invariantly defined by the flow
  lines (u·∂Φᵃ = 0, normalized). Y measures the **counterflow** between the clock
  condensate and the material flow lines.

Both invariances were verified *non-linearly* (random metric, generic quadratic
internal diffeomorphism: ΔX = ΔY = 0 identically). A Schur identity gives the
pair physical flesh (verified):

    V · B⁻¹ · V = X + Y² .

So U(X,Y) is a two-component object — a clock condensate plus flow lines — whose
only memory of ever having had a lattice is the flow direction: *a superfluid
that forgot its lattice*. CCP [5] found the one-variable subclass U(X + Y²) in
2017 as the isentropic thermodynamic class — without noting the unrestricted
symmetry, and without the connection that is the point of this paper. What
U(X,Y) is **not**: it is not the ghost condensate P(X) — flat-space tadpoles
force U_X = 0 on P(X) (hence its m₁² = 0), while U(X,Y) sustains U_X ≠ 0 because
the counterflow compensates the tadpole (U_Y = 2U_X, next section); and it is not
BCP's superfluid U(X,Y,b) — any dependence on b regenerates m₃² = U_bb/2 ≠ 0 and
m₄² ≠ 0. U(X,Y) is the exact point where the medium stops feeling its own volume.

## 4. The protected phase emerges from the vacuum conditions

Feeding U(X,Y) to the calibrated dictionary (`parteB_medioXY.py`):

**Off-shell:**

    m₀² = −U₀/2 − 2U_X + 2U_XX − 2U_XY + U_Y/2 + U_YY/2
    m₁² = U₀ + 2U_X
    m₂² = U₀
    m₃² = U₀/2
    m₄² = U₀/2 + U_X − U_Y/2

**Flat-vacuum (tadpole) conditions:** t₀₀ = −U₀/2 − U_X + U_Y/2 = 0 and
t₁₁ = U₀/2 = 0, i.e. U₀ = 0 and U_Y = 2U_X. Then, **with nothing further
imposed**:

    m₂² = 0 ,  m₃² = 0 ,  m₄² = 0      (identically)
    m₁² = 2U_X
    m₀² = −U_X + 2U_XX − 2U_XY + U_YY/2

This is exactly Dubovsky's phase (72), and no accident: the residual symmetry
(71), xⁱ → xⁱ + ξⁱ(x⃗), *is* Φᵃ → Ψᵃ(Φᵇ) read in unitary gauge. We verified
directly that the resulting mass Lagrangian is invariant under
δh_ij = ∂ᵢξⱼ + ∂ⱼξᵢ with time-independent ξ: the masslessness is
symmetry-protected, and any quantum counterterm respecting the symmetry is again
of the form U(X,Y), whose vacuum masses vanish again — Dubovsky's
UV-insensitivity, now with an explicit medium carrying it.

**The ghost-free corner is explicit.** Taking

    U = (X+1) + 2(Y−1) + ½(X+1)²

(U(vac) = 0, U_X = 1, U_Y = 2U_X, U_XX = 1), the dictionary gives

    (m₀², m₁², m₂², m₃², m₄²) = (1, 2, 0, 0, 0) ,   m₀²m₁² = 2 > 0  ✓

satisfying Dubovsky's health condition (75). The vector sector has the healthy
gapped dispersion of his eq. (73) whenever m₁² = 2U_X ≠ 0. The scalar sector is
§6. Death criterion 1 of the campaign (m₂² ≠ 0, or no ghost-free corner) was not
triggered.

## 5. The exclusion lemma: the graviton mass is the medium's shear rigidity

The identification comes with a price tag, and the price is itself a result.
From the transverse sector of the **general** medium (not just U(X,Y)), on-shell:

    m₁² = 2·K_T ,   m₂² = −2·G_T ,   v_T² = m₂²/m₁²

with K_T = U_X + Σₙ U_yₙ the inertia of the medium's shear sector and
G_T = Σₙ n²·U_τₙ its **shear rigidity** (the gradient coefficient of the
transverse phonon Lagrangian). Verified symbolically for the general U.

**Lemma.** At leading order, the medium's shear phonons propagate iff
m₁²m₂² ≠ 0. Hence *either* UV-insensitive phase of Dubovsky switches them off:
the m₁ = 0 phase freezes them (no inertia); the m₂ = m₃ = m₄ = 0 phase leaves
them rigidity-less (v_T = 0 — pure gauge of the residual symmetry (71)).

**Moral.** The spin-2 graviton mass *is* the shear rigidity of the medium, with
sign and factor: m₂² = −2G_T. A medium with dynamical tensor order at leading
order — a solid, a supersolid, anything that creaks when sheared — endows the
graviton with mass and loses the protection. Conversely, a medium that protects
the massless graviton cannot contribute propagating spin-2 of its own at low
energies: **protection and dynamical tensor order are mutually exclusive at
leading order.** This is why solid inflation [16] generically has m₂ ≠ 0
(tensor-mode masses from shear rigidity are a *feature* there), and it sharpens,
from the gravity side, an intuition long present in other communities: in
holographic massive gravity the bulk graviton mass maps to boundary elasticity
[17], and in "crystal gravity" [18] solids and gravity are intertwined precisely
through shear. What we add is the statement *inside* the BCP/Dubovsky framework,
as an exact on-shell identity, with the iff, and with the consequence for
protection.

Declared escapes (they define, not embarrass, the program): higher-derivative
kinetic structures (spin-nematic Goldstone routes à la Chojnacki [15], with
non-relativistic dispersion), and induced gravity à la Sakharov — which is
exactly debt 3 of this paper (the EH term is assumed throughout, here as in
[1, 4, 5]). Death criterion 2 did not trigger as a no-go: it became this lemma.

## 6. The scalar sector is frozen at leading order

Here this paper corrects its own campaign's earlier internal note, which had
paraphrased Dubovsky as "one scalar mode with ω² ∝ p⁴". The precise statement,
now machine-verified with gravitational mixing included (independent adversarial
re-derivation from √−g R; no refutation):

1. **At strict leading order (U(X,Y) + quadratic EH), the scalar sector does not
   propagate.** The determinant of the scalar block is

       det ∝ −(M_Pl⁴ m₀² m₁²/2) · ω⁴ p⁶

   — a **double zero** at ω² = 0 for every p. This matches Dubovsky's eq. (99)
   verbatim ("mixing with gravity does not introduce new propagating modes").

2. **The famous ω² ∝ p⁴ requires the medium's NLO operators** (the
   higher-derivative invariants compatible with the residual symmetry ξⁱ(x⃗):
   K̄ᵢⱼK̄ᵢⱼ, (tr K̄)², …). With them, exactly one scalar mode turns on, and its p⁴
   coefficient is **UV-sensitive**: c₄ ≈ −(α+β)/m₀², where α, β are NLO couplings
   — it is *not* expressible in the masses alone. Dubovsky left the coefficient
   generic (verified against his source); the exact dispersion below is, to our
   knowledge, its first explicit form for this medium. The second root stays
   ω² = 0 exactly at all orders computed — the surviving gauge zero after the
   double zero splits.

3. **With gravity, the deep infrared is not p⁴ but a Jeans p²:** with κ ≡ α+β
   and M_Pl = 1,

       ω²(p) = p²·[κ(2p² − m₀²) + p²m₀²(ρ²/2 − 2κσ)] / [m₀²(−2 − α + 3β + α² + 3αβ)]

   whose EFT limit (|α|,|β| ≪ 1) is ω² ≈ (κ/2)p² − [κ/m₀² + (ρ²−4σκ)/4]p⁴ and
   whose decoupling limit M_Pl → ∞ recovers the pure p⁴ form. The no-ghost
   conditions, disaggregated (refining m₀²m₁² > 0): **κ < 0** (ghost-condensate
   sign of the NLO), **m₀² > 0** (no gradient instability at p⁴), **m₁² > 0**
   (healthy vector). In the explicit corner (m₀², m₁²) = (1, 2) with β = −ε:
   kinetic coefficient K = 3 + 2/ε > 0 and ω² = εp²(2p² − 1)/(2 + 3ε) — a soft
   Jeans below p² = ½, stable above.

4. **In this sector the medium is *indistinguishable* from the ghost
   condensate.** The dictionary is exact and arithmetic (residue 0 by two
   routes): M⁴ = 2m₀², κ = −M̄²/2 in ACLM's notation [8]. The structural reason:
   **m₁² cancels exactly in the scalar dispersion and in the scalar kinetic
   term** — it lives only in the vector sector. All of ACLM's phenomenology
   therefore imports wholesale: the Jeans instability is harmless (τ ≈ 18–21
   Hubble ages at Λ = 10 MeV, ∝ Λ⁻³; Hubble friction erases it below
   Λ ≈ 30 MeV; above, nonlinearities saturate it in percent-level lumps),
   and the viability window for U = Λ⁴Û runs from Λ ~ 10⁻³ eV (where the medium
   would *be* the dark energy) up to Λ ≲ 10 MeV conservatively, ~100 GeV if
   percent-level lumping is accepted [9]. The hierarchy Λ ≪ M_Pl is declared,
   not explained — the standard ghost-condensate tuning, inherited, not cured.

The remaining sectors with gravity, verified: the vector does not propagate at
LO (det = (m₁²/4)·ω²p²(M_Pl² + α)); the tensor is massless **exactly**, with
c_T² = M_Pl²/(M_Pl² + α) — luminal at α = 0, untouched by everything above. Mode
counting: 2 (LO), 2+1 (NLO), matching Dubovsky.

The one thing the ghost condensate is *forbidden* to have — by its own residual
symmetry, verified textually — is m₁² ≠ 0. That is where the medium signs its
name, and it is the subject of the next two sections.

## 7. Matter coupling: Einstein by theorem, not by tuning

Couple a conserved source T_μν minimally to g_μν (the medium couples only
gravitationally; no direct Φ–matter coupling — declared assumption). One expects
a massive theory to deform Newton. It does not, and the reason is structural:

**Causal theorem (verified to residues [0,0,0,0] in the eight field equations).**
For any conserved source switched on at a finite time, the leading-order solution
of the massive system is **exactly** the solution of pure GR; the mass term
selects the synchronous gauge of that solution and costs zero action on-shell
(L_mass = 0 identically on the causal branch). Consequently γ_PPN = 1 **exactly**
(not approximately) in all principal regimes, Newton's constant is the bare one
(no renormalization), and the static potential of an eternal source — the
oscillating cos(μ_s r)/r family, μ_s² = m₀²/(2M_Pl²), *not* Yukawa — is a fixed
point that a causal history approaches only on times t_c ~ 18 Hubble ages: it is
unreachable, exactly as in the ghost condensate [8], with which the dictionary is
again arithmetic (μ_s² = m²_ACLM). At NLO the static PPN correction is

    γ(p) = 1 − 2σp²/M_Pl² + p⁴[ρ_op²/(M_Pl² m₁²) + 4σ²/M_Pl⁴] + O(p⁶)

— scale-dependent, outside the constant-γ PPN book-keeping, and utterly
unobservable at solar-system scales for the allowed Λ. Dubovsky's remark that in
this phase the mass "has the form of a gauge fixing" [1] is the qualitative shadow
of this theorem; the theorem makes it exact and extends it to the full causal
initial-value problem (closed-form: ΔΨ(t,p) = A(p)[1 − cos Ω(p)t], with
cos → cosh in the Jeans band).

Everywhere Einstein is well measured, then, this phase *is* Einstein — by
theorem, not by calibration. A theory that hides this well needs to be caught
somewhere else.

## 8. Frame dragging: two branches, one untested signature

The place it cannot hide is the sector where m₁² lives: gravitomagnetism. Here
the campaign found structure that, as far as our searches reach, nobody had
noticed in any phase of this class.

**The two branches.** The same residual symmetry ξⁱ(x⃗) that protects m₂ = 0
gives the vector sector an exact conservation law, which leaves a flat direction
in the space of stationary vector states. The physical consequences bifurcate:

- **Relaxed branch (medium in its ground state).** The gravitomagnetic potential
  obeys a **derived** massive equation,

      (∇² − μ²) Sᵢ = 16πG̃ τᵢ ,   μ² = m₁²/(M_Pl² + α) ,   G̃ = G·M_Pl²/(M_Pl² + α)

  — a gravitomagnetic Meissner effect: the medium expels frame dragging beyond
  the screening length ℓ₁ = 1/μ. For a rigidly rotating sphere of radius R
  (exterior, exact):

      h₀ᵢ = 2G̃ (x⃗×J⃗)ᵢ (1 + μr) e^(−μr) / r³ · 𝔉(μR) ,
      𝔉(y) = 15[(y² + 3)sinh y − 3y cosh y]/y⁵ ,

  with the μ → 0 limit reproducing linearized Kerr exactly. Nodal precession of
  a satellite at semi-major axis a is suppressed by 𝒮 = (1 + x)e^(−x), x = μa —
  note **no linear term** (the Yukawa dipole cancels it); the gyroscope (GP-B)
  factor is (1 + x − x²)e^(−x). Ω⃗_nodo ∥ J⃗ holds for arbitrary inclination.

- **Co-rotating branch (medium recently stirred, no dissipation).** The exact
  solution is **GR in disguise**: the medium co-rotates with the frames and the
  screening is invisible. This branch is a genuinely excited state (higher
  Hamiltonian, verified, robust to boundary terms), and any dissipation relaxes
  it toward the screened branch — but a superfluid medium could in principle
  sustain it as a persistent current.

**The caveat that is also the discovery.** Which branch describes the Earth is
**not decidable at quadratic order**: it depends on the relaxation history of the
medium around the source (nonlinear dissipation, vortices, formation history).
We therefore state the screening as a *conditional* prediction — conditional on
the medium relaxing — and we promote the condition itself to the open problem of
the phase: massive-gravity phases with m₁² ≠ 0 have a two-state structure in
their gravitomagnetic response that the literature has not noticed. Dubovsky's
gauge-fixing remark describes our co-rotating branch; the relaxed branch is new.

**Numbers.** Restoring units, μ = 2Λ²/M̄_Pl, i.e.

    ℓ₁ = 2.40×10⁸ m · (MeV/Λ)²   — at Λ = 1 MeV, roughly the Earth–Moon distance.

Lense–Thirring measurements with LAGEOS/LARES (claimed accuracy 2–5% [21]; the
error budget is contested in the literature [22]) give **Λ ≲ 2.0–2.6 MeV** on
the relaxed branch. **In July 2026 — while this draft was being written — the
LARES-2 team published the measurement this test was waiting for** [23]:
combining LARES-2 (in orbit since 2022) with LAGEOS and GRACE data, they report
agreement with GR at their design accuracy of 0.2%. Taken at face value this
already pushes the relaxed-branch bound to **Λ < 1.12 MeV**, i.e. ℓ₁ > 30 R⊕ —
well inside the window where the medium is otherwise viable (§6); at Λ = 1 MeV
the predicted nodal deviation is 0.13%. Honesty requires both caveats: the 0.2%
error budget is actively disputed [22, 24] (the even-zonal cancellation depends
on achieved orbital injection accuracies), and on the co-rotating branch the
measurement constrains nothing. What is no longer hypothetical is the
*instrument*: the measurement exists, and any sharpening of either the
error-budget dispute or the state-selection problem now converts directly into
MeV-scale physics. (An earlier internal bound used a criterion with a spurious
linear term; the corrected suppression factor weakens the bound by 2.7× in Λ —
the correction is part of this paper's record. We have so far verified [23]
through its abstract and press coverage only — full-text verification is on the
pre-publication block list.)

**Virgin territory (searches declared).** Every computation of sources we could
find in Lorentz-violating massive gravity lives in the *mirror* family m₁² = 0
with massive tensor: the static solutions of [10, 11, 12], and the rotating
"bumpy black holes" of [13], which state verbatim that the linear-in-J dragging
is exactly GR there. PPN α₁, α₂ have never been computed for any of Dubovsky's
phases (zero occurrences in the canonical review [3]); our scale-dependent
screening is in any case outside the constant-coefficient PPN formalism.
Full-text searches for screened/Yukawa Lense–Thirring in massive or
Lorentz-violating gravity return nothing comparable; the closest conceptual echo
is the gravitomagnetic London moment claimed for laboratory superconductors [19]
— a different object in a different setting. The Einstein-aether/khronometric
family modifies frame dragging *fractionally* (via preferred-frame parameters),
without a screening length: different in kind. The signature is, to the searches
declared below, untested territory.

## 9. What this paper does not claim

- **It does not derive the Einstein–Hilbert term.** The EH kinetic term is
  assumed, as in the entire framework [1, 4, 5]. A fully emergent graviton faces
  Weinberg–Witten and needs different ideas (induced gravity, holography, or
  non-relativistic routes [15]); this paper does not touch that front.
- **It does not explain the hierarchy Λ ≪ M_Pl.** Inherited from the ghost
  condensate, declared, not cured.
- **The scalar sector is not a discovery channel.** It is exactly the ghost
  condensate's (m₁² cancels there); every scalar-sector bound and signature of
  [8, 9] applies verbatim, nothing new to measure on that side.
- **The frame-dragging signature is conditional** on the medium relaxing to its
  ground state around rotating sources. If nature sustains the persistent
  current, the Earth sees exact GR and there is no bound and no signal. Deciding
  the branch exceeds this paper's order of computation — stated as the open
  problem it is.
- **It does not validate the TCI program.** It answers one open question of the
  massive-gravity literature with one medium and its phenomenology. Within our
  own program the result *constrains*: by the exclusion lemma, any medium of
  this class underlying gravity must be positionally fluid at leading order —
  solids are out. (This converges with independent falsifications published in
  the program's record.)
- **The BCP misprint claim is provisional** until the authors confirm; the query
  letter is drafted and the evidence is public. Our own results do not hinge on
  it (U(X,Y) involves neither τₙ nor yₙ; the lemma's weights are the
  five-times-verified ones).

## 10. Open problems

1. **State selection** — the branch question of §8: what relaxation dynamics
   (nonlinear dissipation, vortex nucleation, formation history of the source)
   picks the gravitomagnetic state? This is now *the* question of the phase.
2. **FRW cosmology** of U(X,Y): equation of state, perturbations, comparison
   with the isentropic machinery of CCP [5, 6].
3. **Precise map to the tensor-order program**: the phase found here
   (m₂ = m₃ = m₄ = 0, m₀²m₁² > 0) is not identical to the phase targeted in an
   earlier note of our program (m₀ = 0 ∧ m₂ = 0); the exact relation remains to
   be written.
4. **Independent CAS re-derivation** (xAct/cadabra) of the dictionary — desirable
   redundancy before contacting the BCP authors, not load-bearing.
5. **NLO frame dragging on the co-rotating branch**: the first observable that
   could distinguish a persistent current from GR proper, if any exists.

## Acknowledgments

The derivations, the code and the drafting of this paper were developed in
collaboration with an AI system (Claude, Anthropic — working name *Fable*),
under the author's direction. All numerical and symbolic results are
reproducible with the public scripts referenced below. The author takes full
responsibility for the content.

## Reproducibility

All scripts are Python 3 + SymPy, total runtime under a minute on a laptop,
in `especulativo/campana-m2/` of the public repository
(github.com/IrigoyenNicolas1991/ift-theory):

| Block | Scripts | What they verify |
|---|---|---|
| Dictionary + calibrations | `masas_medio.py`, `calibracion_fonones.py` | general dictionary; isotropy; BCP (7.5); Dubovsky m₁=0 phase; gold calibration (Goldstone route, remainder 0); transverse sector |
| U(X,Y) and the protected phase | `parteB_medioXY.py` | off/on-shell masses; ghost-free corner; Schur identity; nonlinear invariance; residual-symmetry invariance; exclusion lemma |
| Misprint verification | `verificacion_independiente.py`, `refutador_pesos_bcp.py` | exact-inverse rederivation; blind refutation (4 methods) |
| Scalar sector | `escalar/derivador/*`, `escalar/verificador/*`, `escalar/cotas_fenomenologicas.py` | EH from scratch; LO freeze-out; NLO dispersion; ACLM dictionary; bounds — derivation and independent verification pipelines share no code |
| Matter coupling | `acople/estatico/*`, `acople/frame-dragging/*`, `acople/verificador/*` | causal theorem; γ(p); two branches; rotating-sphere exterior; precession factors; bounds — again with a disjoint verification pipeline |

## Novelty search (method declared)

Full-text INSPIRE searches (2026-07-21): "unrestricted internal diffeomorphisms"
— 0 hits; "unrestricted spatial diffeomorphisms" — 3 hits, all in shape
dynamics/unimodular gravity (physical-space diffeomorphisms, different object);
"shear rigidity" ∧ "graviton mass" and "graviton mass" ∧ "shear modulus" — the
holographic-elasticity literature [17] and crystal gravity [18], which relate
mass and rigidity in other frameworks but do not state the protection lemma in
the BCP/Dubovsky setting; Lense–Thirring ∧ massive gravity and gravitomagnetic ∧
Meissner sweeps — no screened frame dragging in any massive/LV gravity phase
(closest echo: [19], laboratory superconductors). All 19 papers citing [1] since
2024 were listed; none constructs a medium for the protected phase. The 2026-07-20
campaign additionally swept arXiv/INSPIRE 2004–2026 for the U(X,Y)
identification (closest: CCP's isentropic U(X+Y²) [5], without the symmetry or
the phase connection). If prior art exists that these searches missed, the
novelty rows above are forfeit and this file will say so.

## References

[1] S. L. Dubovsky, "Phases of massive gravity", JHEP 10 (2004) 076,
arXiv:hep-th/0409124.
[2] V. A. Rubakov, "Lorentz-violating graviton masses...", arXiv:hep-th/0407104.
[3] V. A. Rubakov, P. G. Tinyakov, "Infrared-modified gravities and massive
gravitons", Phys. Usp. 51 (2008) 759, arXiv:0802.4379.
[4] G. Ballesteros, D. Comelli, L. Pilo, "Massive and modified gravity as
self-gravitating media", Phys. Rev. D 94 (2016) 124023, arXiv:1603.02956.
[5] M. Celoria, D. Comelli, L. Pilo, JCAP 09 (2017) 036, arXiv:1704.00322.
[6] M. Celoria, D. Comelli, L. Pilo, arXiv:1712.04827.
[7] arXiv:1907.11784 (same group; appendix mass formulas used in §2).
[8] N. Arkani-Hamed, H.-C. Cheng, M. A. Luty, S. Mukohyama, "Ghost
condensation...", arXiv:hep-th/0312099.
[9] N. Arkani-Hamed et al., arXiv:hep-ph/0507120 (CMB "twinkling" bound).
[10] S. L. Dubovsky, P. G. Tinyakov, I. I. Tkachev, arXiv:hep-th/0504067.
[11] M. V. Bebronne, P. G. Tinyakov, arXiv:0705.1301; arXiv:0902.3899.
[12] D. Comelli, F. Nesti, L. Pilo, arXiv:1010.4773.
[13] S. Dubovsky, P. Tinyakov, M. Zaldarriaga, "Bumpy black holes from
spontaneous Lorentz violation", arXiv:0706.0288.
[14] D. T. Son, arXiv:cond-mat/0501658.
[15] L. Chojnacki, arXiv:2310.10078.
[16] S. Endlich, A. Nicolis, J. Wang, "Solid inflation", arXiv:1210.0569.
[17] L. Alberte et al., "Solid Holography and Massive Gravity",
arXiv:1510.09089 (and the holographic-elasticity literature that followed).
[18] J. Zaanen et al., "Crystal gravity", arXiv:2109.11325.
[19] M. Tajmar, C. J. de Matos, "Gravitomagnetic London moment and the graviton
mass inside a superconductor", arXiv:cond-mat/0602591.
[20] LIGO-Virgo-KAGRA, GWTC-3 tests of GR (graviton-mass bound
m_g ≤ 1.27×10⁻²³ eV), arXiv:2112.06861.
[21] I. Ciufolini et al., "A test of general relativity using the LARES and
LAGEOS satellites and a GRACE Earth gravity model", Eur. Phys. J. C (2016).
[22] L. Iorio, "Limitations in Testing the Lense–Thirring Effect with LAGEOS
and the Newly Launched Geodetic Satellite LARES 2", Universe 9 (2023) 211; and
"Will LAGEOS and LARES 2 succeed in accurately measuring frame-dragging?",
Eur. Phys. J. C (2025), arXiv:2503.07264.
[23] I. Ciufolini et al., "LARES-2 satellite measures frame-dragging effect
around the Earth", Nature (2026), doi:10.1038/s41586-026-10715-0 (published
July 2026).
[24] I. Ciufolini et al., "On the high accuracy to test dragging of inertial
frames with the LARES 2 space experiment", Eur. Phys. J. C (2024); and "A new
laser-ranged satellite for General Relativity and space geodesy: I. An
introduction to the LARES2 space experiment", arXiv:1910.13818.

## Pre-publication block list (nothing leaves the repo before these)

1. **In-house adversarial audit of THIS TEXT** (the three technical actas passed
   theirs; the paper's framing, claims-to-evidence map and every number
   transcribed here must be re-audited against the actas and scripts).
2. **Experimental accuracies — partially closed 2026-07-21**: primary references
   now cited ([21]–[24]) including the July-2026 LARES-2 Nature measurement and
   the Iorio error-budget dispute (both sides). Remaining: read the FULL TEXT of
   [23] (only abstract + press verified so far — paywall); complete
   volume/page data for [21], [22]-EPJC, [24]; add the GP-B primary reference
   (Everitt et al.) for the gyroscope factor of §8.
3. **BCP misprint**: send the query letter (drafted; requires Nico's explicit
   OK) and ideally receive an answer before any public claim beyond "probable
   misprint"; an xAct/cadabra run remains desirable redundancy.
4. **Verify reference [7]'s** bibliographic data (cited here by arXiv ID only)
   and complete journal data for [6, 9–15, 17–19].
5. **FRW section or explicit scope statement** (task 4 of the campaign) —
   referees will ask what the medium does cosmologically; §6's window partially
   answers, but the isentropic comparison with CCP is the natural completion.
6. **Explicit OK from Nicolás** on: channel (arXiv hep-th + PRD/JCAP as per the
   campaign plan), timing, and the final text. House policy: nothing public
   without per-piece sign-off.
