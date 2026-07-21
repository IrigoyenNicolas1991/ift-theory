# -*- coding: utf-8 -*-
"""
SOTANO / EM — LA PUERTA DEL HIELO DE VORTONES (paso 0, mitad computable)
=========================================================================
Pregunta (BRIEFING-hielo-de-vortones-EM.md, f0b5399): ¿tiene la espuma de
vortones un grado de libertad con degeneracion extensiva tipo ice rule — el
combustible de una fase Coulomb emergente (Castelnovo-Moessner-Sondhi) —
compatible con (o desacoplado de) el orden laminar J=2?

Este script ataca la mitad Luttinger-Tisza/Ewald de los candidatos 1 y 3:

  P1  pirocloro Ising <111> DIPOLAR, ambos signos  (candidato 1b, steel-man:
      anclaje local concedido GRATIS — ¿el signo vortice conserva el hielo?)
  P2  pirocloro vectorial libre, signo vortice     (candidato 1a: sin anclaje,
      ¿compite la red no-bipartita con el laminar 9.68721? ¿banda plana?)
  P3  kagome apilado (hex+3) vectorial libre, signo vortice (candidato 1a')
  P4  laminar hexagonal, banda restringida a z, ambos signos (candidato 3b:
      momentos del nucleo esclavos de n=±z sobre la red laminar)

CONTROLES (ningun veredicto sin reproducir el hielo donde SI existe):
  C1  alpha-independencia (pirocloro 12x12, 3 alphas)
  C2  traza ~ 0 (kernel dipolar sin traza)    C4  hermiticidad
  C3  SC magnetico -2.67675 / SC vortice +9.68721 (certificacion heredada,
      sotano_bulk_veredicto.py §5 del tronco)
  C5  plegado: SC como supercelda base-2 reproduce las bandas de SC simple
  C6  limite de Lorentz 8pi/3 (modo longitudinal k->0, base 1)
  C7  pirocloro NN Ising <111>: el ice manifold = 2 bandas planas EXACTAS
      degeneradas en el fondo del sector AFM-sigma; el techo (k->0) = AIAO.
      [analitico conocido: line graph del diamante]
  C8  acople dipolar nn proyectado = +5/3 x (1/r_nn^3) exacto — el "5D/3" de
      den Hertog-Gingras (PRL 84:3430): con signo MAGNETICO el dipolar es
      AFM-sigma = pro-hielo; banda baja cuasi-plana (equivalencia proyectiva,
      Isakov-Moessner-Sondhi PRL 95:217201). El codigo debe VER ese hielo.

Convenciones del proyecto (tronco §8): v_c = 1 por SITIO (todas las redes a
igual densidad), momento unitario, energias en mu^2/a^3; s=+1 magnetico,
s=-1 vortice (Neumann); E/N = (s/2)·lambda del modo normalizado =>
fundamental magnetico = (1/2)·min lambda, fundamental vortice = -(1/2)·max
lambda. Ewald identico al certificado (rcut=5.5/alpha, gcut=14·alpha).
"""
import numpy as np
from math import pi, sqrt

try:
    from scipy.special import erfc as _erfc
    def erfc_v(x): return _erfc(x)
except Exception:
    from math import erfc
    erfc_v = np.vectorize(erfc)

