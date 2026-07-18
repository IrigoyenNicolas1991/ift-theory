# ETAPA ESPECULATIVA TCI 2.0 - calculo preliminar, no validado
# ============================================================================
# LA BINARIA DEL MAR (batalla del acople §29, mitad DINAMICA -> bitacora §31):
# dos medios-nudos (HQV) de carga opuesta del mismo sector orbitandose en el
# condensado D4-BN, con evolucion temporal REAL del campo de 10 componentes.
#
# Preguntas: (1) ¿la orbita decae por radiacion (mini-Hulse-Taylor)?
# (2) ¿en que CANALES radia (fase / rot-z [= sectores q+-] / rot-x,y
#     [vectoriales] / amplitud)? — la pregunta del dipolo (§28.3) en miniatura.
# (3) ¿a que frecuencia (dipolo Omega vs cuadrupolo 2*Omega)?
#
# DECLARADO: dinamica de SEGUNDO ORDEN (lagrangiano L = 1/2 xdot^2 - E[x],
# consistente con los espectros §14-16 — el medio TCI es lorentziano de
# fabrica, NO Gross-Pitaevskii; por eso el control Kozik-Svistunov (dinamica
# GP/Magnus de primer orden) NO aplica directo y queda para otra sesion).
# Gradiente espacial isotropo K1 solo (como Parte B de §30, declarado).
# Controles internos: autotest del gradiente analitico; conservacion de
# energia sin esponja (piloto); pureza sectorial de la radiacion.
#
# Uso: python binaria_del_mar.py pilot   (estabilidad + conservacion, corto)
#      python binaria_del_mar.py full    (la corrida real, ~30-40 min)
# ============================================================================
import numpy as np, time, sys

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(11)

E5 = np.zeros((5, 3, 3))
E5[0] = np.diag([1, -1, 0]) / np.sqrt(2)
E5[1] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / np.sqrt(2)
E5[2] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]]) / np.sqrt(2)
E5[3] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]]) / np.sqrt(2)
E5[4] = np.diag([-1, -1, 2]) / np.sqrt(6)

AL, BE, GA, EPS = -1.0, 1.0, +0.15, 0.05   # caso C (§16)
K = 1.0
PARAMS = (AL, BE, GA, EPS)

def V_sites(x, al, be, ga, eps):
    xc = x[:5] + 1j * x[5:]
    A = np.einsum('am,aij->mij', xc, E5); Ab = A.conj()
    t = np.einsum('mij,mij->m', A, Ab).real
    u = np.einsum('mij,mji->m', A, A); ub = u.conj()
    A2 = A @ A; Ab2 = Ab @ Ab
    tr = lambda P, Q: np.einsum('mij,mji->m', P, Q)
    q4 = t**2 - tr(Ab2, A2).real
    M1 = Ab @ A
    s6 = (-3 * t * (u * ub).real + 4 * t**3
          + 6 * t * tr(Ab2, A2).real + 12 * t * tr(M1, M1).real
          - 6 * (ub * tr(Ab @ A2, A)).real - 6 * (u * tr(Ab2 @ Ab, A)).real
          - 12 * tr(Ab2 @ Ab, A @ A2).real + 12 * tr(Ab2 @ A2, M1).real
          + 8 * tr(M1 @ M1, M1).real)
    return al * t + be * q4 + ga * s6 + eps * t**4

