"""Ringdown (modos cuasinormales, aproximacion eikonal) en TCI vs RG.

Correspondencia anillo de luz <-> QNM (Cardoso et al. 2009):
  omega_QNM ~ l*Omega_c - i*(n+1/2)*lambda_L
  Omega_c  = frecuencia orbital del anillo de fotones = c/b_c
  lambda_L = exponente de Lyapunov de geodesicas nulas en el anillo

Con la ecuacion radial nula (du/dtheta)^2 = H(u) = n(u)^2/b^2 - u^2:
  en el anillo (b=b_c): H=H'=0;  kappa_theta = sqrt(H''/2);  lambda_L = kappa_theta*Omega_c
Chequeo RG conocido: lambda_L = Omega_c (kappa_theta = 1), Omega_c = c/(3*sqrt(3) GM/c^2).
Unidades GM=c=1; phi = u.
"""
import math

def n2_gr(u):  return (1+u/2)**6/(1-u/2)**2   # n^2 = B/A, Schwarzschild isotropo
def n2_tci(u): return math.exp(4*u)           # metrica exponencial (Yilmaz/TCI)

def analyze(n2, name, u_lo=1e-4, u_hi=1.2):
    # anillo de fotones: minimo de F(u) = n/u  (= n*r)
    from_golden = lambda f, a, b: _golden(f, a, b)
    F = lambda u: math.sqrt(n2(u))/u
    u_ph = _golden(F, u_lo, u_hi)
    b_c  = F(u_ph)
    eps  = 1e-5
    H    = lambda u: n2(u)/b_c**2 - u*u
    H2   = (H(u_ph+eps) - 2*H(u_ph) + H(u_ph-eps))/eps**2
    kappa = math.sqrt(H2/2)
    Om   = 1.0/b_c          # Omega_c = c/b_c
    lam  = kappa*Om
    print(f"{name:18s} u_ph={u_ph:.6f}  b_c={b_c:.6f}  Omega_c={Om:.6f}  kappa={kappa:.6f}  lambda_L={lam:.6f}")
    return b_c, Om, lam

def _golden(f, a, b, tol=1e-12):
    g = (math.sqrt(5)-1)/2
    c, d = b-g*(b-a), a+g*(b-a)
    while abs(b-a) > tol:
        if f(c) < f(d): b, d = d, c; c = b-g*(b-a)
        else:           a, c = c, d; d = a+g*(b-a)
    return 0.5*(a+b)

print("(unidades GM=c=1; RG exacto: b_c=5.196152, Omega_c=0.192450, kappa=1)")
bc_g, Om_g, lam_g = analyze(n2_gr,  "RG  Schwarzschild")
bc_t, Om_t, lam_t = analyze(n2_tci, "TCI exponencial  ")

print(f"\nfrecuencia ringdown (parte real):  TCI/RG = {Om_t/Om_g:.5f}  ({100*(Om_t/Om_g-1):+.2f} %)")
print(f"amortiguamiento (parte imaginaria): TCI/RG = {lam_t/lam_g:.5f}  ({100*(lam_t/lam_g-1):+.2f} %)")

# ejemplo fisico: remanente tipo GW150914, M ~ 62 M_sol (eikonal l=2: omega_R ~ 2*Omega_c)
Msun_s = 4.925491e-6            # GM_sol/c^3 en segundos
M = 62*Msun_s
for name, Om, lam in (("RG ", Om_g, lam_g), ("TCI", Om_t, lam_t)):
    f  = 2*Om/(2*math.pi*M)     # Hz (eikonal l=2, subestima ~15% el valor exacto; sirven los cocientes)
    tau = M/lam*1e3             # ms
    print(f"{name} remanente 62 M_sol:  f_ring ~ {f:6.1f} Hz   tau ~ {tau:.2f} ms")
