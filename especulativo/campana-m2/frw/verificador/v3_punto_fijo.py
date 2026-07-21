# -*- coding: utf-8 -*-
"""
v3_punto_fijo.py — Tarea 3: los puntos fijos de la esquina concreta
U = (X+1) + 2(Y-1) + (X+1)^2/2  sobre FRW (J/a^3 = f(w) -> 0 en expansion).

f(w) = U_Y - 2w U_X|_{X=-w^2,Y=w} = 2(w^3 - 2w + 1) = 2(w-1)(w^2+w-1).
OJO: la cubica tiene TRES raices reales (el mandato lista dos):
  w1 = 1, w2 = (sqrt5-1)/2 ~ 0.618, w3 = -(1+sqrt5)/2 ~ -1.618.

(a) estabilidad y cuencas; singularidades de la EOM en f'(w)=0 (w=+-sqrt(2/3));
(b) rho, p, U exactos en cada punto (w2: AdS-like? chequear +-0.045);
(c) genericidad del segundo punto en la clase U(X,Y).
Numerica: RK4 propio con  adot = aH, Hdot = -(rho+p)/2, wdot = -3Hf/f'
(constraint 3H^2 = rho_tot monitoreada; dust opcional).
Convenciones: M_Pl=1, 3H^2 = rho. Todo PASS/FAIL con residuo simbolico.
"""
import sympy as sp
import math

ok = True
def check(nombre, expr, esperado=0):
    global ok
    r = sp.simplify(sp.expand(expr - esperado))
    estado = "PASS" if r == 0 else "FAIL"
    if r != 0: ok = False
    print(f"  [{estado}] {nombre}: residuo = {r}")

w = sp.Symbol('w', real=True)
X, Y = sp.symbols('X Y')
Uc = (X + 1) + 2*(Y - 1) + (X + 1)**2/2
sub = {X: -w**2, Y: w}
UX = sp.diff(Uc, X).subs(sub, simultaneous=True)
UY = sp.diff(Uc, Y).subs(sub, simultaneous=True)
Ub = Uc.subs(sub, simultaneous=True)
f = sp.expand(UY - 2*w*UX)
fp = sp.diff(f, w)
rho = sp.expand(-Ub - 2*w**2*UX + w*UY)
p = sp.expand(Ub)

print("=" * 72)
print("(b) puntos fijos exactos y sus rho, p, U")
print("=" * 72)
raices = sp.solve(f, w)
raices = sorted(raices, key=lambda r: float(r))
print(f"  raices de f(w) = {sp.factor(f)}:")
w3_, w2_, w1_ = raices   # ordenadas: -(1+s5)/2, (s5-1)/2, 1
check("raiz 1 == 1", w1_ - 1)
check("raiz 2 == (sqrt5-1)/2", w2_ - (sp.sqrt(5) - 1)/2)
check("raiz 3 == -(1+sqrt5)/2  [TERCERA raiz, no listada en el mandato]",
      w3_ + (1 + sp.sqrt(5))/2)
for nombre, r_ in (("w1 = 1", w1_), ("w2 = (sqrt5-1)/2", w2_), ("w3 = -(1+sqrt5)/2", w3_)):
    Uv = sp.simplify(Ub.subs(w, r_)); rv = sp.simplify(rho.subs(w, r_)); pv = sp.simplify(p.subs(w, r_))
    print(f"  {nombre}:  U = {sp.nsimplify(Uv)} = {float(Uv):+.6f} ; rho = {float(rv):+.6f} ; p = {float(pv):+.6f}")
check("en w2: U == (5*sqrt5-11)/4 (exacto)", sp.simplify(Ub.subs(w, w2_) - (5*sp.sqrt(5) - 11)/4))
check("en w2: rho == -U (w_eos = -1 exacto)", sp.simplify((rho + Ub).subs(w, w2_)))
check("numeros del mandato: U(w2) ~ +0.045, rho(w2) ~ -0.045",
      sp.Integer(0 if abs(float(Ub.subs(w, w2_)) - 0.045) < 1e-3 else 1))
print("  => w2 es un punto w_eos=-1 con rho<0: CC NEGATIVA (AdS-like).")
print("     w3 es un punto w_eos=-1 con rho>0: CC POSITIVA (dS-like), pero con")
print(f"     phid<0 (flecha del reloj del medio invertida) y U_X = {float(UX.subs(w, w3_)):+.4f} < 0")
print("     => m1^2_efectivo = 2U_X < 0 en ese fondo: sector vectorial enfermo ahi.")
check("rho+p == w*f (identidad, cualquier w)", sp.expand(rho + p - w*f))
check("rho(w1) == 0 (atractor de tadpoles = Minkowski)", rho.subs(w, w1_))

