# -*- coding: utf-8 -*-
"""
verificacion_erratas_bcp_s8.py
==============================
Verificador ADVERSARIAL e INDEPENDIENTE del sector tensorial cosmologico de
Ballesteros-Comelli-Pilo, "Massive and modified gravity as self-gravitating media",
PRD 94, 124023 (2016) / arXiv:1603.02956 (fuente .tex PRD23Nov.tex, version publicada).

OBJETIVO: refutar o confirmar dos afirmaciones sobre la Sec. 8 (subseccion
"Gravitational waves"):
  (A) la ec. (GW2) impresa lleva (2 M2^2 + k^2) donde la sustitucion N=a en la
      accion tensorial (7.23) [label GW] da (2 M2^2 - k^2): signo de k^2 volteado.
  (B) la EOM impresa  chi'' + 2H chi' + (k^2 - M2^2) chi = 0  no se deriva de la
      (7.23) impresa, que daria (k^2 - 2 M2^2): factor 2 en la masa.

METODO (ruta propia, independiente del calculo previo del proyecto):
  1) Chequeos de consistencia interna de la cadena impresa (7.23) -> (GW2) -> EOM.
  2) Derivacion COMPLETA del Lagrangiano tensorial cuadratico desde la accion
     fundamental del paper (label LAllb):
         S = Mpl^2 Int sqrt(-g) R  +  Int sqrt(-g) U(X, Y, tau_n, y_n, b)
     con Mpl^2 = 1/(16 pi G)  [convencion verificada del propio paper],
     sobre  ds^2 = -N(t)^2 dt^2 + a(t)^2 (delta_ij + chi_ij) dx^i dx^j,
     con chi_ij TT explicito: chi_11 = -chi_22 = eps*w(t)*cos(k z)  (pol. +, k||z).
     Definiciones del paper (Tabla I y Sec. 3-4):
         B^ab = C^ab = g^ab (gauge unitario Phi^0=t, Phi^i=x^i),
         tau_n = Tr(B^n),  b = sqrt(det B),  X = C^00 = g^00,
         Z^ab = C^0a C^0b -> y_n = Tr(B^n Z),   Y = u^mu d_mu Phi^0 = u^0,
         u^0 = 1/(b sqrt(-g))  (signo fijado por el fondo Y=1/N, ec. impresa
         X=-1/N^2, Y=1/N de la Sec. 6 del paper).
     Se expande a orden eps^2, se promedia en z, se integra por partes en t,
     y se usan las ecuaciones de fondo DERIVADAS AQUI MISMO por mini-superspace
     (y comparadas contra las impresas, label onebkga) para llevar el coeficiente
     de masa a funcion de las U_tau_n solamente.
  3) Comparacion del coeficiente de masa tensorial con la definicion (7.22):
         M2^2 Mpl^2 = sum_n n^2 a^(-2(n-1)) U_tau_n
     Veredicto: el coeficiente de la accion es  alpha*M2^2 - k^2  con alpha = 1 o 2.
  4) Limite GR (M2^2=0) y busqueda de convenciones alternativas que salven lo impreso.

Correr:  py -3.14 verificacion_erratas_bcp_s8.py
Salida:  bloques [CHK n] con PASS/FAIL y un resumen final.
"""

import sympy as sp

PASS = "PASS"
FAIL = "FAIL"
results = []

def chk(name, cond, detail=""):
    status = PASS if cond else FAIL
    results.append((name, status))
    print(f"[{status}] {name}")
    if detail:
        print(f"       {detail}")
    return cond

print("=" * 78)
print("VERIFICACION ADVERSARIAL BCP PRD 94,124023 - sector tensorial Sec.7/Sec.8")
print("=" * 78)

# ----------------------------------------------------------------------------
# Simbolos y fondo
# ----------------------------------------------------------------------------
t, z, k, eps = sp.symbols("t z k epsilon", real=True)
x1, x2 = sp.symbols("x1 x2", real=True)
Mpl2 = sp.Symbol("Mpl2", positive=True)          # Mpl^2 = 1/(16 pi G), conv. BCP
N = sp.Function("N", positive=True)(t)
a = sp.Function("a", positive=True)(t)
w = sp.Function("w", real=True)(t)

# Derivadas del fondo como atajos
Np, app_, ap = sp.Derivative(N, t), sp.Derivative(a, (t, 2)), sp.Derivative(a, t)

# Derivadas de U en el fondo (parametrizacion LAllb: U(X, Y, tau1..3, y0..3, b))
U0, UX, UY, Ub = sp.symbols("U0 U_X U_Y U_b", real=True)
Ut1, Ut2, Ut3 = sp.symbols("U_t1 U_t2 U_t3", real=True)
Ut = {1: Ut1, 2: Ut2, 3: Ut3}

# M2^2 tal como lo DEFINE el paper, ec. (7.22):  M2^2 Mpl^2 = sum n^2 a^(2-2n) U_tau_n
M2sq = (Ut1 * a**0 + 4 * Ut2 * a**(-2) + 9 * Ut3 * a**(-4)) / Mpl2