def gradV_sites(x, al, be, ga, eps):
    xc = x[:5] + 1j * x[5:]
    A = np.einsum('am,aij->mij', xc, E5); Ab = A.conj()
    t = np.einsum('mij,mij->m', A, Ab).real
    u = np.einsum('mij,mji->m', A, A); ub = u.conj()
    A2 = A @ A; Ab2 = Ab @ Ab; A3 = A2 @ A; Ab3 = Ab2 @ Ab
    AbA = Ab @ A; AAb = A @ Ab
    trc = lambda P, Q: np.einsum('mij,mji->m', P, Q)
    Tr32 = trc(Ab2, A2); Tr1212 = trc(AbA, AbA); T6 = trc(Ab3, A)
    sc = lambda s: s[:, None, None]
    Ab2A = Ab2 @ A; AAb2 = A @ Ab2; AbA2 = Ab @ A2; A2Ab = A2 @ Ab
    P = (al * Ab + be * (2 * sc(t) * Ab - (Ab2A + AAb2)) + eps * 4 * sc(t**3) * Ab)
    if ga != 0.0:
        P = P + ga * (
            -3 * (sc(u * ub) * Ab + 2 * sc(t) * sc(ub) * A)
            + 12 * sc(t**2) * Ab
            + 6 * (sc(Tr32) * Ab + sc(t) * (Ab2A + AAb2))
            + 12 * (sc(Tr1212) * Ab + 2 * sc(t) * (Ab @ AAb))
            - 6 * sc(ub) * (AbA2 + A @ AbA + A2Ab)
            - 6 * (2 * sc(T6) * A + sc(u) * Ab3)
            - 12 * (Ab3 @ A2 + A @ Ab3 @ A + A2 @ Ab3)
            + 12 * (Ab2A @ AbA + AAb2 @ AAb + AbA2 @ Ab2)
            + 24 * AbA @ AbA @ Ab)
    tp = np.einsum('mij,aij->am', P, E5)
    g = np.empty_like(x)
    g[:5] = 2 * tp.real
    g[5:] = -2 * tp.imag
    return g

def V_scalar(x, *p):
    return V_sites(x.reshape(10, 1), *p)[0]

# autotest gradiente
xt = 0.4 * rng.standard_normal((10, 4))
gnum = np.empty((10, 4))
for a in range(10):
    xp = xt.copy(); xp[a] += 1e-6; xm = xt.copy(); xm[a] -= 1e-6
    gnum[a] = (V_sites(xp, *PARAMS) - V_sites(xm, *PARAMS)) / 2e-6
assert np.max(np.abs(gradV_sites(xt, *PARAMS) - gnum)) < 1e-6
print("[autotest] gradiente analitico OK")

# vacio
D = np.diag([1., -1., 0.])
def x_of_A(A):
    return np.concatenate([[np.real(np.trace(A @ E5[a])) for a in range(5)],
                           [np.imag(np.trace(A @ E5[a])) for a in range(5)]])
aa = np.linspace(0.2, 0.9, 1500)
Va = np.array([V_scalar(x_of_A(a * D), *PARAMS) for a in aa])
a0 = aa[np.argmin(Va)]
V0 = V_scalar(x_of_A(a0 * D), *PARAMS)
print(f"[vacio] a = {a0:.5f}")

# ------------------------------------------------------------------ geometria
N = 200
CX = CY = N / 2
R_RING = 70.0      # anillo de medicion
R_INNER = 62.0     # energia interna
R_SP0, R_SP1 = 78.0, 98.0   # esponja
DT = 0.12
XI = 2.0
D0 = 14.0          # separacion inicial de la binaria

yy, xx = np.mgrid[0:N, 0:N].astype(float)
rr = np.hypot(xx - CX, yy - CY)
mask_inner = rr < R_INNER
sponge = np.clip((rr - R_SP0) / (R_SP1 - R_SP0), 0, 1)**2 * 0.06  # gamma(r)

def ansatz(vortices):
    phi = np.zeros((N, N)); alp = np.zeros((N, N)); amp = np.ones((N, N))
    for (cx, cy, w, v) in vortices:
        th = np.arctan2(yy - cy, xx - cx)
        r = np.hypot(xx - cx, yy - cy)
        phi += w * th; alp += v * th
        amp *= np.tanh(np.maximum(r, 1e-9) / XI)
    c0 = amp * a0 * np.sqrt(2) * np.cos(2 * alp)
    c1 = amp * a0 * np.sqrt(2) * np.sin(2 * alp)
    x = np.zeros((10, N, N))
    x[0] = c0 * np.cos(phi); x[5] = c0 * np.sin(phi)
    x[1] = c1 * np.cos(phi); x[6] = c1 * np.sin(phi)
    return x

