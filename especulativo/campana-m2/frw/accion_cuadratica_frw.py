# -*- coding: utf-8 -*-
"""
accion_cuadratica_frw.py — TAREA A de la lista de bloqueo del paper missing-row
(item 5 / "Open problems" 2): ACCION CUADRATICA COMPLETA de las perturbaciones
del medio U(X,Y) + metrica sobre un fondo FLRW generico a(t), sector por sector
(tensor / vector / escalar).

GAUGE (declarado): unitario cosmologico EXACTO — Phi^0 = phi(t), Phi^a = x^a
sin fluctuar; las 10-4=... TODAS las perturbaciones van en la metrica. Los
cuatro difeomorfismos quedan completamente fijados por los cuatro campos de
Stuckelberg (phid != 0): NO queda gauge residual continuo sobre las
perturbaciones. (La simetria interna residual Phi^a -> Psi^a(Phi^b) del medio
NO es gauge del sistema total: es la simetria fisica que protege los ceros.)

DESCOMPOSICION SVT con k // z (sin perdida de generalidad por isotropia del
fondo; los tres sectores se desacoplan a orden cuadratico — teorema SVT):
  tensor:  gamma_ij = a^2 (delta_ij + h_ij^TT),  h_xx=-h_yy=hp, h_xy=hx
  vector:  N_i = eps S_i (transverso),  gamma_ij = a^2(delta_ij + d_i F_j + d_j F_i)
           [por isotropia basta la polarizacion x: S=(S,0,0), F=(F,0,0)]
  escalar: N = 1 + eps*alpha,  N_i = eps d_i beta,
           gamma_ij = a^2[(1+2 eps psi) delta_ij + 2 eps d_i d_j E]

VARIABLES ADM (declarado): la parametrizacion es la ADM exacta
  ds^2 = -N^2 dt^2 + gamma_ij (dx^i + N^i dt)(dx^j + N^j dt),
que difiere de la parametrizacion "g_00 = -(1+2 alpha)" de v4 en terminos
O(eps^2); las acciones cuadraticas de dos parametrizaciones difieren en
(EOM de fondo) x (campos)^2 y las EOM lineales coinciden ON-SHELL del fondo.
El cross-check S7 contra la matriz covariante de v4 verifica esto en numeros.

ACCION (convenciones de la campana): S = int sqrt(-g) [ R/2 + U(X,Y) ],
signatura (-,+,+,+), Mbar_Pl^2 = 1 (coeficiente R/2 => 1/(16 pi G) = 1/2).
En ADM (modulo el termino de borde de Gibbons–Hawking, derivada total):
  S = int dt d3x { (1/2) N sqrt(gamma) [ K_ij K^ij - K^2 + R3 ] + N sqrt(gamma) U }
  K_ij = (gammadot_ij - D_i N_j - D_j N_i)/(2N)
INVARIANTES EXACTOS en gauge unitario (derivados, no asumidos):
  X = C^00 = g^{00} phid^2 = -phid^2/N^2            (solo lapse)
  Y = u.dPhi^0 con u^mu = delta^mu_0/sqrt(-g_00)  (u resuelve u.dPhi^a = 0)
    = phid/sqrt(-g_00) = phid/sqrt(N^2 - N_i N^i)   (lapse Y shift!)
  [El shift entra en Y a orden cuadratico: un contraflujo transverso. De ahi
   la masa vectorial del medio — el analogo FRW del m1^2 h_0i h_0i.]
U(X,Y) ARBITRARIA: se expande en Taylor alrededor del fondo (X0=-phid^2,
Y0=phid) — para la accion CUADRATICA el Taylor a orden 2 es exacto, con
coeficientes U0(t), UX(t), ..., UYY(t) funciones del tiempo via phid(t), y
reglas de cadena declaradas (aparecen terceras derivadas UXXX(t)... via las
integraciones por partes; para la U cuadratica de las validaciones son 0).

FONDO on-shell (cuando se impone; derivado en A0):
  Friedmann I  : 3 H^2 = rho = -U0 - 2 phid^2 UX + phid UY
  Friedmann II : 2 addot/a + H^2 = -p = -U0
  EOM de phi   : J = a^3 (UY - 2 phid UX) conservada
La masa tensorial nula usa SOLO Friedmann II (identidad FLRW, sin tadpoles).

CHEQUEOS (PASS/FAIL):
 A0   fondo: L(eps^0) reproduce el mini-superespacio de fondo_frw.py.
 A0b  orden eps^1 (modo homogeneo): coef(alpha) = Friedmann I, coef(psi) =
      3 x Friedmann II, coef(E) = 0 — los tadpoles FRW correctos.
 T1   accion cuadratica tensorial canonizada:
        S2_T = int a^3/4 * [ hdot^2 - (dz h)^2/a^2 - M_T^2(t) h^2 ]  (por pol.)
      con M_T^2 = 0 IDENTICO al imponer SOLO Friedmann II, para U(X,Y)
      arbitraria sobre a(t) arbitrario. c_T^2 = 1 exacto AL ORDEN DOMINANTE
      (el LO U(X,Y); los NLO tipo alpha K.K desplazan c_T — fuera de este
      calculo, ya declarado en el paper §6). delta X = delta Y = 0
      REDESCUBIERTO por el calculo (no asumido).
 V1   accion cuadratica vectorial: S entra sin Sdot (constraint); F sin masa
      ni gradiente propios (R3 de un difeo espacial = 0: verificado).
 V2   integrando S: L_V ~ c(t) Fdot^2 — CERO potencial de F on-shell del fondo
      => el vector NO propaga sobre ningun FLRW (el analogo del M2^2 = 0:
      cf. BCP (7.24)-(7.25): "dispersion not trivial only when M2^2 != 0").
 V3   limite Minkowski: c = (m1^2/2) k^2/(k^2 + m1^2...) — el cero doble
      omega^2 * (coef) = 0 de la campana (sector vectorial congelado a LO).
 S1   sector escalar: alpha y beta son multiplicadores (sin derivadas
      temporales en L2) — verificado, no asumido. La ACCION CUADRATICA
      COMPLETA del sector escalar es L2Sk (4 campos, coeficientes en t):
      ese es el objeto entregado; la reduccion se hace en el sistema
      CONGELADO (declarado: la reduccion exacta con coeficientes
      t-dependientes no se entrega — ver "que quedo afuera" en el acta).
 S2   constraints (filas alpha, beta) algebraicas en omega — verificado;
      eliminacion por complemento de Schur en el sistema congelado.
 S4   validacion Minkowski (a=1, H=0, w=1, tadpoles): det de las EOM
      reducidas = c * omega^4 * m0^2 m1^2 (el CERO DOBLE de la campana, con
      el coeficiente correcto m0^2 m1^2).
 S5   atractor (esquina sana, w = 1+(3/2)H^2, congelado): BLANCO CORREGIDO
      2026-07-27 — la auditoria fisica de la seccion 9 refuto la formula del
      acta (+-(H/sqrt2)k + 3iH, artefacto de truncar antes del escaleo). El
      blanco es el orden dominante
        det_dom = k^3[-8i om^4 - 48 H om^3 + 4i H^2(k^2+18) om^2 + 24 k^2 H^3 om]
      con espectro PURAMENTE DISIPATIVO en la ventana EFT: {0 exacto,
      i(k^2/3)H difusivo, i(3 -+ k/sqrt2)H}, y k* ~ 1.27 donde nace Re(om).
      Este script NO trunca antes de escalar (blindaje anti-bug) y verifica
      el cero omega=0 exacto sobre el fondo on-shell exacto.
 S6   no-fantasma sobre FRW: autovalores de la matriz cinetica K reducida
      sobre el atractor de la esquina sana — el enunciado nuevo mas alla del
      limite Minkowski. Se reporta el resultado tal cual salga.
 S7   cross-check adversarial: det del sistema 4x4 congelado propio
      proporcional al det de la matriz de v4 (ruta covariante independiente),
      razon independiente de omega (numerico, varios puntos).

LECCION METODOLOGICA (encontrada y corregida en este script, 2026-07-27):
en la ACCION cuadratica no vale el atajo f -> f e^{ikz} con division por
e^{2ikz}: (ik)^2 = -k^2 invierte el signo de TODOS los terminos de gradiente
respecto del modo real, y eso volteaba el signo del cinetico vectorial
(dando una constraint estatica oscilatoria en vez del Yukawa del paper y un
desacuerdo espurio con BCP (7.24)). En las EOM lineales el ansatz complejo
si es legitimo (v4 y el resto de la campana no estan afectados). Aca se usan
modos reales f(t) cos(kz) con promedio en z (funcion fourier_real). Tras la
correccion, el sector vectorial cierra contra BCP (7.24) EXACTO on-shell
(lectura H = adot/a) y contra Fierz-Pauli + patron (7.3).

USO:  py -3.14 accion_cuadratica_frw.py [T|V|S|todo]     (default: todo)
"""
import sys
import sympy as sp

ok = True
def check(nombre, expr, esperado=0):
    global ok
    r = sp.simplify(sp.expand(expr - esperado))
    estado = "PASS" if r == 0 else "FAIL"
    if r != 0: ok = False
    print(f"  [{estado}] {nombre}: residuo = {r}")

t, z = sp.symbols('t z', real=True)
eps = sp.Symbol('eps')
a = sp.Function('a', positive=True)(t)
ph = sp.Function('phi', real=True)(t)
w = sp.diff(ph, t)
H = sp.diff(a, t)/a
ad, add = sp.diff(a, t), sp.diff(a, t, 2)
I = sp.I
k = sp.Symbol('k', positive=True)

