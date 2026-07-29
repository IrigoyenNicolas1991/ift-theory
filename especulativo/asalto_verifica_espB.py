# ETAPA ESPECULATIVA TCI 2.0 - verificador del C_B=-2 de la especie B
# Los 10 cruces del BdG de la especie B tienen peso de core 0.42-0.48 (contra
# 0.85 del A). Antes de creer el conteo: re-diagonalizar en los kz de cruce y
# mirar el PERFIL RADIAL de los estados cercanos a E=0 — ¿core gordo que
# desborda el disco r<8 (peso legitimo) o mezcla interfaz/bulk (espurio)?
# Reporta pesos con discos r<8/12/16 y el perfil por anillos del estado.
import numpy as np, os, json, time
import scipy.sparse as sp
import scipy.sparse.linalg as spla

t0 = time.time()
AQUI = os.path.dirname(os.path.abspath(__file__))
E5 = np.zeros((5, 3, 3))
E5[0] = np.diag([1, -1, 0]) / np.sqrt(2)
E5[1] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / np.sqrt(2)
E5[2] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]]) / np.sqrt(2)
E5[3] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]]) / np.sqrt(2)
E5[4] = np.diag([-1, -1, 2]) / np.sqrt(6)
H_LAT, MU, KF, DELTA0, NEV = 1.0, 0.64, 0.8, 0.6, 60

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
r = np.hypot(xx - N/2, yy - N/2).ravel()
db = np.minimum.reduce([xx, yy, N - xx, N - yy]).ravel()
M = N * N

flujo = np.load(os.path.join(AQUI, "asalto_flujo_espB.npz"), allow_pickle=True)
cruces = json.loads(str(flujo["cruces"]))
print(f"cruces reportados: {[(round(c['kz'],3), c['signo']) for c in cruces]}")
print(f"suma = {sum(c['signo'] for c in cruces)}")
print("\nperfil de los estados |E| minimos en cada kz de cruce:")
print("   kz     E        w(r<8) w(r<12) w(r<16) w(borde)  perfil por anillos [0-4|4-8|8-12|12-16|16-24|24+no-borde]")
for c in cruces:
    kz = c["kz"]
    Hc = bdg_sparse(Afield, kz).tocsc()
    E, V = spla.eigsh(Hc, k=12, sigma=0.0, which='LM')
    orden = np.argsort(np.abs(E))
    for n in orden[:2]:
        w = np.abs(V[:, n])**2
        wsite = w[:M] + w[M:2*M] + w[2*M:3*M] + w[3*M:]
        wsite /= wsite.sum()
        w8 = wsite[r < 8].sum(); w12 = wsite[r < 12].sum(); w16 = wsite[r < 16].sum()
        wb = wsite[db < 6].sum()
        anillos = [wsite[(r >= a) & (r < b)].sum()
                   for a, b in ((0, 4), (4, 8), (8, 12), (12, 16), (16, 24))]
        resto = wsite[(r >= 24) & (db >= 6)].sum()
        print(f"  {kz:+.3f} {E[n]:+.5f}  {w8:.2f}   {w12:.2f}    {w16:.2f}    {wb:.2f}     "
              + " ".join(f"{a:.2f}" for a in anillos) + f" | {resto:.2f}")
print(f"\n[{time.time()-t0:.0f}s] FIN")
