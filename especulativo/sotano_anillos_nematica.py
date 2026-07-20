# -*- coding: utf-8 -*-
"""
SOTANO — Fase C, calculo 2 (VIRGEN): ¿una poblacion de anillos de vortice
ordena sola sus planos (orden J=2, "gota") sin flecha neta (J=1)?

Modelo (idealizacion declarada): anillos = dipolos hidrodinamicos puntuales,
posiciones y tamanios CONGELADOS, solo orientaciones n_i libres. Energia de
interaccion lejana = formula de Neumann (inductancia mutua de espiras con
corriente Gamma) — para VORTICES la energia cinetica del fluido es
+rho*G1*G2*M12, el signo OPUESTO al magnetico U=-m.B:

    E_vort(i,j) = -C * [ n_i.n_j - 3 (n_i.rhat)(n_j.rhat) ] / d^3,  C>0
    E_mag (i,j) = +C * [ n_i.n_j - 3 (n_i.rhat)(n_j.rhat) ] / d^3

CONTROLES EXACTOS (a mano):
  par magnetico  -> cabeza-cola sobre el eje (E=-2C/d^3)
  par vortice    -> coaxial ANTIparalelo (E=-2C/d^3); coplanar paralelo da -C/d^3
  SC magnetico   -> antiferro columnar (Luttinger-Tisza 1946): P~0, S alto
  (El control "FCC magnetico -> ferro" NO aplica en cluster abierto: la
   energia de forma/desmagnetizacion penaliza el ferro — declarado; LT es
   resultado de bulk. Lo reemplazan los controles de par, exactos.)

METODO ANTI-DOMINIOS: ademas del recocido numerico, construimos candidatos
analiticos y comparamos energias directamente. Si un candidato ordenado gana
al mejor numerico, el numerico estaba en policristal.

Observables (mitad interior): P=|<n>| (flecha J=1; alta = MUERTE),
S = autovalor max de (3/2)(<nn>-I/3) (nematico J=2 con n como directores),
S_local = idem sobre los 12 vecinos mas cercanos de cada sitio (vidrio vs
policristal: S_local alto + S global bajo = dominios).
"""
import numpy as np

rng = np.random.default_rng(7)

# ---------- geometrias ----------
def lattice_sc(L):
    return np.array([[i, j, k] for i in range(L) for j in range(L) for k in range(L)], float)

def lattice_fcc(L):
    base = [[0, 0, 0], [0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]]
    return np.array([[i+b[0], j+b[1], k+b[2]]
                     for i in range(L) for j in range(L) for k in range(L)
                     for b in base], float)

def random_isotropic(N, density, seed=1):
    rr = np.random.default_rng(seed)
    Lbox = (N/density)**(1/3)
    dmin = 0.7*(1.0/density)**(1/3)
    pts = []
    tries = 0
    while len(pts) < N and tries < 500000:
        p = rr.uniform(0, Lbox, 3)
        if not pts or np.min(np.linalg.norm(np.array(pts)-p, axis=1)) > dmin:
            pts.append(p)
        tries += 1
    return np.array(pts)

# ---------- energia ----------
def pair_tensors(pos):
    D = pos[:, None, :] - pos[None, :, :]
    d = np.linalg.norm(D, axis=-1)
    np.fill_diagonal(d, np.inf)
    rhat = D/d[..., None]
    return (np.eye(3)[None, None] - 3*rhat[..., :, None]*rhat[..., None, :]) / d[..., None, None]**3

def energy_grad(n, Tt, sign):
    h = np.einsum('ijab,jb->ia', Tt, n)
    return 0.5*sign*np.einsum('ia,ia->', n, h), sign*h

def relax(n0, Tt, sign, iters=3000, lr=0.05, noise0=0.0):
    n = n0.copy()
    for it in range(iters):
        E, g = energy_grad(n, Tt, sign)
        gt = g - (np.einsum('ia,ia->i', g, n))[:, None]*n
        noise = noise0*np.exp(-4*it/iters)
        n = n - lr*gt + (noise*rng.normal(size=n.shape) if noise0 else 0.0)
        n /= np.linalg.norm(n, axis=1, keepdims=True)
    E, _ = energy_grad(n, Tt, sign)
    return E, n

def minimize(Tt, N, sign, n_starts=8, iters=3500):
    best = None
    for st in range(n_starts):
        n = rng.normal(size=(N, 3))
        n /= np.linalg.norm(n, axis=1, keepdims=True)
        E, n = relax(n, Tt, sign, iters=iters, noise0=0.03)
        E, n = relax(n, Tt, sign, iters=800, noise0=0.0)  # pulido final
        if best is None or E < best[0]:
            best = (E, n)
    return best

def order_params(pos, n):
    c = pos.mean(0)
    r = np.linalg.norm(pos - c, axis=1)
    core = r <= np.percentile(r, 50)
    m = n[core]
    P = np.linalg.norm(m.mean(0))
    Q = 1.5*(np.einsum('ia,ib->ab', m, m)/len(m) - np.eye(3)/3)
    S = np.max(np.linalg.eigvalsh(Q))
    # nematico local: 12 vecinos mas cercanos de cada sitio interior
    D = np.linalg.norm(pos[:, None] - pos[None, :], axis=-1)
    Sl = []
    for i in np.where(core)[0]:
        nb = np.argsort(D[i])[1:13]
        mm = n[nb]
        Ql = 1.5*(np.einsum('ia,ib->ab', mm, mm)/len(mm) - np.eye(3)/3)
        Sl.append(np.max(np.linalg.eigvalsh(Ql)))
    return P, S, float(np.mean(Sl))