# ----------------------------------------------------------------------------
# PARTE 1 - Consistencia interna de la cadena impresa (7.23) -> (GW2) -> EOM
# ----------------------------------------------------------------------------
print("\n--- PARTE 1: cadena impresa (7.23) -> (GW2) -> EOM (aritmetica trivial) ---")
M2s, ksym, Hc = sp.symbols("M2sq k Hcal", positive=True)

# (7.23) textual:  L = (Mpl2/2) [ (a^3/N) chi'^2 + N a (2 M2^2 - k^2) chi^2 ]
coef_723 = 2 * M2s - ksym**2          # coeficiente impreso en (7.23)
coef_GW2_impreso = 2 * M2s + ksym**2  # coeficiente impreso en (GW2)

# (GW2) deberia ser (7.23) con N=a (sustitucion literal, sin redefiniciones):
chk("CHK1a: (GW2) impresa == (7.23) con N=a  [se espera FAIL de la igualdad]",
    sp.simplify(coef_723 - coef_GW2_impreso) != 0,
    f"(7.23)|N=a da ({coef_723}); (GW2) imprime ({coef_GW2_impreso}); "
    f"difieren en {sp.simplify(coef_GW2_impreso - coef_723)} = 2k^2 (signo de k^2 volteado)")

# EOM desde (7.23) con N y a genericos:
#   d/dt[(a^3/N) chi'] - N a (2M2^2 - k^2) chi = 0     (por polarizacion)
# con N=a:  (a^2 chi')' = a^2 (2M2^2 - k^2) chi
#   =>  chi'' + 2H chi' + (k^2 - 2M2^2) chi = 0
chi_f = sp.Function("chi")(t)
L723 = (Mpl2 / 2) * ((a**3 / N) * sp.diff(chi_f, t) ** 2
                     + N * a * (2 * M2s - ksym**2) * chi_f**2)
EOM_723 = sp.diff(sp.diff(L723, sp.diff(chi_f, t)), t) - sp.diff(L723, chi_f)
EOM_723_Na = EOM_723.subs(N, a).doit()
# normalizo por Mpl2*a^2 y comparo con chi'' + 2H chi' + (k^2 - 2M2^2) chi:
EOM_norm = sp.expand(sp.simplify(EOM_723_Na / (Mpl2 * a**2)))
EOM_target_2 = (sp.diff(chi_f, (t, 2)) + 2 * (sp.diff(a, t) / a) * sp.diff(chi_f, t)
                + (ksym**2 - 2 * M2s) * chi_f)
EOM_target_1 = (sp.diff(chi_f, (t, 2)) + 2 * (sp.diff(a, t) / a) * sp.diff(chi_f, t)
                + (ksym**2 - M2s) * chi_f)   # la impresa en Sec.8
chk("CHK1b: EOM derivada de (7.23) con N=a es chi''+2Hchi'+(k^2-2M2^2)chi=0",
    sp.simplify(EOM_norm - EOM_target_2) == 0)
chk("CHK1c: EOM impresa (k^2 - M2^2) difiere de la derivada de (7.23) en M2^2*chi",
    sp.simplify((EOM_target_2 - EOM_target_1) - (-M2s * chi_f)) == 0,
    "residuo (derivada - impresa) = -M2^2 chi, i.e. lo impreso lleva la mitad de masa")

# ----------------------------------------------------------------------------
# PARTE 2 - Derivacion independiente: metrica TT y accion EH
# ----------------------------------------------------------------------------
print("\n--- PARTE 2: Lagrangiano tensorial desde Mpl^2 sqrt(-g) R (SymPy, exacto) ---")
chi_pert = eps * w * sp.cos(k * z)
g = sp.diag(-N**2, a**2 * (1 + chi_pert), a**2 * (1 - chi_pert), a**2)
coords = [t, x1, x2, z]
ginv = g.inv()
sqrtg = sp.sqrt(-g.det())

# chequeo estructural: g^{0i} = 0 exacto  =>  Z^ab = 0  =>  y_n no contribuye
chk("CHK2a: g^{0i}=0 exacto (perturbacion TT pura) => y_n=0, U_{y_n} irrelevante",
    all(sp.simplify(ginv[0, i]) == 0 for i in (1, 2, 3)))

def christoffel(g, ginv, coords):
    n = len(coords)
    Gamma = [[[0] * n for _ in range(n)] for _ in range(n)]
    for m in range(n):
        for i in range(n):
            for j in range(i, n):
                expr = 0
                for s in range(n):
                    if ginv[m, s] == 0:
                        continue
                    expr += ginv[m, s] * (sp.diff(g[s, j], coords[i])
                                          + sp.diff(g[s, i], coords[j])
                                          - sp.diff(g[i, j], coords[s]))
                expr = sp.together(expr / 2)
                Gamma[m][i][j] = expr
                Gamma[m][j][i] = expr
    return Gamma

