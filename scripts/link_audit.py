#!/usr/bin/env python3
"""
link_audit.py — brama jakości linkowania wewnętrznego dla terrariumdla.pl

Liczy <a href> wewnątrz <main>, pomijając ramkę breadcrumbs, nagłówek i stopkę,
i sprawdza, czy każdy wewnętrzny href prowadzi do istniejącego pliku lub
katalogu z index.html. Nie sprawdza <img src> — obrazy weryfikuj ręcznie
(patrz SITE_WORKFLOW.md).

Użycie:
    python3 scripts/link_audit.py                       # cała strona
    python3 scripts/link_audit.py weze gekony            # jeden lub więcej katalogów
    python3 scripts/link_audit.py weze/waz-zbozowy/przewodnik/index.html   # jeden plik
    python3 scripts/link_audit.py --strict               # progi per archetyp z internal-linking-plan.md

Kod wyjścia 1, jeśli którakolwiek strona nie przechodzi progu albo ma martwy
link wewnętrzny.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

FLAT_FLOOR = 5  # minimalna liczba linków w <main>, tryb domyślny (bez --strict)

# Progi per archetyp, zgodne z tabelą w internal-linking-plan.md
STRICT_RULES = [
    (re.compile(r"^index\.html$"), "strona główna", 20),
    (re.compile(r"^[a-z-]+/index\.html$"), "hub rodziny", 10),
    (re.compile(r".*/przewodnik/index\.html$"), "filar gatunku", 10),
    (re.compile(r"^sprzet/"), "strona sprzętu", 6),
    (re.compile(r"^poradniki/"), "poradnik ogólny", 6),
    (re.compile(r"^blog/"), "wpis blogowy", 5),
]
DEFAULT_ARCHETYPE = ("satelita gatunku", 5)

BREADCRUMB_RE = re.compile(
    r'<nav[^>]*class="[^"]*breadcrumbs[^"]*"[^>]*>.*?</nav>', re.DOTALL | re.IGNORECASE
)
MAIN_RE = re.compile(r"<main\b[^>]*>(.*?)</main>", re.DOTALL | re.IGNORECASE)
HREF_RE = re.compile(r'<a\s[^>]*href="([^"]+)"', re.IGNORECASE)


def classify(rel_path: str):
    if not STRICT_MODE:
        return ("płaski próg", FLAT_FLOOR)
    for pattern, name, floor in STRICT_RULES:
        if pattern.match(rel_path):
            return (name, floor)
    return DEFAULT_ARCHETYPE


def resolve_internal_href(href: str, repo_root: Path) -> bool:
    """Zwraca True, jeśli wewnętrzny href prowadzi do realnego pliku/katalogu."""
    path_part = href.split("#")[0].split("?")[0]
    if not path_part or path_part == "/":
        return (repo_root / "index.html").is_file()
    candidate = repo_root / path_part.lstrip("/")
    if candidate.is_file():
        return True
    if candidate.is_dir() and (candidate / "index.html").is_file():
        return True
    # href bez końcowego slasha wskazujący na katalog z index.html
    if not path_part.endswith("/"):
        alt = repo_root / (path_part.lstrip("/") + "/index.html")
        if alt.is_file():
            return True
        alt_html = repo_root / (path_part.lstrip("/") + ".html")
        if alt_html.is_file():
            return True
    return False


def audit_file(file_path: Path, repo_root: Path):
    rel_path = str(file_path.relative_to(repo_root))
    html = file_path.read_text(encoding="utf-8")

    main_match = MAIN_RE.search(html)
    if not main_match:
        return {"path": rel_path, "error": "brak znacznika <main>...</main>"}

    main_html = main_match.group(1)
    main_html_no_crumbs = BREADCRUMB_RE.sub("", main_html)

    hrefs = HREF_RE.findall(main_html_no_crumbs)
    link_count = len(hrefs)

    broken = []
    for href in hrefs:
        if href.startswith("/"):
            if not resolve_internal_href(href, repo_root):
                broken.append(href)

    archetype, floor = classify(rel_path)
    passed = link_count >= floor and not broken

    return {
        "path": rel_path,
        "archetype": archetype,
        "floor": floor,
        "count": link_count,
        "broken": broken,
        "passed": passed,
    }


def collect_html_files(args, repo_root: Path):
    if not args:
        return sorted(repo_root.rglob("index.html")) + sorted(
            p for p in repo_root.rglob("*.html") if p.name != "index.html" and ".git" not in p.parts
        )

    files = []
    for arg in args:
        target = (repo_root / arg).resolve() if not Path(arg).is_absolute() else Path(arg)
        if target.is_file():
            files.append(target)
        elif target.is_dir():
            files.extend(sorted(target.rglob("*.html")))
        else:
            print(f"Ostrzeżenie: nie znaleziono {arg}", file=sys.stderr)
    return files


def main():
    global STRICT_MODE
    raw_args = sys.argv[1:]
    STRICT_MODE = "--strict" in raw_args
    args = [a for a in raw_args if a != "--strict"]

    files = collect_html_files(args, REPO_ROOT)
    files = [f for f in files if ".git" not in f.parts and f.name.endswith(".html")]

    if not files:
        print("Brak plików HTML do sprawdzenia.")
        sys.exit(0)

    any_failed = False
    for f in files:
        result = audit_file(f, REPO_ROOT)
        if "error" in result:
            print(f"BŁĄD  {result['path']}: {result['error']}")
            any_failed = True
            continue

        status = "OK  " if result["passed"] else "FAIL"
        print(
            f"{status}  {result['path']}  "
            f"({result['archetype']}, {result['count']}/{result['floor']} linków)"
        )
        if result["broken"]:
            for b in result["broken"]:
                print(f"      martwy link wewnętrzny: {b}")
            any_failed = True
        if not result["passed"] and not result["broken"]:
            any_failed = True

    sys.exit(1 if any_failed else 0)


if __name__ == "__main__":
    main()
