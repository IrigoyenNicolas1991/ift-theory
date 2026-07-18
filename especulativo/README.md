# ⚠️ Carpeta especulativa — investigación en desarrollo, NO es parte del corpus TCI

**Leé esto antes que nada.** Esta carpeta contiene trabajo exploratorio **en curso** de
la línea "TCI 2.0" (gravedad y materia emergentes de un condensado con orden tensorial).
Se guarda acá como respaldo y bitácora de trabajo, con separación deliberada del resto
del repositorio:

- **NO está validado.** Hay hipótesis vivas, conjeturas declaradas, cálculos
  preliminares con parámetros de prueba, e ideas que ya fueron falsadas y se conservan
  documentadas (la bitácora registra el proceso completo, muertes incluidas).
- **NO es lo que TCI afirma públicamente.** El corpus publicado (paper, sitios, Zenodo)
  vive en la raíz del repo y en las ramas publicadas; nada de esta carpeta se mergea a
  `main` ni aparece en los sitios.
- **Es la parte más especulativa del proyecto**, y se presenta como tal. Si llegaste
  acá navegando: bienvenido, pero calibrá expectativas — esto es un cuaderno de
  laboratorio, no un resultado.

## Las páginas divulgativas (las caras visuales de esta carpeta)

Todo lo de acá tiene su versión contada para no-físicos, con simulaciones jugables:

- **«El mar y sus nudos»** (la materia): https://irigoyennicolas1991.github.io/ift-theory/mar-y-nudos/
- **«El taller electromagnético del mar»** (el EM): https://irigoyennicolas1991.github.io/ift-theory/taller-electromagnetico/

Ambas llevan el aviso de etapa especulativa y enlazan de vuelta a esta carpeta como
respaldo formal. No están enlazadas desde las sedes públicas de TCI (decisión
deliberada: se comparten en persona).

## Contenido

| Archivo | Qué es |
|---|---|
| `BITACORA-campana-condensado-2026-07-16.md` | Bitácora completa de la campaña (19 secciones): scoping, 10 verificaciones bibliográficas, 4 rutas falsadas con causa citada, los cálculos numéricos, el estado actual y los **próximos pasos** (§19) |
| `espectro_biaxial_real.py` | Cálculo 1: espectro de un condensado J=2 REAL (modelo mínimo, 5 componentes) — controles uniaxial/biaxial/SO(5) |
| `espectro_biaxial_complejo.py` | Cálculo 2: versión COMPLEJA (10 componentes) con set de prueba declarado — aparecen las dos polarizaciones TT |
| `espectro_biaxial_3p2.py` | Cálculo 3: funcional GL textual de la literatura ³P₂ (Yasui-Chatterjee-Nitta) — caso γ<0 reproduce la física publicada (control), caso γ>0 (postulado declarado) selecciona la fase D₄-BN con el par TT |

Los scripts corren con Python 3 + numpy, sin más dependencias
(`python espectro_biaxial_3p2.py`).

## El estado en una línea (2026-07-17)

Hipótesis de trabajo actual: *un superfluido con orden cuadrupolar interno soldado al
espacio, en su fase biaxial máxima, tiene como modos sin masa sobre su eje especial
exactamente las dos polarizaciones tensoriales de una onda gravitacional — una es el
Goldstone rotacional y la otra es el fonón del superfluido vestido por el orden.*
Verificaciones a favor, deudas y criterios de muerte: en la bitácora. Reglas de la
casa: honestidad brutal, toda derrota se documenta el mismo día, ningún "exactamente"
sin ecuación de respaldo.
