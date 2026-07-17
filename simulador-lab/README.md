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

## Los tres experimentos que vienen (Fase 1-2)

1. **¿La fricción de onda es física o granularidad?** Subir n 100× manteniendo
   la densidad de masa del mar y medir la tasa de decaimiento orbital vs n.
   Si decae más lento con mar más fino → era granularidad (y el servo del
   simulador web sobra a escala); si no → es el análogo real de radiación.
2. **Ley de fuerza emergente F(d)**: dos intrusas quietas, barrer la distancia,
   medir la fuerza neta. En 2D lo esperable es ~1/d (el Newton del mundo plano).
3. **Binaria = mini-Hulse-Taylor**: dos soles orbitándose, medir energía
   radiada al mar vs parámetros del medio. Conecta con el fruto 3 de TCI 2.0.
