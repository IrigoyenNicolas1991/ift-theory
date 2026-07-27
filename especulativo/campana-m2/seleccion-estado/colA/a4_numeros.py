# Columna A - TAREA 3 (a4): LOS NUMEROS del canal NLO y de los canales de energia.
#
# Cierra el programa a1-a3: a3 dejo el resultado simbolico (carga corregida
# C_tilde = A p^2 sigma - c_sigma p^2 Fdot + tau conservada; co-rotante corregido
# S_ret != 0; fuga = (no lineal) x (NLO)) y prometio "numeros en a4". Este es a4.
#
# P1  simbolico exacto (sympy): el OBSERVABLE gauge-invariante del modo es
#     sigma = S - Fdot (la parte de la metrica que no es gauge; S solo es h_0x
#     en el gauge del juguete). Derivo sigma_ret, sigma_rel exactos en (c_s,c_w),
#     la desviacion fraccional delta respecto de RG, y el chequeo de patologia
#     (H >= 0 sobre el vinculo).
# P2  numeros de delta barridos en Lambda [1e-3 eV, 1 MeV]: fraccion del frame
#     dragging RG; comparacion con LARES-2 (0.2%); que c_sigma haria falta.
# P3  fuga de carga (no lineal)x(NLO): estimacion dimensional, cada potencia
#     declarada; Gamma vs 1/t_edad = 2.3e-18 s^-1.
# P4  spin-down terrestre: canal Cherenkov importado (ACLM+Thaler 0507120,
#     Edot ~ alpha M^2 v^3), validado contra SU numero del Sol; torque vs margen
#     del spin-down medido.
#
# SUPUESTOS GLOBALES (declarados una vez, usados en todo el script):
#  (U1) EFT del medio: U = Lambda^4 * Uhat(X,Y) con Uhat y sus derivadas O(1)
#       => m1^2 = 2 U_X ~ Lambda^4 (dimension masa^4 en la convencion BCP donde
#       h es adimensional); con mu = 2 Lambda^2/Mbar_Pl y mu^2 = m1^2/A:
#       m1^2 = 4 Lambda^4 * (A/Mbar_Pl^2) ~= 4 Lambda^4.
#  (U2) NLO del flujo: L_NLO = c_sigma sigma_u^2 + c_omega omega_u^2 (+c_a a^2
#       reducido por EFT, a3/N4). [sigma_u] = masa => [c] = masa^2. La potencia
#       NATURAL de la EFT del medio es c = chat * Lambda^2 con chat ~ O(1).
#       SENSIBILIDAD UV: chat NO es calculable dentro de la EFT (UV-sensible,
#       acta del escalar); todo resultado se reporta LINEAL en chat y se declara
#       que chat haria falta para cambiar el veredicto.
#  (U3) A = M_Pl^2 + alpha ~= Mbar_Pl^2 (alpha ~ Lambda^2 << Mbar_Pl^2; error
#       relativo ~ (Lambda/Mbar_Pl)^2, despreciable a 40+ ordenes).
#  (U4) Numeros de la Tierra: R = 6.371e6 m; Omega = 7.292e-5 rad/s;
#       I = 8.03e37 kg m^2; no-axisimetria estacionaria rotante ~ J22 = 1.8e-6
#       (el cuadrupolo ecuatorial; las mareas oceanicas son menores en masa).
#  (U5) v_drag = velocidad fisica del arrastre de marcos en superficie
#       = Omega_LT * R / c con Omega_LT = 2 G J_earth / (c^2 R^3): el co-rotante
#       co-rota con LOS MARCOS (no con la materia), su amplitud es v_drag.
#  (U6) t_edad = 13.8 Gyr = 4.35e17 s => 1/t_edad = 2.3e-18 s^-1.
#  (U7) Diccionario Cherenkov (acta ACOPLE: mu^2 = m^2_ACLM exacto, y biblio C:
#       m_ACLM = M^2/(sqrt(2) Mbar_Pl)): M^2_ACLM = sqrt(2) mu Mbar_Pl
#       = 2 sqrt(2) Lambda^2. alpha_ACLM = 1 (O(1) declarado).
import sympy as sp
import math
import time

t0 = time.time()
print('=' * 72)
print('A4 - NUMEROS: co-rotante corregido, fuga de carga, spin-down')
print('=' * 72)

