# Columna B - TAREA 2: el IVP ADIABATICO del modo plano vectorial.
# Fuente tau(t) = f(t/T) tau_c con T -> infinito (formacion planetaria, T ~ 1e8 anios).
# La direccion plana NO tiene gap => no hay teorema adiabatico estandar. Pregunta:
# a que estado llega el medio cuando T >> todo? depende de T, de la historia f, o es
# universal?
#
#   S1  solucion candidata universal S(t)=0, F=int tau/(A p^2): residuos de las DOS
#       EOMs con tau(t) ARBITRARIA (no solo lenta) -> 0.
#   S2  solucion GENERAL del sistema (S auxiliar + F): S(t) = const = -C/m1^2 con
#       C fijada por las condiciones iniciales; F esclava de la historia integrada.
#       NO hay frecuencias propias: el modo plano es holonomico (primer orden), no
#       un oscilador de gap cero. Por eso no hace falta teorema adiabatico: la
#       solucion es UNICA (mod gauge) dada la historia y las CI.
#   S3  formulacion canonica con tau(t): H = (2pi-tau)^2/(4 m1^2) + pi^2/(A p^2)
#       - F taudot/2 ; Hamilton == Lagrange; pidot = taudot/2 EXACTA =>
#       pi(t) = pi_0 + [tau(t)-tau(0)]/2. Con CI relajadas: pi = tau/2 = rama
#       co-rotante EN TODO INSTANTE (no solo al final).
#   S4  RK4 numerico: 4 historias f (suave, rampa, tanh, no-monotona con
#       oscilaciones) x 4 valores de T (1 a 1e6): el estado final es IDENTICO
#       (co-rotante) con error solo numerico. + corrida con CI no relajadas:
#       el final depende SOLO de C, no de la historia ni de T.
#   S5  energia: H(C;tau) = C^2/(4m1^2) + (tau-C)^2/(4Ap^2). El minimo GLOBAL en C
#       es C_rel (la relajada), pero C esta congelada: a C=0 el co-rotante es el
#       UNICO estado del sector (su "vacio"). H(0;tau) = H_ret; H(C_rel;tau) = H_min
#       (los 0.250 vs 0.227 de v2b con los numeros de test).
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

# Lagrangiano canonico verificado (t1 [B1], = v2 [2] con tau(t) generica)
L = A*p**2*sig**2/4 + m12*S**2/4 + S*tau/2 + F*sp.diff(tau, t)/2
eqS = sp.expand(EL(L, S))
eqF = sp.expand(EL(L, F))

# ---- S1: la candidata universal, tau(t) ARBITRARIA ----
cand = {S: sp.S(0), F: sp.integrate(tau, t)/(A*p**2)}
r1 = sp.simplify(eqS.subs(cand).doit())
r2 = sp.simplify(eqF.subs(cand).doit())
print('[S1] S=0, F=int tau/(A p^2) con tau(t) ARBITRARIA: eqS =', r1, ', eqF =', r2)
print('     => la co-rotante instantanea es solucion EXACTA para CUALQUIER historia,')
print('        rapida o lenta: no es un limite adiabatico, es una identidad.')

# ---- S2: solucion general -> S constante fijada por la carga ----
# vinculo (eqS): S = (A p^2 Fdot - tau)/(A p^2 + m1^2)
Ssol = sp.solve(eqS, S)[0]
print('[S2] vinculo: S =', sp.simplify(Ssol))
# eqF reducida: sustituyo S y obtengo la EOM de F sola
eqF_red = sp.expand(eqF.subs(S, Ssol).doit())
print('[S2] eqF reducida / (Fddot - taudot/(A p^2)) =',
      sp.simplify(eqF_red/(sp.diff(F, t, 2) - sp.diff(tau, t)/(A*p**2))))
