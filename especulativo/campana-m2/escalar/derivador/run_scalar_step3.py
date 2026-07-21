"""Sector escalar, paso 3: LO (EH + masas) + operadores NLO del medio
invariantes bajo la simetria residual x^i -> x^i + xi^i(x):
  K_ij := (1/2) Kbar_ij,  Kbar_ij = dh_ij/dt - d_i h_0j - d_j h_0i
  R3   := d_i d_j h_ij - lap(h_kk)   (curvatura 3d linealizada)
  DL = (al/4) Kbar_ij Kbar_ij + (be/4) (tr Kbar)^2 + (si/4) R3^2
       + (rho/4) (tr Kbar) R3
Derivacion exacta: det de dispersion, reduccion de vinculos (phi, B
auxiliares; Pi_E = 0 en el sector oscilatorio), modo fisico, omega^2(p)
exacta, expansion p->0, condicion de no-fantasma, esquina (1,2), limites.
"""
import sympy as sp
from eh_lib import t, z, x, y, p, X, zavg, L12_of_ansatz, EL

Mp2 = sp.Symbol('Mpl2', positive=True)
m0s, m1s = sp.symbols('m0sq m1sq', real=True)
al, be, si, rho = sp.symbols('alpha beta sigma rho', real=True)

phi = sp.Function('phi')(t)
B = sp.Function('B')(t)
psi = sp.Function('psi')(t)
E = sp.Function('Ef')(t)
fields = [phi, B, psi, E]
dpsi = sp.Derivative(psi, t)
dE = sp.Derivative(E, t)

c = sp.cos(p * z)
H = sp.zeros(4, 4)
H[0, 0] = 2 * phi * c
H[0, 3] = H[3, 0] = sp.diff(B * c, z)
H[1, 1] = 2 * psi * c
H[2, 2] = 2 * psi * c
H[3, 3] = 2 * psi * c + sp.diff(E * c, (z, 2))

L1d, L2d = L12_of_ansatz(H)
LEH = sp.expand(zavg(L2d))

# --- forma canonica del EH escalar: LEH = LEH_can + dW/dt (verificado) ---
LEH_can = (-3 * dpsi**2 + p**2 * psi**2 - 2 * p**2 * phi * psi
           - 2 * p**2 * B * dpsi + p**2 * dpsi * dE)
W = (3 * phi * dpsi + p**2 * phi * B - sp.Rational(1, 2) * p**2 * phi * dE
     - sp.Rational(1, 4) * p**4 * E * dE
     - sp.Rational(1, 2) * p**2 * (E * dpsi + psi * dE)
     + 3 * psi * dpsi)
resid = sp.simplify(LEH - LEH_can - sp.diff(W, t))
print("LEH - LEH_can - dW/dt (esperado 0):", resid)

# --- masas ---
Lmass = sp.expand(zavg(sp.Rational(1, 4) * (
    m0s * H[0, 0]**2 + 2 * m1s * (H[0, 1]**2 + H[0, 2]**2 + H[0, 3]**2))))

# --- operadores NLO ---
Kb = sp.zeros(3, 3)
for a in range(3):
    for b in range(3):
        Kb[a, b] = (sp.diff(H[a + 1, b + 1], t)
                    - sp.diff(H[0, b + 1], X[a + 1])
                    - sp.diff(H[0, a + 1], X[b + 1]))
trK = sum(Kb[a, a] for a in range(3))
R3 = (sum(sp.diff(H[a + 1, b + 1], X[a + 1], X[b + 1])
          for a in range(3) for b in range(3))
      - sum(sp.diff(H[b + 1, b + 1], X[a + 1], X[a + 1])
            for a in range(3) for b in range(3)))
DL = (sp.Rational(1, 4) * al * sum(Kb[a, b]**2 for a in range(3) for b in range(3))
      + sp.Rational(1, 4) * be * trK**2
      + sp.Rational(1, 4) * si * R3**2
      + sp.Rational(1, 4) * rho * trK * R3)
DLavg = sp.expand(zavg(sp.expand(DL)))
print("DL promediado:")
print(sp.collect(DLavg, [al, be, si, rho]))

Ltot = sp.expand(Mp2 * LEH_can + Lmass + DLavg)

# --- control: simetria residual E -> E + 2C (C constante) ---
Cc = sp.Symbol('Cc')
replres = {phi: sp.Integer(0), B: sp.Integer(0), psi: sp.Integer(0), E: 2 * Cc}
ok = all(sp.simplify(EL(Ltot, f).subs(replres).doit()) == 0 for f in fields)
print("simetria residual (EL en config residual pura = 0):", ok)