# ---- derivadas de U como funciones de t (Taylor exacto para S2) ----
U0f = sp.Function('U0')(t)
UXf = sp.Function('U_X')(t); UYf = sp.Function('U_Y')(t)
UXXf = sp.Function('U_XX')(t); UXYf = sp.Function('U_XY')(t); UYYf = sp.Function('U_YY')(t)
UXXXf = sp.Function('U_XXX')(t); UXXYf = sp.Function('U_XXY')(t)
UXYYf = sp.Function('U_XYY')(t); UYYYf = sp.Function('U_YYY')(t)
X0, Y0 = -w**2, w
X0d, Y0d = sp.diff(X0, t), sp.diff(Y0, t)   # -2 w wdot ; wdot
regla_cadena = {
    sp.Derivative(U0f, t):  UXf*X0d + UYf*Y0d,
    sp.Derivative(UXf, t):  UXXf*X0d + UXYf*Y0d,
    sp.Derivative(UYf, t):  UXYf*X0d + UYYf*Y0d,
    sp.Derivative(UXXf, t): UXXXf*X0d + UXXYf*Y0d,
    sp.Derivative(UXYf, t): UXXYf*X0d + UXYYf*Y0d,
    sp.Derivative(UYYf, t): UXYYf*X0d + UYYYf*Y0d,
}
def aplica_cadena(e):
    e = sp.expand(e.doit())
    for _ in range(4):
        e2 = sp.expand(e.subs(regla_cadena, simultaneous=True).doit())
        if e2 == e:
            break
        e = e2
    return e

def ptrunc(e, n=2):
    e = sp.expand(e)
    return sum(e.coeff(eps, j)*eps**j for j in range(n+1))

def taylor_U(Xp, Yp):
    """U(Xp,Yp) a orden eps^2 alrededor del fondo (exacto para S2)."""
    dX = ptrunc(sp.expand(Xp - X0), 2)
    dY = ptrunc(sp.expand(Yp - Y0), 2)
    return ptrunc(U0f + UXf*dX + UYf*dY
                  + sp.Rational(1, 2)*UXXf*dX**2 + UXYf*dX*dY
                  + sp.Rational(1, 2)*UYYf*dY**2, 2)

# ---- rutinas geometricas 3D (truncado polinomico en eps) ----
def christoffel3(gam, gaminv, xyz, n_=2):
    G = [[[0]*3 for _ in range(3)] for _ in range(3)]
    for r in range(3):
        for m in range(3):
            for v in range(m, 3):
                e = sum(gaminv[r, s]*(sp.diff(gam[s, m], xyz[v])
                                      + sp.diff(gam[s, v], xyz[m])
                                      - sp.diff(gam[m, v], xyz[s]))
                        for s in range(3))/2
                e = ptrunc(e, n_)
                G[r][m][v] = e
                G[r][v][m] = e
    return G

def ricci3(G, xyz, n_=2):
    Ric = sp.zeros(3, 3)
    for m in range(3):
        for v in range(m, 3):
            e = 0
            for r in range(3):
                e += sp.diff(G[r][m][v], xyz[r]) - sp.diff(G[r][r][m], xyz[v])
                for lam in range(3):
                    e += G[r][r][lam]*G[lam][m][v] - G[r][v][lam]*G[lam][r][m]
            e = ptrunc(e, n_)
            Ric[m, v] = e
            Ric[v, m] = e
    return Ric

xs, ys = sp.symbols('x y', real=True)
XYZ = (xs, ys, z)

def sqrt_serie(expr_pol):
    """sqrt de un polinomio en eps con parte 0 positiva, a orden eps^2."""
    e = sp.expand(expr_pol)
    p0 = e.coeff(eps, 0)
    u = sp.expand(sp.cancel((e - p0)/p0))
    return ptrunc(sp.sqrt(p0)*(1 + u/2 - u**2/8), 2)

def adm_L(N_, Ni_cov, gam, n_=2):
    """L = (1/2) N sqrt(gamma)(K.K - K^2 + R3) + N sqrt(gamma) U(X,Y), a eps^2.
    Ni_cov: lista [N_x, N_y, N_z] covariante. Devuelve (L, sqrtgam, R3)."""
    # inversa 3D por serie de Neumann alrededor del fondo (gam0 = gam|eps=0):
    gam0 = gam.applyfunc(lambda e: sp.expand(e).subs(eps, 0))
    gam0inv = gam0.inv()
    dg = (gam - gam0).applyfunc(sp.expand)
    gaminv = (gam0inv - gam0inv*dg*gam0inv
              + gam0inv*dg*gam0inv*dg*gam0inv).applyfunc(lambda e: ptrunc(sp.expand(e), n_))
    chk = (gam*gaminv).applyfunc(lambda e: ptrunc(sp.expand(e), n_)) - sp.eye(3)
    assert all(sp.expand(e) == 0 for e in chk), "inversa 3D mal truncada"
    G3 = christoffel3(gam, gaminv, XYZ, n_)
    Ric3 = ricci3(G3, XYZ, n_)
    R3 = ptrunc(sum(gaminv[m, v]*Ric3[m, v] for m in range(3) for v in range(3)), n_)
    # D_i N_j = d_i N_j - Gamma^k_ij N_k
    DN = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            DN[i, j] = ptrunc(sp.diff(Ni_cov[j], XYZ[i])
                              - sum(G3[kk][i][j]*Ni_cov[kk] for kk in range(3)), n_)
    Kij = sp.zeros(3, 3)
    # 1/N como serie en eps (N_ = 1 + eps(...)):
    dN = sp.expand(N_ - 1)
    Ninv = ptrunc(1 - dN + dN**2, n_)
    for i in range(3):
        for j in range(3):
            Kij[i, j] = ptrunc((sp.diff(gam[i, j], t) - DN[i, j] - DN[j, i])*Ninv/2, n_)
    KK = ptrunc(sum(gaminv[i, m]*gaminv[j, v]*Kij[i, j]*Kij[m, v]
                    for i in range(3) for j in range(3)
                    for m in range(3) for v in range(3)), n_)
    Ktr = ptrunc(sum(gaminv[i, j]*Kij[i, j] for i in range(3) for j in range(3)), n_)
    sqrtgam = sqrt_serie(-(-gam.det()))
    # invariantes del medio:
    Xp = ptrunc(-w**2*Ninv**2, n_)
    NiNi = ptrunc(sum(gaminv[i, j]*Ni_cov[i]*Ni_cov[j] for i in range(3) for j in range(3)), n_)
    # Y = phid/sqrt(N^2 - NiNi):  1/sqrt(N^2 - NiNi) en serie
    arg = ptrunc(sp.expand(N_**2 - NiNi), n_)
    p0 = arg.coeff(eps, 0)
    du = sp.expand(sp.cancel((arg - p0)/p0))
    inv_sqrt = ptrunc((1 - du/2 + 3*du**2/8)/sp.sqrt(p0), n_)
    Yp = ptrunc(w*inv_sqrt, n_)
    Umedio = taylor_U(Xp, Yp)
    L = ptrunc(N_*sqrtgam*(sp.Rational(1, 2)*(KK - Ktr**2 + R3) + Umedio), n_)
    return L, sqrtgam, R3, Xp, Yp

# ---- canonicalizacion temporal (IPP modulo derivadas totales) ----
def canon_t(L, campos, mult=()):
    """L cuadratico en campos(t) y sus derivadas temporales (tras Fourier en z).
    IPP hasta forma canonica:
      - ningun f_dd;
      - los multiplicadores m in mult aparecen SOLO sin derivar;
      - c*f*f_d -> -(c_d/2) f^2;
      - c*f*g_d -> (c/2)(f g_d - f_d g) - (c_d/2) f g   (solo campos dinamicos).
    Coeficientes: funciones de t (regla de cadena de U aplicada)."""
    L = sp.expand(aplica_cadena(L))
    for _ in range(30):
        cambio = False
        nuevo = sp.S(0)
        for term in L.as_ordered_terms():
            hecho = False
            # regla 1: segundas derivadas de cualquier campo
            for f in campos:
                fdd = sp.Derivative(f, t, 2)
                if term.has(fdd):
                    resto = sp.cancel(term/fdd)
                    if resto.has(fdd):
                        nuevo += term          # fdd^2: se deja (se reporta)
                        hecho = True
                        break
                    if any(resto.has(m) for m in mult):
                        nuevo += term          # fdd * multiplicador: se deja
                        hecho = True           # (lo maneja la constraint;
                        break                  # evita el ping-pong de IPP)
                    fd_ = sp.Derivative(f, t)
                    if resto.has(fd_):
                        c_ = sp.cancel(resto/fd_)
                        if not c_.has(fd_) and not c_.has(f):
                            # c fdd fd = (c/2) d/dt(fd^2) -> -(cd/2) fd^2
                            nuevo += sp.expand(-sp.diff(c_, t)/2*fd_**2)
                            cambio = True
                            hecho = True
                            break
                    nuevo += sp.expand(-sp.diff(resto, t)*sp.Derivative(f, t))
                    cambio = True
                    hecho = True
                    break
            if hecho:
                continue
            # regla 2: primeras derivadas de multiplicadores
            for m in mult:
                md = sp.Derivative(m, t)
                if term.has(md):
                    resto = sp.cancel(term/md)
                    if not resto.has(md):
                        nuevo += sp.expand(-sp.diff(resto, t)*m)
                        cambio = True
                    else:
                        nuevo += term     # md^2: no reducible (se reporta afuera)
                    hecho = True
                    break
            if not hecho:
                nuevo += term
        L = sp.expand(aplica_cadena(nuevo))
        if not cambio:
            break
    # reglas 3 y 4 (una pasada): solo entre campos dinamicos
    din = [f for f in campos if f not in mult]
    out = sp.S(0)
    for term in L.as_ordered_terms():
        hecho = False
        for i, f in enumerate(din):
            fd = sp.Derivative(f, t)
            # c f fd -> -(cd/2) f^2
            if term.has(fd) and term.has(f):
                c = sp.cancel(term/(f*fd))
                if not c.has(f) and not c.has(fd):
                    out += sp.expand(-sp.diff(c, t)/2*f**2)
                    hecho = True
                    break
            for j in range(i+1, len(din)):
                g = din[j]
                gd = sp.Derivative(g, t)
                if term.has(gd) and term.has(f) and not term.has(fd):
                    c = sp.cancel(term/(f*gd))
                    if not any(c.has(v) for v in (f, g, fd, gd)):
                        out += sp.expand(c/2*(f*gd - fd*g) - sp.diff(c, t)/2*f*g)
                        hecho = True
                        break
                if term.has(fd) and term.has(g) and not term.has(gd):
                    c = sp.cancel(term/(g*fd))
                    if not any(c.has(v) for v in (f, g, fd, gd)):
                        out += sp.expand(-c/2*(f*gd - fd*g) - sp.diff(c, t)/2*f*g)
                        hecho = True
                        break
            if hecho:
                break
        if not hecho:
            out += term
    out = sp.expand(aplica_cadena(out))
    # control: derivadas de multiplicadores no deben quedar; los f_dd solo
    # pueden quedar multiplicando un multiplicador (regla anti-ping-pong).
    residuales = [m for m in mult if out.has(sp.Derivative(m, t))]
    for f in campos:
        fdd = sp.Derivative(f, t, 2)
        if out.has(fdd):
            for term in out.as_ordered_terms():
                if term.has(fdd) and not any(term.has(m) for m in mult):
                    residuales.append(f)
                    break
    if residuales:
        print(f"  [WARN canon_t] quedaron derivadas no canonicas de: {residuales}")
    return out

