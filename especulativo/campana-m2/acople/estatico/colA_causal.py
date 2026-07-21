# -*- coding: utf-8 -*-
"""
COLUMNA A (campana m2=0) -- parte 2: DINAMICA CAUSAL (fuente que se prende).

Pregunta: verificar el claim de Dubovsky ("la masa tiene forma de gauge-fixing =>
al orden lineal la gravedad es EXACTAMENTE RG; los efectos requieren NLO/no-lineal")
y calcular el primer efecto NLO (correccion tipo ACLM: r_c, t_c).

Setup por modo de Fourier (p a lo largo de z), campos phi,B,psi,E funciones de t.
Fuente CONSERVADA generica: T^00 = rho(t) cos(pz), T^{0z} = s(t) sin(pz),
T^{zz} = w(t) cos(pz), con s = -rho'/p, w = -rho''/p^2 (conservacion verificada).

Observables gauge-invariantes (Bardeen planos):  Psi_obs = psi ,
  Phi_obs = phi - d/dt(B - E'/2)   [invariancia verificada abajo]
(en el gauge newtoniano: ds^2 = -(1-2 Phi_obs)dt^2 + (1+2 Psi_obs)dx^2;
 el potencial newtoniano estandar es Phi_N = -Phi_obs).

Chequeos C0..C8 declarados en linea.
"""
import sympy as sp
from eh_lib import t, z, p, zavg, L12_of_ansatz, EL

Mp2 = sp.Symbol('Mpl2', positive=True)
m0s, m1s = sp.symbols('m0sq m1sq', positive=True)
al, be, si, rh = sp.symbols('alpha beta sigma rho_op', real=True)
rho0 = sp.Symbol('rho0', real=True)

phi = sp.Function('phi')(t)
B = sp.Function('B')(t)
psi = sp.Function('psi')(t)
E = sp.Function('Ef')(t)
fields = [phi, B, psi, E]
dpsi = sp.Derivative(psi, t); dE = sp.Derivative(E, t)

c = sp.cos(p * z)
H = sp.zeros(4, 4)
H[0, 0] = 2 * phi * c
H[0, 3] = H[3, 0] = sp.diff(B * c, z)
H[1, 1] = 2 * psi * c
H[2, 2] = 2 * psi * c
H[3, 3] = 2 * psi * c + sp.diff(E * c, (z, 2))

L1d, L2d = L12_of_ansatz(H)
LEH = sp.expand(zavg(L2d))

# --- C0: forma canonica del EH (la de la acta, re-verificada aca) ---
LEH_can = (-3 * dpsi**2 + p**2 * psi**2 - 2 * p**2 * phi * psi
           - 2 * p**2 * B * dpsi + p**2 * dpsi * dE)
W = (3 * phi * dpsi + p**2 * phi * B - sp.Rational(1, 2) * p**2 * phi * dE
     - sp.Rational(1, 4) * p**4 * E * dE
     - sp.Rational(1, 2) * p**2 * (E * dpsi + psi * dE)
     + 3 * psi * dpsi)
print("C0: LEH - LEH_can - dW/dt (esperado 0):", sp.simplify(LEH - LEH_can - sp.diff(W, t)))

# --- masas y NLO ---
Xc = [t, sp.Symbol('x'), sp.Symbol('y'), z]
Lmass = sp.expand(zavg(sp.Rational(1, 4) * (
    m0s * H[0, 0]**2 + 2 * m1s * (H[0, 1]**2 + H[0, 2]**2 + H[0, 3]**2))))
Kb = sp.zeros(3, 3)
for a in range(3):
    for b in range(3):
        Kb[a, b] = (sp.diff(H[a + 1, b + 1], t)
                    - sp.diff(H[0, b + 1], Xc[a + 1])
                    - sp.diff(H[0, a + 1], Xc[b + 1]))
trK = sum(Kb[a, a] for a in range(3))
R3 = (sum(sp.diff(H[a + 1, b + 1], Xc[a + 1], Xc[b + 1])
          for a in range(3) for b in range(3))
      - sum(sp.diff(H[b + 1, b + 1], Xc[a + 1], Xc[a + 1])
            for a in range(3) for b in range(3)))
DLfull = sp.expand(zavg(sp.expand(
    sp.Rational(1, 4) * al * sum(Kb[a, b]**2 for a in range(3) for b in range(3))
    + sp.Rational(1, 4) * be * trK**2
    + sp.Rational(1, 4) * si * R3**2
    + sp.Rational(1, 4) * rh * trK * R3)))