# --- ruta 1: det de dispersion exacto ---
w = sp.Symbol('omega')
amps = sp.symbols('phi0 B0 psi0 E0')
ex = sp.exp(-sp.I * w * t)
repl = {f: a * ex for f, a in zip(fields, amps)}
eqs = [sp.expand(sp.simplify(EL(Ltot, f).subs(repl).doit() / ex)) for f in fields]
M = sp.Matrix([[sp.expand(eq).coeff(a) for a in amps] for eq in eqs])
det = sp.factor(M.det())
print("det M(omega) =", det)
roots = sp.solve(sp.Eq(det, 0), w**2)
print("raices omega^2:", roots)

# --- ruta 2: reduccion en el Lagrangiano ---
# phi y B auxiliares (sin derivadas temporales en Ltot):
assert sp.diff(Ltot, sp.Derivative(phi, t)) == 0
assert sp.diff(Ltot, sp.Derivative(B, t)) == 0
elphi = sp.expand(sp.diff(Ltot, phi))
elB = sp.expand(sp.diff(Ltot, B))
sol = sp.solve([elphi, elB], [phi, B], dict=True)[0]
print("phi resuelto:", sp.simplify(sol[phi]))
print("B resuelto:  ", sp.simplify(sol[B]))
Lred = sp.expand(sp.simplify(Ltot.subs(sol)))
print("dL_red/dE (esperado 0):", sp.simplify(sp.diff(Lred, E)))
Acoef = Lred.coeff(dpsi, 2)
Fcoef = Lred.coeff(dE, 2)
Dcoef = sp.expand(Lred - Acoef * dpsi**2 - Fcoef * dE**2).coeff(dpsi).coeff(dE)
Ccoef = Lred.coeff(psi, 2).subs({dpsi: 0, dE: 0})
Gcoef = sp.expand(Lred).coeff(psi, 1).coeff(dE)   # termino psi*dE (de rho)
Hcoef = sp.expand(Lred).coeff(psi, 1).coeff(dpsi)  # termino psi*dpsi
print("A (psidot^2):", sp.simplify(Acoef))
print("F (Edot^2):  ", sp.simplify(Fcoef))
print("D (psidot Edot):", sp.simplify(Dcoef))
print("C (psi^2):   ", sp.simplify(Ccoef))
print("G (psi Edot):", sp.simplify(Gcoef))
print("Hc (psi psidot):", sp.simplify(Hcoef))
# reconstruccion como forma cuadratica (control de completitud)
Lq = (Acoef * dpsi**2 + Fcoef * dE**2 + Dcoef * dpsi * dE + Ccoef * psi**2
      + Gcoef * psi * dE + Hcoef * psi * dpsi)
print("L_red - forma cuadratica (esperado 0):", sp.simplify(Lred - Lq))

# sector oscilatorio: Pi_E = dL/dEdot = 0  ->  Edot = ...
PiE = sp.expand(sp.diff(Lred, dE))
solE = sp.solve(PiE, dE)[0]
Lmode = sp.expand(sp.simplify(Lred.subs(dE, solE)))
Kkin = sp.simplify(Lmode.coeff(dpsi, 2))
Vpot = sp.simplify(-Lmode.coeff(psi, 2).subs(dpsi, 0))
cross = sp.simplify(sp.expand(Lmode).coeff(psi, 1).coeff(dpsi))
print("K (cinetico del modo):", Kkin)
print("V (potencial del modo):", Vpot)
print("cruce psi*psidot (deriv total, coef const):", cross)
w2_routh = sp.simplify(Vpot / Kkin)
print("omega^2 exacta (Routh) =", sp.simplify(w2_routh))

# comparacion con la raiz no nula del det
w2_det = [r for r in roots if sp.simplify(r) != 0]
print("omega^2 exacta (det)   =", sp.simplify(w2_det[0]) if w2_det else "solo 0")
if w2_det:
    print("difieren? ", sp.simplify(w2_routh - w2_det[0]))

# --- expansiones y limites ---
print()
print("== expansion p->0 de omega^2 ==")
ser = sp.series(w2_routh, p, 0, 8)
print(sp.simplify(ser.removeO()))
print()
print("== limite de desacople Mpl2 -> oo ==")
w2_dec = sp.limit(w2_routh, Mp2, sp.oo)
print(sp.simplify(w2_dec))
print()
print("== limite NLO -> 0 (debe recuperar omega^2 -> 0) ==")
w2_nlo0 = sp.simplify(w2_routh.subs({al: 0, be: 0, si: 0, rho: 0}))
print(w2_nlo0)
print()
print("== K en el limite NLO chico (estructura del signo) ==")
lam = sp.Symbol('lambda', positive=True)
Ksc = Kkin.subs({al: lam * al, be: lam * be, si: lam * si, rho: lam * rho})
print("K ~ (lambda->0):", sp.simplify(sp.series(Ksc, lam, 0, 2).removeO()))
