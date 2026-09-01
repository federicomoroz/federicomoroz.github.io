# Sincronizacion automatica

Dos scripts, los dos stdlib puro y los dos con su workflow:

| Script | Que escribe | Cuando corre |
|---|---|---|
| `sync_repos.py` | `_data/repos.yml` | diario 06:17 UTC · a demanda · al tocar los curados |
| `sync_diagrams.py` | `diagramas/**/*.html` | diario 06:37 UTC · a demanda · `repository_dispatch` |
| `check_visibilidad.py` | nada: solo verifica | en push · diario 06:57 UTC · a demanda |

## sync_diagrams

Los diagramas se generan en el repo de cada proyecto. Antes se copiaban a mano,
asi que la copia publicada podia quedar vieja sin que nada avisara.

La primera corrida los encontro **a todos al dia**: el drift era un riesgo, no
una deuda acumulada. (En la primera version el script reportaba los cinco de
contracargos como desactualizados, pero era un falso positivo por fin de linea
CRLF contra LF; ver `normalizar()`.)

Que sincronizar sale de `scripts/diagramas.json`. Agregar un proyecto es una
entrada ahi, no un workflow nuevo:

```jsonc
"mi-proyecto": {
  "repo": "federicomoroz/mi-repo",
  "branch": "main",
  "archivos": { "destino.html": "docs/diagrams/origen.html" }
}
```

Solo funciona con repos **publicos**: se bajan por `raw.githubusercontent` sin
credenciales. Si un repo pasa a privado, el workflow falla ruidosamente en vez
de publicar una pagina de error — que es lo que se quiere.

Antes de escribir nada valida que la respuesta sea 200, pese al menos 2 KB y
parezca HTML. Si un archivo falla, **aborta la corrida entera sin tocar el
disco**: dejar la carpeta con unos diagramas nuevos y otros viejos seria peor
que no sincronizar.

```sh
python scripts/sync_diagrams.py            # sincroniza
python scripts/sync_diagrams.py --check    # no escribe; sale 1 si hay algo viejo
python scripts/sync_diagrams.py --solo contracargos
```

## Sincronizacion inmediata (opcional)

Con lo de arriba, un diagrama regenerado tarda hasta 24 h en publicarse, o se
sube a mano desde **Actions -> sync-diagrams -> Run workflow**.

Para que salga en el momento, el repo de origen tiene que avisar. Hace falta un
token porque el `GITHUB_TOKEN` de un repo no puede disparar workflows en otro.

**1. Crear un fine-grained PAT** en Settings -> Developer settings -> Personal
access tokens. Alcance minimo: solo el repositorio `federicomoroz.github.io`,
permiso **Contents: read and write**. Nada mas.

**2. Guardarlo** como secret `SITIO_DISPATCH_TOKEN` en cada repo de origen
(Settings -> Secrets and variables -> Actions).

**3. Agregar este workflow** en el repo de origen:

```yaml
name: avisar-al-sitio
on:
  push:
    branches: [main]      # 'master' en MegaTrainingSystem
    paths:
      - "docs/diagrams/**"       # o 'docs/architecture/**'
jobs:
  avisar:
    runs-on: ubuntu-latest
    steps:
      - name: Disparar sync-diagrams
        run: |
          curl -sS -X POST \
            -H "Authorization: Bearer ${{ secrets.SITIO_DISPATCH_TOKEN }}" \
            -H "Accept: application/vnd.github+json" \
            https://api.github.com/repos/federicomoroz/federicomoroz.github.io/dispatches \
            -d '{"event_type":"diagramas-actualizados"}'
```

El `paths` importa: sin el, cada push al repo dispara una corrida al pedo.

**Si no se hace nada de esto, el sistema igual funciona** — solo que con hasta
un dia de retraso en vez de al instante. El cron diario es la red de seguridad,
no el plan B.

## check_visibilidad

La regla del sitio: **lo publico linkea el repo; lo privado se explica y se
muestra, sin link.** Es declarativa —alguien escribe `repo_visibility: private`
a mano— y acordarse no es un mecanismo.

Falla si un proyecto declara `public` y el repo ya no lo es, si declara
`private` uno que si es publico, o si un proyecto privado dejo el link en el
hero de su case study. Ese ultimo importa porque el listado respeta
`repo_visibility` solo; el hero es HTML escrito a mano y no lo mira nadie.

La visibilidad se lee del campo `private` de la API, **no** de si la llamada dio
200: con un token que si tiene acceso al repo privado, deducirla del codigo lo
daba como publico. Si la API falla por otra cosa —rate limit, red— lo reporta
como "no pude verificar" en vez de asumir: una alarma falsa aca haria sacar un
link que estaba bien.

```sh
python scripts/check_visibilidad.py       # sale 1 si hay desvios
python scripts/check_visibilidad.py -v    # lista tambien lo correcto
```
