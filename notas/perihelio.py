"""Precesion del perihelio de Mercurio en TCI: verificacion numerica.

Integra la geodesica ecuatorial en una metrica isotropa estatica
  ds^2 = A(r) c^2 dt^2 - B(r) (dr^2 + r^2 dtheta^2)
con B = 1 + 2*phi (gamma_PPN = 1, fijado por la luz en la seccion 7.4) y
cuatro candidatos para A (el sector temporal):

  1. exp(-2*phi),          sigma=0   -> beta_PPN = 1    (equivalencia local + estatica lineal)
  2. (1-phi)^2                       -> beta_PPN = 1/2  (acoplamiento lineal, ec. 43-48 del paper)
  3. exp(-2*(phi+phi^2)),  sigma=+1  -> beta_PPN = 0    (no linealidad en el sector espacial, F=1-4phi)
  4. exp(-2*(phi-phi^2)),  sigma=-1  -> beta_PPN = 2    (signo opuesto)

Metodo: ecuacion de la orbita u(theta), u=1/r, con
  (du/dtheta)^2 = G(u) = B*(e^2/A - 1)/l^2 - u^2,   u'' = G'(u)/2
e^2/A - 1 se evalua como expm1(lambda - lnA) para evitar cancelacion catastrofica.
e^2, l^2 se fijan exigiendo puntos de retorno en r_p = a(1-e), r_a = a(1+e).
Perihelios detectados por ajuste parabolico en los maximos de u(theta);
precesion = pendiente del ajuste lineal theta_n vs n, menos 2*pi.
Unidades: r en unidades de a (semieje), c = 1.
"""
import math

GM   = 1.32712440018e20   # m^3/s^2 (Sol)
c    = 2.99792458e8       # m/s
a_m  = 5.790905e10        # m, semieje mayor de Mercurio
ecc  = 0.205630
P_d  = 87.9691            # dias, periodo orbital
orbits_century = 36525.0 / P_d
RAD2AS = 180/math.pi*3600

m = GM/(a_m*c*c)          # GM/(a c^2) adimensional (r en unidades de a)
u_p, u_a = 1/(1-ecc), 1/(1+ecc)

def make_metric(mode, sigma=0.0):
    if mode == 'exp':
        def lnA(u):  return -2*(m*u + sigma*(m*u)**2)
        def dlnA(u): return -2*m - 4*sigma*m*m*u
    elif mode == 'old':   # A = (1 - m u)^2
        def lnA(u):  return 2*math.log1p(-m*u)
        def dlnA(u): return -2*m/(1 - m*u)
    def B(u):  return 1 + 2*m*u
    def dB(u): return 2*m
    return lnA, dlnA, B, dB

def conserved(lnA, B):
    # X/A - Y u^2/B = 1 en u_p y u_a  ->  resolver X=e^2, Y=l^2
    a11, a12 = math.exp(-lnA(u_p)), -u_p*u_p/B(u_p)
    a21, a22 = math.exp(-lnA(u_a)), -u_a*u_a/B(u_a)
    det = a11*a22 - a12*a21
    X = (a22 - a12)/det
    Y = (a11 - a21)/det
    return math.log(X), Y   # lambda = ln(e^2), l^2

def run(mode, sigma=0.0, n_orbits=100, steps_per_orbit=3000):
    lnA, dlnA, B, dB = make_metric(mode, sigma)
    lam, Y = conserved(lnA, B)
    def ddu(u):  # u'' = G'(u)/2
        t = lam - lnA(u)
        return 0.5*((dB(u)*math.expm1(t) - B(u)*math.exp(t)*dlnA(u))/Y - 2*u)
    h = 2*math.pi/steps_per_orbit
    u, w, th = u_p, 0.0, 0.0
    prev = []   # ventana (theta, u) para deteccion de maximos
    peri = []
    for k in range(n_orbits*steps_per_orbit):
        # RK4 para u''=ddu(u)
        k1u, k1w = w, ddu(u)
        k2u, k2w = w + 0.5*h*k1w, ddu(u + 0.5*h*k1u)
        k3u, k3w = w + 0.5*h*k2w, ddu(u + 0.5*h*k2u)
        k4u, k4w = w + h*k3w,     ddu(u + h*k3u)
        u  += h*(k1u + 2*k2u + 2*k3u + k4u)/6
        w  += h*(k1w + 2*k2w + 2*k3w + k4w)/6
        th += h
        prev.append((th, u))
        if len(prev) > 3: prev.pop(0)
        if len(prev) == 3 and prev[0][1] < prev[1][1] > prev[2][1] and th > 1.0:
            (t0,y0),(t1,y1),(t2,y2) = prev
            d = (y0 - 2*y1 + y2)
            peri.append(t1 - 0.5*h*(y2 - y0)/d)   # vertice de la parabola
    # ajuste lineal theta_n = alpha + slope*n
    n = len(peri); xs = range(n)
    xm = sum(xs)/n; ym = sum(peri)/n
    slope = sum((x-xm)*(y-ym) for x, y in zip(xs, peri))/sum((x-xm)**2 for x in xs)
    dw = slope - 2*math.pi                    # rad/orbita
    return dw*orbits_century*RAD2AS           # arcsec/siglo

newt = 6*math.pi*m/(1-ecc**2)                 # 6 pi GM/(a(1-e^2)c^2), rad/orbita
gr_th = newt*orbits_century*RAD2AS
print(f"GM/(a c^2) = {m:.6e}   |   formula PPN: [(2+2g-b)/3] * {gr_th:.3f}\"/siglo (con g=b=1)")
print()
cases = [
    ("A=exp(-2phi)          sigma= 0  (beta=1)  ", 'exp',  0.0, 1.0),
    ("A=(1-phi)^2           ec.(43)   (beta=1/2)", 'old',  0.0, 0.5),
    ("A=exp(-2(phi+phi^2))  sigma=+1  (beta=0)  ", 'exp', +1.0, 0.0),
    ("A=exp(-2(phi-phi^2))  sigma=-1  (beta=2)  ", 'exp', -1.0, 2.0),
]
print(f"{'metrica':47s} {'numerico':>12s} {'PPN teorico':>12s}")
for label, mode, sigma, beta in cases:
    num = run(mode, sigma)
    th  = (2+2*1-beta)/3*gr_th
    print(f"{label:47s} {num:10.2f}\"  {th:10.2f}\"")
print(f"\nObservado: 42.98 +/- 0.04 \"/siglo")
