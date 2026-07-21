# Paso 5: auditoria aritmetica de las cotas fenomenologicas (unidades restauradas).
import math

GeV_s = 6.582e-25        # 1 GeV^-1 en s
GeV_m = 1.9733e-16       # 1 GeV^-1 en m
Mred = 2.435e18          # M_Pl reducida GeV (1/8piG)^(1/2)
Mp2 = Mred**2/2          # nuestro Mp^2 = 1/16piG en GeV^2
H0 = 1.5e-42             # GeV
age = 4.35e17            # s

print("== dispersion: maximo de |w| y p_J (formulas verificadas simbolicamente en paso 2) ==")
# w2 = -(|k|/2Mp2)p^2 + (|k|/m02)p^4 ; max en p2=m02/(4Mp2), |w|max = sqrt(|k| m02)/(4 Mp2); p_J^2 = m02/(2Mp2)

for Lam_MeV in [10.0, 1.0, 100.0]:
    Lam = Lam_MeV*1e-3   # GeV
    m02 = Lam**4         # GeV^4 (esquina reescalada, U=Lam^4 Uhat, U_X=1 -> m0^2=Lam^4 aprox)
    kap = Lam**2         # |kappa| ~ Lam^2 (naturalidad tipo ghost condensate, igual que ACLM)
    Gam = math.sqrt(kap*m02)/(4*Mp2)          # GeV
    tau = (1/Gam)*GeV_s
    pJ = math.sqrt(m02/(2*Mp2))               # GeV
    lJ = (1/pJ)*GeV_m
    print(f"Lam={Lam_MeV} MeV: Gamma={Gam:.2e} GeV, tau={tau:.2e} s = {tau/age:.1f} edades; 1/p_J={lJ:.2e} m")

print("\n== cota 1: m0^2 en unidades M_Pl^4 para M=10 MeV (M^4=2 m0^2) ==")
M = 10e-3
print("m0^2 =", (M**4/2)/Mred**4, "M_red^4  (claim ~3e-82: mismo orden)")

print("\n== cota 5: Gamma < H0 ==")
# Gamma = alpha M^3/(4 M_ACLM^2), M_ACLM^2 = 2*Mp2 = Mred^2
M5 = (4*Mred**2*H0)**(1/3)
print("M_max =", M5*1e3, "MeV (claim 32-33 MeV)")

print("\n== cota 3: frame dragging (LARES 5% a r=1.2e7 m) ==")
r = 1.2e7
m1max_eV = 0.05*(GeV_m*1e9)/r    # 0.05/r en eV (hbar*c = 1.97e-7 eV m)
print("m1_fis_max =", m1max_eV, "eV (claim 8e-16)")
# CORRECTO segun NUESTRA reduccion vectorial (polo (Mp2+al)p^2 + m1^2): m1_fis^2 = m1B^2/Mp2
# esquina reescalada: m1B^2 = 2 U_X Lam^4 = 2 Lam^4  =>  m1_fis = sqrt(2) Lam^2/Mp = 2 Lam^2/Mred
m1max = m1max_eV*1e-9  # GeV
Lam_ok = math.sqrt(m1max*Mred/2)
Lam_fen = math.sqrt(m1max*Mred/math.sqrt(2))   # formula del fenomenologo: m1 = sqrt(2) Lam^2/Mred
print("Lam_max correcto (m1=2Lam^2/Mred):", Lam_ok*1e3, "MeV ; fenomenologo (sqrt2):", Lam_fen*1e3, "MeV")

print("\n== c_T con NLO ==")
Lam = 10e-3; al = Lam**2
print("delta c_T ~ alpha/(2 Mp2) =", al/(2*Mp2), " (claim ~1e-41)")

print("\n== densidad de grumos vs energia oscura (Lam=10MeV) ==")
M = 2**0.25*10e-3
rho_c = M**6/Mred**2
rho_DE = (2.3e-12)**4   # (2.3 meV)^4 en GeV^4
print("rho_c/rho_DE =", rho_c/rho_DE, " (claim ~1%)")