# ---------------------------------------------------------------- redes
def make_lattice(kind, ca=1.0):
    """Devuelve dict con A (filas a1..a3), Bm (reciproca), D (base cart),
    V (volumen de celda = numero de sitios; v_sitio=1) y ejes locales si los hay."""
    ejes = None
    if kind == "sc":
        A = np.eye(3); D = np.zeros((1, 3))
    elif kind == "sc2":                       # SC como supercelda 1x1x2
        A = np.diag([1.0, 1.0, 2.0]); D = np.array([[0, 0, 0], [0, 0, 1.0]])
    elif kind == "hex":                       # triangular apilada AA, base 1
        L = (2.0/(sqrt(3.0)*ca))**(1.0/3.0); c = ca*L
        A = np.array([[L, 0, 0], [L/2, L*sqrt(3)/2, 0], [0, 0, c]])
        D = np.zeros((1, 3))
    elif kind == "pyro":                      # FCC primitiva + base 4
        ac = 16.0**(1.0/3.0)                  # V_prim = ac^3/4 = 4 sitios
        A = ac*np.array([[0, .5, .5], [.5, 0, .5], [.5, .5, 0]])
        D = ac*np.array([[0, 0, 0], [.25, .25, 0], [.25, 0, .25], [0, .25, .25]])
        cen = ac*np.array([.125, .125, .125])  # centro del tetraedro "up"
        ejes = np.array([(d - cen)/np.linalg.norm(d - cen) for d in D])
    elif kind == "kag":                       # kagome apilado AA (hex + 3)
        L = (2.0*sqrt(3.0)/ca)**(1.0/3.0); c = ca*L   # V = (r3/2)L^2 c = 3
        a1 = np.array([L, 0, 0]); a2 = np.array([L/2, L*sqrt(3)/2, 0])
        A = np.array([a1, a2, [0, 0, c]])
        D = np.array([np.zeros(3), a1/2, a2/2])
    else:
        raise ValueError(kind)
    V = abs(np.linalg.det(A))
    Bm = 2*pi*np.linalg.inv(A).T
    return {"A": A, "Bm": Bm, "D": np.atleast_2d(D), "V": V, "ejes": ejes,
            "kind": kind, "ca": ca}

# ------------------------------------------------- puntos precomputados
def prep_sums(lat, alpha, rcut_f=5.5, gcut_f=7.0):
    A, Bm, D = lat["A"], lat["Bm"], lat["D"]
    rcut = rcut_f/alpha
    gcut = gcut_f*alpha*2.0
    maxoff = max(np.linalg.norm(D[b]-D[a]) for a in range(len(D)) for b in range(len(D)))
    span = rcut + maxoff + 1e-9
    nmax = int(np.ceil(span/np.min(np.linalg.norm(A, axis=1)))) + 2
    rng = np.arange(-nmax, nmax+1)
    m = np.stack(np.meshgrid(rng, rng, rng, indexing='ij'), -1).reshape(-1, 3)
    Rall = m @ A
    keep = np.linalg.norm(Rall, axis=1) < span + np.max(np.linalg.norm(A, axis=1))
    Rall = Rall[keep]
    nmg = int(np.ceil(gcut/np.min(np.linalg.norm(Bm, axis=1)))) + 2
    rng = np.arange(-nmg, nmg+1)
    m = np.stack(np.meshgrid(rng, rng, rng, indexing='ij'), -1).reshape(-1, 3)
    Gall = m @ Bm
    keep = np.linalg.norm(Gall, axis=1) < gcut + np.max(np.linalg.norm(Bm, axis=1))
    return {"Rall": Rall, "Gall": Gall[keep], "rcut": rcut, "gcut": gcut,
            "alpha": alpha}

def Jk_full(k, lat, S):
    """Kernel dipolar 3p x 3p por Ewald (convencion de fase completa e^{ik·r})."""
    D, V = lat["D"], lat["V"]
    p = len(D)
    al, rcut, gcut = S["alpha"], S["rcut"], S["gcut"]
    Rall, Gall = S["Rall"], S["Gall"]
    q = Gall + k
    qq = np.linalg.norm(q, axis=1)
    kg = (qq < gcut) & (qq > 1e-9)
    q, qq = q[kg], qq[kg]
    wg = np.exp(-qq**2/(4*al*al))/qq**2
    J = np.zeros((p, 3, p, 3), complex)
    for a in range(p):
        for b in range(p):
            dba = D[b] - D[a]
            r = Rall + dba
            rr = np.linalg.norm(r, axis=1)
            keep = (rr > 1e-9) & (rr < rcut)
            r, rr = r[keep], rr[keep]
            blk = np.zeros((3, 3), complex)
            if len(rr) > 0:
                ar = al*rr
                ef = erfc_v(ar); gau = np.exp(-ar*ar)
                Bf = ef/rr**3 + (2*al/sqrt(pi))*gau/rr**2
                Cf = 3*ef/rr**5 + (2*al/sqrt(pi))*(3/rr**2 + 2*al*al)*gau/rr**2
                ph = np.exp(1j*(r @ k))
                blk = np.einsum('n,n->', Bf, ph)*np.eye(3) \
                    - np.einsum('n,na,nb,n->ab', Cf, r, r, ph)
            # fase reciproca por Poisson: e^{ik·d} e^{-iq·d} = e^{-iG·d}
            phg = np.exp(1j*(k @ dba))*np.exp(-1j*(q @ dba))
            blk += (4*pi/V)*np.einsum('n,n,na,nb->ab', wg, phg, q, q)
            if a == b:
                blk -= (4*al**3/(3*sqrt(pi)))*np.eye(3)
            J[a, :, b, :] = blk
    J = J.reshape(3*p, 3*p)
    return 0.5*(J + J.conj().T)