print()
print("=" * 72)
print("(a) estabilidad: linealizacion y cuencas")
print("=" * 72)
# EOM del fondo: d/dt[a^3 f(w)] = 0 => wdot = -3H f/f'. En una raiz SIMPLE w*:
# wdot = -3H (w-w*) + O((w-w*)^2)  (el f' se cancela) => delta-w ~ a^{-3} si H>0.
e = sp.Symbol('e')
for nombre, r_ in (("w1", w1_), ("w2", w2_), ("w3", w3_)):
    Hs = sp.Symbol('H', positive=True)
    serie = sp.series((-3*Hs*f/fp).subs(w, r_ + e), e, 0, 2).removeO()
    check(f"{nombre}: wdot|_(w*+e) == -3 H e + O(e^2)  [atractor local si H>0, repulsor si H<0]",
          sp.expand(serie + 3*Hs*e))
# delta-rho cerca de cada raiz: drho/dw = w f'(w) (identidad V1) => dust local
for nombre, r_ in (("w1", w1_), ("w2", w2_), ("w3", w3_)):
    val = sp.simplify((w*fp).subs(w, r_))
    print(f"  {nombre}: d(rho)/dw|_* = w* f'(w*) = {sp.nsimplify(val)} = {float(val):+.4f}  (!=0 => delta-rho ~ a^-3, dust)")

# singularidades de la EOM: f'(w) = 0 con f != 0 => phidd -> infinito (caustica;
# el hessiano del mini-superspace degenera: alli la EFT del fondo revienta)
sing = sp.solve(fp, w)
print(f"  f'(w)=0 en w = {[sp.nsimplify(s) for s in sing]} = {[f'{float(s):+.4f}' for s in sing]}")
for s_ in sing:
    check(f"la singularidad w={float(s_):+.4f} NO es punto fijo (f != 0 alli)",
          sp.Integer(0 if sp.simplify(f.subs(w, s_)) != 0 else 1))
print("  CUENCAS con H>0 (flujo wdot = -3Hf/f', separatrices en f'=0):")
smax = float(sp.sqrt(sp.Rational(2, 3)))
casos = [(1.5, "w > +0.816"), (0.9, "0.816 > w > 0.618"), (0.3, "0.618 > w > -0.816"),
         (-1.0, "-0.816 > w > -1.618"), (-2.0, "w < -1.618")]
for wv, tag in casos:
    fv = float(f.subs(w, wv)); fpv = float(fp.subs(w, wv))
    dirr = "-> baja" if -fv/fpv < 0 else "-> sube"
    print(f"    {tag:22s}: signo(f)={'+' if fv>0 else '-'}, signo(f')={'+' if fpv>0 else '-'}  {dirr}")
print("  => cuenca de w1={w>+0.816}; cuenca de w2={-0.816<w<+0.816}; cuenca de w3={w<-0.816}.")
print("     En w=+-0.816 el coeficiente de phidd se anula con f!=0: phidd diverge")
print("     (breakdown del fondo, medida cero en datos iniciales).")

print()
print("=" * 72)
print("(a') numerico RK4: el flujo real con Friedmann acoplado")
print("=" * 72)
fN = sp.lambdify(w, f, "math"); fpN = sp.lambdify(w, fp, "math")
rhoN = sp.lambdify(w, rho, "math"); pN = sp.lambdify(w, p, "math")

def integra(w0, rho_m0=0.0, dt=2e-4, tmax=400.0, tag="", tsample=None):
    """adot=aH, Hdot=-(rho_tot+p_tot)/2, wdot=-3Hf/f'; dust p=0. Devuelve historia."""
    a, W = 1.0, w0
    rtot = rhoN(W) + rho_m0
    if rtot < 0:
        print(f"  {tag}: dato inicial INADMISIBLE en FRW plano (rho_tot={rtot:.4f} < 0)")
        return None
    Hv = math.sqrt(rtot/3.0)
    n = int(tmax/dt); hist = []
    isample = max(1, int((tsample or tmax/8)/dt))
    for i in range(n):
        def deriv(y):
            av, Hv_, Wv = y
            if abs(fpN(Wv)) < 1e-12: raise OverflowError("f'=0")
            rm = rho_m0/av**3
            return [av*Hv_, -(rhoN(Wv) + rm + pN(Wv))/2.0, -3*Hv_*fN(Wv)/fpN(Wv)]
        y = [a, Hv, W]
        try:
            k1 = deriv(y); k2 = deriv([y[j]+dt/2*k1[j] for j in range(3)])
            k3 = deriv([y[j]+dt/2*k2[j] for j in range(3)])
            k4 = deriv([y[j]+dt*k3[j] for j in range(3)])
            a, Hv, W = [y[j] + dt/6*(k1[j]+2*k2[j]+2*k3[j]+k4[j]) for j in range(3)]
        except OverflowError:
            print(f"    [t={i*dt:8.2f}] CAUSTICA: f'(w)=0 alcanzado (w={W:+.5f}) — EOM degenera, corto.")
            break
        if i % isample == 0 or a < 0.05:
            con = 3*Hv**2 - (rhoN(W) + rho_m0/a**3)
            hist.append((i*dt, a, Hv, W, con))
        if a < 0.05:
            print(f"    [t={i*dt:8.2f}] CRUNCH: a = {a:.3f} -> 0")
            break
        if a > 1e4:
            break
    for (tt, av, Hv_, Wv, con) in hist:
        print(f"    t={tt:8.2f}  a={av:10.4f}  H={Hv_:+.5f}  w={Wv:+.6f}  |3H^2-rho|={abs(con):.2e}")
    return (a, Hv, W)