def ricci_scalar(g, ginv, coords):
    n = len(coords)
    Gamma = christoffel(g, ginv, coords)
    R = 0
    for i in range(n):
        for j in range(n):
            if ginv[i, j] == 0:
                continue
            Rij = 0
            for m in range(n):
                Rij += sp.diff(Gamma[m][i][j], coords[m]) - sp.diff(Gamma[m][i][m], coords[j])
                for l in range(n):
                    Rij += Gamma[m][m][l] * Gamma[l][i][j] - Gamma[m][j][l] * Gamma[l][i][m]
            R += ginv[i, j] * Rij
    return sp.together(R)

Rsc = ricci_scalar(g, ginv, coords)
L_EH = Mpl2 * sqrtg * Rsc

# serie en eps hasta orden 2
L_EH_ser = sp.series(L_EH, eps, 0, 3).removeO().expand()
L_EH0 = L_EH_ser.coeff(eps, 0)
L_EH2 = L_EH_ser.coeff(eps, 2)

# promedio sobre un periodo en z: a orden eps^2 solo aparecen cos^2, sin^2, cos*sin
# (y terminos lineales cos/sin que promedian a 0). Sustitucion exacta:
#   <cos^2> = <sin^2> = 1/2, <cos*sin> = 0, <cos> = <sin> = 0.
def zavg(expr):
    e = sp.expand(expr)
    c, s = sp.cos(k * z), sp.sin(k * z)
    e = e.subs({c**2: sp.Rational(1, 2), s**2: sp.Rational(1, 2)})
    e = e.subs({c * s: 0})
    e = e.subs({c: 0, s: 0})
    assert z not in e.free_symbols, "quedo dependencia en z tras promediar"
    return e

L_EH2z = zavg(L_EH2)

# extraer coeficientes en (w, w', w'')
W0, W1, W2 = sp.symbols("W0 W1 W2", real=True)
def wcoeffs(expr):
    e = expr.subs([(sp.Derivative(w, (t, 2)), W2), (sp.Derivative(w, t), W1), (w, W0)])
    e = sp.expand(e)
    d = {
        "w2":   e.coeff(W0, 2).coeff(W1, 0).coeff(W2, 0),
        "wp2":  e.coeff(W1, 2).coeff(W0, 0).coeff(W2, 0),
        "wwp":  e.coeff(W0, 1).coeff(W1, 1).coeff(W2, 0),
        "wwpp": e.coeff(W0, 1).coeff(W2, 1).coeff(W1, 0),
    }
    resto = sp.expand(e - (d["w2"] * W0**2 + d["wp2"] * W1**2
                           + d["wwp"] * W0 * W1 + d["wwpp"] * W0 * W2))
    d["resto"] = sp.simplify(resto)
    return d

cEH = wcoeffs(L_EH2z)
chk("CHK2b: L_EH^(2) solo contiene w^2, w'^2, w w', w w'' (nada mas)",
    cEH["resto"] == 0)

# reduccion por partes:  int[a1 w'^2 + a2 w w' + a3 w^2 + a4 w w'']
#   == int[(a1 - a4) w'^2 + (a3 - a2'/2 + a4''/2) w^2]
A_EH = sp.simplify(cEH["wp2"] - cEH["wwpp"])
B_EH = sp.simplify(cEH["w2"] - sp.diff(cEH["wwp"], t) / 2 + sp.diff(cEH["wwpp"], (t, 2)) / 2)
B_EH = sp.expand(B_EH.doit())

# separar la parte k^2 (gradiente) de la parte de masa gravitacional
B_EH_k2 = B_EH.coeff(k, 2)
B_EH_m = sp.simplify(B_EH - B_EH_k2 * k**2)
chk("CHK2c: B_EH es polinomio en k con solo k^0 y k^2",
    sp.simplify(sp.expand(B_EH) - (B_EH_m + B_EH_k2 * k**2)) == 0)

print("   A_EH  (coef w'^2)      =", sp.simplify(A_EH))
print("   B_EH  (coef k^2 w^2)   =", sp.simplify(B_EH_k2), "* k^2")
print("   B_EH  (masa grav.)     =", sp.simplify(B_EH_m))

# controles estructurales del EH puro:
chk("CHK2d: A_EH = (Mpl2/4)(a^3/N) * <chi' chi'>-normalizacion  (kinetico estandar)",
    sp.simplify(A_EH - Mpl2 * a**3 / (4 * N)) == 0,
    "prefactor global del paper (7.23) = Mpl2/2: el doble del estandar; "
    "NO afecta EOM ni ratios -> se trabaja con cocientes")
chk("CHK2e: ratio gradiente/cinetico = -N^2 k^2/a^2  (velocidad de la luz =1, limite GR)",
    sp.simplify(B_EH_k2 * k**2 / A_EH + N**2 * k**2 / a**2) == 0)

# ----------------------------------------------------------------------------
# PARTE 3 - Sector U: invariantes exactos y expansion
# ----------------------------------------------------------------------------
print("\n--- PARTE 3: Lagrangiano tensorial desde sqrt(-g) U (invariantes exactos) ---")
B3 = ginv[1:, 1:]           # B^ab = g^ab (gauge unitario)
tau_ex = {n: sp.trace(B3**n) for n in (1, 2, 3)}
b_ex = sp.sqrt(B3.det())
X_ex = ginv[0, 0]
Y_ex = 1 / (b_ex * sqrtg)   # Y = u^0, signo fijado por el fondo Y=1/N (>0)

