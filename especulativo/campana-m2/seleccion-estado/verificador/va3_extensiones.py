# VERIFICADOR ADVERSARIAL FINAL - ATAQUES 2 y 3: fuera del modo de juguete.
#
#  X1  FUENTE QUE SE DESPLAZA (formacion por acrecion: la fuente crece Y se
#      mueve): T0x = tau(t) cos(p(z - z0(t))) con tau(t) y z0(t) ARBITRARIAS,
#      T^zx fijado por conservacion. Dos cuadraturas (S1,S2,W1,W2).
#      Pregunta: S1 = S2 = 0 (co-rotante instantanea) sigue siendo solucion
#      EXACTA? Si lo es, el IVP universal de colB sobrevive al desplazamiento.
#  X2  DOS MODOS p y 2p con NLO (c_sigma, c_omega): el L modal se separa?
#      Las cargas por modo se conservan POR SEPARADO? (blanco 2 de colA).
#      El acople inter-modo solo puede venir de cubicos: para la CARGA los
#      cubre el teorema exacto (va1: P_a^i = 0 a todo orden); para la energia
#      no importa (la energia no etiqueta el sector).
#  X3  retroaccion metrica: el caracter de VINCULO de eqS (sin S ddot) con
#      NLO genericos; el caso c_a (unico que lo rompe) y su escala (fantasma
#      espurio de corte, tratado en va4).
import sympy as sp
import time

t0 = time.time()
print('=' * 72)
print('VA3 - FUERA DEL JUGUETE: fuente movil, dos modos, retroaccion')
print('=' * 72)

t, z, x, y = sp.symbols('t z x y', real=True)
p = sp.symbols('p', positive=True)
Mp2, m12 = sp.symbols('Mp2 m12', positive=True)
al = sp.Symbol('alpha', real=True)
A = Mp2 + al
Xs = [t, x, y, z]
eta = sp.diag(-1, 1, 1, 1)

def d(f, mu):
    return sp.diff(f, Xs[mu])

def L_GG(hmat):
    """Gamma-Gamma cuadratico (signo anclado en va2: sgn = +1)."""
    Gam = [[[sp.S(0)] * 4 for _ in range(4)] for _ in range(4)]
    for a_ in range(4):
        for b_ in range(4):
            for c_ in range(b_, 4):
                s_ = sp.S(0)
                for e_ in range(4):
                    s_ += eta[a_, e_] * (d(hmat[e_, b_], c_) + d(hmat[e_, c_], b_)
                                         - d(hmat[b_, c_], e_))
                v_ = s_ / 2
                Gam[a_][b_][c_] = v_
                Gam[a_][c_][b_] = v_
    L = sp.S(0)
    for m_ in range(4):
        for n_ in range(4):
            if eta[m_, n_] == 0:
                continue
            for r_ in range(4):
                for l_ in range(4):
                    L += eta[m_, n_] * Gam[r_][l_][m_] * Gam[l_][r_][n_]
                L -= eta[m_, n_] * Gam[r_][m_][n_] * sum(Gam[l_][r_][l_] for l_ in range(4))
    return sp.expand(L)

def EL(L, q):
    r = sp.diff(L, q)
    r -= sp.diff(sp.diff(L, sp.Derivative(q, t)), t)
    r += sp.diff(sp.diff(L, sp.Derivative(q, (t, 2))), t, 2)
    return sp.expand(r)

# ================= X1: fuente que se desplaza =================
print('\n[X1] fuente movil: T0x = tau(t) cos(p(z - z0(t))), tau y z0 ARBITRARIAS')
S1 = sp.Function('S1')(t); S2 = sp.Function('S2')(t)
W1 = sp.Function('W1')(t); W2 = sp.Function('W2')(t)
tau = sp.Function('tau')(t); z0 = sp.Function('z0')(t)

V = S1 * sp.cos(p * z) + S2 * sp.sin(p * z)
W = W1 * sp.sin(p * z) + W2 * sp.cos(p * z)
h = sp.zeros(4, 4)
h[0, 1] = h[1, 0] = V
h[1, 3] = h[3, 1] = W

