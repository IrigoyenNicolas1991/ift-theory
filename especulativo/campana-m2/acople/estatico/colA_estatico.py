# -*- coding: utf-8 -*-
"""
COLUMNA A (campana m2=0) -- parte 1: ESTATICA EXACTA de una masa puntual quieta.

Sistema: EH linealizado + medio U(X,Y) en gauge unitario (fase protegida:
m2=m3=m4=0; vivos m0^2, m1^2) + operadores NLO del medio (alpha, beta, sigma, rho_op)
+ materia estandar: T^00 = M delta^3(x), T^{0i} = T^{ij} = 0 (estatico, conservado).

Convenciones (identicas a la campana, actas SECTOR-ESCALAR-2026-07-21):
  signatura (-,+,+,+);  g = eta + h;  L = Mp2*(sqrt(-g)R)^(2) + L_m + DL_NLO + L_src
  Mp2 = 1/(16 pi G);  L_m = (1/4)[m0^2 h00^2 + 2 m1^2 h0i h0i]   ([m^2]=masa^4)
  L_src = (1/2) h_mn T^mn  (normalizacion verificada abajo con el control RG)
  h00 = 2 phi, h0i = d_i B, hij = 2 psi delta_ij + d_i d_j E
  (o sea g00 = -(1-2phi): el potencial newtoniano estandar es Phi_N = -phi, Psi_N = -psi)

Por modo de Fourier con p a lo largo de z; amplitudes constantes (estatica exacta).
Chequeos E1..E7 declarados en linea.
"""
import sympy as sp
from eh_lib import t, z, p, zavg, L12_of_ansatz

Mp2 = sp.Symbol('Mpl2', positive=True)
m0s, m1s = sp.symbols('m0sq m1sq', positive=True)   # m0^2, m1^2 (esquina sana: >0)
al, be, si, rh = sp.symbols('alpha beta sigma rho_op', real=True)
rho0 = sp.Symbol('rho0', real=True)                 # Ttilde^00(p) = M (FT de M delta^3)

# ---------- ansatz estatico ----------
ph, Bb, ps, Ee = sp.symbols('phi B psi E', real=True)
c = sp.cos(p * z)
H = sp.zeros(4, 4)
H[0, 0] = 2 * ph * c
H[0, 3] = H[3, 0] = sp.diff(Bb * c, z)
H[1, 1] = 2 * ps * c
H[2, 2] = 2 * ps * c
H[3, 3] = 2 * ps * c + sp.diff(Ee * c, (z, 2))

L1d, L2d = L12_of_ansatz(H)
LEH = sp.expand(zavg(L2d))
print("LEH estatico (por modo, promediado):", sp.simplify(LEH))

# ---------- masas LO ----------
Lmass = sp.expand(zavg(sp.Rational(1, 4) * (
    m0s * H[0, 0]**2 + 2 * m1s * (H[0, 1]**2 + H[0, 2]**2 + H[0, 3]**2))))
print("L_masas estatico:", Lmass)

# ---------- NLO del medio (base de la campana, run_scalar_step3) ----------
Xc = [t, sp.Symbol('x'), sp.Symbol('y'), z]
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
DL = (sp.Rational(1, 4) * al * sum(Kb[a, b]**2 for a in range(3) for b in range(3))
      + sp.Rational(1, 4) * be * trK**2
      + sp.Rational(1, 4) * si * R3**2
      + sp.Rational(1, 4) * rh * trK * R3)
DLavg = sp.expand(zavg(sp.expand(DL)))
print("DL_NLO estatico:", sp.collect(DLavg, [al, be, si, rh]))

# ---------- fuente ----------
T00 = rho0 * c
Lsrc = sp.expand(zavg(sp.Rational(1, 2) * H[0, 0] * T00))
print("L_src estatico:", Lsrc)

Ltot = sp.expand(Mp2 * LEH + Lmass + DLavg + Lsrc)

# ---------- E1: el modo E no aparece (simetria residual xi^i(x)) ----------
print("\n== E1: dL/dE (esperado 0 identicamente; E = gauge residual xi^i(x)) ==")
print("dL/dE =", sp.simplify(sp.diff(Ltot, Ee)))

# ---------- EOMs estaticas y solucion exacta ----------
eqs = [sp.expand(sp.diff(Ltot, v)) for v in (ph, Bb, ps)]
for nm, e in zip(('phi', 'B', 'psi'), eqs):
    print(f"EOM_{nm}: ", e)

sol = sp.solve(eqs, [ph, Bb, ps], dict=True)[0]
phi_sol = sp.simplify(sol[ph]); B_sol = sp.simplify(sol[Bb]); psi_sol = sp.simplify(sol[ps])
print("\n== SOLUCION ESTATICA EXACTA (todos los NLO encendidos) ==")
print("phi(p) =", phi_sol)
print("B(p)   =", B_sol)
print("psi(p) =", psi_sol)
print("gamma(p) = psi/phi =", sp.simplify(psi_sol / phi_sol))

