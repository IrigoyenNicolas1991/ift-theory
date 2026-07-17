# ETAPA ESPECULATIVA TCI 2.0 - calculo preliminar, no validado (2026-07-17)
# ============================================================================
# ARQUITECTURA B: espectro de la fase CICLICA (A ~ diag(1, w, w^2), w=e^{2pi i/3})
# ----------------------------------------------------------------------------
# La ciclica anula Tr(A^2) exactamente => se selecciona agregando b1|TrA^2|^2 con
# b1>0 (DECLARADO: rol de la correccion de strong coupling que la literatura
# dice que favorece la ciclica; el cuartico weak-coupling la deja casi degenerada
# con las nematicas). Estabilizador esperado: grupo tetraedrico T (discreto)
# combinado con fase => 4 generadores rotos (3 rot + U(1)) => 4 Goldstones.
# CAVEAT DECLARADO: la ciclica rompe inversion temporal => podria haber termino
# de Berry de 1er orden en el tiempo (estructura type-B) que esta maquinaria
# (2do orden) NO captura. Primera pasada exploratoria.
# ============================================================================
import numpy as np

src = open('espectro_biaxial_3p2.py').read().split('# ============================ CASOS')[0]
exec(src)

rng = np.random.default_rng(31)
K = 1.0

# potencial: al*t + be*(t^2 - tr(A*2A2)) + b1*|TrA^2|^2  (b1>0 selecciona ciclica)
def Vc(x, al, be, b1):
    A = Amat(x); Ab = np.conj(A)
    t = np.real(np.trace(A @ Ab))
    u = np.trace(A @ A)
    q4 = t**2 - np.real(np.trace(Ab @ Ab @ A @ A))
    return al * t + be * q4 + b1 * np.real(u * np.conj(u))

def gradc(x, *p, h=1e-6):
    g = np.zeros(10)
    for a in range(10):
        dx = np.zeros(10); dx[a] = h
        g[a] = (Vc(x + dx, *p) - Vc(x - dx, *p)) / (2 * h)
    return g

def hessc(x, *p, h=1e-4):
    H = np.zeros((10, 10))
    for i in range(10):
        for j in range(i, 10):
            di = np.zeros(10); di[i] = h
            dj = np.zeros(10); dj[j] = h
            H[i, j] = (Vc(x+di+dj, *p) - Vc(x+di-dj, *p) - Vc(x-di+dj, *p) + Vc(x-di-dj, *p)) / (4*h*h)
            H[j, i] = H[i, j]
    return H

def find_min_c(x0, params, iters=60000, lr=0.01):
    x = x0.astype(float).copy()
    for _ in range(iters):
        gv = gradc(x, *params)
        if np.linalg.norm(gv) < 1e-10:
            break
        x -= lr * gv
    return x

al, be, b1 = -1.0, 1.0, 1.5
params = (al, be, b1)

# semilla ciclica + ruido; y semilla aleatoria como control de convergencia
w = np.exp(2j*np.pi/3)
Acyc = np.diag([1, w, w**2]) / np.sqrt(3) * 0.7
seeds = [xvec(Acyc) + 0.02*rng.standard_normal(10),
         0.4*rng.standard_normal(10)]

for si, x0 in enumerate(seeds):
    xm = find_min_c(x0, params)
    A0 = Amat(xm)
    ev = np.linalg.eigvals(A0)
    u = np.trace(A0 @ A0)
    t = np.real(np.trace(A0 @ np.conj(A0)))
    print("=" * 78)
    print(f"SEMILLA {si}: |grad| = {np.linalg.norm(gradc(xm, *params)):.2e}   V = {Vc(xm, *params):.6f}")
    print(f"  |autovalores| = {np.sort(np.abs(ev))}   (ciclica: los 3 iguales)")
    print(f"  |TrA^2| = {abs(u):.2e}  (ciclica: 0)   Tr(AA*) = {t:.4f}")
    M = hessc(xm, *params)
    wM = np.sort(np.linalg.eigvalsh(M))
    nz = np.sum(np.abs(wM) < 1e-6)
    R = broken_dirs(xm)
    rank = np.linalg.matrix_rank(R, tol=1e-6) if len(R) else 0
    print(f"  rotos (rot+U1): {rank}   gapless k=0: {nz}   masas^2 no nulas: {wM[np.abs(wM)>1e-6][:4]}")
    if si == 0:
        # espectro direccional + mini-mapa de anisotropia
        for kdir, name in [(np.array([0,0,1.]), "k||z"), (np.array([1,0,0.]), "k||x"),
                           (np.array([1,1,1.])/np.sqrt(3), "k||(111)"),
                           (np.array([1,1,0.])/np.sqrt(2), "k||(110)")]:
            kk = 1e-3 * kdir
            w2, U = np.linalg.eigh(M + Kgrad(kk, K))
            out = []
            for m in range(10):
                if w2[m] < (10e-3)**2:
                    v = np.sqrt(max(w2[m], 0))/1e-3
                    h2, h1, h0 = helicity_content(U[:, m], kk)
                    cls = "TT" if h2 > 0.9 else ("V" if h1 > 0.9 else ("S" if h0 > 0.9 else f"mix({h2:.2f}/{h1:.2f}/{h0:.2f})"))
                    out.append(f"{cls} v={v:.3f}")
            print(f"  {name}: " + " | ".join(out))
        # mini-mapa: 200 direcciones
        Nk = 200
        i2 = np.arange(Nk)
        phig = np.pi*(3-np.sqrt(5))*i2
        zz = 1 - 2*(i2+0.5)/Nk
        rr = np.sqrt(1-zz*zz)
        kds = np.stack([rr*np.cos(phig), rr*np.sin(phig), zz], axis=1)
        tt_best, tt_2nd, v_tt = [], [], []
        for kd in kds:
            kk = 1e-3*kd
            w2, U = np.linalg.eigh(M + Kgrad(kk, K))
            hs, vs = [], []
            for m in range(10):
                if w2[m] < (10e-3)**2:
                    h2, h1, h0 = helicity_content(U[:, m], kk)
                    hs.append(h2); vs.append(np.sqrt(max(w2[m],0))/1e-3)
            hs = np.array(hs); vs = np.array(vs)
            o = np.argsort(-hs)
            tt_best.append(hs[o[0]]); tt_2nd.append(hs[o[1]]); v_tt.append(vs[o[0]])
        tt_best = np.array(tt_best); tt_2nd = np.array(tt_2nd); v_tt = np.array(v_tt)
        print(f"  MINI-MAPA ({Nk} dir): TT mejor modo media {tt_best.mean():.3f} min {tt_best.min():.3f}")
        print(f"                        TT 2do modo   media {tt_2nd.mean():.3f} min {tt_2nd.min():.3f}")
        print(f"                        v_TT anisotropia {(v_tt.max()-v_tt.min())/v_tt.mean()*100:.1f} %  (D4 daba 12.6%)")