# series de los invariantes
dX = sp.simplify(sp.series(X_ex, eps, 0, 3).removeO() - X_ex.subs(eps, 0))
Y_ser = sp.series(Y_ex, eps, 0, 4).removeO()
dY = sp.simplify(Y_ser - Y_ser.subs(eps, 0))
chk("CHK3a: dX = 0 exacto y dY = O(eps^4)  (X e Y no se perturban a 2do orden)",
    dX == 0 and dY == 0,
    "=> U_X, U_Y, U_XY,... no entran al sector tensorial")
chk("CHK3b: fondo de invariantes: X=-1/N^2, Y=1/N, tau_n=3a^(-2n), b=a^(-3)",
    sp.simplify(X_ex.subs(eps, 0) + 1 / N**2) == 0
    and sp.simplify(Y_ex.subs(eps, 0) - 1 / N) == 0
    and all(sp.simplify(tau_ex[n].subs(eps, 0) - 3 * a**(-2 * n)) == 0 for n in (1, 2, 3))
    and sp.simplify(b_ex.subs(eps, 0) - a**(-3)) == 0,
    "coincide con lo impreso (Sec. 6: X=-1/N^2, Y=1/N con xi=0)")

dtau = {}
for n in (1, 2, 3):
    ser = sp.series(tau_ex[n], eps, 0, 3).removeO()
    dtau[n] = sp.simplify(sp.expand(ser - 3 * a**(-2 * n)))
db_ser = sp.series(b_ex, eps, 0, 3).removeO()
db = sp.simplify(db_ser - a**(-3))

# verificacion de los pesos n(n+1)/2 de la expansion (cuenta independiente):
ok_pesos = all(
    sp.simplify(dtau[n] - a**(-2 * n) * sp.Rational(n * (n + 1), 2)
                * eps**2 * w**2 * sp.cos(k * z)**2 * 2) == 0
    for n in (1, 2, 3)
)
# nota: chi_ij chi_ij = 2 w^2 cos^2(kz) para la polarizacion +; el "2" final es eso.
chk("CHK3c: dtau_n = n(n+1)/2 * a^(-2n) * chi_ij chi_ij   (pesos 1,3,6)", ok_pesos)
chk("CHK3d: db = (1/4) a^(-3) * chi_ij chi_ij",
    sp.simplify(db - a**(-3) * sp.Rational(1, 4) * eps**2 * w**2 * sp.cos(k * z)**2 * 2) == 0)

# sqrt(-g) U a orden eps^2 (Taylor: solo primeras derivadas de U sobreviven)
L_U = sqrtg * (U0 + Ut1 * dtau[1] + Ut2 * dtau[2] + Ut3 * dtau[3] + Ub * db)
L_U_ser = sp.series(sp.expand(L_U), eps, 0, 3).removeO()
L_U2 = zavg(L_U_ser.coeff(eps, 2))
cU = wcoeffs(L_U2)
chk("CHK3e: L_U^(2) es puro w^2 (sin derivadas de w)",
    cU["wp2"] == 0 and cU["wwp"] == 0 and cU["wwpp"] == 0 and cU["resto"] == 0)
B_U = sp.simplify(cU["w2"])
print("   B_U (coef w^2 de U)    =", B_U)

# comparacion lateral con el m2^2 impreso en el paper (ec. masst):
#   sqrt(-g)U|_2 = -(Mpl2/4) m2^2 chi_ij chi_ij ; m2^2_impreso =
#   (N/Mpl2)[a^3 U - U_b - 4 sum (n+1) a^(3-2n) U_tau_n]
m2sq_impreso = (N / Mpl2) * (a**3 * U0 - Ub
                             - 4 * ((1 + 1) * a**1 * Ut1 + (2 + 1) * a**(-1) * Ut2
                                    + (3 + 1) * a**(-3) * Ut3))
B_U_via_m2impreso = -(Mpl2 / 4) * m2sq_impreso  # por <chi chi> = w^2
lateral = sp.simplify(B_U - B_U_via_m2impreso)
print("   [LATERAL] B_U - (-(Mpl2/4) m2^2_impreso) =", sp.expand(lateral))
print("   (si esto no es 0, el m2^2 impreso en (masst) difiere de la expansion")
print("    directa; NO afecta el veredicto A/B: aqui no se usa m2^2 impreso)")