# ---------- controles de par (exactos) ----------
print("=== CONTROLES DE PAR (exactos a mano; d=1, C=1) ===")
posp = np.array([[0., 0., 0.], [0., 0., 1.]])
Tp = pair_tensors(posp)
for tag, sign, na, nb, exp in [
    ("mag cabeza-cola (n=n=z)      esperado -2", +1, [0, 0, 1], [0, 0, 1], -2.0),
    ("mag coplanar paralelo (n=x)  esperado +1 (imanes lado a lado se repelen)", +1, [1, 0, 0], [1, 0, 0], +1.0),
    ("vort coaxial ANTIpar (z,-z)  esperado -2", -1, [0, 0, 1], [0, 0, -1], -2.0),
    ("vort coplanar paralelo (x,x) esperado -1", -1, [1, 0, 0], [1, 0, 0], -1.0),
    ("vort coaxial paralelo (z,z)  esperado +2", -1, [0, 0, 1], [0, 0, 1], +2.0),
]:
    nn = np.array([na, nb], float)
    E, _ = energy_grad(nn, Tp, sign)
    ok = "OK" if abs(E - exp) < 1e-12 else "FALLA"
    print(f"  {tag}: E={E:+.4f}  [{ok}]")

# ---------- control SC magnetico (Luttinger-Tisza) ----------
print()
print("=== CONTROL RED: SC magnetico -> antiferro columnar (LT 1946) ===")
pos = lattice_sc(7)
Tt = pair_tensors(pos)
E, n = minimize(Tt, len(pos), sign=+1)
P, S, Sl = order_params(pos, n)
print(f"  numerico: E={E:9.3f}  P={P:.3f}  S={S:.3f}  S_local={Sl:.3f}"
      f"   (esperado P~0, S alto)")

# ---------- VORTICES en SC: candidatos analiticos vs numerico ----------
print()
print("=== VORTICES en SC (7^3): candidatos analiticos vs recocido ===")
L = 7
ii, jj, kk = np.meshgrid(range(L), range(L), range(L), indexing='ij')
ii, jj, kk = ii.ravel(), jj.ravel(), kk.ravel()

def cfg_from_signs(s, axis):
    n = np.zeros((L**3, 3)); n[:, axis] = s
    return n

candidatos = {
    "laminado z (+z/-z alternando en k, uniforme en xy)": cfg_from_signs((-1.0)**kk, 2),
    "Neel total ((-1)^(i+j+k) z)": cfg_from_signs((-1.0)**(ii+jj+kk), 2),
    "ferro z": cfg_from_signs(np.ones(L**3), 2),
    "laminado x (idem, eje x)": cfg_from_signs((-1.0)**ii, 0),
}
resultados = {}
for tag, n0 in candidatos.items():
    E0, _ = energy_grad(n0, Tt, -1)
    Er, nr = relax(n0, Tt, -1, iters=1500)   # ¿es minimo local? ¿baja al relajar?
    P, S, Sl = order_params(pos, nr)
    resultados[tag] = Er
    print(f"  {tag}")
    print(f"     E_exacta={E0:9.3f}  E_relajada={Er:9.3f}  P={P:.3f}  S={S:.3f}  S_local={Sl:.3f}")

E, n = minimize(Tt, len(pos), sign=-1)
P, S, Sl = order_params(pos, n)
print(f"  recocido numerico (8 arranques): E={E:9.3f}  P={P:.3f}  S={S:.3f}  S_local={Sl:.3f}")
mejor = min(resultados, key=resultados.get)
print(f"  --> mejor candidato analitico: '{mejor}' (E={resultados[mejor]:.3f})"
      f"  {'GANA al numerico' if resultados[mejor] < E else 'pierde con el numerico'}")

# ---------- VORTICES en FCC ----------
print()
print("=== VORTICES en FCC (5^3 celdas, N=500) ===")
posf = lattice_fcc(5)
Ttf = pair_tensors(posf)
kf = np.round(2*posf[:, 2]).astype(int)   # capa segun z (paso 1/2)
candf = {
    "laminado z por capas (+z/-z segun capa)": None,
    "ferro z": None,
}
n0 = np.zeros((len(posf), 3)); n0[:, 2] = (-1.0)**kf
candf["laminado z por capas (+z/-z segun capa)"] = n0
n1 = np.zeros((len(posf), 3)); n1[:, 2] = 1.0
candf["ferro z"] = n1
resf = {}
for tag, n0 in candf.items():
    E0, _ = energy_grad(n0, Ttf, -1)
    Er, nr = relax(n0, Ttf, -1, iters=1500)
    P, S, Sl = order_params(posf, nr)
    resf[tag] = Er
    print(f"  {tag}: E_exacta={E0:9.3f}  E_relajada={Er:9.3f}  P={P:.3f}  S={S:.3f}  S_local={Sl:.3f}")
E, n = minimize(Ttf, len(posf), sign=-1)
P, S, Sl = order_params(posf, n)
print(f"  recocido numerico (8 arranques): E={E:9.3f}  P={P:.3f}  S={S:.3f}  S_local={Sl:.3f}")

# ---------- ESPUMA isotropa ----------
print()
print("=== VORTICES en ESPUMA isotropa (posiciones congeladas al azar, N=343) ===")
pose = random_isotropic(343, 1.0)
Tte = pair_tensors(pose)
E, n = minimize(Tte, len(pose), sign=-1, n_starts=10)
P, S, Sl = order_params(pose, n)
print(f"  recocido numerico (10 arranques): E={E:9.3f}  P={P:.3f}  S={S:.3f}  S_local={Sl:.3f}")
print(f"  lectura: S_local >> S global = dominios nematicos sin eje comun (policristal/vidrio);")
print(f"           S_local ~ S ~ 0 = desorden genuino; P alto = flecha (muerte).")