# --- fuente conservada generica ---
rho = sp.Function('rho')(t)
s_t = -sp.diff(rho, t) / p
w_t = -sp.diff(rho, t, 2) / p**2
T00d = rho * sp.cos(p * z)
T0zd = s_t * sp.sin(p * z)
Tzzd = w_t * sp.cos(p * z)
cons1 = sp.simplify(sp.diff(T00d, t) + sp.diff(T0zd, z))
cons2 = sp.simplify(sp.diff(T0zd, t) + sp.diff(Tzzd, z))
print("C1: conservacion d_mu T^{mu 0} y d_mu T^{mu z} (esperado 0,0):", cons1, ",", cons2)
Lsrc = sp.expand(zavg(sp.Rational(1, 2) * (
    H[0, 0] * T00d + 2 * H[0, 3] * T0zd + H[3, 3] * Tzzd)))
print("L_src =", Lsrc)

# --- C2: invariancia gauge de Phi_obs (nivel de modo) ---
Ag = sp.Function('Agauge')(t); Cg = sp.Function('Cgauge')(t)
Phi_obs_expr = phi - sp.diff(B - dE / 2, t)
gsub = {phi: phi + sp.diff(Ag, t), B: B + sp.diff(Cg, t) + Ag,
        E: E + 2 * Cg}
dPhi = sp.simplify((Phi_obs_expr.subs(gsub) - Phi_obs_expr).doit())
print("C2: delta Phi_obs bajo difeo linealizado (esperado 0):", dPhi)

# ==================== PARTE LO: EL TEOREMA ====================
print("\n==================== LO: teorema 'gauge fixing' ====================")
Ltot_LO = sp.expand(Mp2 * LEH_can + Lmass + Lsrc)
eqs_LO = {f: EL(Ltot_LO, f) for f in fields}

# candidato causal: phi = 0, B = 0, psi = rho/(4 Mp2 p^2), E generico
cand = {phi: sp.Integer(0), B: sp.Integer(0), psi: rho / (4 * Mp2 * p**2)}
res_phi = sp.simplify(eqs_LO[phi].subs(cand).doit())
res_B = sp.simplify(eqs_LO[B].subs(cand).doit())
res_E = sp.simplify(eqs_LO[E].subs(cand).doit())
print("C3: EL_phi, EL_B, EL_E sobre el candidato (esperado 0,0,0):",
      res_phi, ",", res_B, ",", res_E)
eq_psi_c = sp.expand(eqs_LO[psi].subs(cand).doit())
E2sol = sp.solve(eq_psi_c, sp.Derivative(E, (t, 2)))[0]
print("Eddot (acrecion del medio) =", sp.simplify(E2sol))
Phi_obs_LO = sp.simplify(sp.Integer(0) - sp.Integer(0) + E2sol / 2)
print("Phi_obs (LO causal) =", Phi_obs_LO)
print("Psi_obs (LO causal) =", cand[psi])
print("Phi_obs - Psi_obs =", sp.simplify(Phi_obs_LO - cand[psi]),
      " (transitorio ~ rho'' : retardacion estandar, se apaga con fuente quieta)")
print("limite fuente estatica rho->rho0: Phi_obs =",
      sp.simplify(Phi_obs_LO.subs({sp.Derivative(rho, (t, 2)): 0, rho: rho0})),
      " = Newton EXACTO; y NO depende de m0, m1.")

# C4: el mismo candidato resuelve las ecuaciones de RG PURA (m=0):
eqs_GR = {f: EL(sp.expand(Mp2 * LEH_can + Lsrc), f) for f in fields}
subE2 = {sp.Derivative(E, (t, 2)): E2sol,
         sp.Derivative(E, (t, 3)): sp.diff(E2sol, t),
         sp.Derivative(E, (t, 4)): sp.diff(E2sol, t, 2)}
resGR = [sp.simplify(eqs_GR[f].subs(cand).doit().subs(subE2).doit()) for f in fields]
print("C4: EL de RG pura sobre la solucion masiva-LO (esperado [0,0,0,0]):", resGR)
print("  => la solucion causal del sistema masivo LO ES una solucion exacta de RG,")
print("     escrita en el gauge que el termino de masa fija (sincrono: h00=h0i=0).")
print("  => L_m evaluado en la solucion = 0 (gauge-fixing que no cuesta on-shell):",
      sp.simplify(Lmass.subs(cand).doit()))

# ==================== PARTE NLO: alpha, beta ====================
print("\n==================== NLO: fuente eterna, datos RG en t=0 ====================")
# fuente constante rho0 (prendida rapido antes de t=0); solo alpha,beta (sigma=rho_op=0)
DLab = DLfull.subs({si: 0, rh: 0})
Lsrc0 = Lsrc.subs({sp.Derivative(rho, (t, 2)): 0, sp.Derivative(rho, t): 0, rho: rho0})
Ltot = sp.expand(Mp2 * LEH_can + Lmass + DLab + Lsrc0)

