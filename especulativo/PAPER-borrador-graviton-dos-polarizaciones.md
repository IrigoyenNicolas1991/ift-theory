# The phonon as the second graviton polarization: exactly two massless transverse-traceless modes in the D₄ biaxial-nematic phase of a spin-2 superfluid

**Nicolás Irigoyen**

*Draft v0.1 — 2026-07-21. First written form of the results obtained 2026-07-16/17
(program logbook `BITACORA-campana-condensado-2026-07-16.md`, §14–§17, §22; master
document `NUCLEO-TCI2-lagrangiano.md`). Internal working paper of the speculative
stage of the Intangible Field Theory (TCI) program. **Not submitted anywhere. This
text has NOT yet passed the in-house adversarial audit** (see the pre-publication
block list at the end). Honesty rules of the house apply: all assumptions declared,
all negative results stated with the same prominence as positive ones.*

---

## Abstract

Emergent-gravity programs built on condensed-matter substrates have a
polarization problem: media whose order parameter is a displacement field carry
at most spin-1 collective modes, and the known spin-2 collective modes of
tensor-ordered media are all **gapped** — the J = 2± squashing modes of ³He-B,
the chiral gravitons measured in fractional quantum Hall systems (helicity ±2,
but massive), and the "graviton" modes in Volovik's emergent-gravity scenarios
(Higgs-like, massive). The object that gravitational-wave phenomenology actually
requires — **two** massless transverse-traceless (TT) modes and nothing else at
zero helicity gap — had, to our knowledge, no realization as the spontaneous
spectrum of a condensate. We exhibit one. In a J = 2 superfluid with spatial
spin-orbit locking, described by the **textual** ³P₂ Ginzburg–Landau functional
of the neutron-star literature (quartic + sixth order), with second-order
(Lorentzian) dynamics and one declared sign hypothesis (γ > 0 on the sixth-order
invariant; real neutron matter has γ < 0), the ground state is spontaneously the
maximal biaxial nematic with residual symmetry D₄, A₀ ∝ diag(1, −1, 0). Along
the special axis of this vacuum the massless spectrum is exactly
{helicity ±2 (×2), helicity ±1 (×2)}: **two TT modes with nearly degenerate
speeds (v = 1.078 and 1.083 in house units), verified by projection to be one
100% rotational Goldstone and one 100% superfluid-phase mode.** The mechanism of
the second polarization is, to our knowledge, new: the U(1) phase fluctuation
δA = iεA₀ *inherits the tensor structure of the vacuum*, and diag(a, −a, 0) is
exactly transverse-traceless with respect to its own special axis — **the sound
of the superfluid, dressed by the biaxial order, is the second graviton
polarization.** Both modes are exact Goldstones (zero projection onto the
accidental flat direction), so the masslessness is symmetry-protected at T = 0,
not tuned. We state the debts with the same prominence: the TT purity is exact
only on the special axis (off-axis, one near-TT mode survives across the whole
sky with mean purity 0.951, while the phonon polarization degrades from 0.97 to
0.20 at the equator; TT speed anisotropy 12.6% with toy parameters); two gapless
vector modes remain (dynamically dark in the one collision computed — 0.00%
exactly, by symmetry of that event — but not silenced in general); γ > 0 is a
hypothesis about the medium, not a derivation; and this result does **not** by
itself constitute emergent gravity: within this same program we have published
falsifications showing that naive monometricity fails (v_GW/v_light = 0.774),
that the minimal class cannot reproduce the GW Shapiro delay (refraction bound
β = 2(1 − v²/c₀²) < 4), and that no bulk channel — the TT pair included — can
mediate a universal static 1/r force (von Laue census). What this paper claims
is strictly the spectrum and the mechanism: a condensate whose massless sector,
along its special axis, has exactly the polarization content of linearized
gravitational waves, with the superfluid phonon as one of the two polarizations.

---

## 1. Introduction: the polarization problem

