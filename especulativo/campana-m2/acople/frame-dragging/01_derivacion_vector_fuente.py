# -*- coding: utf-8 -*-
"""
COLUMNA B - paso 1: sector vectorial CON FUENTE ROTANTE, ecuaciones exactas.

Convenciones (identicas a la campana m2=0, verificadas por el verificador adversarial):
  signatura (-,+,+,+), g = eta + h, L_EH = M_Pl^2 sqrt(-g) R  (M_Pl^2 = 1/16piG)
  L_m = (1/4)[m0^2 h00^2 + 2 m1^2 h0i h0i - ...]  (BCP; fase m2=m3=m4=0)
  NLO del medio: DL = (alpha/4) Kbar_ij Kbar_ij + (beta/4)(trKbar)^2,
                 Kbar_ij = hdot_ij - d_i h0j - d_j h0i
  Acople a materia (diff-invariante, el medio no toca el acople):
                 L_int = (1/2) h_munu T^munu
Ansatz vectorial (polarizacion x, momento p en z):
  h_0x = S(t) cos(pz),   h_xz = d_z( F(t) cos(pz) )
Fuente conservada EXACTA (rotante, estacionaria o con spin-up):
  T^{0x} = tau(t) cos(pz),  T^{xz} = -(taudot(t)/p) sin(pz)
  (verifica d_mu T^{mu nu} = 0 exactamente; estacionario => T^{xz}=0)

Reusa eh_lib.py del derivador de la campana (pipeline ya auditado por el
verificador independiente); el limite RG se contrasta ademas contra Kerr en
el script 02.
"""
import sys, os
sys.path.insert(0, r"C:\ClaudeInMyComputer\TCI CON Fable New folder\ift-theory\especulativo\campana-m2\escalar\derivador")
import sympy as sp
from eh_lib import t, z, p, X, zavg, check_zavg, L12_of_ansatz, EL

Mp2 = sp.Symbol('Mpl2', positive=True)   # M_Pl^2 = 1/16 pi G
m1s = sp.Symbol('m1sq', positive=True)   # m1^2 = 2 U_X  (dimension E^4)
al  = sp.Symbol('alpha', real=True)
tau = sp.Function('tau')(t)              # T^{0x}(t) por modo

S = sp.Function('S')(t)
F = sp.Function('F')(t)
c = sp.cos(p * z)

H = sp.zeros(4, 4)
H[0, 1] = H[1, 0] = S * c
H[1, 3] = H[3, 1] = sp.diff(F * c, z)

# ---------- L_EH cuadratico exacto desde sqrt(-g) R ----------
L1d, L2d = L12_of_ansatz(H)
assert check_zavg(L2d) == 0
LEH = sp.expand(Mp2 * zavg(L2d))
print("L_EH^vec =", sp.simplify(LEH))
# El termino -4F*Fdd es (p.p.) +4Fd^2: L_EH ~ (Mp2 p^2/4) (S-Fdot)^2 = (Mp2 p^2/4) sigma^2.
# Verifico la equivalencia por partes comparando EOMs contra la forma IBP:
LEH_ibp = Mp2 * p**2 / 4 * (S - sp.Derivative(F, t))**2
for f in [S, F]:
    assert sp.simplify(EL(LEH, f) - EL(sp.expand(LEH_ibp), f)) == 0
print("L_EH^vec == (Mpl2 p^2/4)(S - Fdot)^2  (mod deriv. total; EOMs identicas)  OK")
print("=> EH depende SOLO del invariante sigma = S - Fdot  (diff-invariancia exacta)")

# ---------- masa m1 + NLO alpha ----------
Lm = sp.expand(zavg(sp.Rational(1, 4) * 2 * m1s * (H[0, 1]**2 + H[0, 2]**2 + H[0, 3]**2)))
print("L_m^vec =", Lm)

Kb = sp.zeros(3, 3)
for a in range(3):
    for b in range(3):
        Kb[a, b] = (sp.diff(H[a + 1, b + 1], t)
                    - sp.diff(H[0, b + 1], X[a + 1])
                    - sp.diff(H[0, a + 1], X[b + 1]))
