# Mantenimiento del sitio

Manual del portfolio. Explica cómo agregar contenido sin tocar plantillas.

> El repo se llama `federicomoroz.github.io`, que es la convención de GitHub Pages para
> un *user site*: se publica en la **raíz del dominio**,
> `https://federicomoroz.github.io/`, sin subpath. Por eso `baseurl` está vacío en
> `_config.yml`.

## GitHub Pages

**Settings → Pages → Build and deployment → Source: Deploy from a branch**, branch `main`,
folder `/ (root)`. Cada push a `main` rebuildea solo.

Si alguna vez el sitio se moviera a un repo con otro nombre, el único cambio sería poner
ese nombre en `baseurl` (`/nombre-del-repo`). Todos los links usan `relative_url`, así que
se reacomodan solos: no hay ni un path hardcodeado en las plantillas.

## Estructura

- `index.html` — redirect de la raíz a `/es/` o `/en/` según el navegador (y lo último elegido).
- `es/index.md` + `en/index.md` — landing por idioma.
- `es/projects.md` + `en/projects.md` — listado de proyectos.
- `es/tools.md` + `en/tools.md` — listado de herramientas/librerías.
- `es/about.md` + `en/about.md` — perfil, skills, cómo trabajo, educación, idiomas.
- `es/projects/<id>.md` + `en/projects/<id>.md` — case study por proyecto, bilingüe.
- `_data/i18n.yml` — **todos** los textos de interfaz, por idioma.
- `_data/projects.yml` — metadata de proyectos.
- `_data/tools.yml` — metadata de herramientas.
- `_data/cv.yml` — perfil, skills, educación e idiomas que se muestran en `/about/`.
- `_layouts/`, `_includes/`, `assets/css/style.scss` — el tema.
- `cv/` — los PDFs del CV que se ofrecen para descargar.

Las páginas de `es/` y `en/` son **el mismo cuerpo Liquid**; lo único distinto es el front
matter. Todo el texto sale de `_data/i18n.yml` vía `page.lang`. Si tocás una, tocá la otra.

## Auto-descubrimiento de repos

`_data/repos.yml` lo **genera** `scripts/sync_repos.py` desde la API pública de GitHub:
descripción, lenguaje, topics, stars, último push y si está archivado. **No se edita a
mano**: se pisa entero en cada corrida.

El reparto es deliberado:

| | Archivo | Quién lo escribe |
|---|---|---|
| Los hechos del repo | `_data/repos.yml` | el script, solo |
| Qué se lista y cómo se cuenta | `_data/projects.yml`, `_data/tools.yml` | vos, a mano |

**El contenido se refresca solo; la inclusión se decide a mano.** Si un repo público nuevo
apareciera automáticamente en el sitio, cualquier repo de prueba terminaría en el portfolio.
Lo que hace el script es *avisarte* que existe.

Corre solo una vez por día (`.github/workflows/sync-repos.yml`), y también a demanda desde
**Actions → sync-repos → Run workflow**. Si commitea, deja el resumen en la corrida.

A mano:

```sh
python scripts/sync_repos.py            # regenera repos.yml
python scripts/sync_repos.py --check    # solo reporta, no escribe
```

El reporte dice dos cosas:

- **Repos públicos sin entrada curada** — existen en GitHub pero no se muestran. Para
  publicarlos, se les escribe una entrada en `projects.yml` o en `tools.yml`.
- **Repos curados que ya no son públicos** — se volvieron privados, se renombraron o se
  borraron. La entrada sigue ahí y su link está roto: hay que revisarla. **El script nunca
  borra una entrada curada**, porque perder un write-up por un cambio de visibilidad sería
  mucho peor que un link roto.

**Solo ve repos públicos.** Es una limitación real de la API sin credenciales, y también lo
correcto: el sitio no debería listar nada que no lo sea.

Lo que ese archivo alimenta hoy es la línea de metadata de cada proyecto —cuándo se pusheó
por última vez, las estrellas, si está archivado—, que es lo que se refresca sin tocar nada.

## Agregar un proyecto

1. Sumá la entrada a `_data/projects.yml`. Campos:
   - `id` — slug público y estable. Para trabajo con NDA **nunca** codifica el nombre del cliente.
   - `listed: true` — lo muestra en el listado y en el home. `false` lo oculta sin borrar nada.
   - `case_study: true` — agrega el link "Leer case study" y **requiere** las dos páginas de detalle.
   - `repo_visibility: public|private` — `public` linkea el repo; `private` muestra la etiqueta
     "repo privado". Un proyecto se puede listar con el repo privado: en ese caso el
     **write-up es el artefacto público**.
   - `short.{es,en}` — una línea por idioma.
   - `status: active|paused|done` — el tag se traduce solo vía `i18n.status`.
2. Si lleva case study, copiá `es/projects/task-queue.md` y `en/projects/task-queue.md`,
   renombralos con el `id` nuevo y ajustá el `permalink`.
3. Commit y push. GitHub Pages buildea solo.

## Agregar una herramienta

Entrada nueva en `_data/tools.yml`. Arranca en `visibility: private` (no aparece); cuando
esté para mostrar, `visibility: public`. El campo `install` es el snippet que la gente copia
y pega, tal cual.

## Actualizar el perfil de /about/

Se edita `_data/cv.yml`. **No se escribe a mano desde cero**: la fuente de verdad es el store
de CVs en `../Cv/store/`. El flujo es:

```sh
python ../Cv/cvq.py gather backend
```

y de ese briefing se baja a `cv.yml` solo lo que sea `visibilidad: publico` y no tenga datos
de contacto. El `cv.yml` es la **proyección pública** del store, no una segunda fuente.

## Publicar el PDF del CV

1. Generar el PDF (ver `../Cv/README.md`).
2. Copiarlo a `cv/`.
3. Poner el nombre del archivo en `cv_pdf.es` / `cv_pdf.en` dentro de `_data/cv.yml`.
   Si el campo está vacío, el botón de descarga no aparece.

Regla: el PDF que se publica en la web es la **versión pública** — sin teléfono ni email,
para no dejarlos expuestos a scrapers. El CV con contacto se manda al aplicar.

## Preview local

Requiere Ruby + Bundler.

```sh
bundle install
bundle exec jekyll serve
```

Abre `http://localhost:4000/`.

El preview local es opcional: GitHub Pages buildea al pushear a `main`. Sirve para iterar
visuales sin ensuciar el historial.

## Estilos

Toda la paleta está en el bloque `:root` de `assets/css/style.scss`. Ninguna regla más abajo
hardcodea un color: para reestilar el sitio entero se tocan esas variables y nada más.

El tema es **oscuro único**, sin variante clara: viene de un PDF de referencia y los stops
del gradiente están muestreados de sus píxeles. El detalle, con los ratios de contraste
medidos, está en `design/README.md` del repo privado.
