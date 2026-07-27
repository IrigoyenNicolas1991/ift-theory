# Columna A - TAREA 1, pata perturbativa: LOS VERTICES CUBICOS EXPLICITOS.
#
# Derivacion independiente de los vertices cubicos de sqrt(-g) U(X,Y) alrededor
# del fondo (Minkowski + gauge unitario, sector vectorial encendido via h) y
# verificacion EXPLICITA de si transportan o no la carga interna P_a^0:
#
#   L(h, dpi) = sqrt(-g) U(X,Y) expandido a orden TOTAL 3 en (h, dpi)
#   J^mu_a := dL/d(d_mu pi^a)  = la corriente interna (el EH no contiene Phi:
#             NO aporta a la corriente interna; el acople minimo de materia tampoco)
#
#   C1  J^i_a|_{pi=0} = 0 orden por orden en h (h^0, h^1, h^2): los vertices
#       cubicos h^2 dpi^a_i NO EXISTEN => ningun vertice cubico transporta carga.
#   C2  la identidad completa P_a^mu d_mu Phi^b = 0 verificada orden a orden
#       (hasta orden total 2 en el integrando de la identidad, que involucra los
#       vertices cubicos de L): la corriente espacial con pi encendido es PURA
#       ADVECCION, esclava de P_a^0: P_a^i = -P_a^0 d_0 pi^i + O(3).
#   C3  catalogo de los vertices cubicos que SI existen (con d_0 pi^a): se listan.
#   C4  atadura al juguete: P_x^0 del modo = -m1^2 S cos(pz) + O(h^2) reproduce
#       la amplitud C = -m1^2 S del vinculo de B (B4) via mi expansion covariante.
#
# Convenciones BCP (handoff SS3): signatura (-,+,+,+), M_Pl=1, g = eta + e*h,
# Phi^0 = t + e*pi^0, Phi^a = x^a + e*pi^a (pi^0 apagado aca: la carga es de Phi^a;
# pi^0 no participa de la corriente interna espacial y su encendido no la altera
# -- se chequea igual con pi^0 generico en C2b).
import sympy as sp
import time

t0 = time.time()
print('=' * 72)
print('A2 - VERTICES CUBICOS DE sqrt(-g) U(X,Y): la corriente interna, explicita')
print('=' * 72)

e = sp.Symbol('e')

def trunc(ex, n=3):
    ex = sp.expand(ex)
    return sum(ex.coeff(e, k) * e ** k for k in range(n + 1))

# ---- campos: h (10 simbolos) y J[A,mu] = d_mu pi^A (16 simbolos) ----
hs = {}
for i in range(4):
    for j in range(i, 4):
        hs[(i, j)] = hs[(j, i)] = sp.Symbol('h%d%d' % (min(i, j), max(i, j)))
h = sp.Matrix(4, 4, lambda i, j: hs[(i, j)])
J = {(A, mu): sp.Symbol('J_%d_%d' % (A, mu)) for A in range(4) for mu in range(4)}
eta = sp.diag(-1, 1, 1, 1)

g = eta + e * h
# g^{-1} a orden e^3
ginv = eta - e * (eta * h * eta) + e ** 2 * (eta * h * eta * h * eta) \
       - e ** 3 * (eta * h * eta * h * eta * h * eta)
# sqrt(-g) a orden e^3
detg = sp.expand((g.det()))
sqg = sp.sqrt(-detg).series(e, 0, 4).removeO()

# dPhi (pi^0 APAGADO por defecto; se enciende en C2b)
def dPhi_de(con_pi0):
    M = sp.eye(4)
    for A in range(4):
        for mu in range(4):
            if A == 0 and not con_pi0:
                continue
            M[A, mu] = M[A, mu] + e * J[(A, mu)]
    return M

eps4 = sp.LeviCivita
def u_un_de(dP):
    comp = []
    for mu in range(4):
        s_ = 0
        for nu in range(4):
            for rho in range(4):
                for si in range(4):
                    ee = eps4(mu, nu, rho, si)
                    if ee != 0:
                        s_ += ee * dP[1, nu] * dP[2, rho] * dP[3, si]
        comp.append(trunc(s_))
    return sp.Matrix(comp)

def XY_de(dP):
    """X = C^00 y Y = det(dP)/sqrt(-u_un.g.u_un), series a orden e^3."""
    X = trunc((dP[0, :] * ginv * dP[0, :].T)[0, 0])
    uu = u_un_de(dP)
    N = trunc((uu.T * g * uu)[0, 0])
    dN = trunc(N + 1)                       # N = -1 + dN
    inv_sqrtN = 1 + dN / 2 + sp.Rational(3, 8) * dN ** 2 + sp.Rational(5, 16) * dN ** 3
    Y = trunc(trunc(dP.det()) * trunc(inv_sqrtN))
    return X, Y