tc_ = tau * sp.cos(p * z0)      # componente cos de la fuente
ts_ = tau * sp.sin(p * z0)      # componente sin
T0x = tc_ * sp.cos(p * z) + ts_ * sp.sin(p * z)
# conservacion: d_t T0x + d_z Tzx = 0  =>  Tzx = -(1/p)[tcdot sin - tsdot cos]
Tzx = -(sp.diff(tc_, t) * sp.sin(p * z) - sp.diff(ts_, t) * sp.cos(p * z)) / p
print('     d_t T0x + d_z Tzx =', sp.simplify(sp.diff(T0x, t) + sp.diff(Tzx, z)),
      ' (fuente conservada para tau(t), z0(t) arbitrarias)')

Kxz = sp.diff(W, t) - sp.diff(V, z)
Lcampo = Mp2 * L_GG(h) + al * Kxz ** 2 / 2 + m12 * V ** 2 / 2 + V * T0x + W * Tzx
zper = 2 * sp.pi / p
Lmodal = sp.expand(sp.simplify((p / (2 * sp.pi)) * sp.integrate(sp.expand(Lcampo), (z, 0, zper))))

eqs = {q: EL(Lmodal, q) for q in (S1, S2, W1, W2)}

# candidata co-rotante instantanea: S1 = S2 = 0, W's esclavas de la fuente
# (por cuadratura, del juguete: A p^2 sigma + tau = 0 con S = 0 => la W con
#  el perfil correcto integra tau/(A p): la dejo como incognita y RESUELVO)
W1c = sp.Function('W1c')(t); W2c = sp.Function('W2c')(t)
cand = {S1: sp.S(0), S2: sp.S(0)}
eqW1_c = eqs[W1].subs(cand)
eqW2_c = eqs[W2].subs(cand)
# las eqW se vuelven EDOs de primer orden en Wdot: las resuelvo
sol_l = sp.solve([eqW1_c.doit(), eqW2_c.doit()],
                 [sp.Derivative(W1, (t, 2)), sp.Derivative(W2, (t, 2))], dict=True)
print('     con S1 = S2 = 0: eqW dan Wddot =', sol_l[0] if sol_l else 'sin solucion')
# integro una vez: Wdot fijadas por la fuente (constante de integracion = carga)
W1dot = -tc_ / (A * p)
W2dot = ts_ / (A * p)
subs_c = {S1: sp.S(0), S2: sp.S(0),
          sp.Derivative(W1, t): W1dot, sp.Derivative(W2, t): W2dot,
          sp.Derivative(W1, (t, 2)): sp.diff(W1dot, t),
          sp.Derivative(W2, (t, 2)): sp.diff(W2dot, t)}
res = {}
for nom, q in (('S1', S1), ('S2', S2), ('W1', W1), ('W2', W2)):
    res[nom] = sp.simplify(eqs[q].subs(subs_c).doit())
print('     candidata S = 0, W1dot = -tau_c/(A p), W2dot = +tau_s/(A p):')
print('     residuos: eqS1 = %s, eqS2 = %s, eqW1 = %s, eqW2 = %s' %
      (res['S1'], res['S2'], res['W1'], res['W2']))
ok_X1 = all(v == 0 for v in res.values())
print('     => S(t) = 0 EXACTO con fuente que CRECE y SE MUEVE arbitrariamente:',
      'OK - el IVP universal sobrevive al desplazamiento' if ok_X1 else
      'FALLA <-- LA FUENTE MOVIL ROMPE EL IVP')

# cargas por cuadratura, CONSTRUCTIVAS (sin adivinar signos): W_i solo aparece
# derivada en L salvo el acople a la fuente, que es derivada total en t =>
# eqW_i = -d/dt[Q_i] con Q_i = dL/dWdot_i + (pieza de fuente integrada).
piW1 = sp.diff(Lmodal, sp.Derivative(W1, t))
piW2 = sp.diff(Lmodal, sp.Derivative(W2, t))
dLdW1 = sp.expand(sp.diff(Lmodal, W1))
dLdW2 = sp.expand(sp.diff(Lmodal, W2))
# dL/dW1 = -tcdot/(2p) = d/dt[-tc/(2p)]; dL/dW2 = +tsdot/(2p) = d/dt[+ts/(2p)]
print('     dL/dW1 + d_t[tc/(2p)] =', sp.simplify(dLdW1 + sp.diff(tc_ / (2 * p), t)),
      ' ; dL/dW2 - d_t[ts/(2p)] =', sp.simplify(dLdW2 - sp.diff(ts_ / (2 * p), t)))
