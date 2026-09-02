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
import re
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


MARCA_DARK = "/* dark forzado por el sitio */"


def bloques_dark(texto: str) -> list[str]:
    """El cuerpo de cada @media (prefers-color-scheme: dark){...}.

    Se cuentan llaves en vez de usar una regex sobre todo el bloque: el cuerpo
    tiene llaves adentro y una regex golosa se comeria medio archivo.
    """
    cuerpos = []
    for m in re.finditer(r"@media[^{]*prefers-color-scheme:\s*dark[^{]*\{", texto):
        i = m.end()
        prof, j = 1, i
        while j < len(texto) and prof:
            if texto[j] == "{":
                prof += 1
            elif texto[j] == "}":
                prof -= 1
            j += 1
        cuerpos.append(texto[i:j - 1])
    return cuerpos


def forzar_dark(datos: bytes) -> bytes:
    """Aplica el bloque dark del archivo FUERA de su media query.

    El sitio es dark siempre. Estos HTML siguen la preferencia del sistema, asi
    que alguien con el SO en claro veia el sitio oscuro y el diagrama blanco.

    No se reescribe el diseno: se toma el bloque que el propio archivo ya define
    para dark -que son overrides de variables sobre :root- y se emite de nuevo
    al final, donde gana por orden de cascada. Donde el selector es
    `:root:not([data-theme=light])`, el toggle manual del archivo sigue
    funcionando: solo cambia cual es el default.

    Un archivo sin bloque dark se devuelve intacto: no hay nada que forzar sin
    inventarle una paleta.
    """
    try:
        texto = datos.decode("utf-8")
    except UnicodeDecodeError:
        return datos

    if MARCA_DARK in texto:
        return datos

    cuerpos = bloques_dark(texto)
    if not cuerpos:
        return datos

    # chr(10) y no un escape: este archivo se genera desde un script y los
    # backslashes no sobreviven bien el viaje.
    nl = chr(10)
    estilo = nl + "<style>" + MARCA_DARK + nl + nl.join(cuerpos) + nl + "</style>" + nl
    cierre = texto.rfind("</body>")
    if cierre == -1:
        texto += estilo
    else:
        texto = texto[:cierre] + estilo + texto[cierre:]

    return texto.encode("utf-8")


def _lum_rel(r: float, g: float, b: float) -> float:
    """Luminancia relativa WCAG de un color en 0..1 por canal."""
    def lineal(c: float) -> float:
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    return 0.2126 * lineal(r) + 0.7152 * lineal(g) + 0.0722 * lineal(b)


def _hsl_a_rgb(tono: float, sat: float, lum: float) -> tuple[float, float, float]:
    if sat == 0:
        return lum, lum, lum

    def canal(p: float, q: float, t: float) -> float:
        t = t % 1
        if t < 1 / 6:
            return p + (q - p) * 6 * t
        if t < 1 / 2:
            return q
        if t < 2 / 3:
            return p + (q - p) * (2 / 3 - t) * 6
        return p

    q = lum * (1 + sat) if lum < 0.5 else lum + sat - lum * sat
    p = 2 * lum - q
    return canal(p, q, tono + 1 / 3), canal(p, q, tono), canal(p, q, tono - 1 / 3)


def _invertir_lum(hexa: str) -> str:
    """Da vuelta la luminancia de un color, conservando tono y saturacion.

    Para un archivo que no trae paleta dark no alcanza con mapear colores a
    mano: son cincuenta y la lista envejece en cuanto el origen cambia uno. Esto
    es una regla, no una tabla.

    Se invierte la luminancia RELATIVA (WCAG), no la de HSL. La diferencia no es
    teorica: un ambar saturado tiene L=0.77 en HSL y se ve casi blanco, asi que
    tratarlo como "medio" dejaba un badge claro con texto claro encima, 1.02:1
    de contraste. Medido sobre los informes, no supuesto.

    El L de HSL que da una luminancia objetivo depende del tono, asi que se
    resuelve por biseccion: doce pasos dejan el error por debajo de lo que el
    ojo distingue.

    El objetivo se comprime a [0.02, 0.88] para no terminar en blanco o negro
    puros, que sobre pantalla vibran.
    """
    h = hexa.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))

    alto, bajo = max(r, g, b), min(r, g, b)
    lum = (alto + bajo) / 2

    if alto == bajo:
        tono = sat = 0.0
    else:
        d = alto - bajo
        sat = d / (2 - alto - bajo) if lum > 0.5 else d / (alto + bajo)
        if alto == r:
            tono = ((g - b) / d + (6 if g < b else 0)) / 6
        elif alto == g:
            tono = ((b - r) / d + 2) / 6
        else:
            tono = ((r - g) / d + 4) / 6

    objetivo = 0.88 - 0.86 * _lum_rel(r, g, b)

    izq, der = 0.0, 1.0
    for _ in range(12):
        medio = (izq + der) / 2
        if _lum_rel(*_hsl_a_rgb(tono, sat, medio)) < objetivo:
            izq = medio
        else:
            der = medio

    r2, g2, b2 = _hsl_a_rgb(tono, sat, (izq + der) / 2)
    return "#{:02x}{:02x}{:02x}".format(*(max(0, min(255, round(c * 255))) for c in (r2, g2, b2)))