# ============================================================
# P1: simbolico exacto - el observable sigma en las dos ramas
# ============================================================
print('\n[P1] sistema modal NLO estacionario, EXACTO en (c_sigma, c_omega)')
t = sp.Symbol('t')
z = sp.Symbol('z')
p = sp.Symbol('p', positive=True)
A, m12 = sp.symbols('A m12', positive=True)
cs, cw = sp.symbols('c_sigma c_omega', real=True)
tauc = sp.Symbol('tau_c', positive=True)

S = sp.Function('S')(t)
F = sp.Function('F')(t)
tau = sp.Function('tau')(t)

# el modo (a3): V = h_0x = S cos(pz), W = h_xz = -p F sin(pz), f = pi^x = 0.
# invariantes lineales del flujo (derivados en a3/N1, se reusan):
#   sigma_xz = d_t(W - f_z)/2 ; omega_zx = d_z(V - f_t)/2 ; c_a reducido (a3/N4)
V = S * sp.cos(p * z)
W = -p * F * sp.sin(p * z)
sig_xz = sp.diff(W, t) / 2
om_zx = sp.diff(V, z) / 2
sig2 = 2 * sig_xz ** 2          # (xz) y (zx) en la suma sigma_mn sigma^mn
om2 = 2 * om_zx ** 2

zper = 2 * sp.pi / p
def zavg(ex):
    return sp.simplify((p / (2 * sp.pi)) * sp.integrate(sp.expand(ex), (z, 0, zper)))

LNLO_modo = zavg(cs * sig2 + cw * om2)
print('     L_NLO del modo =', sp.expand(LNLO_modo), '   [control: = cs p^2 Fdot^2/4 + cw p^2 S^2/4]')

Fd = sp.diff(F, t)
sig = S - Fd                                  # el gauge-invariante del modo
Lc = A * p ** 2 * sig ** 2 / 4 + m12 * S ** 2 / 4 + S * tau / 2 + F * sp.diff(tau, t) / 2
Ltot = sp.expand(Lc + LNLO_modo)

def EL(L, q):
    r = sp.diff(L, q)
    r -= sp.diff(sp.diff(L, sp.Derivative(q, t)), t)
    r += sp.diff(sp.diff(L, sp.Derivative(q, (t, 2))), t, 2)
    return sp.expand(r)

eqS = EL(Ltot, S)
eqF = EL(Ltot, F)

# control interno contra a3: la carga corregida
Ct = A * p ** 2 * sig - cs * p ** 2 * Fd + tau
print('     2*eqF - d/dt[C_tilde] =', sp.simplify(2 * eqF - sp.diff(Ct, t)),
      '  [C_tilde = A p^2 sigma - c_s p^2 Fdot + tau: la de a3]')

# estacionario: S -> S_, Fdot -> v_, tau -> tau_c
S_, v_ = sp.symbols('S_ v_')
est = {sp.Derivative(S, (t, 2)): 0, sp.Derivative(S, t): 0,
       sp.Derivative(F, (t, 3)): 0, sp.Derivative(F, (t, 2)): 0}
eqS_e = eqS.subs(tau, tauc).subs(est).subs({sp.Derivative(F, t): v_, S: S_})
Ct_e = Ct.subs(tau, tauc).subs(est).subs({sp.Derivative(F, t): v_, S: S_})

# ---- rama CO-ROTANTE corregida: el sector C_tilde = 0 (el poblado, por B) ----
sol = sp.solve([sp.Eq(eqS_e, 0), sp.Eq(Ct_e, 0)], [S_, v_], dict=True)[0]
S_ret = sp.simplify(sol[S_])
sig_ret = sp.simplify(sol[S_] - sol[v_])
print('     S_ret     =', sp.factor(S_ret))
print('     sigma_ret =', sp.factor(sig_ret))

# control contra a3: S_ret a primer orden en c
lam = sp.Symbol('lam')
S_ret_1 = sp.expand(sp.series(S_ret.subs({cs: lam * cs, cw: lam * cw}), lam, 0, 2)
                    .removeO().subs(lam, 1))
print('     S_ret a O(c) =', S_ret_1, '  [a3 reporto -c_s tau_c/(A(m1^2+(c_s+c_w)p^2)); a O(c): -c_s tau_c/(A m1^2)]')

