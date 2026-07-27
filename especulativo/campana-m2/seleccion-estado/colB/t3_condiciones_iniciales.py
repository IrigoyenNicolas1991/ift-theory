# Columna B - TAREA 3: condiciones iniciales REALES (FRW) + tareas 1 y 2
# => cual rama selecciona la historia, SIN invocar disipacion.
#
#   F1  la carga vectorial sobre CUALQUIER fondo FRW es CERO EXACTO:
#       P_a^0 = sqrt(-g) U_Y g_{0a}/(g_00 sqrt(-g_00)) (formula cerrada t1[A4],
#       exacta) y en FRW g_{0a} = 0. No es una aproximacion: es identidad.
#       (La carga que el acta FRW siguio, J = a^3(U_Y - 2 phidot U_X), es la del
#        RELOJ Phi^0 -> Phi^0 + c: otra simetria. La nuestra es la espacial.)
#   F2  cualquier carga vectorial primordial se DILUYE: d_mu P_a^mu = 0 con
#       P_a^mu = rho_a u^mu sqrt(-g) (t1[A2]: P_a^mu solo tiene componente de
#       flujo) => en FRW comovil rho_a prop a^-3. La expansion prepara carga 0.
#   F3  el matiz del acta, resuelto con la formula EXACTA:
#       - rama CO-ROTANTE: h_{0i} = 0 => P_a^0 = 0 PUNTO A PUNTO Y EXACTO (no
#         es "carga neta cero por compensacion": es densidad identicamente nula).
#         El encendido de la fuente la puebla sin costo de carga (t2).
#       - rama RELAJADA: P_a^0 = -U_Y S(x) != 0 localmente (neta global 0,
#         dipolar, t1[B6]): ES una redistribucion. Poblarla desde carga 0
#         exigiria TRANSPORTAR carga de un punto a otro, y el vehiculo no
#         existe: P_a^i = 0 identicamente (t1[A3]). Prohibido a LO aun siendo
#         redistribucion. [El temor de la apertura era el caso inverso.]
#   F4  contraste materia/medio: la MATERIA si transporta su momento
#       (T^{zx} != 0 mientras taudot != 0); el MEDIO no puede transportar su
#       carga. Por eso la fuente puede formarse y el medio queda clavado en
#       carga cero: co-rotante.
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', 'escalar', 'verificador'))
import sympy as sp
from lib_eh import t, z, p, Mp2, zavg

t0 = time.time()

# ---------- F1: P_a^0 = 0 exacto sobre FRW ----------
s = sp.Symbol('s')
a_ = sp.Function('a', positive=True)(t)
aa = sp.Symbol('a', positive=True)                 # a(t) en un instante: valor generico

def Y_de(dP, g):
    u1, u2, u3 = sp.symbols('u1 u2 u3')
    v = sp.Matrix([1, u1, u2, u3])
    eqs = [sum(v[mu]*dP[am, mu] for mu in range(4)) for am in (1, 2, 3)]
    solu = sp.solve(eqs, [u1, u2, u3], dict=True)
    vsol = v.subs(solu[0])
    N = (vsol.T*g*vsol)[0, 0]
    return (1/sp.sqrt(-N))*sum(vsol[mu]*dP[0, mu] for mu in range(4))

gFRW = sp.diag(-1, aa**2, aa**2, aa**2)
ok_F1 = True
for am in (1, 2, 3):
    dPU = sp.eye(4)
    dPU[am, 0] = dPU[am, 0] + s
    val = sp.simplify(sp.diff(Y_de(dPU, gFRW), s).subs(s, 0))
    ok_F1 = ok_F1 and (val == 0)
print('[F1] dY/d(d_0 Phi^a) sobre FRW (las 3 componentes) = 0 ?', ok_F1)
print('     => P_a^0 = 0 EXACTO en todo FRW, toda epoca, todo a(t): el universo en')
print('        expansion entrega el medio con carga vectorial IDENTICAMENTE NULA.')
print('     (formula cerrada: P_a^0 prop g_{0a} = 0 en FRW; y el acta FRW ya dio el')
print('      fondo relajado J=0 para la carga del reloj: CI totales = carga cero.)')