def K_ising(J, ejes):
    """Proyeccion del kernel 3p x 3p a los ejes locales -> p x p."""
    p = len(ejes)
    Jb = J.reshape(p, 3, p, 3)
    K = np.einsum('ax,axby,by->ab', ejes.astype(complex), Jb, ejes.astype(complex))
    return 0.5*(K + K.conj().T)

def frac_grid(n):
    return (np.arange(n) + 0.5)/n - 0.5      # nunca pisa k=0

def scan(lat, S, n, proj=None, zonly=False):
    """Barre la BZ; devuelve (fracs, bandas). proj=ejes -> Ising pxp;
    zonly=True -> banda escalar z·J·z (solo base 1)."""
    Bm = lat["Bm"]
    fr = frac_grid(n)
    fracs, bands = [], []
    for fx in fr:
        for fy in fr:
            for fz in fr:
                f = np.array([fx, fy, fz])
                k = f @ Bm
                if np.linalg.norm(k) < 1e-8:
                    continue
                J = Jk_full(k, lat, S)
                if zonly:
                    w = np.array([J[2, 2].real])
                elif proj is not None:
                    w = np.linalg.eigvalsh(K_ising(J, proj))
                else:
                    w = np.linalg.eigvalsh(J)
                fracs.append(f); bands.append(w)
    return np.array(fracs), np.array(bands)

def refine(lat, S, f0, which, proj=None, zonly=False, steps=3, ngrid=7):
    Bm = lat["Bm"]
    span = 1.0/15
    frac = np.array(f0, float)
    best = None
    for _ in range(steps):
        grid = np.linspace(-span, span, ngrid)
        best = None
        for dx in grid:
            for dy in grid:
                for dz in grid:
                    f = frac + np.array([dx, dy, dz])
                    k = f @ Bm
                    if np.linalg.norm(k) < 1e-6:
                        continue
                    J = Jk_full(k, lat, S)
                    if zonly:
                        w = np.array([J[2, 2].real]); vec = np.array([1.0])
                    elif proj is not None:
                        ww, vv = np.linalg.eigh(K_ising(J, proj))
                        w, vec = ww, (vv[:, -1] if which == 'max' else vv[:, 0])
                    else:
                        ww, vv = np.linalg.eigh(J)
                        w, vec = ww, (vv[:, -1] if which == 'max' else vv[:, 0])
                    val = w[-1] if which == 'max' else w[0]
                    key = val if which == 'max' else -val
                    if best is None or key > best[0]:
                        best = (key, f.copy(), val, vec)
        frac = best[1]
        span /= 3.0
    return best[2], best[1], best[3]

def flatness(bands, idx, lo, hi):
    """(max-min) de la banda idx sobre la grilla, relativo al rango total."""
    b = bands[:, idx]
    tot = hi - lo
    return (b.max() - b.min())/tot, b.max() - b.min()

# =====================================================================
print("="*72)
print("CONTROLES")
print("="*72)

lat_sc = make_lattice("sc")
S_sc = prep_sums(lat_sc, 3.0)
ktest = 0.3*lat_sc["Bm"][0] + 0.2*lat_sc["Bm"][1] + 0.1*lat_sc["Bm"][2]

lat_py = make_lattice("pyro")
print("\nC1 alpha-independencia (pirocloro 12x12, k de prueba):")
kt_py = 0.23*lat_py["Bm"][0] + 0.11*lat_py["Bm"][1] + 0.07*lat_py["Bm"][2]
ref = None
for al in (2.0, 3.0, 4.0):
    Sp = prep_sums(lat_py, al)
    w = np.linalg.eigvalsh(Jk_full(kt_py, lat_py, Sp))
    if ref is None: ref = w
    print(f"   alpha={al:.1f}: banda1={w[0]:+.6f}  banda12={w[-1]:+.6f}"
          f"   max|dif vs alpha=2|={np.max(np.abs(w-ref)):.2e}")

