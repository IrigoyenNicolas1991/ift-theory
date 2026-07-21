"""Sector escalar, paso 1: L_EH^(2) crudo sobre el ansatz escalar,
promediado en z, + control de promedio + control de invariancia gauge
(EH puro debe ser invariante bajo difeos linealizados dependientes de t)."""
import sympy as sp
from eh_lib import t, z, p, zavg, check_zavg, L12_of_ansatz, EL

phi = sp.Function('phi')(t)
B = sp.Function('B')(t)
psi = sp.Function('psi')(t)
E = sp.Function('Ef')(t)
fields = [phi, B, psi, E]

c = sp.cos(p * z)
H = sp.zeros(4, 4)
H[0, 0] = 2 * phi * c
H[0, 3] = H[3, 0] = sp.diff(B * c, z)            # h_{0i} = d_i B
H[1, 1] = 2 * psi * c
H[2, 2] = 2 * psi * c
H[3, 3] = 2 * psi * c + sp.diff(E * c, (z, 2))   # h_{ij} = 2 psi delta + d_i d_j E

L1d, L2d = L12_of_ansatz(H)
print("check_zavg escalar:", check_zavg(L2d))
L1avg = zavg(L1d)
print("L1 promediado (esperado 0):", sp.simplify(L1avg))
LEH = sp.expand(zavg(L2d))
print("LEH promediado (crudo):")
print(LEH)
print()

# --- Control de invariancia gauge del EH puro ---
# delta h_mn = d_m xi_n + d_n xi_m, con xi_0 = A(t) cos(pz), xi_z = d_z(C(t)cos(pz))
# => delta phi = Adot, delta B = Cdot + A, delta psi = 0, delta E = 2C
A = sp.Function('Agauge')(t)
C = sp.Function('Cgauge')(t)
repl = {phi: sp.diff(A, t), B: sp.diff(C, t) + A, psi: sp.Integer(0), E: 2 * C}
for f in fields:
    e = EL(LEH, f)
    e2 = sp.simplify(e.subs(repl).doit())
    print(f"EL_{f.func.__name__} sobre gauge puro (esperado 0):", e2)
