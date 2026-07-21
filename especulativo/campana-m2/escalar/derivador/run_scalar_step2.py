"""Sector escalar, paso 2: L total = Mpl^2 * L_EH^(2) + L_masas,
EOMs exactas, matriz de dispersion 4x4, determinante, y reduccion.
Todo directo de sympy, sin IBP a mano (las EL son invariantes ante
derivadas totales)."""
import sympy as sp
from eh_lib import t, z, p, zavg, L12_of_ansatz, EL

Mp2 = sp.Symbol('Mpl2', positive=True)
m0s, m1s = sp.symbols('m0sq m1sq', real=True)

phi = sp.Function('phi')(t)
B = sp.Function('B')(t)
psi = sp.Function('psi')(t)
E = sp.Function('Ef')(t)
fields = [phi, B, psi, E]

c = sp.cos(p * z)
H = sp.zeros(4, 4)
H[0, 0] = 2 * phi * c
H[0, 3] = H[3, 0] = sp.diff(B * c, z)
H[1, 1] = 2 * psi * c
H[2, 2] = 2 * psi * c
H[3, 3] = 2 * psi * c + sp.diff(E * c, (z, 2))

L1d, L2d = L12_of_ansatz(H)
LEH = sp.expand(zavg(L2d))

# masas: L = (1/4)[m0^2 h00^2 + 2 m1^2 h0i h0i]  (m2=m3=m4=0 exactas)
Lmass_d = sp.Rational(1, 4) * (m0s * H[0, 0]**2
                               + 2 * m1s * (H[0, 1]**2 + H[0, 2]**2 + H[0, 3]**2))
Lmass = sp.expand(zavg(Lmass_d))
print("L_masas promediado:", Lmass)

Ltot = sp.expand(Mp2 * LEH + Lmass)

# --- EOMs exactas y matriz de dispersion ---
w = sp.Symbol('omega')
amps = sp.symbols('phi0 B0 psi0 E0')
ex = sp.exp(-sp.I * w * t)
repl = {f: a * ex for f, a in zip(fields, amps)}

eqs = []
for f in fields:
    e = EL(Ltot, f)
    ew = sp.expand(sp.simplify(e.subs(repl).doit() / ex))
    eqs.append(ew)
    print(f"EOM_{f.func.__name__}: ", sp.collect(ew, amps))

M = sp.Matrix([[sp.expand(eq).coeff(a) for a in amps] for eq in eqs])
# control: las eqs son lineales homogeneas en amps
resid = sp.simplify(sp.Matrix(eqs) - M * sp.Matrix(amps))
print("residuo linealidad (esperado [0,0,0,0]):", list(resid))
det = sp.factor(M.det())
print("det M(omega) =", det)
print("raices en omega^2:", sp.solve(sp.Eq(det, 0), w**2))

# --- control RG puro ---
det0 = sp.factor(det.subs({m0s: 0, m1s: 0}))
print("det con m0=m1=0 (RG puro):", det0)

# rango de M en RG puro (degeneracion gauge)
M0 = M.subs({m0s: 0, m1s: 0})
print("rango M (RG puro):", M0.rank(), " / rango M (masas genericas):", M.rank())

# nucleo de M(omega) con masas genericas para omega generico y omega=0
print("nucleo con omega generico:", M.nullspace())
print("nucleo en omega=0:", M.subs(w, 0).nullspace())
