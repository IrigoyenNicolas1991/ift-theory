"""Motor TCI 2D — port EXACTO del motor del simulador web.

Fuente de verdad: teoria-campo-intangible/simulador/verificacion-orbita.js
(resultado de referencia 2026-07-16: sin servo captura en ~2.3 vueltas;
con servo de torque puro 38.74 vueltas en 60.000 pasos y seguia).

Fisica identica, sin agregados:
  - mar de granos I con repulsion de largo alcance KII/d^2 entre todos los pares
  - sol = fuente fija KTSOL/d^2 en el centro (huella impuesta, no grano)
  - planeta = fuente movil KTP/d^2; el mar le devuelve la reaccion x MASA
  - d^2 acotado por MIND2 (regulariza el contacto)
  - modo 'frio': damping global 0.995 (enfriamiento inicial)
  - modo 'vivo': playa absorbente de PLAYA px en los bordes (hasta 5% por paso)
  - paredes: rebote con restitucion 0.6
  - integracion: Euler semi-implicito (v += a; x += v), dt=1 como en la web

Diferencia declarada con el original: f32 en GPU (la web usa f64). Para un
sistema caotico con damping la trayectoria exacta nunca coincide (tampoco
coincide entre dos semillas); lo que se verifica es el comportamiento:
enfriamiento, a_r medida, captura sin servo, supervivencia con servo.
"""

import numpy as np
import taichi as ti


@ti.data_oriented
class MarTCI:
    def __init__(self, W=600, H=600, densidad=500, n=None,
                 kii=14.0, ktsol=400.0, ktp=40.0, masa=0.03,
                 mind2=36.0, playa=60.0, semilla=1):
        self.W, self.H = float(W), float(H)
        self.cx, self.cy = self.W / 2.0, self.H / 2.0
        self.n = int(round(W * H / densidad)) if n is None else int(n)
        self.kii, self.ktsol, self.ktp = float(kii), float(ktsol), float(ktp)
        self.masa, self.mind2, self.playa = float(masa), float(mind2), float(playa)

        self.pos = ti.Vector.field(2, ti.f32, self.n)
        self.vel = ti.Vector.field(2, ti.f32, self.n)
        self.acc = ti.Vector.field(2, ti.f32, self.n)
        self.fpl = ti.Vector.field(2, ti.f32, shape=())
        # la reaccion se acumula repartida en 512 slots: n atomicas f32 sobre
        # UNA sola direccion en vulkan pierden actualizaciones a n grande
        # (verificado 2026-07-16: a n=28800 el ruido reportado era 10x el real)
        self.fplpar = ti.Vector.field(2, ti.f32, 512)
        self.reinit(semilla)

    def reinit(self, semilla=1):
        """Mar nuevo: posiciones uniformes, velocidades cero (como initSea())."""
        rng = np.random.default_rng(semilla)
        p = rng.random((self.n, 2)) * np.array([self.W, self.H])
        self.pos.from_numpy(p.astype(np.float32))
        self.vel.from_numpy(np.zeros((self.n, 2), np.float32))

    @ti.kernel
    def _fuerzas(self, plx: ti.f32, ply: ti.f32, hay_pl: ti.i32):
        for i in self.pos:
            xi = self.pos[i]
            a = ti.Vector([0.0, 0.0])
            # mar-mar: todos los pares (equivale al medio-bucle simetrico del JS)
            for j in range(self.n):
                if i != j:
                    d = xi - self.pos[j]
                    d2 = ti.max(d.dot(d), self.mind2)
                    a += d * (self.kii / (d2 * ti.sqrt(d2)))
            # sol fijo en el centro
            ds = xi - ti.Vector([self.cx, self.cy])
            d2s = ti.max(ds.dot(ds), self.mind2)
            a += ds * (self.ktsol / (d2s * ti.sqrt(d2s)))
            # planeta movil + reaccion sobre el
            if hay_pl == 1:
                dp = xi - ti.Vector([plx, ply])
                d2p = ti.max(dp.dot(dp), self.mind2)
                fz = self.ktp / (d2p * ti.sqrt(d2p))
                a += dp * fz
                self.fplpar[i & 511] += -dp * (fz * self.masa)
            self.acc[i] = a

    @ti.kernel
    def _limpiar_fpl(self):
        for k in self.fplpar:
            self.fplpar[k] = ti.Vector([0.0, 0.0])

    @ti.kernel
    def _reducir_fpl(self):
        self.fpl[None] = ti.Vector([0.0, 0.0])
        for k in self.fplpar:
            self.fpl[None] += self.fplpar[k]

    @ti.kernel
    def _mover(self, frio: ti.i32, dt: ti.f32, damp_frio: ti.f32):
        for i in self.pos:
            v = self.vel[i] + self.acc[i] * dt
            if frio == 1:
                v *= damp_frio
            else:
                p0 = self.pos[i]
                db = ti.min(ti.min(p0.x, self.W - p0.x),
                            ti.min(p0.y, self.H - p0.y))
                if db < self.playa:
                    s = 1.0 - db / self.playa
                    v *= 1.0 - 0.05 * s * s * dt
            p = self.pos[i] + v * dt
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

    def step(self, modo='vivo', planeta=None, dt=1.0):
        """Un paso de dt unidades de tiempo (dt=1 = la referencia web).
        planeta = dict {x,y,vx,vy,fixed} (se muta) o None.
        Devuelve (fx, fy): fuerza del mar sobre el planeta en este paso."""
        if planeta is None:
            self._fuerzas(0.0, 0.0, 0)
        else:
            self._limpiar_fpl()
            self._fuerzas(planeta['x'], planeta['y'], 1)
            self._reducir_fpl()
        self._mover(1 if modo == 'frio' else 0, dt, 0.995 ** dt)
        fx = fy = 0.0
        if planeta is not None:
            f = self.fpl[None]
            fx, fy = float(f[0]), float(f[1])
            if not planeta.get('fixed', False):
                planeta['vx'] += fx * dt
                planeta['vy'] += fy * dt
                planeta['x'] += planeta['vx'] * dt
                planeta['y'] += planeta['vy'] * dt
        return fx, fy
