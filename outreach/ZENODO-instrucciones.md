# Zenodo: cómo sellar el corpus con DOI (guía paso a paso)

Zenodo (del CERN) da un **DOI permanente y con fecha** — la prueba de prioridad de la predicción de campo fuerte. Gratis y en 15 minutos.

## Paso 0 — Limpieza previa (importante)
Entrá a zenodo.org con tu cuenta y revisá si alguna vez subiste el `TCI_Zenodo.zip` viejo (diciembre 2025). Si está publicado, contiene material de la etapa anterior (incluido el paper galáctico retirado): crear una **nueva versión** que lo reemplace con el corpus actual, o marcarlo como obsoleto apuntando al nuevo DOI. Si nunca lo subiste, mejor: empezamos limpio.

## Camino recomendado — Integración GitHub ↔ Zenodo (automática)
1. Entrá a zenodo.org → login (podés entrar directamente **con tu cuenta de GitHub**).
2. Menú de tu cuenta → **GitHub** (zenodo.org/account/settings/github/).
3. Activá el interruptor del repo **IrigoyenNicolas1991/ift-theory**.
4. En GitHub, creá un **Release**: página del repo → Releases → "Draft a new release" → Tag: `v1.0-corpus-honesto` → título: "TCI — corpus honesto, julio 2026" → descripción: pegá el resumen del ONE-PAGER → Publish.
5. Zenodo archiva el release automáticamente y te da el DOI en minutos.

## Metadatos sugeridos (cuando Zenodo te los pida)
- **Título**: Intangible Field Theory (TCI): an elastic-medium substrate model for gravity, with dated strong-field predictions and a public ledger of its own falsifications
- **Autor**: Irigoyen, Nicolás (independent researcher, La Plata, Argentina)
- **Contributor / agradecimientos**: Developed in collaboration with Claude (Anthropic) — declarar la colaboración con IA abiertamente es parte de la credencial de honestidad.
- **Licencia**: CC-BY 4.0 (permite que cualquiera lo use citándote — lo que queremos)
- **Keywords**: analogue gravity, emergent gravity, modified gravity, black hole shadow, Yilmaz metric, MOND, radial acceleration relation, AI-assisted research
- **Descripción**: el texto del ONE-PAGER tal cual.

## Después del DOI
- Agregá el DOI al pie de los dos sitios (yo lo hago apenas me lo pases).
- Recién entonces salen los correos de DESTINATARIOS.md — con el DOI incluido, que transforma "un link a un GitHub" en "un objeto académico citable con fecha".
