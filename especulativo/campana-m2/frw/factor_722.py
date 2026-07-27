# -*- coding: utf-8 -*-
"""
factor_722.py — TAREA B de la lista de bloqueo del paper missing-row:
dirimir el "factor 2 global vs (7.22)" que el acta FRW-2026-07-21 dejo anotado
en el diccionario cosmologico de BCP (arXiv:1603.02956).

FUENTE PRIMARIA (leida del .tex, e-print https://arxiv.org/e-print/1603.02956,
version PRD23Nov.tex = arXiv v2, descargada 2026-07-27; el .tex NO entra al
repo). La numeracion (7.x) se verifico contando entornos equation/align de la
seccion 7 ("Cosmological perturbations in FLRW", la 7a \\section del .tex) con
tres anclas que coinciden con las citas ya verificadas de la campana:
(7.3) = patron de masas [label masst], (7.5)-(7.7) = m0^2, m1^2, m2^2 (con las
erratas de pesos confirmadas por Pilo). Con ese conteo:

  (7.20)  M_0^2 = m_0^2 N^5 - 3 a^7 H^2 ,  M_1^2 = 6 a^5 H^2 + m_1^2 N^3
  (7.21)  [label anis]  delta T_ij  superset  M_2^2 d_i d_j pi_L
  (7.22)  M_2^2 M_pl^2 = sum_{n=1}^3 n^2 a^{-2(n-1)} U_{tau_n}
  (7.23)  [label GW]  L2_t = (M_pl^2/2)[ (a^3/N) chi'_ij chi'_ij
                                         + N a (2 M_2^2 - k^2) chi_ij chi_ij ]
  (8.GW2) [label GW2, subseccion "Gravitational waves", con N(t)=a(t)]
          S = (M_pl^2/2) int dt d3k a^2 [ chi' chi' + (2 M_2^2 + k^2) chi chi ]
  (8.EOM) chi'' + 2 H chi' + (k^2 - M_2^2) chi = 0        [' = d/d(eta), N=a]

  y la ACCION de BCP es (label LAllb, tambien ugaction):
          S = M_pl^2 int d4x sqrt(-g) R  +  int d4x sqrt(-g) U
  ==> el M_pl^2 de BCP es el coeficiente de R SIN 1/2:  M_pl^2 = 1/(16 pi G).
  Los scripts de la campana usan S = int sqrt(-g)[ R/2 + U ]  (Mbar^2 = 1, o
  sea 1/(8 pi G) = 1): el coeficiente de R aca es 1/2, no 1.

HIPOTESIS A DIRIMIR (mandato): el factor 2 del acta es (a) la convencion de
M_Pl^2 (1/16piG vs 1/8piG), (b) la definicion de M_2^2, o (c) una errata mas
de BCP.

METODO (todo derivado aca, sin reciclar resultados): accion tensorial
cuadratica de S = int sqrt(-g) [ Mp2 * R + U(tau_1,tau_2,tau_3) ] sobre
FRW con lapse N(t) GENERICO, con Mp2 el coeficiente de R como SIMBOLO (la
convencion BCP es Mp2 = M_pl^2; la de la casa, Mp2 = 1/2). Perturbacion TT
en la parametrizacion de BCP (7.15): g_ij = a^2 (delta_ij + chi_ij),
chi TT con k // z, dos polarizaciones hp, hx. U(tau_n) = c1 tau1 + c2 tau2 +
c3 tau3 + (q11/2) tau1^2 (el termino cuadratico es testigo de que las
segundas derivadas U_{tau tau} no entran: la masa solo carga las PRIMERAS
derivadas evaluadas en el fondo, que es lo que (7.22) postula).

CHEQUEOS:
  B1  fondo: EOM de a (Friedmann II con lapse) derivada del mini-superespacio.
  B2  L2 tensorial: coeficientes cinetico / friccion / gradiente / masa.
      c_T^2 = N^2/a^2 (k comovil) — control estandar.
  B3  masa on-shell (EOM de a impuesta): masa_eff en terminos de U_tau_n.
      Regresion contra v2 (N=1, Mp2=1/2): masa_eff = -(4/a^2) sum n^2
      a^{-2(n-1)} U_tau_n.
  B4  comparacion con (7.22)+(7.23) usando el MISMO Mp2 en la accion y en la
      definicion de M_2^2  ==> residuo (si 0: no hay factor 2, la (7.22) es
      correcta tal como esta impresa, y el factor del acta era mezclar
      M_pl^2=1 en la formula con R/2 en la accion).
  B5  la comparacion INCONSISTENTE que hizo el acta (accion con R/2 pero
      (7.22) leida con M_pl^2 = 1): reproduce el factor 2 fantasma.
  B6  consistencia interna de BCP: (8.GW2) y (8.EOM) contra la (7.23) y contra
      nuestra derivacion — se decide cual ecuacion de BCP lleva errata.
  B7  prefactor cinetico ABSOLUTO de (7.23) vs derivado (en espacio real):
      se reporta el cociente (posible convencion de Fourier de BCP; no afecta
      EOM ni cocientes).

Convenciones: signatura (-,+,+,+); gauge unitario Phi^0 = t, Phi^a = x^a;
tau_n = Tr(B^n), B^{ab} = g^{mu nu} d_mu Phi^a d_nu Phi^b (bloque espacial de
la metrica inversa). Corre con: py -3.14 factor_722.py  (~1-2 min).
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
N = sp.Function('N', positive=True)(t)
hp = sp.Function('h_p', real=True)(t, z)
hx = sp.Function('h_x', real=True)(t, z)
Mp2 = sp.Symbol('Mp2', positive=True)          # coeficiente de R en la accion
c1, c2, c3, q11 = sp.symbols('c1 c2 c3 q11', real=True)

def ptrunc(e, n=2):
    e = sp.expand(e)
    return sum(e.coeff(eps, k)*eps**k for k in range(n+1))

# ---------------- metrica TT sobre FRW con lapse ----------------
hmat = sp.Matrix([[hp, hx, 0], [hx, -hp, 0], [0, 0, 0]])
g = sp.zeros(4, 4)
g[0, 0] = -N**2
for i in range(3):
    for j in range(3):
        g[i+1, j+1] = a**2*(sp.eye(3)[i, j] + eps*hmat[i, j])

gamma_inv = (sp.eye(3) - eps*hmat + eps**2*hmat*hmat)/a**2
ginv = sp.zeros(4, 4)
ginv[0, 0] = -1/N**2
for i in range(3):
    for j in range(3):
        ginv[i+1, j+1] = gamma_inv[i, j]
resid_inv = (g*ginv).applyfunc(lambda e: ptrunc(e, 2)) - sp.eye(4)
check("interno: g.ginv == 1 + O(eps^3)", sum(sp.Abs(sp.simplify(e)) for e in resid_inv))

detg = sp.expand(-g.det())
p0 = detg.coeff(eps, 0)
u = sp.expand(sp.cancel((detg - p0)/p0))
sqrtg = ptrunc(sp.sqrt(p0)*(1 + u/2 - u**2/8), 2)
sqrtg = sqrtg.subs(sp.sqrt(a**6*N**2), a**3*N)
check("interno: sqrtg^2 == -det g + O(eps^3)", ptrunc(sqrtg**2 - detg, 2))

# ---------------- curvatura (truncado polinomico) ----------------
def christoffel(g_, ginv_, coords_):
    n = len(coords_)
    Gam = [[[0]*n for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for m in range(n):
            for v in range(m, n):
                e = sum(ginv_[r, s]*(sp.diff(g_[s, m], coords_[v])
                                     + sp.diff(g_[s, v], coords_[m])
                                     - sp.diff(g_[m, v], coords_[s]))
                        for s in range(n))/2
                e = ptrunc(e, 2)
                Gam[r][m][v] = e
                Gam[r][v][m] = e
    return Gam

def ricci_tensor(Gam, coords_):
    n = len(coords_)
    Ric = sp.zeros(n, n)
    for m in range(n):
        for v in range(m, n):
            e = 0
            for r in range(n):
                e += sp.diff(Gam[r][m][v], coords_[r]) - sp.diff(Gam[r][r][m], coords_[v])
                for lam in range(n):
                    e += Gam[r][r][lam]*Gam[lam][m][v] - Gam[r][v][lam]*Gam[lam][r][m]
            e = ptrunc(e, 2)
            Ric[m, v] = e
            Ric[v, m] = e
    return Ric

print("== curvatura con lapse N(t) generico (tarda ~1 min) ==")
Gam = christoffel(g, ginv, coords)
Ric = ricci_tensor(Gam, coords)
R = ptrunc(sum(ginv[m, v]*Ric[m, v] for m in range(4) for v in range(4)), 2)
ad, add = sp.diff(a, t), sp.diff(a, t, 2)
Nd = sp.diff(N, t)
R0_esp = 6*(add/(a*N**2) + ad**2/(a**2*N**2) - ad*Nd/(a*N**3))
check("interno: R fondo (lapse) == 6[add/(a N^2) + ad^2/(a^2 N^2) - ad Nd/(a N^3)]",
      R.coeff(eps, 0) - R0_esp)

# ---------------- medio U(tau_n) ----------------
Bmat = ginv[1:, 1:]
tau1 = ptrunc(sp.trace(Bmat), 2)
Bmat2 = (Bmat*Bmat).applyfunc(lambda e: ptrunc(e, 2))
tau2 = ptrunc(sp.trace(Bmat2), 2)
Bmat3 = (Bmat2*Bmat).applyfunc(lambda e: ptrunc(e, 2))
tau3 = ptrunc(sp.trace(Bmat3), 2)
U = c1*tau1 + c2*tau2 + c3*tau3 + sp.Rational(1, 2)*q11*tau1**2
U = ptrunc(sp.expand(U), 2)
# primeras derivadas de U en el fondo (tau1 = 3/a^2):
Ut1_fondo = c1 + q11*3/a**2
Ut2_fondo = sp.S(c2)
Ut3_fondo = sp.S(c3)

# ---------------- accion y L2 ----------------
L_full = ptrunc(sp.expand(sqrtg*(Mp2*R + U)), 2)
L0 = L_full.coeff(eps, 0)
L2 = sp.expand(L_full.coeff(eps, 2))

# ---------------- B1: fondo (EOM de a con lapse, mini-superespacio) ----------
# L0 contiene add (el R sin integrar por partes). El mini-superespacio con la
# IPP temporal hecha es el estandar  L_EH,mini = -6 Mp2 a ad^2 / N  (con
# Mp2 = 1/2 reproduce el -3 a ad^2/N de fondo_frw.py). Chequeo la IPP:
U0_fondo = sp.expand(U.subs({hp: 0, hx: 0}))
L0mini = -6*Mp2*a*ad**2/N + N*a**3*U0_fondo
borde = 6*Mp2*a**2*ad/N
check("interno: L0 == L0mini + d/dt(6 Mp2 a^2 ad / N)",
      sp.expand(L0 - L0mini - sp.diff(borde, t).doit()))
eom_a = sp.expand((sp.diff(sp.diff(L0mini, ad), t) - sp.diff(L0mini, a)).doit())
# despejo add del fondo:
sol_add = sp.solve(sp.Eq(eom_a, 0), add)
print("\n== B1: EOM de fondo de a (Friedmann II con lapse) ==")
print("  add =", sp.simplify(sol_add[0]))

# ---------------- B2: EOM tensorial ----------------
def euler_lagrange_field(L, q):
    eom = sp.diff(L, q)
    for i in range(3):
        for j in range(3):
            if i == 0 and j == 0:
                continue
            D = sp.Derivative(q, *([t]*i + [z]*j))
            dLdD = sp.diff(L, D)
            if dLdD != 0:
                term = dLdD
                for _ in range(i): term = sp.diff(term, t)
                for _ in range(j): term = sp.diff(term, z)
                eom += (-1)**(i + j)*term
    return sp.expand(eom.doit())

print("\n== B2: coeficientes de la EOM de h_p (h_x identica por isotropia) ==")
eom = euler_lagrange_field(L2, hp)
ckin = sp.simplify(eom.coeff(sp.Derivative(hp, t, 2)))
cfric = sp.simplify(eom.coeff(sp.Derivative(hp, t)))
cgrad = sp.simplify(eom.coeff(sp.Derivative(hp, z, 2)))
cmass = sp.expand(eom.coeff(hp))
print("  coef(hpdd)          =", ckin)
print("  friccion/cinetico   =", sp.simplify(cfric/ckin))
H = ad/a
check("friccion/kin == 3H - Nd/N (la friccion estandar con lapse)",
      sp.simplify(cfric/ckin - (3*H - Nd/N)))
check("grad/kin == -N^2/a^2  (c_T^2 = 1: k comovil viaja con N^2/a^2)",
      sp.simplify(cgrad/ckin + N**2/a**2))

# EOM de h_x: mismo resultado (isotropia)
eom_x = euler_lagrange_field(L2, hx)
check("isotropia: EOM(h_x) tiene los mismos coeficientes",
      sp.simplify(sp.expand(eom_x.coeff(hx) - cmass))
      + sp.simplify(eom_x.coeff(sp.Derivative(hx, t, 2)) - ckin))

# ---------------- B3: masa on-shell ----------------
print("\n== B3: masa on-shell (impongo la EOM de fondo de a) ==")
masa_off = sp.simplify(cmass/ckin)
masa_on = sp.expand(sp.simplify(masa_off.subs(add, sol_add[0])))
masa_on = sp.simplify(masa_on)
print("  masa_eff (por chi, EOM normalizada: hpdd + ... + masa_eff*hp = 0 con signo:")
print("   masa_eff = -coef(hp)/coef(hpdd) ... aca reporto M2eff := cmass/ckin)")
print("  M2eff on-shell =", masa_on)
# forma esperada: (2/(Mp2)) * N^2/a^2 * sum n^2 a^{-2(n-1)} U_tau_n (con signo)
Sigma = Ut1_fondo + 4*Ut2_fondo/a**2 + 9*Ut3_fondo/a**4
check("M2eff on-shell == -(2/Mp2)*(N^2/a^2)*[sum n^2 a^{-2(n-1)} U_tau_n]",
      sp.expand(masa_on + (2/Mp2)*(N**2/a**2)*Sigma))
check("las SEGUNDAS derivadas U_tautau (q11) solo entran via U_tau1(fondo)",
      sp.expand(sp.expand(masa_on).coeff(q11) + (2/Mp2)*(N**2/a**2)*(3/a**2)))

# regresion contra v2 (N=1, Mp2=1/2, U lineal):
reg = masa_on.subs({N: 1, Mp2: sp.Rational(1, 2), q11: 0})
check("regresion v2 (N=1, Mp2=1/2): M2eff == -(4/a^2)(c1 + 4 c2/a^2 + 9 c3/a^4)",
      sp.expand(reg + (4/a**2)*(c1 + 4*c2/a**2 + 9*c3/a**4)))

# ---------------- B4: (7.22)+(7.23) con el MISMO Mp2 ----------------
print("\n== B4: comparacion consistente con BCP ==")
# (7.22): M2^2 = (1/M_pl^2) sum n^2 a^{-2(n-1)} U_tau_n, con M_pl^2 = Mp2
M22_BCP = Sigma/Mp2
# (7.23): L = (Mpl^2/2)[(a^3/N) chi' chi' + N a (2 M2^2 - k^2) chi chi]
# EOM de (7.23) para una componente chi (la normalizacion global cancela):
#   (a^3/N) chidd + d/dt(a^3/N) chid - N a (2 M2^2 - k^2) chi = 0
# => M2eff_(7.23) = -N^2/a^2 (2 M2^2 - k^2)|_{parte de masa} = -(2 N^2/a^2) M2^2
M2eff_723 = -(2*N**2/a**2)*M22_BCP
check("VEREDICTO B4: nuestra masa on-shell == la de (7.22)+(7.23) [mismo Mp2]",
      sp.expand(masa_on - M2eff_723))

# ---------------- B5: la comparacion que hizo el acta ----------------
print("\n== B5: reproduccion del 'factor 2' del acta ==")
# accion de la casa (Mp2 = 1/2) pero (7.22) leida con M_pl^2 = 1:
masa_casa = masa_on.subs({Mp2: sp.Rational(1, 2)})
M22_mal = Sigma  # M_pl^2 = 1 en (7.22)
M2eff_mal = -(2*N**2/a**2)*M22_mal
razon = sp.simplify(masa_casa/M2eff_mal)
print("  masa(casa, R/2) / masa((7.22) con M_pl^2=1) =", razon)
check("el 'factor 2 global' del acta reproducido: la razon es exactamente 2",
      razon - 2)

# ---------------- B6: consistencia interna de BCP ----------------
print("\n== B6: (8.GW2) y (8.EOM) de BCP contra (7.23) y contra lo derivado ==")
# En conforme (N=a), nuestra EOM: chidd + 2 (a'/a) chid + (k^2 - 2 M2^2) chi = 0
# [k comovil; ' = d/deta]. La (8.EOM) impresa: chidd + 2H chid + (k^2 - M2^2) chi.
eta = sp.Symbol('eta', real=True)
masa_conf = sp.simplify(masa_on.subs(N, a))          # M2eff en N=a (por chi)
# nuestro termino de masa en la EOM conforme (sin el k^2): -masa_conf*a^2... :
# la EOM general: hdd + (3H - Nd/N) hd + [N^2 k^2/a^2 + (-masa_on)] h = 0 (t generico)
# con N=a y pasando a eta (dt = a d eta con t el tiempo del lapse... N=a YA es eta):
# coeficiente de masa (sin gradiente) = -masa_conf. (7.23)->(k^2 - 2 M2^2);
# (8.EOM)->(k^2 - M2^2):
termino_723 = 2*M22_BCP.subs(N, a)
termino_8eom = M22_BCP.subs(N, a)
check("nuestro termino de masa conforme == 2*M2^2 [el de (7.23)]",
      sp.expand(-masa_conf - termino_723*1))
resid_8 = sp.simplify(sp.expand(-masa_conf - termino_8eom))
print(f"  residuo contra la (8.EOM) impresa (k^2 - M2^2): {resid_8}")
print("  => si el residuo de arriba es M2^2 (no cero): la EOM de GW impresa en la")
print("     seccion 8 de BCP lleva un factor 2 de errata en M2^2 (deberia ser")
print("     k^2 - 2 M2^2), ADEMAS del signo de k^2 en (GW2) [(2M2^2 + k^2) impreso;")
print("     de (7.23) con N=a se obtiene (2M2^2 - k^2)].")
check("residuo == M2^2 (la (8.EOM) esta a LA MITAD de la masa correcta)",
      sp.expand(resid_8 - M22_BCP.subs(N, a)))

# ---------------- B7: prefactor cinetico absoluto de (7.23) ----------------
print("\n== B7: normalizacion absoluta (cinetico y gradiente canonizados) ==")
# El L2 crudo contiene h*hdd y h*h'' (derivadas segundas): para leer el
# cinetico fisico hay que integrar por partes:
#   c1(t) f fdd -> -c1 fd^2 - c1d f fd   (IPP en t)
#   c3(t) f f'' -> -c3 f'^2              (IPP en z; c3 no depende de z)
f = hp
fd, fdd = sp.Derivative(f, t), sp.Derivative(f, t, 2)
fz, fzz = sp.Derivative(f, z), sp.Derivative(f, z, 2)
L2e = sp.expand(L2)
c_ffdd = L2e.coeff(fdd).coeff(f)          # coef de f*fdd
c_fdfd = L2e.coeff(fd, 2)                 # coef de fd^2
c_ffzz = L2e.coeff(fzz).coeff(f)          # coef de f*f''
c_fzfz = L2e.coeff(fz, 2)                 # coef de f'^2
kin_fis = sp.simplify(c_fdfd - c_ffdd)
grad_fis = sp.simplify(c_fzfz - c_ffzz)
print("  cinetico fisico  (coef de hp_dot^2 tras IPP)  =", kin_fis)
print("  gradiente fisico (coef de hp_z^2   tras IPP)  =", grad_fis)
# (7.23) por polarizacion: chi'chi' = 2(hp'^2+hx'^2), chi chi = 2(hp^2+hx^2):
#   cinetico_(7.23) = Mp2 a^3/N ;  gradiente_(7.23) = -Mp2 N a k^2 -> coef de
#   hp_z^2 en espacio real: -Mp2 N a * (-1) ... en Fourier -k^2 hp^2 ~ hp_z^2:
#   comparo coeficientes de k^2 hp^2 == -hp_z^2:  grad_(7.23) = -Mp2 N a.
r_kin = sp.simplify(kin_fis/(Mp2*a**3/N))
r_grad = sp.simplify(grad_fis/(-Mp2*N*a))
print("  cociente cinetico  [derivado/(7.23)] =", r_kin)
print("  cociente gradiente [derivado/(7.23)] =", r_grad)
check("el factor absoluto es GLOBAL (mismo cociente en cinetico y gradiente)",
      sp.simplify(r_kin - r_grad))
print("  => (7.23) escribe 1/r veces nuestro Lagrangiano en espacio real por")
print("     unidad de volumen comovil. Un factor global NO afecta la EOM ni")
print("     M_2^2: consistente con la convencion de modos de Fourier complejos")
print("     (chi chi* con condicion de realidad) no declarada en el paper.")
print("     Los cocientes fisicos (friccion, c_T^2, masa) ya cerraron arriba.")

print()
print("VEREDICTO TAREA B:", "TODO PASS" if ok else "HAY FALLOS — revisar arriba")
print("""
CONCLUSION (si TODO PASS):
 1. La (7.22) de BCP es CORRECTA tal como esta impresa, CON SU M_pl^2 =
    coeficiente de R de SU accion (S = M_pl^2 int sqrt(-g) R, es decir
    M_pl^2 = 1/(16 pi G)).
 2. El "factor 2 global" del acta FRW-2026-07-21 NO es una errata de BCP ni
    un error del pipeline: es la mezcla de convenciones M_pl^2 = 1 (formula)
    con R/2 (accion). Con el mismo M_pl^2 en los dos lados el residuo es 0.
 3. Bonus encontrado al dirimir: en la subseccion de GW de la seccion 8 de
    BCP, (GW2) lleva el signo de k^2 volteado y la ecuacion de propagacion
    impresa lleva M2^2 donde la (7.23) (correcta) da 2 M2^2. Erratas menores
    de BCP, sin consecuencia para nuestros resultados (U(X,Y) tiene M2^2 = 0
    identico), pero reportables si se reabre el canal con los autores.
""")