trK = sp.simplify(sum(Kb[a, a] for a in range(3)))
assert trK == 0  # beta no toca el vector
DL = sp.expand(zavg(sp.Rational(1, 4) * al * sum(Kb[a, b]**2 for a in range(3) for b in range(3))))
print("DL_alpha^vec =", sp.simplify(DL))

# ---------- fuente conservada exacta ----------
T0x = tau * c
Txz = -sp.diff(tau, t) / p * sp.sin(p * z)
# chequeo de conservacion: d_t T^{t x} + d_z T^{z x} = 0  (indices arriba, fondo plano)
cons = sp.simplify(sp.diff(T0x, t) + sp.diff(Txz, z))
print("conservacion d_mu T^{mu x} =", cons)
assert cons == 0
# L_int = (1/2) h_munu T^munu ; con (-,+,+,+): h_{0i}T^{0i} aparece 2 veces con
# signo (h_{0x} T^{0x} via g^{00}g^{xx} => -h_0x T_0x = +h_0x T^{0x}... el signo
# global se FIJA en el limite RG contra Kerr (script 02); aca definimos
# L_int = h_{0x} T^{0x} + h_{xz} T^{xz} y verificamos consistencia interna.
Lint = sp.expand(zavg(H[0, 1] * T0x + H[1, 3] * Txz))
print("L_int =", Lint)

Ltot = sp.expand(LEH + Lm + DL + Lint)
print("\nL_total =", sp.collect(Ltot, [Mp2, m1s, al]))

# ---------- ecuaciones de movimiento EXACTAS ----------
eqS = sp.expand(EL(Ltot, S))
eqF = sp.expand(EL(Ltot, F))
print("\nEOM S:  0 =", sp.collect(eqS, [Mp2, m1s, al]))
print("EOM F:  0 =", sp.collect(eqF, [Mp2, m1s, al]))

# estructura: la EOM de F debe ser una derivada temporal total => ley de conservacion
prim = sp.integrate(eqF, t)  # primitiva formal
print("EOM F es d/dt de:", sp.simplify(prim))

# ---------- caso ESTACIONARIO ----------
# fuente estacionaria: tau = const, taudot = 0; buscamos solucion estacionaria:
tauc = sp.Symbol('tau0')
Sc, Fdotc = sp.symbols('S0 Fdot0')
sub_stat = {sp.Derivative(S, (t, 2)): 0, sp.Derivative(S, t): 0, S: Sc,
            sp.Derivative(F, (t, 2)): 0, sp.Derivative(F, t): Fdotc,
            sp.Derivative(tau, t): 0, tau: tauc}
eqS_st = sp.expand(eqS.subs(sub_stat))
eqF_st = sp.expand(eqF.subs(sub_stat))
print("\nESTACIONARIO:")
print("EOM S:", eqS_st, "= 0")
print("EOM F:", eqF_st, "= 0   (trivial: la EOM de F es d/dt[...])")

# La EOM de F se satisface identicamente en estacionario => el sistema NO fija
# Fdot0: direccion plana. La condicion fisica extra: h_ij estacionaria y
# sin marco rotante en infinito => Fdot = 0 salvo el modo de memoria (ver abajo).
solS_relaj = sp.solve(eqS_st.subs(Fdotc, 0), Sc)[0]
print("\nSolucion con Fdot=0 (medio relajado):  S0 =", sp.factor(solS_relaj))
S_GR = solS_relaj.subs({m1s: 0, al: 0})
print("Limite RG (m1=alpha=0):  S0_GR =", S_GR)
ratio = sp.simplify(solS_relaj / S_GR)
print("Apantallamiento S0/S0_GR =", sp.factor(ratio))
mu2 = sp.Symbol('mu2')
ratio_esperado = Mp2 * p**2 / ((Mp2 + al) * p**2 + m1s)
assert sp.simplify(ratio - ratio_esperado) == 0
print("=> (Mpl^2+alpha) (d^2/dr^2...) : propagador 1/((Mpl2+al)p^2 + m1^2)  CONFIRMADO")
print("=> masa fisica de apantallamiento mu^2 = m1^2/(Mpl^2+alpha)  CONFIRMADO")