# solucion general: Fdot(t) = Fdot0 + [tau(t)-tau0]/(A p^2)
Fdot0, tau_0 = sp.symbols('Fdot0 tau0')
Fdot_gen = Fdot0 + (tau - tau_0)/(A*p**2)
S_gen = sp.simplify(Ssol.subs(Fd, Fdot_gen))
print('[S2] S a lo largo de la solucion general =', S_gen)
C_ini = A*p**2*(sp.Symbol('S0') - Fdot0) + tau_0     # carga con S0 = S(t0)
# con S0 = S_gen(t0): consistencia
S0v = S_gen  # es constante
C_val = sp.simplify((A*p**2*(S_gen - Fdot_gen) + tau))
print('[S2] C a lo largo de la solucion general =', C_val, ' (constante) ;')
print('     -m1^2 * S_gen =', sp.simplify(-m12*S_gen), '  => S = -C/m1^2 SIEMPRE.')
print('     La historia f y la escala T NO aparecen: el estado esta 1-1 con la carga C.')

# ---- S3: canonico con tau(t) ----
piv, Sv, Fdv, Fv = sp.symbols('piv Sv Fdv Fv')
pi_c = sp.diff(L, Fd)
pi_sym = pi_c.subs({S: Sv, Fd: Fdv})
Fd_of = sp.solve(sp.Eq(pi_sym, piv), Fdv)[0]
Hfull = sp.expand(piv*Fd_of - L.subs({S: Sv, F: Fv, Fd: Fdv}).subs(Fdv, Fd_of))
solSv = sp.solve(sp.diff(Hfull, Sv), Sv)[0]
Hred = sp.simplify(Hfull.subs(Sv, solSv))
Hclaim = (2*piv - tau)**2/(4*m12) + piv**2/(A*p**2) - Fv*sp.diff(tau, t)/2
print('[S3] H(pi,F;t) - claim =', sp.simplify(Hred - Hclaim))
print('[S3] pidot = -dH/dF =', sp.simplify(-sp.diff(Hred, Fv)),
      ' => pi(t) = pi0 + [tau(t)-tau(0)]/2 EXACTA, cualquier historia.')
print('[S3] con CI relajadas (pi0=0, tau(0)=0): pi(t) = tau(t)/2 = rama co-rotante')
print('     INSTANTANEA en todo t (v2b: pi_ret = tau/2). El medio "sigue" a la fuente.')

# ---- S4: RK4, 4 historias x 4 escalas T ----
print('[S4] RK4 del sistema canonico (Fdot = dH/dpi, pidot = taudot/2):')
Ap2n = 1.0; m12n = 0.1; tauc = 1.0     # numeros de test de v2/v2b (Mp2=1, al=0, p=1)

def historias():
    fs = {
        'coseno-suave': (lambda u: (1 - math.cos(math.pi*u))/2,
                         lambda u: math.pi*math.sin(math.pi*u)/2),
        'rampa-lineal': (lambda u: u, lambda u: 1.0),
        'tanh':         (lambda u: math.tanh(4*u)/math.tanh(4.0),
                         lambda u: (4/math.cosh(4*u)**2)/math.tanh(4.0)),
        'no-monotona':  (lambda u: u + 0.3*math.sin(6*math.pi*u)*(1 - u),
                         lambda u: 1 + 0.3*(6*math.pi*math.cos(6*math.pi*u)*(1 - u)
                                            - math.sin(6*math.pi*u))),
    }
    return fs

def rk4(Tn, f, fp, pi0=0.0, F0=0.0, N=4000):
    """integra en [0, Tn]; tau(t) = tauc*f(t/Tn), taudot = tauc*fp(t/Tn)/Tn."""
    h = Tn/N
    Fn, pin = F0, pi0
    def taut(tt): return tauc*f(min(tt/Tn, 1.0))
    def taud(tt): return tauc*fp(min(tt/Tn, 1.0))/Tn
    def rhs(tt, Fn, pin):
        ta = taut(tt)
        Fdot = (2*pin - ta)/m12n + 2*pin/Ap2n
        pidot = taud(tt)/2
        return Fdot, pidot
    tt = 0.0
    maxdev = 0.0
    for k in range(N):
        k1 = rhs(tt, Fn, pin)
        k2 = rhs(tt + h/2, Fn + h/2*k1[0], pin + h/2*k1[1])
        k3 = rhs(tt + h/2, Fn + h/2*k2[0], pin + h/2*k2[1])
        k4 = rhs(tt + h, Fn + h*k3[0], pin + h*k3[1])
        Fn += h/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
        pin += h/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
        tt += h
        maxdev = max(maxdev, abs(pin - taut(tt)/2))
    return Fn, pin, maxdev

