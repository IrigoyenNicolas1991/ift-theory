# ETAPA ESPECULATIVA TCI 2.0 - herramienta de visualizacion del Paso B
# Lee paso_b_flujo_hqv.npz (y opcionalmente el espejo) y dibuja el espectro
# E(kz) coloreado por peso de core: la figura del flujo espectral del acta.
# Uso: python paso_b_grafico.py [archivo.npz [salida.png]]
import numpy as np, sys, os, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AQUI = os.path.dirname(os.path.abspath(__file__))
fin = sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, "paso_b_flujo_hqv.npz")
fout = sys.argv[2] if len(sys.argv) > 2 else fin.replace(".npz", ".png")

d = np.load(fin, allow_pickle=True)
kzs, Es, wcs, wbs = d["kzs"], d["Es"], d["wcs"], d["wbs"]
cruces = json.loads(str(d["cruces"])) if "cruces" in d else []
anticr = json.loads(str(d["anticruces"])) if "anticruces" in d else []

fig, ax = plt.subplots(figsize=(9, 6), dpi=150)
# nube de estados: color por peso de core (gris borde/bulk -> naranja core)
for i, kz in enumerate(kzs):
    sc = ax.scatter(np.full(Es.shape[1], kz), Es[i], c=wcs[i],
                    cmap="inferno", vmin=0, vmax=0.8, s=8, lw=0)
for c in cruces:
    ax.axvline(c["kz"], color="tab:red", ls=":", lw=0.8, alpha=0.6)
    ax.plot([c["kz"]], [0], marker="^" if c["signo"] > 0 else "v",
            color="tab:red", ms=9, zorder=5)
for a in anticr:
    ax.plot([a["kz"]], [0], marker="x", color="tab:blue", ms=7, zorder=5)
ax.axhline(0, color="k", lw=0.6)
ax.set_xlabel(r"$k_z$  (nodos polares del fondo D$_4$ en $\pm\sqrt{\mu}=\pm0.8$)")
ax.set_ylabel(r"$E$")
ax.set_title("Paso B — flujo espectral del HQV: espectro BdG vs $k_z$\n"
             "(color = peso en el core $r<8$; triangulos = cruces netos; "
             "x = anticruces de caja)")
cb = fig.colorbar(sc, ax=ax); cb.set_label("peso de core")
fig.tight_layout()
fig.savefig(fout)
print("->", fout)
