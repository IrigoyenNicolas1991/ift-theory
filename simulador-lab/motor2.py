"""Motor TCI 2D de ALTA DENSIDAD — P3M (particula-particula + malla).

La misma fisica continua que motor.py, con el mar afinado n veces.

RECETA DE ESCALADO (para que el continuo no cambie al afinar el mar):
  cada grano lleva masa m = (W*H/500)/n   (a n = W*H/500 -> m=1: motor 1 exacto)
  acc grano<-grano:  KII*m/d^2            (la masa total del mar se conserva)
  mind2 grano-grano: 36*m                 (el regularizador es el tamano del grano)
  sol/planeta -> grano: KTSOL/d^2, KTP/d^2 sin cambio (con mind2=36 fijo:
                        es el tamano de la FUENTE, no del grano)
  reaccion sobre el planeta: MASA*m por grano (el total se conserva)
  damping, playa, paredes, dt: identicos al motor 1

ALGORITMO (rompe el O(n^2)):
  malla de celdas; tamano balanceado: ~max(16, sqrt(n)/5) granos por celda
  (costo total ~O(n^1.5) en vez de O(n^2)).
  - corto alcance: pares EXACTOS dentro del vecindario 5x5 de celdas,
    via counting-sort con prefix sum (SIN tope de granos por celda:
    las pilas contra las paredes no pierden fisica)
  - largo alcance: las celdas a distancia chebyshev > 2 se ven como masas
    puntuales en su CENTRO DE MASA real, evaluadas en la posicion exacta
    de cada grano receptor (complemento exacto del vecindario PP: ni
    doble conteo ni hueco)
  Error declarado: solo el multipolo (una celda lejana = masa puntual en
  su COM). La version centro-geometrico + evaluacion en centro de celda
  daba 13% mediana / colas de 1476% contra el exacto (2026-07-16) y
  corria a_r con n; esta version se verifica en verificar_motor2.py y
  el arbitro numpy del scratchpad.
"""

import numpy as np
import taichi as ti

MIND2_FUENTE = 36.0
NRED = 512   # slots del acumulador de la reaccion del planeta


