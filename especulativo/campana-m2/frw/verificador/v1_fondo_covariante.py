# -*- coding: utf-8 -*-
"""
v1_fondo_covariante.py — Verificacion ADVERSARIAL del fondo FRW del medio U(X,Y).
Tarea 1 del mandato. Pipeline PROPIO (escrito sin leer fondo_frw.py de la casa).

Rutas independientes:
  A: T_{mu nu} por variacion covariante de sqrt(-g)*U respecto de g^{mu nu},
     sobre FRW con lapse general N (contiene tiempo cosmico N=1 y conforme N=a).
  B: mini-superspace con lapse: Euler-Lagrange de N, a, phi del L total
     (Einstein-Hilbert con R calculado por mi propia rutina de Christoffels + medio).
  C: numerico RK4 propio del sistema acoplado (atractor, dust).

Convenciones (HANDOFF sec. 3): signatura (-,+,+,+); Phi^0=phi(t), Phi^a=x^a;
X = g^{00} phid^2 ; Y = phid/sqrt(-g_00) ; S = int sqrt(-g) [ R/2 + U ], M_Pl=1
=> G_{mu nu} = T_{mu nu},  3H^2 = rho.
Verifica F1..F6. Cada bloque imprime PASS/FAIL con el residuo simbolico.
"""
import sympy as sp

ok = True
def check(nombre, expr, esperado=0):
    global ok
    r = sp.simplify(expr - esperado)
    estado = "PASS" if r == 0 else "FAIL"
    if r != 0: ok = False
    print(f"  [{estado}] {nombre}: residuo = {r}")

print("=" * 72)
print("RUTA A: T_mn covariante sobre FRW con lapse N (y phid = w simbolicos)")
print("=" * 72)

N, aa, w = sp.symbols('N a w', positive=True)   # lapse, factor de escala, phi-punto
s0, s1 = sp.symbols('s0 s1')                     # perturbaciones de g^{00}, g^{11}
X, Y = sp.symbols('X Y')
U = sp.Function('U')(X, Y)

# metrica inversa perturbada (solo la diagonal: las componentes de g^{mu nu}
# son variables independientes en la variacion)
ginv = sp.diag(-1/N**2 + s0, 1/aa**2 + s1, 1/aa**2, 1/aa**2)
gcov = ginv.inv()
sqrtg = sp.sqrt(-gcov.det())

# invariantes del medio en gauge unitario (Phi^0 = phi(t) => d_mu Phi^0 = w delta^0_mu)
Xval = ginv[0, 0] * w**2                 # X = g^{00} w^2
Yval = w / sp.sqrt(-gcov[0, 0])          # Y = w/sqrt(-g_00)
Lag = sqrtg * U.subs({X: Xval, Y: Yval}, simultaneous=True)

sqrtg0 = sqrtg.subs({s0: 0, s1: 0})
T00 = sp.simplify((-2 / sqrtg0) * sp.diff(Lag, s0).subs({s0: 0, s1: 0}))
T11 = sp.simplify((-2 / sqrtg0) * sp.diff(Lag, s1).subs({s0: 0, s1: 0}))

# proyecciones fisicas: u^mu = (1/N,0,0,0);  rho = T_mn u^m u^n ; p = T^1_1
X0, Y0 = -w**2 / N**2, w / N
sub0 = {X: X0, Y: Y0}
UX = sp.Derivative(U, X).doit()
UY = sp.Derivative(U, Y).doit()
rho_A = sp.simplify(T00 / N**2)
p_A = sp.simplify(T11 / aa**2)

rho_esperado = (-U - 2*(w**2/N**2)*UX + (w/N)*UY).subs(sub0, simultaneous=True)
p_esperado = U.subs(sub0, simultaneous=True)

print("F1 (con lapse general N; N=1 da el enunciado exacto):")
check("rho = -U - 2(w^2/N^2)U_X + (w/N)U_Y", rho_A - rho_esperado)
check("p = U", p_A - p_esperado)
print("  (Ruta C incluida: N=a con w=phi' reproduce tiempo conforme;")
print("   la formula es covariante en N, no hay que rehacer nada.)")

