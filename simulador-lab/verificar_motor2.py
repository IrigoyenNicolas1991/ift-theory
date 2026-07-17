"""Verificacion del motor 2 (P3M + receta de escalado).

Tres controles:
  A. REDUCCION: a n=720 en cancha 600 (m=1), con el MISMO init que el motor 1
     (uniforme al azar), el motor 2 debe dar la misma a_r que el exacto
     (referencia motor 1: 1.36-1.43e-3). Prueba que la malla no rompe nada.
  B. ESCALADO: a n=7200 y n=28800 en la misma cancha (mar 10x y 40x mas
     fino, granos proporcionalmente mas livianos) a_r debe mantenerse.
     Prueba que la receta conserva el continuo.
  C. VELOCIDAD: pasos/s a n grande.

Uso: python verificar_motor2.py [--arch cpu]
"""

import argparse
import math
import time

import taichi as ti


def medir_ar(mar, frio, R0):
    for _ in range(frio):
        mar.step('frio')
    pl = {'x': mar.cx + R0, 'y': mar.cy, 'vx': 0.0, 'vy': 0.0, 'fixed': True}
    for _ in range(700):
        mar.step('frio', pl)
    fx = 0.0
    for _ in range(300):
        f, _ = mar.step('frio', pl)
        fx += f
    return -fx / 300.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--arch', default='vulkan', choices=['vulkan', 'cpu'])
    args = ap.parse_args()
    ti.init(arch=getattr(ti, args.arch))
    from motor2 import MarTCI2

    R0 = 150.0
    print('--- A. reduccion a n=720 (esperado a_r ~ 1.4e-3, la del motor 1) ---')
    m720 = MarTCI2(W=600, H=600, n=720, semilla=1, init='uniforme')
    t0 = time.perf_counter()
    ar = medir_ar(m720, 3500, R0)
    print(f"n=720   m={m720.m:.3f}  malla {m720.gx}x{m720.gy}  "
          f"a_r={ar:.3e}  v_circ={math.sqrt(max(ar, 0) * R0):.3f}  "
          f"({time.perf_counter() - t0:.0f}s)")

    print('--- B. escalado (misma cancha, mar mas fino: a_r debe mantenerse) ---')
    for n in (7200, 28800):
        m = MarTCI2(W=600, H=600, n=n, semilla=1, init='uniforme')
        t0 = time.perf_counter()
        ar_n = medir_ar(m, 3500, R0)
        print(f"n={n:<6} m={m.m:.4f}  malla {m.gx}x{m.gy}  "
              f"a_r={ar_n:.3e}  v_circ={math.sqrt(max(ar_n, 0) * R0):.3f}  "
              f"({time.perf_counter() - t0:.0f}s)")

    print('--- C. velocidad a n grande (cancha 900, densidad estandar del continuo) ---')
    for n, lado in ((60000, 900), (150000, 900)):
        m = MarTCI2(W=lado, H=lado, n=n, semilla=1)
        for _ in range(3):
            m.step('vivo')
        ti.sync()
        t0 = time.perf_counter()
        PASOS = 60
        for _ in range(PASOS):
            m.step('vivo')
        ti.sync()
        dt = (time.perf_counter() - t0) / PASOS * 1000
        print(f"n={n:<7} malla {m.gx}x{m.gy}  {dt:7.2f} ms/paso  "
              f"({1000 / dt:.0f} pasos/s)")


if __name__ == '__main__':
    main()
