"""
Libreria: expansion cuadratica de sqrt(-g) R alrededor de Minkowski
sobre un ansatz h_{mu nu}(t,z) (modo de Fourier con p a lo largo de z).

Convenciones (BCP 1603.02956 / MTW):
  signatura (-,+,+,+),  g_{mu nu} = eta_{mu nu} + h_{mu nu}
  Gamma^a_{bc} = (1/2) g^{ad} (d_b g_{dc} + d_c g_{db} - d_d g_{bc})
  R_{bc} = d_a Gamma^a_{bc} - d_c Gamma^a_{ab}
           + Gamma^a_{ad} Gamma^d_{bc} - Gamma^a_{cd} Gamma^d_{ab}
  R = g^{bc} R_{bc}
Con estas convenciones sqrt(-g) R da termino cinetico SANO (+) para el
graviton TT (se verifica en run_tensor.py, no se asume).
"""
import sympy as sp

t, z = sp.symbols('t z', real=True)
x, y = sp.symbols('x y', real=True)
p = sp.symbols('p', positive=True)
eps = sp.Symbol('epsilon')
X = [t, x, y, z]
eta = sp.diag(-1, 1, 1, 1)


def trunc2(e):
    """Trunca un polinomio en eps a orden eps^2."""
    e = sp.expand(e)
    return sum(e.coeff(eps, k) * eps**k for k in range(3))


def L12_of_ansatz(H):
    """H: Matrix 4x4 simetrica, entradas funciones de (t,z).
    g = eta + eps*H. Devuelve (L1, L2): coeficientes de eps^1 y eps^2
    de la densidad sqrt(-g) R (sin promediar en z)."""
    g = eta + eps * H
    etainv = eta  # diagonal +-1: su propia inversa
    ginv = (etainv - eps * etainv * H * etainv
            + eps**2 * etainv * H * etainv * H * etainv)
    # Christoffel a O(eps^2)
    Gam = [[[sp.Integer(0)] * 4 for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c in range(b, 4):
                expr = sp.Integer(0)
                for d in range(4):
                    expr += ginv[a, d] * (sp.diff(g[d, c], X[b])
                                          + sp.diff(g[d, b], X[c])
                                          - sp.diff(g[b, c], X[d]))
                expr = trunc2(expr / 2)
                Gam[a][b][c] = expr
                Gam[a][c][b] = expr
    # Ricci
    Ric = sp.zeros(4, 4)
    for b in range(4):
        for c in range(b, 4):
            expr = sp.Integer(0)
            for a in range(4):
                expr += sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                for d in range(4):
                    expr += Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
            e2 = trunc2(expr)
            Ric[b, c] = e2
            Ric[c, b] = e2
    R = sp.Integer(0)
    for b in range(4):
        for c in range(4):
            R += ginv[b, c] * Ric[b, c]
    R = trunc2(R)
    detg = trunc2(g.det())
    sq = sp.series(sp.sqrt(-detg), eps, 0, 3).removeO()
    L = trunc2(sp.expand(sq * R))
    return sp.expand(L.coeff(eps, 1)), sp.expand(L.coeff(eps, 2))


def zavg(expr):
    """Promedio sobre un periodo en z: cos^2, sin^2 -> 1/2; cos*sin y
    potencias impares -> 0. Valido porque la densidad cuadratica tiene a lo
    sumo dos factores trigonometricos por termino (uno por campo)."""
    half = sp.Rational(1, 2)
    c_, s_ = sp.cos(p * z), sp.sin(p * z)
    e = sp.expand(expr).subs({c_**2: half, s_**2: half})
    e = sp.expand(e)
    kept = [T for T in sp.Add.make_args(e) if not (T.has(c_) or T.has(s_))]
    return sp.Add(*kept)


def check_zavg(expr, seed=7):
    """Control: compara zavg contra la integral explicita en z con las
    funciones de t reemplazadas por racionales aleatorios."""
    import random
    random.seed(seed)
    e = sp.expand(expr)
    dsubs = {a: sp.Rational(random.randint(1, 9), random.randint(1, 9))
             for a in e.atoms(sp.Derivative)}
    fsubs = {a: sp.Rational(random.randint(1, 9), random.randint(1, 9))
             for a in e.atoms(sp.Function) if a.args == (t,)}
    pv = sp.Rational(3, 2)
    e_num = e.subs(dsubs).subs(fsubs).subs(p, pv)
    direct = sp.integrate(e_num, (z, 0, 2 * sp.pi / pv)) * pv / (2 * sp.pi)
    via = zavg(e).subs(dsubs).subs(fsubs).subs(p, pv)
    return sp.simplify(direct - via)


def EL(L, f):
    """Ecuacion de Euler-Lagrange de L respecto de f(t), hasta 4a derivada."""
    e = sp.diff(L, f)
    for k in range(1, 5):
        d = sp.Derivative(f, (t, k))
        pl = sp.diff(L, d)
        if pl != 0:
            e += (-1)**k * sp.diff(pl, (t, k))
    return sp.expand(e)
