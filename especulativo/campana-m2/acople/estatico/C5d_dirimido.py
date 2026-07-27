# -*- coding: utf-8 -*-
"""
C5d DIRIMIDO (2026-07-27) -- veredicto reproducible del item 7 de la block list.

EL PROBLEMA: el chequeo C5d de colA_causal.py imprime un residuo NO nulo
    -m1^2 p^4 rho_op^2 / [2 (alpha^2+3 alpha beta-alpha+3 beta-2)(m1^2+2 kappa p^2)]
contra "esperado 0", comparando su omega^2 (con todos los NLO) contra la formula
exacta del acta SECTOR-ESCALAR-2026-07-21. En apariencia contradice la cancelacion
exacta de m1^2 en el sector escalar.

VEREDICTO (demostrado abajo, cada paso con chequeo simbolico):
  El residuo es un ARTEFACTO DEL METODO DE EXTRACCION de C5d, no fisica.
  C5d leia omega^2 como -coeff(psi) de psi_dd en el sistema reducido (psi, E).
  Eso es valido solo si psi_dd no contiene Edot. El operador rho_op*trK*R3 es el
  UNICO NLO que genera un termino G*psi*Edot en L_red (R3 es el unico invariante
  con psi sin derivar), asi que con rho_op != 0 el despeje crudo da
      psi_dd = -W2_raw*psi + b*Edot + c*psi_dot,   b, c ∝ rho_op,
  y -coeff(psi) = W2_raw NO es la frecuencia de ningun modo. La frecuencia fisica
  (Routhiana con Pi_E conservado, o det 4x4 sin reduccion) es
      omega^2_fis = W2_raw + G^2/(4AF - D^2),
  que coincide EXACTAMENTE con la formula del acta y NO depende de m1^2:
      residuo_C5d = W2_raw - omega^2_fis = -G^2/(4AF - D^2)  ∝ rho_op^2.
  La dependencia en m1^2 del artefacto entra por el vinculo de B
  (B ∝ 1/(m1^2 + 2 kappa p^2)), heredada por F y G: por eso el residuo tiene la
  forma m1^2 p^4 rho_op^2 / [2 den_acta (m1^2 + 2 kappa p^2)].

  NO es mezcla de convenciones rho vs rho_op: se verifica abajo (paso [7]) que el
  DL_NLO del pipeline escalar (run2_scalar.py, simbolo 'rho') y el del acople
  (colA_causal.py, simbolo 'rho_op') son la MISMA densidad lagrangiana termino a
  termino: (1/4)[al KK + be trK^2 + si R3^2 + rho trK R3] con el mismo Kbar_ij
  (con shift) y el mismo R3. rho == rho_op, un solo acople.

  NO es un problema real: la cancelacion exacta de m1^2 en omega^2 del sector
  escalar queda CONFIRMADA tambien por el pipeline del acople (pasos [5] y [6]).
  colA_cierre.py (D1) ya contenia el control correcto por la ruta del det; este
  script agrega la explicacion cerrada del residuo (la identidad -G^2/(4AF-D^2)).

Requiere: eh_lib.py (misma carpeta). Corre en ~10 s (sympy 1.14, py 3.14).
Uso:  py -3.14 C5d_dirimido.py
Salida esperada: 26 chequeos [PASS] y el bloque VEREDICTO; cualquier [FAIL]
invalida el cierre del item 7 (el script lo dice explicitamente).
Corrida de referencia: 2026-07-27, todos PASS, t_total = 10 s.
"""
import sys
import time
import sympy as sp
from eh_lib import t, z, p, zavg, EL

# consola Windows cp1252: nunca morir por un caracter (los prints son ASCII igual)
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

T0 = time.time()
FALLAS = []


def check(nombre, expr_o_bool, esperado="0"):
    """PASS/FAIL con registro."""
    if isinstance(expr_o_bool, bool):
        ok = expr_o_bool
        val = expr_o_bool
    else:
        val = sp.simplify(expr_o_bool)
        ok = (val == 0)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {nombre}: {val}  (esperado {esperado})")
    if not ok:
        FALLAS.append(nombre)
    return ok


print("=" * 78)
print("C5d DIRIMIDO -- construccion identica a colA_causal.py (lineas 23-74, 191-201)")
print("=" * 78)

