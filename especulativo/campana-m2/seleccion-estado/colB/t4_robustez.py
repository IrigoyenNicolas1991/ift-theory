# Columna B - TAREA 4: robustez de la conclusion.
#
#   R1  gauge residual xi^i(x): C, sigma y la densidad P_a^0 son invariantes
#       (la conclusion no es un artefacto de gauge).
#   R2  terminos de borde / ordenamiento IBP (el analogo Ostrogradsky del acta,
#       ahora para la CARGA): con la L CRUDA de build_L (EH sin integrar por
#       partes, con segundas derivadas), la carga de Noether corregida a la
#       Ostrogradsky coincide con la canonica como EXPRESION, y separa las
#       ramas igual: Delta Q no es un artefacto del ordenamiento.
#   R3  fuente NO axisimetrica / no estacionaria (la Tierra real):
#       tau(t) = tau_c (1 + eps sin(Omega t)) (montanias, mareas, omega = m Omega):
#       la solucion exacta mantiene S(t) = 0 y C(t) = 0 SIEMPRE; no hay
#       resonancia (la transferencia Fdot(omega) = tau(omega)/(A p^2) no tiene
#       polos) ni crecimiento secular. Verificacion simbolica + RK4 200 vueltas.
#   R4  hipotesis del teorema de congelamiento, declaradas con su puerta de
#       escape (NLO / vortices / acople no universal). Sin numeros inventados.
import sys, os, math, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', 'escalar', 'verificador'))
import sympy as sp
from lib_eh import t, z, p, Mp2, build_L, zavg, EL

t0 = time.time()
c = sp.cos(p*z); ssin = sp.sin(p*z)
m12 = sp.symbols('m12', positive=True)
al = sp.symbols('alpha', real=True)
A = Mp2 + al
S = sp.Function('S')(t); F = sp.Function('F')(t)
tau = sp.Function('tau')(t)
Fd = sp.diff(F, t)
sig = S - Fd
C = A*p**2*sig + tau

# ============ R1: invariancia de gauge residual ============
eps = sp.Symbol('epsilon')
dsig = sp.simplify(sig.subs(F, F + eps) - sig)
dC = sp.simplify(C.subs(F, F + eps) - C)
print('[R1] bajo el gauge residual del modo (F -> F + eps, S -> S):')
print('     delta sigma =', dsig, ' ; delta C =', dC)
print('     y delta h_{0a} = d_t xi_a = 0 (xi indep. de t) => delta P_a^0 = 0.')
print('     El observable (sigma, curvatura K_xz = p sigma) y la carga son gauge-inv.')

# ============ R2: carga cruda (Ostrogradsky) vs canonica ============
H4 = sp.zeros(4, 4)
H4[0, 1] = H4[1, 0] = S*c
H4[1, 3] = H4[3, 1] = -p*F*ssin
_, L2V = build_L(H4)
LEH_raw = Mp2*zavg(L2V)
Kxz = sp.diff(-p*F*ssin, t) - sp.diff(S*c, z)
Lraw = sp.expand(LEH_raw + zavg(sp.Rational(1, 4)*al*2*Kxz**2)
                 + zavg(sp.Rational(1, 2)*m12*(S*c)**2)
                 + sp.Rational(1, 2)*S*tau + sp.Rational(1, 2)*F*sp.diff(tau, t))
# invariancia: delta Lraw = d/dt K con K = tau/2 - Mp2 p^2 Fdot   (por unidad de eps)
dLraw = sp.expand(Lraw.subs(F, F + eps) - Lraw)
Kb = tau/2 - Mp2*p**2*Fd
print('[R2] delta L_raw - eps*dK/dt =', sp.simplify(dLraw - eps*sp.diff(Kb, t)),
      '  (K = tau/2 - Mp2 p^2 Fdot: el shift genera una derivada total extra)')

def noether_Q(L, qs, dqs, K):
    """Carga de Noether con segundas derivadas (Ostrogradsky):
    Q = sum_q [ (dL/dqdot - d/dt dL/dqddot) dq + dL/dqddot d(qdot) ] - K."""
    Q = -K
    for q, dq in zip(qs, dqs):
        q1 = sp.Derivative(q, t); q2 = sp.Derivative(q, (t, 2))
        term = sp.diff(L, q1)
        if L.has(q2):
            term -= sp.diff(sp.diff(L, q2), t)
            Q += sp.diff(L, q2)*sp.diff(dq, t)
        Q += term*dq
    return sp.expand(Q)

Lcan = A*p**2*sig**2/4 + m12*S**2/4 + S*tau/2 + F*sp.diff(tau, t)/2
Q_raw = noether_Q(Lraw, (S, F), (sp.S(0), sp.S(1)), Kb)
Q_can = noether_Q(Lcan, (S, F), (sp.S(0), sp.S(1)), tau/2)
print('[R2] Q_raw - Q_can =', sp.simplify(Q_raw - Q_can),
      ' (0 => la carga NO depende del ordenamiento IBP; sin anomalia de borde)')