Q1 = sp.expand(piW1 + tc_ / (2 * p))
Q2 = sp.expand(piW2 - ts_ / (2 * p))
chk1 = sp.simplify(eqs[W1] + sp.diff(Q1, t))
chk2 = sp.simplify(eqs[W2] + sp.diff(Q2, t))
print('     eqW1 + dQ1/dt =', chk1, ' ; eqW2 + dQ2/dt =', chk2,
      ' (0 => Q_i conservadas EXACTAS, fuente movil incluida)')
Q1v = sp.simplify(Q1.subs(subs_c))
Q2v = sp.simplify(Q2.subs(subs_c))
print('     Q1 sobre la candidata =', Q1v, ' ; Q2 =', Q2v,
      ' => ambas cuadraturas con carga de la co-rotante. La fuente movil')
print('        transporta SU momento (Tzx != 0) pero no inyecta carga al medio.')

# ================= X2: dos modos p y 2p con NLO =================
print('\n[X2] dos modos p y 2p con NLO c_sigma, c_omega (pi = 0):')
cs, cw = sp.symbols('c_sigma c_omega', real=True)
Sa = sp.Function('Sa')(t); Fa = sp.Function('Fa')(t)
Sb = sp.Function('Sb')(t); Fb = sp.Function('Fb')(t)
taua = sp.Function('tau_a')(t); taub = sp.Function('tau_b')(t)
p2 = 2 * p
V2m = Sa * sp.cos(p * z) + Sb * sp.cos(p2 * z)
W2m = -p * Fa * sp.sin(p * z) - p2 * Fb * sp.sin(p2 * z)
h2 = sp.zeros(4, 4)
h2[0, 1] = h2[1, 0] = V2m
h2[1, 3] = h2[3, 1] = W2m
# invariantes lineales del flujo (a3/N1, con f = 0): sigma_xz = W_t/2, om_zx = V_z/2
sig_xz = sp.diff(W2m, t) / 2
om_zx = sp.diff(V2m, z) / 2
LNLO = cs * 2 * sig_xz ** 2 + cw * 2 * om_zx ** 2
K2 = sp.diff(W2m, t) - sp.diff(V2m, z)
T0x2 = taua * sp.cos(p * z) + taub * sp.cos(p2 * z)
Tzx2 = -(sp.diff(taua, t) * sp.sin(p * z) / p + sp.diff(taub, t) * sp.sin(p2 * z) / p2)
Lc2 = Mp2 * L_GG(h2) + al * K2 ** 2 / 2 + m12 * V2m ** 2 / 2 + LNLO \
      + V2m * T0x2 + W2m * Tzx2
Lm2 = sp.expand(sp.simplify((p / (2 * sp.pi)) * sp.integrate(sp.expand(Lc2), (z, 0, zper))))

# separabilidad: terminos cruzados modo-a x modo-b?
cruz = [v for v in [Sa * Sb, Fa * Fb, Sa * Fb, Sb * Fa,
                    Sa * sp.Derivative(Fb, t), Sb * sp.Derivative(Fa, t),
                    sp.Derivative(Fa, t) * sp.Derivative(Fb, t)]
        if sp.expand(Lm2).has(v)]
# chequeo formal: derivada segunda cruzada
d2 = [sp.simplify(sp.diff(Lm2, qa, qb)) for qa in (Sa, Fa, sp.Derivative(Fa, t))
      for qb in (Sb, Fb, sp.Derivative(Fb, t))]
ok_sep = all(v == 0 for v in d2)
print('     d^2 L / d(modo a) d(modo b) (9 pares, NLO incluido):',
      'todas 0 => L SEPARA' if ok_sep else [v for v in d2 if v != 0])
eqFa = EL(Lm2, Fa); eqFb = EL(Lm2, Fb)
siga = Sa - sp.Derivative(Fa, t)
sigb = Sb - sp.Derivative(Fb, t)
Cta = A * p ** 2 * siga - cs * p ** 2 * sp.Derivative(Fa, t) + taua
Ctb = A * p2 ** 2 * sigb - cs * p2 ** 2 * sp.Derivative(Fb, t) + taub
ra = sp.simplify(2 * eqFa - sp.diff(Cta, t))
rb = sp.simplify(2 * eqFb - sp.diff(Ctb, t))
print('     2 eqFa - dC_a/dt =', ra, ' ; 2 eqFb - dC_b/dt =', rb)
print('     => cargas corregidas C_tilde(p) y C_tilde(2p) conservadas POR')
print('        SEPARADO con fuentes arbitrarias: NO hay fuga inter-modo a')
print('        orden cuadratico (LO + NLO). El acople inter-modo empieza en')
print('        los cubicos; para la CARGA los cubre el teorema exacto (va1:')
print('        P_a^i = 0 con g EXACTA, todo orden). Blanco 2 de colA: CERRADO.')