Mp2 = sp.Symbol('Mpl2', positive=True)
m0s, m1s = sp.symbols('m0sq m1sq', positive=True)
al, be, si, rh = sp.symbols('alpha beta sigma rho_op', real=True)

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

# LEH canonico (verificado contra sqrt(-g)R en C0 de colA_causal.py: residuo 0)
LEH_can = (-3 * dpsi**2 + p**2 * psi**2 - 2 * p**2 * phi * psi
           - 2 * p**2 * B * dpsi + p**2 * dpsi * dE)

Xc = [t, sp.Symbol('x'), sp.Symbol('y'), z]
Lmass = sp.expand(zavg(sp.Rational(1, 4) * (
    m0s * H[0, 0]**2 + 2 * m1s * (H[0, 1]**2 + H[0, 2]**2 + H[0, 3]**2))))
Kb = sp.zeros(3, 3)
for a in range(3):
    for b in range(3):
        Kb[a, b] = (sp.diff(H[a + 1, b + 1], t)
                    - sp.diff(H[0, b + 1], Xc[a + 1])
                    - sp.diff(H[0, a + 1], Xc[b + 1]))
trK = sum(Kb[a, a] for a in range(3))
R3 = (sum(sp.diff(H[a + 1, b + 1], Xc[a + 1], Xc[b + 1])
          for a in range(3) for b in range(3))
      - sum(sp.diff(H[b + 1, b + 1], Xc[a + 1], Xc[a + 1])
            for a in range(3) for b in range(3)))
DLfull = sp.expand(zavg(sp.expand(
    sp.Rational(1, 4) * al * sum(Kb[a, b]**2 for a in range(3) for b in range(3))
    + sp.Rational(1, 4) * be * trK**2
    + sp.Rational(1, 4) * si * R3**2
    + sp.Rational(1, 4) * rh * trK * R3)))

Ltot4 = sp.expand(Mp2 * LEH_can + Lmass + DLfull)

# formula exacta del acta SECTOR-ESCALAR-2026-07-21 (la que C5d usaba, Mp2=1)
kap = al + be
den_acta = -2 - al + 3 * be + al**2 + 3 * al * be
W2_acta4 = p**2 * (kap * (2 * p**2 - m0s) + p**2 * m0s * (rh**2 / 2 - 2 * kap * si)) \
    / (m0s * den_acta)
# la misma formula con Mp2 completo (verificador escalar run2_scalar.py, linea 72)
W2_acta_full = p**2 * (kap * Mp2 * (2 * Mp2 * p**2 - m0s)
                       + p**2 * m0s * (rh**2 / 2 - 2 * kap * si)) \
    / (m0s * (-2 * Mp2**2 - Mp2 * al + 3 * Mp2 * be + al**2 + 3 * al * be))
check("[0] acta(Mp2 completo) se reduce a acta(Mp2=1) del C5d",
      W2_acta_full.subs(Mp2, 1) - W2_acta4)

# ---------------------------------------------------------------------------
print("\n[1] Reproduccion EXACTA del chequeo C5d original (metodo crudo)")
# ---------------------------------------------------------------------------
elphi4 = sp.expand(sp.diff(Ltot4, phi))
elB4 = sp.expand(sp.diff(Ltot4, B))
# phi y B son auxiliares tambien con todos los NLO (nada de phi_dot, B_dot):
check("[1a] Ltot4 sin phi_dot (phi auxiliar)", sp.diff(Ltot4, sp.Derivative(phi, t)))
check("[1b] Ltot4 sin B_dot (B auxiliar)", sp.diff(Ltot4, sp.Derivative(B, t)))
solc4 = sp.solve([elphi4, elB4], [phi, B], dict=True)[0]
B_c = sp.simplify(solc4[B])
print("    B (vinculo) =", B_c)
print("    -> denominador del vinculo de B: m1^2 + 2*kappa*p^2 (de aqui hereda")
print("       m1^2 el artefacto; comparar con el denominador del residuo)")
Lred4 = sp.expand(sp.simplify(Ltot4.subs(solc4)))
check("[1c] E ciclica en Lred4 (dL/dE = 0 => Pi_E conservado)",
      sp.diff(Lred4, E))
print(f"    [t={time.time()-T0:.0f}s] reduccion lista")

