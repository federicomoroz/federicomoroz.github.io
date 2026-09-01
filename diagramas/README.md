# Diagramas

HTML autocontenidos que se sirven tal cual: **sin front matter**, así Jekyll los copia
verbatim en vez de procesarlos. No dependen de nada externo — se abren offline y se
imprimen a PDF.

Cada subcarpeta es un proyecto. Se linkean desde su case study en `es|en/projects/<id>.md`.

`mega-training-system/` es la documentacion de arquitectura, copiada de `docs/architecture/`
de su repo. **Ojo: a diferencia de los de contracargos, estos NO son autocontenidos** —
cargan mermaid y font-awesome por CDN, asi que necesitan conexion. Mismo problema de sync:
si alla se regeneran, hay que volver a copiarlos.

`contracargos/` son los cinco diagramas del agente de investigación de contracargos,
copiados de `docs/diagrams/` de su repo. Si allá se regeneran, hay que volver a copiarlos:
no hay sync automático.