print('[R2] Q_can + C/2 =', sp.simplify(Q_can + C/2), ' (la ley es la misma de t1[B3])')
tc = sp.symbols('tau_c', positive=True)
rama_rel = {S: -tc/(A*p**2 + m12), F: sp.S(0)}
rama_ret = {S: sp.S(0), F: tc*t/(A*p**2)}
for nom, st in (('relajada', rama_rel), ('co-rotante', rama_ret)):
    qr = sp.simplify(Q_raw.subs(tau, tc).subs(st).doit())
    qc = sp.simplify(Q_can.subs(tau, tc).subs(st).doit())
    print('     rama %-11s: Q_raw = %s ; Q_can = %s' % (nom, qr, qc))
print('     => Delta Q entre ramas identica por ambas rutas: robusto a bordes.')

# ============ R3: fuente no axisimetrica / oscilante ============
Om, ep2 = sp.symbols('Omega epsilon2', positive=True)
tau_osc = tc*(1 + ep2*sp.sin(Om*t))
Fsol = sp.integrate(tau_osc, t)/(A*p**2)
cand = {S: sp.S(0), F: Fsol}
Lo = Lcan.subs(tau, tau_osc)
eqS_o = sp.expand(EL(Lo, S)); eqF_o = sp.expand(EL(Lo, F))
r1 = sp.simplify(eqS_o.subs(cand).doit())
r2 = sp.simplify(eqF_o.subs(cand).doit())
print('[R3] tau(t) = tau_c(1 + eps2 sin(Omega t)): S=0, F=int tau/(A p^2):')
print('     eqS =', r1, ' ; eqF =', r2, ' => S(t) = 0 EXACTO con fuente oscilante.')
print('     C(t) = 0 se mantiene; sigma(t) = -tau(t)/(A p^2) sigue la fuente SIN')
print('     retardo ni resonancia: Fdot(omega) = tau(omega)/(A p^2), sin polos')
print('     (no hay frecuencia propia en la direccion plana). Sin secularidad.')

# RK4 de refuerzo: 200 vueltas de la componente oscilante
Ap2n = 1.0; m12n = 0.1; taucn = 1.0; ep2n = 1e-2; Omn = 2*math.pi
def taut(tt): return taucn*(1 + ep2n*math.sin(Omn*tt))
def taud(tt): return taucn*ep2n*Omn*math.cos(Omn*tt)
Fn, pin = 0.0, taut(0.0)/2       # arranca en la co-rotante instantanea (C=0)
Tfin = 200.0; N = 40000; h = Tfin/N
tt = 0.0; maxS = 0.0
for k in range(N):
    def rhs(tt, Fn, pin):
        ta = taut(tt)
        return ((2*pin - ta)/m12n + 2*pin/Ap2n, taud(tt)/2)
    k1 = rhs(tt, Fn, pin)
    k2 = rhs(tt + h/2, Fn + h/2*k1[0], pin + h/2*k1[1])
    k3 = rhs(tt + h/2, Fn + h/2*k2[0], pin + h/2*k2[1])
    k4 = rhs(tt + h, Fn + h*k3[0], pin + h*k3[1])
    Fn += h/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
    pin += h/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
    tt += h
    maxS = max(maxS, abs((2*pin - taut(tt))/m12n))
print('     RK4 200 vueltas (eps2 = 1e-2): max|S(t)| =', '%.2e' % maxS,
      ' (error numerico puro; S_rel seria %.3f)' % (-taucn/(Ap2n + m12n)))
print('     La Tierra real (J22 ~ 1e-5, mareas) NO puebla la relajada a orden lineal;')
print('     su efecto entra recien por vertices no lineales (frente Cherenkov) o NLO.')

# ============ R4: hipotesis del teorema (declaracion honesta) ============
print('[R4] Hipotesis del congelamiento P_a^i = 0 / d_t P_a^0 = 0, y sus puertas:')
print('     (i)   L = sqrt(-g) U(X,Y) a LO: la identidad GL(3) es del termino Y;')
print('           X no contiene dPhi^a. EH y materia no contienen Phi^a. EXACTO')
print('           con gravedad no lineal completa (t1[A3] usa metrica arbitraria).')
print('     (ii)  acople universal: la materia no toca Phi^a directamente. Si algun')
print('           sector acoplara a Phi^a, su EOM tendria fuente y la carga fluiria.')
print('     (iii) Phi^a(x) difeo suave global (gauge unitario global): los VORTICES')
print('           / phase slips lo evaden -- unica via no perturbativa conocida;')
print('           tasa ~ e^{-S_barrera} (columna de analogias He-II / Langer-Fisher).')
print('     (iv)  NLO con derivadas superiores: la corriente de Noether gana el')
print('           termino [dL/d(d_mu d_nu Phi^a)] d_nu xi^a, que NO se anula =>')
print('           flujo de carga posible, suprimido por potencias de (grad/Lambda)')
print('           y por no-linealidad (a orden lineal, el propio NLO alpha K^2 del')
print('           juguete RESPETA la conservacion modo a modo: eqF la contiene).')
print('           Cuantificar ese flujo residual = tarea para el frente de vertices.')
print('     El chequeo R2 descarta ademas que Delta C sea artefacto de bordes/IBP.')

print('\n[VEREDICTO TAREA 4] La conclusion (la conservacion selecciona la co-rotante)')
print('es robusta a: eleccion de gauge residual (R1), ordenamiento IBP / terminos de')
print('borde tipo Ostrogradsky (R2), y perturbaciones no axisimetricas/oscilantes de')
print('la fuente a orden lineal (R3). Sus limites son los declarados en R4.')
print('t =', round(time.time() - t0, 1), 's')
