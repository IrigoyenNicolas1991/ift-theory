# -*- coding: utf-8 -*-
"""Test HONESTO del sector galactico con datos SPARC reales.

Reproduce la Relacion de Aceleracion Radial (RAR, McGaugh-Lelli-Schombert 2016)
y confronta:
  (a) Newton / TCI lineal:      g_obs = g_bar               (sin materia oscura)
  (b) Funcion RAR (MOND-like):  g_obs = g_bar/(1-exp(-sqrt(g_bar/a0))), a0 ajustado

Cortes de MLS16: Inc > 30 deg, Q != 3, e_Vobs/Vobs < 0.10. M/L: 0.5 disco, 0.7 bulbo.
g = V^2/R en SI. Objetivo: a0_fit y dispersion (dex) de cada modelo.
"""
import math, io, sys

KPC = 3.0857e19   # m
KMS = 1.0e3       # m/s

# --- parse tabla 1 (propiedades) ---
props = {}
with io.open('SPARC_Lelli2016c.mrt', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
start = max(i for i,l in enumerate(lines) if l.startswith('----')) + 1
for l in lines[start:]:
    f = l.split()
    if len(f) < 18: continue
    try:
        name = f[0]; inc = float(f[5]); q = int(f[17])
    except ValueError: continue
    props[name] = (inc, q)

# --- parse mass models ---
pts = []
with io.open('MassModels_Lelli2016c.mrt', encoding='utf-8', errors='replace') as f:
    mlines = f.readlines()
mstart = max(i for i,l in enumerate(mlines) if l.startswith('----')) + 1
for l in mlines[mstart:]:
    f = l.split()
    if len(f) < 10: continue
    try:
        name = f[0]
        R, Vobs, eV, Vgas, Vdisk, Vbul = (float(x) for x in f[2:8])
    except ValueError: continue
    pts.append((name, R, Vobs, eV, Vgas, Vdisk, Vbul))

# --- cortes de calidad (MLS16) ---
UD, UB = 0.5, 0.7   # M/L disco y bulbo en [3.6]
data = []
gals = set()
for name, R, Vobs, eV, Vgas, Vdisk, Vbul in pts:
    if name not in props: continue
    inc, q = props[name]
    if inc <= 30 or q == 3: continue
    if Vobs <= 0 or eV/Vobs >= 0.10: continue
    Rm = R*KPC
    gobs = (Vobs*KMS)**2/Rm
    gbar = (Vgas*abs(Vgas) + UD*Vdisk*abs(Vdisk) + UB*Vbul*abs(Vbul))*(KMS**2)/Rm
    if gbar <= 0: continue
    data.append((gobs, gbar))
    gals.add(name)

N = len(data)
print(f"puntos tras cortes: {N} | galaxias: {len(gals)}  (MLS16: 2693 pts / 153 gal)")

def rms_dex(a0=None):
    s = 0.0
    for gobs, gbar in data:
        pred = gbar if a0 is None else gbar/(1.0 - math.exp(-math.sqrt(gbar/a0)))
        s += (math.log10(gobs) - math.log10(pred))**2
    return math.sqrt(s/N)

# --- ajuste de a0 (busqueda aurea en log a0) ---
def golden(f, a, b, tol=1e-4):
    g = (math.sqrt(5)-1)/2
    c, d = b-g*(b-a), a+g*(b-a)
    while abs(b-a) > tol:
        if f(c) < f(d): b, d = d, c; c = b-g*(b-a)
        else:           a, c = c, d; d = a+g*(b-a)
    return 0.5*(a+b)

la0 = golden(lambda x: rms_dex(10**x), -11.0, -9.0)
a0_fit = 10**la0

# --- sesgo sistematico de Newton en baja aceleracion ---
low = [(go, gb) for go, gb in data if gb < 1e-11]
bias_newton = sum(math.log10(go/gb) for go, gb in low)/len(low)

# --- TCI: a0 = c*sqrt(G*rho0) con rho0 = 2.4e-27 (calibrado de esta misma escala) ---
G, c, rho0 = 6.674e-11, 2.998e8, 2.4e-27
a0_tci = c*math.sqrt(G*rho0)

print(f"\nNewton / TCI lineal (g_obs = g_bar):        rms = {rms_dex(None):.3f} dex")
print(f"  sesgo en g_bar < 1e-11 (n={len(low)}): g_obs/g_bar = 10^{bias_newton:.2f} = {10**bias_newton:.1f}x")
print(f"\nRAR con a0 ajustado:  a0 = {a0_fit:.3e} m/s^2   rms = {rms_dex(a0_fit):.3f} dex")
print(f"  (MLS16 publico: a0 = 1.20e-10, scatter ~0.13 dex)")
print(f"\nTCI  c*sqrt(G*rho0)  = {a0_tci:.3e} m/s^2  (rho0 calibrado DE esta escala: no es prediccion)")
print(f"RAR con a0 = a0_tci:  rms = {rms_dex(a0_tci):.3f} dex")
