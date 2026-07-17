"""Verificacion del port contra el motor de referencia (verificacion-orbita.js).

Replica el protocolo exacto del JS:
  1. 3500 pasos de enfriamiento (mar solo + sol)
  2. planeta FIJO en (cx+150, cy), 700 pasos de acomodacion
  3. 300 pasos midiendo la fuerza radial -> a_r y v_circ
  4. soltar el planeta con v tangencial = v_circ y contar vueltas

Resultados de referencia del motor JS (2026-07-16, f64):
  - a_r tal que v_circ ~ da periodo ~2100 pasos
  - SIN servo: captura en ~2.3 vueltas (friccion de onda)
  - CON servo (torque puro, K=3, tope 40%): 38.74 vueltas en 60.000 pasos
    y seguia; torque medio 34.5% de a_central

Uso:
  python verificar_port.py                (vulkan, sin y con servo)
  python verificar_port.py --arch cpu
  python verificar_port.py --pasos 20000  (mas corto)
"""

import argparse
import math
import time

import taichi as ti


def experimento(mar, servo, max_pasos, etiqueta):
    print(f"\n=== {etiqueta} ===")
    t0 = time.perf_counter()

    for _ in range(3500):
        mar.step('frio')

    R0 = 150.0
    pl = {'x': mar.cx + R0, 'y': mar.cy, 'vx': 0.0, 'vy': 0.0, 'fixed': True}
    for _ in range(700):
        mar.step('frio', pl)

    fx_acum = 0.0
    for _ in range(300):
        fx, _fy = mar.step('frio', pl)
        fx_acum += fx
    aR = -fx_acum / 300.0
    vc = math.sqrt(aR * R0)
    print(f"a_r={aR:.3e}  v_circ={vc:.3f}  (periodo ~{round(2 * math.pi * R0 / vc)} pasos)")

    pl['fixed'] = False
    pl['vx'], pl['vy'] = 0.0, vc
    L0 = R0 * vc
    SERVO_K, SERVO_TOPE = 3.0, 0.4

    th = 0.0
    prev = math.atan2(pl['y'] - mar.cy, pl['x'] - mar.cx)
    rmin = rmax = R0
    boost_acum = 0.0
    boost_max = 0.0
    out = 'SIGUE ORBITANDO al cortar'
    s = 0
    for s in range(max_pasos):
        mar.step('vivo', pl)
        if servo:
            rx, ry = pl['x'] - mar.cx, pl['y'] - mar.cy
            r = math.hypot(rx, ry) or 1.0
            L = rx * pl['vy'] - ry * pl['vx']
            deficit = (L0 - L) / L0
            if deficit > 0:
                g = aR * min(SERVO_TOPE, SERVO_K * deficit)
                pl['vx'] += g * (-ry / r)
                pl['vy'] += g * (rx / r)
                rel = g / aR
                boost_acum += rel
                boost_max = max(boost_max, rel)
        dx, dy = pl['x'] - mar.cx, pl['y'] - mar.cy
        r = math.hypot(dx, dy)
        rmin, rmax = min(rmin, r), max(rmax, r)
        a = math.atan2(dy, dx)
        d = a - prev
        if d > math.pi:
            d -= 2 * math.pi
        if d < -math.pi:
            d += 2 * math.pi
        th += d
        prev = a
        if r < 30:
            out = 'CAPTURADO'
            break
        if r > 260:
            out = 'ESCAPO'
            break
        if s > 0 and s % 6000 == 0:
            v = math.hypot(pl['vx'], pl['vy'])
            print(f"  paso {s}: r={r:.0f}, vueltas={abs(th) / (2 * math.pi):.2f}, "
                  f"v={v:.3f}, torque medio={boost_acum / s * 100:.1f}% de a_central")

    vueltas = abs(th) / (2 * math.pi)
    print(f"-> {out} (paso {s}); vueltas={vueltas:.2f}; r en [{rmin:.0f}, {rmax:.0f}]")
    if servo:
        print(f"   torque del servo: medio {boost_acum / max(1, s) * 100:.1f}% "
              f"de a_central, maximo {boost_max * 100:.0f}%")
    print(f"   ({time.perf_counter() - t0:.0f}s)")
    return out, vueltas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--arch', default='vulkan', choices=['vulkan', 'cpu'])
    ap.add_argument('--pasos', type=int, default=60000)
    ap.add_argument('--semilla', type=int, default=1)
    args = ap.parse_args()

    ti.init(arch=getattr(ti, args.arch), random_seed=args.semilla)
    from motor import MarTCI
    mar = MarTCI(semilla=args.semilla)
    print(f"n={mar.n}, KII={mar.kii}, KTSOL={mar.ktsol}, KTP={mar.ktp}, "
          f"arch={args.arch}")

    # Referencia JS: captura en ~2.3 vueltas
    mar.reinit(args.semilla)
    out1, v1 = experimento(mar, servo=False, max_pasos=args.pasos,
                           etiqueta='SIN SERVO (esperado: captura en ~2.3 vueltas)')

    # Referencia JS: 38.74 vueltas en 60.000 pasos y seguia
    mar.reinit(args.semilla + 1)
    out2, v2 = experimento(mar, servo=True, max_pasos=args.pasos,
                           etiqueta='CON SERVO (esperado: sobrevive los 60.000 pasos)')

    print('\n=== VEREDICTO ===')
    ok1 = out1 == 'CAPTURADO' and 1.0 <= v1 <= 5.0
    ok2 = out2 == 'SIGUE ORBITANDO al cortar'
    print(f"sin servo: {'OK' if ok1 else 'DISTINTO AL DE REFERENCIA'} ({out1}, {v1:.2f} vueltas)")
    print(f"con servo: {'OK' if ok2 else 'DISTINTO AL DE REFERENCIA'} ({out2}, {v2:.2f} vueltas)")


if __name__ == '__main__':
    main()
