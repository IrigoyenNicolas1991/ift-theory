# -*- coding: utf-8 -*-
"""
SOTANO — Fase C, calculo 3: LA ESPUMA VIVA (posiciones descongeladas).

En el calculo 2 (posiciones congeladas) los anillos fabricaron orden J=2
LOCAL sin flecha, pero el fundamental era una textura frustrada multi-eje,
no el nematico uniforme. Pregunta de este script: si los anillos ademas
pueden MOVERSE, ¿la frustracion se disuelve? ¿cristalizan en columnas
coaxiales antiparalelas (nematico uniforme = la gota J=2 macroscopica)?

Modelo (idealizaciones declaradas):
  - anillos = dipolos puntuales de Neumann con signo vortice:
        E_dip = -C [ n_i.n_j - 3 (n_i.dhat)(n_j.dhat) ] / d^3,  C=1
  - nucleo repulsivo A/d^9 (stand-in del solape de nucleos; A=2/3 fija el
    espaciado del par optimo en d*=1; robustez chequeada con exponente 6)
  - sin autopropulsion ni dinamica real: solo MINIMIZamos energia
    (= pregunta de estatica: ¿que estructura prefiere la energia?)

CONTROLES:
  - autotest de gradientes por diferencias finitas (posiciones y orientaciones)
  - par aislado: debe relajar a coaxial antiparalelo con d=1, E=-4/3
  - candidato analitico (cristal columnar tetragonal, espaciados optimizados
    por barrido) compite contra el recocido desde el azar
"""
import numpy as np

rng = np.random.default_rng(11)
C = 1.0

def energy_forces(pos, n, A=2.0/3.0, p=9):
    N = len(pos)
    D = pos[:, None, :] - pos[None, :, :]          # r_i - r_j
    d = np.linalg.norm(D, axis=-1)
    np.fill_diagonal(d, np.inf)
    dh = D/d[..., None]
    ni_dh = np.einsum('ia,ija->ij', n, dh)          # n_i . dhat_ij
    nj_dh = np.einsum('ja,ija->ij', n, dh)          # n_j . dhat_ij
    ninj = n @ n.T
    Edip = -C*(ninj - 3*ni_dh*nj_dh)/d**3
    Erep = A/d**p
    E = 0.5*np.sum(Edip + Erep)
    # gradiente respecto de n_i (sin proyectar):
    gn = -C*np.einsum('ij,ja->ia', 1.0/d**3, n) \
         + 3*C*np.einsum('ij,ija->ia', nj_dh/d**3, dh)
    # gradiente respecto de r_i (E_pair es par en D; el 0.5 y la doble suma
    # se cancelan -> gradiente de par completo sumado en j):
    t1 = 3*C*ninj/d**4                    # de -C ninj/d^3
    t2 = -15*C*ni_dh*nj_dh/d**4           # parte radial de +3C(ni.dh)(nj.dh)/d^3
    t3 = -p*A/d**(p+1)                    # nucleo repulsivo
    rad = (t1 + t2 + t3)[..., None]*dh
    ang = 3*C*(n[None, :, :]*ni_dh[..., None]
               + n[:, None, :]*nj_dh[..., None])/d[..., None]**4
    gr = np.sum(rad + ang, axis=1)
    return E, gr, gn

def autotest():
    N = 5
    pos = rng.normal(size=(N, 3))*1.5
    n = rng.normal(size=(N, 3)); n /= np.linalg.norm(n, axis=1, keepdims=True)
    E, gr, gn = energy_forces(pos, n)
    eps = 1e-6
    okr = okn = True
    for i in range(N):
        for a in range(3):
            pp = pos.copy(); pp[i, a] += eps
            E2, _, _ = energy_forces(pp, n)
            num = (E2 - E)/eps
            if abs(num - gr[i, a]) > 1e-4*max(1, abs(num)):
                okr = False
            nn2 = n.copy(); nn2[i, a] += eps   # sin normalizar: gradiente crudo
            E2, _, _ = energy_forces(pos, nn2)
            num = (E2 - E)/eps
            if abs(num - gn[i, a]) > 1e-4*max(1, abs(num)):
                okn = False
    print(f"AUTOTEST gradientes: posiciones [{'OK' if okr else 'FALLA'}]  "
          f"orientaciones [{'OK' if okn else 'FALLA'}]")
    return okr and okn

def relax(pos, n, iters=6000, lrx=0.02, lrn=0.05, noise0=0.0, p=9):
    pos = pos.copy(); n = n.copy()
    for it in range(iters):
        E, gr, gn = energy_forces(pos, n, p=p)
        gt = gn - (np.einsum('ia,ia->i', gn, n))[:, None]*n
        f = np.exp(-4*it/iters)
        pos -= lrx*np.clip(gr, -1, 1)
        n -= lrn*gt
        if noise0:
            pos += noise0*0.5*f*rng.normal(size=pos.shape)
            n += noise0*f*rng.normal(size=n.shape)
        n /= np.linalg.norm(n, axis=1, keepdims=True)
    E, _, _ = energy_forces(pos, n, p=p)
    return E, pos, n

