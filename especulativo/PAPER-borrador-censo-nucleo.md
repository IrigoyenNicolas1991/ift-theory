# Static long-range forces in a spin-2 condensate: a refraction bound, a symmetry-protected perihelion constraint, and a no-go census for emergent Newtonian gravity

**Nicolás Irigoyen**

*Draft v2 — 2026-07-21 (v1 2026-07-20; v2 incorporates the 17 corrections of the
in-house adversarial audit — see Reproducibility). Internal working paper of the
speculative stage of the Intangible Field Theory (TCI) program. Not submitted
anywhere. Every numbered claim is backed by a script or a closed-form derivation
in the program's logbooks (see Reproducibility). Honesty rules of the house
apply: all assumptions declared, all negative results stated with the same
prominence as positive ones.*

---

## Abstract

We study the static and refractive sector of a spin-2 (J=2) condensate in the
D₄ biaxial-nematic phase, described by the textual ³P₂ Ginzburg–Landau
functional with second-order (Lorentzian) dynamics — a substrate whose two
massless transverse-traceless (TT) modes make it a candidate arena for
emergent-gravity scenarios. We establish three structural results for the
minimal model class (canonical kinetic term, polynomial GL potential, quadratic
gradients) — one proved exactly in a U(1) toy model and verified numerically in
the full functional, two proved by symmetry and by von Laue's theorem.
**(1) Refraction bound:** the response of the tensor (TT) mode speeds to a
local condensate depletion ("vacancy", the model's matter) obeys
**β = 2(1 − v²/c₀²)**, where β is defined by c²(φ) = c²(1−βφ) and c₀ is the
kinetic normalization speed — exact in the U(1) toy model, verified to 0.6–10%
in the full ³P₂ functional at three chemical potentials (the gapless vector
modes do *not* follow the law: β_V ≈ +0.27, K₂₃-gradient-dominated, consistent
with their decoupled "dark" role). Since the multimessenger Shapiro-delay
constraint from GW170817/GRB170817A requires β_TT ≈ 4 for tensor modes, while
the law gives β_TT ≤ 2 with β_TT → 0 as v_TT → c₀, the minimal class is
excluded as the sector realizing the observed (GR-equal) Shapiro delay of
gravitational waves — and with it, the refractive-bulk route to gravity; the
required non-minimality is *located* in the next-order temporal operator
𝒢(t)|∂_t A|². **(2) A Mercury-protecting Z₂:** the real diagonal nematic
sector carries an exact Z₂ symmetry, diag(d₁,d₂,d₃) → (−d₃,−d₂,−d₁), under
which the light quasi-Goldstone (nematic) mode is odd while the D₄-BN vacuum
is invariant. This single symmetry simultaneously (i) forces the cubic
self-coupling of the light mode to vanish — protecting the second-order static
profile (σ = 0, the perihelion constraint that scalar-sector theories must
otherwise tune) — and (ii) gives the light mode exactly zero linear coupling
to amplitude (vacancy) sources: the symmetry that saves Mercury also forbids
the mode from mediating a force. We further obtain the closed-form relation
m²_r = 32γa₀⁴ for the light mode's gap (numerically exact to 8 decimals over
11 values of γ; analytic derivation pending). **(3) No-go census:** channel by
channel, no bulk excitation of the condensate can mediate a universal
attractive 1/r force coupled to total energy: the amplitude channel is
screened at the healing length; the light nematic mode decouples (Z₂); the
superfluid phase sector couples to charge, not energy; and the massless TT
pair couples only to the transverse-traceless part of the *spatial stress*,
which vanishes when integrated over any equilibrated source (von Laue's
theorem), is blind to energy density, and has orientation-dependent sign with
zero angular average. As a positive by-product, the tension of a vortex line
(computed in the standard 2D U(1) reduction — the 3D ring defects of the
D₄-BN remain open) reproduces the equivalence-principle structure
E = E₀(1 − pφ) with **p = 1 + 1/(2 ln(R/ξ))**: within this channel, and if it
is the one that ultimately couples to gravity, universality of free fall
emerges, violated only at a log-suppressed level. Auxiliary results include
the exact second-order vacancy profile φ = A/r − (f₁/4)A²/r² +
3λ₃A²[ln(3mr) + γ_E − 1] and a perihelion bound |λ₃| < 6×10⁻²⁵ m⁻² for light
scalar mediators with a cubic self-interaction. We situate these results
within the known "dynamics gap" of analogue/emergent gravity and state
precisely what a defect-sector mechanism must provide.

