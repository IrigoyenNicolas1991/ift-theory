# -*- coding: utf-8 -*-
"""
v4b_escalar_frw_analisis.py — Tarea 4, parte B: analisis del determinante
escalar 4x4 congelado sobre FRW (esquina sana c10=1, c01=2, c20=1, resto 0).

Preguntas del mandato:
 (1) p >> H: hay modo propagante nuevo a LO? su c_s^2?
 (2) la friccion de Hubble modifica la conclusion "congelado"?
 (3) criterio D3: inestabilidad RAPIDA nueva en la esquina sana?

Metodo: det(om,k;H) del sistema congelado (v4 parte A, validado en Minkowski
contra el resultado de la campana), sobre la superficie on-shell del fondo:
 - atractor perturbado: w = 1+delta, 3H^2 = rho(1+delta) (esquina: rho ~ 2 delta)
 - fondo generico w0 lejos del atractor con 3H^2 = rho(w0), raices numericas.
Convencion temporal: e^{i om t} => INESTABLE si Im(om) < 0.
"""
import pickle, os, math
import sympy as sp

outdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(outdir, "v4_matriz_congelada.pkl"), "rb") as fh:
    dat = pickle.load(fh)
M = dat["M"]
as_, Hs, ws, k, om, c00, c10, c01, c20, c11, c02 = dat["syms"]

esquina = {c00: 0, c10: 1, c01: 2, c20: 1, c11: 0, c02: 0}
Me = M.subs(esquina, simultaneous=True)

# el factor de escala solo debe aparecer como k/a (k comovil): fijo a=1 y
# declaro k FISICO. Chequeo: det(a,k) == det(1, k->k/a) * a^n para algun n.
det_a = sp.expand(sp.simplify(Me.det()))
det_1 = det_a.subs(as_, 1)
n_ = sp.Symbol('n_')
print("=" * 72)
print("chequeo: a_s entra solo via k/a_s (k comovil)?")
print("=" * 72)
cand = sp.simplify(det_a/det_1.subs(k, k/as_))
print(f"  det(a)/det(1, k->k/a) = {sp.factor(cand)}   [debe ser potencia pura de a_s]")
ok_a = not sp.simplify(cand).has(k, om, Hs, ws)
print(f"  {'OK: potencia pura' if ok_a else 'ATENCION: no factoriza — revisar'}")
det = sp.expand(det_1)

# ---------- fondo de la esquina ----------
w_ = sp.Symbol('w', real=True)
U_ = (1 - w_**2 + 1) - 1 + 2*(w_ - 1) + (1 - w_**2)**2/2   # U(X=-w^2,Y=w), (X+1)=1-w^2
U_ = sp.expand((1 - w_**2) + 2*(w_ - 1) + (1 - w_**2)**2/2)
UX_ = 1 + (1 - w_**2)
rho_ = sp.expand(-U_ - 2*w_**2*UX_ + 2*w_)
print(f"\n  rho(w) esquina = {rho_}   [rho(1)=0, drho/dw(1)={sp.diff(rho_, w_).subs(w_, 1)}]")

print()
print("=" * 72)
print("(A) atractor perturbado: w = 1+d, 3H^2 = rho(1+d);  d ~ (3/2)H^2")
print("=" * 72)
d = sp.Symbol('delta', positive=True)
rho_d = sp.expand(rho_.subs(w_, 1 + d))
# invierto 3H^2 = rho(1+d) a orden d^2: d = (3/2)H^2 + O(H^4)
dd = sp.solve(sp.Eq(3*Hs**2, sp.expand(rho_d + sp.O(d**2)).removeO()), d)[0]
print(f"  a orden lineal: delta = {dd}")
det_d = det.subs(ws, 1 + d, simultaneous=True)
det_d = sp.expand(det_d.subs(d, dd, simultaneous=True))
serie = sp.expand(det_d + sp.O(Hs**3)).removeO()
serie = sp.collect(sp.expand(serie), Hs)
print("  det = sum_j H^j * D_j(om,k) hasta O(H^2):")
for j in range(3):
    Dj = sp.expand(serie.coeff(Hs, j))
    Djc = sp.collect(Dj, om)
    print(f"   D_{j} = {sp.factor(Djc) if Dj != 0 else 0}")