S_rel = -tauc/(Ap2n + m12n)
print('     (S_relajada = %+.6f seria la firma Yukawa; S_corotante = 0)' % S_rel)
print('     %-14s %-10s %-12s %-12s %-12s' % ('historia', 'T', 'S_final', 'Fdot*Ap2/tau-1', 'max|pi-tau/2|'))
univ_ok = True
for nom, (f, fp) in historias().items():
    for Tn in (1.0, 10.0, 1e3, 1e6):
        Fn, pin, maxdev = rk4(Tn, f, fp)
        ta = tauc
        Sfin = (2*pin - ta)/m12n
        Fdfin = (2*pin - ta)/m12n + 2*pin/Ap2n
        dev = Fdfin*Ap2n/tauc - 1
        univ_ok = univ_ok and abs(Sfin) < 1e-9 and abs(dev) < 1e-9
        print('     %-14s %-10g %-12.3e %-12.3e %-12.3e' % (nom, Tn, Sfin, dev, maxdev))
print('[S4] estado final = CO-ROTANTE para toda historia y todo T ?', univ_ok)
print('     max|pi - tau/2| ~ error RK4: el sistema esta en la co-rotante instantanea')
print('     DURANTE todo el encendido, no solo al final. UNIVERSAL: no depende de T')
print('     ni de f. (El teorema adiabatico no hace falta: no hay dinamica propia.)')

# CI no relajadas: el final depende SOLO de C
print('[S4b] CI no relajadas pi0 != 0 (carga C = -2 pi0 congelada):')
for pi0 in (0.05, -0.02):
    Fn, pin, _ = rk4(1e3, *historias()['coseno-suave'], pi0=pi0)
    Sfin = (2*pin - tauc)/m12n
    Cn = -2*pi0          # C = tau - 2pi ; en t=0: tau=0 => C = -2 pi0
    print('      pi0=%+.3f: S_final = %+.6f ; -C/m1^2 = %+.6f ; dif = %.1e'
          % (pi0, Sfin, -Cn/m12n, abs(Sfin + Cn/m12n)))
print('      => el estado final esta etiquetado por C y NADA MAS.')

# ---- S5: energia por sector de carga ----
Cs, taus = sp.symbols('C tau', real=True)
# estado de carga C: S=-C/m1^2, sigma=(C-tau)/(A p^2), pi=(tau-C)/2
Hsec = ((2*((taus - Cs)/2) - taus)**2/(4*m12) + ((taus - Cs)/2)**2/(A*p**2))
Hsec = sp.simplify(Hsec)
print('[S5] H(C;tau) =', sp.simplify(Hsec), ' = C^2/(4m1^2) + (tau-C)^2/(4Ap^2) ?',
      sp.simplify(Hsec - (Cs**2/(4*m12) + (taus - Cs)**2/(4*A*p**2))) == 0)
Cmin = sp.solve(sp.diff(Hsec, Cs), Cs)[0]
print('[S5] argmin_C H =', sp.simplify(Cmin), ' = C_relajada (t1 [B5]) ?',
      sp.simplify(Cmin - m12*taus/(A*p**2 + m12)) == 0)
num = {Mp2: 1, al: 0, p: 1, m12: sp.Rational(1, 10), taus: 1}
print('[S5] H(C=0) =', float(Hsec.subs(Cs, 0).subs(num)),
      ' (= H_ret 0.250 de v2b) ; H(C_rel) =',
      round(float(Hsec.subs(Cs, Cmin).subs(num)), 6), ' (= H_min 0.227 de v2b)')
print('[S5] la "energia extra" del co-rotante vive en OTRO sector de carga: no es')
print('     un estado excitado sobre el mismo vacio, es el FUNDAMENTAL del sector C=0.')
print('     Liberarla exige cambiar C: prohibido a LO (t1). Sin canal, no hay decaimiento.')

print('\n[VEREDICTO TAREA 2] El encendido LENTO (y el rapido, y cualquiera) termina en')
print('la CO-ROTANTE: resultado UNIVERSAL, independiente de T y de la historia f.')
print('No hay teorema adiabatico porque no hace falta: el modo plano no tiene dinamica')
print('propia (holonomico); su estado es esclavo de la carga conservada, y la carga')
print('inicial cosmologica es CERO = la carga de la co-rotante.')
print('t =', round(time.time() - t0, 1), 's')
