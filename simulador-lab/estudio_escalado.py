"""EXPERIMENTO 0 — ¿la receta de escalado conserva a_r en el limite fino?

Confusor conocido: a n=28800 el mar NO estaba relajado tras 3500 pasos de
enfriamiento (|v| medio seguia subiendo). Aca se mide a_r en tres momentos
del enfriamiento (3500 / 10000 / 20000 pasos) con barras de error, en ambos
motores. Si a_r converge al mismo valor con mas enfriamiento -> era
relajacion; si queda abajo -> la receta pierde algo real en el limite fino.

Nota historica: las mediciones del 2026-07-16 con el acumulador de reaccion
de UNA direccion eran ruido (std 10x); esta corrida usa el acumulador
repartido en ambos motores.

Uso: python estudio_escalado.py [--arch cpu] [--n 720 7200 28800]
"""

import argparse
import math
import time

import numpy as np
import taichi as ti


def medir(mar, pasos_extra_frio, pl, dt):
    """Enfria pasos_extra_frio mas (con el planeta fijo puesto) y mide 400
    pasos. Devuelve (a_r, error, |v|medio del mar)."""
    for _ in range(pasos_extra_frio):
        mar.step('frio', pl, dt=dt)
    fs = []
    for _ in range(400):
        f, _ = mar.step('frio', pl, dt=dt)
        fs.append(f)
    fs = np.array(fs)
    v = np.abs(mar.vel.to_numpy()).mean()
    return -fs.mean(), fs.std() / math.sqrt(len(fs)), v


def protocolo(mar, etiqueta, momentos=3, dt=1.0):
    """Los conteos de pasos se escalan 1/dt: mismo TIEMPO fisico simulado."""
    R0 = 150.0
    t0 = time.perf_counter()
    esc = 1.0 / dt
    for _ in range(int(3500 * esc)):
        mar.step('frio', dt=dt)
    pl = {'x': mar.cx + R0, 'y': mar.cy, 'vx': 0.0, 'vy': 0.0, 'fixed': True}
    for _ in range(int(700 * esc)):
        mar.step('frio', pl, dt=dt)
    # mediciones con enfriamiento creciente entre medio
    plan = (('t~4.2k', 0), ('t~10k', int(5400 * esc)),
            ('t~20k', int(9600 * esc)))[:momentos]
    for momento, extra in plan:
        ar, err, v = medir(mar, extra, pl, dt)
        print(f"  {etiqueta} dt={dt:.2f} frio {momento}: a_r={ar:.3e} "
              f"+/- {err:.1e}  |v|mar={v:.3f}", flush=True)
    print(f"  ({time.perf_counter() - t0:.0f}s)", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--arch', default='vulkan', choices=['vulkan', 'cpu'])
    ap.add_argument('--n', type=int, nargs='+', default=[720, 7200, 28800])
    ap.add_argument('--solo', default='ambos',
                    choices=['ambos', 'exacto', 'motor2'])
    ap.add_argument('--momentos', type=int, default=3)
    args = ap.parse_args()
    ti.init(arch=getattr(ti, args.arch))
    from motor import MarTCI
    from motor2 import MarTCI2

    for n in args.n:
        m = (600 * 600 / 500.0) / n
        dt = 1.0   # el nucleo blando (mind2=36*sqrt(m)) es estable con dt=1
        print(f"== n={n} (m={m:.4f}, nucleo blando, dt={dt:.2f}) ==", flush=True)
        if args.solo in ('ambos', 'exacto'):
            protocolo(MarTCI(W=600, H=600, n=n, semilla=1,
                             kii=14.0 * m, masa=0.03 * m,
                             mind2=36.0 * m ** 0.5),
                      'EXACTO', args.momentos, dt)
        if args.solo in ('ambos', 'motor2'):
            protocolo(MarTCI2(W=600, H=600, n=n, semilla=1, init='uniforme'),
                      'MOTOR2', args.momentos, dt)


if __name__ == '__main__':
    main()