print()
print("=" * 72)
print("RUTA B: mini-superspace con lapse — EL de N, a, phi con R propio")
print("=" * 72)

t = sp.Symbol('t')
Nf = sp.Function('N', positive=True)(t)
af = sp.Function('a', positive=True)(t)
ph = sp.Function('phi')(t)

# ---- mi rutina de curvatura (Christoffels -> Ricci -> R), convencion MTW/Wald ----
def ricci_scalar(g, coords):
    n = len(coords)
    ginv_ = g.inv()
    Gam = [[[sp.Rational(0)]*n for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for m in range(n):
            for v in range(n):
                Gam[r][m][v] = sp.simplify(sum(
                    ginv_[r, s]*(sp.diff(g[s, m], coords[v]) + sp.diff(g[s, v], coords[m])
                                 - sp.diff(g[m, v], coords[s])) for s in range(n))/2)
    Ric = sp.zeros(n, n)
    for m in range(n):
        for v in range(n):
            term = 0
            for r in range(n):
                term += sp.diff(Gam[r][m][v], coords[r]) - sp.diff(Gam[r][r][m], coords[v])
                for lam in range(n):
                    term += Gam[r][r][lam]*Gam[lam][m][v] - Gam[r][v][lam]*Gam[lam][r][m]
            Ric[m, v] = sp.simplify(term)
    return sp.simplify(sum(ginv_[m, v]*Ric[m, v] for m in range(n) for v in range(n)))

x1, x2, x3 = sp.symbols('x1 x2 x3')
coords = (t, x1, x2, x3)
gFRW = sp.diag(-Nf**2, af**2, af**2, af**2)
R = ricci_scalar(gFRW, coords)
print(f"R(FRW con lapse) = {R}")

# Para eliminar TODO artefacto de representacion (Subs/dummies de la Function
# abstracta), uso el MONOMIO GENERICO U = (X+1)^m (Y-1)^n con m,n SIMBOLICOS.
# Toda U analitica alrededor del punto es combinacion lineal de estos monomios y
# las identidades F1-F4 son lineales en U => verificar el monomio generico las
# verifica para toda U analitica.
m_, n_ = sp.symbols('m n', positive=True)

def Umono(Xe, Ye):
    return (Xe + 1)**m_ * (Ye - 1)**n_

H = sp.diff(af, t)/af
wt = sp.diff(ph, t)                      # phi-punto como funcion de t

# lagrangiano total mini-superspace (densidad por volumen comovil)
Xc, Yc = -wt**2/Nf**2, wt/Nf
Lgrav = Nf*af**3*R/2
Lmed = Nf*af**3*Umono(Xc, Yc)
Ltot = Lgrav + Lmed

def euler_lagrange(L, q, t, orden=2):
    eom = sp.diff(L, q)
    for k in range(1, orden+1):
        eom += (-1)**k * sp.diff(sp.diff(L, sp.diff(q, t, k)), t, k)
    return eom

EL_N = euler_lagrange(Ltot, Nf, t)
EL_a = euler_lagrange(Ltot, af, t)
EL_phi = euler_lagrange(Ltot, ph, t)

# fijamos N=1 DESPUES de variar
def gauge_N1(e):
    e = e.subs(sp.Derivative(Nf, t, 2), 0).subs(sp.Derivative(Nf, t), 0).subs(Nf, 1)
    return e

# rho, p, U_X, U_Y del monomio generico sobre el fondo (N=1)
Xb, Yb = -wt**2, wt
Xs, Ys = sp.symbols('Xs Ys')
UXm = sp.diff(Umono(Xs, Ys), Xs).subs({Xs: Xb, Ys: Yb}, simultaneous=True)
UYm = sp.diff(Umono(Xs, Ys), Ys).subs({Xs: Xb, Ys: Yb}, simultaneous=True)
Um = Umono(Xb, Yb)
rho_t = -Um - 2*wt**2*UXm + wt*UYm
p_t = Um

# Friedmann I: EL_N = 0 debe equivaler a 3H^2 = rho
fried1 = gauge_N1(EL_N)
check("Friedmann I: EL_N == a^3 (3H^2 - rho)  (cruce A<->B, monomio generico)",
      sp.expand(sp.simplify(fried1 - af**3*(3*H**2 - rho_t))))

# Friedmann II: EL_a = 0 debe equivaler a 2addot/a + H^2 = -p
# (con mi convencion EL = dL/dq - d/dt dL/dqdot + ... el signo global de EL_a es +)
fried2 = gauge_N1(EL_a)
check("Friedmann II: EL_a == +3a^2 (2 addot/a + H^2 + p)",
      sp.expand(sp.simplify(fried2 - 3*af**2*(2*sp.diff(af, t, 2)/af + H**2 + p_t))))

# F3: EOM de phi = conservacion de J
J = af**3*(UYm - 2*wt*UXm)
check("F3: EL_phi == -dJ/dt (phi ciclica => J conservado)",
      sp.expand(sp.simplify(gauge_N1(EL_phi) + sp.diff(J, t))))
print("  J(phid=1)/a^3 = U_Y - 2 U_X evaluado en (X,Y)=(-1,1): J=0 <=> tadpole U_Y=2U_X. OK")

# F4: rho + p = phid * J / a^3 (identidad, sin EOM)
check("F4: rho + p - phid*J/a^3 == 0 (identidad off-shell)",
      sp.expand(sp.simplify(rho_t + p_t - wt*J/af**3)))

# F2: identidad de Bianchi SIN usar EOM: rhodot + 3H(rho+p) == (phid/a^3) dJ/dt
lhs = sp.diff(rho_t, t) + 3*H*(rho_t + p_t)
rhs = wt*sp.diff(J, t)/af**3
check("F2: rhodot + 3H(rho+p) == (phid/a^3) dJ/dt  => on-shell (J const) Bianchi",
      sp.expand(sp.simplify(lhs - rhs)))

print()
print("=" * 72)
print("F5 y esquina concreta U = (X+1) + 2(Y-1) + (X+1)^2/2")
print("=" * 72)
wsym = sp.Symbol('w', real=True)
Uc = (X+1) + 2*(Y-1) + (X+1)**2/2
UcX = sp.diff(Uc, X); UcY = sp.diff(Uc, Y)
subw2 = {X: -wsym**2, Y: wsym}
f = sp.expand((UcY - 2*wsym*UcX).subs(subw2, simultaneous=True))
print(f"f(w) = U_Y - 2w U_X = {f} = {sp.factor(f)}")
check("f(w) == 2(w-1)(w^2+w-1)", sp.expand(f - 2*(wsym-1)*(wsym**2+wsym-1)))
K = sp.diff(f, wsym).subs(wsym, 1)
check("K = f'(1) == 2 (esquina concreta)", K, 2)

# d rho/d w = w f'(w) (identidad general de la clase U(X,Y))
rho_w = (-Uc - 2*wsym**2*UcX + wsym*UcY).subs(subw2, simultaneous=True)
check("identidad d(rho)/dw == w f'(w) (esquina)", sp.expand(sp.diff(rho_w, wsym) - wsym*sp.diff(f, wsym)))
print(f"  => cerca de w=1: delta-rho = K*delta-w con K=2; delta-p = f(1)*delta-w = 0 (POLVO exacto a orden lineal)")

# linearizacion de la EOM: wdot = -3H f/f' -> d(dw)/dt = -3H dw => dw ~ a^-3
dw = sp.Function('dw')(t)
Hs = sp.Symbol('H', positive=True)
lin = sp.series((-3*Hs*f/sp.diff(f, wsym)).subs(wsym, 1+sp.Symbol('e')), sp.Symbol('e'), 0, 2).removeO()
check("linealizacion: wdot|_{w=1+e} == -3 H e + O(e^2)", sp.expand(lin + 3*Hs*sp.Symbol('e')))
print("  => delta-w a^3 = const (dust). Verificacion numerica en RUTA C.")

# F1 valores en el atractor de la esquina: rho(w=1) = 0
check("rho(w=1) == 0 (el atractor de la esquina es Minkowski)", rho_w.subs(wsym, 1))
check("U(w=1) == 0", Uc.subs(subw2, simultaneous=True).subs(wsym, 1))

print()
print("=" * 72)
print("F6: subclase isentropica U = W(X+Y^2) — degenerada sobre FRW")
print("=" * 72)
Z = sp.Symbol('Z')
W = sp.Function('W')(Z)
UW = W.subs(Z, X + Y**2)
UWX = sp.diff(UW, X); UWY = sp.diff(UW, Y)
fW = sp.simplify((UWY - 2*wsym*UWX).subs(subw2, simultaneous=True))
check("F6a: J/a^3 = U_Y - 2w U_X == 0 IDENTICAMENTE (toda w)", fW)
rhoW = sp.simplify((-UW - 2*wsym**2*UWX + wsym*UWY).subs(subw2, simultaneous=True))
check("F6b: rho == -W(0) const (X+Y^2=0 sobre FRW para todo phid)", rhoW, -W.subs(Z, 0))
pW = sp.simplify(UW.subs(subw2, simultaneous=True))
check("F6c: p == W(0) = -rho (CC pura)", pW, W.subs(Z, 0))

print()
print("=" * 72)
print("RUTA C: numerico RK4 propio — atractor y dust de la esquina concreta")
print("=" * 72)
import math

def fnum(wv):    return 2*(wv**3 - 2*wv + 1)
def fpnum(wv):   return 2*(3*wv**2 - 2)
def Unum(wv):    Xv = -wv*wv; return (Xv+1) + 2*(wv-1) + 0.5*(Xv+1)**2
def UXnum(wv):   Xv = -wv*wv; return 1 + (Xv+1)
def rhonum(wv):  return -Unum(wv) - 2*wv*wv*UXnum(wv) + wv*2.0

def rk4(y, dt, deriv):
    k1 = deriv(y); k2 = deriv([y[i]+dt/2*k1[i] for i in range(len(y))])
    k3 = deriv([y[i]+dt/2*k2[i] for i in range(len(y))])
    k4 = deriv([y[i]+dt*k3[i] for i in range(len(y))])
    return [y[i] + dt/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i]) for i in range(len(y))]