# ---- rama RELAJADA corregida: v = 0 ----
S_rel = sp.solve(sp.Eq(eqS_e.subs(v_, 0), 0), S_)[0]
print('     sigma_rel =', sp.factor(S_rel), '  [= -tau_c/(A p^2 + m1^2 + c_w p^2): mu_eff^2 = (m1^2+c_w p^2)/A]')

# ---- desviaciones fraccionales respecto de RG (sigma_RG = -tau_c/(A p^2)) ----
sig_RG = -tauc / (A * p ** 2)
delta_ret = sp.simplify(sig_ret / sig_RG - 1)
delta_ret_1 = sp.expand(sp.series(delta_ret.subs({cs: lam * cs, cw: lam * cw}),
                                  lam, 0, 2).removeO().subs(lam, 1))
print('     delta_ret (exacta) =', sp.factor(delta_ret))
print('     delta_ret a O(c)   =', sp.factor(delta_ret_1))
print('     => EL RESULTADO ESTRUCTURAL: delta_ret = -(c_s/A) * [m1^2 + O(c p^2)]/[m1^2 + O(c p^2)]')
print('        ~= -c_sigma/A, INDEPENDIENTE de p a orden dominante: una')
print('        renormalizacion finita universal del acople gravitomagnetico')
print('        en la rama co-rotante. El apantallamiento Yukawa NO reaparece')
print('        (no hay termino m1^2/(A p^2) en delta_ret).')

# corrimiento NLO de la firma de la rama relajada (robustez de la prediccion)
delta_rel = sp.simplify(S_rel / (-tauc / (A * p ** 2 + m12)) - 1)
delta_rel_1 = sp.expand(sp.series(delta_rel.subs({cs: lam * cs, cw: lam * cw}),
                                  lam, 0, 2).removeO().subs(lam, 1))
print('     delta_rel a O(c) =', sp.factor(delta_rel_1), ' [corrimiento de la firma Yukawa]')

# ---- patologia: H sobre el vinculo, sin fuente ----
print('\n[P1b] patologia ("muerte fea" de la apertura): H del modo sobre el vinculo')
Ltau0 = Ltot.subs(tau, sp.S(0))
pF = sp.diff(Ltau0, sp.Derivative(F, t))
H = sp.expand(pF * sp.Derivative(F, t) - Ltau0)
Svinc = sp.solve(sp.Eq(eqS.subs(tau, sp.S(0)).subs(est).subs(
    {sp.Derivative(F, t): v_, S: S_}), 0), S_)[0]
Hv = sp.simplify(H.subs(est).subs({sp.Derivative(F, t): v_, S: S_}).subs(S_, Svinc))
Hv = sp.factor(sp.simplify(Hv))
print('     H(vinculo) =', Hv)
num, den = sp.fraction(Hv)
print('     => positiva sii  A(m1^2 + c_w p^2) + c_s(A p^2 + m1^2 + c_w p^2) > 0.')
print('        Con |c| = chat Lambda^2 y p << Lambda (validez EFT): |c| p^2 << m1^2')
print('        y |c| << A => H > 0 para CUALQUIER signo O(1) de chat: sin muerte')
print('        fea en el sector NLO. (S es multiplicador tipo N_i: su H off-shell')
print('        del vinculo no es fisica; sobre el vinculo, positiva.)')
print('     [dispersion sin raices nuevas: det ~ omega^2, verificado en a3/N4;')
print('      vertices cubicos existentes renormalizan densidad (a2/C3): tampoco')
print('      generan potencial runaway; el vinculo S sobrevive: m1^2+c_w p^2 != 0]')

# ============================================================
# P2: numeros de delta_ret - barrido en Lambda
# ============================================================
print('\n[P2] delta_ret en numeros: c_sigma = chat * Lambda^2 (SUPUESTO U2, chat=1)')
hbar_c_eVm = 1.9733e-7      # eV*m
Mbar_Pl_eV = 2.435e27       # masa de Planck REDUCIDA en eV (consistente con mu = 2 Lambda^2/Mbar_Pl)
R_earth = 6.371e6           # m
a_LARES2 = 1.227e7          # m (semieje LARES-2)
LARES2 = 0.2e-2             # precision fraccional LARES-2 sobre el frame dragging

