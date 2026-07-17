# ETAPA ESPECULATIVA TCI 2.0 - calculo preliminar, no validado (2026-07-17)
# ============================================================================
# MAPA DE ANISOTROPIA del estado D4-BN (caso C de espectro_biaxial_3p2.py)
# ----------------------------------------------------------------------------
# Pregunta: que tan grave es el dragon de la anisotropia? Barremos ~400
# direcciones k (esfera de Fibonacci) y medimos en cada una:
#   - velocidades de los 4 modos gapless
#   - contenido de helicidad +-2 (TT) de los 2 modos "mas TT"
# Salida: estadisticas de pureza TT y dispersion de velocidades del sector TT.
# ============================================================================
import numpy as np

src = open('espectro_biaxial_3p2.py').read().split('# ============================ CASOS')[0]
exec(src)

rng = np.random.default_rng(23)
K = 1.0
al, be = -1.0, 1.0
paramsC = (al, be, +0.15, 0.05)

# reencontrar el minimo D4 (mismas semillas que el script original)
xmC = find_min(np.concatenate([0.4*rng.standard_normal(5), np.zeros(5)]), paramsC)
A0 = Amat(xmC)
ph = np.angle(np.trace(A0 @ A0)) / 2
w_eig, vecs = np.linalg.eigh(np.real(A0 * np.exp(-1j*ph)))
axis = vecs[:, np.argmin(np.abs(w_eig))]
print("estado D4 reencontrado; autovalores:", np.round(np.sort(w_eig), 4))
M = hess(xmC, *paramsC)

# esfera de Fibonacci
Nk = 400
i = np.arange(Nk)
phi_g = np.pi * (3 - np.sqrt(5)) * i
z = 1 - 2*(i + 0.5)/Nk
r = np.sqrt(1 - z*z)
kdirs = np.stack([r*np.cos(phi_g), r*np.sin(phi_g), z], axis=1)

kmag = 1e-3
tt_best, tt_second, v_tt, v_all_gapless = [], [], [], []
ang_axis = []
for kd in kdirs:
    kk = kmag * kd
    w2, U = np.linalg.eigh(M + Kgrad(kk, K))
    h2s, vs = [], []
    for m in range(10):
        if w2[m] < (10*kmag)**2:
            h2, h1, h0 = helicity_content(U[:, m], kk)
            h2s.append(h2)
            vs.append(np.sqrt(max(w2[m], 0))/kmag)
    h2s = np.array(h2s); vs = np.array(vs)
    order = np.argsort(-h2s)
    tt_best.append(h2s[order[0]]); tt_second.append(h2s[order[1]])
    v_tt.append(vs[order[0]])
    v_all_gapless.append(vs)
    ang_axis.append(np.degrees(np.arccos(min(1, abs(kd @ axis)))))

tt_best = np.array(tt_best); tt_second = np.array(tt_second)
v_tt = np.array(v_tt); ang_axis = np.array(ang_axis)

print(f"\n=== MAPA SOBRE {Nk} DIRECCIONES ===")
print(f"pureza TT del mejor modo:    media {tt_best.mean():.3f}  min {tt_best.min():.3f}  max {tt_best.max():.3f}")
print(f"pureza TT del segundo modo:  media {tt_second.mean():.3f}  min {tt_second.min():.3f}  max {tt_second.max():.3f}")
print(f"velocidad del sector TT:     media {v_tt.mean():.4f}  min {v_tt.min():.4f}  max {v_tt.max():.4f}")
print(f"anisotropia de velocidad TT: (max-min)/media = {(v_tt.max()-v_tt.min())/v_tt.mean()*100:.1f} %")

# fraccion del cielo con pureza alta
for umbral in (0.9, 0.7, 0.5):
    f1 = np.mean(tt_best >= umbral)*100
    f2 = np.mean(tt_second >= umbral)*100
    print(f"fraccion del cielo con TT>= {umbral}: mejor modo {f1:.0f}%   segundo {f2:.0f}%")

# pureza vs angulo al eje especial (bins)
print("\npureza (mejor / segundo) por angulo al eje especial:")
for lo, hi in [(0,15),(15,30),(30,45),(45,60),(60,75),(75,90)]:
    sel = (ang_axis >= lo) & (ang_axis < hi)
    if sel.sum():
        print(f"  {lo:>2}-{hi:<2} grados: {tt_best[sel].mean():.3f} / {tt_second[sel].mean():.3f}   (n={sel.sum()})")