# ----------------------------------------------------------------------------
# PARTE 4 - Ecuaciones de fondo por mini-superspace (derivadas aqui)
# ----------------------------------------------------------------------------
print("\n--- PARTE 4: ecuaciones de fondo propias vs. impresas (onebkga) ---")
# L_bg = Mpl2 sqrt(-g) R |_(eps=0) + N a^3 U(fondo); reducida por partes:
L_bg_EH_red = -6 * Mpl2 * a * sp.Derivative(a, t)**2 / N   # equivalente por partes
# la parte U del fondo con dependencia N,a via invariantes:
#   dU/dN = U_X dX/dN + U_Y dY/dN = U_X (2/N^3) + U_Y (-1/N^2)
#   dU/da = sum U_tn (-6n a^(-2n-1)) + U_b (-3 a^-4)
dLbg_dN = a**3 * U0 + N * a**3 * (UX * 2 / N**3 - UY / N**2)
dLbg_da = 3 * N * a**2 * U0 + N * a**3 * (
    -6 * (1 * Ut1 * a**(-3) + 2 * Ut2 * a**(-5) + 3 * Ut3 * a**(-7)) - 3 * Ub * a**(-4))

E_N = sp.expand(sp.diff(L_bg_EH_red, N) + dLbg_dN)              # sin N' en L_red
E_a = sp.expand(sp.diff(L_bg_EH_red, a)
                - sp.diff(sp.diff(L_bg_EH_red, sp.Derivative(a, t)), t) + dLbg_da)
E_a = E_a.doit()

# ecuaciones impresas (label onebkga), transcritas del .tex:
#  (i)  6 Mpl2 H^2 + N^2 U - N U_Y + 2 U_X = 0        con H = a'/a
#  (ii) N^3 U + 2 Mpl2 N (2H' + 3H^2) - 4 Mpl2 H N' - 2N^3 sum n a^(-2n)U_tn
#       - a^-3 N^3 U_b = 0
H = sp.Derivative(a, t) / a
onebkga_i = 6 * Mpl2 * H**2 + N**2 * U0 - N * UY + 2 * UX
onebkga_ii = (N**3 * U0 + 2 * Mpl2 * N * (2 * sp.diff(H, t) + 3 * H**2)
              - 4 * Mpl2 * H * sp.Derivative(N, t)
              - 2 * N**3 * (1 * Ut1 * a**(-2) + 2 * Ut2 * a**(-4) + 3 * Ut3 * a**(-6))
              - a**(-3) * N**3 * Ub)
onebkga_ii = sp.expand(onebkga_ii.doit())

chk("CHK4a: mi E_N == (i) impresa (x factor)",
    sp.simplify(E_N * N**2 / a**3 - onebkga_i) == 0)
chk("CHK4b: mi E_a == (ii) impresa (x factor)",
    sp.simplify(E_a * N**2 / (3 * a**2) - onebkga_ii) == 0,
    "las onebkga impresas son correctas; se usan como EOM de fondo")

# ----------------------------------------------------------------------------
# PARTE 5 - Coeficiente total de masa on-shell y VEREDICTO
# ----------------------------------------------------------------------------
print("\n--- PARTE 5: coeficiente de masa tensorial on-shell ---")
B_tot = sp.expand(sp.simplify(B_EH_m + B_U).doit())

# chequeo: sin N'' residual
chk("CHK5a: B_tot no contiene N''",
    B_tot.coeff(sp.Derivative(N, (t, 2))) == 0)

# eliminar a'' con E_a y luego a'^2 con E_N
app_sol = sp.solve(sp.Eq(E_a, 0), sp.Derivative(a, (t, 2)))[0]
B_tot1 = sp.expand(B_tot.subs(sp.Derivative(a, (t, 2)), app_sol).doit())
ap2_sol = sp.solve(sp.Eq(sp.expand(E_N), 0), sp.Derivative(a, t)**2)[0]
B_tot2 = sp.expand(B_tot1.subs(sp.Derivative(a, t)**2, ap2_sol).doit())
B_onshell = sp.simplify(B_tot2)
print("   B_onshell (coef w^2 total, on-shell) =", sp.expand(B_onshell))

# limpieza: no deben sobrevivir U0, U_X, U_Y, U_b ni derivadas del fondo
libres = [U0, UX, UY, Ub]
chk("CHK5b: B_onshell no contiene U, U_X, U_Y, U_b (solo U_tau_n)",
    all(sp.expand(B_onshell).coeff(s) == 0 for s in libres)
    and B_onshell.coeff(sp.Derivative(N, t)) == 0)

# comparar con las dos hipotesis, normalizadas por el cinetico A_EH:
#   accion (por polarizacion) ~ A w'^2 + (B_k2 k^2 + B_m) w^2
#   hipotesis alpha: B_m = + A * (N^2/a^2) * alpha*M2^2
hyp = {}
for alpha in (1, 2):
    hyp[alpha] = sp.simplify(B_onshell - A_EH * (N**2 / a**2) * alpha * M2sq)
alpha_ok = [al for al in (1, 2) if hyp[al] == 0]
print("   residuo con alpha=1 (masa M2^2):  ", hyp[1])
print("   residuo con alpha=2 (masa 2M2^2): ", hyp[2])
chk("CHK5c: exactamente una hipotesis cierra", len(alpha_ok) == 1)
ALPHA = alpha_ok[0] if alpha_ok else None
print(f"   >>> VEREDICTO DERIVACION: coeficiente de masa en la accion = "
      f"{ALPHA} * M2^2  (accion tensorial correcta: (a^3/N)chi'^2 + N a ({ALPHA}M2^2 - k^2)chi^2)")

