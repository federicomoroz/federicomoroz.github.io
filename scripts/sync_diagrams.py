#!/usr/bin/env python3
"""Copia los diagramas HTML desde los repos de origen a diagramas/.

ZERO dependencias: solo stdlib.

Por que existe
--------------
Los diagramas se generan en el repo de cada proyecto y se servian aca copiados
a mano. Cuando alla se regeneraban, la copia publicada quedaba vieja sin que
nada avisara. Ya habian pasado dos proyectos por lo mismo.

Que hace, y que NO hace
-----------------------
Escribe los archivos listados en `diagramas.json`, que son **generados**: se
pisan enteros en cada corrida y no se editan a mano.

NO toca el `README.md` de diagramas/ ni decide que proyecto se publica. Eso es
criterio editorial y vive en el case study de cada proyecto.

La red no es confiable, asi que nada se escribe sin validar antes: una respuesta
que no sea 200, que venga vacia o que no parezca HTML aborta la corrida entera
sin tocar el disco. Pisar un diagrama bueno con una pagina de error de GitHub
seria peor que no sincronizar.

Uso:
    python scripts/sync_diagrams.py
    python scripts/sync_diagrams.py --check      # no escribe: dice que cambiaria
    python scripts/sync_diagrams.py --solo mega-training-system
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE.parent
MANIFIESTO = HERE / "diagramas.json"
DESTINO = SITE / "diagramas"

RAW = "https://raw.githubusercontent.com"

# Un diagrama real pesa decenas de KB. Cualquier cosa mas chica que esto es una
# pagina de error, un redirect o un archivo truncado.
MINIMO_BYTES = 2048


def bajar(repo: str, branch: str, ruta: str) -> bytes:
    url = f"{RAW}/{repo}/{branch}/{ruta}"
    req = urllib.request.Request(url, headers={"User-Agent": "sync-diagrams-script"})

    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            if r.status != 200:
                raise RuntimeError(f"HTTP {r.status}")
            return r.read()
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code} en {url}") from None
    except urllib.error.URLError as e:
        raise RuntimeError(f"sin respuesta de {url}: {e.reason}") from None


def normalizar(datos: bytes) -> bytes:
    """Fin de linea unificado, para poder comparar dos copias del mismo archivo.

    En Windows con core.autocrlf=true la copia de trabajo queda con CRLF, y lo
    que baja de raw.githubusercontent viene con LF. Comparar bytes crudos daba
    TODOS los archivos como desactualizados en cada corrida local: ruido puro,
    y peor, un "hallazgo" de drift que no existia.
    """
    return datos.replace(b"\r\n", b"\n")


def validar(datos: bytes, url: str) -> None:
    """Aborta si lo que llego no puede ser un diagrama."""
    if len(datos) < MINIMO_BYTES:
        raise RuntimeError(f"{url}: solo {len(datos)} bytes, esperaba >= {MINIMO_BYTES}")

    cabeza = datos[:2048].lower()
    if b"<html" not in cabeza and b"<!doctype" not in cabeza:
        raise RuntimeError(f"{url}: no parece HTML")


def main() -> None:
    ap = argparse.ArgumentParser(description="Sincroniza los diagramas desde sus repos")
    ap.add_argument("--check", action="store_true",
                    help="no escribe nada; informa que cambiaria y sale 1 si hay cambios")
    ap.add_argument("--solo", default=None, help="sincronizar una sola carpeta")
    args = ap.parse_args()

    manifiesto = json.loads(MANIFIESTO.read_text(encoding="utf-8"))
    proyectos = {k: v for k, v in manifiesto.items() if not k.startswith("_")}
    if args.solo:
        if args.solo not in proyectos:
            print(f"  [error] '{args.solo}' no esta en el manifiesto", file=sys.stderr)
            sys.exit(1)
        proyectos = {args.solo: proyectos[args.solo]}

    print(f"Sincronizando diagramas de {len(proyectos)} proyecto(s)...\n")

    # Primero se baja y valida TODO, despues se escribe. Asi una falla a mitad
    # de camino no deja la carpeta con unos archivos nuevos y otros viejos.
    pendientes: list[tuple[Path, bytes, str]] = []
    for carpeta, cfg in proyectos.items():
        repo, branch = cfg["repo"], cfg["branch"]
        print(f"  {carpeta}  <- {repo}@{branch}")

        for destino, origen in cfg["archivos"].items():
            url = f"{RAW}/{repo}/{branch}/{origen}"
            try:
                datos = bajar(repo, branch, origen)
                validar(datos, url)
            except RuntimeError as e:
                print(f"    [error] {e}", file=sys.stderr)
                print("\n  Nada se escribio: la corrida aborta entera para no dejar "
                      "la carpeta a medias.", file=sys.stderr)
                sys.exit(1)

            ruta = DESTINO / carpeta / destino
            previo = ruta.read_bytes() if ruta.exists() else None

            # Se compara normalizando fin de linea. En Windows, con
            # core.autocrlf=true, la copia de trabajo tiene CRLF y lo que baja
            # de raw.githubusercontent viene con LF: comparar bytes crudos daba
            # TODOS los archivos como desactualizados en cada corrida.
            if previo is not None and normalizar(previo) == normalizar(datos):
                print(f"    = {destino}  ({len(datos) // 1024} KB, sin cambios)")
            else:
                estado = "nuevo" if previo is None else "actualizado"
                print(f"    + {destino}  ({len(datos) // 1024} KB, {estado})")
                pendientes.append((ruta, datos, f"{carpeta}/{destino}"))

    if not pendientes:
        print("\nTodo al dia.")
        return

    if args.check:
        print(f"\n[check] {len(pendientes)} archivo(s) desactualizado(s):")
        for _, _, nombre in pendientes:
            print(f"  - {nombre}")
        sys.exit(1)

    for ruta, datos, nombre in pendientes:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_bytes(datos)

    print(f"\n{len(pendientes)} archivo(s) actualizado(s).")


if __name__ == "__main__":
    main()