---

## 1. Model and conventions

The order parameter is a complex symmetric traceless 3×3 matrix A(x,t)
(spin-2 condensate, 10 real components), with second-order dynamics **declared
as a model assumption** (not Gross–Pitaevskii):

    L = tr|∂_t A|² − F_grad[A] − V(A),        (c₀ = 1 units)

    F_grad = K tr|∇A|² + 2K |∂_j A_jk|²        (weak-coupling K₁=K₂=K₃)
    V = α t + β₄ q₄ + γ s₆ + ε t⁴,   t = tr(AA†)

with q₄ and the nine-term s₆ taken textually from the ³P₂ literature
[Yasui–Chatterjee–Nitta, arXiv:1810.04901, eqs. 17–19], and house parameters
α=−1, β₄=1, γ=+0.15 (γ>0 is a declared hypothesis; in neutron matter γ<0),
ε=0.05, K=1. The weak-coupling gradient choice K₁=K₂=K₃ is itself a declared
input: the mode content of the gradient-dominated sectors (e.g. the vector
modes below) is sensitive to it. For γ>0 the ground state is the D₄ biaxial
nematic (D₄-BN), A₀ = a·diag(1,−1,0)/√2-class with a₀ = 0.4721. Its gapless
spectrum on the symmetry axis contains exactly two TT (helicity ±2) modes —
one rotational Goldstone and one U(1)-phase mode "dressed" into a TT pattern —
plus two vector modes; this two-TT structure is the model's claim to relevance
for gravitational-wave phenomenology and is imported here as given (program
logbook, §14–§17), subject to the same gradient-choice caveat.

Matter is modeled as *vacancy*: a localized deficit of the condensate
sustained by a source, following the program's founding ontology (matter =
deficit of the medium). Finite chemical potential μ is included where stated
(A → A e^{−iμt}).

## 2. The refraction bound β = 2(1 − v²)

**Setup.** Light bending in a medium framework requires the local propagation
speed of the relevant mode to decrease near masses: c²(φ) = c²(1 − βφ), with
φ the fractional local depletion, and observation (1919 eclipse, PPN γ=1)
fixing β = 4. The GW170817/GRB170817A coincidence further constrains the
*difference* of Shapiro delays between gravitational waves and photons
[Abbott et al., ApJL 848 L13 (2017)], at a level we quote as 10⁻⁶–10⁻⁷
(declared debt: the exact numerical bound is pending verification against the
ApJL text; the order of magnitude was confirmed by literature search, and
tighter reanalyses exist). Cassini fixes the photon side to the GR value;
hence **β_TT ≈ 4 is mandatory** for the tensor modes of any substrate theory,
independently of how the photon sector is realized.

**Result.** For the minimal class defined above, expanding around a depleted
background at fixed μ (vacancy parametrization: A_bg = s·A₀, φ = 1−s²) and
extracting mode speeds from the slope of ω²(k²) of the quadratic pencil
(−ω² − 2iμωJ + W(k))u = 0, we find for the TT modes:

    β = − d ln v² / dφ = 2 (1 − v²/c₀²),

exact in the U(1) toy model, and verified to 0.6–10% in the full ³P₂
functional at μ = 0.25, 0.60, 0.90. The gapless vector modes do *not* follow
the law (β_V ≈ +0.27 at μ=0.25, with v_V > c₀; their stiffness is dominated
by the K₂₃ gradient terms). Closed-form derivation (toy): the phonon branch
of the pencil admits the exact small-k expansion W(K) = K(1 − 4u/B) + const,
B = δ + 4u − ε, whence the slope gives c² = 1 − 4u/B and β(k→0) = 2(1−c²).
Two systematic effects were caught by our own controls and are documented:
(i) a finite-k measurement window *underestimates* β through a cross term
8u·εδ·K/B³ that does not cancel in the slope (verified against the closed
form to 4 decimals); (ii) off-shell backgrounds develop a benign tachyonic
offset that cancels exactly in the slope — but at μ ≥ 0.6 this offset expels
the modes from the low-k window (pairing artifacts, discarded), so
measurements there use the high-k window corrected by the closed-form window
bias: at those points the law is tested jointly with its own window
correction, a circularity risk we declare. On-shell (varying μ) the sign of
β is *negative* — a Mexican-hat superfluid refracts away from overdensities —
which independently excludes the naive "denser = slower" picture.