# ---------- Lagrangiano equivalente IBP (sin F Fdd) y cotejo con la campana ----------
Lint_sym = tau * S / 2 + sp.Derivative(tau, t) * F / 2
L_ibp = sp.expand((Mp2 + al) * p**2 / 4 * (S - sp.Derivative(F, t))**2
                  + m1s * S**2 / 4 + Lint_sym)
for f in [S, F]:
    dif = sp.simplify(EL(Ltot, f) - EL(L_ibp, f))
    assert dif == 0, (f, dif)
print("\nL_ibp = ((Mpl2+al)p^2/4) sigma^2 + (m1^2/4) S^2 + (tau/2) S + (taudot/2) F")
print("  EOMs(L_ibp) == EOMs(L_total)  OK  (equivalencia modulo derivadas totales)")

# L reducido (S auxiliar, sin fuente) — cotejo con el de la campana:
solS_nofuente = sp.solve(sp.diff(L_ibp.subs({tau: 0, sp.Derivative(tau, t): 0}), S), S)[0]
Lred = sp.simplify(L_ibp.subs({tau: 0, sp.Derivative(tau, t): 0}).subs(S, solS_nofuente))
Lred_camp = m1s * (Mp2 + al) * p**2 / (4 * ((Mp2 + al) * p**2 + m1s)) * sp.Derivative(F, t)**2
print("L_red (sin fuente) =", sp.factor(Lred))
assert sp.simplify(Lred - Lred_camp) == 0
print("cotejo con L_red de la campana (polo (Mpl2+al)p^2+m1^2): OK")

# ---------- LA SUTILEZA: direccion plana y seleccion del estado ----------
# Analisis canonico LIMPIO sobre L_ibp (primer orden en derivadas; S auxiliar).
print("\n--- Hamiltoniano y seleccion del estado (fuente estacionaria tau0) ---")
Fd = sp.Symbol('Fdot')
Ssym = sp.Symbol('S_')
A = Mp2 + al
Lmec = sp.expand(A * p**2 / 4 * (Ssym - Fd)**2 + m1s * Ssym**2 / 4 + tauc * Ssym / 2)
pi_F = sp.diff(Lmec, Fd)
print("pi_F = dL/dFdot =", sp.factor(pi_F), "   (= -(A p^2/2) sigma)")
pis = sp.Symbol('pi')
Fd_of_pi = sp.solve(sp.Eq(pis, pi_F), Fd)[0]
Hmec = sp.expand((pis * Fd - Lmec).subs(Fd, Fd_of_pi))
# S es auxiliar: se elimina con dH/dS = 0 a pi fijo
S_of_pi = sp.solve(sp.diff(Hmec, Ssym), Ssym)[0]
H_red = sp.factor(sp.expand(Hmec.subs(Ssym, S_of_pi)))
print("S(pi) del vinculo =", S_of_pi)
H_forma = (2 * pis - tauc)**2 / (4 * m1s) + pis**2 / (A * p**2)
assert sp.simplify(H_red - H_forma) == 0
print("H(pi; tau0) = (2 pi - tau0)^2/(4 m1^2) + pi^2/((Mpl2+al) p^2)")
print("  => POSITIVA DEFINIDA si m1^2>0 y (Mpl2+al)>0: sector sin fantasma  OK")
print("  => pi (momento del modo plano de F) es CONSTANTE de movimiento: dH/dF = 0")
# minimo sobre la direccion plana pi:
pimin = sp.solve(sp.diff(H_red, pis), pis)[0]
S_min = sp.simplify(S_of_pi.subs(pis, pimin))
Fd_min = sp.simplify(Fd_of_pi.subs({pis: pimin, Ssym: S_min}))
d2H = sp.simplify(sp.diff(H_red, pis, 2))
print("pi* =", sp.factor(pimin))
print("S en el minimo =", sp.factor(S_min), "  (== Yukawa?",
      sp.simplify(S_min - solS_relaj) == 0, ")")