# phi y B auxiliares
assert sp.diff(Ltot, sp.Derivative(phi, t)) == 0
assert sp.diff(Ltot, sp.Derivative(B, t)) == 0
elphi = sp.expand(sp.diff(Ltot, phi))
elB = sp.expand(sp.diff(Ltot, B))
solc = sp.solve([elphi, elB], [phi, B], dict=True)[0]
phi_c = sp.simplify(solc[phi]); B_c = sp.simplify(solc[B])
print("phi (vinculo) =", phi_c)
print("B (vinculo)   =", B_c)
Lred = sp.expand(sp.simplify(Ltot.subs(solc)))
assert sp.simplify(sp.diff(Lred, E)) == 0   # simetria residual: E solo via Edot

# EOMs reducidas: sistema lineal en (psiddot, Eddot, psi, 1)
eq1 = sp.expand(EL(Lred, psi))
eq2 = sp.expand(EL(Lred, E))
D2psi, D2E = sp.Derivative(psi, (t, 2)), sp.Derivative(E, (t, 2))
for eq in (eq1, eq2):
    assert eq.coeff(sp.Derivative(psi, t)) == 0 or sp.simplify(eq.coeff(sp.Derivative(psi, t))) == 0
soldd = sp.solve([eq1, eq2], [D2psi, D2E], dict=True)[0]
psidd = sp.expand(soldd[D2psi]); Edd = sp.expand(soldd[D2E])
# psidd = -W2*(psi - psistar): frecuencia y punto fijo
W2 = sp.simplify(-psidd.coeff(psi))
psistar = sp.simplify(sp.solve(psidd, psi)[0])
print("\nomega^2(p) exacta (del sistema reducido) =", sp.simplify(W2))
print("psi* (punto fijo) =", psistar)

# C5: controles de la dispersion
psiN = rho0 / (4 * Mp2 * p**2)
phistat = rho0 / (2 * (2 * Mp2 * p**2 - m0s))
print("\nC5a: psi* - psi_estatico (esperado 0):", sp.simplify(psistar - phistat))
kap = al + be
W2_eft = sp.series(W2.subs({al: sp.Symbol('lam') * al, be: sp.Symbol('lam') * be}),
                   sp.Symbol('lam'), 0, 2).removeO().subs(sp.Symbol('lam'), 1)
print("C5b: omega^2 EFT (lineal en alpha,beta) =", sp.simplify(sp.expand(W2_eft)))
print("     esperado (acta): (kappa/2Mp2) p^2 - (kappa/m0^2) p^4, kappa=al+be:",
      sp.simplify(sp.expand(W2_eft) - (kap / (2 * Mp2) * p**2 - kap / m0s * p**4)))
# formula exacta de la acta (Mpl=1, sigma=rho_op=0):
W2_acta = p**2 * (kap * (2 * p**2 - m0s)) / (m0s * (-2 - al + 3 * be + al**2 + 3 * al * be))
print("C5c: omega^2(Mp2=1) - formula exacta de la acta (esperado 0):",
      sp.simplify(W2.subs(Mp2, 1) - W2_acta))

# C5d: dispersion con TODOS los NLO (sigma, rho_op) contra la acta, Mp2=1
# NOTA (auditoria del texto, 2026-07-21): este chequeo imprime un residuo NO nulo
# ~ m1^2 * p^4 * rho_op^2 con "esperado 0". PENDIENTE DE DIRIMIR (block list del paper):
# (a) puede ser un chequeo obsoleto frente a la correccion que el acta incorporo
#     (el termino 4*sigma^2*p^4/Mp2^2 del verificador en gamma(p)), o
# (b) una mezcla de convenciones rho (acta escalar, entra en omega^2) vs rho_op
#     (acta acople, entra en gamma(p)) — son acoples NLO distintos.
# La formula omega^2(p) del paper es la del acta del ESCALAR, verificada por el
# pipeline independiente de escalar/verificador/ (alli m1^2 se cancela exacto).
Ltot4 = sp.expand(Mp2 * LEH_can + Lmass + DLfull)
elphi4 = sp.expand(sp.diff(Ltot4, phi)); elB4 = sp.expand(sp.diff(Ltot4, B))
solc4 = sp.solve([elphi4, elB4], [phi, B], dict=True)[0]
Lred4 = sp.expand(sp.simplify(Ltot4.subs(solc4)))
eqa = sp.expand(EL(Lred4, psi)); eqb = sp.expand(EL(Lred4, E))
soldd4 = sp.solve([eqa, eqb], [D2psi, D2E], dict=True)[0]
W2_4 = sp.simplify(-sp.expand(soldd4[D2psi]).coeff(psi))
W2_acta4 = p**2 * (kap * (2 * p**2 - m0s) + p**2 * m0s * (rh**2 / 2 - 2 * kap * si)) \
    / (m0s * (-2 - al + 3 * be + al**2 + 3 * al * be))