def energia_partes(x, v):
    gx = x[:, :, 1:] - x[:, :, :-1]; gy = x[:, 1:, :] - x[:, :-1, :]
    Ek = 0.5 * np.sum(v**2)
    Eg = K * (np.sum(gx**2) + np.sum(gy**2))
    Ev = np.sum(V_sites(x.reshape(10, -1), *PARAMS) - V0)
    return Ek, Eg, Ev

def energia_interna(x, v):
    dens = 0.5 * np.sum(v**2, axis=0)
    Vloc = (V_sites(x.reshape(10, -1), *PARAMS) - V0).reshape(N, N)
    gx2 = np.zeros((N, N)); gy2 = np.zeros((N, N))
    gx2[:, :-1] = np.sum((x[:, :, 1:] - x[:, :, :-1])**2, axis=0)
    gy2[:-1, :] = np.sum((x[:, 1:, :] - x[:, :-1, :])**2, axis=0)
    return np.sum((dens + K * (gx2 + gy2) + Vloc)[mask_inner])

def nucleos(x, prev=None):
    """Rastreador TOPOLOGICO: winding de fase del sector q+ por plaqueta.
    psi_{q+} = z0 + i z1 ~ e^{i(phi+2alpha)} lleva winding +1 en el nudo y -1
    en el antinudo — inmune a las ondas de amplitud (los rastreadores de
    amplitud fallaron: el core se rellena, Seo 2015). Aniquilacion = no quedan
    plaquetas con winding. Devuelve (pos_nudo, pos_antinudo, d)."""
    z0 = x[0] + 1j * x[5]; z1 = x[1] + 1j * x[6]
    th = np.angle(z0 + 1j * z1)
    wrap = lambda a: (a + np.pi) % (2 * np.pi) - np.pi
    w = (wrap(np.diff(th, axis=1)[:-1, :])          # lado inferior
         + wrap(np.diff(th, axis=0)[:, 1:])         # lado derecho
         - wrap(np.diff(th, axis=1)[1:, :])         # lado superior (inverso)
         - wrap(np.diff(th, axis=0)[:, :-1]))       # lado izquierdo (inverso)
    w = w / (2 * np.pi)                             # ~ +-1 en los cores
    w[:28, :] = 0; w[-28:, :] = 0; w[:, :28] = 0; w[:, -28:] = 0
    pos = np.argwhere(w > 0.5); neg = np.argwhere(w < -0.5)
    if len(pos) == 0 or len(neg) == 0:
        c = np.array([N / 2., N / 2.])
        return c, c, 0.0
    m1 = pos.mean(axis=0)[::-1] + 0.5               # (x, y) del nudo +
    m2 = neg.mean(axis=0)[::-1] + 0.5               # (x, y) del antinudo
    return m1, m2, float(np.hypot(*(m1 - m2)))

# direcciones de canal (10-dim, vacio uniforme)
L = np.zeros((3, 3, 3))
L[0] = np.array([[0,0,0],[0,0,-1],[0,1,0]]); L[1] = np.array([[0,0,1],[0,0,0],[-1,0,0]])
L[2] = np.array([[0,-1,0],[1,0,0],[0,0,0]])
A0m = a0 * D
def unit(v): return v / np.linalg.norm(v)
u_fase = unit(x_of_A(1j * A0m))
u_rotz = unit(x_of_A(L[2] @ A0m + A0m @ L[2].T))
u_rotx = unit(x_of_A(L[0] @ A0m + A0m @ L[0].T))
u_roty = unit(x_of_A(L[1] @ A0m + A0m @ L[1].T))
u_amp  = unit(x_of_A(A0m))
CANALES = {"fase": u_fase, "rot-z": u_rotz, "rot-x": u_rotx, "rot-y": u_roty, "amp": u_amp}