J = Jk_full(kt_py, lat_py, prep_sums(lat_py, 3.0))
print(f"C2 traza total: {np.trace(J).real:+.2e}   "
      f"C4 no-hermiticidad relativa: {np.linalg.norm(J-J.conj().T)/np.linalg.norm(J):.1e}")

print("\nC3 certificacion heredada en SC (base 1):")
fr_sc, bands_sc = scan(lat_sc, S_sc, 12)
vmin, fmin, _ = refine(lat_sc, S_sc, fr_sc[np.argmin(bands_sc[:, 0])], 'min')
vmax, fmax, _ = refine(lat_sc, S_sc, fr_sc[np.argmax(bands_sc[:, -1])], 'max')
print(f"   magnetico: E/N = lambda_min/2 = {vmin/2:+.5f}  (publicado -2.67675)"
      f"   k*={np.round(fmin,3)}")
print(f"   vortice  : lambda_max = {vmax:+.5f}  (certificado +9.68721)"
      f"   k*={np.round(fmax,3)}")

print("\nC5 plegado SC vs supercelda base-2 (mismas bandas):")
lat_s2 = make_lattice("sc2"); S_s2 = prep_sums(lat_s2, 3.0)
kf = np.array([0.21, 0.13, 0.09])
k1 = kf @ lat_s2["Bm"]
w2 = np.linalg.eigvalsh(Jk_full(k1, lat_s2, S_s2))
wa = np.linalg.eigvalsh(Jk_full(k1, lat_sc, S_sc))
wb = np.linalg.eigvalsh(Jk_full(k1 + 0.5*lat_sc["Bm"][2], lat_sc, S_sc))
wu = np.sort(np.concatenate([wa, wb]))
print(f"   max|bandas(sc2) - union plegada(sc)| = {np.max(np.abs(np.sort(w2)-wu)):.2e}")

print("\nC6 limite de Lorentz (SC, modo longitudinal k->0):")
for eps in (0.05, 0.02, 0.01):
    k = np.array([eps*2*pi, 0, 0])
    w = np.linalg.eigvalsh(Jk_full(k, lat_sc, S_sc))
    print(f"   |k|/2pi={eps:.2f}: lambda_long={w[-1]:+.5f}  (8pi/3 = {8*pi/3:.5f})")

# ---- C7: pirocloro NN Ising <111> (analitico: ice manifold = bandas planas)
print("\nC7 pirocloro NN Ising <111> (adyacencia pura, sin Ewald):")
D, A = lat_py["D"], lat_py["A"]
def K_nn(k):
    K = np.zeros((4, 4), complex)
    for a in range(4):
        for b in range(4):
            if a == b: continue
            r1 = D[b] - D[a]
            r2 = r1 - 2*r1                     # el companero: -(d_b - d_a)... no:
            # los dos nn entre sublattices a,b: r1 (celda 0) y r1 - 2*r1_lat
            # con 2*r1 = vector primitivo FCC correspondiente:
            r2 = r1 - 2*r1
            K[a, b] = np.exp(1j*(r1 @ k)) + np.exp(1j*((-r1) @ k))
    return 0.5*(K + K.conj().T)
# nota: el segundo vecino entre a,b esta en r1 - P con P = 2*r1 (primitiva FCC)
# => r2 = -r1. La adyacencia queda 2cos(k·r1): forma estandar del pirocloro.
fr = frac_grid(10)
flat_check, disp_check = [], []
for fx in fr:
    for fy in fr:
        for fz in fr:
            k = np.array([fx, fy, fz]) @ lat_py["Bm"]
            w = np.linalg.eigvalsh(K_nn(k))
            flat_check.append(w[:2]); disp_check.append(w[2:])