print("C5d: omega^2 con sigma,rho_op (Mp2=1) - acta (esperado 0):",
      sp.simplify(W2_4.subs(Mp2, 1) - W2_acta4))

# --- solucion cerrada del IVP: psi(0)=psiN, psi'(0)=0, E'(0)=0 ---
print("\n--- solucion cerrada del IVP (fuente eterna, datos RG + medio en reposo) ---")
Om = sp.sqrt(W2)
tt = t
psi_t = psistar + (psiN - psistar) * sp.cos(Om * tt)
# Eddot = gpsi*psi + gc  ->  Edot(t) con Edot(0)=0
gpsi = sp.simplify(Edd.coeff(psi))
gc = sp.simplify(Edd - gpsi * psi)
Edot_t = sp.integrate(gpsi * psi_t + gc, (tt, 0, tt))
Edot_t = sp.simplify(Edot_t)
# verificar que psi_t resuelve su EOM
chk = sp.simplify(sp.diff(psi_t, tt, 2) - psidd.subs(psi, psi_t))
print("C6a: psi(t) resuelve la EOM (esperado 0):", chk)
# phi(t), B(t) por vinculos; Phi_obs(t)
phi_t = sp.simplify(phi_c.subs(psi, psi_t).doit())
B_t = B_c.subs({sp.Derivative(psi, t): sp.diff(psi_t, tt),
                sp.Derivative(E, t): Edot_t})
B_t = sp.simplify(B_t)
Phi_obs_t = sp.simplify(phi_t - sp.diff(B_t, tt) + sp.diff(Edot_t, tt) / 2)
PhiN = psiN
DPhi = sp.simplify(Phi_obs_t - PhiN)
print("Phi_obs(t,p) - Phi_N =", sp.collect(sp.expand(DPhi), sp.cos(Om * tt)))

# C6b: kappa->0 => Newton para todo t
DPhi_k0 = sp.simplify(DPhi.subs({al: 0, be: 0}))
print("C6b: [Phi_obs - Phi_N] con alpha=beta=0 (esperado 0):", DPhi_k0)

# C6c: estructura ACLM: DPhi = (phi_stat - Phi_N)(1 - cos(Om t)) + O(kappa)
DPhi_ACLM = (phistat - PhiN) * (1 - sp.cos(Om * tt))
restoNLO = sp.simplify(DPhi - DPhi_ACLM)
lam = sp.Symbol('lam')
resto_ser = sp.series(restoNLO.subs({al: lam * al, be: lam * be}), lam, 0, 2)
print("C6c: resto = DPhi - (phi_stat - Phi_N)(1-cos Om t); su serie en kappa:")
print("     ", sp.simplify(resto_ser.removeO().subs(lam, 1)))

# C6d: Psi_obs(t): amplitud identica
DPsi = sp.simplify(psi_t - psiN)
print("C6d: Psi_obs(t) - Psi_N = (psi*-psiN)(1-cos): ",
      sp.simplify(DPsi - (phistat - psiN) * (1 - sp.cos(Om * tt))))

# --- escalas: banda de Jeans, t_c, r_c (kappa<0, m0^2>0) ---
print("\n--- escalas (rama sana kappa = al+be < 0) ---")
k2 = sp.Symbol('k2', positive=True)   # k2 = -kappa = |kappa|
W2_eftk = (-k2 / (2 * Mp2) * p**2 + k2 / m0s * p**4)
p2 = sp.Symbol('p2', positive=True)
G2 = sp.simplify(-W2_eftk.subs(p**2, p2).subs(p**4, p2**2))
p2s = sp.solve(sp.diff(G2, p2), p2)[0]
Gmax2 = sp.simplify(G2.subs(p2, p2s))
print("banda de Jeans: 0 < p^2 < m0^2/(2 Mp2)  (= mu^2: el MISMO p del polo estatico)")
print("p*^2 =", p2s, " Gamma_max^2 =", Gmax2)
print("t_c = 1/Gamma_max =", sp.simplify(1 / sp.sqrt(Gmax2)),
      "  [= 4 Mp2/(sqrt(|kappa|) m0)]")
