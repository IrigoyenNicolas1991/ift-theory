# -*- coding: utf-8 -*-
"""
Tarea 2b (fenomenologo): mapeo U(X,Y) <-> ghost condensate + cotas.
Parte A (sympy): verifica que la dispersion EFT del derivador coincide
  termino a termino con la ec. [ghostJeans] de ACLM hep-th/0312099 bajo
  el diccionario:
     M^4        = 2 m0^2(BCP)             (de 1/8 M^4 h00^2  vs  1/4 m0^2 h00^2)
     kappa=a+b  = -Mbar^2/2               (de -1/2 Mt^2 K^2 - 1/2 Mt'^2 Kij^2,
                                           Kij_ACLM = K̄ij_nuestro/2, Mbar^2=Mt^2+Mt'^2)
     MPl_ours^2 = MPl_ACLM^2 / 2          (L_EH: nuestro MPl^2 R  <->  1/(16piG);
                                           ACLM MPl^2 = 1/(8piG))
Parte B (numerico): tabla de cotas fisicas para U = Lambda^4 * Uhat
  (esquina sana: m0^2 = Lambda^4, m1^2 = 2 Lambda^4).
Controles declarados: Gamma_max reproducido por dos vias (formula ACLM y
  maximizacion directa de nuestra omega^2); todos los numeros con constantes
  estandar (PDG/Planck 2018 con 2 cifras).
"""
import sympy as sp

# ---------- PARTE A: diccionario exacto ----------
p, kappa, m02, MPl2_ours, Mbar2, M4, MPl2_ACLM = sp.symbols(
    'p kappa m02 MPl2_ours Mbar2 M4 MPl2_ACLM', positive=True)

# Dispersion EFT del derivador (limite |alpha|,|beta| << MPl^2), M_Pl restaurado:
#   omega^2 = (kappa/(2 MPl_ours^2)) p^2 - (kappa/m0^2) p^4
omega2_ours = kappa/(2*MPl2_ours)*p**2 - kappa/m02*p**4

# Dispersion ACLM eq.[ghostJeans]: omega^2 = Mbar^2/M^4 k^4 - Mbar^2/(2 MPl_ACLM^2) k^2
omega2_ACLM = Mbar2/M4*p**4 - Mbar2/(2*MPl2_ACLM)*p**2

dic = {kappa: -Mbar2/2, m02: M4/2, MPl2_ours: MPl2_ACLM/2}
diff = sp.simplify(omega2_ours.subs(dic) - omega2_ACLM)
print("PARTE A1: omega2_ours(diccionario) - omega2_ACLM =", diff)
assert diff == 0, "FALLA el diccionario"

# Tasa maxima de Jeans: via nuestra formula (maximizar |omega^2| en la banda)
p2 = sp.symbols('p2', positive=True)
om2 = kappa/(2*MPl2_ours)*p2 - kappa/m02*p2**2   # kappa<0: om2<0 para p2 chico
p2star = sp.solve(sp.diff(om2, p2), p2)[0]
Gamma2_ours = sp.simplify(-om2.subs(p2, p2star))  # = |omega^2|_max
print("PARTE A2: p2* =", p2star, " Gamma^2_ours =", Gamma2_ours)
# ACLM: Gamma = alpha M^3/(4 MPl_ACLM^2), alpha^2 = Mbar^2/M^2
M2, Mb, Mpa = sp.symbols('M2 Mb Mpa', positive=True)  # M2=M^2, Mb=Mbar, Mpa=MPl_ACLM
Gamma_ACLM = (Mb/sp.sqrt(M2))*M2*sp.sqrt(M2)/(4*Mpa**2)   # alpha*M^3/(4 MPl^2)
Gamma2_ACLM = Gamma_ACLM**2
# nuestro Gamma^2 en variables ACLM:
Gamma2_ours_ACLM = sp.simplify(Gamma2_ours.subs({kappa: -Mb**2/2, m02: M2**2/2,
                                                 MPl2_ours: Mpa**2/2}))
diffG = sp.simplify(Gamma2_ours_ACLM - Gamma2_ACLM)
print("PARTE A3: Gamma^2_ours(dic) - Gamma^2_ACLM =", diffG)
assert diffG == 0, "FALLA Gamma"
print("PARTE A: DICCIONARIO VERIFICADO (dispersion y tasa de Jeans identicas)\n")

# ---------- PARTE B: numeros fisicos ----------
import math
# constantes (eV salvo indicacion)
MPl_red = 2.435e27        # masa de Planck reducida = 1/sqrt(8 pi G), en eV  (ACLM MPl)
H0      = 1.44e-33        # Hubble hoy ~ 67.4 km/s/Mpc en eV
age     = 4.35e17         # edad del universo en s
eVinv_s = 6.582e-16       # 1 eV^-1 en segundos
eVinv_m = 1.973e-7        # 1 eV^-1 en metros
rho_DE  = (2.4e-3)**4     # densidad de energia oscura ~ (2.4 meV)^4 en eV^4
r_LAGEOS = 1.2e7          # radio orbital LAGEOS/LARES-region, m
delta_fd = 0.05           # precision frame dragging LARES ~5%