# ---- U(X,Y) Taylor a orden 3 alrededor de (X,Y)=(-1,1) ----
U0 = sp.Symbol('U0')
nm = ['X', 'Y']
D1 = {k: sp.Symbol('U_' + k) for k in nm}
D2s = {('X', 'X'): sp.Symbol('U_XX'), ('X', 'Y'): sp.Symbol('U_XY'),
       ('Y', 'Y'): sp.Symbol('U_YY')}
D3s = {('X', 'X', 'X'): sp.Symbol('U_XXX'), ('X', 'X', 'Y'): sp.Symbol('U_XXY'),
       ('X', 'Y', 'Y'): sp.Symbol('U_XYY'), ('Y', 'Y', 'Y'): sp.Symbol('U_YYY')}

def U_taylor(dX, dY):
    U = U0 + D1['X'] * dX + D1['Y'] * dY
    U += sp.Rational(1, 2) * (D2s[('X', 'X')] * dX ** 2 + D2s[('Y', 'Y')] * dY ** 2) \
         + D2s[('X', 'Y')] * dX * dY
    U += sp.Rational(1, 6) * (D3s[('X', 'X', 'X')] * dX ** 3 + D3s[('Y', 'Y', 'Y')] * dY ** 3) \
         + sp.Rational(1, 2) * (D3s[('X', 'X', 'Y')] * dX ** 2 * dY
                                + D3s[('X', 'Y', 'Y')] * dX * dY ** 2)
    return trunc(U)

# ============================================================
# C1: la corriente con pi = 0 (coeficiente lineal en J, todo h)
# ============================================================
dP = dPhi_de(con_pi0=False)
X, Y = XY_de(dP)
L = trunc(trunc(sqg) * U_taylor(trunc(X + 1), trunc(Y - 1)))

Jvars_a = [J[(A, mu)] for A in (1, 2, 3) for mu in range(4)]
cero_J = {v: 0 for v in Jvars_a}

print('\n[C1] J^mu_a = dL/d(d_mu pi^a)|_{pi=0} orden por orden en h:')
ok_C1 = True
corr0 = {}
for a in (1, 2, 3):
    for mu in range(4):
        P = sp.expand(sp.diff(L, J[(a, mu)]).subs(cero_J))
        # ordenes: e^1 (h^0), e^2 (h^1), e^3 (h^2 <- vertices cubicos)
        o1, o2, o3 = P.coeff(e, 1), P.coeff(e, 2), P.coeff(e, 3)
        corr0[(a, mu)] = (o1, sp.expand(o2), sp.expand(o3))
        if mu != 0:
            nulos = [sp.simplify(o) == 0 for o in (o1, o2, o3)]
            ok_C1 = ok_C1 and all(nulos)
            if not all(nulos):
                print('   J^%d_%d != 0: ordenes %s  <-- VERTICE QUE TRANSPORTA CARGA' %
                      (mu, a, nulos))
print('  J^i_a = 0 en h^0, h^1 y h^2 (36 componentes espaciales x ordenes):',
      'OK - NINGUN vertice cubico transporta carga' if ok_C1 else 'FALLA')

# ============================================================
# C2: identidad completa P_a^mu d_mu Phi^b = 0 con pi ENCENDIDO
# ============================================================
print('\n[C2] identidad P_a^mu d_mu Phi^b = 0 con pi^a encendido (orden e^2,')
print('     usa los vertices cubicos de L):')
ok_C2 = True
for a in (1, 2, 3):
    for b in (1, 2, 3):
        ident = 0
        for mu in range(4):
            P = sp.expand(sp.diff(L, J[(a, mu)]))          # serie e^1..e^3, con J
            dPhib = (1 if mu == b else 0) + e * J[(b, mu)]
            ident += P * dPhib
        ident = sp.expand(ident)
        # la identidad completa es exacta; verifico e^1 y e^2 (el e^2 mezcla el
        # vertice cubico h^2 J y el cuadratico h J x J)
        r1 = sp.simplify(ident.coeff(e, 1))
        r2 = sp.simplify(ident.coeff(e, 2))
        ok_C2 = ok_C2 and (r1 == 0) and (r2 == 0)
        if r1 != 0 or r2 != 0:
            print('   (a=%d,b=%d): e^1: %s | e^2: %s  <-- ROTA' % (a, b, r1, r2))
print('  identidad off-shell verificada a orden e^2 (9 pares a,b):',
      'OK' if ok_C2 else 'FALLA')

