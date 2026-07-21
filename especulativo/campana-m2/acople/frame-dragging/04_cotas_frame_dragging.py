# -*- coding: utf-8 -*-
"""
COLUMNA B - paso 4: cotas numericas sobre mu = m1_fis, l1 = 1/mu y Lambda.
  Prediccion (medio relajado): Omega_LT = Omega_LT^RG * S(mu a),
    nodo:      S_node(x) = (1+x) e^-x          [x = mu a]
    giroscopo: S_gyro(x) = (1+x-x^2) e^-x      [GP-B, orbita polar]
  (correcciones declaradas: factor de forma FF(mu R)=1+ (mu R)^2/14 ~ 1.001,
   y G_eff/G = M_Pl^2/(M_Pl^2+alpha) ~ 1 + O(Lambda^4/M_Pl^4): despreciables)
  Relacion con el medio: m1^2 = 2 U_X = 2 Lambda^4 (U = Lambda^4 Uhat, Uhat_X=1),
    M_Pl^2 = 1/16 pi G = Mbar_Pl^2/2  =>  mu = 2 Lambda^2 / Mbar_Pl
    (la acta SECTOR-ESCALAR ya tenia l1 = Mbar_Pl/(2 Lambda^2): consistente)
"""
import math

# constantes
hbar_c_GeVm = 1.97327e-16      # GeV * m
Mbar_Pl_GeV = 2.4353e18        # masa de Planck reducida
G_SI = 6.674e-11; c_SI = 2.998e8; hbar_SI = 1.0546e-34
R_E = 6.371e6

# ---------- control dimensional completo (unidades fisicas restauradas) ----------
# natural: mu = 2 Lambda^2/Mbar_Pl  <->  SI: mu[1/m]^2 = 32 pi G Lambda^4/(hbar^3 c^7)
Lam_GeV = 1e-3                  # 1 MeV
mu_nat = 2 * Lam_GeV**2 / Mbar_Pl_GeV          # GeV
mu_nat_m = mu_nat / hbar_c_GeVm                # 1/m
Lam_J = Lam_GeV * 1.60218e-10                  # GeV -> J
mu_SI = math.sqrt(32 * math.pi * G_SI * Lam_J**4 / (hbar_SI**3 * c_SI**7))
print("Control dimensional (Lambda = 1 MeV):")
print(f"  mu natural = {mu_nat_m:.4e} 1/m ; mu SI (32 pi G L^4/hbar^3 c^7)^1/2 = {mu_SI:.4e} 1/m")
assert abs(mu_nat_m / mu_SI - 1) < 1e-3
print(f"  => l1(Lambda=1 MeV) = {1/mu_nat_m:.3e} m  [~ distancia Tierra-Luna 3.8e8 m]")
print(f"  escala: l1 = 2.40e8 m * (MeV/Lambda)^2 ;  mu = 4.16e-9 1/m * (Lambda/MeV)^2\n")


def bisect(fun, lo, hi, tol=1e-12):
    flo = fun(lo)
    for _ in range(200):
        mid = (lo + hi) / 2
        if fun(mid) * flo > 0:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return (lo + hi) / 2


S_node = lambda x: (1 + x) * math.exp(-x)
S_gyro = lambda x: (1 + x - x**2) * math.exp(-x)


def cota(nombre, S, eps, a):
    x_max = bisect(lambda x: (1 - S(x)) - eps, 1e-8, 5.0)
    mu_max = x_max / a                       # 1/m
    l1_min = 1 / mu_max
    mu_eV = mu_max * hbar_c_GeVm * 1e9       # eV
    Lam_MeV = math.sqrt(mu_max * hbar_c_GeVm * Mbar_Pl_GeV / 2) * 1e3
    print(f"{nombre}: eps={eps*100:.1f}% en a={a/1e3:.0f} km")
    print(f"   x_max = mu*a = {x_max:.4f}   [1-S ~ x^2/2: sin termino lineal en mu]")
    print(f"   mu = m1_fis  < {mu_max:.3e} 1/m  =  {mu_eV:.2e} eV")
    print(f"   l1 = 1/mu    > {l1_min:.3e} m  = {l1_min/R_E:.1f} R_Tierra")
    print(f"   Lambda       < {Lam_MeV:.2f} MeV")
    ffy = mu_max * R_E
    print(f"   [control: FF(mu R_E)-1 = {(ffy**2/14):.1e} -> despreciable]\n")
    return x_max, mu_max, Lam_MeV


print("== COTAS (prediccion nodal S_node, giroscopo S_gyro) ==")
a_LAG = 1.227e7; a_GPB = 7.027e6; a_L2 = 1.227e7
r5 = cota("LAGEOS/LARES conservador", S_node, 0.05, a_LAG)
r2 = cota("LAGEOS/LARES Ciufolini-2019", S_node, 0.02, a_LAG)
rg = cota("GP-B", S_gyro, 0.19, a_GPB)
rl2 = cota("LARES-2 (proyeccion)", S_node, 0.002, a_L2)

# ---------- comparacion con la deduccion previa de la campana ----------
print("== correccion a la cota previa de la campana ==")
eps = 0.05
mu_prev = eps / a_LAG
Lam_prev = math.sqrt(mu_prev * hbar_c_GeVm * Mbar_Pl_GeV / 2) * 1e3
print(f"criterio previo (e^-x ~ 1-x, x_max=eps): mu < {mu_prev:.2e} 1/m -> Lambda < {Lam_prev:.2f} MeV")
print(f"criterio correcto (S_node, x_max={r5[0]:.3f}): Lambda < {r5[2]:.2f} MeV")
print(f"=> la cota previa 1.0 MeV era {r5[2]/Lam_prev:.1f}x demasiado FUERTE: el dipolo")
print("   Yukawa (1+x)e^-x no tiene termino lineal; la desviacion nodal es x^2/2.\n")

# ---------- que mejora LARES-2 ----------
print("== LARES-2 ==")
print(f"mu: {r2[1]/rl2[1]:.1f}x mejor que 2% actual ({r5[1]/rl2[1]:.1f}x vs 5%)")
print(f"Lambda: {r2[2]:.2f} -> {rl2[2]:.2f} MeV ({r2[2]/rl2[2]:.2f}x)")
print(f"escala general: x_max ~ sqrt(2 eps) => mu ~ eps^(1/2), Lambda ~ eps^(1/4)")

# ---------- controles finales ----------
print("\n== controles ==")
print(f"m1->0: S_node(0) = {S_node(0):.1f} (RG exacto);  "
      f"r<<l1: 1-S_node(0.01) = {1-S_node(0.01):.1e} ~ x^2/2 = {0.01**2/2:.1e}")
imp = 1 - S_node(1.227e7 / 2.402e8)
print(f"si Lambda = 1 MeV: x_LAGEOS = {1.227e7/2.402e8:.4f} -> desviacion nodal {imp*100:.2f}%"
      f" (bajo el 2% actual: consistente)")
