# Segundo correo a Pilo (CC Comelli) — enviado 2026-09-02

**Contexto.** El hilo (Gmail 19f85b4233d39528) estaba quieto desde nuestra
respuesta del 25/7 (5 semanas y media; agosto italiano). El plan confirmado por
Nico el 30/7 era UN solo correo juntando (a) la nota missing-row prometida
"in the coming weeks", (b) las dos erratas de BCP §8 (confirmadas por la
campaña del 27/7, párrafo listo en `CIERRE-BLOCKLIST-2026-07-27.md` §8), y
(c) el re-flote suave del permiso de cita. El gate era la lectura final de
Nico; el 2/9 Nico decidió explícitamente **enviar sin esperar su lectura**
("quiero que lo mandes con el paper... manda el mail igual") y leer el paper
en paralelo. Envió Fable desde la casilla de Nico vía el conector de Gmail.

**El paper compartido.** PDF generado desde el .md v0.7
(`especulativo/PAPER-missing-row-UXY-draft-v0.7.pdf`, commit acc784c) — el
draft se presenta como tal en el propio correo ("still a draft — a final
read-through is in progress on my side"). Sin adjunto (limitación técnica del
conector con archivos grandes): va por link directo al PDF en GitHub, escrito
como texto plano para evitar el mangler de URLs de Gmail que afectó a los dos
correos anteriores.

**Threading.** Reply al mensaje 19f9bd780ce2bfd6 (nuestro del 25/7);
message id del enviado: 1a062af81aee4c1d. To: luigi.pilo@aquila.infn.it,
CC: comelli@fe.infn.it.

**Contenido honesto clave**: el correo declara de frente que la firma de
frame dragging apantallado anunciada en el resumen del 25/7 quedó SUPRIMIDA
por el teorema de superselección del propio paper (regla de la casa: la
derrota con la misma prominencia). Las erratas §8 van con el párrafo del
refutador casi verbatim + numeración arXiv v2 declarada + puntero al script
público (`erratas-bcp-s8/`).

---

## Texto enviado (verbatim)

Dear Luigi,

I hope you had a good summer break. Three things — the note I promised, two
further (minor) typos we believe we found in Sec. VIII of 1603.02956, and a
small pending question.

1. The note. The draft is here (PDF, ~25 pages, with the full reproducibility
table; it took longer than the "coming weeks" I wrote — the audit passes kept
finding things worth fixing, including one formula of our own, refuted and
corrected in place):

https://github.com/IrigoyenNicolas1991/ift-theory/blob/desarrollo-fable/especulativo/PAPER-missing-row-UXY-draft-v0.7.pdf

(The Markdown source and all scripts are in the same public folder,
especulativo/. Still a draft — a final read-through is in progress on my
side; comments, critical ones especially, are very welcome.)

One honest update with respect to the summary in my last message: the
screened frame-dragging branch I described there as the falsifiable signature
is now suppressed — by the paper's own main theorem. The residual symmetry
Φᵃ → Φᵃ + ξᵃ(Φ⃗) turns out to have a Noether current with no spatial
components (P_aⁱ = 0, an exact off-shell identity of √−g U(X,Y) + EH,
verified four independent ways), so the internal charge density is frozen
pointwise: the relaxed (screened) and co-rotating branches are disconnected
superselection sectors, and cosmological initial conditions populate the
co-rotating one universally. The phase therefore predicts GR gravitomagnetism
outright, and the LARES-2 numbers I mentioned become counterfactuals of an
unpopulated branch. The two-branch structure and the suppressed signature are
kept on record with the same prominence as the wins. The corrected weights of
(7.6)–(7.7) enter the exclusion lemma of §5 (on-shell m₁² = 2K_T,
m₂² = −2G_T: protecting the massless graviton is switching off the medium's
shear phonons).

2. Two further typos, closely related to each other, this time in Sec. VIII
("Gravitational waves") — Eqs. (8.17)–(8.18) in the arXiv v2 numbering.
Substituting N(t) = a(t) in the quadratic tensor Lagrangian of Sec. VII,
L = (M_pl²/2)[(a³/N) χ′ᵢⱼχ′ᵢⱼ + N a (2M₂² − k²) χᵢⱼχᵢⱼ], the Fourier-space
action in Sec. VIII should read a²[χ′ᵢⱼχ′ᵢⱼ + (2M₂² − k²)χᵢⱼχᵢⱼ], whereas the
printed equation has (2M₂² + k²); as printed, the M₂² → 0 limit would not
reproduce standard wave propagation. Likewise, the propagation equation that
follows should then be χ″ᵢⱼ + 2ℋχ′ᵢⱼ + (k² − 2M₂²)χᵢⱼ = 0, while the printed
version has (k² − M₂²), i.e. half the mass term. We re-derived the tensor
Lagrangian directly from your action S = M_pl²∫√−g R + ∫√−g U with the
definitions of Table I, and we recover exactly your Sec. VII expression
(2M₂² − k²), so the Lagrangian itself appears correct and only the two
Sec. VIII equations seem affected. Reassuringly, both corrected expressions
also match the tensor sector of your later paper JCAP 09 (2017) 036, where
M₂^there = −2a²M₂²^here via its Appendix A. The verification script
(symbolic, ~30 checks) is public in the repository
(especulativo/campana-m2/erratas-bcp-s8/), and I would be happy to send a
short self-contained derivation if useful. None of this affects our row
(M₂² ≡ 0 identically there).

3. The pending question from my last message, at your convenience: may I cite
your July confirmation as "L. Pilo, private communication (2026)"? The draft
currently paraphrases it, marked as pending permission (§2). If you would
rather I not, I will simply present the printed-vs-derived discrepancy as
before.

No hurry with any of this, of course.

Kind regards,

Nicolás

---

## Qué esperar / próximos pasos

- **Si responde con permiso de cita** → §2 y scoreboard del paper pasan a
  referencia formal "L. Pilo, private communication (2026)"; momento natural
  para el pedido de endorsement arXiv (estrategia en memoria).
- **Si confirma las erratas §8** → misma mecánica que la primera: se declara
  en el paper (§9/Declared limits ya las menciona como confirmadas por
  nuestra campaña; sumaría la confirmación de autor).
- **Si comenta la nota** → oro puro, se procesa con Nico.
- **Si silencio** → nada de pings; la nota ya está entregada y el paper no
  depende de Pilo (la lectura final de Nico sigue siendo el gate de
  submission).
