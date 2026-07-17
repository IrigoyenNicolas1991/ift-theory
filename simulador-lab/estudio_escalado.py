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


def medir(mar, pasos_extra_frio, pl):
    """Enfria pasos_extra_frio mas (con el planeta fijo puesto) y mide 400
    pasos. Devuelve (a_r, error, |v|medio del mar)."""
    for _ in range(pasos_extra_frio):
        mar.step('frio', pl)
    fs = []
    for _ in range(400):
        f, _ = mar.step('frio', pl)
        fs.append(f)
    fs = np.array(fs)
    v = np.abs(mar.vel.to_numpy()).mean()
    return -fs.mean(), fs.std() / math.sqrt(len(fs)), v


def protocolo(mar, etiqueta):
    R0 = 150.0
    t0 = time.perf_counter()
    for _ in range(3500):
        mar.step('frio')
    pl = {'x': mar.cx + R0, 'y': mar.cy, 'vx': 0.0, 'vy': 0.0, 'fixed': True}
    for _ in range(700):
        mar.step('frio', pl)
    # tres mediciones con enfriamiento creciente entre medio
    for momento, extra in (('~4.2k', 0), ('~10k', 5400), ('~20k', 9600)):
        ar, err, v = medir(mar, extra, pl)
        print(f"  {etiqueta} frio {momento}: a_r={ar:.3e} +/- {err:.1e}  "
              f"|v|mar={v:.3f}", flush=True)
    print(f"  ({time.perf_counter() - t0:.0f}s)", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--arch', default='vulkan', choices=['vulkan', 'cpu'])
    ap.add_argument('--n', type=int, nargs='+', default=[720, 7200, 28800])
    args = ap.parse_args()
    ti.init(arch=getattr(ti, args.arch))
    from motor import MarTCI
    from motor2 import MarTCI2

    for n in args.n:
        m = (600 * 600 / 500.0) / n
        print(f"== n={n} (m={m:.4f}) ==", flush=True)
        protocolo(MarTCI(W=600, H=600, n=n, semilla=1,
                         kii=14.0 * m, masa=0.03 * m, mind2=36.0 * m),
                  'EXACTO')
        protocolo(MarTCI2(W=600, H=600, n=n, semilla=1, init='uniforme'),
                  'MOTOR2')


if __name__ == '__main__':
    main()