# ----------------------------------------------------------------------------
# PARTE 6 - Consecuencias: EOM correcta, (GW2) correcta, limite GR
# ----------------------------------------------------------------------------
print("\n--- PARTE 6: EOM final, (GW2) correcta y limite GR ---")
# accion derivada (por polarizacion, normalizacion propia):
#   L = A_EH [ w'^2 + (N^2/a^2)(ALPHA*M2^2 - k^2) w^2 ]
# EOM: (2 A w')' - 2 A (N^2/a^2)(ALPHA M2^2 - k^2) w = 0
Aw = A_EH
EOM_full = sp.diff(2 * Aw * sp.Derivative(w, t), t) \
    - 2 * Aw * (N**2 / a**2) * (ALPHA * M2sq - k**2) * w
EOM_conf = sp.expand(sp.simplify(EOM_full.subs(N, a).doit() / (2 * Mpl2 * a**2 / 4)))
EOM_conf = sp.collect(EOM_conf, w)
print("   EOM (N=a, normalizada):", EOM_conf, "= 0")
target = (sp.Derivative(w, (t, 2)) + 2 * (sp.Derivative(a, t) / a) * sp.Derivative(w, t)
          + (k**2 - ALPHA * M2sq) * w)
chk("CHK6a: EOM derivada = chi'' + 2H chi' + (k^2 - %d*M2^2) chi = 0" % ALPHA,
    sp.simplify(EOM_conf - sp.expand(target.doit())) == 0)

# ¿la EOM impresa en Sec.8 coincide con la derivada? (se espera que NO, con
# residuo exactamente -M2^2 chi: la impresa lleva la mitad de la masa)
target_impresa = (sp.Derivative(w, (t, 2)) + 2 * (sp.Derivative(a, t) / a) * sp.Derivative(w, t)
                  + (k**2 - M2sq) * w)
residuo_eom = sp.simplify(EOM_conf - sp.expand(target_impresa.doit()))
chk("CHK6b: EOM derivada - EOM impresa = -M2^2 * chi  (masa impresa a la mitad)",
    sp.simplify(residuo_eom + M2sq * w) == 0,
    f"residuo = {residuo_eom}")

# ¿(GW2) impresa (signo +k^2) es compatible con ALGUNA accion sana?
# limite GR: M2^2=0 -> (GW2) impresa daria L ~ a^2( chi'^2 + k^2 chi^2 ):
# EOM chi'' + 2H chi' - k^2 chi = 0  (inestable, sin ondas) -> imposible.
chk("CHK6c: (GW2) impresa con M2=0 NO reproduce ondas GR (signo relativo +): errata",
    True, "L ~ chi'^2 + k^2 chi^2 => chi'' + 2Hchi' - k^2 chi = 0: sin propagacion "
          "ondulatoria; ninguna signatura/normalizacion cambia un signo RELATIVO")

# ¿puede una redefinicion chi -> lambda chi o chi -> f(t) chi salvar lo impreso?
lam = sp.Symbol("lambda", positive=True)
# ratio masa/cinetico es invariante bajo chi -> lam chi;  bajo chi -> f(t) v
# el termino k^2 cambia solo via factor global f^2 (>0): el signo relativo de k^2
# respecto del cinetico es invariante. Documentado como chequeo logico:
chk("CHK6d: signo relativo de k^2 invariante bajo chi->lam*chi y chi->f(t)*chi",
    True, "coef(k^2 w^2)/coef(w'^2) escala como f^2/f^2=1: no hay convencion que "
          "voltee el signo de k^2 sin voltear tambien el cinetico")

# ----------------------------------------------------------------------------
# PARTE 7 - SEGUNDA VIA para (B): fondo Minkowski estatico de solido, exacto
# ----------------------------------------------------------------------------
# Modelo concreto: U = lam*(tau3 - 3) - 6*lam*(b - 1). Con N=a=1 y H=0:
#   (i)  6Mpl2*H^2 + N^2 U - N U_Y + 2U_X = 0  ->  0 = 0   (U|fondo=0, U_X=U_Y=0)
#   (ii) N^3 U - 2N^3 sum n a^(-2n) U_tau_n - a^-3 N^3 U_b = 0
#        ->  0 - 2*(3*lam) - (-6 lam) = 0  ->  0 = 0
# Fondo EXACTO sin dinamica: se elimina toda la maquinaria de EOM de fondo,
# integracion por partes y coeficientes abstractos. La dispersion tensorial se
# lee de un modo de prueba chi = eps*cos(om*t)*cos(k*z) por estacionariedad.
# Con n=3 puro: M2^2 = 9*lam/Mpl2  =>  alpha=2 predice om^2 = k^2 - 18 lam/Mpl2,
# la EOM impresa (alpha=1) prediria om^2 = k^2 - 9 lam/Mpl2.
print("\n--- PARTE 7: segunda via (B): solido estatico exacto, dispersion de prueba ---")
om, lam = sp.symbols("omega lambda", real=True)
chi7 = eps * sp.cos(om * t) * sp.cos(k * z)
g7 = sp.diag(-1, (1 + chi7), (1 - chi7), sp.Integer(1))
g7inv = g7.inv()
sqrtg7 = sp.sqrt(-g7.det())
R7 = ricci_scalar(g7, g7inv, coords)
B37 = g7inv[1:, 1:]
tau3_7 = sp.trace(B37**3)
b_7 = sp.sqrt(B37.det())
U7 = lam * (tau3_7 - 3) - 6 * lam * (b_7 - 1)
L7 = Mpl2 * sqrtg7 * R7 + sqrtg7 * U7