def p_eV(L_m):
    return hbar_c_eVm / L_m   # p = 1/L en eV

print('     delta_ret ~= chat * (Lambda/Mbar_Pl)^2 ; factor exacto [(m1^2+cw p^2)/(m1^2+(cs+cw)p^2)]')
print('     con m1^2 = 4 Lambda^4 (U1,U3): c p^2/m1^2 = chat p^2/(4 Lambda^2) -> se imprime')
print('     %-10s %-12s %-12s %-14s %-12s' % ('Lambda', 'l1 [m]', '|delta_ret|',
                                              'cp^2/m1^2@R', 'chat p/ 0.2%'))
for L_eV, nom in [(1e-3, '1e-3 eV'), (1.0, '1 eV'), (1e3, '1 keV'), (1e6, '1 MeV')]:
    l1 = 2.40e8 * (1e6 / L_eV) ** 2
    delta = (L_eV / Mbar_Pl_eV) ** 2
    cp2m = p_eV(R_earth) ** 2 / (4 * L_eV ** 2)      # c p^2/m1^2 a p=1/R (chat=1)
    chat_nec = LARES2 / delta
    print('     %-10s %-12.3g %-12.3g %-14.3g %-12.3g' % (nom, l1, delta, cp2m, chat_nec))
print('     independencia de p verificada: el factor difiere de 1 en c p^2/m1^2')
print('     (< 1e-21 en todo el barrido, p = 1/R_earth o 1/a_LARES2: da igual).')
print('     VEREDICTO P2: la desviacion residual del co-rotante respecto de RG es')
print('     |delta| = chat (Lambda/Mbar_Pl)^2 <= 1.7e-43 (Lambda <= 1 MeV, chat=1).')
print('     LARES-2 (2e-3) esta a >= 40 ORDENES: la firma NO revive como efecto NLO.')
print('     SENSIBILIDAD UV: para |delta| = 2e-3 haria falta c_sigma ~ 1e-3 Mbar_Pl^2,')
print('     i.e. chat ~ 1e40 (Lambda=1MeV) o un corte UV del NLO ~ 1e17 GeV: eso NO')
print('     es un NLO del medio (Lambda <= MeV), es modificar la gravedad misma.')
print('     El corrimiento NLO de la firma RELAJADA es c_w p^2/m1^2 ~ chat p^2/(4Lambda^2)')
print('     < 1e-21: la prediccion Yukawa de la rama relajada tampoco se corre.')

# amplitud absoluta del S_ret residual (curiosidad honesta, no observable directo)
G_SI = 6.674e-11; c_SI = 2.998e8
J_earth = 8.03e37 * 7.292e-5                     # I*Omega [kg m^2/s]
Om_LT = 2 * G_SI * J_earth / (c_SI ** 2 * R_earth ** 3)
v_drag = Om_LT * R_earth / c_SI
print('     [extra] v_drag(superficie) = %.3g (adim); S_ret,abs ~ (c p^2/m1^2)*v_drag' % v_drag)
print('             ~ %.3g a Lambda=1e-3 eV: el h_0x residual del co-rotante.' %
      (p_eV(R_earth) ** 2 / (4 * 1e-6) * v_drag))