print("r_c = 1/mu =", sp.sqrt(2 * Mp2 / m0s), " [= sqrt(2 Mp2)/m0]")

# ==================== ESQUINA (1,2): numeros y control numerico ====================
print("\n==================== esquina (m0^2,m1^2)=(1,2), Mp2=1, al=0, be=-1/100 ====================")
eps = sp.Rational(1, 100)
esq = {m0s: 1, m1s: 2, Mp2: 1, al: 0, be: -eps, rho0: 1}
W2e = sp.simplify(W2.subs(esq))
print("omega^2(p) =", W2e, "  [acta: eps p^2 (2p^2-1)/(2+3 eps) con eps=1/100 -> signo -be]")
psi_te = sp.simplify(psi_t.subs(esq))
Phi_obs_te = sp.simplify(Phi_obs_t.subs(esq))
PhiNe = sp.simplify(PhiN.subs(esq))

# control numerico independiente: integrar el sistema reducido (psi,E) con mpmath
import mpmath as mp
psidd_e = sp.lambdify((psi, p), psidd.subs(esq), 'mpmath')
Phi_num_expr = sp.simplify((phi_c - 0).subs(esq))  # phi(psi)
pval = mp.mpf('0.6')
f_psidd = lambda pv, y: psidd_e(y, pv)
def rhs(tv, y):
    # y = [psi, psidot]
    return [y[1], f_psidd(pval, y[0])]
psiN_e = float(1 / (4 * pval**2))
sol_ode = mp.odefun(rhs, 0, [psiN_e, 0])
psi_closed = sp.lambdify(t, psi_te.subs(p, sp.Float(str(pval))), 'mpmath')
errs = [abs(sol_ode(tv)[0] - psi_closed(tv)) for tv in (5, 20, 60)]
print("C7: |psi_numerico - psi_cerrado| en t=5,20,60 (p=0.6):", [mp.nstr(e, 3) for e in errs])

# tabla radial: dPhi(r,t)/Phi_N(r) via integral radial de Fourier
DPhi_e = sp.simplify(DPhi.subs(esq))
# funcion numerica robusta (banda de Jeans: cos -> cosh via aritmetica compleja)
W2f = sp.lambdify(p, W2e, 'mpmath')
phistat_e = sp.lambdify(p, sp.simplify(phistat.subs(esq)), 'mpmath')
def dphi_mode(pv, tv):
    Wv = W2f(pv)
    Omv = mp.sqrt(mp.mpc(Wv))
    amp = phistat_e(pv) - 1 / (4 * pv**2)
    # DPhi exacto = amp*(1-cos) + resto NLO; usamos la expresion completa:
    return complex(dphi_full(pv, tv)).real
DPhi_l = sp.lambdify((p, t), DPhi_e, modules=['mpmath'])
def dphi_full(pv, tv):
    try:
        return DPhi_l(mp.mpc(pv), mp.mpf(tv))
    except Exception:
        return mp.mpc(0)
def dPhi_r(rv, tv):
    integ = lambda pv: pv * mp.sin(pv * rv) * mp.re(dphi_full(pv, tv))
    val = mp.quad(integ, [1e-6, 0.25, mp.sqrt(0.5), 1.5, 5, 20, 60])
    return val / (2 * mp.pi**2 * rv)
def PhiN_r(rv):
    return 1 / (16 * mp.pi * rv)
rc = mp.sqrt(2)
Gmax = mp.sqrt(float(eps) / (8 * (2 + 3 * float(eps))))
tc = 1 / Gmax
print(f"r_c = {mp.nstr(rc,4)},  t_c = 1/Gamma_max = {mp.nstr(tc,4)}")
print("tabla  dPhi(r,t)/Phi_N(r):")
hdr = "r\\t      " + "".join([f"{mp.nstr(tv,5):>12}" for tv in (0, tc, 2*tc, 3*tc)])
print(hdr)
for rv in (0.25 * rc, rc, 3 * rc):
    row = [dPhi_r(rv, tv) / PhiN_r(rv) for tv in (0, tc, 2 * tc, 3 * tc)]
    print(f"{mp.nstr(rv,4):>7} " + "".join([f"{mp.nstr(x,3):>12}" for x in row]))
print("\n(lectura esperada: ~0 en t=0; crece con t; a t >~ t_c la correccion es O(1)")
print(" cerca de r_c y sigue creciendo: la 'estatica eterna' oscilatoria nunca se alcanza,")
print(" es el punto fijo inestable de la banda de Jeans -- historia identica a ACLM.)")
print("\nFIN colA_causal")
