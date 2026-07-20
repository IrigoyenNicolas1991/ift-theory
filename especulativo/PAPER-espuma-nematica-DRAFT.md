# Inverted dipolar order: the laminar nematic ground state of vortex-ring arrays

**Nicolás Irigoyen** (with Fable/Claude, AI research collaborator)
*Draft v0.9 — 2026-07-20. Working document on the `desarrollo-fable` branch;
not yet submitted anywhere. Comments welcome.*

---

## Abstract

Quantized vortex rings in an ideal fluid interact, at long range, through a
dipole–dipole energy whose sign is inverted, term by term, with respect to
the interaction of permanent magnetic dipoles. The inversion is elementary
but consequential: the interaction energy of vortices at fixed circulation
is the *true cross kinetic energy* of the flow (Neumann's formula), which
carries the sign of the mutual-inductance form +M I₁I₂ rather than that of
the magnetostatic potential U = −m·B, because Kelvin's theorem fixes the
circulations with no external "battery". As a result, the classical
ground-state problem of dipolar lattices (Luttinger–Tisza 1946) is turned
upside down: the configuration that *maximizes* the standard dipolar energy
becomes the ground state of a vortex-ring array. We solve the resulting
problem in three steps. (1) We compute the lattice Fourier tensor J(k) by
Ewald summation, certified against published constants to 4–5 digits
(simple-cubic antiferromagnetic constant −2.67675 μ²/a³; type-A maximal
eigenvalue 9.6874; longitudinal Lorentz limit 8π/3). (2) With the inverted
sign, the Luttinger–Tisza bound is *saturated* by a commensurate laminar
mode (k* at the zone boundary, polarization parallel to k*): on simple-cubic
and tetragonal lattices, no orientational configuration — multi-k,
non-collinear, or glassy — can undercut layered, antialigned sheets of
co-oriented rings. The excluded uniform (k → 0) modes obey a shape-
independent bound 8π/3 < 9.687 that is rigorous precisely for this sign.
(3) At packing distances (d ~ 2–3 ring radii), where the point-dipole model
is unreliable, we evaluate the exact Neumann/mutual-inductance integral:
the in-plane bond is enhanced (×2.16 at d = 2.2R) and the stacking bond
suppressed (×0.575 at d = 2R), so the winning sheets are *triangular*
(a honeycomb-packed layer of touching rings), deeper than square packing by
~30%, while the stacking registry is quasi-degenerate — a stacking-polytype
softness analogous to FCC/HCP. In every regime computed the emergent order
is purely nematic (director order parameter S = 1) with vanishing vector
order (P ≈ 0): arrays of vortex rings spontaneously build a *headless*
axis, never a net arrow. We state explicitly the assumptions under which
the static problem is well posed (topologically frozen ring sizes à la
vorton, suppressed reconnections, rings at rest) and the open dynamical
questions (tilt/precession spectrum, reconnection barrier).

## 1. Introduction

The ground states of point dipoles on lattices form a classical chapter of
condensed-matter theory: Luttinger and Tisza (1946) diagonalized the
dipolar quadratic form on cubic lattices and found, e.g., the columnar
antiferromagnet on the simple-cubic lattice, with ground-state constant
−2.676 μ²/a³ [LT46, Johnston16, Schonke20]. The *maximum*-energy states of
the same problem — laminar, side-by-side arrangements — were recently
computed explicitly [NatSciRep20]. They are usually a curiosity: no
magnetic system wants them.

Hydrodynamics supplies a system that does. The interaction energy of two
vortex filaments at fixed circulations Γ₁, Γ₂ in an ideal incompressible
fluid is Neumann's integral

> E_int = (ρ Γ₁Γ₂ / 4π) ∮∮ dl₁·dl₂ / |r₁₂|,   (1)

the cross term of the (positive-definite) kinetic energy ρ∫v₁·v₂ dV
[Saffman92; transcribed in Talalov22 §3; equivalent vorticity form in
Ruban00, footnote 1; Dyson's coaxial-ring model, verified against the
Maxwell elliptic integral, in Meleshko10]. Formula (1) is *identical* to
the mutual-inductance energy of current loops under ρ ↔ μ₀, Γ ↔ I — with
the co-energy sign +M I₁I₂. For circuits, that sign requires a battery
holding the currents fixed; for vortices, Kelvin's circulation theorem
plays the battery at zero cost. In the far field, with ring impulse
P = ρΓπR² n̂,

> E_int = (1/4πρ) [ 3(d̂·P₁)(d̂·P₂) − P₁·P₂ ] / d³,   (2)

term-by-term the *opposite* of the magnetostatic dipole potential
[Ruban00, eq. 25; the d ≫ R limit of the elliptic formula agrees
quantitatively]. Consequently: coaxial co-oriented rings *raise* the energy
(+2C/d³), antialigned stacking lowers it (−2C/d³), and side-by-side
co-oriented rings lower it (−C/d³) — a magnet's preferences, inverted. To
our knowledge this inversion, while implicit in the formulas of [Ruban00],
has not been exploited as a route to an ordered phase.

This paper treats the resulting statics seriously: *if* a population of
identical vortex rings is held at fixed sizes and positions-on-a-lattice
(assumptions spelled out in §5), what orientational order does the energy
select?

## 2. The sign theorem and the monopole theorem

**Sign.** E_int of (1) is the cross term of a positive-definite quadratic
form; no convention can flip it while the circulations are fixed. The
dipolar limit (2) then fixes the pair hierarchy quoted above. We stress the
vocabulary: (1) is the *true kinetic energy* of the flow, not a co-energy
bookkeeping device; minimizing it at fixed Γ with a dissipative channel
(phonon emission [KozikSvistunov05]) is legitimate relaxational dynamics —
no Legendre trap is involved.

**Monopole.** Since ∇·ω = 0, any localized vorticity distribution has
∫ω dV = 0: the far field of a ring *starts* at the dipole. There is no
Coulombic 1/d² sector in a ring array; (2) is the leading term.

## 3. Luttinger–Tisza with the inverted sign: the laminar theorem

For identical point dipoles n_i (|n_i| = 1) on a Bravais lattice with the
vortex sign, E/N = −(1/2N) Σ n_i^T T(R_ij) n_j with
T(R) = (1 − 3R̂R̂)/R³. Fourier transforming, every configuration is a
weighted average of eigenvalues of J(k) = Σ_{R≠0} T(R) e^{ik·R}
(weak bound, [LyonsKaplan60]); a commensurate single-k mode with a real
eigenvector and |n_i| = 1 at every site saturates the bound and is the
*exact* ground state among all orientational configurations on that
lattice.

We computed J(k) by Ewald summation (real-space B, C functions; reciprocal
sum; self term — formulas as in [WangHolm01, Cerda08]). Certification of
the code against the literature:

| Quantity | This work | Published |
|---|---|---|
| SC magnetic ground state (columnar AFM) | −2.67675 μ²/a³ | −2.67675 [LT46/Johnston16]; −2.67679(2) [Schonke20] |
| SC maximal (type-A laminar) eigenvalue | 9.68721 | 9.6874 [Johnston16]; 9.6895 [NatSciRep20] |
| Longitudinal k→0 (Lorentz) limit | 8.3775 | 8π/3 = 8.37758 |
| Ewald-parameter independence | 6 digits | — |

**Result.** Scanning the Brillouin zone on simple-cubic and tetragonal
lattices (grids 14³/12³, shifted to avoid k = 0, 3-step refinement), the
maximal eigenvalue for the vortex sign sits at the commensurate zone-
boundary point k* = (0,0,½) (fractions of the reciprocal basis) with
polarization ε ∥ k*, is isolated (quadratic decrease verified in 5
directions × 2 scales × 3 aspect ratios), and satisfies the strong
constraint. Hence, on these lattices:

> **The ground state is the laminar antialigned crystal — sheets of
> co-oriented rings, alternating orientation sheet by sheet. No multi-k,
> non-collinear or glassy configuration can undercut it.**

It is a uniform *nematic*: director ±ẑ everywhere (S = 1), zero net vector
order (P = 0). Uniform (k → 0) states are excluded rigorously for this
sign: any uniform mode has eigenvalue 8π/3 − N_α ≤ 8π/3 = 8.3776 < 9.687
for *any* sample shape and boundary condition (with the standard magnetic
sign this exclusion would fail — the ferromagnet competes through shape
terms; the rigor is sign-specific). FCC and BCC are eliminated by the
weak bound alone: sup_k λ ≤ 8.378 < 9.687 at equal density, without
needing saturation. (HCP and the remaining Bravais classes are pending as
bounds; see §5.)

In open clusters (N ≈ 150–500, gradient descent with annealing) the same
model produces strong *local* nematic order but a multi-domain mosaic —
surface closure domains, as in real magnets. The bulk theorem shows the
frustration is not intrinsic.

## 4. Exact Neumann interaction at packing distance: triangular sheets and polytype softness

At d ~ 2–3R the point dipole fails quantitatively: evaluating (1) exactly
(spectrally accurate quadrature, equal to the Maxwell elliptic form at
10⁻¹⁶; far field → (2)), the exact/dipole ratio is 0.575 for coaxial pairs
at d = 2R and 2.16 for coplanar pairs at d = 2.2R — the near field
*enhances* the in-plane bond and *suppresses* the stacking bond. Comparing
laminar structures at fixed density (volume per ring v_c = 9–16 R³, hard
core a ≥ 2.05R in-plane):

| Structure | E/ring (v_c = 12) |
|---|---|
| square sheets, aligned stacking | −0.795 |
| square sheets, offset (bct-like) | −0.796 |
| **triangular sheets, aligned** | **−1.077** |
| triangular sheets, offset (HCP-like) | −1.073 |

Triangular (honeycomb-packed) sheets win by ~30%; the in-plane spacing
saturates the hard core (rings touch side by side); and the stacking
registry is quasi-degenerate (gaps 10⁻³–10⁻⁴, order swapping with
density): a stacking-polytype softness. The robust conclusions — laminar
family, headless nematic axis, P = 0 — are independent of the registry.

## 5. Assumptions, limitations, and open dynamics

The statics above is well posed under three explicit hypotheses, none
proven here: **(H1)** ring radii are frozen — otherwise phonon emission at
fixed Γ shrinks rings to annihilation ([KozikSvistunov03]; vortex-collider
experiments [Nature598]) and the energy minimum at fixed circulation is
the ring-free vacuum. A concrete freezing mechanism exists in
two-component condensates: vortons, rings whose core traps a second
condensed component with winding N and particle number Q, E(R) = 2πμR +
N²Q/R², stable at rest [MetlitskiZhitnitsky03]; stability windows favor
"fat" rings [GaraudRaduVolkov13, BattyeCotterill21]. **(H2)** reconnections
are suppressed (note that touching co-oriented in-plane neighbours present
antiparallel core segments — the canonical reconnection geometry; the
barrier for charged cores is an open calculation). **(H3)** rings are at
rest (fat rings kill the self-propulsion logarithm; mutual induction in
the lattice is an alternative). Orientational relaxation is gyroscopic —
dq/dt = (J − γD)∇E with Kirchhoff's symplectic structure — and the
dissipative tensor for the tilt mode is not derived here; the
precession-with-drag analogy (LLG; spiral-out of trapped vortices
[FedichevShlyapnikov99]) makes relaxation plausible, not proven. The full
dynamical spectrum of the laminar crystal (tilt + lattice phonons) is the
natural next calculation, and would also yield the effective elastic
medium that the ordered foam constitutes.

## 6. Discussion

The columnar↔laminar map under sign inversion connects two published
extremes of the dipolar lattice problem [LT46, NatSciRep20] through a
physical system that genuinely lives on the inverted side. Three features
seem noteworthy. (i) The order is nematic by construction: ring arrays
build a macroscopic J = 2 order parameter with strictly zero J = 1
moment, in every regime we computed. (ii) The near field reinforces the
laminar family (contrary to the usual situation where near-field
corrections destabilize dipolar order), selecting close-packed triangular
sheets. (iii) The stacking softness suggests polytypism and stacking
entropy in any realization. Candidate realizations — rotating multi-
component condensates hosting vorton-like rings, or driven quantum fluids
with long-lived ring populations — face H1–H3 as the real obstacles.
A speculative cosmological motivation (a substrate for emergent-medium
models of gravity) is developed elsewhere and is not needed for any
result above.

## References

[LT46] J.M. Luttinger, L. Tisza, Phys. Rev. 70, 954 (1946); erratum 72, 257.
[LyonsKaplan60] D.H. Lyons, T.A. Kaplan, Phys. Rev. 120, 1580 (1960).
[Johnston16] D.C. Johnston, Phys. Rev. B 93, 014421 (2016); arXiv:1505.00498.
[Schonke20] J. Schönke et al., Sci. Rep. 10, 19153 (2020).
[NatSciRep20] "Minimum and maximum energy for crystals of magnetic dipoles", Sci. Rep. 10, 18781 (2020).
[GrohDietrich01] B. Groh, S. Dietrich, Phys. Rev. E 63, 021203 (2001).
[Saffman92] P.G. Saffman, *Vortex Dynamics*, CUP (1992).
[Talalov22] S. Talalov, arXiv:2112.04859.
[Ruban00] V.P. Ruban, arXiv:physics/0001070.
[Meleshko10] V.V. Meleshko, Theor. Comput. Fluid Dyn. 24, 403 (2010).
[FukumotoMoffatt08] Y. Fukumoto, H.K. Moffatt, Physica D 237, 271 (2008).
[CampbellZiff79] L.J. Campbell, R.M. Ziff, Phys. Rev. B 20, 1886 (1979).
[WangHolm01] Z. Wang, C. Holm, J. Chem. Phys. 115, 6351 (2001).
[Cerda08] J.J. Cerdà et al., J. Chem. Phys. 129, 234104 (2008).
[deLeeuw80] S.W. de Leeuw, J.W. Perram, E.R. Smith, Proc. R. Soc. A 373, 27 & 57 (1980).
[KozikSvistunov05] E. Kozik, B. Svistunov, cond-mat/0505020; [KozikSvistunov03] cond-mat/0308193.
[Nature598] Vortex collider, Nature 598 (2021).
[MetlitskiZhitnitsky03] M.A. Metlitski, A.R. Zhitnitsky, cond-mat/0307559.
[GaraudRaduVolkov13] J. Garaud, E. Radu, M.S. Volkov, arXiv:1303.3044.
[BattyeCotterill21] R.A. Battye, S.J. Cotterill, PRL 127, 241601 (2021); JHEP 04 (2022) 005.
[FedichevShlyapnikov99] P.O. Fedichev, G.V. Shlyapnikov, PRA 60, R1779 (1999).
[Tkachenko66] V.K. Tkachenko, Sov. Phys. JETP 22, 1282; 23, 1049 (1966); 29, 945 (1969).

---

*Draft status: pending before submission — HCP/remaining-Bravais bounds;
INSPIRE/ADS novelty sweep on the inversion; decision on venue. All code
(Ewald-certified, with control tables) in `especulativo/sotano_*.py` of the
ift-theory repository.*