D2psi, D2E = sp.Derivative(psi, (t, 2)), sp.Derivative(E, (t, 2))
eqa = sp.expand(EL(Lred4, psi))
eqb = sp.expand(EL(Lred4, E))
soldd4 = sp.solve([eqa, eqb], [D2psi, D2E], dict=True)[0]
psidd4 = sp.expand(soldd4[D2psi])
W2_4 = sp.simplify(-psidd4.coeff(psi))          # <- lo que C5d llamaba "omega^2"
residuo = sp.simplify(W2_4.subs(Mp2, 1) - W2_acta4)
print("    residuo C5d reproducido =", residuo)

# el residuo capturado de la corrida de colA_causal.py (2026-07-27, exit 0):
locald = {'m1sq': m1s, 'rho_op': rh, 'alpha': al, 'beta': be, 'p': p}
residuo_capturado = sp.sympify(
    "-m1sq*p**4*rho_op**2/(4*alpha**3*p**2 + 16*alpha**2*beta*p**2"
    " + 2*alpha**2*m1sq - 4*alpha**2*p**2 + 12*alpha*beta**2*p**2"
    " + 6*alpha*beta*m1sq + 8*alpha*beta*p**2 - 2*alpha*m1sq - 8*alpha*p**2"
    " + 12*beta**2*p**2 + 6*beta*m1sq - 8*beta*p**2 - 4*m1sq)", locals=locald)
check("[1d] residuo reproducido == residuo impreso por colA_causal.py",
      residuo - residuo_capturado)

# forma factorizada (cerrada) del artefacto:
residuo_fact = -m1s * p**4 * rh**2 / (2 * den_acta * (m1s + 2 * kap * p**2))
check("[1e] residuo == -m1^2 p^4 rho_op^2 / [2 den_acta (m1^2+2 kappa p^2)]",
      residuo - residuo_fact)

# ---------------------------------------------------------------------------
print("\n[2] POR QUE el metodo de C5d es invalido con rho_op != 0:")
print("    psi_dd despejado del sistema (psi,E) contiene Edot y psi_dot")
# ---------------------------------------------------------------------------
b_coef = sp.simplify(psidd4.coeff(dE))
c_coef = sp.simplify(psidd4.coeff(dpsi))
print("    coeff(Edot)  en psi_dd =", b_coef)
print("    coeff(psidot) en psi_dd =", c_coef)
check("[2a] coeff(Edot) se anula al apagar rho_op (el acople es puro rho_op)",
      b_coef.subs(rh, 0))
check("[2b] coeff(psidot) se anula al apagar rho_op",
      c_coef.subs(rh, 0))
check("[2c] con rho_op != 0 el coeff(Edot) NO es cero (por eso -coeff(psi) "
      "no es omega^2)", sp.simplify(b_coef) != 0, esperado="True")
check("[2d] completitud: psi_dd == -W2_raw*psi + b*Edot + c*psi_dot",
      sp.expand(psidd4 - (-W2_4 * psi + b_coef * dE + c_coef * dpsi)))

# ---------------------------------------------------------------------------
print("\n[3] Forma cuadratica de Lred4 y la IDENTIDAD DEL ARTEFACTO")
# ---------------------------------------------------------------------------
Ac = sp.simplify(Lred4.coeff(dpsi, 2))
Fc = sp.simplify(Lred4.coeff(dE, 2))
resto = sp.expand(Lred4 - Ac * dpsi**2 - Fc * dE**2)
Dc = sp.simplify(resto.coeff(dpsi).coeff(dE))
Cc = sp.simplify(Lred4.coeff(psi, 2).subs({dpsi: 0, dE: 0}))
Gc = sp.simplify(sp.expand(Lred4).coeff(psi, 1).coeff(dE))
Hc = sp.simplify(sp.expand(Lred4).coeff(psi, 1).coeff(dpsi))
Lq = (Ac * dpsi**2 + Fc * dE**2 + Dc * dpsi * dE + Cc * psi**2
      + Gc * psi * dE + Hc * psi * dpsi)
check("[3a] Lred4 == A psidot^2 + F Edot^2 + D psidot Edot + C psi^2 "
      "+ G psi Edot + Hc psi psidot", sp.expand(Lred4 - Lq))
check("[3b] G ~ rho_op (G|rho_op=0 == 0): trK*R3 es el unico NLO con psi "
      "sin derivar", Gc.subs(rh, 0))