A medium made of displacements — an elastic solid, a fluid — has collective
modes of spin at most 1: longitudinal (P) and transverse (S) sound. This is not
a technicality but a representation-theory fact (a vector field decomposes into
helicities 0, ±1), and it is the reason the first, elastic-medium version of
this program (TCI 1.0) was falsified in its radiation sector and the
falsification published: LIGO's binaries radiate spin-2, tensor-polarized waves
(GW170817/GWTC-3 constrain non-tensor modes decisively [1, 2]), and an
elastic-displacement medium cannot produce them at linear order [Note 7 of the
TCI corpus].

Media with a **tensor order parameter** can. A J = 2 (spin-2) order parameter
has five components, and its collective modes include genuine helicity-±2
objects. The catalogue of known realizations, however, shares one feature: the
spin-2 modes are **gapped**.

- In superfluid ³He-B, the J = 2± "squashing" modes have been measured since
  1980 [3, 4]; Volovik has called them "mass­ive gravitons" since 1990 [5, 6].
- In fractional quantum Hall liquids, the chiral graviton mode — helicity ±2,
  measured in 2024 [7] — is gapped by construction (it is the massive
  fluctuation of Haldane's internal metric).
- In Volovik's emergent-gravity scenarios the graviton-like modes are Higgs
  (amplitude) modes: massive [6].
- In spin nematics, the recently proposed GW analogues [8] involve modes that
  are Goldstones of an *internal* spin symmetry, with the spatial TT structure
  installed by a dictionary rather than carried by the mode itself.

Gravitational-wave phenomenology requires the opposite object: **two** massless
TT modes — the + and × polarizations — and nothing else gapless in the tensor
channel, with masslessness protected (the observational bound is
m_g ≤ 1.27 × 10⁻²³ eV [9]).

During a systematic search (logbook §§2–13) we falsified, with cited cause,
four candidate routes to this object (SL(3) internal shear symmetry; spin
nematics with naive spin-orbit locking; coherent-state SU(3) breaking; the
route through the adjoint), before finding it where the neutron-star
literature had already built most of the machinery: the ³P₂ superfluid — a
J = 2 condensate **with spatial locking of its fabric** (the Cooper pairs carry
J = L + S; rotations act simultaneously on space and on the order parameter).
The phase diagram of that system contains biaxial-nematic phases whose spectrum
had not been computed [10]. We computed it. One sign choice away from neutron
matter, the spectrum is the object sought.

## 2. The model (all choices declared)

**Order parameter.** A(x,t): 3×3 complex symmetric traceless matrix (10 real
components) — the standard ³P₂ order parameter.

**Dynamics (declared choice).** Second-order, Lorentzian:
L = ½|∂ₜA|² − F[A]. This is a *choice of the program* (the medium is postulated
relativistic at the level of its effective dynamics), not the
Gross–Pitaevskii first-order dynamics of cold-atom experiments. All mode
speeds below refer to this convention. With first-order dynamics the counting
of Goldstone modes would change (type-B pairing); none of the claims below are
about GP dynamics.

**Energy functional (textual, from the ³P₂ literature).** Gradients at weak
coupling (K₁ = K₂ = K₃ = K) and the quartic + sextic potential exactly as in
Yasui–Chatterjee–Nitta [10] (their eqs. 17–19):

    F_grad = K ∂ᵢA*_jk ∂ᵢA_jk + 2K (∂_jA*_jk)(∂_lA_lk)
    V      = α t + β q₄ + γ s₆ + ε t⁴
    t  = tr(AA†),   q₄ = t² − tr(A†A†AA),   s₆ = [nine textual sextic terms]

with ε t⁴ a declared regularizer (constant on the quartic-degenerate nematic
family: it does not bias the selection). House parameters: α = −1, β = 1,
γ = +0.15, ε = 0.05, K = 1.

**The one sign hypothesis.** In weak-coupling neutron matter γ < 0. We take
**γ > 0, declared as a hypothesis about the TCI medium** (which is not neutron
matter; the sign of the sextic term is a property of the underlying
micro-model, which is open). Everything below is conditional on this sign.

## 3. Vacua and controls

Minimizing V from random seeds (10-component gradient descent, analytic
Wirtinger gradients validated against numerics — the house rule):

| case | potential | ground state | massless modes | status |
|---|---|---|---|---|
| A | quartic only | any unitary A (V = −0.5 exactly, all seeds) | 5 | control ✓: the classic ³P₂ quartic degeneracy (Sauls–Serene) [11] |
| B | γ < 0 (real neutron matter) | uniaxial nematic (UN), r = −1/2 | 3 (2 angulons + phonon) | **control ✓: reproduces the published physics of ³P₂** (Bedaque–Nicholson) [12] |
| C | **γ > 0 (declared hypothesis)** | **D₄ biaxial nematic, A₀ = a·diag(1,−1,0)**, a = 0.47211, V₀ = −0.264719 | **4 (see §4)** | the result |

Case B is the decisive control: with the sign nature actually chose, our
machinery lands on the phase and the massless counting of the published
literature. (Additional controls passed on the way: the minimal *real* B_ij
model reproduces the uniaxial angulon picture and the accidental SO(5)
quasi-Goldstone structure of spin-2 BECs [13]; see Reproducibility.)

**The D₄-BN vacuum.** A₀ = a·diag(1, −1, 0), purely real after gauge fixing,
eigenvalues (−0.472, 0, +0.472). Its residual group is D₄ *mixing phase and
rotation*: rotating by π/2 about the special axis equals a phase π. In the
spherical basis the condensate lives entirely in ψ₊₂ and ψ₋₂ — the biaxial
nematic is, secretly, a two-component superfluid (this identity is what powers
the mechanism of §4, and further downstream results of the program: the exact
4:1 stiffness ratio and the two decoupled Coulomb sectors of the vortex
electrodynamics).

Broken generators: 3 rotations + U(1) phase = 4. Gapless modes found: 4 —
every massless mode is an exact Goldstone; there is no accidental massless
mode left (the quartic flat direction, the "r-mode", is lifted by the sextic
term to m²_r = 0.24, obeying the closed-form law m²_r = 32γa₀⁴ found later in
the program).

## 4. The central result: the spectrum on the special axis

Quadratic fluctuation spectrum around A₀, propagation k ∥ ẑ (the special axis,
eigenvalue-0 direction), full 10-component Hessian + gradient matrix,
eigenvalues by direct diagonalization:

    ω²(k) branches, k ∥ ẑ (house units):

    helicity ±2 :  v = 1.078   (massless)   ← 100% U(1)-phase mode
    helicity ±2 :  v = 1.083   (massless)   ← 100% rotational Goldstone
    helicity ±1 :  v = 1.463   (massless)
    helicity ±1 :  v = 1.464   (massless)
    r-mode      :  gap m² = 0.24
    amplitude   :  gapped band ω ≈ 2.6–2.8

**Two massless transverse-traceless modes, nearly degenerate in speed, and no
gapless scalar on the axis.** The helicity content is measured with respect to
the propagation direction directly (TT projector on the mode eigenvector), not
through any dictionary.

**Mode composition (the mechanism).** Projecting each TT eigenvector onto the
broken-symmetry directions:

1. **× polarization = the rotational Goldstone.** δA ∝ [L_z, A₀]: the in-plane
   rotation of the biaxial fabric. Projection onto the rotational Goldstone
   direction: 1.00.

2. **+ polarization = the superfluid phonon, dressed.** δA = iεA₀: the global
   U(1) phase fluctuation. Because the fluctuation is *proportional to the
   vacuum itself*, it inherits the tensor structure of A₀ — and
   diag(a, −a, 0) is **exactly transverse-traceless with respect to its own
   special axis**. Projection onto the U(1) direction: 1.00. The sound of the
   superfluid, wearing the biaxial fabric, *is* the second gravitational
   polarization.

Both projections onto the accidental (quartic-flat) direction are 0.00: the
two TT modes are **exact Goldstones**, so their masslessness at T = 0 is
protected by the Goldstone theorem for the spontaneously broken exact
symmetries SO(3) × U(1) — it does not depend on the accidental degeneracy, on
the toy parameters, or on tuning. (This was checked explicitly in the
test-parameter run, where the same two TT modes appear at v ≈ 1.035/1.039
with a different quartic set: the mechanism, not the numbers, is the result.)

A statement of the result as a physical proposition:

> **In a J = 2 superfluid with spatial locking and sextic coefficient γ > 0,
> the spontaneous ground state is the maximal biaxial nematic (residual group
> D₄), and along its special axis the massless spectrum is exactly
> {helicity +2, −2 (one rotational, one of phase), helicity ±1 (×2)} — the two
> polarizations of a gravitational wave, from a condensate, with the
> superfluid phonon as the second polarization — using the textual functional
> of the ³P₂ literature except for one declared sign.**

## 5. Why the masslessness is protected (and the one controversy)

At T = 0 the two TT modes are Goldstones of exact symmetries (spatial
rotations, particle-number U(1)), both spontaneously broken by the D₄-BN
vacuum. There is no fine-tuning: the gap of every non-Goldstone mode is
parametrically set by the potential (the r-mode by 32γa₀⁴, the amplitude band
by the condensate scale).

One controversy in the parent literature must be declared. Leinson [14] argued
that the angulons of ³P₂ acquire an exponentially small thermal gap at T > 0
(a known phenomenon for Goldstones in anisotropic superfluids); at T = 0 his
own calculation *reproduces exactly* the Bedaque–Nicholson dispersions, and
the disagreement at T > 0 remains open in the literature (Bedaque–Nicholson–
Sen: "we do not understand the origin of this discrepancy" [15]; Baldo's 2021
review leans toward Leinson but declares it unsettled [16]). **Our claims are
at T = 0, where both sides of the controversy agree.** We note without
claiming it a potential signature: if Leinson is right, at T > 0 the two
polarizations de-degenerate — the phonon polarization stays gapless (protected
by particle number), the rotational one picks up an exponentially small
thermal gap. An emergent graviton whose two polarizations split with
temperature is a falsifiable structure (against m_g bounds and polarization
tests) that we leave computed-in-principle but unexplored.

## 6. Off the axis: the anisotropy debt, measured

The TT purity is exact only for k along the special axis. We mapped the full
sky (400 directions, same functional, same machinery):

- **One near-TT mode survives everywhere**: best-mode TT purity has mean 0.951
  over the sky, and 100% of directions exceed 0.7. (For comparison, the cyclic
  phase of the same functional — the natural competitor vacuum — gives mean
  0.909 with no clean axis, and was discarded as a gravity candidate on that
  measurement.)
- **The second polarization is the anisotropic one.** Its purity is 0.97 near
  the axis (0–15°) and degrades monotonically to 0.20 at the equator
  (75–90°). This is the phonon: its tensor dress is the vacuum A₀, which is TT
  only with respect to its own axis. At the equator only one clean
  polarization remains.
- **TT-sector speed anisotropy: 12.6%** with these (toy) parameters. The
  discrete-D₄ *structure* of the anisotropy is symmetry-fixed; the percentage
  is not (it moves with the parameters).

This is the program's standing "CMB dragon": a preferred axis of this size is
not cosmologically viable as-is, and we do not hide it. Whether the observable
anisotropy can cancel in *relative* measurements (everything that propagates
sharing the same medium) was tested downstream in the program and the naive
version **failed**: see §8.

## 7. The extra gapless modes (the second debt)

Two helicity-±1 modes remain massless on the axis (v ≈ 1.46). LIGO/Virgo
constrain extra polarizations; these modes must either decouple from
matter/detectors or be gapped by physics beyond this functional. What we can
report is one dynamical fact, not a proof: in the one full nonlinear event
computed in this program (the collapse and merger of a vortex/anti-vortex pair
in the 2D reduction, with 91% of the internal energy radiated), the two vector
channels received **0.00% exactly** — dark by symmetry of that event, with the
radiation emerging entirely in the phase sector plus a massive tail ringing at
the amplitude gap. This is encouraging but event-specific; generic sources
(asymmetric, dipole-active) are precisely where extra polarizations kill
theories (the binary-pulsar dipole test), and that examination is open.

## 8. What this result is NOT (in-program falsifications, published)

This paper claims a spectrum and a mechanism. It does **not** claim emergent
gravity. Within the same program, with the same honesty rules, we have already
published the falsifications that mark the distance:

1. **Naive monometricity is dead (5th tombstone).** If light were another
   Goldstone of the same condensate, GW and light would share speed and
   anisotropy. Computed: v_GW/v_light = 0.774 ≠ 1, and the anisotropies
   *compound* (26.9%) instead of cancelling. GW170817 (|Δv|/c ≲ 10⁻¹⁵) kills
   it. Consequence adopted by the program: light must emerge from the defect
   sector, not the bulk.
2. **The refractive route to gravity is dead for this class (7th tombstone).**
   For the minimal class (canonical kinetic term, polynomial GL, quadratic
   gradients) the response of mode speeds to a local condensate depletion
   obeys β = 2(1 − v²/c₀²) ≤ 2, while the GW Shapiro delay of GW170817
   requires β_TT ≈ 4. The TT pair of this paper does **not**, in this minimal
   class, bend around masses the way gravity does.
3. **No bulk channel mediates Newton (census, von Laue).** The TT pair couples
   to the transverse-traceless part of spatial stress, which integrates to
   zero for any equilibrated source; it is blind to energy density. Static
   universal 1/r attraction cannot come from these modes.

(Full statements, numbers and scripts in the companion working paper "Static
long-range forces in a spin-2 condensate" and in logbook §§22–23, N1–N9.)

The honest reading of the three tombstones plus this paper's result: the
condensate supplies the correct *radiative skeleton* (two massless TT modes
with protected masslessness) while gravity's *static and optical* faces must
come from elsewhere in the system (defect sector / induced dynamics) — or the
program dies there. That is the program's current front, and it is declared.

## 9. Novelty and neighbors (pre-registered claim boundary)

A 14-search sweep (2026-07-17) found no publication of either statement:
(i) "the U(1) phonon of a tensor-ordered condensate inherits the TT structure
of the vacuum and becomes a gapless helicity-±2 mode", or (ii) "phonon +
rotational Goldstone = the two GW polarizations". Confidence: moderate-high.
**A full-text INSPIRE sweep is pending and is declared a precondition to any
public claim of novelty** (block list below).

Neighbors that must always be cited, with the boundary drawn:

- **FQH chiral gravitons** [7]: helicity ±2 measured — but gapped, and of an
  internal metric. Ours are massless Goldstones of spatial+phase symmetries.
- **Volovik** [5, 6]: the emergent-gravity program closest in spirit; his
  graviton candidates are massive (Higgs) modes. The gapless phonon *as a
  polarization* is exactly the piece his catalogue lacks.
- **Spin-2 BEC spectra** [13]: the massless counting of the biaxial phase is
  published; what is claimable is only the tensorial/GW reading of the phase
  mode (its TT dress and helicity), not the counting.
- **Spin-nematic GW analogues** [8]: internal spin-2 Goldstones with a
  dictionary-installed spatial structure; no U(1) phonon in the pair.
- **Zaanen–Beekman elasticity duality**: a different mechanism (we found one
  attributed "massless spin-2" quote we could not verify; flagged).

One technical caution, declared: in the D₄-BN vacuum phase and rotation are
discretely entangled (ψ±₂ → e∓²ⁱᵅ under rotation α; rotating π/2 = phase π).
Our numerical projections separate the two TT modes cleanly (1.00/0.00), but
the stabilizer structure should be handled explicitly when this is
formalized.

## 10. Reproducibility

All scripts in `ift-theory/especulativo/` (branch `desarrollo-fable`), NumPy
only, each with built-in self-tests (analytic gradients validated against
numerics before use):

- `espectro_biaxial_real.py` — minimal real model; controls: uniaxial angulon
  picture, biaxial 3-Goldstone counting, SO(5) quasi-NG structure.
- `espectro_biaxial_complejo.py` — 10-component test-parameter run; first
  appearance of the two TT modes; projection diagnostics.
- `espectro_biaxial_3p2.py` — **the textual functional; cases A/B/C; the
  central spectrum of §4.**
- `anisotropia_mapa.py` — the 400-direction sky map of §6.
- `monometricidad_test.py`, `binaria_del_mar.py` — the in-program
  falsifications and the dark-channel event cited in §7–§8.

Controls that any re-run must reproduce before being believed (house rule):
(a) case B lands on UN with 3 gapless modes [12]; (b) spin-2 BEC counting
[13]; (c) quartic-only degeneracy V = −0.5 from any seed [11]; (d) the
r-mode gap follows m²_r = 32γa₀⁴.

## Pre-publication block list (nothing public before ALL boxes tick)

1. [ ] Full-text INSPIRE novelty sweep (the §9 debt).
2. [ ] In-house adversarial audit of this text (overclaims, claims, citations
       — the same three-audit protocol as the census paper; v0.1 has had NONE).
3. [ ] Transcribe the 8th-order GL terms (1904.11399 eq. 40) and verify the
       D₄ selection survives.
4. [ ] Formalize the stabilizer bookkeeping (the §9 caution).
5. [ ] Explicit OK from Nicolás + channel decision (Zenodo vs arXiv).

## References

[1] B.P. Abbott et al., "GW170817: Observation of Gravitational Waves from a
    Binary Neutron Star Inspiral", PRL 119, 161101 (2017); multimessenger
    ApJL 848, L13 (2017).
[2] Polarization content constraints: PRD 103, 064037 (2021); review
    arXiv:2408.05240; GWTC-3 tests arXiv:2112.06861.
[3] R.W. Giannetta et al., PRL 45, 262 (1980); D.B. Mast et al., PRL 45, 266
    (1980) — observation of the J = 2± modes of ³He-B.
[4] R. Movshovich et al., PRL 61, 1732 (1988) — Zeeman quintet of the J = 2−
    mode.
[5] G.E. Volovik, "Gravitons as Goldstone modes...", Physica B 162, 222
    (1990).
[6] G.E. Volovik, arXiv:2111.07817 — tetrads and analog gravity in ³He;
    massive graviton modes.
[7] J. Liang et al., "Evidence for chiral graviton modes in fractional
    quantum Hall liquids", Nature 628, 78 (2024).
[8] L. Chojnacki, R. Pohle, H. Yan, Y. Akagi, N. Shannon, PRB 109, L220407
    (2024) [arXiv:2310.10078] — gravitational-wave analogues in spin nematics.
[9] LVK Collaboration, GWTC-3 tests of GR, arXiv:2112.06861 —
    m_g ≤ 1.27 × 10⁻²³ eV.
[10] S. Yasui, C. Chatterjee, M. Nitta, PRC 99, 035213 (2019)
    [arXiv:1810.04901] — ³P₂ Ginzburg–Landau functional (eqs. 17–19) and
    biaxial-nematic phases.
[11] J.A. Sauls, J.W. Serene, PRD 17, 1524 (1978) — degeneracy of the ³P₂
    quartic ("any unitary order parameter").
[12] P.F. Bedaque, A.N. Nicholson, PRC 87, 055807 (2013) [arXiv:1307.8183] —
    angulons of the uniaxial ³P₂ phase.
[13] S. Uchino, M. Kobayashi, M. Ueda, PRA 81, 063632 (2010)
    [arXiv:0912.0355]; arXiv:1010.2864 — spectra of spin-2 BEC nematic
    phases; accidental SO(5) quasi-Goldstone.
[14] L.B. Leinson, arXiv:1309.5451 — Comment on angulon masslessness at
    T > 0.
[15] P.F. Bedaque, A.N. Nicholson, S. Sen, PRC 89, 035809 (2014)
    [arXiv:1408.5145].
[16] M. Baldo, Universe 7, 16 (2021) — review of the controversy.

---

**Acknowledgments — AI-assistance statement.** The derivations, the code and
the drafting of this manuscript were developed in collaboration with an AI
system (Claude, Anthropic — working name *Fable*), under the author's
direction. All numerical results are reproducible with the public scripts of
the program (control: case B reproduces the published uniaxial ³P₂ spectrum of
Bedaque–Nicholson). The author takes full responsibility for the content.

---

*Drafted 2026-07-21 within the TCI program's speculative stage, with the AI
assistance declared above. The physics in §§3–7 was computed and controlled on
2026-07-16/17 and is recorded, with its errata, in the program logbook. The
falsifications of §8 are as much a result of the program as §4 — the house
publishes its defeats on the same day and with the same font size as its
victories.*
