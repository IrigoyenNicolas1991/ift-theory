# Paso 4: cotejo contra Dubovsky hep-th/0409124 (transcripciones del control textual).
# (a) limite de desacople: nuestro L_m con h = d pi + d pi vs su ec. (22) en la fase (72)
# (b) su (86) -> vinculos (87),(88) -> (99); chequeo del signo de 6(d0 tau)^2
# (c) normalizacion: EH de (86) vs EH canonico Mp^2 sqrt(-g)R (mi pipeline, ya validado)
import sympy as sp
from lib_eh import t, z, p, Mp2, zavg, EL

c = sp.cos(p*z); s = sp.sin(p*z)
m02, m12 = sp.symbols('m02 m12', real=True)   # masas BCP (nuestras)
w = sp.symbols('omega', real=True)

# ---------- (a) Goldstones ----------
P0 = sp.Function('P0')(t); PL = sp.Function('PL')(t)
# pi_0 = P0 c ; pi_z = (dz/sqrt(-dz^2)) (PL c) = -PL s  => h = d pi + d pi (indices abajo)
pi0 = P0*c; piz = -PL*s
h00 = 2*sp.diff(pi0, t)
h0z = sp.diff(piz, t) + sp.diff(pi0, z)
Lm_ours = zavg(sp.Rational(1, 4)*(m02*h00**2 + 2*m12*h0z**2))
print("L_m goldstone (nuestro) =", sp.simplify(Lm_ours))
# dispersion
amps = sp.symbols('c0:2')
sub = {P0: amps[0]*sp.exp(sp.I*w*t), PL: amps[1]*sp.exp(sp.I*w*t)}
eqs = [sp.expand(EL(Lm_ours, f).subs(sub).doit()/sp.exp(sp.I*w*t)) for f in (P0, PL)]
M = sp.Matrix([[ex.coeff(a) for a in amps] for ex in eqs])
detG = sp.factor(sp.simplify(M.det()))
print("det goldstone =", detG)
# Dubovsky fase (72): d = alpha nu^4 con alpha = 2 m0D^2/m1D^2; su det(M24) = alpha nu^4 (por su normalizacion)
# lo estructural: det proporcional a omega^4 (cero doble), coeficiente ~ m0^2*m1^2
print("  -> proporcional a omega^4 ?", sp.simplify(detG/w**4).has(w) == False)

# su (22) en fase 72 con conversion m_D^2 = m_B^2/(2 Mp2): comparo Lagrangianos termino a termino
# (22): Mp2*(2 m0D^2 (d0 pi0)^2 + m1D^2 (d0 piL)^2 + m1D^2 (di pi0)^2 + 2 m1D^2 pi0 d0 sqrt(-d^2) piL)
m0D = m02/(2*Mp2); m1D = m12/(2*Mp2)
# modo: pi0 = P0 c, piL = PL c, sqrt(-d^2) piL = p PL c
L22 = Mp2*(2*m0D*sp.diff(P0, t)**2*c**2 + m1D*sp.diff(PL, t)**2*c**2 + m1D*p**2*P0**2*s**2
           + 2*m1D*P0*sp.diff(p*PL, t)*c**2)
L22a = zavg(L22)
dif = sp.expand(Lm_ours - L22a)
okEL = all(sp.simplify(EL(dif, f)) == 0 for f in (P0, PL))
print("(22) fase72 vs nuestro L_m (mod deriv total, conversion 2Mp2):", okEL)

# ---------- (b) (86) -> (99) ----------
tau = sp.Function('tau')(t); sig = sp.Function('sigmaD')(t)
vD = sp.Function('v')(t); psD = sp.Function('psiD')(t)
m0d, m1d = sp.symbols('m0d m1d', positive=True)
MpD = sp.symbols('MpD2', positive=True)
d2 = -p**2  # di^2 en modo
L86 = (MpD/2)*(4*(psD - 2*sp.diff(vD, t) + sp.diff(sig, (t, 2)))*d2*tau
               + 6*tau*sp.diff(tau, (t, 2)) - 2*tau*d2*tau
               + m0d*psD**2 + 2*m1d*(-d2)*vD**2)
# vinculos
solps = sp.solve(sp.diff(L86, psD), psD)[0]
print("(88) a m4=0: psiD =", sp.simplify(solps), "  [claim: 2 p^2 tau / m0d]")
elv = EL(L86, vD)
solv = sp.solve(elv, vD)[0]
print("(87): v =", sp.simplify(solv), "  [claim: 2 taudot / m1d]")
Lred = sp.expand(L86.subs(psD, solps).subs(vD, solv).doit())
# (99) verbatim (lectura euclidea de los cuadrados): (MpD/2)(-4/m0d p^4 tau^2 - 8/m1d p^2 taudot^2
#      + 4 p^2 taudot sigdot + 6 taudot^2 + 2 p^2 tau^2)
L99v = (MpD/2)*(-4*p**4*tau**2/m0d - 8*p**2*sp.diff(tau, t)**2/m1d
                + 4*p**2*sp.diff(tau, t)*sp.diff(sig, t) + 6*sp.diff(tau, t)**2 + 2*p**2*tau**2)
dif99 = sp.expand(Lred - L99v)
print("EL(mi(86->red) - (99) verbatim):")
for f in (tau, sig):
    print("   ", f, ":", sp.simplify(sp.together(EL(dif99, f))))
# con el signo corregido -6 taudot^2:
L99c = L99v - (MpD/2)*12*sp.diff(tau, t)**2
dif99c = sp.expand(Lred - L99c)
print("con -6(d0 tau)^2 en lugar de +6:")
for f in (tau, sig):
    print("   ", f, ":", sp.simplify(sp.together(EL(dif99c, f))))

# ---------- (c) normalizacion EH de (86) ----------
# mi EH canonico escalar (validado paso 1, variables nuestras): Mp2*(-3 psidot^2 + p^2 psi^2 - 2p^2 phi psi - 2p^2 B psidot + p^2 psidot Edot)
# en variables de Dubovsky: tau = 2 psi, v = B, sigma = E, psiD = 2 phi  => psi = tau/2, phi = psiD/2
ps_ = sp.Function('psi_')(t)
LEH_ours_unavg = 2*Mp2*(-3*sp.diff(tau/2, t)**2 + p**2*(tau/2)**2 - 2*p**2*(psD/2)*(tau/2)
                        - 2*p**2*vD*sp.diff(tau/2, t) + p**2*sp.diff(tau/2, t)*sp.diff(sig, t))
# EH de (86) = (86) sin masas:
L86_EH = (MpD/2)*(4*(psD - 2*sp.diff(vD, t) + sp.diff(sig, (t, 2)))*d2*tau
                  + 6*tau*sp.diff(tau, (t, 2)) - 2*tau*d2*tau)
# test: L86_EH == r * LEH_ours_unavg (mod deriv total) con MpD = r' * Mp2 ?
for r in (1, 2):
    difr = sp.expand(L86_EH.subs(MpD, r*Mp2) - LEH_ours_unavg)
    ok = all(sp.simplify(sp.together(EL(difr, f))) == 0 for f in (tau, sig, vD, psD))
    print(f"EH(86) con MpD={r}*Mp2 == EH canonico (mod dt) ?", ok)