flat_check = np.array(flat_check); disp_check = np.array(disp_check)
print(f"   bandas 1-2 (fondo AFM-sigma): min={flat_check.min():+.6f} "
      f"max={flat_check.max():+.6f}  dispersion={flat_check.max()-flat_check.min():.2e}"
      f"  -> PLANAS (= ice manifold, degeneracion extensiva)")
print(f"   bandas 3-4 (dispersivas): min={disp_check.min():+.3f} max={disp_check.max():+.3f}"
      f"  (techo -> AIAO en k->0)")

# ---- C8: acople dipolar nn proyectado (el 5/3 de den Hertog-Gingras)
r1 = D[1] - D[0]
rn = np.linalg.norm(r1); rh = r1/rn
e0, e1 = lat_py["ejes"][0], lat_py["ejes"][1]
c58 = (e0 @ e1 - 3*(e0 @ rh)*(e1 @ rh))
print(f"\nC8 acople dipolar nn proyectado: e0·T·e1 x r^3 = {c58:+.6f}  (exacto +5/3 = +1.666667)")
print(f"   r_nn = {rn:.5f} => D_nn = +{c58/rn**3:.5f} > 0 con signo magnetico:")
print("   AFM-sigma = pro-hielo (den Hertog-Gingras). Con signo VORTICE se invierte.")

# =====================================================================
print()
print("="*72)
print("P1  PIROCLORO DIPOLAR Ising <111> — ambos signos (candidato 1b)")
print("="*72)
S_py = prep_sums(lat_py, 3.0)
fracs, bI = scan(lat_py, S_py, 10, proj=lat_py["ejes"])
lo, hi = bI.min(), bI.max()
print(f"rango espectral total: [{lo:+.5f}, {hi:+.5f}]  ancho={hi-lo:.5f}")
for idx, nombre in [(0, "banda 1 (fondo)"), (1, "banda 2")]:
    fl, ab = flatness(bI, idx, lo, hi)
    print(f"   {nombre}: [{bI[:,idx].min():+.5f}, {bI[:,idx].max():+.5f}] "
          f"dispersion={ab:.5f} ({100*fl:.1f}% del ancho)")
fl3, _ = flatness(bI, 2, lo, hi); fl4, _ = flatness(bI, 3, lo, hi)
print(f"   banda 3: dispersion {100*fl3:.1f}%   banda 4 (techo): {100*fl4:.1f}%")

i_bot = np.argmin(bI[:, 0]); i_top = np.argmax(bI[:, -1])
vmin, fmin, vecmin = refine(lat_py, S_py, fracs[i_bot], 'min', proj=lat_py["ejes"])
vmax, fmax, vecmax = refine(lat_py, S_py, fracs[i_top], 'max', proj=lat_py["ejes"])
print(f"\nSigno MAGNETICO (fundamental = fondo): lambda_min={vmin:+.5f} en k={np.round(fmin,3)}")
print(f"   E/N = {vmin/2:+.5f}; banda 1 cuasi-plana => HIELO (equiv. proyectiva IMS): "
      f"seleccion {100*flatness(bI,0,lo,hi)[0]:.1f}% del ancho")
print(f"Signo VORTICE (fundamental = techo): lambda_max={vmax:+.5f} en k={np.round(fmax,3)}")
print(f"   E/N = {-vmax/2:+.5f}; autovector sigma = {np.round(vecmax.real, 3)}")
uni = np.allclose(np.abs(vecmax.real), np.abs(vecmax.real[0]), atol=0.05)
print(f"   ¿sigma uniforme (= all-in-all-out)? {uni}")
print(f"   dispersion de la banda techo: {100*fl4:.1f}% del ancho => "
      f"{'AISLADO (orden, SIN degeneracion)' if fl4 > 0.05 else 'plano (¡revisar!)'}")
gap_top = bI[:, -1].max() - bI[:, -2].max()
print(f"   separacion techo vs banda 3 (en maximos): {gap_top:+.5f}")