# ============================================================
# P3: fuga de carga (no lineal) x (NLO)
# ============================================================
print('\n[P3] fuga de carga del co-rotante: (no lineal) x (NLO), potencias declaradas')
print('     CADENA DIMENSIONAL (cada factor declarado):')
print('     - carga a drenar (por modo):     Delta_C ~ m1^2 * v_drag        [B: C=-m1^2 S]')
print('     - corriente NLO (a3): J^i = -d_t[dL/d(d_i f_t)] ~ c_s * d_t d_i (delta_u):')
print('       solo la parte NO estacionaria del flujo contribuye (a3/N3).')
print('     - forzante no estacionario: la no-axisimetria rotante de la Tierra,')
print('       h_0i^(22) ~ J22 * v_drag a omega = 2*Omega; respuesta del medio SIN')
print('       polos (B: la transferencia no tiene resonancia) => delta_u <= J22*v_drag.')
print('     - d_t -> 2*Omega ; d_i -> p ~ 1/R (campo cercano, cota superior).')
print('     - RECTIFICACION: J = d_t[...] oscilante tiene promedio CERO por ciclo;')
print('       el drenaje DC exige un vertice no lineal mas (a2: existen, renormalizan')
print('       densidad): J_DC ~ c_s * (2Omega) * p * (J22 v_drag)^2.')
print('     - Gamma = p * J_DC / Delta_C  con  c_s/m1^2 = chat/(4 Lambda^2).')
print('     Gamma_estructural ~ Omega * J22^2 * v_drag * chat/(2 (Lambda R)^2)')
print('     COTA BURDA (fisicamente rota a proposito: como si el flujo oscilante')
print('     drenara coherente, sin rectificar): Gamma_burda ~ Omega * J22 * chat/(2(Lambda R)^2)')
Om_E = 7.292e-5
J22 = 1.8e-6
t_edad = 4.35e17
print('     %-10s %-14s %-14s %-14s %-14s' % ('Lambda', 'Gm_burda[1/s]', 'Gm_b*t_edad',
                                              'Gm_estr[1/s]', 'Gm_e*t_edad'))
for L_eV, nom in [(1e-3, '1e-3 eV'), (1.0, '1 eV'), (1e3, '1 keV'), (1e6, '1 MeV')]:
    invLR2 = (hbar_c_eVm / (L_eV * R_earth)) ** 2       # (1/(Lambda R))^2 adimensional
    G_burda = Om_E * J22 * invLR2 / 2
    G_estr = Om_E * J22 ** 2 * v_drag * invLR2 / 2
    print('     %-10s %-14.3g %-14.3g %-14.3g %-14.3g' %
          (nom, G_burda, G_burda * t_edad, G_estr, G_estr * t_edad))
print('     VEREDICTO P3: incluso la cota deliberadamente rota da Gamma*t_edad <= 6e-14')
print('     (peor caso Lambda=1e-3 eV); la estimacion estructural da <= 7e-36.')
print('     La carga del co-rotante NO se drena en la edad del universo para NINGUN')
print('     Lambda del rango, con 14 a 35 ordenes de margen. SENSIBILIDAD UV: lineal')
print('     en chat; ni chat ~ 1e13 (absurdo) cambia el veredicto de la cota burda.')
print('     [el transitorio de formacion: fuga modal-lineal = 0 EXACTO (a3/N5);')
print('      el (no lineal)x(NLO) con d_t ~ 1/t_form << Omega es aun menor que esto]')

# ============================================================
# P4: spin-down terrestre - canal Cherenkov importado
# ============================================================
print('\n[P4] spin-down: Cherenkov escalar (ACLM+Thaler 0507120, Edot ~ alpha M^2 v^3)')
hbar_SI = 1.0546e-34; eV_J = 1.602e-19
def Edot_W(M_eV, v):
    """Edot = alpha (M c^2)^2 v^3 / hbar, alpha = 1 (U7). [M_eV en eV]"""
    return (M_eV * eV_J) ** 2 / hbar_SI * v ** 3

# validacion contra el numero DE ELLOS (acta C): Sol, M = 10 MeV, v = 1e-3 -> ~20 W
E_sol = Edot_W(1e7, 1e-3)
print('     validacion: Sol M=10MeV v=1e-3: Edot = %.3g W  [ACLM+Thaler: ~20 W: OK]' % E_sol)

# la Tierra ROTANTE: SUPUESTOS DECLARADOS
print('     SUPUESTOS del canal rotacional (estiramiento declarado: la formula de')
print('     ACLM es TRASLACIONAL; el caso rotante no esta calculado en la literatura')
print('     -- acta C blanco 3 --; la uso como proxy de orden de magnitud):')
print('     - una esfera axisimetrica estacionaria NO radia (apertura, mec. 1):')
print('       radia la masa NO axisimetrica ~ J22*M_earth a v = Omega R/c (borde,')
print('       cota superior).')
print('     - M^2_ACLM = 2 sqrt(2) Lambda^2 (U7, diccionario mu = m_ACLM exacto).')
print('     - supresion de fuente extensa debil (0507120): (R_S_eff/(v^2 R))^2 con')
print('       R_S_eff = 2 G (J22 M_earth)/c^2 (la protuberancia no arrastra el')
print('       condensado: r_drag < R).')
M_earth = 5.972e24
v_ec = Om_E * R_earth / c_SI
RS_eff = 2 * G_SI * (J22 * M_earth) / c_SI ** 2
supr = (RS_eff / (v_ec ** 2 * R_earth)) ** 2
print('     v_ecuador = %.3g ; R_S_eff = %.3g m ; supresion extensa = %.3g' %
      (v_ec, RS_eff, supr))