# ---------- E2: control RG ----------
print("\n== E2: control RG (m->0, NLO->0) ==")
rg = {m0s: 0, m1s: 0, al: 0, be: 0, si: 0, rh: 0}
# en RG la EOM de B es 0=0: resolver solo phi,psi
eqs_rg = [sp.expand(e.subs(rg)) for e in eqs]
sol_rg = sp.solve([eqs_rg[0], eqs_rg[2]], [ph, ps], dict=True)[0]
print("phi_RG =", sp.simplify(sol_rg[ph]), " | psi_RG =", sp.simplify(sol_rg[ps]))
print("(esperado ambos = rho0/(4 Mp2 p^2), o sea phi(r)=psi(r)=GM/r, gamma=1)")
print("check:", sp.simplify(sol_rg[ph] - rho0 / (4 * Mp2 * p**2)),
      sp.simplify(sol_rg[ps] - rho0 / (4 * Mp2 * p**2)))

# ---------- E3: LO exacto ----------
print("\n== E3: LO (NLO=0) ==")
lo = {al: 0, be: 0, si: 0, rh: 0}
phi_LO = sp.simplify(phi_sol.subs(lo)); psi_LO = sp.simplify(psi_sol.subs(lo))
B_LO = sp.simplify(B_sol.subs(lo))
mu2 = m0s / (2 * Mp2)
print("phi_LO =", phi_LO)
print("psi_LO =", psi_LO)
print("B_LO   =", B_LO)
print("phi_LO - (rho0/4Mp2)/(p^2 - mu^2) =",
      sp.simplify(phi_LO - (rho0 / (4 * Mp2)) / (p**2 - mu2)))
print("gamma_LO =", sp.simplify(psi_LO / phi_LO))

# ---------- E4: teorema alpha-beta ----------
print("\n== E4: NLO alpha,beta SOLOS no cambian la estatica ==")
ab = {si: 0, rh: 0}
print("phi(al,be) - phi_LO =", sp.simplify(phi_sol.subs(ab) - phi_LO))
print("psi(al,be) - psi_LO =", sp.simplify(psi_sol.subs(ab) - psi_LO))
print("B(al,be)  =", sp.simplify(B_sol.subs(ab)))
print("(razon estructural: Kbar_ij estatico = -2 d_i d_j B: alpha,beta solo tocan la EOM de B,")
print(" y B=0 sigue siendo la solucion; sigma(R3^2) y rho_op(trKbar R3) si entran)")

# ---------- E5: efecto de sigma y rho_op ----------
print("\n== E5: sigma, rho_op — gamma(p) exacta y serie ==")
gam = sp.simplify(psi_sol / phi_sol)
print("gamma(p) exacta =", gam)
gam_ser = sp.series(gam.subs({al: 0, be: 0}), p, 0, 5)
print("serie p->0 (al=be=0):", sp.simplify(gam_ser.removeO()))

# ---------- E6: r-espacio ----------
print("\n== E6: verificacion r-espacio ==")
r, mu = sp.symbols('r mu', positive=True)
f = sp.cos(mu * r) / r
lap = sp.diff(f, r, 2) + 2 / r * sp.diff(f, r)
print("(lap + mu^2) cos(mu r)/r  (r>0, esperado 0):", sp.simplify(lap + mu**2 * f))
g2 = sp.sin(mu * r) / r
lap2 = sp.diff(g2, r, 2) + 2 / r * sp.diff(g2, r)
print("(lap + mu^2) sin(mu r)/r  (r>0, esperado 0):", sp.simplify(lap2 + mu**2 * g2))
print("cos(mu r)/r ~", sp.series(f, r, 0, 4))
print("sin(mu r)/r ~", sp.series(g2, r, 0, 4), " (regular en r=0: modo homogeneo permitido)")
print("singularidad 1/r de cos: la delta se normaliza igual que Newton ->")
print("  phi(r) = psi(r) = G M [cos(mu r) + C sin(mu r)]/r ,  mu^2 = m0^2/(2 Mp2)")
print("  C NO fijado por la estatica (contorno en infinito no decae): familia declarada.")

# ---------- E7: esquina (m0^2, m1^2) = (1, 2), Mp2 = 1 ----------
print("\n== E7: esquina (1,2), Mp2=1 ==")
esq = {m0s: 1, m1s: 2, Mp2: 1, al: 0, be: 0, si: 0, rh: 0}
phi_esq = sp.simplify(phi_sol.subs(esq))
print("phi(p) =", phi_esq, "  (polo en p^2 = 1/2: mu = 1/sqrt(2), r_c = sqrt(2))")
print("coincide con el cero no trivial de omega^2(p) de la acta (p^2 = 1/2): mismo p.")
print("\nFIN colA_estatico")