def order_params(pos, n):
    c = pos.mean(0)
    r = np.linalg.norm(pos - c, axis=1)
    core = r <= np.percentile(r, 60)
    m = n[core]
    P = np.linalg.norm(m.mean(0))
    Q = 1.5*(np.einsum('ia,ib->ab', m, m)/len(m) - np.eye(3)/3)
    w, v = np.linalg.eigh(Q)
    S = w[-1]; eje = v[:, -1]
    # S local (10 vecinos)
    D = np.linalg.norm(pos[:, None] - pos[None, :], axis=-1)
    Sl = []
    for i in np.where(core)[0]:
        nb = np.argsort(D[i])[1:11]
        mm = n[nb]
        Ql = 1.5*(np.einsum('ia,ib->ab', mm, mm)/len(mm) - np.eye(3)/3)
        Sl.append(np.max(np.linalg.eigvalsh(Ql)))
    # geometria: distancia al vecino mas cercano "a lo largo del director local"
    # vs "perpendicular" (firma columnar: d_paralelo < d_perp)
    dpar, dperp = [], []
    for i in np.where(core)[0]:
        nb = np.argsort(D[i])[1:11]
        for j in nb:
            b = pos[j] - pos[i]; db = np.linalg.norm(b)
            cosb = abs(b @ n[i])/db
            (dpar if cosb > 0.8 else dperp if cosb < 0.3 else []).append(db)
    return P, S, float(np.mean(Sl)), \
        (float(np.mean(dpar)) if dpar else np.nan), \
        (float(np.mean(dperp)) if dperp else np.nan)

print("=== AUTOTEST ===")
assert autotest(), "gradientes mal — no seguir"

print()
print("=== CONTROL: par aislado -> coaxial antiparalelo, d=1, E=-4/3 ===")
pos = np.array([[0., 0., 0.], [0.3, 0.4, 0.8]])
n = rng.normal(size=(2, 3)); n /= np.linalg.norm(n, axis=1, keepdims=True)
E, pos2, n2 = relax(pos, n, iters=4000, noise0=0.01)
dfin = np.linalg.norm(pos2[1]-pos2[0])
cosnn = n2[0] @ n2[1]
b = (pos2[1]-pos2[0])/dfin
print(f"  E={E:.5f} (teo -1.33333)  d={dfin:.4f} (teo 1)  n1.n2={cosnn:+.4f} (teo -1)"
      f"  |n.dhat|={abs(n2[0]@b):.4f} (teo 1)")

print()
print("=== CANDIDATO ANALITICO: cristal columnar tetragonal (5x5x6=150) ===")
best_cand = None
for dz in (0.90, 0.95, 1.00, 1.05, 1.10):
    for dxy in (0.95, 1.05, 1.15, 1.25, 1.35):
        ii, jj, kk = np.meshgrid(range(5), range(5), range(6), indexing='ij')
        posc = np.stack([ii.ravel()*dxy, jj.ravel()*dxy, kk.ravel()*dz], axis=1)
        nc = np.zeros((150, 3)); nc[:, 2] = (-1.0)**kk.ravel()
        E, _, _ = energy_forces(posc, nc)
        if best_cand is None or E < best_cand[0]:
            best_cand = (E, dz, dxy, posc, nc)
E0, dz, dxy, posc, nc = best_cand
print(f"  mejor barrido: dz={dz:.2f} dxy={dxy:.2f}  E_exacta={E0:.3f}")
Ec, posr, nr = relax(posc, nc, iters=3000)
P, S, Sl, dpar, dperp = order_params(posr, nr)
print(f"  relajado: E={Ec:.3f}  P={P:.3f}  S={S:.3f}  S_local={Sl:.3f}  "
      f"d_par={dpar:.3f} d_perp={dperp:.3f}")

print()
print("=== RECOCIDO DESDE EL AZAR (N=150, 6 arranques) ===")
best = None
for st in range(6):
    pos = rng.uniform(0, 150**(1/3)/0.75, size=(150, 3))
    n = rng.normal(size=(150, 3)); n /= np.linalg.norm(n, axis=1, keepdims=True)
    E, pos2, n2 = relax(pos, n, iters=6000, noise0=0.05)
    print(f"  arranque {st}: E={E:.3f}")
    if best is None or E < best[0]:
        best = (E, pos2, n2)
E, pos2, n2 = best
P, S, Sl, dpar, dperp = order_params(pos2, n2)
print(f"  MEJOR: E={E:.3f}  P={P:.3f}  S={S:.3f}  S_local={Sl:.3f}  "
      f"d_par={dpar:.3f}  d_perp={dperp:.3f}")
print(f"  candidato columnar: E={Ec:.3f}  -> "
      f"{'el CANDIDATO gana (el recocido quedo en mosaico)' if Ec < E else 'el RECOCIDO gana (la espuma no elige columnas)'}")

print()
print("=== ROBUSTEZ: nucleo d^6 en vez de d^9 (candidato vs un recocido) ===")
A6 = 1.0  # d* del par optimo: dE/dd=0 -> 6/d^4 = 6*A6/d^7 -> d*=A6^(1/3)=1
Ec6, _, _ = relax(posc, nc, iters=2000, p=6)
pos = rng.uniform(0, 150**(1/3)/0.75, size=(150, 3))
n = rng.normal(size=(150, 3)); n /= np.linalg.norm(n, axis=1, keepdims=True)
Er6, p6, n6 = relax(pos, n, iters=6000, noise0=0.05, p=6)
P6, S6, Sl6, _, _ = order_params(p6, n6)
print(f"  p=6: candidato relajado E={Ec6:.3f} | recocido E={Er6:.3f} "
      f"(P={P6:.3f} S={S6:.3f} S_local={Sl6:.3f})")
print()
print("Lectura: si el columnar gana en energia y el recocido muestra S_local alto")
print("con S global chico => el nematico uniforme ES el fundamental y el mosaico")
print("es cinetica (dominios). Si el recocido gana con S~0 => frustracion robusta.")