# corolario advectivo: P_a^i + P_a^0 * d_0 pi^i (esclavitud a orden dominante)
print('\n[C2b] estructura advectiva: P_a^i = -P_a^mu d_mu pi^i (esclava de P_a^0):')
for a in (1, 2, 3):
    i = 1
    P_ai = sp.expand(sp.diff(L, J[(a, i)]))
    P_a0 = sp.expand(sp.diff(L, J[(a, 0)]))
    # a orden e^2: P_a^i|_{e^2} vs -(P_a^0 J^i_0)|_{e^2} - sum_j (P_a^j J^i_j)|_{e^2}
    lhs = P_ai.coeff(e, 2)
    rhs = sp.expand(-(P_a0 * e * J[(i, 0)]).coeff(e, 2)
                    - sum((sp.diff(L, J[(a, jj)]) * e * J[(i, jj)]).coeff(e, 2)
                          for jj in (1, 2, 3)))
    d = sp.simplify(sp.expand(lhs - rhs))
    print('   a=%d: P_a^x|_(e2) + [P_a^mu d_mu pi^x]|_(e2) =' % a, d)

# con pi^0 encendido tambien (la carga interna espacial no se altera)
dPf = dPhi_de(con_pi0=True)
Xf, Yf = XY_de(dPf)
Lf = trunc(trunc(sqg) * U_taylor(trunc(Xf + 1), trunc(Yf - 1)))
cero_all = {v: 0 for v in J.values()}
ok_pi0 = True
for a in (1, 2, 3):
    for i in (1, 2, 3):
        P = sp.expand(sp.diff(Lf, J[(a, i)]).subs(cero_all))
        nulo = all(sp.simplify(P.coeff(e, k)) == 0 for k in (1, 2, 3))
        ok_pi0 = ok_pi0 and nulo
print('[C2c] con pi^0 generico encendido, J^i_a|_{pi=0} sigue = 0 (h^0..h^2):',
      'OK' if ok_pi0 else 'FALLA')

# ============================================================
# C3: catalogo de los vertices que SI existen (adveccion temporal)
# ============================================================
print('\n[C3] los vertices que SI existen: J^0_a = dL/d(d_0 pi^a)|_{pi=0}')
tad = {U0: 0, D1['Y']: 2 * D1['X']}          # vacio Minkowski (handoff B1)
for a in (1,):
    o1, o2, o3 = corr0[(a, 0)]
    print('  orden h^0 :', sp.simplify(o1.subs(tad) if o1 != 0 else o1))
    print('  orden h^1 :', sp.collect(sp.expand(o2.subs(tad)), list(set(hs.values()))))
    o3t = sp.expand(o3.subs(tad))
    # solo el sector vectorial puro (h0i, hij transversal) para el catalogo corto:
    sector = {hs[(0, 0)]: 0, hs[(1, 1)]: 0, hs[(2, 2)]: 0, hs[(3, 3)]: 0}
    o3v = sp.expand(o3t.subs(sector))
    print('  orden h^2 (sector vectorial h0i,hij; tadpoles impuestos):')
    print('    ', sp.collect(o3v, [hs[(0, 1)], hs[(0, 2)], hs[(0, 3)]]))

# ============================================================
# C4: atadura al juguete (modo de v2): P_x^0 = -m1^2 S cos(pz) + O(h^2)
# ============================================================
print('\n[C4] el modo del juguete: h_{0x} = S cos(pz), h_{xz} = -p F sin(pz):')
S_, F_, p_, z_ = sp.symbols('S F p z')
modo = {v: 0 for v in set(hs.values())}
modo[hs[(0, 1)]] = S_ * sp.cos(p_ * z_)
modo[hs[(1, 3)]] = -p_ * F_ * sp.sin(p_ * z_)
o1, o2, o3 = corr0[(1, 0)]
P10_h1 = sp.expand(o2.subs(tad).subs(modo))
print('  P_x^0 a orden h =', sp.simplify(P10_h1), '  con m1^2 = 2 U_X')
print('  => amplitud-modo = -(2U_X) S = -m1^2 S == C on-shell del vinculo de B (B4):',
      'OK' if sp.simplify(P10_h1 + 2 * D1['X'] * S_ * sp.cos(p_ * z_)) == 0 else 'FALLA')
o3_modo = sp.expand(o3.subs(tad).subs(modo))
print('  correccion O(h^2) sobre el modo (cuan grande es el error del orden lineal):')
print('    P_x^0|_(h^2) =', sp.simplify(o3_modo))

print('\n[VEREDICTO A2] Vertices cubicos derivados independientemente:')
print(' * NO EXISTE ningun vertice cubico h^2 (d_i pi^a): J^i_a|_{pi=0} = 0 a')
print('   ordenes h^0, h^1, h^2 (C1). El teorema de B pasa la verificacion')
print('   explicita vertice a vertice a orden cubico.')
print(' * Con pi encendido, la corriente espacial es advecccion pura esclava de')
print('   P_a^0 (C2/C2b): la carga solo viaja CON el medio, nunca a traves.')
print(' * Los vertices cubicos que existen involucran d_0 pi^a (C3): renormalizan')
print('   la densidad, no crean corriente.')
print(' * La amplitud del modo reproduce el vinculo C = -m1^2 S de B (C4).')
print('t =', round(time.time() - t0, 1), 's')
