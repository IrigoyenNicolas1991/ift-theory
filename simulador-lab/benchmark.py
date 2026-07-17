"""Benchmark del motor: ms/paso en funcion de n (granos del mar).

Un n por invocacion (Taichi no permite crear fields nuevos tras el primer
kernel). Barrido tipico:
  foreach n: python benchmark.py --n 1000 5000 20000 50000 100000  (uno por vez)

El kernel es el O(n^2) exacto del port (sin planeta, modo vivo).
"""

import argparse
import time

import taichi as ti


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, required=True)
    ap.add_argument('--arch', default='vulkan', choices=['vulkan', 'cpu'])
    ap.add_argument('--pasos', type=int, default=20)
    args = ap.parse_args()

    ti.init(arch=getattr(ti, args.arch))
    from motor import MarTCI
    # W,H crecen con n para mantener la densidad del simulador web (1 grano/500px^2)
    lado = int((args.n * 500) ** 0.5)
    mar = MarTCI(W=lado, H=lado, n=args.n)

    for _ in range(3):  # warmup + compilacion
        mar.step('vivo')
    ti.sync()
    t0 = time.perf_counter()
    for _ in range(args.pasos):
        mar.step('vivo')
    ti.sync()
    dt = (time.perf_counter() - t0) / args.pasos * 1000
    gint = args.n * args.n / (dt / 1000) / 1e9
    print(f"arch={args.arch}  n={args.n:>7}  lado={lado}px  "
          f"{dt:8.2f} ms/paso  {gint:6.1f} G int/s  "
          f"({1000 / dt:.0f} pasos/s)")


if __name__ == '__main__':
    main()