# ---- reglas on-shell del fondo ----
rho_bg = -U0f - 2*w**2*UXf + w*UYf
p_bg = U0f
f_J = UYf - 2*w*UXf                      # J/a^3 = f_J(w)
fp_J = sp.expand(aplica_cadena(sp.diff(f_J, t))/sp.diff(w, t))  # d f_J / d w
wdot_rule = -3*H*f_J/fp_J                # EOM de phi (J conservada)
# Friedmann II PURA (EOM de a: 2 addot/a + H^2 = -p, SIN usar Friedmann I):
addot_rule = sp.expand(-a*(p_bg + H**2)/2)

# ---- Fourier REAL para la ACCION (aprendizaje de este script, declarado):
# en la accion cuadratica NO vale sustituir f -> f e^{ikz} y dividir por
# e^{2ikz}: (ik)^2 = -k^2 invierte el signo de los terminos de gradiente
# respecto del modo real ((d_z f)^2 -> +k^2 f^2/2). En las EOM lineales el
# ansatz complejo si vale (por eso v4 esta a salvo). Aca: modos reales
# f(t,z) = f(t) cos(kz), expandir y promediar en z (cos^2, sin^2 -> 1/2;
# sin cos -> 0). El factor global 1/2 del promedio es comun a todos los
# terminos (irrelevante para EOM y cocientes).
def fourier_real(L, mapa):
    ckz, skz = sp.cos(k*z), sp.sin(k*z)
    subs_c = {f_tz: f_t*ckz for f_tz, f_t in mapa.items()}
    Lf = L.subs(subs_c, simultaneous=True).doit()
    Lf = sp.expand(Lf)
    Lf = Lf.subs({ckz**2: sp.Rational(1, 2), skz**2: sp.Rational(1, 2)},
                 simultaneous=True)
    Lf = sp.expand(Lf.subs(ckz*skz, 0))
    if Lf.has(z):
        raise RuntimeError("fourier_real: quedo dependencia en z sin promediar")
    return Lf