disc = 4 * Ac * Fc - Dc**2
check("[3c] W2_raw (lo que C5d extrajo) == -4CF/(4AF-D^2)",
      W2_4 - (-4 * Cc * Fc / disc))
# la frecuencia fisica en forma cerrada (Routh, ver [4]): (G^2-4CF)/(4AF-D^2)
w2_fis_forma = sp.simplify((Gc**2 - 4 * Cc * Fc) / disc)
check("[3d] IDENTIDAD DEL ARTEFACTO: residuo C5d == -G^2/(4AF-D^2)",
      sp.simplify((W2_4 - w2_fis_forma).subs(Mp2, 1)) - residuo)
print(f"    [t={time.time()-T0:.0f}s]")

# ---------------------------------------------------------------------------
print("\n[4] La frecuencia FISICA por Routh (Pi_E = Pi0 conservado, Pi0 generico)")
# ---------------------------------------------------------------------------
Pi0 = sp.Symbol('Pi0', real=True)
PiE = sp.expand(sp.diff(Lred4, dE))          # = 2F Edot + D psidot + G psi
solEd = sp.solve(sp.Eq(PiE, Pi0), dE)[0]
Routh = sp.expand(Lred4.subs(dE, solEd) - Pi0 * solEd)
eqpsi = sp.expand(EL(Routh, psi))
# EL de eh_lib = dL/dpsi - d/dt(dL/dpsidot); para L = K psidot^2 - V psi^2 da
# -2V psi - 2K psidd = 0 => omega^2 = V/K = +coeff(psi)/coeff(psidd):
check("[4-pre] EOM de Routh sin friccion aparente (coeff(psidot) == 0; "
      "el c*psidot del metodo crudo era espurio)", eqpsi.coeff(dpsi))
w2_routh = sp.simplify(eqpsi.coeff(psi) / eqpsi.coeff(D2psi))
check("[4a] frecuencia de Routh NO depende de Pi0 (Pi0 solo corre el punto fijo)",
      sp.diff(w2_routh, Pi0))
check("[4b] omega^2(Routh) == (G^2-4CF)/(4AF-D^2)", w2_routh - w2_fis_forma)
check("[4c] omega^2(Routh, Mp2=1) == formula exacta del acta ESCALAR "
      "(el 'esperado 0' que C5d nunca podia dar)",
      w2_routh.subs(Mp2, 1) - W2_acta4)
check("[4d] omega^2(Routh, Mp2 completo) == formula del verificador escalar",
      w2_routh - W2_acta_full)
check("[4e] CANCELACION DE m1^2 con TODOS los NLO: d(omega^2)/d(m1^2) == 0",
      sp.diff(sp.together(w2_routh), m1s))
print(f"    [t={time.time()-T0:.0f}s]")

# ---------------------------------------------------------------------------
print("\n[5] Control independiente: ruta del DET 4x4 (sin ninguna reduccion)")
# ---------------------------------------------------------------------------
w = sp.Symbol('omega')
amps = sp.symbols('phi0 B0 psi0 E0')
ex = sp.exp(-sp.I * w * t)
repl = {f: a * ex for f, a in zip(fields, amps)}
eqs = [sp.expand(sp.simplify(EL(Ltot4, f).subs(repl).doit() / ex)) for f in fields]
M = sp.Matrix([[sp.expand(eq).coeff(a) for a in amps] for eq in eqs])
det = sp.factor(M.det())
roots = sp.solve(sp.Eq(det, 0), w**2)
w2nz = [r for r in roots if sp.simplify(r) != 0]
print("    raices omega^2 no nulas del det:", len(w2nz))
check("[5a] hay exactamente UNA raiz no nula", len(w2nz) == 1, esperado="True")
check("[5b] omega^2(det) == omega^2(Routh) (dos rutas, mismo resultado)",
      sp.simplify(w2nz[0] - w2_routh))
check("[5c] omega^2(det) es independiente de m1^2",
      sp.diff(sp.together(sp.simplify(w2nz[0])), m1s))
print(f"    [t={time.time()-T0:.0f}s]")

# ---------------------------------------------------------------------------
print("\n[6] Esquina numerica ilustrativa (magnitud del artefacto)")
# ---------------------------------------------------------------------------
esq = {m0s: 1, m1s: 2, Mp2: 1, al: 0, be: -sp.Rational(1, 100),
       si: sp.Rational(1, 50), rh: sp.Rational(1, 20), p: sp.Rational(3, 5)}