# ---------- F2: dilucion a^-3 de una carga primordial ----------
rho = sp.Function('rho')(t)
sqrtg = a_**3
# P^mu = rho u^mu sqrt(-g), u = (1,0,0,0) comovil  =>  d_mu P^mu = d_t(rho a^3)
cons = sp.expand(sp.diff(rho*sqrtg, t))
sol = sp.dsolve(sp.Eq(cons, 0), rho)
print('[F2] d_mu(rho a^3 u^mu) = 0  =>', sol, ' => rho prop a^-3: cualquier carga')
print('     vectorial primordial se diluye con la expansion (mismo destino que la J')
print('     del reloj en el acta FRW). Refuerza: C(t_formacion) = 0.')

# ---------- F3: el matiz, con la formula exacta ----------
S, Fam = sp.symbols('S F_amp', real=True)
UYs = sp.Symbol('U_Y', positive=True)
h00v, h0av = sp.symbols('h00 h0a', real=True)
P0_exacto = UYs*h0av/((-1 + h00v)*sp.sqrt(1 - h00v))     # sin el factor sqrt(-g): prop g_{0a}
print('[F3] P_a^0 exacto prop g_{0a}:')
print('     co-rotante: h_{0i} = 0 (S=0)  => P_a^0 =', sp.simplify(P0_exacto.subs(h0av, 0)),
      ' PUNTO A PUNTO, EXACTO (no hay nada que compensar: densidad nula).')
P0_rel = sp.series(P0_exacto.subs({h0av: S*sp.cos(p*z), h00v: 0}), S, 0, 2).removeO()
print('     relajada:   P_a^0 =', sp.expand(P0_rel), ' + O(S^2) != 0 localmente')
print('     (con S = -tau_c/(A p^2 + m1^2): perfil dipolar, neta global 0, t1[B6]).')
print('     => la RELAJADA es la redistribucion; la CO-ROTANTE es carga cero genuina.')
print('     Poblar la relajada desde carga 0 = transportar carga entre puntos, y')
print('     P_a^i = 0 (t1[A3]): NO EXISTE la corriente que lo haga a LO.')

# ---------- F4: la materia si transporta; el medio no ----------
tau = sp.Function('tau')(t)
c = sp.cos(p*z); ss = sp.sin(p*z)
T0x = tau*c
Txz = -(sp.diff(tau, t)/p)*ss
print('[F4] conservacion materia: d_t T^{0x} + d_z T^{zx} =',
      sp.simplify(sp.diff(T0x, t) + sp.diff(Txz, z)),
      ' con T^{zx} != 0 mientras taudot != 0:')
print('     la materia redistribuye SU momento al formarse la Tierra; la carga del')
print('     medio no tiene vehiculo. El medio queda en su sector C=0: co-rotante.')

print('\n[VEREDICTO TAREA 3] La historia cosmologica (FRW relajado, carga cero exacta,')
print('F1-F2) + el encendido de la fuente (universal, t2) seleccionan la CO-ROTANTE,')
print('sin invocar disipacion. El matiz del acta queda respondido AL REVES del temor')
print('de la apertura: la co-rotante NO es la que requiere carga (requiere carga CERO,')
print('que es lo que hay); la RELAJADA es la redistribucion imposible de crear')
print('suavemente. El argumento de conservacion SI cortocircuita -- hacia D2, no D1.')
print('Puertas que quedan (declaradas): NLO con derivadas superiores (corriente de')
print('carga de orden superior), defectos/vortices de Phi (no perturbativo), y estados')
print('"relajada + nube compensante estacionaria" (no son la rama Yukawa limpia y no')
print('resultan de ningun decaimiento suave del co-rotante).')
print('t =', round(time.time() - t0, 1), 's')
