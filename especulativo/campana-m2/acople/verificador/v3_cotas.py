# Verificador adversarial - auditoria aritmetica de las cotas LT con unidades explicitas.
import math

def brentq(fun, lo, hi, tol=1e-14):
    flo = fun(lo)
    for _ in range(200):
        mid = 0.5*(lo + hi)
        fm = fun(mid)
        if flo*fm <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
        if hi - lo < tol:
            break
    return 0.5*(lo + hi)

# constantes SI / conversion
G = 6.674e-11          # m^3 kg^-1 s^-2
cl = 2.99792458e8      # m/s
hbar = 1.054571817e-34 # J s
hbarc_eVm = 1.973269804e-7   # eV*m
hbarc_GeVm = 1.973269804e-16 # GeV*m
Mred = 2.435e18        # GeV (M_Pl reducida)
Re = 6.371e6           # m
yr = 3.156e7           # s
mas = 1000*180*3600/math.pi  # mas por radian

# --- criterios de cota ---
S_nodo = lambda x: (1 + x)*math.exp(-x)
S_gpb = lambda x: (1 + x - x**2)*math.exp(-x)

def cota(nombre, Sfun, eps, a_m):
    xmax = brentq(lambda x: Sfun(x) - (1 - eps), 1e-9, 5)
    mu = xmax/a_m                     # 1/m
    m_eV = mu*hbarc_eVm               # eV
    ell = 1/mu                        # m
    mu_GeV = mu*hbarc_GeVm            # GeV
    Lam_GeV = math.sqrt(mu_GeV*Mred/2)   # mu = 2 Lam^2/Mred
    print(f"{nombre}: eps={eps} -> x_max={xmax:.4f}  m1_fis<{mu:.3g} m^-1 = {m_eV:.3g} eV"
          f"  ell1>{ell:.3g} m ({ell/Re:.1f} R_E)  Lam<{Lam_GeV*1e3:.3g} MeV")
    return xmax, mu

a_lageos = 1.227e7
a_gpb = 7.027e6
print("== cotas (criterio nodal (1+x)e^-x, GP-B (1+x-x^2)e^-x) ==")
cota("LAGEOS 5%  ", S_nodo, 0.05, a_lageos)
cota("LAGEOS 2%  ", S_nodo, 0.02, a_lageos)
cota("GP-B 19%   ", S_gpb, 0.19, a_gpb)
cota("LARES-2 .2%", S_nodo, 0.002, a_lageos)

print("\n== criterio viejo (lineal, e^-x ~ 1-x => x_max = eps): factor de debilitamiento ==")
x5 = brentq(lambda x: S_nodo(x) - 0.95, 1e-9, 5)
print(f"5%: x_max nuevo/viejo = {x5/0.05:.2f} (claim ~7x en mu, ~{math.sqrt(x5/0.05):.2f}x en Lam)")

print("\n== escala ell_1 = 1/mu = Mred/(2 Lam^2) ==")
for LamMeV in (1.0, 2.05, 2.6):
    Lam = LamMeV*1e-3
    mu_GeV = 2*Lam**2/Mred
    ell = hbarc_GeVm/mu_GeV
    print(f"Lam={LamMeV} MeV: ell1 = {ell:.3g} m ({ell/Re:.1f} R_E)")

print("\n== control dimensional SI: mu^2 = 32 pi G Lam^4/(hbar^3 c^7) ==")
Lam_J = 1e6*1.602176634e-19   # 1 MeV en J
mu2_SI = 32*math.pi*G*Lam_J**4/(hbar**3*cl**7)
mu_SI = math.sqrt(mu2_SI)
mu_nat = 2*(1e-3)**2/Mred/hbarc_GeVm   # 1/m
print(f"mu(1 MeV): SI={mu_SI:.4g} 1/m  natural={mu_nat:.4g} 1/m  ratio={mu_SI/mu_nat:.4f}")
print(f"ell1(1 MeV) = {1/mu_SI:.4g} m (claim 2.40e8 m)")

print("\n== numeros RG de literatura ==")
J_E = 5.86e33  # kg m^2/s
Om_lageos = 2*G*J_E/(cl**2*a_lageos**3)
print(f"nodo LAGEOS: {Om_lageos*yr*mas:.1f} mas/yr (lit 30.7)")
Om_gpb = G*J_E/(2*cl**2*a_gpb**3)
print(f"GP-B: {Om_gpb*yr*mas:.1f} mas/yr (publicado 39.2; claim propio 40.8)")

print("\n== desviacion a Lam=1 MeV en LAGEOS ==")
mu1 = 2*(1e-3)**2/Mred/hbarc_GeVm
x1 = mu1*a_lageos
print(f"x = {x1:.4f}; 1 - S_nodo = {1 - S_nodo(x1):.2%} (claim 0.13%)")

print("\n== factor de forma de la Tierra en la zona de cotas ==")
FF = lambda y: 15*((y*y + 3)*math.sinh(y) - 3*y*math.cosh(y))/y**5
for xm, aa in ((0.355, a_lageos), (0.215, a_lageos)):
    y = xm*Re/aa
    print(f"x={xm}: mu R_E = {y:.4f}  FF-1 = {FF(y)-1:.2e} (claim <3e-3)")

print("\n== r_c y t_c del escalar (Lam=10 MeV, kappa~Lam^2) ==")
Mp2 = Mred**2/2
Lam = 10e-3
m02 = 2*Lam**4/2   # M^4 = 2 m0^2 con M = ~Lam: uso m0^2 = Lam^4 (normalizacion Uhat=1)
rc = math.sqrt(2)*math.sqrt(Mp2)/math.sqrt(m02)*hbarc_GeVm
kap = Lam**2
tc = 4*Mp2/(math.sqrt(kap)*math.sqrt(m02))*6.582e-25
age = 4.35e17
print(f"r_c = {rc:.3g} m (claim ~5e3 km*(10MeV/Lam)^2 => 5e6 m); t_c = {tc:.3g} s = {tc/age:.1f} edades (claim ~18)")