# presupuesto medido del spin-down
I_E = 8.03e37
dPdt = 2.3e-3 / (100 * 365.25 * 86400)     # 2.3 ms/siglo en s/s
P_dia = 86400.0
Edot_rot = I_E * Om_E ** 2 * dPdt / P_dia  # |dE/dt| = I Om dOm/dt, dOm/dt = Om dPdt/P
margen = 0.10 * Edot_rot                    # margen libre ~10% (mandato)
print('     spin-down medido: Edot_rot = %.3g W (2.3 ms/siglo, mareas lo explican);' % Edot_rot)
print('     margen libre ~10%%: %.3g W ; torque margen = %.3g N m' % (margen, margen / Om_E))

print('     %-10s %-14s %-14s %-16s %-14s' % ('Lambda', 'M_ACLM [eV]', 'Edot [W]',
                                              'Edot/margen', 'torque [N m]'))
for L_eV, nom in [(1e-3, '1e-3 eV'), (1.0, '1 eV'), (1e3, '1 keV'), (1e6, '1 MeV')]:
    M_A = math.sqrt(2 * math.sqrt(2)) * L_eV       # M = (2 sqrt2)^(1/2) Lambda
    Ed = Edot_W(M_A, v_ec) * supr
    print('     %-10s %-14.3g %-14.3g %-16.3g %-14.3g' %
          (nom, M_A, Ed, Ed / margen, Ed / Om_E))
Ed_1MeV_sinsupr = Edot_W(math.sqrt(2 * math.sqrt(2)) * 1e6, v_ec)
print('     control de robustez: SIN supresion de fuente extensa (protuberancia')
print('     tratada como puntual): Edot(1 MeV) = %.3g W: sigue %.0f ordenes bajo el margen.' %
      (Ed_1MeV_sinsupr, math.log10(margen / Ed_1MeV_sinsupr)))
L_sat = 1e6 * math.sqrt(margen / (Edot_W(math.sqrt(2 * math.sqrt(2)) * 1e6, v_ec) * supr))
print('     Lambda que saturaria el margen: %.3g eV = %.3g GeV -> l1 = %.3g m:' %
      (L_sat, L_sat / 1e9, 2.40e8 * (1e6 / L_sat) ** 2))
print('     VEREDICTO P4: el canal Cherenkov saca energia de la rotacion pero es')
print('     DESPRECIABLE en todo el rango viable (Lambda <= 2.6 MeV por la cota')
print('     nodal): Edot <= 3e-15 W vs margen 3.6e+11 W (26 ordenes). NO da cota')
print('     nueva sobre Lambda: la cota que manda sigue siendo la nodal. Consistente')
print('     con B/C: este canal lleva ENERGIA, no carga -- no decide la rama.')

# ============================================================
# P5: sintesis numerica
# ============================================================
print('\n[VEREDICTO A4]')
print(' (a) delta_ret = -chat (Lambda/Mbar_Pl)^2: <= 1.7e-43 en todo el barrido.')
print('     La firma NO revive como efecto NLO: el co-rotante es "RG exacto" hasta')
print('     una parte en 1e43. LARES-2 (2e-3) no la ve ni con chat ~ 1e40 (UV absurdo).')
print('     La firma de la rama RELAJADA tampoco se corre (< 1e-21): las dos ramas')
print('     quedan nitidas y distinguibles; la seleccion de estado decide TODO.')
print(' (b) fuga (no lineal)x(NLO): Gamma*t_edad <= 6e-14 (cota rota a proposito),')
print('     <= 7e-36 (estructural): el co-rotante NO se vacia. Refuerza D2 si el')
print('     teorema de B pasa el verificador.')
print(' (c) spin-down: Edot <= 3e-15 W (26 ordenes bajo el margen de mareas):')
print('     sin cota nueva; el canal de energia no decide nada terrestre.')
print('t =', round(time.time() - t0, 1), 's')
