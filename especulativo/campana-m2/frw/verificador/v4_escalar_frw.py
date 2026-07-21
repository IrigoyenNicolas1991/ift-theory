# -*- coding: utf-8 -*-
"""
v4_escalar_frw.py — Tarea 4: perturbaciones ESCALARES del medio U(X,Y)+EH
sobre FRW, al orden dominante (sin operadores de derivadas superiores).

METODO (declarado):
 - Gauge UNITARIO cosmologico (Phi^0 = phi(t), Phi^a = x^a exactos): las 4
   funciones escalares van todas en la metrica:
     g_00 = -(1+2 e alpha),  g_0z = e dz(beta),
     g_xx = g_yy = a^2(1+2 e psi),  g_zz = a^2(1+2 e psi + 2 e dz^2 E).
   Sin gauge residual: los ceros del det son fisicos (mod factores k^n de la
   parametrizacion).
 - EOM covariantes linealizadas E_mn = G_mn - T_mn a O(e), con T_mn del medio
   por la formula covariante exacta (verificada en V2):
     T_mn = -2 phid^2 U_X d0m d0n + phid U_Y (-g00)^{-3/2} g0m g0n + g_mn U,
   con U, U_X, U_Y evaluadas en (X,Y) PERTURBADOS (U cuadratica general:
   U = c00 + c10(X+1) + c01(Y-1) + c20(X+1)^2/2 + c11(X+1)(Y-1) + c02(Y-1)^2/2;
   la esquina sana es c10=1, c01=2, c20=1, resto 0).
 - Fourier + coeficientes CONGELADOS (regimen p >> H, WKB local): ansatz
   e^{i(om t + k z)} y reglas on-shell del fondo (addot, adot, wdot, wddot ->
   Friedmann + EOM de phi). Valido al orden dominante y primer orden en H/p;
   terminos O(H^2) del det: indicativos.
 - det de la matriz 4x4 (filas E_00, E_0z, E_zz, E_xx; columnas alpha,beta,psi,E).
VALIDACION: en Minkowski (H=0, w=1, tadpoles) el det debe ser prop. a
m0^2 m1^2 om^4 k^6 (resultado verificado de la campana, SECTOR-ESCALAR).
Convenciones: (-,+,+,+), S = int sqrt(-g)[R/2 + U], M_Pl=1.
"""
import sympy as sp

ok = True
def check(nombre, expr, esperado=0):
    global ok
    r = sp.simplify(sp.expand(expr - esperado))
    estado = "PASS" if r == 0 else "FAIL"
    if r != 0: ok = False
    print(f"  [{estado}] {nombre}: residuo = {r}")

t, z, x, y = sp.symbols('t z x y', real=True)
coords = (t, x, y, z)
eps = sp.Symbol('eps')
a = sp.Function('a', positive=True)(t)
ph = sp.Function('phi', real=True)(t)
w = sp.diff(ph, t)
H = sp.diff(a, t)/a

al = sp.Function('alpha', real=True)(t, z)
be = sp.Function('beta', real=True)(t, z)
ps = sp.Function('psi', real=True)(t, z)
Ee = sp.Function('E', real=True)(t, z)

def ptr(e, n=1):
    e = sp.expand(e)
    return sum(e.coeff(eps, kk)*eps**kk for kk in range(n+1))

# ---------------- metrica a O(eps) ----------------
Bz = sp.diff(be, z)
Ezz = sp.diff(Ee, z, 2)
g = sp.zeros(4, 4)
g[0, 0] = -(1 + 2*eps*al)
g[0, 3] = g[3, 0] = eps*Bz
g[1, 1] = g[2, 2] = a**2*(1 + 2*eps*ps)
g[3, 3] = a**2*(1 + 2*eps*ps + 2*eps*Ezz)

gb = sp.diag(-1, a**2, a**2, a**2)          # fondo
gbinv = sp.diag(-1, 1/a**2, 1/a**2, 1/a**2)
dg = (g - gb)/eps                            # perturbacion O(1)
ginv = (gbinv - eps*gbinv*dg*gbinv).applyfunc(lambda e_: ptr(e_, 1))
resid = (g*ginv).applyfunc(lambda e_: ptr(e_, 1)) - sp.eye(4)
check("interno: g.ginv == 1 + O(eps^2)", sum(sp.Abs(sp.simplify(e_)) for e_ in resid))