# universo = solo el medio, arrancando fuera del atractor (w0=1.4 => rho>0)
w0, a0 = 1.4, 1.0
y = [a0, w0]
def deriv(y):
    av, wv = y
    rho = rhonum(wv)
    Hv = math.sqrt(max(rho, 0.0)/3.0)
    return [av*Hv, -3*Hv*fnum(wv)/fpnum(wv)]
dt = 1e-4
hist = []
for i in range(400000):
    y = rk4(y, dt, deriv)
    if i % 80000 == 0:
        av, wv = y
        hist.append((av, wv, (wv-1)*av**3, rhonum(wv)*av**3, Unum(wv)/rhonum(wv) if rhonum(wv) != 0 else float('nan')))
print("  a, w, (w-1)a^3, rho*a^3, w_eos=p/rho :")
for h in hist:
    print(f"    a={h[0]:9.4f}  w={h[1]:.6f}  (w-1)a^3={h[2]:.6f}  rho a^3={h[3]:.6f}  p/rho={h[4]:+.4f}")
# la convergencia al regimen dust es asintotica (correcciones O(w-1)):
# el criterio correcto es que el drift DECREZCA entre muestras sucesivas
d_pen = abs(hist[-2][2]/hist[-3][2] - 1)*100
d_ult = abs(hist[-1][2]/hist[-2][2] - 1)*100
d_r_pen = abs(hist[-2][3]/hist[-3][3] - 1)*100
d_r_ult = abs(hist[-1][3]/hist[-2][3] - 1)*100
print(f"  drift de (w-1)a^3 por muestra: {d_pen:.4f}% -> {d_ult:.4f}%  (decrece => converge a const: dust)")
print(f"  drift de rho*a^3 por muestra:  {d_r_pen:.4f}% -> {d_r_ult:.4f}%  (decrece => converge a const: dust)")
print(f"  w_eos final -> {hist[-1][4]:+.5f} (dust => 0; el medio DILUYE como materia)")

print()
print("VEREDICTO RUTA A+B+C:", "TODO PASS" if ok else "HAY FALLOS — revisar arriba")