print("  caso A: w0=0.3 (cuenca de w2), SOLO medio:")
integra(0.3, 0.0, tag="A")
print("  caso B: w0=0.65 (cuenca de w2), SOLO medio:")
integra(0.65, 0.0, tag="B")
print("  caso C: w0=0.7 + dust rho_m0=2 (converge a w2 y luego AdS-crunch):")
integra(0.7, 2.0, dt=2e-4, tmax=400.0, tag="C", tsample=2.0)
print("  caso D: w0=-2.0 (cuenca de w3, dS-like):")
integra(-2.0, 0.0, dt=1e-3, tmax=40.0, tag="D")

print()
print("=" * 72)
print("(c) genericidad del segundo punto en la clase U(X,Y)")
print("=" * 72)
# 1) grado: para U polinomica de grado d en (X,Y), f = U_Y - 2w U_X con X=-w^2
#    es polinomio de grado <= 2d-1: hasta 2d-1 raices. d=2 => cubica (3 raices) OK.
d1, d2_ = sp.symbols('d1 d2')
# 2) U LINEAL: f tiene UNA sola raiz => el segundo punto NO existe:
Ulin = d1*(X + 1) + d2_*(Y - 1)
flin = sp.expand((sp.diff(Ulin, Y) - 2*w*sp.diff(Ulin, X)).subs(sub, simultaneous=True))
print(f"  U lineal generica: f = {flin}  -> grado 1: UNICA raiz w = U_Y/(2U_X).")
check("U lineal: f es grado 1 en w (sin segundo punto)", sp.degree(flin, w) - 1)
# 3) familia con (Y-1)^2: U_c + c(Y-1)^2 => f = 2(w-1)(w^2+w-1+c):
c = sp.Symbol('c', real=True)
Ufam = Uc + c*(Y - 1)**2
ffam = sp.expand((sp.diff(Ufam, Y) - 2*w*sp.diff(Ufam, X)).subs(sub, simultaneous=True))
check("familia: f == 2(w-1)(w^2+w-1+c)", sp.expand(ffam - 2*(w - 1)*(w**2 + w - 1 + c)))
print("  => la posicion del segundo punto se mueve con c: w2(c) = [-1+sqrt(5-4c)]/2;")
print("     para c>5/4 las raices extra son COMPLEJAS: el segundo punto DESAPARECE.")
Ufam_b = Ub + c*(w - 1)**2
print("  signo de U en el segundo punto (decide AdS vs dS), escaneo en c:")
for cv in (0.0, 0.5, 1.0, 1.2, -1.0, -2.0):
    disc = 5 - 4*cv
    if disc <= 0:
        print(f"    c={cv:+.1f}: sin raiz real extra")
        continue
    w2c = (-1 + math.sqrt(disc))/2
    Uv = float(Ufam_b.subs({w: w2c, c: cv}))
    print(f"    c={cv:+.1f}: w2 = {w2c:+.4f},  U(w2) = {Uv:+.5f}  ({'AdS-like (rho<0)' if Uv > 0 else 'dS-like (rho>0)'})")
# 4) el punto w=1 en cambio esta FIJADO por el tadpole para TODA U(X,Y) sana:
Ug = sp.Function('U')(X, Y)
fg = (sp.diff(Ug, Y) - 2*w*sp.diff(Ug, X)).subs(sub, simultaneous=True)
print("  el punto w=1 existe para TODA U con tadpoles (f(1) = U_Y-2U_X|_(-1,1) = 0);")
print("  los puntos extra son genericos en U no lineal pero modelo-dependientes")
print("  (numero <= 2d-1, posicion y caracter AdS/dS segun coeficientes; en la")
print("  subclase isentropica U(X+Y^2), f == 0: TODO w es fijo — degenerado, V1/F6).")

print()
print("VEREDICTO TAREA 3:", "TODO PASS" if ok else "HAY FALLOS — revisar arriba")
