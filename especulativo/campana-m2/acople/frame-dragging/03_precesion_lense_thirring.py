# -*- coding: utf-8 -*-
"""
COLUMNA B - paso 3: precesion de Lense-Thirring con h_0 = f(r) (x x J).
  RG:      f(r) = 2G/r^3
  medio:   f(r) = 2Gt (1+mu r) e^(-mu r)/r^3 * FF(mu R)
(a) fuerza gravitomagnetica desde la geodesica (sin factores GEM a mano)
(b) B = rot h_0 para f generica
(c) promedio orbital (orbita circular, inclinacion arbitraria) => Omega_nodo = f(a) J
(d) giroscopo (GP-B, orbita polar): <Omega_gyro> = -(1/2)<B>
(e) chequeos RG numericos: LAGEOS 30.7 mas/yr, GP-B 39 mas/yr.
"""
import sympy as sp

x, y, z, t = sp.symbols('x y z t', real=True)
v1, v2, v3 = sp.symbols('v1 v2 v3', real=True)
eps = sp.Symbol('epsilon')

# ---------- (a) geodesica => a = v x (rot h0), con g00=-1, gij=delta ----------
h1, h2, h3 = [sp.Function(f'h{i}')(x, y, z) for i in (1, 2, 3)]
gmat = sp.Matrix([[-1, eps * h1, eps * h2, eps * h3],
                  [eps * h1, 1, 0, 0],
                  [eps * h2, 0, 1, 0],
                  [eps * h3, 0, 0, 1]])
eta = sp.diag(-1, 1, 1, 1)
Hm = sp.Matrix(4, 4, lambda i_, j_: sp.expand((gmat[i_, j_] - eta[i_, j_]) / eps))
ginv = eta - eps * eta * Hm * eta + eps**2 * eta * Hm * eta * Hm * eta  # O(eps^2)
X4 = [t, x, y, z]
v = [1, v1, v2, v3]     # dx^mu/dt, v pequeño
acc = []
for i in range(1, 4):
    a_i = 0
    for b_ in range(4):
        for c_ in range(4):
            Gam = 0
            for d_ in range(4):
                Gam += ginv[i, d_] * (sp.diff(gmat[d_, c_], X4[b_])
                                      + sp.diff(gmat[d_, b_], X4[c_])
                                      - sp.diff(gmat[b_, c_], X4[d_])) / 2
            a_i -= Gam * v[b_] * v[c_]
    # orden lineal en h (eps) y lineal en v:
    a_i = sp.expand(a_i).coeff(eps, 1)
    a_i = sum(sp.expand(a_i).coeff(vv, 1) * vv for vv in (v1, v2, v3))
    acc.append(sp.expand(a_i))
hvec = sp.Matrix([h1, h2, h3])
vvec = sp.Matrix([v1, v2, v3])
rot = sp.Matrix([sp.diff(h3, y) - sp.diff(h2, z),
                 sp.diff(h1, z) - sp.diff(h3, x),
                 sp.diff(h2, x) - sp.diff(h1, y)])
vxB = vvec.cross(rot)
assert all(sp.simplify(acc[i] - vxB[i]) == 0 for i in range(3))
print("(a) geodesica estacionaria: a_i = [v x B]_i con B = rot h_0  (orden v^1, h^1)  OK")

# ---------- (b) B para h_0 = f(r) (x x J) ----------
r = sp.sqrt(x**2 + y**2 + z**2)
rr = sp.Symbol('r', positive=True)
f = sp.Function('f')
Jx, Jy, Jz = sp.symbols('J_x J_y J_z', real=True)
Jv = sp.Matrix([Jx, Jy, Jz])
xv = sp.Matrix([x, y, z])
h0 = f(r) * xv.cross(Jv)
Bv = sp.Matrix([sp.diff(h0[2], y) - sp.diff(h0[1], z),
                sp.diff(h0[0], z) - sp.diff(h0[2], x),
                sp.diff(h0[1], x) - sp.diff(h0[0], y)])
P = sp.Function('P')(rr)   # B = P J + Q (J.rhat) rhat
fp = sp.Derivative(f(rr), rr)
P_expr = -(2 * f(rr) + rr * fp)
Q_expr = rr * fp
rhat = xv / r
Jdotr = (Jv.T * rhat)[0]
B_pred = P_expr.subs(rr, r).doit() * Jv + Q_expr.subs(rr, r).doit() * Jdotr * rhat
assert all(sp.simplify(sp.together(Bv[i] - B_pred[i])) == 0 for i in range(3))
print("(b) B = -(2f + r f') J + (r f') (J.rhat) rhat   OK")

