# Verificador adversarial: pipeline propio EH cuadratico (independiente del derivador).
# Convenciones: signatura (-,+,+,+), g = eta + e*H, Ricci tipo MTW (R_bd = dGam^a_bd,a - dGam^a_ba,d + GG - GG).
import sympy as sp

t, z = sp.symbols('t z', real=True)
p = sp.symbols('p', positive=True)
e = sp.symbols('e')
Mp2 = sp.symbols('Mp2', positive=True)

def _d(f, mu):
    if mu == 0: return sp.diff(f, t)
    if mu == 3: return sp.diff(f, z)
    return sp.S(0)

def _tr2(ex):
    ex = sp.expand(ex)
    return ex.coeff(e, 0) + e*ex.coeff(e, 1) + e**2*ex.coeff(e, 2)

def build_L(H):
    """Devuelve (L1, L2): coeficientes de e^1 y e^2 de sqrt(-g)R (sin Mp2)."""
    eta = sp.diag(-1, 1, 1, 1)
    G = eta + e*H
    Ginv = eta - e*(eta*H*eta) + e**2*(eta*H*eta*H*eta)
    Gam = [[[sp.S(0)]*4 for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c in range(b, 4):
                s = sp.S(0)
                for dd in range(4):
                    s += Ginv[a, dd]*(_d(G[dd, b], c) + _d(G[dd, c], b) - _d(G[b, c], dd))
                v = _tr2(s/2)
                Gam[a][b][c] = v
                Gam[a][c][b] = v
    Ric = sp.zeros(4, 4)
    for b in range(4):
        for dd in range(b, 4):
            s = sp.S(0)
            for a in range(4):
                s += _d(Gam[a][b][dd], a) - _d(Gam[a][b][a], dd)
                for c in range(4):
                    s += Gam[a][a][c]*Gam[c][b][dd] - Gam[a][dd][c]*Gam[c][b][a]
            v = _tr2(s)
            Ric[b, dd] = v
            Ric[dd, b] = v
    R = sp.S(0)
    for b in range(4):
        for dd in range(4):
            R += Ginv[b, dd]*Ric[b, dd]
    R = _tr2(R)
    detG = sp.expand(G.det())
    sqrtg = sp.sqrt(-detG).series(e, 0, 3).removeO()
    L = _tr2(sp.expand(sqrtg*R))
    return sp.expand(L.coeff(e, 1)), sp.expand(L.coeff(e, 2))

def zavg(ex):
    return sp.expand(sp.simplify((p/(2*sp.pi))*sp.integrate(sp.expand(ex), (z, 0, 2*sp.pi/p))))

def EL(L, f):
    """Euler-Lagrange para L(f, f', f'') mecanica 1D en t."""
    r = sp.diff(L, f)
    d1 = sp.Derivative(f, t)
    d2 = sp.Derivative(f, (t, 2))
    r -= sp.diff(sp.diff(L, d1), t)
    r += sp.diff(sp.diff(L, d2), t, 2)
    return sp.expand(r)