**Consequences.** (i) β_TT ≤ 2 in the entire class; β = 4 is unreachable.
(ii) β_TT → 0 precisely when v_TT → c₀. If one additionally identifies c₀
with c_light (a photon-sector hypothesis, declared), GW170817's speed
constraint (|v_GW/c_light − 1| ≲ 10⁻¹⁵) makes the failure double: correct
speed forces zero refraction. The single failure β_TT ≤ 2 < 4 requires no
such identification. (iii) The escape is located, not speculative: a
non-minimal temporal kinetic function 𝒢(t)|∂_t A|² unlocks arbitrary β — and
this is precisely the operator form (1+4φ)φ̇² that the program's
phenomenological predecessor (TCI 1.0) had to calibrate against the 1919
eclipse. In this framework, **the eclipse measures the Wilson coefficient
𝒢′(t₀)**; its microscopic origin is an open problem stated as such. The
identification of the condensate depletion φ with the phenomenological
gravitational potential assumes the vacancy↔φ dictionary is a pure rescaling;
this dictionary is pending (logbook §N7), and the verdict is robust unless
the mapping carries an exponent < 1/2 (which we consider unlikely but have
not excluded).

A structural bonus, free of calculation: in any superfluid at finite μ the
background that breaks Lorentz invariance is purely temporal (θ̇ = μ), so in
the P(X) effective theory the EOS nonlinearity P″ dresses only the temporal
kinetic term: L₂ = P′[θ̇² − |∇θ|²] + 2μ²P″θ̇². The *location* of the
nonlinearity — which the predecessor theory had to fix against the perihelion
of Mercury (f₁=0, alternatives excluded at ~300σ) — is automatic here.

## 3. The Z₂ that protects Mercury and disarms the mediator

Restricted to real diagonal order parameters A = diag(a,b,−a−b) (the sector
containing the D₄-BN vacuum and its nematic deformations), the full potential
collapses — verified to 2.7×10⁻¹⁵ against the nine-term textual s₆ — to

    V = −p₂ + p₂²/2 + γ(6p₂³ + (8/3)p₃²) + εp₂⁴,
    p₂ = tr A², p₃ = tr A³,

and the identity tr A⁴ = t²/2 holds on this slice, so the quartic cannot
distinguish nematic phases: the entire selection of D₄-BN, and the entire mass
of the light mode, come from γp₃². The mass obeys the closed-form relation

    m²_r = 32 γ a₀⁴    (numerically exact to 8 decimals over 11 values of γ;
                        analytic derivation pending),

confirming that the mode is the parametrically light quasi-Nambu–Goldstone of
the accidental SO(5) of the quartic [Uchino–Kobayashi–Nitta–Ueda, PRL 105,
230406; Turner et al., PRL 98, 190404; Song–Semenoff–Zhou, PRL 98, 160408 —
in cold-atom spin-2 BECs the lifting is by quantum fluctuations; here it is
by the classical sextic, a declared difference of microphysics].

**The symmetry.** The map Z₂: diag(d₁,d₂,d₃) → (−d₃,−d₂,−d₁) leaves V
invariant (all invariants are even), is an isometry of the kinetic metric on
the slice, and fixes the D₄-BN vacuum, while the light (nematic) direction is
*odd*. Two exact consequences follow:

1. **σ = 0 automatically.** Every vertex with an odd number of light legs
   vanishes; in particular λ₃ = 0 exactly, so the second-order static profile
   of the light mode carries no σφ₁² correction. The perihelion constraint
   that scalar-mediator theories must impose by hand is here a symmetry
   consequence.