# ---------------- curvatura a O(eps) ----------------
def christoffel(g_, ginv_, coords_, n_=1):
    n = len(coords_)
    Gam = [[[0]*n for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for m in range(n):
            for v in range(m, n):
                e_ = sum(ginv_[r, s]*(sp.diff(g_[s, m], coords_[v])
                                      + sp.diff(g_[s, v], coords_[m])
                                      - sp.diff(g_[m, v], coords_[s]))
                         for s in range(n))/2
                e_ = ptr(e_, n_)
                Gam[r][m][v] = e_
                Gam[r][v][m] = e_
    return Gam

def ricci_tensor(Gam, coords_, n_=1):
    n = len(coords_)
    Ric = sp.zeros(n, n)
    for m in range(n):
        for v in range(m, n):
            e_ = 0
            for r in range(n):
                e_ += sp.diff(Gam[r][m][v], coords_[r]) - sp.diff(Gam[r][r][m], coords_[v])
                for lam in range(n):
                    e_ += Gam[r][r][lam]*Gam[lam][m][v] - Gam[r][v][lam]*Gam[lam][r][m]
            e_ = ptr(e_, n_)
            Ric[m, v] = e_
            Ric[v, m] = e_
    return Ric

Gam = christoffel(g, ginv, coords)
Ric = ricci_tensor(Gam, coords)
Rsc = ptr(sum(ginv[m, v]*Ric[m, v] for m in range(4) for v in range(4)), 1)

# ---------------- medio U(X,Y) cuadratica general ----------------
c00, c10, c01, c20, c11, c02 = sp.symbols('c00 c10 c01 c20 c11 c02', real=True)
Xs, Ys = sp.symbols('Xs Ys')
Ufun = c00 + c10*(Xs+1) + c01*(Ys-1) + c20*(Xs+1)**2/2 + c11*(Xs+1)*(Ys-1) + c02*(Ys-1)**2/2
UX_f = sp.diff(Ufun, Xs); UY_f = sp.diff(Ufun, Ys)

# invariantes perturbados (exactos a O(eps)):
Xp = ptr(ginv[0, 0]*w**2, 1)                     # X = g^{00} phid^2
mg00 = 1 + 2*eps*al                              # -g_00
Yp = ptr(w*(1 - eps*al), 1)                      # Y = phid (-g00)^{-1/2} a O(eps)
pow_m32 = 1 - 3*eps*al                           # (-g00)^{-3/2} a O(eps)

def evalU(F):
    return ptr(F.subs({Xs: Xp, Ys: Yp}, simultaneous=True), 1)

Up = evalU(Ufun); UXp = evalU(UX_f); UYp = evalU(UY_f)

T = sp.zeros(4, 4)
for mu in range(4):
    for nu in range(4):
        T[mu, nu] = ptr(-2*w**2*UXp*(1 if mu == 0 and nu == 0 else 0)
                        + w*UYp*pow_m32*g[0, mu]*g[0, nu]
                        + g[mu, nu]*Up, 1)

E = sp.zeros(4, 4)
for mu in range(4):
    for nu in range(4):
        E[mu, nu] = ptr(Ric[mu, nu] - g[mu, nu]*Rsc/2 - T[mu, nu], 1)

# ---------------- fondo: cruce con V1 ----------------
print("=" * 72)
print("fondo (orden eps^0): reproduce V1")
print("=" * 72)
Ub0 = Ufun.subs({Xs: -w**2, Ys: w}, simultaneous=True)
UX0 = UX_f.subs({Xs: -w**2, Ys: w}, simultaneous=True)
UY0 = UY_f.subs({Xs: -w**2, Ys: w}, simultaneous=True)
rho0 = -Ub0 - 2*w**2*UX0 + w*UY0
p0 = Ub0
check("E_00|_eps0 == 3H^2 - rho", sp.expand(E[0, 0]).coeff(eps, 0) - (3*H**2 - rho0))
check("E_xx|_eps0 == -a^2(2addot/a + H^2 + p)",
      sp.expand(E[1, 1]).coeff(eps, 0) + a**2*(2*sp.diff(a, t, 2)/a + H**2 + p0))

# ---------------- Fourier + ansatz temporal + congelado ----------------
print()
print("=" * 72)
print("Fourier, ansatz e^{i(om t + k z)}, congelado on-shell")
print("=" * 72)
k, om = sp.symbols('k omega', real=True)
A0, B0, P0, E0 = sp.symbols('A0 B0 P0 E0')
I = sp.I
fase = sp.exp(I*(om*t + k*z))
ansatz = {al: A0*fase, be: B0*fase, ps: P0*fase, Ee: E0*fase}

eqs = []
for (mu, nu) in ((0, 0), (0, 3), (3, 3), (1, 1)):
    e_ = sp.expand(E[mu, nu]).coeff(eps, 1)
    e_ = e_.subs(ansatz, simultaneous=True).doit()
    e_ = sp.expand(e_/fase)
    eqs.append(e_)

# reglas de fondo on-shell (de V1, verificadas): se aplican de mayor a menor orden
ws, Hs, as_ = sp.symbols('w_s H_s a_s', positive=True)
f_w = sp.expand((UY0 - 2*w*UX0))
fp_w = sp.diff(f_w, w)
wdot_rule = -3*H*f_w/fp_w                     # EOM de phi
Hdot_rule = -(rho0 + p0)/2                     # Friedmann combinadas
addot_rule = a*(Hdot_rule + H**2)              # addot = a(Hdot+H^2)
wddot_rule = sp.diff(wdot_rule, t)             # contiene addot, wdot: se re-sustituye

def congela(e_):
    # phi(t) solo entra via w = phid: renombro Derivative(phi,t)->w simbolico via ws
    reglas1 = {sp.Derivative(ph, t, 3): sp.diff(wddot_rule, t),
               sp.Derivative(ph, t, 2): wdot_rule,
               sp.Derivative(a, t, 2): addot_rule}
    e_ = e_.subs(reglas1, simultaneous=True).doit()
    # iterar hasta que no queden derivadas altas
    for _ in range(4):
        e_ = e_.subs({sp.Derivative(ph, t, 2): wdot_rule,
                      sp.Derivative(a, t, 2): addot_rule}, simultaneous=True).doit()
    e_ = e_.subs({sp.Derivative(a, t): as_*Hs}, simultaneous=True)
    e_ = e_.subs({sp.Derivative(ph, t): ws, a: as_}, simultaneous=True)
    return sp.expand(sp.simplify(e_))

M = sp.zeros(4, 4)
vars_ = (A0, B0, P0, E0)
for i, e_ in enumerate(eqs):
    e_ = congela(e_)
    for j, v_ in enumerate(vars_):
        M[i, j] = sp.expand(e_.coeff(v_))
    resto = sp.simplify(e_ - sum(M[i, j]*vars_[j] for j in range(4)))
    if resto != 0:
        print(f"  [WARN] ecuacion {i}: resto no lineal = {resto}")

print("  matriz 4x4 armada (filas E00,E0z,Ezz,Exx; columnas alpha,beta,psi,E).")

# ---------------- VALIDACION MINKOWSKI ----------------
print()
print("=" * 72)
print("VALIDACION: Minkowski (a=1, H=0, w=1, tadpoles c00=0, c01=2c10)")
print("=" * 72)
mink = {as_: 1, Hs: 0, ws: 1, c00: 0, c01: 2*c10}
Mm = M.subs(mink, simultaneous=True)
detm = sp.factor(sp.simplify(Mm.det()))
print(f"  det(Minkowski) = {detm}")
m0_dic = -c10 + 2*c20 - 2*c11 + c02/2   # m0^2 del diccionario (handoff/B) en w=1
m1_dic = 2*c10
print(f"  diccionario: m0^2 = {m0_dic},  m1^2 = {m1_dic}")
# NOTA de parametrizacion: mis columnas son (alpha, beta, psi, E) con beta y E
# entrando via dz(beta) ~ k y dz^2(E) ~ k^2: el det carga k^3 MENOS que el de
# la casa (que reporta om^4 p^6). El contenido fisico es el CERO DOBLE en om^2=0
# para todo k y el coeficiente m0^2 m1^2. Chequeo la identidad exacta:
check("det(Minkowski) == -4*I * m0^2 m1^2 * om^4 k^3  (cero doble + coef m0^2 m1^2:"
      " matchea el det ~ m0^2 m1^2 om^4 p^6 de SECTOR-ESCALAR mod parametrizacion)",
      sp.expand(detm + 4*I*m0_dic*m1_dic*om**4*k**3))
# cero doble genuino: los coeficientes de om^0..om^3 son cero y el de om^4 no
poly_om = sp.Poly(sp.expand(detm), om)
check("coeficientes de om^0..om^3 == 0 (cero DOBLE en om^2, sin termino nuevo)",
      sum(sp.Abs(cf) for cf in [poly_om.coeff_monomial(om**j) for j in range(4)]))

import pickle, os
outdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(outdir, "v4_matriz_congelada.pkl"), "wb") as fh:
    pickle.dump({"M": M, "syms": (as_, Hs, ws, k, om, c00, c10, c01, c20, c11, c02)}, fh)
print("  [matriz congelada guardada en v4_matriz_congelada.pkl para la parte B]")

print()
print("VEREDICTO PARTE A:", "TODO PASS" if ok else "HAY FALLOS — revisar arriba")