# anillo de medicion
NRING = 240
ang = np.linspace(0, 2 * np.pi, NRING, endpoint=False)
rix = np.clip(np.round(CX + R_RING * np.cos(ang)).astype(int), 0, N - 1)
riy = np.clip(np.round(CY + R_RING * np.sin(ang)).astype(int), 0, N - 1)

def vel_inicial(vortices, omega, delta=0.35):
    """xdot por rotacion rigida: cada nucleo con velocidad tangencial Omega x r"""
    v = np.zeros((10, N, N))
    for j, (cx, cy, w, va) in enumerate(vortices):
        rx, ry = cx - CX, cy - CY
        vx, vy = -omega * ry, omega * rx
        sp = np.hypot(vx, vy)
        if sp < 1e-12: continue
        ux, uy = vx / sp, vy / sp
        vp = list(vortices); vm = list(vortices)
        vp[j] = (cx + delta * ux, cy + delta * uy, w, va)
        vm[j] = (cx - delta * ux, cy - delta * uy, w, va)
        v += sp * (ansatz(vp) - ansatz(vm)) / (2 * delta)
    return v

def prerelajar(x, vort, pasos=1200, lr=0.04, mom=0.9):
    """relajacion overdamped con cores anclados (protocolo §30 Parte B):
    elimina el exceso de energia del ansatz crudo antes de soltar la dinamica."""
    libre = np.ones((N, N), bool)
    libre[:3, :] = libre[-3:, :] = libre[:, :3] = libre[:, -3:] = False
    for (cx, cy, _, _) in vort:
        libre[np.hypot(xx - cx, yy - cy) <= 2.5] = False
    vel = np.zeros_like(x)
    for it in range(pasos):
        lap = np.zeros_like(x)
        lap[:, 1:-1, 1:-1] = (x[:, 2:, 1:-1] + x[:, :-2, 1:-1] +
                              x[:, 1:-1, 2:] + x[:, 1:-1, :-2] - 4 * x[:, 1:-1, 1:-1])
        F = 2 * K * lap - gradV_sites(x.reshape(10, -1), *PARAMS).reshape(10, N, N)
        vel = mom * vel + lr * F
        vel[:, ~libre] = 0.0
        x = x + vel
    return x

