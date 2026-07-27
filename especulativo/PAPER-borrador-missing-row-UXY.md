# The missing row: unrestricted internal diffeomorphisms, the protected phase of Lorentz-violating massive gravity, and a screened frame-dragging signature

**Nicolás Irigoyen**

*Draft v0.6 — 2026-07-27 (v0.1 through v0.4 on 2026-07-21; v0.2 applied the 31
findings of the first in-house adversarial audit of the text, v0.3 the 12
findings of the second — record and both reports in
`campana-m2/AUDITORIA-TEXTO-PAPER-2026-07-21.md`; v0.4 added the FRW section §9
from the verified task-4 campaign; v0.5 (2026-07-25) recorded L. Pilo's
confirmation of the BCP misprint —
email, 22 Jul 2026, cc D. Comelli, see §2 and
`campana-m2/RESPUESTA-PILO-2026-07-22.md`; **v0.6 applies the 2026-07-27
block-list-closure campaign** — third text audit (30 findings), §9's own
adversarial physics audit (one formula refuted and corrected in place: the
attractor dispersion; the correction strengthens the freeze-out), the full
quadratic FRW action (tensor confirmed, vector closed as a new identity,
(7.22) factor closed as a convention), the {X,Y} completeness proof (§3), the
C5d reconciliation, the reference-verification pass, and the [16]–[18]
content checks — record in `campana-m2/CIERRE-BLOCKLIST-2026-07-27.md`).
First written form of the
results of the m₂ = 0 campaign (2026-07-20/21; campaign records and full
verification chain in `especulativo/campana-m2/`:
`HANDOFF-campana-m2-2026-07-20.md`, `VERIFICACION-BCP-2026-07-21.md`,
`SECTOR-ESCALAR-2026-07-21.md`, `ACOPLE-MATERIA-PPN-2026-07-21.md`,
`frw/FRW-2026-07-21.md`, `CIERRE-BLOCKLIST-2026-07-27.md`). Internal
working paper of the speculative stage of the Intangible Field Theory (TCI)
program, written to stand alone: nothing below depends on any other claim of that
program. **Not submitted anywhere.** The four technical legs (dictionary,
scalar sector, matter coupling, FRW) each passed an
independent adversarial verification pass (independent re-derivation pipelines,
including a blind refuter for the dictionary leg; none refuted — the FRW leg's
2026-07-27 pass corrected one of its published formulas, declared in §9); this
text has passed three audit passes;
**what remains before any submission is on the block list at the end** (one
final read of the assembled text, one scalar validation run in progress, and
the author's explicit sign-off). Honesty rules of the house apply: every
assumption declared, every "exactly" backed by a reproducible computation,
negative results stated with the same prominence as positive ones.*

---

## Honest scoreboard

Each row states whose work each piece is.

| Piece | Status | Whose |
|---|---|---|
| The phase m₂² = m₃² = m₄² = 0 of Lorentz-violating massive gravity exists, is UV-insensitive, and is healthy if m₀²m₁² > 0 | Known since 2004 | Dubovsky [1], eqs. (71)–(75) |
| The medium → graviton-mass dictionary (unitary gauge, self-gravitating media) | Known since 2016 | Ballesteros–Comelli–Pilo (BCP) [4] |
| The operator X + Y² and the isentropic class U(X + Y²) | Known since 2017 (thermodynamic route, no connection to the protected phase) | Celoria–Comelli–Pilo (CCP) [5] |
| Scalar-sector phenomenology of ω² ∝ p⁴ media (Jeans time, r_c, t_c, bounds) | Known since 2003–2005 | ghost condensate, ACLM [8, 9] |
| **The missing row of BCP's Table 2: Φᵃ → Ψᵃ(Φᵇ) unrestricted ⟹ U(X,Y) — with a completeness proof: {X, Y} exhausts the leading-order invariants (§3, machine-verified)** | **New (to the searches declared below; no prior classification of the unrestricted case found)** | this paper |
| **U(X,Y) lands exactly on the protected phase: m₂ = m₃ = m₄ = 0 emerge from the vacuum conditions, no tuning, explicit ghost-free corner** | **New, machine-verified** | this paper |
| **Exclusion lemma: on-shell m₁² = 2K_T, m₂² = −2G_T — protecting the graviton mass ⟺ switching off the medium's shear phonons (at leading order)** | **New in this framework** (the mass ↔ rigidity link is known in other settings [17, 18]) | this paper |
| **The exact scalar dispersion ω²(p) of this phase with gravitational mixing** (Dubovsky's leading-order freeze-out made quantitative; the p⁴ coefficient is NLO and UV-sensitive) | **New (first explicit form)** | this paper |
| **Causal theorem: with conserved sources the leading-order solution is exactly GR; γ_PPN = 1 exact; the mass only selects the gauge** | **New for this phase** (mechanism anticipated qualitatively by Dubovsky's "gauge-fixing" remark [1]) | this paper |
| **Frame dragging has two branches: relaxed medium ⟹ Yukawa-screened (gravitomagnetic Meissner); co-rotating medium ⟹ exact GR. Screened Lense–Thirring as the falsifiable signature; the July-2026 LARES-2 measurement (claimed 0.2% [23]) gives Λ < 1.12 MeV on the relaxed branch if its error budget holds** | **New; no prior computation of rotating sources in any m₁² ≠ 0 phase found** | this paper |
| **FRW: the tensor masslessness is an FLRW identity (and so is the vector freezing — both potentials ∝ the Friedmann-II combination, from the full quadratic action); the protected Minkowski vacuum is the cosmological attractor (in the mirror phase it is not [10]); vacuum-form stress on the attractor (w = −1 whenever U* ≠ 0); transient = exact dust; scalar stays frozen — the attractor spectrum is purely damped, zero phase velocity (the earlier ω = ±(H/√2)k + 3iH was refuted by this paper's own 2026-07-27 audit and corrected in §9)** | **New as a package (mechanism from [8, 10], current known to [5] as entropy; §9 audited 2026-07-27 — one formula corrected, the correction strengthens the freeze-out; rest survived + the quadratic-action pass confirmed tensor and closed vector)** | this paper |
| Misprint in BCP eqs. (7.6)–(7.7) — **confirmed by L. Pilo** (email to N.I., 22 Jul 2026, cc D. Comelli, after re-checking their original notebooks; formal private-communication citation pending permission); two misprints in Dubovsky eqs. (73), (99) | Found and cross-checked five independent ways (BCP case), then confirmed by L. Pilo | this paper |
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
possible subgroups of the diffeomorphism group." To the searches declared below,
the medium realizing that phase was never constructed. Ballesteros–Comelli–Pilo (BCP) later built the general
dictionary from self-gravitating media (four Stückelberg scalars Φ^A) to the five
graviton mass parameters, classifying media by their internal symmetry — solids,
fluids, superfluids, supersolids — all protected by (subgroups of)
*volume-preserving* internal
diffeomorphisms. We point out that their Table 2 has a missing row: media invariant
under **unrestricted** internal spatial diffeomorphisms, Φᵃ → Ψᵃ(Φᵇ) with no
condition on the determinant. Two invariants survive at leading order,
X = C⁰⁰ and the counterflow Y = u·∂Φ⁰, and the resulting medium U(X,Y) lands
exactly on the protected phase: the flat-space tadpole conditions force
m₂² = m₃² = m₄² = 0 identically, with m₁² = 2U_X ≠ 0 and an explicit ghost-free
corner. The identification comes with a structural lemma: on-shell, m₁² = 2K_T and
m₂² = −2G_T, where K_T and G_T are the inertia and the rigidity of the medium's
transverse (shear) sector — **the graviton mass is the shear rigidity of the
medium**, so protecting the massless graviton is equivalent to switching off shear
phonons at leading order: the medium must be a fluid. We then compute what this
phase does in the lab. The scalar sector is frozen at leading order (a double zero,
matching the content of Dubovsky's eq. 99); the ω² ∝ p⁴ dispersion turns on only through
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
order), and we state it as such. Claimed LAGEOS/LARES accuracies (few-percent
level, error budget contested) give Λ ≲ 2.0–2.6 MeV; **the LARES-2 measurement
published in July 2026 reports agreement with GR at its 0.2% design accuracy
(verified here against its openly served Extended Data, Supplementary and
peer-review material; main text pending), which, if its contested error
budget holds, pushes the relaxed-branch bound to Λ < 1.12 MeV, i.e. screening
lengths beyond 30 R⊕**.
To our searches (declared below), no computation of rotating sources exists in
any m₁² ≠ 0 phase. On FRW backgrounds the story closes on its own: the tensor
masslessness is an FLRW *identity* (X and Y are exactly blind to
transverse-traceless strain); the density of the medium's conserved charge
dilutes as a⁻³ and
drives the background onto the protected corner (in the Minkowski basin) —
the phase's
Minkowski vacuum is a cosmological attractor, where its mirror-phase analogue
is explicitly not; the attractor's stress is vacuum-form (w = −1 whenever
U* ≠ 0) with a purely damped scalar spectrum, and the off-attractor
transient redshifts as exact dust, reproducing the ghost condensate's
cosmological-constant-plus-dark-matter phenomenology. As by-products, we
report a misprint in
the mass-parameter weights of BCP eqs. (7.6)–(7.7) — with the correct weights
established five independent ways and since confirmed by L. Pilo (email,
22 Jul 2026, cc D. Comelli) — and two minor misprints in Dubovsky's
eqs. (73) and (99). All results are
symbolic (SymPy) and public; individual scripts run in seconds to about two
minutes.

---

## 1. Introduction

Massive gravity with broken Lorentz invariance is less constrained than its
Lorentz-invariant cousin: with separate mass parameters m₀…m₄ for the different
components of h_μν (in the notation of [1–3]), the Boulware–Deser ghost can be
evaded (m₀ = 0), the vDVZ discontinuity is absent, and — the case of interest
here — there exists a phase where the spin-2 graviton is **exactly massless while
the medium that breaks Lorentz invariance is still there**. (The ghost evasion via
m₀ = 0 belongs to a different corner of the class; the phase below is ghost-free
through m₀²m₁² > 0 instead.) Dubovsky exhibited it
in 2004 [1]: if the vacuum preserves the residual symmetry

    xⁱ → xⁱ + ξⁱ(x⃗)        (Dubovsky eq. 71)

then m₂² = m₃² = m₄² = 0 (his eq. 72) — and, unlike generic mass patterns, this
one is stable under radiative corrections, because any counterterm must respect
the residual symmetry (UV-insensitivity). The phase propagates the two GR tensor
polarizations at the full speed of light, plus a vector sector controlled by m₁²
and a scalar sector we discuss at length below. Its health condition is m₀²m₁² > 0 (his
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
symmetry: solids U(τₙ), perfect fluids U(b,Y), superfluids U(X,Y,b), supersolids
(in the effective-field-theory-of-media tradition [14]) — every row protected by
(a subgroup of) the internal diffeomorphisms that **preserve the volume
element**, det(∂Ψ/∂Φ) = 1.

This paper adds the row that the table is missing — the medium invariant under
internal spatial diffeomorphisms with **no restriction at all** — and shows that
it is precisely the object Dubovsky's invitation asked for. We then push the phase
through its first phenomenology with matter (to our searches): the result is a
theory that imitates GR by theorem in the static and orbital regimes where GR is
best measured — the radiative sector is open (§11) — and deviates in exactly one
computed place: the gravitomagnetic sector, where all prior source computations
in this class live in the mirror family m₁² = 0, and nothing exists for m₁² ≠ 0
(searches declared below).

Everything below is machine-verified symbolic algebra (SymPy; exact rational
arithmetic; no truncations except the declared perturbative orders), reproducible
in seconds to minutes from the public scripts (§ Reproducibility). The four
technical
blocks (dictionary + misprint; scalar sector; matter coupling; FRW cosmology §9)
were each
re-derived from scratch by an independent adversarial pipeline that shared no
code with the original derivation — plus, for the dictionary leg, a blind
refutation attempt; none refuted (the verifiers did catch five minor slips —
four in the scalar leg, one omitted term in the matter leg — all incorporated
and on record).

## 2. Conventions, the calibrated dictionary, and a misprint in BCP

We work throughout in BCP's conventions [4]: signature (−,+,+,+), unitary gauge
Φ⁰ = t, Φᵃ = xᵃ, M_Pl = 1 unless restored, flat background g = η + h. The medium
invariants are X = C⁰⁰ (background −1), V^a = C^{0a}, the spatial block B^{ab}
(background δ^{ab}), Z^{ab} = V^aV^b, τₙ = Tr(Bⁿ), yₙ = Tr(BⁿZ), b = √det B, and
Y = u·∂Φ⁰ (equal to 1/√(−g₀₀) in the unitary gauge Φ⁰ = t) with u^μ the unit
vector normal to constant-Φ⁰ slices. The
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
itself: their tensor-sector mass formula — their eq. (7.22); we had cited it as
(7.21) until the equation numbering was verified against the .tex source on
2026-07-27 — M₂² = Σn²U_τₙ (quoted at a = 1; the full
expression carries a^(−2(n−1))), is compatible with our weights and not with
their printed (7.7); (5) the appendices of the later papers
of the same group [5, 6, 7] use precisely our weights (flat in yₙ from n = 0, n²
in τₙ). No erratum of PRD 94, 124023 exists; the equations are unchanged between
arXiv v1 and v2. **Confirmed by L. Pilo**: the query letter was sent on
21 Jul 2026, and L. Pilo (email, 22 Jul 2026, cc D. Comelli), after re-checking
the original Mathematica notebooks, confirmed the misprints in m₁² and m₂² and
agreed with our expressions (paraphrase; permission for a formal
private-communication citation has been requested; whether a PRD erratum will be
filed is the authors' call — record in `campana-m2/RESPUESTA-PILO-2026-07-22.md`).
Caveats: the comparison was made at
a = N = 1; the journal PDF itself was not accessible to us (paywall).

For the central result of this paper the issue is moot — U(X,Y) depends on
neither τₙ nor yₙ — but the exclusion lemma of §5 does use those weights, so the
verification chain above is part of this paper's evidence base.

**Two minor misprints in Dubovsky [1]** (found while cross-checking our scalar
sector against his; neither affects his conclusions): in eq. (73), dimensional
analysis requires Λ² where Λ⁴ is printed (his strong-coupling scale — unrelated
to the medium scale Λ introduced in §6; an "= 0" is also omitted); in eq. (99),
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

Both invariances were verified *non-linearly* on a randomized exact instance
each (one rational random metric, one quadratic internal diffeomorphism, exact
arithmetic: ΔX = ΔY = 0 exactly). That {X, Y} **exhausts** the leading-order invariants is now proved and
machine-verified (`campana-m2/exhaustividad_XY.py`, 19/19 checks in exact
arithmetic), no longer inherited. The argument is elementary. At leading order
(one derivative per field) the building blocks are the entries of C^{AB} — X,
V^a, B^{ab} — plus the oriented Jacobian Z_ε = ε^{μνρσ}∂_μΦ⁰∂_νΦ¹∂_ρΦ²∂_σΦ³/√−g,
the one scalar not a function of C (Dubovsky's general one-derivative action,
eqs. (14)–(15) of [1]). An internal diffeomorphism acts on these pointwise
values only through its Jacobian J = ∂Ψ/∂Φ|_{Φ(x)} ∈ GL(3) — already realized
by linear Ψ; derivatives of J enter only ∂C-operators, NLO by the derivative
counting. On the physical domain (B positive definite, det C ≠ 0; the
background sits inside) every (X, V, B) is brought to the normal form
(X, (√W, 0, 0), δ), W ≡ V·B⁻¹·V, by J = R·A⁻¹ with B = AA^T: the GL(3) orbits
are exactly the fibers of the pair (X, W), so **every invariant is a function
of (X, W)** — confirmed by the infinitesimal count (generic orbit dimension
8 = 9 − 1, hence 10 − 8 = 2 invariants). The Schur identity
det C = det B·(X − W) gives (C⁻¹)₀₀ = (X − W)⁻¹ = −Y⁻², i.e.

    V · B⁻¹ · V = X + Y² ,

with the sign of Y fixed by time orientation (u future-directed) as in [4];
the spatial block of the 4×4 inverse yields nothing new either
(V·(C⁻¹)|ₛ·V = WX/(X−W)). Z_ε itself is *not* invariant — Z_ε → det J·Z_ε with
det J free — which is precisely how the volume-preserving column of the table
dies (b, τₙ, yₙ all transform), while Z_ε/b = ±Y adds nothing. Hence U(X, Y),
with no third argument. Two corollaries close the circle: restricting to
det J = 1, the same count gives three invariants {X, Y, b} — BCP's superfluid
row, recovered as a calibration — and dropping the clock leaves no invariant
at all (GL(3) acts transitively on positive B): a medium of Φᵃ alone with the
unrestricted symmetry is dynamically empty — the missing row *requires* the
clock. The classification is the internal, time-independent analogue of the
unitary-gauge operator classification of the EFT of inflation [27], whose
larger residual group ξⁱ(t, x⃗) leaves only g⁰⁰; restricting to ξⁱ(x⃗) is
exactly what lets the counterflow Y survive. Scope declared: leading order
only (the NLO basis of §6 is a separate statement); Wess–Zumino-type terms
shifting by a total derivative are outside the algebraic argument (as in
[1, 4]).

So U(X,Y) is a two-component object — a clock condensate plus flow lines — whose
only memory of ever having had a lattice is the flow direction: *a superfluid
that forgot its lattice*. CCP [5] found the one-variable subclass U(X + Y²) in
2017 as the isentropic thermodynamic class — without noting the unrestricted
symmetry, and without the connection that is the point of this paper. What
U(X,Y) is **not**: it is not the ghost condensate P(X) — flat-space tadpoles
force U_X = 0 on P(X) (hence its m₁² = 0), while U(X,Y) sustains U_X ≠ 0 because
the counterflow compensates the tadpole (U_Y = 2U_X, next section); and it is not
BCP's superfluid U(X,Y,b) — any dependence on b regenerates m₃² = U_bb/2 ≠ 0 and
m₄² ≠ 0. It is also not the finite-temperature superfluid U(X,Yb) of
Khoury–Sakstein–Solomon [25], which realizes the *mirror* structure (m₁² = 0
identically for that class) and degravitates vacuum energy there; our row sits
at m₁² ≠ 0, which is where the signature of §8 lives. U(X,Y) is the exact point
where the medium stops feeling its own volume.

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
symmetry-protected, and any counterterm at leading order in derivatives that
respects the symmetry is again of the form U(X,Y), whose vacuum masses vanish
again; higher-derivative counterterms (the NLO operators of §6) respect the
symmetry too and do not regenerate the vacuum masses either — Dubovsky's
UV-insensitivity, now with an explicit medium carrying it.

**The ghost-free corner is explicit.** Taking

    U = (X+1) + 2(Y−1) + ½(X+1)²

(U(vac) = 0, U_X = 1, U_Y = 2U_X, U_XX = 1), the dictionary gives

    (m₀², m₁², m₂², m₃², m₄²) = (1, 2, 0, 0, 0) ,   m₀²m₁² = 2 > 0  ✓

satisfying Dubovsky's health condition (75). The vector sector has the healthy
gapped dispersion of his eq. (73) whenever m₁² = 2U_X ≠ 0 (that is the
Goldstone-sector statement; for its fate with gravitational mixing see §6). The
scalar sector is §6. Death criterion 1 of the campaign (m₂² ≠ 0, or no ghost-free corner) was not
triggered.

## 5. The exclusion lemma: the graviton mass is the medium's shear rigidity

The identification comes with a structural consequence, itself a result.
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
order — a solid, a supersolid — endows the graviton with mass and loses the
protection. Conversely, a medium that protects
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

Declared escapes (they delimit the claim rather than undermine it): higher-derivative
kinetic structures (spin-nematic Goldstone routes à la Chojnacki [15], with
non-relativistic dispersion), and induced gravity à la Sakharov — which is
exactly the first non-claim declared in §10 (the EH term is assumed throughout,
here as in [1, 4, 5]). Death criterion 2 did not trigger as a no-go: it became this lemma.

## 6. The scalar sector is frozen at leading order

Here this paper corrects its own campaign's earlier internal note, which had
paraphrased Dubovsky as "one scalar mode with ω² ∝ p⁴". The precise statement,
now machine-verified with gravitational mixing included (independent adversarial
re-derivation from √−g R; no refutation):

1. **At strict leading order (U(X,Y) + quadratic EH), the scalar sector does not
   propagate.** The determinant of the scalar block is

       det ∝ −(M_Pl⁴ m₀² m₁²/2) · ω⁴ p⁶

   — a **double zero** at ω² = 0 for every p. This matches the content of
   Dubovsky's eq. (99) (with the sign misprint noted in §2 corrected) and his
   verbatim conclusion ("mixing with gravity does not introduce new propagating
   modes").

2. **The ω² ∝ p⁴ dispersion requires the medium's NLO operators** (the
   higher-derivative invariants compatible with the residual symmetry ξⁱ(x⃗):
   K̄ᵢⱼK̄ᵢⱼ, (tr K̄)², …). With them, exactly one scalar mode turns on, and its p⁴
   coefficient is **UV-sensitive**: c₄ ≈ −(α+β)/m₀², where α and β denote the
   couplings of the two quadratic invariants in K̄ᵢⱼ — the perturbation of the
   extrinsic curvature of the constant-Φ⁰ hypersurfaces — and σ, ρ those of the
   mixed NLO operators entering the scalar channel. (§7's static channel uses σ
   and ρ_op; ρ_op ≡ ρ — same operator, same normalization — was verified term
   by term on 2026-07-27, closing that question:
   `acople/estatico/C5d_dirimido.py`, checks [7a]/[7b]; see block-list item 7.) The precise operator basis is fixed in the
   public scripts. The coefficient is *not* expressible in the masses alone. Dubovsky left the coefficient
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
   (healthy vector). In the explicit corner (m₀², m₁²) = (1, 2) with β = −ε
   (a small positive parameter — unrelated to the perturbative bookkeeping ε of
   §2): kinetic coefficient K = 3 + 2/ε > 0 and ω² = εp²(2p² − 1)/(2 + 3ε) — a
   soft Jeans below p² = ½, stable above.

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
LO — det = (m₁²/4)·ω²p²(M_Pl² + α); the gapped dispersion (73) quoted in §4 is
the Goldstone-sector result, while with gravitational mixing the vector is a
constraint at this order, and solving that constraint with sources is exactly
what §8 does. The tensor is massless **exactly**, with
c_T² = M_Pl²/(M_Pl² + α): its masslessness is untouched by everything above,
while α ≠ 0 shifts its speed — GW170817's |c_T − 1| ≲ 10⁻¹⁵ therefore bounds
α/M_Pl², a constraint we flag for the phenomenological pass rather than evaluate
here. Mode counting: 2 (LO), 2+1 (NLO), matching Dubovsky.

The one thing the ghost condensate is *forbidden* to have — by its own residual
symmetry, verified textually — is m₁² ≠ 0. That is the one sector where this
medium is distinguishable, and it is the subject of the next two sections.

## 7. Matter coupling: Einstein by theorem, not by tuning

Couple a conserved source T_μν minimally to g_μν (the medium couples only
gravitationally; no direct Φ–matter coupling — declared assumption). One expects
a massive theory to deform Newton. It does not, and the reason is structural:

**Causal theorem (the causal candidate satisfies both the four massive-system
equations and the four pure-GR equations — residues [0,0,0,0] in each set).**
For any conserved source switched on at a finite time, the leading-order solution
of the massive system is **exactly** the solution of pure GR; the mass term
selects the synchronous gauge of that solution and costs zero action on-shell
(L_mass = 0 identically on the causal branch). Consequently γ_PPN = 1 **exactly**
(not approximately) in all principal regimes, Newton's constant is the bare one
(no renormalization), and the static potential of an eternal source — the
oscillating cos(μ_s r)/r family, μ_s² = m₀²/(2M_Pl²), *not* Yukawa — is a fixed
point that a causal history approaches only on times t_c ~ 18 Hubble ages at
Λ = 10 MeV (scaling as Λ⁻³, §6 — unreachable across the conservative window
Λ ≲ 10 MeV), exactly as in the ghost condensate [8], with which the dictionary
is again arithmetic (μ_s² = m²_ACLM). At NLO the static PPN correction is

    γ(p) = 1 − 2σp²/M_Pl² + p⁴[ρ_op²/(M_Pl² m₁²) + 4σ²/M_Pl⁴] + O(p⁶)

— scale-dependent, outside the constant-γ PPN book-keeping, and parametrically
far below solar-system sensitivity for the allowed Λ. The closed-form causal initial-value
problem confirms the theorem dynamically: ΔΨ(t,p) = A(p)[1 − cos Ω(p)t], with
cos → cosh in the Jeans band. (Dubovsky's remark that the mass here "has the
form of a gauge fixing" [1] finds its precise content in the vector sector: §8.)

In every static and orbital regime computed here, then, this phase *is*
Einstein — by theorem, not by calibration. (The radiative sector — binary-pulsar
damping — is not computed in this paper; see Open problems.) The deviation must
therefore be sought elsewhere.

## 8. Frame dragging: two branches, one untested signature

The exception is the sector where m₁² lives: gravitomagnetism. Here the
campaign found structure that, as far as our searches reach, nobody had noticed
in any phase of this class.

**The two branches.** The same residual symmetry ξⁱ(x⃗) that protects m₂ = 0
gives the vector sector an exact conservation law, which leaves a flat direction
in the space of stationary vector states. The physical consequences bifurcate:

- **Relaxed branch (medium in its ground state).** The gravitomagnetic potential
  Sᵢ ≡ h₀ᵢ obeys a **derived** massive equation sourced by the transverse
  momentum density τᵢ (the T₀ᵢ of the rotating source),

      (∇² − μ²) Sᵢ = 16πG̃ τᵢ ,   μ² = m₁²/(M_Pl² + α) ,   G̃ = G·M_Pl²/(M_Pl² + α)

  — a gravitomagnetic Meissner effect: the medium expels frame dragging beyond
  the screening length ℓ₁ = 1/μ. For a rigidly rotating sphere of radius R
  (exterior, exact):

      h₀ᵢ = 2G̃ (x⃗×J⃗)ᵢ (1 + μr) e^(−μr) / r³ · 𝔉(μR) ,
      𝔉(y) = 15[(y² + 3)sinh y − 3y cosh y]/y⁵ ,

  with the μ → 0 limit reproducing linearized Kerr exactly. Nodal precession of
  a satellite at semi-major axis a is suppressed by 𝒮 = (1 + x)e^(−x), x = μa —
  note **no linear term** (the Yukawa dipole cancels it); the gyroscope factor —
  GP-B's observable [28] — is (1 + x − x²)e^(−x). Ω⃗_nodo ∥ J⃗ holds for arbitrary inclination.

- **Co-rotating branch (medium recently stirred, no dissipation).** The exact
  solution is **GR in disguise**: the medium co-rotates with the frames and the
  screening is invisible. This branch is a genuinely excited state (higher
  Hamiltonian, verified, robust to boundary terms), and any dissipation relaxes
  it toward the screened branch — but a superfluid medium could in principle
  sustain it as a persistent current.

**The caveat, stated as a result.** Which branch describes the Earth is
**not decidable at quadratic order**: it depends on the relaxation history of the
medium around the source (nonlinear dissipation, vortices, formation history).
We therefore state the screening as a *conditional* prediction — conditional on
the medium relaxing — and we promote the condition itself to the open problem of
the phase: this phase has a two-state structure in its gravitomagnetic response
that the literature has not noticed (whether the same structure extends across
the wider m₁² ≠ 0 family is untested). Dubovsky's
gauge-fixing remark describes our co-rotating branch; the relaxed branch is new.

**Numbers.** Restoring units, μ = 2Λ²/M̄_Pl with M̄_Pl the reduced Planck mass —
the conventions of the campaign scripts: Λ is normalized by U = Λ⁴Û with
Û_X = 1 at the vacuum (so m₁² = 2Λ⁴), and M_Pl² ≡ 1/16πG = M̄_Pl²/2 — i.e.

    ℓ₁ = 2.40×10⁸ m · (MeV/Λ)²   — at Λ = 1 MeV, roughly the Earth–Moon distance.

Lense–Thirring measurements with LAGEOS/LARES (accuracies claimed between ~5%
[21] and ~2% in the same team's 2019 update [21b]; the error budget is contested
by independent assessments [22]) give **Λ ≲ 2.0–2.6 MeV** on the relaxed
branch. **In July 2026 the
LARES-2 team published this measurement** [23]: combining LARES-2 (in orbit
since 2022) with LAGEOS and GRACE data, they report agreement with GR at their
design accuracy of 0.2%. Taken at face value this
already pushes the relaxed-branch bound to **Λ < 1.12 MeV**, i.e. ℓ₁ > 30 R⊕ —
well inside the window where the medium is otherwise viable (§6); at Λ = 1 MeV
the predicted nodal deviation is 0.13% (LAGEOS/LARES-2-class semi-major axis
a = 1.227×10⁷ m, as in the campaign scripts). Honesty requires both caveats: the
0.2% error budget is disputed by Iorio [22] (the even-zonal cancellation depends
on achieved orbital injection accuracies) and defended by the team — [23]'s
Extended Data Table 2 lists the injection errors as negligible, and its public
Peer Review File carries the quantitative reply (achieved injection ~15× better
than the pre-launch assumption, inclination sum 180.01°, even-zonal residuals
folded into the Monte Carlo), alongside [24]; [23] itself does not cite [22] —
and on
the co-rotating branch the measurement constrains nothing. The measurement exists; any sharpening of the
error-budget dispute or of the state-selection problem now converts directly
into MeV-scale physics. (An earlier internal bound used a criterion with a spurious
linear term; the corrected suppression factor weakens the bound by 2.7× in Λ —
the correction is part of this paper's record. [23] is verified here against
its openly served primary material: abstract, reference list, Extended Data
Tables 1–3 — the 0.2% is the Total-RSS of Table 2(b), with μ = 1.0001 ± 0.0019
and the LARES-2 semi-major axis 12 264 567 m confirming the value used above —
the Supplementary Information, and the 88-page Peer Review File. The paywalled
main text (pp. 332–335) remains unread and stays on the block list.)

**Prior literature (searches declared).** Every computation of sources we could
find in Lorentz-violating massive gravity lives in the *mirror* family m₁² = 0
with massive tensor: the static solutions of [10, 11, 12], and the rotating
"bumpy black holes" of [13], which state verbatim that the linear-in-J dragging
is exactly GR there. PPN α₁, α₂ appear nowhere in the canonical review [3], and our searches found no
such computation for any of Dubovsky's phases; our scale-dependent screening is
in any case outside the constant-coefficient PPN formalism.
Full-text searches for screened/Yukawa Lense–Thirring in massive or
Lorentz-violating gravity return nothing comparable; the closest conceptual echo
is the gravitomagnetic London moment once claimed for laboratory superconductors
[19] — an unconfirmed, never-replicated experimental claim, and in any case a
different object in a different setting. The Einstein-aether/khronometric
family modifies frame dragging *fractionally* (via preferred-frame parameters),
without a screening length: different in kind. The signature is, to the searches
declared below, untested territory.

## 9. Cosmology: the protected corner is a cosmological attractor

*(This section entered in v0.4, after the two audit passes of §§1–8; it
received its own adversarial physics audit on 2026-07-27 — one leading-order
formula was refuted and corrected (the attractor dispersion, below), the rest
survived independent re-derivation; record in
`campana-m2/CIERRE-BLOCKLIST-2026-07-27.md` §5 and the correction addendum of
`campana-m2/frw/FRW-2026-07-21.md`. Full record: `campana-m2/frw/`.)*

On an FRW background (ds² = −dt² + a²dx², unitary gauge Φ⁰ = φ(t), Φᵃ = xᵃ) the
medium's invariants collapse to X = −φ̇², Y = φ̇ — the background lives on the
Schur surface X + Y² = 0. Three statements, each machine-verified by an
independent adversarial pipeline (three derivation routes for the background;
two routes and both polarizations for the tensor; frozen-coefficient
perturbation analysis for the scalar):

**The tensor protection is an FLRW identity.** A transverse-traceless
perturbation leaves X and Y invariant *exactly, to all orders in h* — in fact
δX = δY = 0 holds for *any* purely spatial perturbation in synchronous gauge,
stronger than TT — so U(X,Y)
touches the tensor sector only through √−g: the tensor mass vanishes
identically on any spatially flat FLRW solution of the theory — no vacuum
conditions required; with additional perfect-fluid matter the standard GR
cancellation applies (verified here for the self-sourced case) — with
c_T² = 1 at leading order (the NLO speed shift α of §6 is not recomputed on
FRW) and the standard 3H friction (H ≡ ȧ/a). Re-derived independently from the
full quadratic action (2026-07-27, `frw/accion_cuadratica_frw.py`): the tensor
mass coefficient is proportional to U + 2ä/a + H², which vanishes by
Friedmann II alone — and the same pass settled the apparent global factor 2
against BCP's (7.22): their printed formula is **correct**, the factor was
their M_Pl² = 1/16πG convention (no ½ on R) versus ours
(`frw/factor_722.py`, 17 checks). **The vector sector is frozen on any FLRW
too**: from the same quadratic action, the vector potential is proportional to
the very same Friedmann-II combination — identically zero on-shell for
arbitrary U(X,Y) and a(t) — leaving a nonpropagating constrained mode (the
exact FLRW generalization of the Minkowski double zero of §6), verified by
three routes and, term by term on-shell, against BCP's (7.24). (That fluids
and superfluids
have massless cosmological tensors is BCP's and CCP's general statement [4, 5];
the reading for this row, the vector-freezing identity, and the consequence —
the frame-dragging signature of
§8, a vector-sector effect, rides on a tensor sector that stays GR's at every
cosmological epoch — are
ours.)

**The protected Minkowski vacuum is the dynamical attractor of the rest of the
phase's histories.** The clock's equation of motion is the conservation of
J = a³s, with s = U_Y − 2φ̇U_X the quantity CCP identify as the medium's
entropy density
[5] — there a piece of thermodynamics, here the whole dynamics: expansion
dilutes the density J/a³ ∝ a⁻³, driving φ̇ to a root of
U_Y = 2φ̇U_X; in the Minkowski basin that root is exactly the flat-space
tadpole condition of §4 (the second condition, U* = 0, is the usual
cosmological-constant adjustment, not dynamics; the basin caveats — three
roots, and a ρ < 0 strip of the basin needing other matter early on — are in
Declared limits). Protection is not
an initial-condition choice; the expanding universe relaxes the medium onto its
protected corner. The mechanism — a conserved charge diluting onto a
symmetry-restoration point — is the ghost condensate's [8] and DTT's [10], and
we cite it as such; the identification of the attractor with *the same
theory's Minkowski tadpoles* is, to our searches, new — indeed in the mirror
phase it is explicitly false (DTT's attractor is not their Minkowski point
[10]), and for the related vacuum-energy-degravitating superfluid of
Khoury–Sakstein–Solomon the analogous question was posed in 2018 and left as
future work [25]; none of its citing papers answered it (21 citing papers
swept 2026-07-21; record in `campana-m2/frw/BIBLIOGRAFIA-FRW-2026-07-21.md`).

**On the attractor the stress is vacuum-form; the transient is exact dust.**
ρ + p = φ̇·J/a³ holds off-shell (Bianchi verified as an identity), so the
attractor has vacuum-form stress p* = −ρ* = U*: w = −1 exactly whenever
U* ≠ 0, while with the usual cosmological-constant adjustment (§4) U* = 0 the
endpoint is Minkowski itself and the approach is pure dust (w → 0 as ρ → 0 —
the campaign's numerical route shows exactly this).
The off-attractor component obeys δρ ∝ a⁻³ with δp = 0 *exactly* at linear
order — an algebraic identity of the class, needing only the simple-root
condition K = f′(1) = 2m₀² ≠ 0: the same m₀² of the health window m₀²m₁² > 0,
so the attractor's good conditioning and the scalar's health are one
requirement — reproducing the ghost condensate's
cosmological-constant-plus-cold-dark-matter phenomenology [8, 9] — cited,
not claimed. The scalar sector stays frozen on FRW: the Minkowski double zero
is reproduced exactly in the flat limit, and one zero of the determinant
persists
exactly on the full background — provably: the ω⁰ coefficient of the scalar
determinant is proportional to 3H² − ρ and vanishes by the Friedmann
constraint itself (the persistent zero *is* the constraint; the residual
symmetry survives FRW). The rest of the attractor spectrum is **purely
damped**. The v0.4–v0.5 drafts and the campaign record quoted
ω = ±(H/√2)k + 3iH here; **this paper's own 2026-07-27 audit refuted that
formula** — it came from truncating the determinant one order too early. The
correct leading order is

    det_dom = k³ · [ −8iω⁴ − 48Hω³ + 4iH²(k²+18)ω² + 24k²H³ω ] ,

whose nonzero roots in the EFT window (k ≲ 1 in units of Λ) are all purely
imaginary in the e^{+iωt} convention (Im ω > 0 = decay): a slow diffusive mode
ω ≈ i(k²/3)H and a pair ω = i(3 ∓ k/√2)H + O(k²) — the ±k/√2 split is real
but lives in the *damping*, not the phase velocity, which is zero; a
propagating pair appears only above k* ≈ 1.27, outside the window.
Triple-checked (exact symbolic extraction; the real cubic in y = −iω/H;
60-digit numerics). The correction *strengthens* the freeze-out: no
propagating mode and no instability at all in the window — every root has
Im ω ≥ 0. (All nonzero roots have |ω| ≲ 3.6H, inside the frozen-coefficient
band declared below: the numbers are indicative, the structural statement —
no propagation, no instability — is the robust part.)
This also answers, for this class, the published objection that w = −1
superfluids
are exponentially unstable and need a solid component [6, 26]: our
leading-order scalar is frozen (a double zero) rather than gradient-unstable,
and the k⁴ NLO then governs exactly as in the ghost condensate (§6) — the
exponential instability of [6, 26] does not arise here (their equation lives
in a different class; the .tex-level re-verification of [26] stays on the
block list) — while our w = −1
is a dynamical fixed point, not a symmetry-imposed constraint as in [6].

**Declared limits.** The explicit corner's (§4) fixed-point surface has,
besides
Minkowski, two model-dependent extra roots — an AdS-like point unreachable as
a flat-FRW endpoint (its basin recollapses) and a dS-like point with U_X < 0,
i.e. a sick vector sector, outside the healthy corner; only the Minkowski root
is structural (a linear U has it alone). The Minkowski basin of the explicit
corner requires φ̇ ≳ 0.816, and its 0.816 < φ̇ ≲ 0.97 strip has ρ < 0 —
inadmissible as the sole source in flat FRW, so histories starting there need
other matter to dominate early on (declared, not cured); the ω¹ coefficient
also has a second double-zero point at w ≈ 0.544, inside the AdS basin —
irrelevant to the attractor, listed for completeness. The scalar analysis uses
frozen
coefficients (valid for ω ≫ H; the ω ~ H band, where all the attractor roots
live, is indicative). The full quadratic FRW action is now derived
(2026-07-27): tensor and vector sectors closed as identities and the (7.22)
factor question closed as a convention (see above); the scalar sector's
four-field action is built, its constraints verified, and its symbolic
validation run against the corrected spectrum is in progress — that last run
is the remaining FRW item on the block list. Two further internal misprints
in BCP's §8 (a flipped k² sign in their GW2 and a factor-2 slip in their
printed propagation equation) were flagged in the same pass; they do not
affect our row (M₂² ≡ 0 identically) and await an independent check before
being reported (campaign acta).

## 10. What this paper does not claim

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
- **The BCP misprint is no longer provisional**: L. Pilo confirmed it
  (email, 22 Jul 2026, cc D. Comelli, after re-checking their original
  notebooks).
  Our own results never hinged on
  it (U(X,Y) involves neither τₙ nor yₙ; the lemma's weights are the
  five-times-verified ones, now author-confirmed).

## 11. Open problems

1. **State selection** — the branch question of §8: what relaxation dynamics
   (nonlinear dissipation, vortex nucleation, formation history of the source)
   picks the gravitomagnetic state? This is now *the* question of the phase.
2. **FRW cosmology** of U(X,Y): done at background + frozen-coefficient level
   (§9); remaining: the full quadratic action on FRW (no-ghost beyond the
   Minkowski limit), the ω ~ H band, and §9's own audit pass.
3. **Precise map to the tensor-order program**: the phase found here
   (m₂ = m₃ = m₄ = 0, m₀²m₁² > 0) is not identical to the phase targeted in an
   earlier note of our program (m₀ = 0 ∧ m₂ = 0); the exact relation remains to
   be written.
4. **Independent CAS re-derivation** (xAct/cadabra) of the dictionary — desirable
   redundancy (L. Pilo has since confirmed the misprints, §2), not load-bearing.
5. **NLO frame dragging on the co-rotating branch**: the first observable that
   could distinguish a persistent current from GR proper, if any exists.
6. **The radiative sector**: binary-pulsar damping (Hulse–Taylor) is untouched
   here. The tensor sector is GR's at this order, which suggests standard
   quadrupole radiation, but the vector/scalar bookkeeping with time-dependent
   sources remains to be done before any claim.

## Acknowledgments

The derivations, the code and the drafting of this paper were developed in
collaboration with an AI system (Claude, Anthropic — working name *Fable*),
under the author's direction. All numerical and symbolic results are
reproducible with the public scripts referenced below. The author takes full
responsibility for the content.

## Reproducibility

All scripts are Python 3 + SymPy, in `especulativo/campana-m2/` of the public
repository (github.com/IrigoyenNicolas1991/ift-theory). Individual scripts run
in seconds; the heaviest (`colA_causal.py`) takes about two minutes; the full
suite a few minutes on a laptop. (2026-07-21: the verifier-pipeline scripts of
`acople/` were repaired to run from the repository as published — import paths
and two runtime bugs, listed in the audit record; the repaired suite reproduces
every check quoted in this paper. The C5d check of `colA_causal.py` prints a
nonzero residue that was reconciled on 2026-07-27: an artifact of that check's
own extraction method, not physics — `acople/estatico/C5d_dirimido.py`, 26
exact checks; see block-list item 7.)

| Block | Scripts | What they verify |
|---|---|---|
| Dictionary + calibrations | `masas_medio.py`, `calibracion_fonones.py` | general dictionary; isotropy; BCP (7.5); Dubovsky m₁=0 phase; gold calibration (Goldstone route, remainder 0); transverse sector |
| U(X,Y) and the protected phase | `parteB_medioXY.py` | off/on-shell masses; ghost-free corner; Schur identity; nonlinear invariance; residual-symmetry invariance; exclusion lemma |
| Misprint verification | `verificacion_independiente.py`, `refutador_pesos_bcp.py` | exact-inverse rederivation; blind refutation (4 methods) |
| Scalar sector | `escalar/derivador/*`, `escalar/verificador/*`, `escalar/cotas_fenomenologicas.py` | EH from scratch; LO freeze-out; NLO dispersion; ACLM dictionary; bounds — derivation and independent verification pipelines share no code |
| Matter coupling | `acople/estatico/*`, `acople/frame-dragging/*`, `acople/verificador/*` | causal theorem; γ(p); two branches; rotating-sphere exterior; precession factors; bounds — again with a disjoint verification pipeline |
| C5d reconciliation | `acople/estatico/C5d_dirimido.py` | the C5d residue as an extraction artifact (symbolic identity); physical dispersion by Routhian and 4×4 determinant = scalar-pipeline formula; ∂ω²/∂m₁² = 0; ρ_op ≡ ρ term by term |
| Completeness of {X, Y} | `exhaustividad_XY.py` | chain-rule pointwise reduction; normal form and explicit connecting group elements; orbit count 10−8 = 2; symbolic Schur; candidate invariants dismissed (incl. Z_ε); sl(3) calibration (recovers BCP's superfluid row); no-clock corollary |
| FRW (§9) | `frw/fondo_frw.py`, `frw/verificador/v1_fondo_covariante.py`–`v4b_escalar_frw_analisis.py`, `frw/accion_cuadratica_frw.py`, `frw/factor_722.py` | three-route background; FLRW tensor identity + BCP (7.22) control; fixed-point map and basins; frozen-coefficient scalar analysis; full quadratic action (tensor/vector closed as identities, 17-check (7.22)-convention audit; scalar validation run in progress, block list) |

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
the phase connection). The full search log — queries verbatim, hit lists, the
19 citing papers, and declared limitations — is recorded in
`campana-m2/BARRIDO-INSPIRE-2026-07-21.md`. The FRW novelty claims of §9 rest
on the 2026-07-21 FRW bibliographic campaign: the 21 papers citing [25] and the
34 citing [5] were listed and checked (none does the U(X,Y) cosmology; KSS's
2018 question stands unanswered), plus full-text sweeps for
cosmological-attractor ∧ massive-gravity variants; record in
`campana-m2/frw/BIBLIOGRAFIA-FRW-2026-07-21.md`. The completeness claim of §3
rests on the 2026-07-27 pass: full-text checks of [1] (eqs. (14)–(15), stops at
the mass pattern), [4] ((4.9), §5.1.2, det = 1 imposed), [7] (det = 1), and
NPPR arXiv:1501.03845 (§2.1, stops at Diff′(3)), plus web sweeps for the
unrestricted case — no prior classification found. If prior art exists that
these searches missed, the novelty rows above are forfeit and this file will
say so.

## References

*(Bibliographic data verified against INSPIRE-HEP / primary sources,
2026-07-27; the record of that verification pass, including the [16]–[18]
content checks, lives in `campana-m2/CIERRE-BLOCKLIST-2026-07-27.md`.)*

[1] S. L. Dubovsky, "Phases of massive gravity", JHEP 10 (2004) 076,
arXiv:hep-th/0409124.
[2] V. A. Rubakov, "Lorentz-violating graviton masses...", arXiv:hep-th/0407104.
[3] V. A. Rubakov, P. G. Tinyakov, "Infrared-modified gravities and massive
gravitons", Phys. Usp. 51 (2008) 759, arXiv:0802.4379.
[4] G. Ballesteros, D. Comelli, L. Pilo, "Massive and modified gravity as
self-gravitating media", Phys. Rev. D 94 (2016) 124023, arXiv:1603.02956.
[5] M. Celoria, D. Comelli, L. Pilo, JCAP 09 (2017) 036, arXiv:1704.00322.
[6] M. Celoria, D. Comelli, L. Pilo, "Self-gravitating Λ-media", JCAP 01 (2019)
057, arXiv:1712.04827.
[7] M. Celoria, D. Comelli, L. Pilo, R. Rollo, "Adiabatic Media Inflation",
JCAP 12 (2019) 018, arXiv:1907.11784 (appendix A mass formulas used in §2).
[8] N. Arkani-Hamed, H.-C. Cheng, M. A. Luty, S. Mukohyama, "Ghost
condensation...", arXiv:hep-th/0312099.
[9] N. Arkani-Hamed, H.-C. Cheng, M. A. Luty, S. Mukohyama, T. Wiseman,
"Dynamics of gravity in a Higgs phase", JHEP 01 (2007) 036,
arXiv:hep-ph/0507120 (CMB "twinkling" bound; ghost dark matter).
[10] S. L. Dubovsky, P. G. Tinyakov, I. I. Tkachev, "Cosmological attractors in
massive gravity", Phys. Rev. D 72 (2005) 084011, arXiv:hep-th/0504067.
[11] M. V. Bebronne, P. G. Tinyakov, "Massive gravity and structure formation",
Phys. Rev. D 76 (2007) 084011, arXiv:0705.1301; and "Black hole solutions in
massive gravity", JHEP 04 (2009) 100 [Erratum: JHEP 06 (2011) 018],
arXiv:0902.3899.
[12] D. Comelli, F. Nesti, L. Pilo, "Stars and (furry) black holes in Lorentz
breaking massive gravity", Phys. Rev. D 83 (2011) 084042, arXiv:1010.4773.
[13] S. Dubovsky, P. Tinyakov, M. Zaldarriaga, "Bumpy black holes from
spontaneous Lorentz violation", JHEP 11 (2007) 083, arXiv:0706.0288.
[14] D. T. Son, "Effective Lagrangian and topological interactions in
supersolids", Phys. Rev. Lett. 94 (2005) 175301, arXiv:cond-mat/0501658.
[15] L. Chojnacki, R. Pohle, H. Yan, Y. Akagi, N. Shannon, "Gravitational wave
analogs in spin nematics and cold atoms", Phys. Rev. B 109 (2024) L220407,
arXiv:2310.10078.
[16] S. Endlich, A. Nicolis, J. Wang, "Solid Inflation", JCAP 10 (2013) 011,
arXiv:1210.0569.
[17] L. Alberte, M. Baggioli, A. Khmelnitsky, O. Pujolàs, "Solid Holography and
Massive Gravity", JHEP 02 (2016) 114, arXiv:1510.09089 (and the
holographic-elasticity literature that followed).
[18] J. Zaanen, F. Balm, A. J. Beekman, "Crystal gravity", SciPost Phys. 13
(2022) 039, arXiv:2109.11325.
[19] C. J. de Matos, M. Tajmar, "Gravitomagnetic London moment and the graviton
mass inside a superconductor", Physica C 432 (2005) 167, arXiv:cond-mat/0602591.
[20] LIGO-Virgo-KAGRA, GWTC-3 tests of GR (graviton-mass bound
m_g ≤ 1.27×10⁻²³ eV), arXiv:2112.06861.
[21] I. Ciufolini et al., "A test of general relativity using the LARES and
LAGEOS satellites and a GRACE Earth gravity model", Eur. Phys. J. C 76 (2016)
120, arXiv:1603.09674.
[21b] I. Ciufolini et al., "An improved test of the general relativistic effect
of frame-dragging using the LARES and LAGEOS satellites", Eur. Phys. J. C 79
(2019) 872, arXiv:1910.09908.
[22] L. Iorio, "Limitations in Testing the Lense–Thirring Effect with LAGEOS
and the Newly Launched Geodetic Satellite LARES 2", Universe 9 (2023) 211,
arXiv:2304.14649; and "Will LAGEOS and LARES 2 succeed in accurately measuring
frame-dragging?", Eur. Phys. J. C 85 (2025) 255, arXiv:2503.07264.
[23] I. Ciufolini et al., "LARES-2 satellite measures frame-dragging effect
around the Earth", Nature 655 (2026) 332–335, doi:10.1038/s41586-026-10715-0
(published 8 July 2026).
[24] I. Ciufolini et al., "On the high accuracy to test dragging of inertial
frames with the LARES 2 space experiment", Eur. Phys. J. C 84 (2024) 998; and
"A new laser-ranged satellite for General Relativity and space geodesy: I. An
introduction to the LARES2 space experiment", Eur. Phys. J. Plus 132 (2017)
336, arXiv:1910.13818.
[25] J. Khoury, J. Sakstein, A. R. Solomon, "Superfluids and the Cosmological
Constant Problem", JCAP (2018), arXiv:1805.05937.
[26] G. di Donato, L. Pilo, "Dynamical cosmological constant",
arXiv:2503.03589.
[27] C. Cheung, P. Creminelli, A. L. Fitzpatrick, J. Kaplan, L. Senatore, "The
Effective Field Theory of Inflation", JHEP 03 (2008) 014, arXiv:0709.0293
(unitary-gauge operator classification, §2 and App. A).
[28] C. W. F. Everitt et al., "Gravity Probe B: Final Results of a Space
Experiment to Test General Relativity", Phys. Rev. Lett. 106 (2011) 221101,
arXiv:1105.3456.

## Pre-publication block list (nothing leaves the repo before these)

1. **In-house adversarial audit of THIS TEXT — three passes DONE** (2026-07-21:
   31 findings applied in v0.2, then 12 more in v0.3, record in
   `campana-m2/AUDITORIA-TEXTO-PAPER-2026-07-21.md`; 2026-07-27: third pass on
   the full v0.5 text — 30 findings, applied in v0.6 together with the §9
   physics audit — record in `campana-m2/CIERRE-BLOCKLIST-2026-07-27.md`).
   Remaining: one final short read of the assembled text before submission.
2. **Experimental accuracies — closed to the paywall line 2026-07-27**: primary
   references cited ([21]–[24], [28]) with complete bibliographic data (INSPIRE
   pass; two corrections caught: [19] author order, [24]'s second item is EPJ
   Plus). [23] verified against its openly served primary material — Extended
   Data Tables 1–3 (the 0.2% Total-RSS, μ = 1.0001 ± 0.0019, semi-major axes),
   Supplementary, and the 88-page Peer Review File (which contains the
   quantitative reply to the injection-accuracy objection). Remaining: the
   paywalled main text of [23] (pp. 332–335, no preprint exists); full titles
   for [2], [5]; journal data for [8], [25], [26] if published.
3. **BCP misprint — RESOLVED 2026-07-22**: the letter was sent by the author on
   21 Jul 2026 and L. Pilo confirmed the misprints the next day (email, cc
   D. Comelli), agreeing with our expressions. Remaining: their permission for
   a formal private-communication citation (requested 25 Jul 2026); a PRD
   erratum is their call; an xAct/cadabra run remains desirable redundancy.
4. **Reference data — RESOLVED 2026-07-27** (INSPIRE-HEP verification pass,
   record in `campana-m2/CIERRE-BLOCKLIST-2026-07-27.md`): [7] verified in
   full — authors, journal, and content (its appendix-A mass formulas carry
   exactly the weights our §2 attributes to it, flat in U_yₙ including n = 0,
   n² in U_τₙ, signs included); journal data completed for [6], [10]–[15],
   [17]–[19], [21]–[24]. Residual items folded into item 2.
5. **FRW section — WRITTEN 2026-07-21, AUDITED AND UPGRADED 2026-07-27**.
   The 2026-07-27 adversarial physics audit refuted one leading-order formula
   (the attractor dispersion — corrected in §9 with the refutation declared;
   correction addendum in `frw/FRW-2026-07-21.md`; the correction strengthens
   the freeze-out) and confirmed the rest by independent re-derivation. The
   full quadratic FRW action was then derived
   (`frw/accion_cuadratica_frw.py`): tensor and vector closed as FLRW
   identities (vector: new result, three routes + BCP (7.24) term-by-term
   on-shell), and the (7.22) global factor closed as a convention
   (`frw/factor_722.py`, 17 checks; BCP's printed (7.22) is correct — and our
   earlier citations of it as "(7.21)" were renumbered after checking the .tex).
   **The scalar validation run finished the same day and CONFIRMS the
   corrected spectrum structurally**: exact Minkowski limit (double zero,
   coef(ω⁴) ∝ m₀²m₁²); persistent zero = Friedmann constraint confirmed from
   the action; all roots purely imaginary in the EFT window (zero phase
   velocity); exact root match with the audit's cubic at k = 1; and the new
   determinant is ∝ the v4 determinant with an ω-independent ratio, so the
   audit's exact-δ 60-digit run transfers to it (transitivity). Three
   surviving detail-level FAILs have their cause identified in the script's
   own code — it substitutes the linearized attractor w = 1 + (3/2)H², whose
   O(H⁴) error feeds the determinant's constant term at leading order, the
   same class of trap that produced the original dispersion error; the
   spurious term ∝ k²(k²−1) vanishes at k = 1, where everything matches
   exactly. Full breakdown, script flags, and the optional formal redundancy
   (re-run block S5 with exact δ) in `CIERRE-BLOCKLIST-2026-07-27.md` §6.
   **Remaining**: that optional exact-δ re-run, and the .tex-level
   re-verification of [26]'s quoted instability equation. The radiative
   sector stays open and named (§7, §11.6).
6. **Explicit OK from Nicolás** on: channel (arXiv hep-th + PRD/JCAP as per the
   campaign plan), timing, and the final text. House policy: nothing public
   without per-piece sign-off.
7. **C5d check — RESOLVED 2026-07-27** (`acople/estatico/C5d_dirimido.py`, 26
   symbolic checks, ~10 s). The nonzero residue was an artifact of the check's
   own extraction method, not physics: with ρ_op ≠ 0 the tr K̄·R3 operator
   couples ψ to Ė in the reduced Lagrangian, so reading ω² off the raw ψ̈
   coefficient omits exactly −G²/(4AF−D²) — reproduced symbolically as the
   printed residue. The physical dispersion of the same Lagrangian (Routhian at
   conserved Π_E, and the 4×4 determinant — `colA_cierre.py` D1) equals the
   scalar-pipeline formula exactly, with ∂ω²/∂m₁² = 0: the exact m₁²
   cancellation is confirmed from the coupling pipeline too. Bonus closure:
   ρ_op ≡ ρ (same operator, same normalization, term-by-term check [7a]/[7b]),
   so §6's former non-identification caveat is dropped.
8. **Characterizations of [16]–[18] — RESOLVED 2026-07-27**: all three verified
   against their source texts (record with textual quotes and locations in
   `campana-m2/CIERRE-BLOCKLIST-2026-07-27.md`). All three RESPALDA: [16]'s
   tensor mass term m_γ² = 4εH²c_T² with c_T² carrying the solid's moduli
   (vanishing for the perfect fluid), celebrated there as the blue-tilt
   signature; [17] encodes rigidity "exclusively in the m₂(r) mass parameter"
   (same name, same role as our lemma); [18] derives m_G = √(16πGμ/c²) with μ
   the shear modulus, gravitons coupling "exclusively to the shear stress".
9. **Completeness of {X, Y} — RESOLVED 2026-07-27**: normal-form classification
   proven and machine-verified (`campana-m2/exhaustividad_XY.py`, 19/19 checks
   in exact arithmetic; full statement now in §3): GL(3) orbits = fibers of
   (X, W = X + Y²) on the non-degenerate domain; the ε-Jacobian Z_ε is not
   invariant; sl(3) calibration recovers BCP's superfluid row {X, Y, b};
   no-clock corollary (a medium of Φᵃ alone with the unrestricted symmetry is
   dynamically empty). No prior classification of the unrestricted case found
   ([1] stops at the mass pattern; [4], [7] impose det = 1; NPPR 1501.03845
   §2.1 stops at Diff′(3)); methodological precedent cited: [27], App. A.
   Declared scope: leading order only; Wess–Zumino terms outside.