@ti.data_oriented
class MarTCI2:
    def __init__(self, W=900, H=900, n=60000, semilla=1, init='grilla',
                 kii=14.0, ktsol=400.0, ktp=40.0, masa=0.03, playa=60.0):
        self.W, self.H = float(W), float(H)
        self.cx, self.cy = self.W / 2.0, self.H / 2.0
        self.n = int(n)
        self.m = (self.W * self.H / 500.0) / self.n
        self.kii0 = float(kii)
        self.kii_m = float(kii) * self.m
        self.ktsol, self.ktp = float(ktsol), float(ktp)
        self.masa_m = float(masa) * self.m
        self.mind2 = 36.0 * self.m
        self.playa = float(playa)

        esp = (self.W * self.H / self.n) ** 0.5
        q_obj = max(16.0, 0.2 * self.n ** 0.5)   # granos por celda (balance)
        hc = q_obj ** 0.5 * esp
        self.gx = max(3, int(self.W / hc))
        self.gy = max(3, int(self.H / hc))
        self.hcx = self.W / self.gx
        self.hcy = self.H / self.gy
        self.ncel = self.gx * self.gy

        self.pos = ti.Vector.field(2, ti.f32, self.n)
        self.vel = ti.Vector.field(2, ti.f32, self.n)
        self.acc = ti.Vector.field(2, ti.f32, self.n)
        self.fpl = ti.Vector.field(2, ti.f32, shape=())
        self.fplpar = ti.Vector.field(2, ti.f32, NRED)
        self.cuenta = ti.field(ti.i32, self.ncel)   # tras el scan: acumulada
        self.cursor = ti.field(ti.i32, self.ncel)
        self.celda_de = ti.field(ti.i32, self.n)
        self.orden = ti.field(ti.i32, self.n)
        self.mcel = ti.field(ti.f32, (self.gx, self.gy))
        self.com = ti.Vector.field(2, ti.f32, (self.gx, self.gy))
        self.reinit(semilla, init)

    def reinit(self, semilla=1, init='grilla'):
        """Mar nuevo. init='grilla' (nace casi sereno, enfria rapido) o
        'uniforme' (al azar, como initSea() del motor 1)."""
        rng = np.random.default_rng(semilla)
        if init == 'uniforme':
            p = rng.random((self.n, 2)) * np.array([self.W, self.H])
        else:
            lado = int(np.ceil(np.sqrt(self.n)))
            xs = (np.arange(self.n) % lado + 0.5) / lado * self.W
            ys = (np.arange(self.n) // lado + 0.5) / lado * self.H
            esp = (self.W * self.H / self.n) ** 0.5
            p = np.stack([xs, ys], axis=1) + rng.normal(0, 0.25 * esp, (self.n, 2))
            p[:, 0] = np.clip(p[:, 0], 0, self.W)
            p[:, 1] = np.clip(p[:, 1], 0, self.H)
        self.pos.from_numpy(p.astype(np.float32))
        self.vel.from_numpy(np.zeros((self.n, 2), np.float32))

    def guardar(self, ruta):
        """Guarda el estado del mar (para cachear mares ya enfriados)."""
        np.savez_compressed(ruta, pos=self.pos.to_numpy(),
                            vel=self.vel.to_numpy(),
                            n=self.n, W=self.W, H=self.H)

    def cargar(self, ruta):
        """Carga un estado guardado. Devuelve False si no coincide la config."""
        try:
            d = np.load(ruta)
        except (FileNotFoundError, OSError):
            return False
        if int(d['n']) != self.n or float(d['W']) != self.W \
                or float(d['H']) != self.H:
            return False
        self.pos.from_numpy(d['pos'])
        self.vel.from_numpy(d['vel'])
        return True

    @ti.func
    def _celda(self, p):
        cx = ti.min(ti.max(int(p.x / self.hcx), 0), self.gx - 1)
        cy = ti.min(ti.max(int(p.y / self.hcy), 0), self.gy - 1)
        return cx, cy

    @ti.kernel
    def _contar(self):
        for c in self.cuenta:
            self.cuenta[c] = 0
        for k in self.fplpar:
            self.fplpar[k] = ti.Vector([0.0, 0.0])
        for i in self.pos:
            cx, cy = self._celda(self.pos[i])
            c = cx * self.gy + cy
            self.celda_de[i] = c
            self.cuenta[c] += 1

    @ti.kernel
    def _celdas_stats(self):
        # masa y centro de masa por celda, desde el orden ya construido
        # (cero atomicas de float; corre DESPUES de _ordenar)
        for cx, cy in self.mcel:
            c = cx * self.gy + cy
            ini = 0
            if c > 0:
                ini = self.cuenta[c - 1]
            fin = self.cuenta[c]
            s = ti.Vector([0.0, 0.0])
            for k in range(ini, fin):
                s += self.pos[self.orden[k]]
            nc = fin - ini
            self.mcel[cx, cy] = nc * self.m
            if nc > 0:
                self.com[cx, cy] = s / nc
            else:
                self.com[cx, cy] = ti.Vector([(cx + 0.5) * self.hcx,
                                              (cy + 0.5) * self.hcy])

    @ti.kernel
    def _scan_serial(self):
        # prefix sum inclusivo, UN hilo: determinista y suficiente para
        # <~20k celdas (el PrefixSumExecutor de taichi 1.7.4 da resultados
        # corruptos en vulkan: scan[-1] != n, verificado 2026-07-16)
        ti.loop_config(serialize=True)
        total = 0
        for c in range(self.ncel):
            total += self.cuenta[c]
            self.cuenta[c] = total

    @ti.kernel
    def _preparar_cursor(self):
        for c in self.cursor:
            ini = 0
            if c > 0:
                ini = self.cuenta[c - 1]
            self.cursor[c] = ini

    @ti.kernel
    def _ordenar(self):
        for i in self.pos:
            k = ti.atomic_add(self.cursor[self.celda_de[i]], 1)
            self.orden[k] = i

    @ti.kernel
    def _fuerzas(self, plx: ti.f32, ply: ti.f32, hay_pl: ti.i32):
        for i in self.pos:
            xi = self.pos[i]
            cx, cy = self._celda(xi)
            a = ti.Vector([0.0, 0.0])
            # largo alcance: celdas lejanas como masas puntuales en su COM,
            # evaluadas en la posicion exacta de ESTE grano
            for ox, oy in ti.ndrange(self.gx, self.gy):
                if ti.abs(ox - cx) > 2 or ti.abs(oy - cy) > 2:
                    mo = self.mcel[ox, oy]
                    if mo > 0:
                        dl = xi - self.com[ox, oy]
                        d2l = dl.dot(dl)
                        a += dl * (self.kii0 * mo / (d2l * ti.sqrt(d2l)))
            # corto alcance: pares exactos en el vecindario 5x5
            for ox in range(ti.max(0, cx - 2), ti.min(self.gx, cx + 3)):
                for oy in range(ti.max(0, cy - 2), ti.min(self.gy, cy + 3)):
                    c = ox * self.gy + oy
                    ini = 0
                    if c > 0:
                        ini = self.cuenta[c - 1]
                    for k in range(ini, self.cuenta[c]):
                        j = self.orden[k]
                        if j != i:
                            d = xi - self.pos[j]
                            d2 = ti.max(d.dot(d), self.mind2)
                            a += d * (self.kii_m / (d2 * ti.sqrt(d2)))
            # sol fijo (fuente: mind2 propio, no escala)
            ds = xi - ti.Vector([self.cx, self.cy])
            d2s = ti.max(ds.dot(ds), MIND2_FUENTE)
            a += ds * (self.ktsol / (d2s * ti.sqrt(d2s)))
            # planeta movil + reaccion (acumulada en NRED slots para no
            # serializar 60k atomicas sobre una sola direccion)
            if hay_pl == 1:
                dp = xi - ti.Vector([plx, ply])
                d2p = ti.max(dp.dot(dp), MIND2_FUENTE)
                fz = self.ktp / (d2p * ti.sqrt(d2p))
                a += dp * fz
                self.fplpar[i & (NRED - 1)] += -dp * (fz * self.masa_m)
            self.acc[i] = a

    @ti.kernel
    def _reducir_fpl(self):
        self.fpl[None] = ti.Vector([0.0, 0.0])
        for k in self.fplpar:
            self.fpl[None] += self.fplpar[k]

    @ti.kernel
    def _mover(self, frio: ti.i32):
        for i in self.pos:
            v = self.vel[i] + self.acc[i]
            if frio == 1:
                v *= 0.995
            else:
                p0 = self.pos[i]
                db = ti.min(ti.min(p0.x, self.W - p0.x),
                            ti.min(p0.y, self.H - p0.y))
                if db < self.playa:
                    s = 1.0 - db / self.playa
                    v *= 1.0 - 0.05 * s * s
            p = self.pos[i] + v
            if p.x < 0.0:
                p.x = 0.0
                v.x *= -0.6
            elif p.x > self.W:
                p.x = self.W
                v.x *= -0.6
            if p.y < 0.0:
                p.y = 0.0
                v.y *= -0.6
            elif p.y > self.H:
                p.y = self.H
                v.y *= -0.6
            self.vel[i] = v
            self.pos[i] = p

    def step(self, modo='vivo', planeta=None):
        """Un paso. Misma interfaz que motor.MarTCI."""
        self._contar()
        self._scan_serial()
        self._preparar_cursor()
        self._ordenar()
        self._celdas_stats()
        if planeta is None:
            self._fuerzas(0.0, 0.0, 0)
        else:
            self._fuerzas(planeta['x'], planeta['y'], 1)
            self._reducir_fpl()
        self._mover(1 if modo == 'frio' else 0)
        fx = fy = 0.0
        if planeta is not None:
            f = self.fpl[None]
            fx, fy = float(f[0]), float(f[1])
            if not planeta.get('fixed', False):
                planeta['vx'] += fx
                planeta['vy'] += fy
                planeta['x'] += planeta['vx']
                planeta['y'] += planeta['vy']
        return fx, fy