# ---------- (c) promedio orbital: orbita circular inclinada ----------
psi, inc, a_ = sp.symbols('psi iota a', real=True, positive=True)
e1 = sp.Matrix([1, 0, 0])
e2 = sp.Matrix([0, sp.cos(inc), sp.sin(inc)])
nhat = e1.cross(e2)
worb = sp.Symbol('omega_orb', positive=True)
pos = a_ * (sp.cos(psi) * e1 + sp.sin(psi) * e2)
vel = a_ * worb * (-sp.sin(psi) * e1 + sp.cos(psi) * e2)
Pa, Qa = sp.symbols('P_a Q_a')   # P(a), Q(a) sobre la orbita (r=a constante)
B_orb = Pa * Jv + Qa * ((Jv.T * pos)[0] / a_**2) * pos
acc_orb = vel.cross(B_orb)
Nvec = pos.cross(acc_orb)                      # torque por unidad de masa
Navg = sp.Matrix([sp.integrate(Nvec[i], (psi, 0, 2 * sp.pi)) / (2 * sp.pi)
                  for i in range(3)])
Navg = sp.simplify(Navg)
# dL/dt = <N>, L = a^2 worb nhat  =>  dnhat/dt = <N>/(a^2 worb) = Omega x nhat
Om = sp.Symbol('Om')
lhs = sp.simplify(Navg / (a_**2 * worb))
# candidato Omega = -(Pa+Qa)/2 * J:
Om_cand = -(Pa + Qa) / 2 * Jv
assert all(sp.simplify(lhs[i] - Om_cand.cross(nhat)[i]) == 0 for i in range(3))
print("(c) <dn/dt> = Omega x n  con  Omega = -(P(a)+Q(a))/2 J = f(a) J   (exacto,")
Om_f = sp.simplify((-(P_expr + Q_expr) / 2).subs(rr, a_))
print("    para f generica: -(P+Q)/2 =", Om_f, "; independiente de la inclinacion)  OK")

# ---------- (d) sustituciones ----------
G, Gt, mu, J0 = sp.symbols('G Gtilde mu J', positive=True)
f_GR = 2 * G / rr**3
f_Yu = 2 * Gt * (1 + mu * rr) * sp.exp(-mu * rr) / rr**3
Om_GR = sp.simplify(Om_f.subs(f(a_), f_GR.subs(rr, a_)))
Om_Yu = Om_f.replace(f(a_), f_Yu.subs(rr, a_))
print("(d) nodo RG:    Omega = f_GR(a) J =", f_GR.subs(rr, a_), "* J   ( = 2GJ/a^3 )")
S_node = sp.simplify(f_Yu.subs(rr, a_) / f_GR.subs(rr, a_) * G / Gt)
print("    apantallamiento nodal S_node(x=mu a) =", sp.simplify(S_node), "* (Gt/G)")
xx = sp.Symbol('x', positive=True)
S_node_x = sp.simplify(S_node.subs(mu, xx / a_))
print("    S_node(x) =", S_node_x, " ; serie:", sp.series(S_node_x, xx, 0, 4))

# giroscopo GP-B: orbita polar (inclinacion pi/2 respecto de J=J zhat)
# <B> sobre la orbita polar: <(J.rhat) rhat> = J/2 zhat (el circulo contiene a J)
Pfun = P_expr
Qfun = Q_expr
B_avg_polar = (Pfun + Qfun / 2).subs(rr, a_)   # coeficiente de J zhat
Om_gyro = -B_avg_polar / 2                      # Omega_gyro = -(1/2) <B>
Om_gyro_GR = sp.simplify(Om_gyro.replace(f(a_), f_GR.subs(rr, a_)).doit())
Om_gyro_Yu = sp.simplify(Om_gyro.replace(f(a_), f_Yu.subs(rr, a_)).doit())
print("(d) giroscopo polar RG: <Omega> =", Om_gyro_GR, "* J   ( = GJ/(2a^3) )")
S_gyro = sp.simplify(Om_gyro_Yu / Om_gyro_GR * G / Gt)
S_gyro_x = sp.simplify(S_gyro.subs(mu, xx / a_))
print("    apantallamiento GP-B S_gyro(x) =", S_gyro_x, "* (Gt/G)")
print("    serie:", sp.series(S_gyro_x, xx, 0, 4))

# ---------- (e) chequeos RG numericos ----------
import math
Gn = 6.674e-11; c_l = 2.998e8; J_E = 5.86e33
mas_yr = lambda om: om * 3.156e7 / (4.8481e-9)   # rad/s -> mas/yr
a_LAG = 1.227e7; a_GPB = 7.027e6
Om_LAG = 2 * Gn * J_E / (c_l**2 * a_LAG**3)
Om_GPB = Gn * J_E / (2 * c_l**2 * a_GPB**3)
print(f"\n(e) RG: nodo LAGEOS = {mas_yr(Om_LAG):.1f} mas/yr  (literatura: 30.7)")
print(f"    RG: GP-B frame-dragging = {mas_yr(Om_GPB):.1f} mas/yr  (literatura: 39.2)")
