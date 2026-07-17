# ETAPA ESPECULATIVA TCI 2.0 - calculo preliminar, no validado (2026-07-17)
# ============================================================================
# TEST DE MONOMETRICIDAD (version ingenua): v_GW(k) vs v_luz(k) en el D4-BN
# ----------------------------------------------------------------------------
# Identificacion INGENUA declarada: "luz" = modos gapless de helicidad +-1 del
# mismo condensado (sector transversal tipo MacCullagh); "GW" = mejor modo TT.
# GW170817: |v_GW/v_luz - 1| < 1e-15. Medimos: (a) cociente medio, (b)
# anisotropia del cociente vs anisotropia de cada sector por separado.
# Si el cociente medio != 1 => la identificacion ingenua muere por GW170817.
# Si la anisotropia del cociente << la de cada sector => la cancelacion
# relativa (monometricidad) tiene alguna realidad incluso en la version ingenua.
# ============================================================================
import numpy as np

src = open('espectro_biaxial_3p2.py').read().split('# ============================ CASOS')[0]
exec(src)

rng = np.random.default_rng(23)
K = 1.0
al, be = -1.0, 1.0
paramsC = (al, be, +0.15, 0.05)
xmC = find_min(np.concatenate([0.4*rng.standard_normal(5), np.zeros(5)]), paramsC)
M = hess(xmC, *paramsC)

Nk = 400
i = np.arange(Nk)
phi_g = np.pi * (3 - np.sqrt(5)) * i
z = 1 - 2*(i + 0.5)/Nk
r = np.sqrt(1 - z*z)
kdirs = np.stack([r*np.cos(phi_g), r*np.sin(phi_g), z], axis=1)

kmag = 1e-3
v_gw, v_luz, ratio = [], [], []
for kd in kdirs:
    kk = kmag * kd
    w2, U = np.linalg.eigh(M + Kgrad(kk, K))
    entries = []
    for m in range(10):
        if w2[m] < (10*kmag)**2:
            h2, h1, h0 = helicity_content(U[:, m], kk)
            entries.append((h2, h1, np.sqrt(max(w2[m], 0))/kmag))
    entries = np.array(entries)
    igw = np.argmax(entries[:, 0])
    vg = entries[igw, 2]
    resto = np.delete(entries, igw, axis=0)
    orden_h1 = np.argsort(-resto[:, 1])[:2]
    vl = resto[orden_h1, 2].mean()
    v_gw.append(vg); v_luz.append(vl); ratio.append(vg/vl)

v_gw = np.array(v_gw); v_luz = np.array(v_luz); ratio = np.array(ratio)

def spread(x):
    return (x.max()-x.min())/x.mean()*100

print("=== TEST DE MONOMETRICIDAD (identificacion ingenua declarada) ===")
print(f"v_GW : media {v_gw.mean():.4f}   anisotropia {spread(v_gw):.1f} %")
print(f"v_luz: media {v_luz.mean():.4f}   anisotropia {spread(v_luz):.1f} %")
print(f"cociente v_GW/v_luz: media {ratio.mean():.4f}   min {ratio.min():.4f}   max {ratio.max():.4f}")
print(f"anisotropia del cociente: {spread(ratio):.1f} %")
print()
print(f"VEREDICTO 1 (cociente medio): {'PASA' if abs(ratio.mean()-1)<1e-3 else 'MUERE'} "
      f"— GW170817 exige 1 a 15 decimales; da {ratio.mean():.3f}")
print(f"VEREDICTO 2 (cancelacion relativa): anisotropia del cociente ({spread(ratio):.1f}%) "
      f"vs sectores ({spread(v_gw):.1f}% / {spread(v_luz):.1f}%)")