def correr(pasos, con_esponja=True, medir_cada=8, rastro_cada=50, informar=1000,
           prerelax=True):
    # binaria: anti-par del sector q+ : (1/2,1/4) y (-1/2,-1/4)
    vort = [(CX - D0/2, CY, 0.5, 0.25), (CX + D0/2, CY, -0.5, -0.25)]
    x = ansatz(vort)
    if prerelax:
        t0 = time.time()
        Ea = energia_partes(x, np.zeros_like(x))
        x = prerelajar(x, vort)
        Eb = energia_partes(x, np.zeros_like(x))
        print(f"  pre-relajacion: E {sum(Ea):.3f} -> {sum(Eb):.3f}  [{time.time()-t0:.0f}s]")
    m1c, m2c, d_c = nucleos(x)
    print(f"  control rastreador topologico: nudo+ en {m1c}, antinudo en {m2c}, "
          f"d = {d_c:.2f} (debe ~{D0:.0f})")
    # Omega0: con potencial log, v_circ = sqrt(lambda/mu) es INDEPENDIENTE de d
    # (curva de rotacion plana) y semi-relativista -> la binaria radia feroz y
    # se fusiona en pocas vueltas SIEMPRE (fisica de cuerdas globales 2D).
    # Barrido empirico: 0.045-0.059 con el kick actual = plunge en 1/4 vuelta.
    om0 = float(sys.argv[2]) if len(sys.argv) > 2 else 0.054
    v = vel_inicial(vort, om0)
    print(f"  Omega0 = {om0:.4f}  (periodo ~{2*np.pi/om0:.0f} u.t., "
          f"dt={DT} -> ~{int(2*np.pi/om0/DT)} pasos/orbita)")
    E0k, E0g, E0v = energia_partes(x, v)
    print(f"  E inicial: cinetica {E0k:.3f} + gradiente {E0g:.3f} + potencial {E0v:.3f}"
          f" = {E0k+E0g+E0v:.3f}")
    reg_ring = []; reg_d = []; reg_E = []
    prev_nuc = None
    t_ini = time.time()
    for it in range(pasos):
        lap = np.zeros_like(x)
        lap[:, 1:-1, 1:-1] = (x[:, 2:, 1:-1] + x[:, :-2, 1:-1] +
                              x[:, 1:-1, 2:] + x[:, 1:-1, :-2] - 4 * x[:, 1:-1, 1:-1])
        F = 2 * K * lap - gradV_sites(x.reshape(10, -1), *PARAMS).reshape(10, N, N)
        v += DT * F
        if con_esponja:
            v *= (1 - sponge)
        x = x + DT * v
        if (it + 1) % medir_cada == 0:
            reg_ring.append(v[:, riy, rix].copy())
        if (it + 1) % rastro_cada == 0:
            m1, m2, dd = nucleos(x, prev_nuc)
            prev_nuc = (m1, m2)
            vec = m2 - m1
            reg_d.append((it + 1, dd, np.arctan2(vec[1], vec[0])))
            reg_E.append((it + 1, energia_interna(x, v)))
        if informar and (it + 1) % informar == 0:
            dd = reg_d[-1][1]
            print(f"    paso {it+1:6d}: d = {dd:5.2f}   E_int = {reg_E[-1][1]:8.3f}"
                  f"   [{time.time()-t_ini:.0f}s]", flush=True)
    return x, v, np.array(reg_ring), reg_d, reg_E, om0

modo = sys.argv[1] if len(sys.argv) > 1 else "pilot"

if modo == "pilot":
    print("\n=== PILOTO: estabilidad + conservacion (sin esponja, 800 pasos) ===")
    x, v, ring, dts, Es, om0 = correr(800, con_esponja=False, informar=200)
    Ek, Eg, Ev = energia_partes(x, v)
    print(f"  E final: {Ek+Eg+Ev:.3f} (drift = conservacion del integrador)")
    for (it, dd, th) in dts[::4]:
        print(f"    paso {it}: d = {dd:.2f}  angulo = {th:+.2f}")
    sys.exit(0)

if modo == "scan":
    # sondeo corto de Omega0: ¿plunge, orbita o escape en las primeras vueltas?
    print(f"\n=== SCAN Omega0 = {sys.argv[2]} (500 pasos, con esponja) ===")
    x, v, ring, dts, Es, _ = correr(500, informar=0, rastro_cada=25)
    for (it, dd, th) in dts:
        print(f"    paso {it:4d}: d = {dd:5.2f}  ang = {th:+.2f}")
    sys.exit(0)

print("\n=== CORRIDA COMPLETA: captura-plunge-estallido del anti-par q+ ===")
PASOS = 2500
x, v, ring, dts, Es, om0 = correr(PASOS, informar=250, rastro_cada=25)

# datos crudos a disco ANTES de analizar (resiliencia)
np.savez_compressed("binaria_datos.npz", ring=ring, campo_final=x, vel_final=v,
                    d_serie=np.array([(r[0], r[1], r[2]) for r in dts]),
                    Es=np.array(Es), om0=om0)
print("[datos crudos guardados en binaria_datos.npz]")

print("\n--- ANALISIS ---")
# 1) orbita: d(t) y Omega(t); ventana pre-fusion para todo lo espectral
its = np.array([r[0] for r in dts]); ds = np.array([r[1] for r in dts])
ths = np.unwrap(np.array([r[2] for r in dts]))
fusion = np.where(ds == 0.0)[0]
i_fus = fusion[0] if len(fusion) else len(ds)
paso_fus = its[i_fus - 1] if i_fus < len(ds) else PASOS
vivo = slice(0, i_fus)
if i_fus < len(ds):
    print(f"FUSION/ANIQUILACION detectada ~paso {its[i_fus]} (t = {its[i_fus]*DT:.0f} u.t.)")
