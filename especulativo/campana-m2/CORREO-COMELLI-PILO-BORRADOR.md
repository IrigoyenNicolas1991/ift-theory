# Correo a Comelli/Pilo — presunta errata en BCP (7.6)–(7.7)

**Estado: ✉️ ENVIADO por Nicolás el 2026-07-21** (desde irigoyennicolas1991@gmail.com,
a comelli@fe.infn.it y luigi.pilo@aquila.infn.it — primer contacto técnico con los
autores del diccionario). Fase: espera de respuesta; no insistir. Si responden:
contestar juntos; si confirman la errata, el paper puede citar "confirmed by the
authors (private communication)" y es el momento natural para el pedido de
endorsement de arXiv (estrategia registrada en la memoria del proyecto). La firma
salió sin línea de email (remitente visible en Gmail). Chequeos hechos el mismo día:
(1) direcciones verificadas en fuente primaria — **comelli@fe.infn.it** (PDF de su
paper arXiv:2501.07968, ene-2025; afiliación real: **INFN Ferrara**, NO Padova como
decía este borrador) y **luigi.pilo@aquila.infn.it** (PDF de arXiv:2208.00075);
(2) título verificado contra arXiv abs/1603.02956: "Massive and modified gravity
as self-gravitating media", Phys. Rev. D 94, 124023 (2016) ✓. Registro de la casa:
la evidencia técnica está en `VERIFICACION-BCP-2026-07-21.md` (5 vías, panel
adversarial incluido).

Política aplicada: consulta técnica puntual y humilde — SOLO la errata; la fila
U(X,Y) aparece en una sola frase de contexto, sin reclamos. Declaración de IA:
una línea sobria al final, ni tema central ni ocultamiento (política de autoría
2026-07-21).

---

**Para:** D. Comelli (INFN Ferrara) — comelli@fe.infn.it — y L. Pilo (Università
dell'Aquila / INFN) — luigi.pilo@aquila.infn.it *(verificadas 2026-07-21 en los
PDFs de sus papers recientes)*
**Asunto:** Possible misprint in the mass-parameter weights of PRD 94, 124023
(arXiv:1603.02956), Eqs. (7.6)–(7.7)

---

Dear Dr. Comelli and Dr. Pilo,

I am writing about your paper "Massive and modified gravity as self-gravitating
media" (PRD 94, 124023; arXiv:1603.02956), whose medium/mass dictionary I have
been using and which I found extremely useful. While rederiving the full
dictionary between the medium Lagrangian and the mass parameters of Eq. (7.3)
(unitary gauge, flat background, a = N = 1), I consistently obtain weights that
differ from the printed Eqs. (7.6)–(7.7), and I believe the printed versions may
contain a misprint:

- in m₁²: I obtain −2n·U_τₙ and +2·U_yₙ (flat in n, including n = 0), whereas
  the printed weights appear with the τ/y roles interchanged (and the printed
  2n·U_yₙ weight annihilates the n = 0 term that the printed sum explicitly
  includes);
- in m₂²: I obtain −2n(n+1)·U_τₙ, whereas the printed weight is −4(n+1)·U_τₙ.

My m₀² matches your Eq. (7.5) exactly, as do all isotropy consistency checks.

Four independent cross-checks select the weights above:

1. A Goldstone-route derivation (flat space, no unitary gauge): the phonon
   Lagrangian equals the mass Lagrangian under h → ∂π term by term (zero
   remainder, up to total derivatives) only with these weights.
2. Internal consistency: the tensor-sector result of your Eq. (7.21),
   M₂² = Σ n²·U_τₙ, is compatible with these weights and, as far as I can see,
   not with the printed (7.7).
3. The appendices of later papers of your group (arXiv:1704.00322, 1712.04827,
   1907.11784) appear to use precisely these weights; I could not find a
   published erratum for PRD 94, 124023 (the equations are unchanged between v1
   and v2 on arXiv).
4. An exact symbolic rederivation (SymPy, exact inverse metric on directed
   configurations, no truncation) and an independent blind refutation attempt
   reproduce the same weights.

The scripts run in seconds and are public in my repository
(https://github.com/IrigoyenNicolas1991/ift-theory, folder
`especulativo/campana-m2/`); I would be happy to send a short self-contained
note with the derivation. Could you confirm whether (7.6)–(7.7) contain a
misprint, or point out what I am missing?

For context only: this came up within an independent research program studying
which media realize the Lorentz-violating phases of Dubovsky's hep-th/0409124 —
in particular the row of your Table 2 corresponding to unrestricted internal
spatial diffeomorphisms, U(X,Y) — which is what led me to recompute the
dictionary. None of that affects the question above (U(X,Y) does not involve
τₙ or yₙ).

Kind regards,

Nicolás Irigoyen
Independent researcher, La Plata, Argentina
nicolasirigoyen@teoriadelcampointangible.org

P.S. In the interest of transparency: the derivations and code behind this
check were developed in collaboration with an AI system (Claude, Anthropic),
under my direction; every result above is reproducible with the public scripts
linked, which verify your Eq. (7.5) and the isotropy identities as controls.