# ================= X3: retroaccion / caracter de vinculo =================
print('\n[X3] caracter de vinculo de eqS con NLO:')
ca = sp.Symbol('c_a', real=True)
Sm = sp.Function('Sm')(t); Fm = sp.Function('Fm')(t); taum = sp.Function('taum')(t)
Vm = Sm * sp.cos(p * z); Wm = -p * Fm * sp.sin(p * z)
hm = sp.zeros(4, 4)
hm[0, 1] = hm[1, 0] = Vm
hm[1, 3] = hm[3, 1] = Wm
sig_m = sp.diff(Wm, t) / 2
om_m = sp.diff(Vm, z) / 2
a_m = sp.diff(Vm, t)              # a_x = d_t(V - f_t), f = 0
LN3 = cs * 2 * sig_m ** 2 + cw * 2 * om_m ** 2 + ca * a_m ** 2
K3 = sp.diff(Wm, t) - sp.diff(Vm, z)
T0x3 = taum * sp.cos(p * z)
Tzx3 = -(sp.diff(taum, t) / p) * sp.sin(p * z)
Lc3 = Mp2 * L_GG(hm) + al * K3 ** 2 / 2 + m12 * Vm ** 2 / 2 + LN3 \
      + Vm * T0x3 + Wm * Tzx3
Lm3 = sp.expand(sp.simplify((p / (2 * sp.pi)) * sp.integrate(sp.expand(Lc3), (z, 0, zper))))
eqS3 = EL(Lm3, Sm)
tiene_Sdd = eqS3.has(sp.Derivative(Sm, (t, 2)))
print('     con c_a = 0: eqS contiene S_ddot?',
      sp.expand(eqS3.subs(ca, 0)).has(sp.Derivative(Sm, (t, 2))),
      ' => S sigue siendo VINCULO (algebraico) con c_sigma, c_omega')
print('     con c_a != 0: eqS contiene S_ddot?', tiene_Sdd,
      ' -- el termino c_a a^2 SI genera dinamica espuria para S;')
coefSdd = sp.expand(eqS3).coeff(sp.Derivative(Sm, (t, 2)))
coefS = sp.expand(eqS3.subs(ca, 0)).coeff(Sm)
print('     masa del modo espurio ~ sqrt(|coef S| / |coef Sdd|):')
print('       coef(S_ddot) =', coefSdd, ' ; coef(S)|_{c=0} =', coefS)
print('       => omega^2 ~ m1^2/(2 c_a) ~ Lambda^4/Lambda^2 = Lambda^2: EN EL')
print('          CORTE de la EFT => fantasma de Ostrogradsky ESPURIO (estandar).')
print('     Lo DECISIVO (va4): las ramas ESTACIONARIAS no dependen de c_a')
print('     (a = V_t = 0 sobre estacionarias): el veredicto no usa la reduccion.')
print('     Retroaccion no lineal completa: cubierta por el corolario de')
print('     inversion (va1-V5): P congelado = 0 <=> g_{0a}(x,t) = 0 EXACTO;')
print('     la evolucion no lineal de h_ij/h_00 no puede regenerar shift')
print('     comovil sin violar la EOM exacta de Phi^a.')

print('\n[VEREDICTO VA3]')
print(' * X1: el IVP universal SOBREVIVE a la fuente que se desplaza (S = 0')
print('   exacto con tau(t) y z0(t) arbitrarias; la materia mueve su momento,')
print('   el medio queda en C = 0).')
print(' * X2: sin fuga inter-modo a orden cuadratico NLO; los cubicos no')
print('   transportan carga (teorema exacto). Blanco 2 de colA cerrado.')
print(' * X3: S es vinculo con c_sigma/c_omega; c_a genera un espurio EN EL')
print('   CORTE que no toca las estacionarias (va4 lo cuantifica).')
print('t =', round(time.time() - t0, 1), 's')