def invertir_a_dark(datos: bytes) -> bytes:
    """Convierte a dark un HTML que solo trae paleta clara."""
    try:
        texto = datos.decode("utf-8")
    except UnicodeDecodeError:
        return datos

    if MARCA_DARK in texto:
        return datos

    texto = re.sub(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b",
                   lambda m: _invertir_lum(m.group(0)), texto)

    # Invertir hex no alcanza: el texto que no declara color hereda el negro por
    # defecto del navegador, que sobre blanco se leia y sobre oscuro desaparece.
    # Medido en el informe de riesgo alto: 20 de 157 elementos quedaban en
    # rgb(0,0,0). Se fija un color base y el color-scheme, que ademas arregla
    # scrollbars y controles nativos.
    # Invertir color por color no puede preservar el contraste de un PAR: cuando
    # el original era texto oscuro sobre fondo medio, los dos terminan claros.
    # Medido: .verdict-warning pasaba de 10.95:1 a 1.85:1.
    #
    # Los badges son un conjunto chico y con nombre, asi que se fijan a mano en
    # vez de confiar en el algoritmo. De paso se arreglan dos que YA fallaban en
    # el original -.verdict-fail daba 2.80:1 y .verdict-pass 2.28:1, los dos con
    # blanco sobre un color medio-, que es un defecto de la plantilla y no de
    # esta conversion.
    badges = (
        ".verdict-blocker{background:#f87171;color:#1a0505}"
        ".verdict-fail{background:#fb923c;color:#1a0d00}"
        ".verdict-warning{background:#fbbf24;color:#1a1200}"
        ".verdict-pass{background:#4ade80;color:#04180b}"
        # `text-black` de Tailwind sobre un badge de color: la inversion lo
        # volvia claro y quedaba claro sobre claro. Los fondos de badge quedan
        # medios o claros, asi que ese texto tiene que seguir siendo oscuro.
        ".text-black{color:#14100a}"
    )

    nl = chr(10)
    base = (nl + "<style>" + MARCA_DARK + nl
            + "html{color-scheme:dark}" + nl
            + "body{color:#d5dae3}" + nl
            + badges + nl
            + "</style>" + nl)

    cierre = texto.rfind("</body>")
    texto = texto + base if cierre == -1 else texto[:cierre] + base + texto[cierre:]

    return texto.encode("utf-8")


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

        # Un repo que paso a privado deja de ser alcanzable por raw. Se congela
        # en vez de sacarlo del manifiesto: lo ya publicado sigue sirviendose y
        # queda escrito por que no se actualiza mas. Sacarlo haria que el dia
        # que vuelva a ser publico nadie se acuerde de reponerlo.
        if cfg.get("congelado"):
            motivo = cfg.get("motivo", "sin motivo declarado")
            print(f"  {carpeta}  [congelado] {motivo}")
            print(f"    se conserva lo publicado; no se sincroniza contra {repo}")
            continue

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

            # Un archivo con paleta dark propia se fuerza a usarla. Uno que solo
            # trae paleta clara se invierte, y eso se declara en el manifiesto:
            # invertir por adivinanza terminaria dando vuelta algo que debia
            # quedarse claro.
            if destino in cfg.get("invertir", []):
                datos = invertir_a_dark(datos)
            else:
                datos = forzar_dark(datos)

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
