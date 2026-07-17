"""Cocina un mar del motor 2 hasta que este bien frio y lo guarda en datos/.
El visor (ver.py --motor 2) carga el mar cacheado al instante en vez de
hacerte esperar minutos de enfriamiento.

Uso: python preparar_mar.py [--n 60000] [--lado 900] [--semilla 1]
Criterio de frio: |v| medio del mar < 0.05 px/paso (o tope de 60000 pasos).
"""

import argparse
import os
import time

import numpy as np
import taichi as ti


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=60000)
    ap.add_argument('--lado', type=int, default=900)
    ap.add_argument('--semilla', type=int, default=1)
    ap.add_argument('--umbral', type=float, default=0.05)
    ap.add_argument('--arch', default='vulkan', choices=['vulkan', 'cpu'])
    args = ap.parse_args()

    ti.init(arch=getattr(ti, args.arch))
    from motor2 import MarTCI2
    mar = MarTCI2(W=args.lado, H=args.lado, n=args.n, semilla=args.semilla)

    os.makedirs('datos', exist_ok=True)
    ruta = f"datos/mar_n{args.n}_l{args.lado}_s{args.semilla}.npz"
    print(f"dt estable del mar: {mar.dt_estable:.2f} (CFL de contacto)")
    t0 = time.perf_counter()
    pasos = 0
    while pasos < 90000:
        for _ in range(1000):
            mar.step('frio')
        pasos += 1000
        v = np.abs(mar.vel.to_numpy()).mean()
        print(f"paso {pasos}: |v|mar={v:.4f}  ({time.perf_counter() - t0:.0f}s)",
              flush=True)
        if v < args.umbral:
            break
    mar.guardar(ruta)
    print(f"guardado: {ruta}  (|v| final={v:.4f}, {pasos} pasos)")


if __name__ == '__main__':
    main()
