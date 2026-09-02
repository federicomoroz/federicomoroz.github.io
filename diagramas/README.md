# Diagramas

HTML autocontenidos que se sirven tal cual: **sin front matter**, así Jekyll los copia
verbatim en vez de procesarlos. No dependen de nada externo — se abren offline y se
imprimen a PDF.

Cada subcarpeta es un proyecto. Se linkean desde su case study en `es|en/projects/<id>.md`.

`mega-training-system/` es la documentacion de arquitectura, copiada de `docs/architecture/`
de su repo. **Ojo: a diferencia de los de contracargos, estos NO son autocontenidos** —
cargan mermaid y font-awesome por CDN, asi que necesitan conexion.

`contracargos/` tiene los cinco diagramas del agente de investigacion de contracargos mas
**tres informes de ejemplo**: la salida real del sistema, uno por cada desenlace del enrutador.
No son diagramas, pero viven aca porque son el mismo tipo de artefacto -HTML autocontenido que
se sirve tal cual- y salen del mismo repo.

Los cinco diagramas son del agente de investigación de contracargos,
copiados de `docs/diagrams/` de su repo.

## No se editan a mano

Estos HTML los **genera** `scripts/sync_diagrams.py` desde el repo de cada
proyecto, y se pisan enteros en cada corrida. Un cambio hecho aca se pierde en
la proxima sincronizacion: se arregla en el repo de origen.

Que se sincroniza sale de `scripts/diagramas.json`; el detalle esta en
`scripts/README-sync.md`.
