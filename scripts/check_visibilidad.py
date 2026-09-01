#!/usr/bin/env python3
"""Verifica la regla del sitio: lo publico linkea el repo, lo privado no.

ZERO dependencias: solo stdlib.

La regla
--------
El sitio es para presentarse. Un proyecto con repo publico se lista CON link al
repo; uno con repo privado se explica y se muestra, pero SIN link. `projects.yml`
ya lo documenta en `repo_visibility`.

El mecanismo es declarativo: alguien tiene que escribir `repo_visibility:
private` a mano. Este script existe porque acordarse no es un mecanismo. Falla
si:

  1. Un proyecto declara `public` y el repo ya no lo es (link roto para un
     recruiter, que es el unico lector que importa).
  2. Un proyecto declara `private` y el repo en realidad es publico (se esta
     ocultando un repo que podria mostrarse).
  3. Un proyecto privado dejo el link al repo en el hero de su case study. El
     listado respeta `repo_visibility` solo; el hero es HTML a mano y no.

Lo que NO hace: decidir que se lista. Eso es curado y vive en projects.yml.

Uso:
    python scripts/check_visibilidad.py          # sale 1 si hay desvios
    python scripts/check_visibilidad.py -v       # ademas lista lo que esta bien
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE.parent
API = "https://api.github.com"


def entradas(path: Path, campo_vis: str) -> list[dict]:
    """Parsea la lista de entradas de un YAML plano.

    A mano, igual que sync_repos: son listas de un nivel con claves indentadas
    dos espacios, y no vale sumar pyyaml al sitio por esto.
    """
    if not path.exists():
        return []

    items: list[dict] = []
    for linea in path.read_text(encoding="utf-8").splitlines():
        if linea.startswith("- id:"):
            items.append({"id": linea.split(":", 1)[1].strip().strip("\"'")})
        elif items and linea.startswith("  ") and ":" in linea:
            clave, _, valor = linea.strip().partition(":")
            if clave in ("repo", campo_vis, "case_study"):
                items[-1][clave] = valor.strip().strip("\"'")

    return items


def visibilidad_real(url: str, token: str | None) -> str:
    """'public', 'private' o 'error:<detalle>'.

    La visibilidad se lee del campo `private` de la respuesta, NO de si la
    llamada dio 200. Deducirla del codigo estaba mal: con un token que si tiene
    acceso al repo privado la llamada devuelve 200 y el repo figuraba publico.
    El campo dice la verdad con cualquier token, y sin token tambien.

    Un 404 es privado o inexistente: desde afuera son indistinguibles, y para un
    recruiter dan lo mismo. Cualquier otro fallo se reporta como error en vez de
    asumir: un rate limit no puede hacer que un repo publico figure cerrado.
    """
    slug = url.split("github.com/", 1)[-1].strip("/")
    req = urllib.request.Request(f"{API}/repos/{slug}", headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "check-visibilidad",
    })
    if token:
        req.add_header("Authorization", f"Bearer {token}")

    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return "private" if json.load(r).get("private") else "public"
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "private"
        return f"error:HTTP {e.code}"
    except urllib.error.URLError as e:
        return f"error:{e.reason}"


def hero_linkea(pid: str, url: str) -> bool | None:
    """True/False si hay case study; None si el proyecto no tiene."""
    encontrado = None
    for lang in ("es", "en"):
        f = SITE / lang / "projects" / f"{pid}.md"
        if not f.exists():
            continue
        hero = f.read_text(encoding="utf-8").split("</section>", 1)[0]
        encontrado = bool(encontrado) or (url in hero)
    return encontrado


def main() -> None:
    ap = argparse.ArgumentParser(description="Verifica la regla publico/privado del sitio")
    ap.add_argument("-v", "--verbose", action="store_true", help="listar tambien lo correcto")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    fuentes = [
        (SITE / "_data" / "projects.yml", "repo_visibility", True),
        (SITE / "_data" / "tools.yml", "visibility", False),
    ]

    desvios: list[str] = []
    revisados = 0

    for path, campo, con_case_study in fuentes:
        for e in entradas(path, campo):
            url = e.get("repo")
            if not url:
                continue

            revisados += 1
            pid = e["id"]
            declarada = e.get(campo, "(sin declarar)")
            real = visibilidad_real(url, token)

            if real.startswith("error:"):
                desvios.append(f"{pid}: no pude verificar ({real[6:]}). "
                               f"No se asume nada: revisar a mano.")
                continue

            if declarada != real:
                desvios.append(
                    f"{pid}: declara '{declarada}' y el repo es {real}. "
                    + ("El link del sitio esta roto para cualquiera que lo abra."
                       if real == "private" else
                       "Se esta ocultando un repo que podria mostrarse."))

            if con_case_study and real == "private" and hero_linkea(pid, url):
                desvios.append(f"{pid}: es privado pero su case study todavia linkea el repo. "
                               f"El listado respeta repo_visibility; el hero es HTML a mano.")

            if args.verbose and not desvios:
                print(f"  ok  {pid:26} {real}")

    print(f"\n{revisados} repo(s) verificado(s).")

    if desvios:
        print(f"\n{len(desvios)} desvio(s) de la regla publico/privado:\n", file=sys.stderr)
        for d in desvios:
            print(f"  - {d}", file=sys.stderr)
        print("\nRegla: lo publico linkea el repo; lo privado se explica y se muestra, "
              "sin link.", file=sys.stderr)
        sys.exit(1)

    print("Sin desvios: lo publico linkea, lo privado no.")


if __name__ == "__main__":
    main()