# ---- maquinaria covariante 4D (usada por T y por la ruta de control de V) ----
coords4 = (t, xs, ys, z)
def christoffel4(g_, ginv_):
    G = [[[0]*4 for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for m in range(4):
            for v in range(m, 4):
                e = sum(ginv_[r, s]*(sp.diff(g_[s, m], coords4[v])
                                     + sp.diff(g_[s, v], coords4[m])
                                     - sp.diff(g_[m, v], coords4[s]))
                        for s in range(4))/2
                e = ptrunc(e, 2)
                G[r][m][v] = e
                G[r][v][m] = e
    return G

def ricci4(G):
    Ric = sp.zeros(4, 4)
    for m in range(4):
        for v in range(m, 4):
            e = 0
            for r in range(4):
                e += sp.diff(G[r][m][v], coords4[r]) - sp.diff(G[r][r][m], coords4[v])
                for lam in range(4):
                    e += G[r][r][lam]*G[lam][m][v] - G[r][v][lam]*G[lam][r][m]
            Ric[m, v] = ptrunc(e, 2)
            Ric[v, m] = Ric[m, v]
    return Ric

def L2_covariante(g4, g4inv):
    """eps^2 de sqrt(-g)[R/2 + U(X,Y)] con X = g^{00} w^2, Y = w/sqrt(-g_00),
    U via Taylor exacto. Chequea la inversa. Devuelve (L2, dX, dY)."""
    resid = (g4*g4inv).applyfunc(lambda e: ptrunc(e, 2)) - sp.eye(4)
    assert all(sp.expand(sp.simplify(e)) == 0 for e in resid), "inversa 4D mala"
    Xp = ptrunc(g4inv[0, 0]*w**2, 2)
    # Y = w/sqrt(-g_00): -g_00 = 1 - eps(...) en serie:
    mg00 = sp.expand(-g4[0, 0])
    p0 = mg00.coeff(eps, 0)
    du = sp.expand(sp.cancel((mg00 - p0)/p0))
    inv_sqrt = ptrunc((1 - du/2 + 3*du**2/8)/sp.sqrt(p0), 2)
    Yp = ptrunc(w*inv_sqrt, 2)
    G4 = christoffel4(g4, g4inv)
    Ric4 = ricci4(G4)
    R4 = ptrunc(sum(g4inv[m, v]*Ric4[m, v] for m in range(4) for v in range(4)), 2)
    detg = sp.expand(-g4.det())
    sq = sqrt_serie(detg)
    sq = sq.subs(sp.sqrt(a**6), a**3)
    L = ptrunc(sp.expand(sq*(R4/2 + taylor_U(Xp, Yp))), 2)
    return sp.expand(L.coeff(eps, 2)), sp.expand(Xp - X0), sp.expand(Yp - Y0)

sector = (sys.argv[1] if len(sys.argv) > 1 else "todo").upper()

# ============================================================
# FONDO + LINEAL (A0, A0b) — con la parametrizacion escalar completa
# ============================================================
if sector in ("TODO", "S", "A0"):
    print("=" * 72)
    print("A0/A0b: fondo y tadpoles FRW (parametrizacion escalar, modo k=0)")
    print("=" * 72)
    al = sp.Function('alpha_h', real=True)(t)
    psih = sp.Function('psi_h', real=True)(t)
    Eh = sp.Function('E_h', real=True)(t)
    # modo homogeneo: beta no aparece (entra con d_i beta)
    N_ = 1 + eps*al
    gam = sp.zeros(3, 3)
    gam[0, 0] = gam[1, 1] = a**2*(1 + 2*eps*psih)
    gam[2, 2] = a**2*(1 + 2*eps*psih)     # E entra con d_z^2: 0 en k=0... salvo E''
    # OJO: en k=0, d_i d_j E = 0 => E desaparece: chequeo coef(E)=0 trivial.
    L_h, _, _, _, _ = adm_L(N_, [0, 0, 0], gam)
    L0 = L_h.coeff(eps, 0)
    check("A0: L(eps^0) == -3 a adot^2 + a^3 U0 (mini-superespacio de fondo_frw)",
          sp.expand(L0 - (-3*a*ad**2 + a**3*U0f)))
    L1 = sp.expand(L_h.coeff(eps, 1))
    cal = sp.expand(L1.coeff(al)); cps = sp.expand(L1.coeff(psih))
    # coef(alpha): a^3 [ U0 + 2w^2 UX - w UY ... ] = -a^3 rho + ... derivado:
    check("A0b: coef(alpha) == -a^3 rho + 3 a adot^2  (Friedmann I como tadpole)",
          sp.expand(cal - (-a**3*rho_bg - (-3*a*ad**2))))
    # coef(psi): tadpole espacial — Friedmann II pura (+ I si hiciera falta):
    cps_on = sp.expand(cps.subs(add, addot_rule))
    cps_on = sp.expand(aplica_cadena(cps_on))
    cps_on2 = sp.expand(cps_on.subs(ad**2, rho_bg*a**2/3))
    check("A0b: coef(psi) == 0 al imponer Friedmann II (+ I) (tadpole espacial)",
          sp.simplify(cps_on2))

# ============================================================
# SECTOR TENSORIAL (T1) — ruta covariante 4D, U generica via Taylor
# ============================================================
if sector in ("TODO", "T"):
    print()
    print("=" * 72)
    print("T: sector tensorial — accion cuadratica covariante, U(X,Y) arbitraria")
    print("=" * 72)
    hp = sp.Function('h_p', real=True)(t, z)
    hx = sp.Function('h_x', real=True)(t, z)
    hmat = sp.Matrix([[hp, hx, 0], [hx, -hp, 0], [0, 0, 0]])
    g4 = sp.zeros(4, 4)
    g4[0, 0] = -1
    for i in range(3):
        for j in range(3):
            g4[i+1, j+1] = a**2*(sp.eye(3)[i, j] + eps*hmat[i, j])
    gamma_inv = (sp.eye(3) - eps*hmat + eps**2*hmat*hmat)/a**2
    g4inv = sp.zeros(4, 4)
    g4inv[0, 0] = -1
    for i in range(3):
        for j in range(3):
            g4inv[i+1, j+1] = gamma_inv[i, j]

    L2T, dXT, dYT = L2_covariante(g4, g4inv)
    print(f"  delta X (calculado) = {dXT}")
    print(f"  delta Y (calculado) = {dYT}")
    check("T: delta X == 0 (redescubierto: el TT no toca g^00)", dXT)
    check("T: delta Y == 0 (redescubierto: el TT no toca g_00)", dYT)

    # canonizar: primero IPP en z de los h*h'' (coef sin z), luego canon_t
    for f in (hp, hx):
        fzz = sp.Derivative(f, z, 2)
        cf = sp.expand(L2T.coeff(fzz).coeff(f))
        L2T = sp.expand(L2T - cf*f*fzz - cf*sp.Derivative(f, z)**2)
    campos_T = [hp, hx]
    L2Tc = canon_t(L2T, campos_T)
    ckin = sp.expand(L2Tc.coeff(sp.Derivative(hp, t), 2))
    cgrad = sp.expand(L2Tc.coeff(sp.Derivative(hp, z), 2))
    cmass = sp.expand(L2Tc.coeff(hp, 2))
    print(f"  S2_T (canonizada, por polarizacion h_p):")
    print(f"    coef(hp_dot^2)  = {ckin}")
    print(f"    coef(hp_z^2)    = {cgrad}")
    print(f"    coef(hp^2) off-shell = {sp.simplify(cmass)}")
    # por polarizacion: (Mbar^2/8) chi_ij chi_ij = (1/8)*2*(hp^2+hx^2) => 1/4
    check("T1: cinetico == a^3/4 por polarizacion (== (Mbar^2/8) a^3 chi.chi; "
          "consistente con B7 de factor_722: (Mp2/2)(a^3/N), Mp2=1/2)",
          ckin - a**3/4)
    check("T1: c_T^2 == 1  (gradiente/cinetico == -1/a^2 con k comovil)",
          sp.simplify(cgrad/ckin + 1/a**2))
    cmass_on = sp.expand(aplica_cadena(cmass.subs(add, addot_rule)))
    check("T1: MASA TENSORIAL on-shell (solo Friedmann II) == 0 — IDENTIDAD "
          "FLRW, U(X,Y) arbitraria, a(t) arbitrario, SIN tadpoles", cmass_on)
    check("T1: isotropia (h_x identica)",
          sp.expand(L2Tc.coeff(sp.Derivative(hx, t), 2) - ckin)
          + sp.expand(L2Tc.coeff(hx, 2) - cmass))

# ============================================================
# SECTOR VECTORIAL (V1-V3) — ADM
# ============================================================
if sector in ("TODO", "V"):
    print()
    print("=" * 72)
    print("V: sector vectorial — ADM, polarizacion x, k // z")
    print("=" * 72)
    S_ = sp.Function('S_v', real=True)(t, z)
    F_ = sp.Function('F_v', real=True)(t, z)
    gamV = sp.zeros(3, 3)
    gamV[0, 0] = gamV[1, 1] = gamV[2, 2] = a**2
    gamV[0, 2] = gamV[2, 0] = a**2*eps*sp.diff(F_, z)
    NiV = [eps*S_, 0, 0]
    L_V, sqg_V, R3_V, Xp_V, Yp_V = adm_L(1, NiV, gamV)
    check("V: R3(gamma) == 0 a todo orden calculado (difeo espacial puro)",
          sp.expand(R3_V))
    check("V: delta X == 0 (el vector no toca el lapse)", sp.expand(Xp_V - X0))
    dY2 = sp.expand(Yp_V - Y0)
    print(f"  delta Y = {dY2}   [= eps^2 w S^2/(2a^2): el contraflujo transverso]")
    check("V: delta Y == eps^2 * w S^2/(2 a^2)", dY2 - eps**2*w*S_**2/(2*a**2))
    L2V = sp.expand(L_V.coeff(eps, 2))
    check("V1: S entra SIN derivada temporal (constraint, no asumido)",
          sp.Integer(1 if L2V.has(sp.Derivative(S_, t)) else 0))

    # Fourier REAL: f(t,z) -> f(t) cos(kz), promedio en z (ver fourier_real)
    Sk = sp.Function('S_k')(t); Fk = sp.Function('F_k')(t)
    L2Vk = fourier_real(L2V, {S_: Sk, F_: Fk})
    check("V: modo real promediado sin residuos (ni z ni i)",
          sp.Integer(1 if (L2Vk.has(z) or L2Vk.has(I)) else 0))
    L2Vk = canon_t(L2Vk, [Sk, Fk], mult=(Sk,))
    print("  L2_V (canonizada) =", sp.collect(L2Vk, [Sk, sp.Derivative(Fk, t)]))

    def reduce_S(L2can, Svar, Fvar):
        """L = c1 S^2 + S(c2 Fdot + c3 F) + [c4 Fdot^2 + c5 Fdot F + c6 F^2]
        => L_red = cK Fdot^2 + cX Fdot F + cM0 F^2 con
           cK = c4 - c2^2/(4c1), cX = c5 - c2 c3/(2c1), cM0 = c6 - c3^2/(4c1);
        canonizando (IPP del termino cruzado): potencial fisico
           cM = cM0 - (d/dt cX)/2.
        Devuelve (cK, cM, S_resuelto). Todo por coeficientes explicitos."""
        Fd_ = sp.Derivative(Fvar, t)
        c1_ = sp.expand(L2can.coeff(Svar, 2))
        lin = sp.expand(L2can.coeff(Svar, 1))
        c2_ = sp.expand(lin.coeff(Fd_))
        c3_ = sp.expand(sp.expand(lin - c2_*Fd_).coeff(Fvar))
        assert sp.expand(lin - c2_*Fd_ - c3_*Fvar) == 0, "lineal en S no es (Fdot,F)"
        resto = sp.expand(L2can.coeff(Svar, 0))
        pol = sp.Poly(resto, Fvar, Fd_)
        c4_ = pol.coeff_monomial(Fd_**2)
        c5_ = pol.coeff_monomial(Fvar*Fd_)
        c6_ = pol.coeff_monomial(Fvar**2)
        assert sp.expand(resto - c4_*Fd_**2 - c5_*Fvar*Fd_ - c6_*Fvar**2) == 0
        Ssol_ = -(c2_*Fd_ + c3_*Fvar)/(2*c1_)
        cK_ = c4_ - c2_**2/(4*c1_)
        cX_ = c5_ - c2_*c3_/(2*c1_)
        cM_ = c6_ - c3_**2/(4*c1_) - aplica_cadena(sp.diff(cX_, t))/2
        return cK_, cM_, Ssol_

    def onshell_num(e):
        """fondo on-shell completo aplicado a un POLINOMIO (numerador):
        Friedmann II pura + EOM de phi (multiplicada por fp_J) iteradas,
        Friedmann I (ad^2 -> rho a^2/3) al final. Devuelve el numerador
        equivalente (cero sii la expresion original es cero on-shell)."""
        e = sp.expand(aplica_cadena(e))
        for _ in range(8):
            e0 = e
            if e.has(add):
                e = sp.expand(e.subs(add, addot_rule))
            if e.has(sp.Derivative(ph, t, 2)):
                # phidd -> -3H f_J/fp_J: multiplico por fp_J^n (no nulo
                # genericamente) via numerador de together:
                e = sp.together(e.subs(sp.Derivative(ph, t, 2),
                                       sp.together(wdot_rule)))
                e = sp.expand(sp.numer(e))
            e = sp.expand(aplica_cadena(e))
            if e == e0:
                break
        for _ in range(4):
            e0 = e
            e = sp.expand(e.subs(ad**3, rho_bg*a**2*ad/3))
            e = sp.expand(e.subs(ad**2, rho_bg*a**2/3))
            e = sp.expand(aplica_cadena(e))
            if e == e0:
                break
        return sp.expand(e)

    cK_adm, cM_adm, Ssol = reduce_S(L2Vk, Sk, Fk)
    print("  S resuelto =", sp.simplify(Ssol))
    cFd = sp.cancel(sp.together(cK_adm))
    print(f"  L_V reducida: coef(Fdot^2) = {cFd}")
    # RESULTADO FUERTE (con el Fourier real; el residuo ~ (f_J, U0) de una
    # version intermedia era artefacto del kernel complejo): el potencial de
    # F es  cM = -(k^2 a^3/4)(U0 + 2 addot/a + H^2)  — proporcional a la
    # MISMA combinacion de Friedmann II que la masa tensorial. Se anula
    # IDENTICAMENTE sobre cualquier FLRW on-shell, para U(X,Y) ARBITRARIA,
    # sin tadpoles ni atractor: la identidad FLRW del sector vectorial.
    print(f"  potencial de F off-shell: cM = {sp.simplify(sp.together(cM_adm))}")
    cM_FII = sp.expand(sp.expand(cM_adm).subs(add, addot_rule).doit())
    cM_FII = sp.expand(aplica_cadena(cM_FII))
    check("V2: potencial de F on-shell == 0 con SOLO Friedmann II — "
          "IDENTIDAD FLRW (U(X,Y) arbitraria, a(t) arbitrario, sin tadpoles): "
          "el analogo vectorial exacto de M_T^2 = 0", sp.simplify(cM_FII))

    # ---- V0: ruta covariante independiente (parametrizacion g_00 = -1) ----
    print()
    print("  --- V0: control por la ruta covariante 4D (g_00 = -1 exacto) ---")
    Sc = sp.Function('S_c', real=True)(t, z)
    Fc = sp.Function('F_c', real=True)(t, z)
    g4v = sp.zeros(4, 4)
    g4v[0, 0] = -1
    g4v[1, 1] = g4v[2, 2] = g4v[3, 3] = a**2
    g4v[0, 1] = g4v[1, 0] = eps*Sc
    g4v[1, 3] = g4v[3, 1] = a**2*eps*sp.diff(Fc, z)
    # inversa por Neumann 4D:
    g0 = g4v.applyfunc(lambda e: sp.expand(e).subs(eps, 0))
    g0i = sp.diag(-1, 1/a**2, 1/a**2, 1/a**2)
    dg = (g4v - g0).applyfunc(sp.expand)
    g4vinv = (g0i - g0i*dg*g0i + g0i*dg*g0i*dg*g0i).applyfunc(lambda e: ptrunc(sp.expand(e), 2))
    L2Vcov, dXv, dYv = L2_covariante(g4v, g4vinv)
    print(f"  delta X (covariante) = {dXv}   [aqui el S^2 entra por X, no por Y]")
    check("V0: delta Y == 0 en esta parametrizacion (g_00 = -1)", dYv)
    Sck = sp.Function('S_ck')(t); Fck = sp.Function('F_ck')(t)
    L2Vcovk = fourier_real(L2Vcov, {Sc: Sck, Fc: Fck})
    check("V0: modo real promediado sin residuos",
          sp.Integer(1 if (L2Vcovk.has(z) or L2Vcovk.has(I)) else 0))

    # En esta parametrizacion S NO es multiplicador puro (aparece Sdot en el
    # EH): comparo por EOMs variacionales de orden alto + det congelado
    # numerico contra la ruta ADM, en el fondo on-shell de la esquina sana.
    def eom_var_alto(L, q):
        e = sp.diff(L, q)
        for n_ in (1, 2):
            dLd = sp.diff(L, sp.Derivative(q, t, n_))
            if dLd != 0:
                term = dLd
                for _ in range(n_):
                    term = sp.diff(term, t)
                e += (-1)**n_*term
        return sp.expand(aplica_cadena(sp.expand(e)))

    def matriz2_congelada(L, q1, q2, om_):
        eqs_ = [eom_var_alto(L, q1), eom_var_alto(L, q2)]
        s1, s2 = sp.symbols('s1_ s2_')
        M2_ = sp.zeros(2, 2)
        for i, e in enumerate(eqs_):
            subs_f = {}
            for qq, s in ((q1, s1), (q2, s2)):
                for n_ in (4, 3, 2, 1):
                    subs_f[sp.Derivative(qq, t, n_)] = (sp.I*om_)**n_*s
                subs_f[qq] = s
            ee = sp.expand(e.subs(subs_f, simultaneous=True))
            M2_[i, 0] = ee.coeff(s1)
            M2_[i, 1] = ee.coeff(s2)
        return M2_

    M2_adm = matriz2_congelada(L2Vk, Sk, Fk, om := sp.Symbol('omega'))
    M2_cov = matriz2_congelada(L2Vcovk, Sck, Fck, om)
    det_adm = sp.expand(M2_adm.det())
    det_cov = sp.expand(M2_cov.det())

    # V0b (diagnostico simbolico): proporcionalidad de los dets con fondo
    # generico on-shell, coeficiente a coeficiente en omega:
    ca2 = sp.expand(det_adm).coeff(om, 2)
    cc2 = sp.expand(det_cov).coeff(om, 2)
    resid_prop = []
    for n_ in (0, 1, 2):
        can = sp.expand(det_adm).coeff(om, n_)
        ccn = sp.expand(det_cov).coeff(om, n_)
        dif = sp.expand(can*cc2 - ccn*ca2)
        dif_on = onshell_num(sp.expand(sp.numer(sp.together(dif))))
        resid_prop.append(sp.simplify(dif_on))
        print(f"  V0b: residuo de proporcionalidad coef(om^{n_}): "
              f"{'0' if resid_prop[-1] == 0 else 'NO NULO'}")
    check("V0b: det_ADM proporcional a det_cov ON-SHELL simbolico "
          "(coeficiente a coeficiente)", sum(sp.Abs(r) for r in resid_prop))
    if any(r != 0 for r in resid_prop):
        print("  [V0b] residuo simbolico no nulo — se imprime el primero para "
              "diagnostico:")
        for n_, r in enumerate(resid_prop):
            if r != 0:
                print(f"    coef(om^{n_}): {r}")
                break
    # NOTA: en la parametrizacion covariante S no es multiplicador (el EH trae
    # Sdot, Sdd): sus EOM son de orden alto y su det tiene grado MAYOR en
    # omega, con raices espurias de parametrizacion. El control fisico: los
    # CEROS del det ADM deben ser ceros del det covariante (fondo on-shell).
    import math as _m
    # fondo numerico de la esquina sana como funcion 1D de w (todo simbolico
    # derivado con sympy y evaluado — sin formulas a mano para las terceras):
    w_ = sp.Symbol('w_bg', positive=True)
    U0w = (1 - w_**2) + 2*(w_ - 1) + (1 - w_**2)**2/2
    UXw = 2 - w_**2
    fw = 2 - 4*w_ + 2*w_**3
    rhow = sp.expand(-U0w - 2*w_**2*UXw + 2*w_)
    Hw = sp.sqrt(rhow/3)
    wdw = -3*Hw*fw/sp.diff(fw, w_)               # phidd(w)  [on-shell 1D]
    wddw = sp.diff(wdw, w_)*wdw                  # phiddd = d(wd)/dw * wd
    gw = -(U0w + Hw**2)/2                        # addot/a
    adddw = Hw*gw + sp.diff(gw, w_)*wdw          # addd en a=1
    def fondo_num(w0v):
        sb = {w_: w0v}
        return {a: 1.0, ad: float(Hw.subs(sb)), add: float(gw.subs(sb)),
                sp.Derivative(a, t, 3): float(adddw.subs(sb)),
                sp.Derivative(ph, t): float(w0v),
                sp.Derivative(ph, t, 2): float(wdw.subs(sb)),
                sp.Derivative(ph, t, 3): float(wddw.subs(sb)),
                U0f: float(U0w.subs(sb)), UXf: float(UXw.subs(sb)), UYf: 2.0,
                UXXf: 1.0, UXYf: 0.0, UYYf: 0.0,
                UXXXf: 0.0, UXXYf: 0.0, UXYYf: 0.0, UYYYf: 0.0}
    fn = fondo_num(1.2)
    kv = 0.7
    pol_adm = sp.Poly(sp.expand(det_adm.subs(fn, simultaneous=True).subs(k, kv)), om)
    pol_cov = sp.Poly(sp.expand(det_cov.subs(fn, simultaneous=True).subs(k, kv)), om)
    print(f"  grados en omega: det_ADM = {pol_adm.degree()}, "
          f"det_cov = {pol_cov.degree()} (extra = espurios de orden alto)")
    raices_adm = [complex(r) for r in pol_adm.nroots()]
    top_cov = max(abs(c) for c in pol_cov.all_coeffs())
    print(f"  ceros fisicos (det_ADM): {[f'{r:.5f}' for r in raices_adm]}")
    ok_v0 = True
    for r_ in raices_adm:
        val = complex(pol_cov.as_expr().subs(om, r_))
        rel = float(abs(val))/float(top_cov)
        print(f"    det_cov en ese cero: |val|/|coef max| = {rel:.2e}")
        if rel > 1e-8:
            ok_v0 = False
    check("V0: cada cero fisico del sistema ADM anula el det covariante "
          "(fondo on-shell w0=1.2, k=0.7): misma fisica, dos parametrizaciones",
          sp.Integer(0 if ok_v0 else 1))

    # ---- V4: limite Minkowski ----
    w0 = sp.Symbol('w0', positive=True)
    mink_map = [(a, 1), (U0f, 0)]
    cFd_mink = cFd.subs(dict(mink_map), simultaneous=True)
    cFd_mink = cFd_mink.subs({sp.Derivative(ph, t): w0, ad: 0, add: 0}, simultaneous=True)
    cFd_mink = sp.simplify(cFd_mink.subs(UYf, 2*w0*UXf))
    m1c = 2*w0**2*UXf
    print(f"  V4 Minkowski ADM (tadpole U_Y = 2wU_X): coef(Fdot^2) = {cFd_mink}")
    # blanco derivado a mano del modo real: L = (k^2/8)(S-Fdot)^2 + (m1^2/4)S^2
    # => reducido (k^2/4) m1^2/(k^2 + 2 m1^2) — la estructura BCP (7.25) con
    # denominador POSITIVO (sin polos espurios en k).
    check("V4: coef(Fdot^2)|_Mink == (k^2/4) m1^2/(k^2 + 2 m1^2), m1^2 = 2w^2 U_X",
          sp.simplify(cFd_mink - (k**2/4)*m1c/(k**2 + 2*m1c)))

    # ---- V5: tercera ruta Minkowski — Fierz-Pauli plano + patron de masas ----
    # L_EH2 forma estandar de Fierz-Pauli (firma -+++):
    #   L = -1/4 dl h_mn dl h^mn + 1/2 (d_m h^mn)(d^l h_ln)
    #       - 1/2 (d_m h^mn) d_n h + 1/4 (dh)^2
    # (la normalizacion se CALIBRA con el sector T: corresponde a sqrt(-g)R,
    # o sea 2x nuestra R/2: se usa L_FP/2). Modos REALES cos(kz) y promedio.
    print()
    print("  --- V5: tercera ruta (Fierz-Pauli plano + patron de masas) ---")
    Sf = sp.Function('S_f')(t); Ff = sp.Function('F_f')(t)
    m1s = sp.Symbol('m1sq', positive=True)
    ckz, skz = sp.cos(k*z), sp.sin(k*z)
    def promedia(e):
        e = sp.expand(e)
        e = e.subs({ckz**2: sp.Rational(1, 2), skz**2: sp.Rational(1, 2)},
                   simultaneous=True)
        return sp.expand(e.subs(ckz*skz, 0))
    eta4 = sp.diag(-1, 1, 1, 1)
    def arma_FP(hmat):
        def dh(mu, nu, lam):
            return sp.diff(hmat[mu, nu], coords4[lam]) if lam in (0, 3) else 0
        htr = sum(eta4[m, m]*hmat[m, m] for m in range(4))
        L = sp.S(0)
        for lam in range(4):
            el = eta4[lam, lam]
            for m in range(4):
                for n_ in range(4):
                    L += -sp.Rational(1, 4)*el*dh(m, n_, lam)*eta4[m, m]*eta4[n_, n_]*dh(m, n_, lam)
        div = [sum(eta4[lam, lam]*dh(lam, m, lam) for lam in range(4)) for m in range(4)]
        dtr = [sp.diff(htr, coords4[lam]) if lam in (0, 3) else 0 for lam in range(4)]
        L += sp.Rational(1, 2)*sum(eta4[m, m]*div[m]*div[m] for m in range(4))
        L += -sp.Rational(1, 2)*sum(eta4[m, m]*div[m]*dtr[m] for m in range(4))
        L += sp.Rational(1, 4)*sum(eta4[lam, lam]*dtr[lam]*dtr[lam] for lam in range(4))
        return promedia(L)
    hFP = sp.zeros(4, 4)
    hFP[0, 1] = hFP[1, 0] = Sf*ckz
    hFP[1, 3] = hFP[3, 1] = sp.diff(Ff*ckz, z)          # = -k F sin(kz)
    L_FPk = arma_FP(hFP)
    # calibracion TT: h_xy real
    hxf = sp.Function('h_xf')(t)
    hTT = sp.zeros(4, 4)
    hTT[1, 2] = hTT[2, 1] = hxf*ckz
    L_T2k = arma_FP(hTT)
    ckin_cal = sp.expand(L_T2k).coeff(sp.Derivative(hxf, t), 2)
    check("V5 calibracion: FP/2 TT da coef(hdot^2) == 1/8 == T1(a=1) x (1/2 "
          "del promedio del modo)", ckin_cal/2 - sp.Rational(1, 8))
    cgrad_cal = sp.expand(L_T2k).coeff(hxf, 2)
    check("V5 calibracion: razon (coef h^2)/(coef hdot^2) == -k^2 (c_T = 1, "
          "modo real: el signo fisico)",
          sp.simplify(cgrad_cal/ckin_cal + k**2))
    # vector FP/2 + masa del patron (7.3), TAMBIEN en modo real y promediada:
    # L_m = (1/4)[2 m1^2 h_0i h_0i] = (m1^2/2) S(t,z)^2 -> (m1^2/4) Sf^2
    L_V5 = sp.expand(L_FPk/2 + promedia(m1s/2*(Sf*ckz)**2))
    L_V5 = canon_t(L_V5, [Sf, Ff], mult=(Sf,))
    cS2 = sp.expand(L_V5).coeff(Sf, 2)
    print(f"  V5: coef(S^2) = {cS2}")
    check("V5: coef(S^2) == m1^2/4 + k^2/8 (gradiente POSITIVO del "
          "multiplicador: la constraint es Yukawa, como el frame-dragging "
          "del paper)", sp.expand(cS2 - (m1s/4 + k**2/8)))
    cK5, cM5, _ = reduce_S(L_V5, Sf, Ff)
    cK5 = sp.cancel(sp.together(cK5))
    print(f"  V5: cinetico reducido = {cK5}")
    check("V5: cinetico reducido == (k^2/4) m1^2/(k^2 + 2 m1^2) — estructura "
          "BCP (7.25) con denominador positivo (tercera ruta)",
          sp.simplify(cK5 - (k**2/4)*m1s/(k**2 + 2*m1s)))
    check("V5: potencial reducido de F == 0 en Minkowski (cero doble: el "
          "vector congelado de la campana)", sp.simplify(cM5))

    # ---- V0c: la ruta covariante en Minkowski OFF-shell vs FP + patron ----
    # blanco off-shell en w=1 (modo real, promediado):
    #   + (1/4)(U0 + 2U_X) S^2   [m1off^2 = U0+2U_X]
    #   - (1/4) U0 k^2 F^2       [-(1/4) m2off^2 h_ij h_ij, h_xz = -kF sin]
    print()
    print("  --- V0c: covariante Minkowski OFF-shell vs FP + patron (7.3) ---")
    mink_off = {a: 1, sp.Derivative(a, t): 0, sp.Derivative(a, t, 2): 0,
                sp.Derivative(ph, t): 1, sp.Derivative(ph, t, 2): 0}
    L_cov_mink = sp.expand(L2Vcovk.subs(mink_off, simultaneous=True).doit())
    L_cov_mink = sp.expand(L_cov_mink.subs(mink_off, simultaneous=True))
    L_cov_mink = canon_t(L_cov_mink, [Sck, Fck], mult=(Sck,))
    m1off = U0f + 2*UXf
    L_blanco = sp.expand(L_FPk.subs({Sf: Sck, Ff: Fck}, simultaneous=True)/2
                         + m1off/4*Sck**2 - U0f*k**2*Fck**2/4)
    L_blanco = canon_t(L_blanco, [Sck, Fck], mult=(Sck,))
    dif_mink = sp.expand(L_cov_mink - L_blanco)
    check("V0c: covariante Minkowski OFF-shell == FP/2 + patron de masas "
          "completo (m1off^2 = U0+2U_X, m2off^2 = U0)", sp.simplify(dif_mink))

    # ---- V6: arbitro externo FRW — BCP (7.24) en su parametrizacion ----
    # (7.24) [.tex fuente, seccion 7]: L2_v = M_pl^2[(a^3 k^2 / 2N)(u_i - s_i')^2
    #   + (M_1^2 / 2N^3) u_i u_i + a N k^2 M_2^2 s_i s_i],
    #   M_1^2 = 6 a^5 H^2 + m_1^2 N^3  (7.20);  para U(X,Y): M_2^2 = 0 y
    #   m_1^2 = (a/(N M_pl^2))[a^4 U + (2 a^4/N^2) U_X]   [(7.6), sin tau/y].
    # BCP parametrizan g_0i = a^2 u_i, g_ij = a^2(d_i s_j + ...) y usan
    # phi = t (w = 1), N(t) del fondo. Comparacion en N = 1, w = 1, OFF-shell
    # del fondo, con M_pl^2 = 1/2 y u = S/a^2, s = F. La lectura de su H:
    # se prueban H = adot y H = adot/a (la que cierre, se declara).
    print()
    print("  --- V6: arbitro FRW — mi ADM vs BCP (7.24), w=1, off-shell ---")
    uB = sp.Function('u_B')(t)
    L_adm_u = sp.expand(L2Vk.subs(Sk, a**2*uB, simultaneous=True).doit())
    L_adm_u = L_adm_u.subs(sp.Derivative(ph, t), 1, simultaneous=True)
    L_adm_u = canon_t(sp.expand(L_adm_u), [uB, Fk], mult=(uB,))
    Mpl2_ = sp.Rational(1, 2)
    m1B = (a/Mpl2_)*(a**4*U0f + 2*a**4*UXf)
    # el 1/2 global extra es el promedio del modo real (comun a mi L_adm_u):
    residuos_v6 = {}
    for lecturaH, nombreH in ((ad, "H=adot"), (ad/a, "H=adot/a")):
        M1B = 6*a**5*lecturaH**2 + m1B
        L_bcp = sp.Rational(1, 2)*Mpl2_*((a**3*k**2/2)*(uB - sp.Derivative(Fk, t))**2
                                         + (M1B/2)*uB**2)
        L_bcp = canon_t(sp.expand(L_bcp), [uB, Fk], mult=(uB,))
        difB = sp.expand(L_adm_u - L_bcp)
        difB = sp.expand(aplica_cadena(difB))
        # reduccion on-shell del residuo (Friedmann II y I, w=1):
        difB_on = sp.expand(difB.subs(add, addot_rule).doit())
        difB_on = sp.expand(aplica_cadena(difB_on))
        rho_w1 = rho_bg.subs(sp.Derivative(ph, t), 1)
        for _ in range(3):
            difB_on = sp.expand(difB_on.subs(ad**2, rho_w1*a**2/3))
        r_ = sp.simplify(sp.expand(difB_on))
        residuos_v6[nombreH] = r_
        print(f"    lectura {nombreH}: residuo ON-shell = {r_}")
    check("V6: mi L_V ADM == BCP (7.24) on-shell (w=1) con alguna lectura de "
          "su H (arbitro externo del sector vectorial FRW)",
          sp.Integer(0 if any(r == 0 for r in residuos_v6.values()) else 1))
    if all(r != 0 for r in residuos_v6.values()):
        print("  [V6] ningun residuo cerro en 0 — queda DECLARADO como "
              "discrepancia con (7.24) a diagnosticar (posible convencion "
              "restante de BCP o errata suya; el contenido fisico del sector "
              "— S constraint, F sin potencial en el punto protegido, sin "
              "modo omega ~ k — no depende de esto).")

# ============================================================
# SECTOR ESCALAR (S1-S7) — ADM
# ============================================================
if sector in ("TODO", "S"):
    print()
    print("=" * 72)
    print("S: sector escalar — ADM, 4 campos (alpha, beta, psi, E), k // z")
    print("=" * 72)
    al_ = sp.Function('alpha', real=True)(t, z)
    be_ = sp.Function('beta', real=True)(t, z)
    ps_ = sp.Function('psi', real=True)(t, z)
    Ee_ = sp.Function('E_s', real=True)(t, z)
    N_ = 1 + eps*al_
    NiS = [0, 0, eps*sp.diff(be_, z)]
    gamS = sp.zeros(3, 3)
    gamS[0, 0] = gamS[1, 1] = a**2*(1 + 2*eps*ps_)
    gamS[2, 2] = a**2*(1 + 2*eps*ps_ + 2*eps*sp.diff(Ee_, z, 2))
    print("  (construyendo L2 escalar ADM... tarda unos minutos)")
    L_S, _, _, _, _ = adm_L(N_, NiS, gamS)
    L2S = sp.expand(L_S.coeff(eps, 2))
    check("S1: alpha SIN derivada temporal en L2 (multiplicador, no asumido)",
          sp.Integer(1 if L2S.has(sp.Derivative(al_, t)) else 0))
    check("S1: beta SIN derivada temporal en L2 (multiplicador, no asumido)",
          sp.Integer(1 if any(L2S.has(sp.Derivative(be_, t, j)) or
                              L2S.has(sp.Derivative(be_, (t, 1), (z, j)))
                              for j in range(3)) else 0))

    # Fourier REAL (modos cos(kz), promedio — ver fourier_real)
    A0s = sp.Function('alpha_k')(t); B0s = sp.Function('beta_k')(t)
    P0s = sp.Function('psi_k')(t); E0s = sp.Function('E_k')(t)
    L2Sk = fourier_real(L2S, {al_: A0s, be_: B0s, ps_: P0s, Ee_: E0s})
    check("S: modo real promediado sin residuos (ni z ni i)",
          sp.Integer(1 if (L2Sk.has(z) or L2Sk.has(I)) else 0))

    campos_S = [A0s, B0s, P0s, E0s]
    L2Skc = canon_t(L2Sk, campos_S, mult=(A0s, B0s))

    # ---- matriz 4x4 congelada del sistema variacional (para S7 y S4/S5) ----
    # EOM variacionales hasta orden 2 (canon_t deja terminos multiplicador*qdd
    # a proposito — regla anti-ping-pong):
    def eom_var(L, q):
        e = sp.diff(L, q)
        for n_ in (1, 2):
            dLd = sp.diff(L, sp.Derivative(q, t, n_))
            if dLd != 0:
                term = dLd
                for _ in range(n_):
                    term = sp.diff(term, t)
                e += (-1)**n_*term
        return sp.expand(aplica_cadena(sp.expand(e.doit())))
    eqs = [eom_var(L2Skc, q) for q in campos_S]

    om = sp.Symbol('omega')
    ws_, Hs_, as_ = sp.symbols('w_s H_s a_s', positive=True)
    c00, c10, c01, c20, c11, c02 = sp.symbols('c00 c10 c01 c20 c11 c02', real=True)
    # U cuadratica general (la de v4): derivadas en el fondo X0=-w^2, Y0=w:
    Xb, Yb = -ws_**2, ws_
    U0q = c00 + c10*(Xb+1) + c01*(Yb-1) + c20*(Xb+1)**2/2 + c11*(Xb+1)*(Yb-1) + c02*(Yb-1)**2/2
    UXq = c10 + c20*(Xb+1) + c11*(Yb-1)
    UYq = c01 + c11*(Xb+1) + c02*(Yb-1)
    subs_U = {U0f: U0q, UXf: UXq, UYf: UYq, UXXf: c20, UXYf: c11, UYYf: c02,
              UXXXf: 0, UXXYf: 0, UXYYf: 0, UYYYf: 0}

    f_Jq = UYq - 2*ws_*UXq
    fp_Jq = sp.diff(f_Jq, ws_)
    rho_q = -U0q - 2*ws_**2*UXq + ws_*UYq
    p_q = U0q
    wdot_q = -3*Hs_*as_*0 + (-3*Hs_*f_Jq/fp_Jq)      # EOM de phi congelada
    Hdot_q = -(rho_q + p_q)/2
    addot_q = as_*(Hdot_q + Hs_**2)

    def congela(e):
        e = sp.expand(aplica_cadena(e))
        e = e.subs(subs_U, simultaneous=True)
        # derivadas del fondo, de mayor a menor. OJO: phiddd por regla de
        # cadena COMPLETA: d/dt(wdot(w,H)) = (dwdot/dw) wdot + (dwdot/dH) Hdot
        phiddd_q = sp.diff(wdot_q, ws_)*wdot_q + sp.diff(wdot_q, Hs_)*Hdot_q
        reglas = [
            (sp.Derivative(ph, t, 3), phiddd_q),
            (sp.Derivative(a, t, 2), addot_q),
            (sp.Derivative(ph, t, 2), wdot_q),
        ]
        for _ in range(5):
            e = e.subs(dict(reglas), simultaneous=True).doit()
            e = sp.expand(e)
            if not any(e.has(r[0]) for r in reglas):
                break
        e = e.subs({sp.Derivative(a, t): as_*Hs_}, simultaneous=True)
        e = e.subs({sp.Derivative(ph, t): ws_, a: as_}, simultaneous=True)
        return sp.expand(e)

    # ansatz e^{i om t} sobre las EOM: q(t) -> q0 e^{i om t}
    q0 = sp.symbols('A0 B0 P0 E0')
    def matriz_congelada(eqs_):
        M4 = sp.zeros(4, 4)
        for i, e in enumerate(eqs_):
            ee = e
            # sustituir campos por q0 e^{i om t} y dividir la fase:
            subs_f = {}
            for qq, s in zip(campos_S, q0):
                for n_ in (4, 3, 2):
                    subs_f[sp.Derivative(qq, t, n_)] = (I*om)**n_*s
                subs_f[sp.Derivative(qq, t)] = I*om*s
                subs_f[qq] = s
            ee = ee.subs(subs_f, simultaneous=True)
            ee = congela(ee)
            for jj, s in enumerate(q0):
                M4[i, jj] = sp.expand(ee.coeff(s))
            resto = sp.simplify(ee - sum(M4[i, jj]*q0[jj] for jj in range(4)))
            if resto != 0:
                print(f"  [WARN] EOM {i}: resto no lineal = {resto}")
        return M4
    M4 = matriz_congelada(eqs)
    det4 = sp.expand(M4.det())

    # ---- S4: validacion Minkowski ----
    print()
    print("--- S4: limite Minkowski (a=1, H=0, w=1, tadpoles) ---")
    mink = {as_: 1, Hs_: 0, ws_: 1, c00: 0, c01: 2*c10}
    det_m = sp.factor(sp.simplify(det4.subs(mink, simultaneous=True)))
    print("  det(Minkowski) =", det_m)
    m0_dic = -c10 + 2*c20 - 2*c11 + c02/2
    m1_dic = 2*c10
    # el det debe ser c * omega^4 * m0^2 m1^2 * k^n (cero DOBLE en omega^2)
    poly_om = sp.Poly(sp.expand(det_m), om)
    check("S4: coeficientes de omega^0..omega^3 == 0 (cero doble en omega^2)",
          sum(sp.Abs(c) for c in [poly_om.coeff_monomial(om**j) for j in range(4)]))
    c4 = sp.expand(poly_om.coeff_monomial(om**4))
    razon = sp.simplify(c4/(m0_dic*m1_dic))
    print(f"  coef(omega^4)/(m0^2 m1^2) = {razon}")
    check("S4: coef(omega^4) proporcional a m0^2 m1^2 (factor puro en k)",
          sp.Integer(0 if not razon.has(c10, c20, c11, c02) else 1))

    # ---- S2/S6: reduccion en el sistema congelado y cinetica WKB ----
    # Las filas 0,1 de M4 (variaciones de alpha, beta) son constraints: su
    # bloque (0,1)x(0,1) es ALGEBRAICO en omega (se chequea). Se eliminan
    # (A0,B0) por complemento de Schur en el sistema congelado: D2(om,k) =
    # detQcc*Schur. Cinetica WKB: K_tilde = coef(om^2) de D2/detQcc; con la
    # convencion variacional de la casa el modo sano tiene coef(om^2) > 0
    # (calibrado con el tensor: su EOM congelada da +om^2 a^3/2).
    print()
    print("--- S2/S6: reduccion congelada (constraints) y cinetica WKB ---")
    ok_alg = all(sp.expand(M4[i, j]).coeff(om, 1) == 0 and
                 sp.expand(M4[i, j]).coeff(om, 2) == 0
                 for i in (0, 1) for j in (0, 1))
    check("S2: el bloque (alpha,beta)x(alpha,beta) es algebraico en omega "
          "(constraints genuinas)", sp.Integer(0 if ok_alg else 1))
    Qcc = M4[0:2, 0:2]
    Qcv = M4[0:2, 2:4]
    Qvc = M4[2:4, 0:2]
    Qvv = M4[2:4, 2:4]
    detQcc = sp.expand(Qcc[0, 0]*Qcc[1, 1] - Qcc[0, 1]*Qcc[1, 0])
    adjQcc = sp.Matrix([[Qcc[1, 1], -Qcc[0, 1]], [-Qcc[1, 0], Qcc[0, 0]]])
    D2 = (Qvv*detQcc - Qvc*adjQcc*Qcv).applyfunc(sp.expand)
    Ktil = sp.zeros(2, 2)
    for i in range(2):
        for j in range(2):
            Ktil[i, j] = sp.expand(D2[i, j]).coeff(om, 2)
    esquina = {c00: 0, c10: 1, c01: 2, c20: 1, c11: 0, c02: 0}
    import math
    print("  autovalores de la cinetica WKB (esquina sana, atractor "
          "w = 1+(3/2)H^2):")
    for Hv in (0.05, 0.2, 0.5):
        wv = 1 + 1.5*Hv**2
        for kv in (0.3, 1.0):
            sub_n = {ws_: wv, Hs_: Hv, as_: 1, k: kv}
            dQ = complex(detQcc.subs(esquina, simultaneous=True).subs(sub_n))
            K11 = complex(Ktil[0, 0].subs(esquina, simultaneous=True).subs(sub_n))/dQ
            K22 = complex(Ktil[1, 1].subs(esquina, simultaneous=True).subs(sub_n))/dQ
            K12 = complex(Ktil[0, 1].subs(esquina, simultaneous=True).subs(sub_n))/dQ
            K21 = complex(Ktil[1, 0].subs(esquina, simultaneous=True).subs(sub_n))/dQ
            A11, A22 = K11.real, K22.real
            A12 = (K12.real + K21.real)/2
            disc = math.sqrt((A11 - A22)**2/4 + A12**2)
            ev1 = (A11 + A22)/2 + disc
            ev2 = (A11 + A22)/2 - disc
            print(f"    H={Hv:4.2f} k={kv:3.1f}: autovalores K_WKB: "
                  f"{ev1:+.4e}, {ev2:+.4e}   (>0 sano; ->0 congelado)")

    # ---- S5: dispersion del atractor desde el det 4x4 propio ----
    # BLANCO CORREGIDO (auditoria fisica de la seccion 9, 2026-07-27): la
    # formula del acta FRW omega = +-(H/sqrt2)k + 3iH quedo REFUTADA (venia de
    # truncar el det a O(H^2) ANTES del escaleo omega = Hx, omitiendo el
    # termino c1*omega con c1 = 8k^5 w H(w-1)(w^3+w^2+w-1) que sobre el
    # atractor aporta 24 k^2 H^3 omega al mismo orden). El orden dominante
    # correcto es
    #   det_dom = k^3 [ -8i om^4 - 48 H om^3 + 4i H^2(k^2+18) om^2
    #                   + 24 k^2 H^3 om ]
    # y el espectro en la ventana EFT (k <~ 1) es PURAMENTE DISIPATIVO:
    #   {0 exacto, om ~ i(k^2/3)H difusivo, om = i(3 -+ k/sqrt2)H + O(k^2)},
    # con un par que gana parte real recien en k > k* ~ 1.27.
    # METODO ANTI-BUG: sustituyo delta = (3/2)H^2 EXACTO (sin truncar el
    # polinomio), escalo om = H x y tomo el grado MINIMO en H del polinomio
    # completo: ninguna truncacion precede al escaleo. (Las correcciones
    # O(H^4) de delta solo tocan ordenes H^5+, subdominantes.)
    print()
    print("--- S5: dispersion del atractor (esquina sana) desde MI det ---")
    print("    [blanco corregido 2026-07-27: espectro disipativo; la formula")
    print("     del acta +-(H/sqrt2)k + 3iH esta refutada por la auditoria]")
    esquina = {c00: 0, c10: 1, c01: 2, c20: 1, c11: 0, c02: 0}
    det_e = sp.expand(det4.subs(esquina, simultaneous=True))
    det_e = sp.expand(det_e.subs(as_, 1))

    # S5a: el cero omega = 0 EXACTO sobre el fondo on-shell exacto (w libre,
    # 3H^2 = rho(w)): la simetria residual sobrevive en FLRW.
    rho_w = sp.expand(rho_q.subs(esquina, simultaneous=True))
    c_om0 = sp.expand(det_e.coeff(om, 0))
    c_om0_on = sp.expand(c_om0.subs(Hs_**2, rho_w/3))
    for _ in range(3):
        c_om0_on = sp.expand(c_om0_on.subs(Hs_**2, rho_w/3))
    check("S5a: coef(omega^0) del det == 0 EXACTO con 3H^2 = rho(w), w libre "
          "(un cero exacto persiste: simetria residual en FLRW)",
          sp.simplify(c_om0_on))

    xx = sp.Symbol('x')
    det_d = sp.expand(det_e.subs(ws_, 1 + sp.Rational(3, 2)*Hs_**2,
                                 simultaneous=True))
    det_sc = sp.expand(det_d.subs(om, Hs_*xx))
    pw = sp.Poly(det_sc, Hs_)
    ming = min(m[0] for m in pw.monoms())
    lead = sp.expand(det_sc.coeff(Hs_, ming))
    print(f"  escaleo om = H x SIN truncado previo: orden dominante H^{ming}")
    print(f"  polinomio dominante = {sp.factor(sp.collect(lead, xx))}")
    # blanco: det_dom / (H^4): k^3[-8i x^4 - 48 x^3 + 4i(k^2+18)x^2 + 24k^2 x]
    obj = k**3*(-8*I*xx**4 - 48*xx**3 + 4*I*(k**2 + 18)*xx**2 + 24*k**2*xx)
    lead4 = sp.expand(lead).coeff(xx, 4)
    obj4 = sp.expand(obj).coeff(xx, 4)
    dif_pol = sp.expand(lead*obj4 - obj*lead4)   # proporcionalidad exacta
    check("S5b: polinomio dominante == det_dom de la auditoria (proporcional "
          "coeficiente a coeficiente, factor global puro)", dif_pol)

    # espectro numerico: k en ventana EFT -> raices puramente imaginarias
    import math as _m
    print("  espectro (raices de lead(x)=0, x = om/H):")
    kstar = None
    for kv in (0.3, 0.5, 1.0, 1.2, 1.27, 1.3, 2.0):
        pol = sp.Poly(lead.subs(k, kv), xx)
        rr = [complex(r) for r in pol.nroots()]
        rr = sorted(rr, key=lambda r_: abs(r_))
        srr = ", ".join(f"{r_.real:+.4f}{r_.imag:+.4f}i" for r_ in rr)
        remax = max(abs(r_.real) for r_ in rr)
        print(f"    k={kv:5.2f}: {srr}   [max|Re| = {remax:.4f}]")
    rr05 = sorted([complex(r) for r in sp.Poly(lead.subs(k, 0.5), xx).nroots()],
                  key=lambda r_: abs(r_))
    ok_im = all(abs(r_.real) < 1e-9 for r_ in rr05)
    check("S5c: en k=0.5 (ventana EFT) TODAS las raices son puramente "
          "imaginarias (cero velocidad de fase: espectro disipativo)",
          sp.Integer(0 if ok_im else 1))
    dif_ap = abs(rr05[1] - complex(0, 0.5**2/3))
    check("S5d: la raiz difusiva en k=0.5 == i k^2/3 a mejor del 15%",
          sp.Integer(0 if dif_ap < 0.15*(0.5**2/3) else 1))
    rr20 = [complex(r) for r in sp.Poly(lead.subs(k, 2.0), xx).nroots()]
    tiene_re = any(abs(r_.real) > 0.1 for r_ in rr20)
    rr12 = [complex(r) for r in sp.Poly(lead.subs(k, 1.2), xx).nroots()]
    sin_re = all(abs(r_.real) < 1e-9 for r_ in rr12)
    rr13 = [complex(r) for r in sp.Poly(lead.subs(k, 1.3), xx).nroots()]
    con_re = any(abs(r_.real) > 1e-6 for r_ in rr13)
    check("S5e: el par con Re(omega) != 0 nace entre k=1.2 y k=1.3 "
          "(k* ~ 1.27 de la auditoria) y esta presente en k=2",
          sp.Integer(0 if (tiene_re and sin_re and con_re) else 1))

    # ---- S7: cross-check contra la matriz de v4 (ruta covariante) ----
    print()
    print("--- S7: razon det(mio)/det(v4) independiente de omega (numerico) ---")
    import pickle, os
    pkl = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "verificador", "v4_matriz_congelada.pkl")
    try:
        with open(pkl, "rb") as fh:
            dat = pickle.load(fh)
        Mv4 = dat["M"]
        as4, Hs4, ws4, k4, om4, c004, c104, c014, c204, c114, c024 = dat["syms"]
        det_v4 = Mv4.det()
        pts = [(1.2, 0.7, 0.9, 0.31), (1.2, 0.7, 1.7, -0.44), (1.05, 1.1, 0.6, 0.2)]
        razones = []
        for (w0, kv, omr, omi) in pts:
            rho0 = float(sp.expand(rho_q.subs(esquina, simultaneous=True)).subs(ws_, w0))
            Hv = math.sqrt(rho0/3.0)
            omv = omr + 1j*omi
            dm = complex(det4.subs(esquina, simultaneous=True).subs(
                {as_: 1, ws_: w0, Hs_: Hv, k: kv, om: omv}))
            dv = complex(det_v4.subs(
                {as4: 1, ws4: w0, Hs4: Hv, k4: kv, om4: omv,
                 c004: 0, c104: 1, c014: 2, c204: 1, c114: 0, c024: 0}))
            razones.append(dm/dv)
            print(f"    w0={w0}, k={kv}, om={omv}: det_mio/det_v4 = {dm/dv:.6g}")
        iguales = abs(razones[0]/razones[1] - 1) < 1e-6
        check("S7: la razon es la misma en dos puntos con igual fondo y k, "
              "distinto omega (misma fisica que v4)",
              sp.Integer(0 if iguales else 1))
    except FileNotFoundError:
        print("  [WARN] no encontre v4_matriz_congelada.pkl — corre antes "
              "verificador/v4_escalar_frw.py")

print()
print("VEREDICTO:", "TODO PASS" if ok else "HAY FALLOS — revisar arriba")
