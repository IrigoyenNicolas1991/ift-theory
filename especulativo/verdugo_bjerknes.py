# -*- coding: utf-8 -*-
# VERDUGO DE LAS RENDIJAS - calculos contra Bjerknes dinamico
import numpy as np
import sympy as sp

print("=" * 70)
print("(A) Primer cero de cos x + x sin x  (alcance espacial de la atraccion)")
x = sp.symbols('x', positive=True)
f = sp.cos(x) + x * sp.sin(x)
x0 = sp.nsolve(f, x, 2.8)
frac = float(x0 / (2 * sp.pi))
print(f"    x* = {float(x0):.6f}   ->   r*/lambda = {frac:.6f}")
print(f"    (la atraccion de signo fijo solo vale hasta r = {frac:.3f} lambda)")

print("=" * 70)
print("(B) Promedio sin drive: fases independientes uniformes")
t, w, p1, p2 = sp.symbols('t w phi1 phi2', real=True, positive=True)
expr = sp.sin(w * t + p1) * sp.sin(w * t + p2)
avg_t = sp.simplify(sp.integrate(expr, (t, 0, 2 * sp.pi / w)) * w / (2 * sp.pi))
print(f"    promedio temporal <sin sin> = {avg_t}")
avg_phase = sp.simplify(sp.integrate(avg_t, (p1, 0, 2 * sp.pi)) / (2 * sp.pi))
print(f"    promediado sobre fase independiente uniforme = {avg_phase}")
print("    => sin drive comun, la fuerza media de Bjerknes es EXACTAMENTE cero.")

print("=" * 70)
print("(C) Fuerza instantanea (drive lento, observacion rapida)")
V0, A1, A2, phi = sp.symbols('V0 A1 A2 phi', positive=True)
V1 = V0 + A1 * sp.sin(w * t)
V2 = V0 + A2 * sp.sin(w * t + phi)
Finst = sp.diff(V1, t, 2) * V2  # F = rho/(4 pi r^2) * V2 * d2V1/dt2 (signo aparte)
Fmean = sp.simplify(sp.integrate(Finst, (t, 0, 2 * sp.pi / w)) * w / (2 * sp.pi))
print(f"    F media ∝ {Fmean}")
osc_amp = A1 * w**2 * V0  # amplitud del termino oscilante proporcional a V0
ratio = sp.simplify(osc_amp / (-Fmean.subs(phi, 0)))
print(f"    amplitud del termino oscilante (∝V0) / |F media| (en fase) = {ratio}")
print("    => en escalas de tiempo << T_drive la fuerza dominante oscila con media 0")
print("       y amplitud 2V0/A2 veces la 'gravedad' promedio. Solo A~V0 la tapa.")

print("=" * 70)
print("(D) LA PINZA ESPACIO-TEMPORAL")
c = 2.998e8
kpc = 3.0857e19
yr = 3.156e7
LLR = 1.5e-13  # |Gdot/G| cota LLR ~ (7.1+-7.6)e-14 /yr -> ~1.5e-13 (memoria, estandar)
for Rmax, nombre in [(50 * kpc, "50 kpc (Newton verificado, halo galactico)"),
                     (1000 * kpc, "1 Mpc (cumulos)")]:
    lam_min = Rmax / frac
    T = lam_min / c  # c_s = c (la luz es del medio)
    om = 2 * np.pi / T
    Gdot = 2 * om * yr  # /yr, con |cot| ~ 1 tipico
    print(f"  R_max = {nombre}")
    print(f"    lambda_min = {lam_min/kpc:.1f} kpc ; T_drive = {T/yr:.3e} yr")
    print(f"    Gdot/G tipico = 2w = {Gdot:.3e} /yr ; exceso sobre LLR = {Gdot/LLR:.1e}")

print("  Drive 'modo fundamental de un universo cerrado': T = 1.4e10 yr")
T2yr = 1.4e10
om2 = 2 * np.pi / T2yr  # /yr
print(f"    Gdot/G tipico = {2*om2:.2e} /yr ; exceso sobre LLR = {2*om2/LLR:.1e}")
win = LLR / (2 * om2**2)
print(f"    ventana de sintonia de epoca (cerca del pico de sin^2): |t-t_pico| < {win:.2e} yr")
print(f"    fraccion del semiperiodo: {win/(0.5*T2yr):.1e}")
tu_yr = 13.8e9
dphase = 2 * np.pi * tu_yr / T2yr
print(f"    fase acumulada desde BBN: {dphase:.3f} rad = {dphase/(2*np.pi):.3f} ciclos")
print(f"    => G(t) paso por CERO {int(dphase/np.pi)} veces entre BBN y hoy.")

print("  T requerido para satisfacer LLR:")
om_max = LLR / 2  # /yr
T_req = 2 * np.pi / om_max  # yr
print(f"    T >= {T_req:.2e} yr = {T_req/13.8e9:.0f} edades del universo")
print(f"    ciclos completados desde el Big Bang: {13.8e9/T_req:.2e}")
print("    => no es una oscilacion: es Vdot = cte -> fuente/sumidero estacionario,")
print("       el canal PROHIBIDO por conservacion de la masa del mar (canal 11).")

print("=" * 70)
print("(E) Reduccion al absurdo del limite DC: Vdot para imitar a Newton")
G = 6.674e-11
mp = 1.6726e-27
t_u = 13.8e9 * yr
for rho, nombre in [(1e3, "agua 1e3"), (1e17, "nuclear 1e17"), (5.16e96, "Planck 5e96")]:
    Vdot = mp * np.sqrt(4 * np.pi * G / rho)  # rho*Vdot1*Vdot2/(4 pi r^2)=G m1 m2/r^2
    dV = Vdot * t_u
    req = (3 * dV / (4 * np.pi)) ** (1.0 / 3.0)
    print(f"    rho_mar = {nombre} kg/m3: Vdot_proton = {Vdot:.2e} m3/s ;"
          f" DV(t_universo) = {dV:.2e} m3 ; radio equivalente = {req:.2e} m")

print("=" * 70)
print("(F) Violacion de equivalencia: carga ∝ N (nucleones), masa incluye ligadura")
BA_Ti, BA_Pt = 8.723, 7.927  # MeV/nucleon, valores de memoria (Ti-48, Pt-195)
eta = (BA_Ti - BA_Pt) / 931.494
print(f"    Delta(B/M) Ti-Pt = {eta:.2e}")
print(f"    exceso sobre MICROSCOPE (|eta|<~2e-15): {eta/2e-15:.1e}  (~11-12 ordenes)")

print("=" * 70)
print("(G) Consecuencia orbital de G(t): adiabatico a ∝ 1/G ; P ∝ G^-2")
print("    con T_drive = 3.7e5 yr, la Tierra duplica su semieje cada vez que")
print("    G cae a la mitad; cuando G->0 el periodo diverge, se rompe la")
print("    adiabaticidad y el planeta queda librado (no vuelve).")