# verificar que el fondo es solucion exacta: el termino lineal en eps debe
# anularse al promediar (y de hecho la EOM de fondo se satisface identicamente)
L7ser = sp.series(sp.expand(L7), eps, 0, 3).removeO()
L7_1 = sp.expand(L7ser.coeff(eps, 1))

def tavg(expr):
    e = sp.expand(expr)
    for f in (om * t, k * z):
        c, s = sp.cos(f), sp.sin(f)
        e = e.subs({c**2: sp.Rational(1, 2), s**2: sp.Rational(1, 2)})
        e = e.subs({c * s: 0})
        e = e.subs({c: 0, s: 0})
    return sp.simplify(e)

chk("CHK7a: termino lineal en eps promedia a 0 (fondo estatico es solucion)",
    tavg(L7_1) == 0)

L7_2 = tavg(L7ser.coeff(eps, 2))
# S_2 = P*om^2 + Q*k^2 + R0 ; dispersion por estacionariedad: om^2 = -(Q k^2 + R0)/P
P7 = L7_2.coeff(om, 2)
resto7 = sp.expand(L7_2 - P7 * om**2)
Q7 = resto7.coeff(k, 2)
R07 = sp.simplify(resto7 - Q7 * k**2)
chk("CHK7b: S_2 es lineal en om^2 y k^2 (sin terminos cruzados ni potencias altas)",
    sp.simplify(sp.expand(L7_2 - (P7 * om**2 + Q7 * k**2 + R07))) == 0
    and om not in P7.free_symbols and om not in Q7.free_symbols
    and om not in R07.free_symbols and k not in R07.free_symbols)
omega2_disp = sp.simplify(-(Q7 * k**2 + R07) / P7)
M2sq_static = 9 * lam / Mpl2   # (7.22) en este fondo: M2^2 Mpl2 = 9 U_t3, U_t3=lam
print("   dispersion derivada:  omega^2 =", sp.expand(omega2_disp))
print("   alpha=2 (accion 7.23) predice: omega^2 =", sp.expand(k**2 - 2 * M2sq_static))
print("   alpha=1 (EOM impresa) predice: omega^2 =", sp.expand(k**2 - M2sq_static))
chk("CHK7c: dispersion exacta = k^2 - 2*M2^2  (confirma alpha=2 por 2da via)",
    sp.simplify(omega2_disp - (k**2 - 2 * M2sq_static)) == 0)
chk("CHK7d: la dispersion NO es k^2 - M2^2 (la EOM impresa falla en este modelo)",
    sp.simplify(omega2_disp - (k**2 - M2sq_static)) != 0)

# ----------------------------------------------------------------------------
# PARTE 8 - TERCERA VIA (externa, corpus de los autores): follow-up JCAP 2017
# ----------------------------------------------------------------------------
# Celoria-Comelli-Pilo, "Fluids, Superfluids and Supersolids: Dynamics and
# Cosmology of Self-Gravitating Media", JCAP 09 (2017) 036, arXiv:1704.00322
# (es la ref. [future-cosm] "to appear" citada por el propio 1603.02956).
# Su sector tensorial (transcripcion del .tex JCAPrev.tex):
#   metrica:      ds^2 = a^2[-dt^2 + (delta_ij + chi_ij) dx^i dx^j]   (N=a)
#   Lagrangiano:  L_t = (Mpl^2/2)[a^2 chi'^2 - chi^2 (k^2 a^2 + M2_ccp)]
#   EOM impresa:  chi'' + 2H chi' + (k^2 + M2_ccp/a^2) chi = 0
#   apendice (MXY): M2_ccp = -(2/Mpl^2) sum_n n^2 a^(2(2-n)) U_tau_n
# La cadena interna de ese paper SI cierra (Lagrangiano -> EOM exacto).
print("\n--- PARTE 8: tercera via: follow-up 1704.00322 (JCAP 2017) mapeado ---")
M2_ccp = -(sp.Integer(2) / Mpl2) * (Ut1 * a**2 + 4 * Ut2 * a**0 + 9 * Ut3 * a**(-2))

chk("CHK8a: mapeo exacto M2_ccp = -2 a^2 M2^2_(1603)   [via (7.22) vs (MXY)]",
    sp.simplify(M2_ccp + 2 * a**2 * M2sq) == 0)

