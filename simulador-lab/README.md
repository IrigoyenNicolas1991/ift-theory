# Simulador-laboratorio TCI 2D

Laboratorio numérico del medio I: acá el simulador no es divulgación, es
instrumento de medición. Cada experimento responde una pregunta abierta de la
teoría y termina en una nota en `notas/` (victoria o derrota, el mismo día).

**Hermano chico (divulgación, publicado):**
https://irigoyennicolas1991.github.io/teoria-campo-intangible/simulador/ —
mismo motor físico, 720 granos, corre en el browser de cualquiera.

## Qué hay

- `motor.py` — port exacto a Taichi (GPU/Vulkan) del motor del simulador web
  (`teoria-campo-intangible/simulador/verificacion-orbita.js`). Misma física:
  repulsión KII/d² entre todos los granos, sol fijo KTSOL, planeta KTP con
  reacción ×MASA, enfriamiento, playa absorbente, rebote 0.6.
- `verificar_port.py` — replica el protocolo de verificación del JS y compara
  contra los resultados de referencia (2026-07-16): sin servo captura en ~2
  vueltas por fricción de onda; con servo de torque puro sobrevive 60.000 pasos.
- `benchmark.py` — ms/paso vs n en esta máquina (Ryzen 5 7535HS + Radeon
  integrada vía Vulkan).

## Cómo correr

```
.venv\Scripts\python.exe verificar_port.py            # verificación completa
.venv\Scripts\python.exe verificar_port.py --pasos 8000   # versión corta
.venv\Scripts\python.exe benchmark.py --n 50000
```

El entorno es un venv local de Python 3.12 (Taichi no corre en 3.14):
`py -3.12 -m venv .venv` + `pip install taichi numpy matplotlib`.

## Diferencias declaradas con el motor JS

- f32 en GPU (el JS usa f64). El sistema es caótico: la trayectoria exacta no
  coincide ni entre dos semillas; lo que se verifica es el comportamiento
  (período orbital, captura sin servo, supervivencia con servo, torque medio).
- El bucle de pares es completo (i≠j) en vez del medio-bucle simétrico del JS:
  mismas fuerzas, orden de suma distinto.

## Motor 2 (P3M) — VERIFICADO 2026-07-17

`motor2.py`: partícula-partícula exacto en vecindario 5×5 de celdas
(counting-sort con prefix-sum propio) + celdas lejanas como masas puntuales
en su centro de masa evaluadas en la posición del grano. Receta de escalado
completa: masa por grano m=(W·H/500)/n, fuerzas ×m, **núcleo blando
mind2=36·√m** (con 36·m hay calentamiento numérico y el mar fino jamás
enfría — ver comentario en motor2.py). Veredicto del estudio
(`estudio_escalado.py`, mar relajado): a_r = 1.405/1.360/1.355e-3 (exacto)
vs 1.420/1.387/1.368e-3 (P3M) a n=720/7200/28800 — el continuo se conserva
al 4% sobre 40× de refinamiento. Planeta residente en GPU
(`correr_planeta`): sin sync CPU↔GPU por paso. Mares fríos cacheados en
`datos/` (`preparar_mar.py`).

**Visor potente**: `VER-SIMULADOR-POTENTE.bat` (60.000 granos, cancha 900,
r0=150 calibrado en frío). Deliberadamente en cámara lenta (sub=2): el
movimiento fino manda; subí velocidad con `+`.

## Los tres experimentos (Fase 1-2)

1. **¿La fricción de onda es física o granularidad?** PRIMER DATO 2026-07-17:
   a 60.000 granos la órbita sin servo aguanta **7,5 vueltas** vs 1,3-2,3 del
   mar de 720 — el mar fino retiene ~4× más: buena parte de la fricción del
   simulador web era ruido granular. Falta la curva completa vueltas(n) con
   estadística (varias semillas por n).
2. **Ley de fuerza emergente F(d)**: perfil ya medido alrededor del sol en
   frío (2.20/1.43/0.98/0.71/0.53e-3 en r=120..240, cancha 900; se hace
   repulsiva cerca de las paredes). Falta el barrido dos-intrusas limpio y
   el ajuste de ley (~1/d esperado en 2D).
3. **Binaria = mini-Hulse-Taylor**: dos soles orbitándose, medir energía
   radiada al mar vs parámetros del medio. Conecta con el fruto 3 de TCI 2.0.