print("PARTE B: esquina sana reescalada U = Lambda^4 Uhat -> m0^2=Lambda^4, m1^2=2Lambda^4 (BCP)")
print("Diccionario fisico: M^4 = 2 m0^2 = 2 Lambda^4 -> M = 2^(1/4) Lambda")
print("m1 fisico (Dubovsky) = sqrt(m1^2(BCP)/(2 MPl_Dub^2)), MPl_Dub^2 = MPl_red^2/2")
print("  -> m1_fis = sqrt(2) Lambda^2 / MPl_red ;  alcance Yukawa l1 = 1/m1_fis")
print()
hdr = f"{'Lambda':>10} | {'M':>9} | {'r_c=MPl/M^2':>12} | {'tau_J=1/Gamma':>13} | {'tau/edad':>9} | {'l1 (m1)':>10} | {'rho_c/rho_DE':>12}"
print(hdr); print("-"*len(hdr))
for Lam_MeV in [1e-9, 1e-3, 1.0, 3.0, 10.0, 30.0, 100.0, 1e3, 1e5]:
    Lam = Lam_MeV*1e6          # eV
    M   = 2**0.25*Lam          # eV  (escala ghost-condensate efectiva)
    r_c = MPl_red/M**2*eVinv_m           # m   (ACLM r_c ~ MPl/M^2, MPl=MPl_red)
    Gam = M**3/(4*MPl_red**2)            # eV  (alpha=1)
    tau = (1/Gam)*eVinv_s                # s
    l1  = MPl_red/(math.sqrt(2)*Lam**2)*eVinv_m   # m, alcance del Yukawa de h0i
    rho_c = M**6/MPl_red**2              # eV^4 (densidad de los grumos saturados)
    print(f"{Lam_MeV:>8.0e}MeV | {M/1e6:>6.2f}MeV | {r_c:>10.2e} m | {tau:>11.2e} s | {tau/age:>9.1e} | {l1:>8.2e} | {rho_c/rho_DE:>12.1e}")
print()

# Cotas invertidas:
# (1) Jeans lineal: tau > edad  ->  M^3 < 4 MPl^2/(edad/eVinv_s)
M_max_J = (4*MPl_red**2/(age/eVinv_s))**(1/3.)
Lam_max_J = M_max_J/2**0.25
print(f"(1) Jeans lineal tau>edad: M < {M_max_J/1e6:.1f} MeV -> Lambda < {Lam_max_J/1e6:.1f} MeV")
# (1b) friccion de Hubble eterna: Gamma < H0
M_max_H = (4*MPl_red**2*H0)**(1/3.)
print(f"(1b) Gamma < H0 (friccion de Hubble mata la inestabilidad): M < {M_max_H/1e6:.1f} MeV")
# (2) frame dragging: m1_fis * r_LAGEOS < delta  (supresion Yukawa e^-mr ~ 1-mr)
m1_max = delta_fd/(r_LAGEOS/eVinv_m)     # eV
Lam_max_fd = (m1_max*MPl_red/math.sqrt(2))**0.5
print(f"(2) frame dragging (LARES {delta_fd*100:.0f}% en r={r_LAGEOS:.1e} m): m1_fis < {m1_max:.1e} eV")
print(f"    -> Lambda < {Lam_max_fd/1e6:.1f} MeV   [deduccion PROPIA, no publicada]")
# con GP-B 19%:
m1_max19 = 0.19/(r_LAGEOS/eVinv_m)
print(f"    (con 19% GP-B: Lambda < {(m1_max19*MPl_red/math.sqrt(2))**0.5/1e6:.1f} MeV)")
# (3) esquina literal (Lambda = MPl):
M_lit = 2**0.25*MPl_red
print(f"(3) esquina literal Lambda=MPl: M = {M_lit/MPl_red:.2f} MPl -> excedida por "
      f"{math.log10(M_lit/M_max_J):.0f} ordenes (Jeans) / "
      f"{math.log10(M_lit/1e11):.0f} ordenes (twinkling 100 GeV)")
# (4) reescalamiento necesario del m0^2 de la esquina:
print(f"(4) m0^2 fisico: Lambda<10MeV -> m0^2 = Lambda^4 < {(1e7/MPl_red)**4:.1e} MPl^4"
      f"  (la esquina m0^2=1 debe reescalarse ~82 ordenes)")
# (5) masa fisica del graviton-escala (m0_Dub) y c_T:
Lam10 = 1e7
m0_fis = Lam10**2/MPl_red
print(f"(5) Lambda=10MeV: m0_fis = m1_fis/sqrt2 = {m0_fis:.1e} eV; "
      f"delta c_T ~ alpha/MPl^2 ~ (Lambda/MPl)^2 = {(Lam10/MPl_red)**2:.0e}  (GW170817 pide <1e-15: OK)")