2. **Zero vacancy charge.** A source coupled to the amplitude t (a vacancy —
   the model's matter) has *exactly zero* projection onto the light mode
   (verified statically and dynamically). The heavy amplitude mode it does
   excite is screened at the healing length (measured Yukawa mass m = 2.39/ξ,
   matching the generalized Hessian eigenvalue to 0.004%).

The same symmetry that rescues the perihelion disarms the mediator: an
elegant and, for the program, sobering trade.

## 4. The no-go census

Combining §2–§3 with two further computations, no bulk channel of the D₄-BN
condensate can mediate the Newtonian interaction V = −G E₁E₂/r (universal,
attractive, coupled to total energy). The census closes every bulk route — by
theorem where one exists (von Laue for the TT channel, the Z₂ for the light
mode), and by explicit model computation for the rest:

| Channel | Static force | Failure mode | Status |
|---|---|---|---|
| Amplitude | Yukawa, range ξ | screened (compressibility) | model computation |
| Light nematic mode | none at linear order | zero source charge | **theorem (Z₂)** |
| U(1) phase(s) | 2D-log / ring-dipole | couples to charge; sign not universal | model computation |
| TT pair (massless) | 1/R anisotropic, zero average | see below | **theorem (von Laue)** |
| Vector pair | — | decoupled from the radiation sector in dynamical simulations (condensate logbook §23/§31) | numerical |
| Tail-overlap (vortex 1/r² density tails) | attractive, universal sign | power law 1/d³ (2D result; steeper in 3D) | model computation |

**The TT channel in detail.** For a massless field carrying only helicity-±2
modes coupled linearly to a localized stress S_ij, the static exchange
potential is (verified by two independent derivations and a numerical
k-integral):

    V(R) = −(1/64π v²R) [2 tr(S¹S²) + t₁t₂ − 5(t₁s₂ + t₂s₁) + 12 n̂S¹S²n̂ + 3 s₁s₂],

with t_a = tr S^a, s_a = n̂·S^a·n̂. Three structural obstructions: (i) the
coupling is blind to energy — an isotropic stress gives V ≡ 0 exactly;
(ii) the sign is orientation-dependent (angular factor spanning [−0.56,
+1.13]) with *zero* average over independent orientations; (iii) **von Laue's
theorem**: for any static, stable, isolated source, ∂_iT_ij = 0 implies
∫T_ij d³x = 0 exactly, so the monopole TT charge of any equilibrated defect
vanishes and the residual interaction falls as 1/R³. The contrast with
general relativity is instructive: Einstein gravity obtains Newton because
the graviton couples to the full T_μν, with the *non-radiative* (constrained)
components h₀₀ seeing T₀₀; a substrate offering only the two propagating TT
modes has nothing with which to build Newton.

**Relation to the literature.** This census is our model's sharp instance of
the known "dynamics gap" of analogue gravity: the analogy is kinematic
[Barceló–Liberati–Visser, Living Rev. Rel. 8:12: the acoustic metric is
related to matter "in a simple algebraic fashion"], induced Einstein–Hilbert
terms are dominated by non-covariant hydrodynamics [Volovik, Phys. Rept. 351,
gr-qc/0005091: "the superfluid liquid is not the best condensed matter for
simulation of Einstein gravity"], and the closest constructive attempt yields
a Poisson equation with Yukawa screening at the healing length
[Girelli–Liberati–Sindoni, PRD 78, 084013: "gravity is of extreme short
range"] — the same wall as our amplitude channel. To our knowledge — and
after a directed search — no derivation exists, from any condensed-matter
substrate, of a universal attractive 1/r force between defects coupled to
their total energy. The gap is real; our contribution is to close every bulk
route in one concrete spin-2 substrate with the sharpest available tool for
each, so that any surviving mechanism must live in the *defect sector*
(topological line defects, their cores, and their network) — a statement we
make precise in §6.

## 5. The equivalence principle from vortex tension

A positive result of the same static sector. The line tension of a vortex,
computed in the standard 2D U(1) reduction (core constant C = 0.3810
reproducing the GP-literature value ln 1.464; the 3D ring defects of the
D₄-BN remain open), is

    T(t_b) = πK t_b [ln(R/ξ(t_b)) + C],    ξ ∝ t_b^{−1/2},

whence the response of a defect's energy to the local condensate level is

    p ≡ d ln T / d ln t_b = 1 + 1/(2 ln(R/ξ)),

numerically 1.1180 vs 1.1165–1.1196 analytic in the tested range. Writing
the local level as t_b = t₀(1−φ), every defect obeys E(x) = E₀(1 − pφ(x))
with a *common* p: the equivalence-principle structure E = mc²e^{−φ} of the
program's phenomenological layer emerges with p → 1, violated only at the
log-suppressed level p − 1 = 1/(2 ln(R/ξ)) — a possible future confrontation
with Eötvös-type bounds *if* this channel is the one that ultimately couples
to gravity. We also verify that the vortex density depression carries a 1/r²
power-law tail (coefficient K/g exact; the amplitude is slaved to the phase
gradient), yielding a universal-sign attractive overlap force ~1/d³ (a 2D
result; steeper in 3D) — close in spirit, wrong in power.

## 6. Auxiliary results and outlook

**Second-order vacancy profile.** For E[φ] = ∫[(1/2)(1+f₁φ)|∇φ|² + ½m²φ² +
λ₃φ³ − Jφ], the exterior profile in the Coulomb window mr ≪ 1 is, exactly:

    φ(r) = A/r − (f₁/4)A²/r² + 3λ₃A²[ln(3mr) + γ_E − 1] + O(A³, A²·mr),

(the constant corrected in-house by adversarial re-derivation: the Yukawa²
source e^{−2mr} shifts ln(mr) → ln(3mr), a Frullani-integral effect verified
to 30 digits). The λ₃ force is *not* suppressed in the deep window
(F_λ₃/F_N = 3λ₃Ar, independent of m), and Mercury's perihelion tolerance
±0.04″/century yields |λ₃| < 6×10⁻²⁵ m⁻². The bound assumes the standard
gravitational calibration of the source (A = GM/c²) and dissolves for
single-scale mediators with λ₃ ~ m²: any mediator with 1/m ≳ 9 AU passes
automatically.

**What a defect-sector mechanism must now provide.** The census leaves one
address for the low-energy world of such substrates: the defect sector. Any
candidate must supply, jointly: a massless (or topologically protected)
collective mode of the defect *network* with universal coupling to energy
(candidate identified: the line-density field, whose masslessness would rest
on the topological conservation of line length, π₂ = 0 — with three explicit
kill criteria stated in the logbook); an emergent U(1) with sources for the
photon — the bosonic routes are closed by a phase dichotomy established in
the condensate logbook (a Motrunich–Senthil-type Coulomb phase of the
condensate's two U(1) sectors *costs one of the two TT polarizations*; only
the fermionic content of defect cores remains); and a common effective metric
(the multimessenger exam). The program's next declared computation — a
Bogoliubov–de Gennes count of chiral branches in a defect tube with the
*relaxed, mixed* core order — carries a pre-registered death criterion for
the whole architecture.

**Honest limitations.** All results are for a specific GL functional with
declared parameters, the weak-coupling gradient choice, and second-order
dynamics; γ > 0 is a hypothesis; the refraction law is proved exactly in the
U(1) toy and verified numerically (0.6–10%, three chemical potentials) in the
full functional, not proved as a general theorem of the class — and the
gapless vector modes explicitly do not obey it; the p ≈ 1 dictionary is
computed in the 2D U(1) reduction, not yet for the 3D ring defects of the
D₄-BN; the vacancy↔φ dictionary is pending; and nothing here claims that
nature *is* such a condensate — these are structure results for a program
that remains speculative and is documented as such, falsifications included.

## Reproducibility

Every claim maps to a script or logbook section in the public repository
(github.com/IrigoyenNicolas1991/ift-theory, branch `desarrollo-fable`, folder
`especulativo/`; the supporting material was published with the program
owner's explicit sign-off on 2026-07-20): refraction law and window bias —
`nucleo_beta4.py`, logbook N §N5–N6; Z₂, closed-form mass relation, vacancy
decoupling — logbook N §N8; TT exchange, von Laue, census — logbook N §N9;
vortex tension p — logbook N §N9.2; second-order profile and Mercury bound —
logbook N §N8.1; GL functional and conventions — `NUCLEO-TCI2-lagrangiano.md`.
Adversarial verification protocol (independent re-derivations, refutation
agents, pre-registered kill criteria) documented throughout; the in-house
errata are confessed with dates in the logbooks (twelve program-wide at the
time of writing; three in the nucleus campaign alone). This draft itself
passed one adversarial audit (overclaim hunt, 17 corrections applied in v2);
two further audits (claim-by-claim numerics; external citations) were
interrupted by compute limits and remain **declared pending** for v3 — the
GW170817 Δγ exact bound and the external textual quotes should be re-verified
against the primary sources before any submission.

**Acknowledgments — AI-assistance statement.** The derivations, the code and
the drafting of this manuscript were developed in collaboration with an AI
system (Claude, Anthropic — working name *Fable*), under the author's
direction. All numerical results are reproducible with the public scripts of
the program, which verify the exact general-relativity values as controls (see
Reproducibility). The author takes full responsibility for the content.

*Correspondence: irigoyennicolas1991@gmail.com*
