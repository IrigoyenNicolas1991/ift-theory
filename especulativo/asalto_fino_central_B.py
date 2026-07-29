import numpy as np, os, time
import scipy.sparse as sp
import scipy.sparse.linalg as spla

AQUI = r"C:\ClaudeInMyComputer\TCI CON Fable New folder\ift-theory\especulativo"
E5 = np.zeros((5, 3, 3))
E5[0] = np.diag([1, -1, 0]) / np.sqrt(2)
E5[1] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / np.sqrt(2)
E5[2] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]]) / np.sqrt(2)
E5[3] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]]) / np.sqrt(2)
E5[4] = np.diag([-1, -1, 2]) / np.sqrt(6)
H_LAT, MU, KF, DELTA0 = 1.0, 0.64, 0.8, 0.6

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

dat = np.load(os.path.join(AQUI, "asalto_especieB.npz"))
x = dat["x"]; N = int(dat["N"])
Afield = np.einsum('aij,ayx->yxij', E5, x[:5] + 1j * x[5:])
yy, xx = np.mgrid[0:N, 0:N].astype(float)
xx = (xx + 0.5); yy = (yy + 0.5)
r = np.hypot(xx - N / 2, yy - N / 2).ravel()
M = N * N

print("barrido fino central del B: estado de CORE (w(r<12) max, |E|<0.02) por kz")
print("   kz      E         w(r<12)")
for kz in np.arange(-0.13, 0.131, 0.013):
    Hc = bdg_sparse(Afield, kz).tocsc()
    E, V = spla.eigsh(Hc, k=16, sigma=0.0, which='LM')
    mejor = None
    for n in range(len(E)):
        if abs(E[n]) > 0.02:
            continue
        w = np.abs(V[:, n])**2
        wsite = w[:M] + w[M:2 * M] + w[2 * M:3 * M] + w[3 * M:]
        wsite /= wsite.sum()
        w12 = wsite[r < 12].sum()
        if mejor is None or w12 > mejor[2]:
            mejor = (kz, float(E[n]), float(w12))
    if mejor:
        print(f"  {mejor[0]:+.3f}  {mejor[1]:+.6f}  {mejor[2]:.2f}", flush=True)
print("FIN")