# los ceros perturbados del cero doble: om^2 = candidatos ~ O(H, Hk, H^2):
# resolver det=0 en el regimen om ~ H << k: escaleo om = H*x, k fijo, orden H^4-dominante
xx = sp.Symbol('x')
det_scaled = sp.expand(serie.subs(om, Hs*xx))
# el termino dominante en H para k fijo:
pw = sp.Poly(det_scaled, Hs)
grados = pw.monoms()
min_g = min(g[0] for g in grados)
lead = sp.expand(det_scaled.coeff(Hs, min_g))
print(f"\n  escaleo om = H x (regimen om ~ H << k): orden dominante H^{min_g}:")
print(f"   coef = {sp.factor(sp.collect(lead, xx))}")
sols = sp.solve(sp.Eq(lead, 0), xx)
print(f"   raices x = om/H: {sols}")

print()
print("=" * 72)
print("(B) fondo generico lejos del atractor: raices numericas de det(om)")
print("=" * 72)
import numpy as np
rhoN = sp.lambdify(w_, rho_, "math")

def raices_num(w0, kval):
    r0 = rhoN(w0)
    if r0 < 0:
        return None, None
    Hv = math.sqrt(r0/3.0)
    pol = sp.Poly(sp.expand(det.subs({ws: w0, Hs: Hv, k: kval}, simultaneous=True)), om)
    cs = [complex(c) for c in pol.all_coeffs()]
    rr = np.roots(cs)
    return Hv, sorted(rr, key=lambda r_: abs(r_))

# nota EFT: en unidades Lambda=1 (las de la esquina), el LO U(X,Y) vale para
# p < Lambda = 1 (los NLO p^4 dominan arriba, SECTOR-ESCALAR). H fija el piso
# del regimen congelado. Barrido: tasa de crecimiento maxima vs k y vs delta.
print("  tabla: peor tasa de crecimiento  Gamma = max(-Im om)  [CRECE si > 0]")
print("  (regimen congelado valido si |om| >> H; ventana EFT: k <= 1)")
print(f"  {'w0':>5} {'H':>7} | " + " ".join(f"k={kk:<7g}" for kk in (0.3, 0.6, 1.0, 2.0, 5.0, 20.0, 50.0)))
for w0 in (1.02, 1.05, 1.1, 1.2, 1.4, 0.5, 0.9):
    fila = []
    Hv0 = None
    for kk in (0.3, 0.6, 1.0, 2.0, 5.0, 20.0, 50.0):
        Hv, rr = raices_num(w0, kk)
        if Hv is None:
            fila.append("rho<0!")
            continue
        Hv0 = Hv
        peor = max((-r_.imag) for r_ in rr)
        fila.append(f"{peor:+.3f} " if peor > 1e-9 else " est.  ")
    Htxt = f"{Hv0:.3f}" if Hv0 else "  -  "
    print(f"  {w0:>5} {Htxt:>7} | " + " ".join(f"{s:<9s}" for s in fila))
print("  ('est.' = todas las raices decaen o son cero)")

# escalamiento de la inestabilidad UV (fuera de ventana EFT): tasa vs k
print()
print("  escalamiento de la tasa con k en w0=1.2 (diagnostico: gradiente vs masa):")
for kk in (10.0, 20.0, 40.0, 80.0, 160.0):
    Hv, rr = raices_num(1.2, kk)
    peor = max((-r_.imag) for r_ in rr)
    print(f"    k={kk:6.1f}: Gamma = {peor:+.4f}   Gamma/k = {peor/kk:+.5f}")

