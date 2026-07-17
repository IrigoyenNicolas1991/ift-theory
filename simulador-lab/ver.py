"""Visor en vivo del simulador-laboratorio TCI (ventana GPU con Taichi GGUI).

La secuencia del simulador web, en la GPU y con el mar que quieras:
  1. enfria el mar (con el sol ya puesto)
  2. acomoda el planeta (fijo) y deja que el mar lo abrace
  3. MIDE el empujon real del mar -> v_circ
  4. lo suelta en orbita

Teclas:
  ESPACIO  pausa
  S        servo de momento angular ON/OFF (apagalo y mira la espiral)
  R        mar nuevo (otra semilla)
  + / -    mas/menos pasos de fisica por cuadro
  ESC      salir

Uso:
  python ver.py                        config exacta del simulador web (720 granos)
  python ver.py --motor 2             MOTOR P3M: 60.000 granos en cancha 900
  python ver.py --motor 2 --n 150000 --lado 1400   el mar que aguante la GPU
"""

import argparse
import math
import os
import time

import numpy as np
import taichi as ti


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--motor', type=int, default=1, choices=[1, 2],
                    help='1 = exacto O(n^2) (web), 2 = P3M alta densidad')
    ap.add_argument('--n', type=int, default=None,
                    help='granos del mar (default: 720 motor 1 / 60000 motor 2)')
    ap.add_argument('--lado', type=int, default=None,
                    help='lado de la cancha en px (default: 600 / 900)')
    ap.add_argument('--r0', type=float, default=None,
                    help='radio inicial de la orbita (default: lado/4)')
    ap.add_argument('--arch', default='vulkan', choices=['vulkan', 'cpu'])
    ap.add_argument('--semilla', type=int, default=1)
    ap.add_argument('--test', action='store_true',
                    help='corre sin ventana unos cuadros y sale (verificacion)')
    args = ap.parse_args()

    ti.init(arch=getattr(ti, args.arch))
    if args.motor == 2:
        from motor2 import MarTCI2 as Motor
        n = args.n or 60000
        lado = args.lado or 900
    else:
        from motor import MarTCI as Motor
        n = args.n or 720
        lado = args.lado or (600 if args.n is None else int((args.n * 500) ** 0.5))
    mar = Motor(W=lado, H=lado, n=n, semilla=args.semilla)
    lado = mar.W
    # dt estable (CFL de contacto): el motor 2 fino integra con dt<1;
    # los conteos de fases se escalan para simular el mismo tiempo fisico
    DT = mar.dt_estable if args.motor == 2 else 1.0
    escala = lado / 600.0
    R0 = args.r0 or 150.0 * escala
    R_CAPTURA = 30.0
    R_ESCAPE = max(260.0 * escala, 1.35 * R0)
    SERVO_K, SERVO_TOPE = 3.0, 0.4

    # ---- campos de render (posiciones normalizadas a [0,1]) ----
    pts = ti.Vector.field(2, ti.f32, mar.n)
    col = ti.Vector.field(3, ti.f32, mar.n)
    f_sol = ti.Vector.field(2, ti.f32, 1)
    f_pl = ti.Vector.field(2, ti.f32, 1)
    N_ESTELA = 1500
    estela = ti.Vector.field(2, ti.f32, N_ESTELA)

    @ti.kernel
    def llenar_render(inv: ti.f32):
        for i in pts:
            pts[i] = mar.pos[i] * inv
            v = mar.vel[i].norm()
            t = ti.min(v / 0.6, 1.0)
            # sereno azul profundo -> tocado blanco-hielo (como la web)
            col[i] = (ti.Vector([0.16, 0.30, 0.52]) * (1.0 - t)
                      + ti.Vector([0.84, 0.91, 1.00]) * t)

    def limpiar_estela():
        estela.from_numpy(np.full((N_ESTELA, 2), -1.0, np.float32))

    # ---- estado de la secuencia ----
    st = {}

    def ruta_cache(s):
        return f"datos/mar_n{mar.n}_l{int(lado)}_s{s}.npz"

    if args.motor == 2:
        os.makedirs('datos', exist_ok=True)

    def reset(semilla):
        mar.reinit(semilla)
        limpiar_estela()
        # motor 2: mar frio cacheado en disco (cocinarlo lleva minutos);
        # si no hay cache, se enfria adaptativo (|v|<0.05) y se guarda solo
        frio_tot = 3500
        if args.motor == 2:
            frio_tot = int(400 / DT) if mar.cargar(ruta_cache(semilla)) else None
        st.update(fase='frio', cont=0, pl=None, fx_acum=0.0, aR=0.0, vc=0.0,
                  L0=0.0, th=0.0, prev=0.0, vueltas=0.0, boost=0.0, pasos_orb=0,
                  msg='', fin_espera=0, semilla=semilla,
                  frio_tot=frio_tot, v_mar=-1.0)

    reset(args.semilla)
    servo = True
    pausa = False
    # slow motion deliberado en el motor 2: pocas fisicas por cuadro = giro
    # lento pero FINO (regla de Nico: suave y continuo antes que rapido)
    sub = 2 if args.motor == 2 else 8
    pasos_seg = 0.0                      # medidor EMA
    t_prev = time.perf_counter()

    ACOM_TOT, MEDIR_TOT = int(700 / DT), int(300 / DT)

    def fisica_del_cuadro():
        f = st['fase']
        if f == 'frio':
            for _ in range(24):
                mar.step('frio')
            st['cont'] += 24
            fin_frio = False
            if st['frio_tot'] is not None:
                fin_frio = st['cont'] >= st['frio_tot']
            elif st['cont'] % 600 == 0:
                v = float(np.abs(mar.vel.to_numpy()).mean())
                st['v_mar'] = v
                if v < 0.05 or st['cont'] >= 60000:
                    fin_frio = True
                    mar.guardar(ruta_cache(st['semilla']))
            if fin_frio:
                st['pl'] = {'x': mar.cx + R0, 'y': mar.cy,
                            'vx': 0.0, 'vy': 0.0, 'fixed': True}
                st['fase'], st['cont'] = 'acomodar', 0
            return 24
        if f == 'acomodar':
            for _ in range(24):
                mar.step('frio', st['pl'])
            st['cont'] += 24
            if st['cont'] >= ACOM_TOT:
                st['fase'], st['cont'], st['fx_acum'] = 'medir', 0, 0.0
            return 24
        if f == 'medir':
            for _ in range(8):
                fx, _ = mar.step('frio', st['pl'])
                st['fx_acum'] += fx
            st['cont'] += 8
            if st['cont'] >= MEDIR_TOT:
                st['aR'] = -st['fx_acum'] / st['cont']
                if st['aR'] <= 0:      # mar raro: reintentar midiendo mas
                    st['cont'] = 0
                    st['fx_acum'] = 0.0
                    return 8
                st['vc'] = math.sqrt(st['aR'] * R0)
                pl = st['pl']
                pl['fixed'] = False
                pl['vx'], pl['vy'] = 0.0, st['vc']
                st['L0'] = R0 * st['vc']
                st['th'] = 0.0
                st['prev'] = math.atan2(pl['y'] - mar.cy, pl['x'] - mar.cx)
                st['fase'] = 'orbita'
                st['boost'], st['pasos_orb'] = 0.0, 0
            return 8
        if f == 'orbita':
            pl = st['pl']
            for _ in range(sub):
                mar.step('vivo', pl)
                st['pasos_orb'] += 1
                if servo:
                    rx, ry = pl['x'] - mar.cx, pl['y'] - mar.cy
                    r = math.hypot(rx, ry) or 1.0
                    L = rx * pl['vy'] - ry * pl['vx']
                    deficit = (st['L0'] - L) / st['L0']
                    if deficit > 0:
                        g = st['aR'] * min(SERVO_TOPE, SERVO_K * deficit)
                        pl['vx'] += g * DT * (-ry / r)
                        pl['vy'] += g * DT * (rx / r)
                        st['boost'] += g / st['aR']
                dx, dy = pl['x'] - mar.cx, pl['y'] - mar.cy
                r = math.hypot(dx, dy)
                a = math.atan2(dy, dx)
                d = a - st['prev']
                if d > math.pi:
                    d -= 2 * math.pi
                if d < -math.pi:
                    d += 2 * math.pi
                st['th'] += d
                st['prev'] = a
                st['vueltas'] = abs(st['th']) / (2 * math.pi)
                if r < R_CAPTURA:
                    st['fase'], st['msg'] = 'fin', 'CAPTURADO por el sol'
                    break
                if r > R_ESCAPE:
                    st['fase'], st['msg'] = 'fin', 'ESCAPO del sistema'
                    break
            return sub
        # fin: el mar sigue vivo, y a los ~4s arranca de nuevo
        for _ in range(sub):
            mar.step('vivo', st['pl'])
        st['fin_espera'] += 1
        if st['fin_espera'] > 240:
            reset(st['semilla'] + 1)
        return sub

    # ---- ventana ----
    window = ti.ui.Window('Simulador TCI - laboratorio (Fase 0)',
                          (900, 900), show_window=not args.test, vsync=True)
    canvas = window.get_canvas()
    gui = window.get_gui()
    inv = 1.0 / lado
    idx_estela = 0
    frames_test = 0

    while window.running:
        for e in ([] if args.test else window.get_events(ti.ui.PRESS)):
            if e.key == ti.ui.ESCAPE:
                window.running = False
            elif e.key == 'r':
                reset(st['semilla'] + 1)
            elif e.key == 's':
                servo = not servo
            elif e.key == ti.ui.SPACE:
                pausa = not pausa
            elif e.key in ('+', '='):
                sub = min(64, sub * 2)
            elif e.key == '-':
                sub = max(1, sub // 2)

        pasos = 0
        if not pausa:
            pasos = fisica_del_cuadro()
        t_ahora = time.perf_counter()
        dt = t_ahora - t_prev
        t_prev = t_ahora
        if dt > 0 and pasos:
            pasos_seg = 0.9 * pasos_seg + 0.1 * (pasos / dt)

        # render
        llenar_render(inv)
        canvas.set_background_color((0.03, 0.05, 0.10))
        esp = (mar.W * mar.H / mar.n) ** 0.5
        canvas.circles(pts, radius=max(0.0008, min(2.2, 0.42 * esp) / lado),
                       per_vertex_color=col)
        f_sol[0] = [mar.cx * inv, mar.cy * inv]
        canvas.circles(f_sol, radius=11.0 / lado, color=(1.0, 0.72, 0.25))
        if st['pl'] is not None:
            pl = st['pl']
            f_pl[0] = [pl['x'] * inv, pl['y'] * inv]
            if st['fase'] == 'orbita' and not pausa:
                estela[idx_estela] = [pl['x'] * inv, pl['y'] * inv]
                idx_estela = (idx_estela + 1) % N_ESTELA
            canvas.circles(estela, radius=1.4 / lado, color=(0.25, 0.65, 0.75))
            canvas.circles(f_pl, radius=6.0 / lado, color=(0.45, 0.95, 1.0))

        # HUD
        with gui.sub_window('TCI', 0.015, 0.015, 0.36, 0.20):
            frio_txt = 'enfriando el mar...'
            if st['frio_tot'] is None:
                v_txt = f"{st['v_mar']:.2f}" if st['v_mar'] >= 0 else '...'
                frio_txt = (f"cocinando mar nuevo (1 sola vez): "
                            f"|v|={v_txt} -> objetivo 0.05")
            nombres = {'frio': frio_txt,
                       'acomodar': 'acomodando la huella del planeta...',
                       'medir': 'midiendo el empujon del mar...',
                       'orbita': 'EN ORBITA (pura repulsion)',
                       'fin': st['msg'] + ' - reinicia solo'}
            gui.text(f"fase: {nombres[st['fase']]}")
            gui.text(f"motor {args.motor} | granos: {mar.n} | "
                     f"cancha: {int(lado)}px | dt={DT:.2f} | "
                     f"{pasos_seg:.0f} pasos/s")
            if st['fase'] == 'orbita' or st['fase'] == 'fin':
                gui.text(f"vueltas: {st['vueltas']:.2f}   v_circ medida: {st['vc']:.3f}")
                torque = (st['boost'] / max(1, st['pasos_orb'])) * 100
                gui.text(f"servo [S]: {'ON' if servo else 'OFF'}   "
                         f"torque medio: {torque:.1f}% de a_central")
            else:
                gui.text(f"servo [S]: {'ON' if servo else 'OFF'}")
            gui.text('[ESPACIO] pausa  [R] mar nuevo  [+/-] velocidad')

        if args.test:
            frames_test += 1
            if frames_test >= 400:
                print(f"TEST OK: 400 cuadros, fase final = {st['fase']}, "
                      f"vueltas = {st['vueltas']:.2f}")
                break
        else:
            window.show()


if __name__ == '__main__':
    main()