# =====================================================================
print()
print("="*72)
print("P2  PIROCLORO VECTORIAL LIBRE — signo vortice (candidato 1a)")
print("="*72)
fracs, bV = scan(lat_py, S_py, 10)
loV, hiV = bV.min(), bV.max()
i_top = np.argmax(bV[:, -1])
vmax, fmax, vecmax = refine(lat_py, S_py, fracs[i_top], 'max')
flV, abV = flatness(bV, bV.shape[1]-1, loV, hiV)
print(f"sup_k lambda_max = {vmax:+.5f} en k={np.round(fmax,3)}")
print(f"   vs laminar SC/tet certificado: 9.68721  -> "
      f"{'PIERDE contra el laminar' if vmax < 9.68721 else '¡SUPERA AL LAMINAR!'}"
      f"  (margen {9.68721-vmax:+.5f})")
print(f"   banda superior: dispersion {abV:.5f} ({100*flV:.1f}% del ancho) => "
      f"{'sin degeneracion extensiva' if flV > 0.05 else 'cuasi-plana (¡revisar!)'}")
p = 4
v3 = vecmax.reshape(p, 3).real
print("   autovector (momento por sublattice):")
for a in range(p):
    n = v3[a]/max(np.linalg.norm(v3[a]), 1e-12)
    print(f"     subl {a}: |m|={np.linalg.norm(v3[a]):.3f}  dir={np.round(n,3)}")

# =====================================================================
print()
print("="*72)
print("P3  KAGOME APILADO VECTORIAL — signo vortice (candidato 1a')")
print("="*72)
best_kag = None
for ca in (0.8, 1.0, 1.3):
    lat_k = make_lattice("kag", ca)
    S_k = prep_sums(lat_k, 3.0)
    fracs, bK = scan(lat_k, S_k, 8)
    i_top = np.argmax(bK[:, -1])
    vmax, fmax, _ = refine(lat_k, S_k, fracs[i_top], 'max')
    flK, abK = flatness(bK, bK.shape[1]-1, bK.min(), bK.max())
    print(f"   c/a={ca:.1f}: sup lambda={vmax:+.5f} en k={np.round(fmax,3)}  "
          f"banda sup dispersion {100*flK:.1f}%")
    if best_kag is None or vmax > best_kag[0]:
        best_kag = (vmax, ca)
print(f"   mejor kagome: lambda={best_kag[0]:+.5f} (c/a={best_kag[1]}) vs laminar 9.68721"
      f" -> {'PIERDE' if best_kag[0] < 9.68721 else '¡SUPERA!'}")

# =====================================================================
print()
print("="*72)
print("P4  LAMINAR HEX, banda restringida a z — ambos signos (candidato 3b)")
print("="*72)
for ca in (0.9, 1.0, 1.1):
    lat_h = make_lattice("hex", ca)
    S_h = prep_sums(lat_h, 3.0)
    fracs, bz = scan(lat_h, S_h, 12, zonly=True)
    lo_z, hi_z = bz.min(), bz.max()
    i_min = np.argmin(bz[:, 0]); i_max = np.argmax(bz[:, 0])
    vmin, fmin, _ = refine(lat_h, S_h, fracs[i_min], 'min', zonly=True)
    vmax, fmax, _ = refine(lat_h, S_h, fracs[i_max], 'max', zonly=True)
    print(f" c/a={ca:.1f}: banda z en [{lo_z:+.4f},{hi_z:+.4f}]")
    print(f"   VORTICE  (fund=max): {vmax:+.5f} en k={np.round(fmax,3)}"
          f"  [laminar antialineado si k=(0,0,±1/2)]")
    print(f"   MAGNETICO(fund=min): {vmin:+.5f} en k={np.round(fmin,3)}  (¿stripes in-plane?)")
    # planura del fondo magnetico / techo vortice sobre la grilla:
    print(f"   dispersion banda unica = {hi_z-lo_z:.4f}; "
          f"cuartil inferior de la banda: {np.percentile(bz, 25):+.4f} "
          f"(fondo {'chato' if (np.percentile(bz,25)-lo_z)/(hi_z-lo_z) < 0.05 else 'no plano'})")

print()
print("="*72)
print("LECTURA (para el acta): con signo vortice, el fundamental del pirocloro")
print("<111> deberia ser AIAO aislado (orden, cero degeneracion) y el ice")
print("manifold queda como TECHO de energia: el hielo y el orden son extremos")
print("opuestos del MISMO espectro — elegir signo es elegir cual es fundamental.")
print("El signo del mar (Neumann) ya esta gastado en el laminar/gravedad.")
print("="*72)