ds_v, ths_v, its_v = ds[vivo], ths[vivo], its[vivo]
if len(ds_v) > 2:
    n_orb = abs(ths_v[-1] - ths_v[0]) / (2 * np.pi)
    print(f"orbita (pre-fusion): d {ds_v[0]:.2f} -> {ds_v[-1]:.2f} en {n_orb:.2f} vueltas")
    mitad = len(ds_v) // 2
    print(f"  d medio 1ra mitad: {ds_v[:mitad].mean():.2f}   2da mitad: {ds_v[mitad:].mean():.2f}")
    om_med = abs(np.gradient(ths_v, its_v * DT)).mean()
else:
    print("orbita: fusion inmediata (sin ventana orbital util)")
    om_med = om0
print(f"  Omega medida (media) = {om_med:.4f}   (lanzada {om0:.4f})")
# recorte de la serie del anillo a la ventana pre-fusion (medida cada 8 pasos)
T_fus = int(paso_fus // 8)
ring_v = ring[:T_fus] if T_fus > 32 else ring

# 2) drenaje de energia interna
itE = np.array([e[0] for e in Es]); EE = np.array([e[1] for e in Es])
pend = np.polyfit(itE * DT, EE, 1)[0]
print(f"energia interna (r<{R_INNER:.0f}): {EE[0]:.3f} -> {EE[-1]:.3f}   dE/dt = {pend:+.5f}")

# 3) potencia por canal en el anillo
def canales_de(datos, titulo):
    print(f"radiacion {titulo} en el anillo r={R_RING:.0f} (fraccion de <vdot^2>):")
    pr = {}
    for nom, u in CANALES.items():
        pr[nom] = np.einsum('a,tan->tn', u, datos)
    tot5 = sum(np.mean(p**2) for p in pr.values())
    resto = max(np.mean(np.sum(datos**2, axis=1)) - tot5, 0.0)
    for nom, p in pr.items():
        print(f"  {nom:6s}: {np.mean(p**2):.3e}   ({np.mean(p**2)/(tot5+resto)*100:6.2f}%)")
    print(f"  resto : {resto:.3e}   ({resto/(tot5+resto)*100:6.2f}%)")
    c = np.mean(pr["fase"] * pr["rot-z"])
    print(f"  correlacion fase*rot-z = {c:+.3e} (maxima "
          f"{np.sqrt(np.mean(pr['fase']**2)*np.mean(pr['rot-z']**2)):.3e}; "
          f"q+ puro => correlacion total)")
    return pr

proys = canales_de(ring_v, "PRE-FUSION (la binaria)")
if T_fus > 32 and T_fus < ring.shape[0] - 64:
    canales_de(ring[T_fus:], "POST-FUSION (el estallido)")

# 4) espectro temporal: ¿radia a Omega (dipolo) o 2*Omega (cuadrupolo)?
Tm = ring_v.shape[0]
dt_m = 8 * DT
for nom in ["fase", "rot-z"]:
    sig = proys[nom] - proys[nom].mean(axis=0)
    S = np.abs(np.fft.rfft(sig, axis=0))**2
    Sm = S.mean(axis=1)
    fr = np.fft.rfftfreq(Tm, dt_m) * 2 * np.pi   # en rad/u.t.
    pico = fr[1 + np.argmax(Sm[1:])]
    print(f"espectro {nom} (pre-fusion): pico en omega = {pico:.4f}"
          f"  ->  pico/Omega_orb = {pico/om_med:.2f}")
    top = np.argsort(Sm[1:])[::-1][:4] + 1
    print(f"    4 picos principales: {[f'{fr[i]:.4f}' for i in top]}")
print("\n[fin]")