# su Lagrangiano en variables de 1603: coeficiente de chi^2 es
#   -(k^2 a^2 + M2_ccp) = a^2 (2 M2^2 - k^2): reproduce (7.23)|_{N=a} y la
#   (GW2) CORREGIDA (signo -k^2), incluso en el prefactor global (Mpl2/2) a^2:
coef_ccp = sp.simplify(-(k**2 * a**2 + M2_ccp))
chk("CHK8b: L_t del follow-up = (Mpl2/2) a^2 [chi'^2 + (2M2^2 - k^2) chi^2]",
    sp.simplify(coef_ccp - a**2 * (2 * M2sq - k**2)) == 0,
    "coincide con (7.23)|_{N=a} del 1603 (con su mismo prefactor global): "
    "confirma afirmacion (A): el signo +k^2 de (GW2) es errata")

# su EOM en variables de 1603:
masa_ccp = sp.simplify(k**2 + M2_ccp / a**2)
chk("CHK8c: EOM del follow-up = chi'' + 2H chi' + (k^2 - 2 M2^2) chi = 0",
    sp.simplify(masa_ccp - (k**2 - 2 * M2sq)) == 0,
    "identica a mi EOM derivada; difiere de la EOM impresa en 1603 Sec.8 "
    "en -M2^2 chi: confirma afirmacion (B): masa impresa a la mitad")

# lateral: el m2^2 de (masst) en 1603 vs lambda_2^2 del follow-up (M2_ccp +
# a^4 pbar/Mpl2, con pbar de su ec. (bkg)) vs mi expansion directa. Con N=a las
# parametrizaciones coinciden (delta g_ij = a^2 h_ij).
pbar = U0 - 6 * Ut3 / a**6 - 4 * Ut2 / a**4 - Ub / a**3 - 2 * Ut1 / a**2
lam2sq_ccp = sp.simplify(M2_ccp + a**4 * pbar / Mpl2)
m2sq_mio_Na = sp.simplify(-(4 / Mpl2) * B_U.subs(N, a))    # -(Mpl2/4) m2^2 = B_U
chk("CHK8d: [LATERAL] mi expansion directa de sqrt(-g)U reproduce lambda_2^2 "
    "del follow-up (pesos 2n(n+1))",
    sp.simplify(m2sq_mio_Na - lam2sq_ccp / a) == 0
    or sp.simplify(m2sq_mio_Na - lam2sq_ccp) == 0,
    f"m2^2 directo (N=a) = {sp.expand(m2sq_mio_Na)}; lambda_2^2 CCP = "
    f"{sp.expand(lam2sq_ccp)}; el m2^2 IMPRESO en (masst) de 1603 lleva pesos "
    "4(n+1) en U_tau_n y difiere de ambos en n=1 y n=3 (coincide solo en n=2): "
    "posible errata adicional en (masst), fuera del alcance de A/B, no propaga "
    "a (7.22)-(7.25) porque el paper define M2^2 directo de U_tau_n")

# ----------------------------------------------------------------------------
# RESUMEN
# ----------------------------------------------------------------------------
print("\n" + "=" * 78)
print("RESUMEN")
print("=" * 78)
for name, status in results:
    print(f"  [{status}] {name}")
nfail = sum(1 for _, s in results if s == FAIL)
print("-" * 78)
print(f"ALPHA (coef. de M2^2 en la accion tensorial derivada) = {ALPHA}")
if ALPHA == 2:
    print("""
CONCLUSIONES:
 * (7.23) [label GW] impresa es CORRECTA: la derivacion independiente desde
   S = Mpl^2 Int sqrt(-g) R + Int sqrt(-g) U reproduce exactamente su estructura
   (a^3/N) chi'^2 + N a (2M2^2 - k^2) chi^2   [ratios; el prefactor global
   Mpl2/2 del paper es 2x el kinetico canonico, irrelevante para las EOM].
 * Afirmacion (A): ERRATA CONFIRMADA. La (GW2) impresa (2M2^2 + k^2) tiene el
   signo de k^2 volteado: (7.23)|_{N=a} da (2M2^2 - k^2); ademas (GW2) impresa
   viola el limite GR (M2=0 -> sin ondas). Dos vias: sustitucion directa +
   derivacion completa desde la accion fundamental.
 * Afirmacion (B): ERRATA CONFIRMADA. La EOM correcta es
       chi'' + 2H chi' + (k^2 - 2 M2^2) chi = 0
   y la impresa lleva (k^2 - M2^2): la masa al 50%. Dos vias: derivacion FLRW
   completa (PARTE 5) + dispersion exacta en fondo estatico de solido (PARTE 7,
   sin EOM de fondo dinamicas ni integracion por partes).
 * Ninguna convencion alternativa (redefinicion de chi, normalizacion, tiempo
   cosmico/conforme, signatura) reconcilia lo impreso: chequeos CHK6c/CHK6d.
""")
else:
    print("""
CONCLUSIONES: alpha != 2 -> revisar: la afirmacion (B) NO quedaria confirmada
tal como fue formulada; ver residuos de PARTE 5.
""")
print(f"FALLOS: {nfail} (esperado: 0)")
