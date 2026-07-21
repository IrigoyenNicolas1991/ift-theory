# [Panel adversarial 2026-07-21: script del REFUTADOR CIEGO — agente sin acceso a los
#  demas scripts de esta carpeta; solo recibio las convenciones BCP y la disputa de
#  pesos. Veredicto: CONFIRMA los pesos del handoff. Ver VERIFICACION-BCP-2026-07-21.md]
# Rederivacion independiente de los pesos de U_tau_n y U_y_n en m1^2 y m2^2
# Convenciones BCP 1603.02956, gauge unitario, Minkowski, M_Pl=1.
# Metodo: g = eta + eps*h con UNA componente de h por vez; inversa EXACTA de g
# expandida en serie a O(eps^2); U lineal en (tau_n - 3) e y_n con coeficientes
# simbolicos = derivadas primeras U_tau_n, U_y_n. Cross-check con la inversa
# perturbativa eta - eta h eta + eta h eta h eta.
import sympy as sp

eps = sp.Symbol('e')
Utau = {n: sp.Symbol(f'Ut{n}') for n in (1, 2, 3)}
Uy = {n: sp.Symbol(f'Uy{n}') for n in (0, 1, 2, 3)}
U0 = sp.Symbol('U0')  # valor de fondo de U (para ver la contaminacion del volumen)

eta = sp.diag(-1, 1, 1, 1)

def coef_eps2(hpos, exact=True):
    """Coeficiente de eps^2 en sqrt(-g)*U con h_{hpos}=eps (simetrizado)."""
    i, j = hpos
    H = sp.zeros(4, 4)
    H[i, j] = 1
    H[j, i] = 1
    g = eta + eps * H
    if exact:
        ginv = g.inv()
        ginv = ginv.applyfunc(lambda ex: sp.series(sp.cancel(ex), eps, 0, 3).removeO())
    else:
        ginv = eta - eps * (eta * H * eta) + eps**2 * (eta * H * eta * H * eta)
    # Operadores en gauge unitario: C^{AB} = g^{AB}
    B = ginv[1:, 1:]                     # bloque espacial 3x3, fondo delta
    V = sp.Matrix([ginv[0, 1], ginv[0, 2], ginv[0, 3]])  # V^a = C^{0a}
    Z = V * V.T                          # Z^{ab} = V^a V^b
    Bp = {0: sp.eye(3), 1: B, 2: B * B, 3: B * B * B}
    tau = {n: sp.trace(Bp[n]) for n in (1, 2, 3)}        # fondo 3
    y = {n: sp.trace(Bp[n] * Z) for n in (0, 1, 2, 3)}   # fondo 0
    U = (U0
         + sum(Utau[n] * (tau[n] - 3) for n in (1, 2, 3))
         + sum(Uy[n] * y[n] for n in (0, 1, 2, 3)))
    sqrtg = sp.series(sp.sqrt(sp.cancel(-g.det())), eps, 0, 3).removeO()
    L = sp.expand(sqrtg * sp.expand(U))
    return sp.expand(L.coeff(eps, 2))

print("=== INVERSA EXACTA (serie a O(eps^2)) ===")
c01 = coef_eps2((0, 1))
c12 = coef_eps2((1, 2))
print("coef de h01^2 en sqrt(-g)U :", c01)
print("m1^2 = 2*coef  ->", sp.expand(2 * c01))
print("coef de h12^2 en sqrt(-g)U :", c12)
print("m2^2 = -2*coef ->", sp.expand(-2 * c12))

print("\n=== ISOTROPIA (otras componentes) ===")
print("m1^2 via h02:", sp.expand(2 * coef_eps2((0, 2))))
print("m1^2 via h03:", sp.expand(2 * coef_eps2((0, 3))))
print("m2^2 via h13:", sp.expand(-2 * coef_eps2((1, 3))))
print("m2^2 via h23:", sp.expand(-2 * coef_eps2((2, 3))))

print("\n=== CROSS-CHECK: inversa perturbativa eta - nhn + nhnhn ===")
print("m1^2 pert:", sp.expand(2 * coef_eps2((0, 1), exact=False)))
print("m2^2 pert:", sp.expand(-2 * coef_eps2((1, 2), exact=False)))

# --- Cross-check final: h simetrica GENERAL con inversa perturbativa,
#     extrayendo coef de h01^2 y h12^2 del desarrollo completo (guarda contra
#     terminos cruzados que la configuracion especial pudiera esconder).
print("\n=== CROSS-CHECK: h general (perturbativa) ===")
hs = {(i, j): sp.Symbol(f'h{i}{j}') for i in range(4) for j in range(i, 4)}
H = sp.Matrix(4, 4, lambda i, j: hs[(i, j)] if i <= j else hs[(j, i)])
g = eta + eps * H
ginv = eta - eps * (eta * H * eta) + eps**2 * (eta * H * eta * H * eta)
B = ginv[1:, 1:]
V = sp.Matrix([ginv[0, 1], ginv[0, 2], ginv[0, 3]])
Z = V * V.T
Bp = {0: sp.eye(3), 1: B, 2: B * B, 3: B * B * B}
tau = {n: sp.trace(Bp[n]) for n in (1, 2, 3)}
y = {n: sp.trace(Bp[n] * Z) for n in (0, 1, 2, 3)}
U = (U0 + sum(Utau[n] * (tau[n] - 3) for n in (1, 2, 3))
        + sum(Uy[n] * y[n] for n in (0, 1, 2, 3)))
detg = sp.expand(g.det())
# serie de sqrt(-det g) a O(eps^2): -det g = 1 + eps*d1 + eps^2*d2 + ...
d1 = sp.expand((-detg).coeff(eps, 1))
d2 = sp.expand((-detg).coeff(eps, 2))
sqrtg = 1 + sp.Rational(1, 2) * (eps * d1 + eps**2 * d2) - sp.Rational(1, 8) * (eps * d1)**2
L = sp.expand(sqrtg * sp.expand(U))
c2 = sp.expand(L.coeff(eps, 2))
c_h01 = c2.coeff(hs[(0, 1)], 2)
c_h12 = c2.coeff(hs[(1, 2)], 2)
print("m1^2 (h general) =", sp.expand(2 * c_h01))
print("m2^2 (h general) =", sp.expand(-2 * c_h12))
