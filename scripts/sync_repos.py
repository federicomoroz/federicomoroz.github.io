#!/usr/bin/env python3
"""Descubre los repos publicos de GitHub y regenera _data/repos.yml.

ZERO dependencias: solo stdlib.

Que hace, y que NO hace
-----------------------
Escribe `_data/repos.yml`, que es **generado**: nunca se edita a mano, y se
pisa entero en cada corrida. Ahi viven los hechos que GitHub ya sabe —
descripcion, lenguaje, topics, stars, ultimo push, si esta archivado.

NO toca `_data/projects.yml`, que es **curado**: los resumenes bilingues, que
proyecto se lista, cual tiene case study y en que orden aparecen. Eso es
criterio editorial y ningun script lo puede adivinar.

De ahi el reparto:

    el contenido se refresca solo   ->  repos.yml, automatico
    la inclusion se decide a mano   ->  projects.yml, curado

Un repo publico nuevo aparece en repos.yml y el script lo REPORTA, pero no se
publica en el sitio hasta que se le escriba una entrada en projects.yml. Si no,
cualquier repo de prueba termina en el portfolio.

Solo ve repos PUBLICOS. Es una limitacion real, no un descuido: la API sin
credenciales no ve otra cosa, y el sitio tampoco deberia.

Uso:
    python scripts/sync_repos.py
    python scripts/sync_repos.py --user federicomoroz --check
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE.parent
OUT = SITE / "_data" / "repos.yml"
# Los dos archivos curados donde un repo puede tener entrada.
CURADOS = (SITE / "_data" / "projects.yml", SITE / "_data" / "tools.yml")

API = "https://api.github.com"

# El repo del sitio no se lista a si mismo.
SKIP = {"federicomoroz.github.io"}


def fetch(url: str) -> list | dict:
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "sync-repos-script",
    })

    # Dentro de GitHub Actions hay token: sube el rate limit de 60/h a 1000/h.
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")

    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 403:
            print("  [error] rate limit de la API. Con GITHUB_TOKEN sube a 1000/h.",
                  file=sys.stderr)
        raise


def public_repos(user: str) -> list[dict]:
    out: list[dict] = []
    page = 1

    while True:
        batch = fetch(f"{API}/users/{user}/repos?per_page=100&page={page}&sort=pushed")
        if not batch:
            break
        out.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    return out


def yaml_str(v) -> str:
    """Escala a YAML con comillas dobles, escapando lo justo."""
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v).replace("\\", "\\\\").replace('"', '\\"')
    s = s.replace("\n", " ").replace("\r", " ")
    return f'"{s}"'


def render(user: str, repos: list[dict]) -> str:
    L = [
        "# GENERADO POR scripts/sync_repos.py — NO EDITAR A MANO.",
        "#",
        "# Se pisa entero en cada corrida. Los hechos de GitHub viven aca; los",
        "# resumenes bilingues y que se lista viven en projects.yml, que es curado",
        "# y el script no toca.",
        "#",
        f"# usuario: {user}",
        f"# generado: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "",
        f"user: {yaml_str(user)}",
        f"generated_at: {yaml_str(datetime.now(timezone.utc).isoformat(timespec='seconds'))}",
        f"count: {len(repos)}",
        "",
        "repos:",
    ]

    for r in repos:
        L.append(f"  - name: {yaml_str(r['name'])}")
        L.append(f"    full_name: {yaml_str(r['full_name'])}")
        L.append(f"    url: {yaml_str(r['html_url'])}")
        L.append(f"    description: {yaml_str(r.get('description'))}")
        L.append(f"    language: {yaml_str(r.get('language'))}")
        L.append(f"    homepage: {yaml_str(r.get('homepage') or None)}")
        L.append(f"    stars: {r.get('stargazers_count', 0)}")
        L.append(f"    forks: {r.get('forks_count', 0)}")
        L.append(f"    archived: {yaml_str(bool(r.get('archived')))}")
        L.append(f"    is_fork: {yaml_str(bool(r.get('fork')))}")
        L.append(f"    pushed_at: {yaml_str(r.get('pushed_at'))}")
        L.append(f"    created_at: {yaml_str(r.get('created_at'))}")

        topics = r.get("topics") or []
        if topics:
            L.append("    topics:")
            for t in topics:
                L.append(f"      - {yaml_str(t)}")
        else:
            L.append("    topics: []")

    return "\n".join(L) + "\n"


def curated_repo_urls() -> set[str]:
    """Las URLs de repo que ya tienen entrada en projects.yml o en tools.yml.

    Se parsea a mano para no depender de pyyaml: alcanza con las lineas `repo:`.
    Hay que mirar los DOS archivos: una herramienta como envcheck vive en
    tools.yml, y mirando solo projects.yml se reportaria como sin curar en cada
    corrida.
    """
    urls = set()

    for path in CURADOS:
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("repo:"):
                urls.add(line.split("repo:", 1)[1].strip().strip('"\''))

    return urls


def report(repos: list[dict]) -> int:
    """Compara lo descubierto contra lo curado. Devuelve la cantidad de avisos."""
    curated = curated_repo_urls()
    live = {r["html_url"] for r in repos}

    sin_curar = [r for r in repos if r["html_url"] not in curated]
    ya_no_publicos = curated - live

    avisos = 0

    if sin_curar:
        avisos += len(sin_curar)
        print(f"\n  {len(sin_curar)} repo(s) publico(s) SIN entrada curada:")
        for r in sin_curar:
            desc = (r.get("description") or "")[:58]
            print(f"    - {r['name']:32} {r.get('language') or '-':12} {desc}")
        print("    -> No aparecen en el sitio hasta que se les escriba una entrada.")

    if ya_no_publicos:
        avisos += len(ya_no_publicos)
        print(f"\n  {len(ya_no_publicos)} repo(s) curado(s) que YA NO son publicos:")
        for u in sorted(ya_no_publicos):
            print(f"    - {u}")
        print("    -> Se volvieron privados, se renombraron o se borraron.")
        print("       Revisar la entrada: el link publico esta roto.")

    if not avisos:
        print("\n  Sin novedades: todo repo publico tiene entrada y viceversa.")

    return avisos


def main() -> None:
    ap = argparse.ArgumentParser(description="Sincroniza los repos publicos a _data/repos.yml")
    ap.add_argument("--user", default="federicomoroz")
    ap.add_argument("--include-forks", action="store_true",
                    help="incluir forks (por defecto se omiten)")
    ap.add_argument("--check", action="store_true",
                    help="no escribe nada; solo reporta")
    args = ap.parse_args()

    print(f"Consultando los repos publicos de {args.user}...")
    todos = public_repos(args.user)

    repos = [r for r in todos
             if r["name"] not in SKIP
             and (args.include_forks or not r.get("fork"))]

    omitidos = len(todos) - len(repos)
    print(f"  {len(repos)} repos ({omitidos} omitidos: el sitio y los forks)")

    avisos = report(repos)

    if args.check:
        print("\n--check: no se escribio nada.")
        sys.exit(1 if avisos else 0)

    nuevo = render(args.user, repos)
    anterior = OUT.read_text(encoding="utf-8") if OUT.exists() else ""

    # `generated_at` cambia siempre; comparar sin esa linea evita commits vacios.
    def sin_fecha(t: str) -> str:
        return "\n".join(l for l in t.splitlines()
                         if not l.startswith(("generated_at:", "# generado:")))

    if sin_fecha(nuevo) == sin_fecha(anterior):
        print(f"\n  {OUT.name} sin cambios.")
        return

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(nuevo, encoding="utf-8", newline="\n")
    print(f"\n  {OUT.name} actualizado.")


if __name__ == "__main__":
    main()
