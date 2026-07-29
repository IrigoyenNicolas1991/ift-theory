# Verificacion de caja: la especie B en N=100 (campo GL 80x80 embebido con
# London analitico del (1/2,-1/4) en el anillo exterior, empalme suave).
# Si los cruces de +-0.568 son topologicos, sobreviven; si son resonancias
# de borde, se mueven/desaparecen. Decide C_B entre -1 (fase) y +1 (marco).
import numpy as np, os, time
import scipy.sparse as sp
import scipy.sparse.linalg as spla

t0 = time.time()
AQUI = r"C:\ClaudeInMyComputer\TCI CON Fable New folder\ift-theory\especulativo"
E5 = np.zeros((5, 3, 3))
E5[0] = np.diag([1, -1, 0]) / np.sqrt(2)
E5[1] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / np.sqrt(2)
E5[2] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]]) / np.sqrt(2)
E5[3] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]]) / np.sqrt(2)
E5[4] = np.diag([-1, -1, 2]) / np.sqrt(6)
H_LAT, MU, KF, DELTA0 = 1.0, 0.64, 0.8, 0.6
A0 = 0.47211
sq2 = np.sqrt(2.0)

def stamp(m): print(f"[{time.time()-t0:6.1f}s] {m}", flush=True)

def bdg_sparse(Afield, kz, mu=MU, D0=DELTA0, h=H_LAT):
    Ny, Nx = Afield.shape[:2]
    M = Ny * Nx
    ii = np.arange(M).reshape(Ny, Nx)
    diag_xi = np.full(M, 4.0 / h**2 + kz**2 - mu)
    rows, cols, vals = [np.arange(M)], [np.arange(M)], [diag_xi]
    for (di, dj) in ((0, 1), (1, 0)):
        src = ii[:Ny - di, :Nx - dj].ravel()
        dst = ii[di:, dj:].ravel()
        hop = np.full(src.size, -1.0 / h**2)
        rows += [src, dst]; cols += [dst, src]; vals += [hop, hop]
    XI = sp.csr_matrix((np.concatenate(vals),
                        (np.concatenate(rows), np.concatenate(cols))),
                       shape=(M, M))
    Amu = np.transpose(Afield, (2, 3, 0, 1))
    pref = D0 / KF
    Dmu = []
    for mu_s in range(3):
        rowsD = [np.arange(M)]; colsD = [np.arange(M)]
        valsD = [pref * kz * Amu[mu_s, 2].ravel().astype(complex)]
        for j_orb, (di, dj) in ((0, (0, 1)), (1, (1, 0))):
            Aj = Amu[mu_s, j_orb]
            src = ii[:Ny - di, :Nx - dj]
            dst = ii[di:, dj:]
            Aenl = 0.5 * (Aj[:Ny - di, :Nx - dj] + Aj[di:, dj:])
            c = -1j / (2.0 * h) * pref * Aenl.ravel()
            rowsD += [src.ravel(), dst.ravel()]
            colsD += [dst.ravel(), src.ravel()]
            valsD += [c, -c]
        Dmu.append(sp.csr_matrix((np.concatenate(valsD),
                                  (np.concatenate(rowsD), np.concatenate(colsD))),
                                 shape=(M, M)))
    D1, D2, D3 = Dmu
    Del_uu = -D1 + 1j * D2
    Del_dd = D1 + 1j * D2
    return sp.bmat([[XI, None, Del_uu, D3],
                    [None, XI, D3, Del_dd],
                    [Del_uu.conj().T, D3.conj().T, -XI, None],
                    [D3.conj().T, Del_dd.conj().T, None, -XI]], format='csr')

# ---- campo del B en caja 100: GL 80 centrado + London analitico afuera
dat = np.load(os.path.join(AQUI, "asalto_especieB.npz"))
x80 = dat["x"]; N8 = int(dat["N"])
NG = 100
off = (NG - N8) // 2      # 10
# London del (1/2,-1/4) en la caja grande (centro NG/2)
yy, xx = np.mgrid[0:NG, 0:NG].astype(float)
xx = (xx + 0.5); yy = (yy + 0.5)
cx = cy = NG / 2.0
th = np.arctan2(yy - cy, xx - cx)
rr = np.hypot(xx - cx, yy - cy)
phi = 0.5 * th; alp = -0.25 * th
amp = np.tanh(np.maximum(rr, 1e-9) / 2.0)
c0 = amp * A0 * sq2 * np.cos(2 * alp)
c1 = amp * A0 * sq2 * np.sin(2 * alp)
xL = np.zeros((10, NG, NG))
xL[0] = c0 * np.cos(phi); xL[5] = c0 * np.sin(phi)
xL[1] = c1 * np.cos(phi); xL[6] = c1 * np.sin(phi)
# embebido con blending: dentro de r<30 el GL manda; 30..36 mezcla; fuera London
xG = xL.copy()
r80 = np.hypot((np.mgrid[0:N8, 0:N8][1] + 0.5) - N8 / 2,
               (np.mgrid[0:N8, 0:N8][0] + 0.5) - N8 / 2)
w_gl = np.clip((36.0 - r80) / 6.0, 0.0, 1.0)      # 1 dentro, 0 fuera
for a in range(10):
    xG[a, off:off + N8, off:off + N8] = (w_gl * x80[a]
                                         + (1 - w_gl) * xL[a, off:off + N8, off:off + N8])
# control del empalme: discrepancia GL vs London en el anillo 28<r<30
sel = (r80 > 28) & (r80 < 30)
disc = max(np.abs(x80[a][sel] - xL[a, off:off + N8, off:off + N8][sel]).max()
           for a in range(10))
stamp(f"empalme: max|GL - London| en anillo r 28-30 = {disc:.4f} (debe ser chico)")

Afield = np.einsum('aij,ayx->yxij', E5, xG[:5] + 1j * xG[5:])
r = rr.ravel()
M = NG * NG

def core_state(kz, rmax=12.0, nev=16):
    Hc = bdg_sparse(Afield, kz).tocsc()
    E, V = spla.eigsh(Hc, k=nev, sigma=0.0, which='LM')
    mejor = None
    for n in range(len(E)):
        if abs(E[n]) > 0.03:
            continue
        w = np.abs(V[:, n])**2
        wsite = w[:M] + w[M:2*M] + w[2*M:3*M] + w[3*M:]
        wsite /= wsite.sum()
        wc = wsite[r < rmax].sum()
        if mejor is None or wc > mejor[1]:
            mejor = (float(E[n]), float(wc))
    return mejor

stamp("rama de core del B en caja 100 (zona central + zona critica ±0.55-0.62):")
print("   kz      E         w(r<12)", flush=True)
for kz in list(np.arange(-0.09, 0.091, 0.03)) + \
          [0.50, 0.53, 0.545, 0.56, 0.568, 0.575, 0.59, 0.61,
           -0.50, -0.53, -0.545, -0.56, -0.568, -0.575, -0.59, -0.61]:
    m = core_state(kz)
    if m:
        print(f"  {kz:+.3f}  {m[0]:+.6f}  {m[1]:.2f}", flush=True)
    else:
        print(f"  {kz:+.3f}  (sin estado de core |E|<0.03)", flush=True)
stamp("FIN")
