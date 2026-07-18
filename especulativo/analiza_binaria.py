# ETAPA ESPECULATIVA TCI 2.0 - analisis post-hoc de binaria_datos.npz (§31)
# El estallido de la fusion: canales y espectro en la ventana POST-fusion
# (la radiacion tarda ~r_anillo/c_s ~ 60 u.t. ~ paso 500 en llegar al anillo).
import numpy as np

np.set_printoptions(precision=4, suppress=True)
d = np.load("binaria_datos.npz", allow_pickle=True)
ring = d["ring"]          # (T, 10, NRING), muestreado cada 8 pasos (dt=0.12)
Es = d["Es"]
DT = 0.12; MED = 8

E5 = np.zeros((5, 3, 3))
E5[0] = np.diag([1, -1, 0]) / np.sqrt(2)
E5[1] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / np.sqrt(2)
E5[2] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]]) / np.sqrt(2)
E5[3] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]]) / np.sqrt(2)
E5[4] = np.diag([-1, -1, 2]) / np.sqrt(6)
L = np.zeros((3, 3, 3))
L[0] = np.array([[0,0,0],[0,0,-1],[0,1,0]]); L[1] = np.array([[0,0,1],[0,0,0],[-1,0,0]])
L[2] = np.array([[0,-1,0],[1,0,0],[0,0,0]])
a0 = 0.47225
A0m = a0 * np.diag([1., -1., 0.])
def x_of_A(A):
    return np.concatenate([[np.real(np.trace(A @ E5[a])) for a in range(5)],
                           [np.imag(np.trace(A @ E5[a])) for a in range(5)]])
def unit(v): return v / np.linalg.norm(v)
CANALES = {"fase": unit(x_of_A(1j * A0m)),
           "rot-z": unit(x_of_A(L[2] @ A0m + A0m @ L[2].T)),
           "rot-x": unit(x_of_A(L[0] @ A0m + A0m @ L[0].T)),
           "rot-y": unit(x_of_A(L[1] @ A0m + A0m @ L[1].T)),
           "amp": unit(x_of_A(A0m))}

T = ring.shape[0]
print(f"muestras totales: {T} (pasos 8..{T*8})")

def tabla(datos, titulo):
    print(f"\n{titulo} (fraccion de <vdot^2> en el anillo r=70):")
    pr = {}
    for nom, u in CANALES.items():
        pr[nom] = np.einsum('a,tan->tn', u, datos)
    tot5 = sum(np.mean(p**2) for p in pr.values())
    resto = max(np.mean(np.sum(datos**2, axis=1)) - tot5, 0.0)
    for nom, p in pr.items():
        print(f"  {nom:6s}: {np.mean(p**2):.3e}   ({np.mean(p**2)/(tot5+resto)*100:6.2f}%)")
    print(f"  resto : {resto:.3e}   ({resto/(tot5+resto)*100:6.2f}%)")
    c = np.mean(pr["fase"] * pr["rot-z"])
    cmax = np.sqrt(np.mean(pr["fase"]**2) * np.mean(pr["rot-z"]**2))
    print(f"  correlacion fase*rot-z: {c:+.3e} / maxima {cmax:.3e}  -> "
          f"{'q+ PURO' if abs(c) > 0.95*cmax else 'mezcla de sectores'}")
    return pr

# ventanas: imprint inicial (pre-llegada), estallido (llegada del frente en
# paso ~ r/c_s/dt ~ 480 => muestra ~60), cola tardia
tabla(ring[:15], "VENTANA 1 — pasos 8-120 (imprint del lanzamiento, pre-fusion)")
pr_burst = tabla(ring[60:200], "VENTANA 2 — pasos 480-1600 (EL ESTALLIDO cruzando el anillo)")
tabla(ring[200:], f"VENTANA 3 — pasos 1600-{T*8} (cola/ringdown tardio)")

# espectro del estallido
print("\nespectro del estallido (ventana 2), por canal:")
Tm = 140; dt_m = MED * DT
fr = np.fft.rfftfreq(Tm, dt_m) * 2 * np.pi
for nom in ["fase", "rot-z", "amp"]:
    sig = pr_burst[nom] - pr_burst[nom].mean(axis=0)
    S = (np.abs(np.fft.rfft(sig, axis=0))**2).mean(axis=1)
    top = np.argsort(S[1:])[::-1][:5] + 1
    print(f"  {nom:6s}: picos en omega = {[f'{fr[i]:.3f}' for i in top]}")
print("  (referencia: gap del modo-r del D4 ~ sqrt(0.24) = 0.49; "
      "frente del plunge t~15 => transitorio ancho)")

# energia radiada
print(f"\nenergia interna: {Es[0,1]:.3f} -> {Es[-1,1]:.3f} "
      f"({(1 - Es[-1,1]/Es[0,1])*100:.1f}% radiada/absorbida por la esponja)")
