"""Campo fuerte en TCI vs Relatividad General: sombra y ISCO.

Metricas isotropas ds^2 = A(r) dt^2 - B(r)(dr^2 + r^2 dOmega^2), c=G=M=1 (phi = 1/r):

  GR (Schwarzschild isotropo):  A = ((1-1/2r)/(1+1/2r))^2,  B = (1+1/2r)^4
  TCI (completacion exponencial, = metrica de Yilmaz 1958):
                                A = exp(-2/r),              B = exp(+2/r)

Ambas coinciden hasta O(phi^2) inclusive (todo el sistema solar); difieren a O(phi^3).

Calcula:
  1. Esfera de fotones y parametro de impacto critico b_c (sombra):
     minimo de F(r) = n(r)*r, n = sqrt(B/A)  [Fermat en coordenadas isotropas]
     + verificacion independiente integrando rayos nulos (biseccion en captura).
  2. ISCO: minimo de L^2(r) para orbitas circulares masivas; frecuencia orbital
     Omega = A*L/(e*B*r^2). Chequeo GR: b_c = 3*sqrt(3) = 5.19615, r_isco(Schw) = 6,
     GM*Omega_isco/c^3 = 6^(-1.5) = 0.0680414.
"""
import math

def gr():
    A  = lambda r: ((1-0.5/r)/(1+0.5/r))**2
    B  = lambda r: (1+0.5/r)**4
    return A, B, 'GR  (Schwarzschild)'

def tci():
    A  = lambda r: math.exp(-2/r)
    B  = lambda r: math.exp(2/r)
    return A, B, 'TCI (exponencial)  '

def golden_min(f, a, b, tol=1e-12):
    g = (math.sqrt(5)-1)/2
    c, d = b-g*(b-a), a+g*(b-a)
    while abs(b-a) > tol:
        if f(c) < f(d): b, d = d, c; c = b-g*(b-a)
        else:           a, c = c, d; d = a+g*(b-a)
    return 0.5*(a+b)

def shadow(A, B, r_lo=0.55, r_hi=20.0):
    n  = lambda r: math.sqrt(B(r)/A(r))
    F  = lambda r: n(r)*r
    rp = golden_min(F, r_lo, r_hi)
    return rp, F(rp)

def captured(A, B, b, r0=500.0):
    # rayo nulo: (du/dth)^2 = n(u)^2/b^2 - u^2 ; integra hacia adentro
    n2 = lambda u: B(1/u)/A(1/u)
    u, w = 1/r0, None
    w = math.sqrt(max(n2(u)/b**2 - u*u, 0))
    h = 1e-3
    for _ in range(2_000_000):
        # RK4 sobre u' = w, w' = d/du[n^2/b^2 - u^2]/2 = (n2'(u)/b^2)/2 - u
        def dw(u_):
            eps = 1e-7*max(u_,1e-9)
            d = (n2(u_+eps)-n2(u_-eps))/(2*eps)
            return 0.5*d/b**2 - u_
        k1u, k1w = w, dw(u)
        k2u, k2w = w+0.5*h*k1w, dw(u+0.5*h*k1u)
        k3u, k3w = w+0.5*h*k2w, dw(u+0.5*h*k2u)
        k4u, k4w = w+h*k3w,     dw(u+h*k3u)
        u += h*(k1u+2*k2u+2*k3u+k4u)/6
        w += h*(k1w+2*k2w+2*k3w+k4w)/6
        if u > 1/0.52:  return True    # llego muy adentro: capturado
        if w < 0:       return False   # punto de giro: escapa
    return True

def bc_by_rays(A, B, lo=4.0, hi=7.0):
    for _ in range(45):
        mid = 0.5*(lo+hi)
        if captured(A, B, mid): lo = mid
        else:                   hi = mid
    return 0.5*(lo+hi)

def isco(A, B, r_lo=0.9, r_hi=30.0):
    def L2(r):
        eps = 1e-6*r
        Ap = (A(r+eps)-A(r-eps))/(2*eps)
        f  = lambda rr: 1/(B(rr)*rr*rr)
        fp = (f(r+eps)-f(r-eps))/(2*eps)
        den = A(r)*fp + Ap*f(r)
        return -Ap/den if den != 0 else float('inf')
    r_i = golden_min(lambda r: L2(r) if L2(r) > 0 else 1e9, r_lo, r_hi, tol=1e-10)
    l   = math.sqrt(L2(r_i))
    e   = math.sqrt(A(r_i)*(1 + L2(r_i)/(B(r_i)*r_i*r_i)))
    Om  = A(r_i)*l/(e*B(r_i)*r_i*r_i)
    return r_i, Om

print(f"{'metrica':22s} {'r_fot(iso)':>10s} {'b_c (min F)':>12s} {'b_c (rayos)':>12s} {'r_isco(iso)':>12s} {'GM*Om/c^3':>12s}")
res = {}
for make in (gr, tci):
    A, B, name = make()
    rp, bc = shadow(A, B)
    bc_r   = bc_by_rays(A, B)
    ri, Om = isco(A, B)
    res[name] = (bc, Om)
    print(f"{name:22s} {rp:10.5f} {bc:12.6f} {bc_r:12.6f} {ri:12.6f} {Om:12.7f}")

bc_gr, Om_gr = res['GR  (Schwarzschild)']; bc_t, Om_t = res['TCI (exponencial)  ']
print(f"\nreferencias exactas GR: b_c = 3*sqrt(3) = {3*math.sqrt(3):.6f} | GM*Om_isco/c^3 = 6^-1.5 = {6**-1.5:.7f}")
print(f"TCI analitico: r_fot = 2 (iso), b_c = 2e = {2*math.e:.6f}")
print(f"\nSOMBRA:  TCI/GR = {bc_t/bc_gr:.5f}  ->  {100*(bc_t/bc_gr-1):+.2f} %")
print(f"ISCO Om: TCI/GR = {Om_t/Om_gr:.5f}  ->  {100*(Om_t/Om_gr-1):+.2f} %")