w2f = w2_routh.subs(esq)
w2c = W2_4.subs(esq)
print("    esquina (m0^2,m1^2)=(1,2), al=0, be=-1/100, si=1/50, rho_op=1/20, p=3/5:")
print("      omega^2 fisica (Routh=det=acta) =", sp.nsimplify(w2f), "=", float(w2f),
      " (<0: banda de Jeans, p^2<1/2 con kappa<0 -- correcto)")
print("      'omega^2' cruda de C5d          =", sp.nsimplify(w2c), "=", float(w2c))
print("      artefacto (w2_cruda - w2_fisica) =", float(w2c - w2f))
check("[6a] esquina: residuo numerico == formula factorizada",
      (w2c - w2f) - residuo_fact.subs(esq))

# ---------------------------------------------------------------------------
print("\n[7] Convenciones: rho (pipeline escalar) y rho_op (pipeline acople)")
print("    son EL MISMO operador -- cotejo termino a termino de las densidades")
# ---------------------------------------------------------------------------
# reconstruccion textual del DL_NLO del verificador escalar (run2_scalar.py,
# lineas 23-30), con el simbolo rh en el lugar de su 'rho':
s_ = sp.sin(p * z)
h0z_esc = -p * B * s_
hxx_esc = 2 * psi * c
hzz_esc = 2 * psi * c - p**2 * E * c
Kxx_esc = sp.diff(hxx_esc, t)
Kyy_esc = Kxx_esc
Kzz_esc = sp.diff(hzz_esc, t) - 2 * sp.diff(h0z_esc, z)
KK_esc = Kxx_esc**2 + Kyy_esc**2 + Kzz_esc**2
trK_esc = Kxx_esc + Kyy_esc + Kzz_esc
R3_esc = 4 * p**2 * psi * c
LNLO_esc = zavg(sp.Rational(1, 4) * (al * KK_esc + be * trK_esc**2)
                + sp.Rational(1, 4) * si * R3_esc**2
                + sp.Rational(1, 4) * rh * trK_esc * R3_esc)
check("[7a] DL_NLO(escalar, rho) == DL_NLO(acople, rho_op) bajo rho<->rho_op "
      "(mismo operador, misma normalizacion)",
      sp.expand(LNLO_esc - DLfull))
# y las masas tambien (misma convencion (1/4)[m0 h00^2 + 2 m1 h0i^2]):
Lm_esc = (sp.Rational(1, 2) * m0s * phi**2
          + sp.Rational(1, 4) * m1s * p**2 * B**2)
check("[7b] L_masa(escalar) == L_masa(acople)", sp.expand(Lm_esc - Lmass))

# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
if not FALLAS:
    print("VEREDICTO [todos los chequeos PASS]:")
    print("  * El residuo C5d es un ARTEFACTO DEL METODO del chequeo: -coeff(psi)")
    print("    de psi_dd no es omega^2 cuando rho_op != 0 (hay acople G psi Edot;")
    print("    residuo == -G^2/(4AF-D^2), identidad [3d]).")
    print("  * La formula del acta ESCALAR es la dispersion correcta TAMBIEN en el")
    print("    pipeline del acople: Routh y det 4x4 la reproducen con residuo 0")
    print("    ([4c][4d][5b]).")
    print("  * m1^2 se cancela EXACTAMENTE en omega^2 con todos los NLO, tambien")
    print("    aca ([4e][5c]): NO hay contradiccion con SECTOR-ESCALAR-2026-07-21.")
    print("  * rho == rho_op: mismo operador trK*R3, misma normalizacion ([7a]).")
    print("  * El chequeo C5d de colA_causal.py debe marcarse como INVALIDO por")
    print("    metodo (no obsoleto, no convencion, no fisica). El control correcto")
    print("    ya existe: colA_cierre.py D1 (det) — y este script (Routh + det +")
    print("    identidad del artefacto).")
else:
    print("VEREDICTO: INCOMPLETO — chequeos fallidos:", FALLAS)
    print("NO usar este script como cierre del item 7 hasta resolverlos.")
print(f"[t total = {time.time()-T0:.0f}s]")
print("FIN C5d_dirimido")