print("Fdot en el minimo =", Fd_min, "  (medio en reposo)")
print("d2H/dpi2 =", sp.factor(d2H), "  > 0: es MINIMO global  OK")

# ---------- rama B: respuesta retardada estricta (spin-up, sin disipacion) ----------
print("\n--- rama B: spin-up adiabatico desde el vacio (memoria del fluido) ---")
solS_t = sp.solve(sp.diff(L_ibp, S), S)[0]   # S auxiliar exacto con tau(t)
print("S(t) del vinculo =", sp.simplify(solS_t))
Lred_t = sp.expand(L_ibp.subs(S, solS_t))
eqF_t = sp.simplify(EL(sp.expand(Lred_t), F))
print("EOM reducida de F:", eqF_t, "= 0")
# solucion retardada exacta desde el vacio (F=Fdot=0, tau=0 en t->-inf):
#   Fdd = taudot/(A p^2)  ==>  Fdot(t) = tau(t)/(A p^2)   (exacto, cond. iniciales nulas)
Fdot_ret = tau / (A * p**2)
chk_F = sp.simplify(eqF_t.subs(sp.Derivative(F, (t, 2)), sp.diff(Fdot_ret, t)))
assert chk_F == 0
S_ret = sp.simplify(solS_t.subs(sp.Derivative(F, t), Fdot_ret))
print("Solucion retardada exacta:  Fdot(t) = tau(t)/((Mpl2+al)p^2),   S(t) =", S_ret)
print("=> la respuesta RETARDADA estricta (sin disipacion) NO da Yukawa: da S=0")
print("   (apantallamiento TOTAL, el medio absorbe el arrastre en un flujo Fdot);")
print("   pero rompe la linealizacion (h_ij crece ~ t) y cuesta energia:")
# energias de ambos estados: pi_ret = -(A p^2/2) sigma_ret; sigma_ret = S - Fdot = -tau/(Ap^2)
pi_ret = sp.simplify(-(A * p**2 / 2) * (S_ret - Fdot_ret))
H_l = sp.lambdify((pis, tauc, Mp2, p, m1s, al), H_red)
vals_n = dict(tau0=1.0, Mpl2=1.0, p=1.0, m1sq=0.1, alpha=0.0)
H_mem = H_l(float(pi_ret.subs({tau: 1, Mp2: 1, p: 1, m1s: sp.Rational(1, 10), al: 0})), 1.0, 1.0, 1.0, 0.1, 0.0)
H_yuk = H_l(float(pimin.subs({tauc: 1, Mp2: 1, p: 1, m1s: sp.Rational(1, 10), al: 0})), 1.0, 1.0, 1.0, 0.1, 0.0)
print(f"   H(estado memoria) = {H_mem:.5f}  vs  H(estado Yukawa/relajado) = {H_yuk:.5f}")
print("   El Yukawa es el fundamental; el estado agitado decae a el con cualquier")
print("   disipacion (fonones/vortices, no-lineal). Caveat superfluido declarado.")

# ---------- identidad clave: la rama de memoria es RG DISFRAZADO ----------
print("\n--- identidad: rama retardada == RG en coordenadas del medio que fluye ---")
sigma_ret = sp.simplify(S_ret - Fdot_ret)
sigma_GR = -tau / (A * p**2)   # solucion RG estacionaria: A p^2 sigma + tau = 0
assert sp.simplify(sigma_ret - sigma_GR) == 0
print("sigma_retardada =", sigma_ret, " == sigma_RG (exacto, incluso con alpha)")
print("=> en la rama retardada el INVARIANTE diff sigma es exactamente el de RG;")
print("   el diff xi^i = -t Fdot^i la lleva a (h_0i = sigma_RG, medio fluyendo):")
print("   la masa m1^2 actua ahi literalmente como termino de gauge-fixing")
print("   (Dubovsky hep-th/0409124, tras su ec. (75): CONFIRMADO y explicado).")
print("   En cambio el estado FUNDAMENTAL (medio quieto) apantalla: Yukawa.")
print("   Meissner gravitomagnetico: expulsar B_g baja la energia (H arriba).")