# escalamiento con delta a k fijo dentro de la ventana EFT
print()
print("  escalamiento con delta = w0-1 a k=1.0 (borde EFT) y k=0.6:")
for w0 in (1.02, 1.05, 1.1, 1.2, 1.3, 1.4):
    for kk in (0.6, 1.0):
        Hv, rr = raices_num(w0, kk)
        peor = max((-r_.imag) for r_ in rr)
        est = "estable" if peor < 1e-9 else f"Gamma={peor:+.4f} (= {peor/Hv:.2f} H)"
        print(f"    w0={w0:5.2f} k={kk:3.1f}: H={Hv:.3f}  {est}")

# cuantos ceros om=0 EXACTOS persisten sobre el fondo on-shell completo?
print()
print("  ceros om=0 exactos en el fondo completo (coefs om^0, om^1 del det):")
for w0, kk in ((1.2, 0.7), (1.4, 5.0), (0.5, 1.0)):
    Hv = math.sqrt(rhoN(w0)/3.0)
    pol = sp.Poly(sp.expand(det.subs({ws: w0, Hs: Hv, k: kk}, simultaneous=True)), om)
    cs = [abs(complex(c)) for c in pol.all_coeffs()]
    top = max(cs)
    c0 = cs[-1]/top; c1 = cs[-2]/top if len(cs) > 1 else 0.0
    diag = ("UN cero om=0 EXACTO (simple); el companero del doblete se desplaza"
            if c0 < 1e-12 and c1 > 1e-12 else
            ("cero DOBLE exacto" if max(c0, c1) < 1e-12 else "sin cero exacto"))
    print(f"    w0={w0}, k={kk}: |c(om^0)|/max = {c0:.2e}, |c(om^1)|/max = {c1:.2e} -> {diag}")
print("  (el companero desplazado es la raiz imaginaria PURA de las tablas de")
print("   arriba: +2.6i, +6.9i, ... en la rama w>1: DECAE — estable)")

print()
print("=" * 72)
print("CONCLUSIONES TAREA 4 (con limites de validez declarados)")
print("=" * 72)
print("""  1. Sobre el ATRACTOR (w=1+delta, delta=(3/2)H^2, la cosmologia natural):
     det = om^2 k^3 [ -8i om^2 - 48 H om + 4i H^2(k^2+18-27 om^2) ] + O(H^3)
     - de los 4 ceros om=0 de Minkowski: UNO persiste EXACTO sobre el fondo
       completo (c(om^0)=0 a precision float: la simetria residual sobrevive);
       otro se desplaza a una frecuencia imaginaria PURA que decae (+2.6i en
       w0=1.2); la factorizacion om^2 de arriba es exacta solo a O(H^2).
     - el par roto: om = +-(H/sqrt2) k + 3iH  =>  "modo" con velocidad de fase
       c = H/sqrt2 -> 0 en Minkowski, y decaimiento a^-3 (el 3H es EXACTAMENTE
       el dust de F5). NO es un modo propagante con c_s^2 = O(1): es la
       respuesta a escala Hubble del fluido-polvo del medio. En p >> H no
       aparece NADA nuevo con om ~ k: el sector sigue congelado a LO.
     - friccion de Hubble: desplaza los ceros a om ~ H (D_1 = -48 k^3 om^3 H),
       no los abre a om ~ k. Conclusion "congelado": SE MANTIENE, degradada
       suavemente a "dinamica de escala Hubble".
  2. Fuera del atractor, rama w>1 (transitorio dust): ESTABLE para todo
     k <= 5 Lambda barrido; crecimiento solo a k >= 20 Lambda con tasa ~ 0.07k
     (gradiente): FUERA del dominio EFT del LO (alli mandan los NLO p^4 ya
     estudiados sobre Minkowski). La tasa -> 0 cuando delta -> 0.
  3. Cuenca AdS (w < 1/sqrt3): crecimiento DENTRO de la ventana EFT pero con
     tasa <= 0.5 H (Jeans-like, lenta en unidades Hubble), sobre un fondo que
     de todos modos recolapsa (V3). No es "inestabilidad rapida".
  4. LIMITES: coeficientes congelados (WKB local): cuantitativo para |om|>>H,
     indicativo para |om| ~ H; la U es la cuadratica general (basta para LO
     alrededor del atractor); k // z sin perdida (SVT + isotropia).""")
