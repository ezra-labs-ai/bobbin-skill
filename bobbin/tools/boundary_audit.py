"""Boundary audit — flag escapes outside the published bobbin skill folder.

I.A.1 lift: cold run lists escape paths that exist on disk. Does not invent folders.
Exit 0 when clean; exit 1 when one or more escapes are present.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
_SKILL = _TOOLS.parent  # bobbin/ (install unit)


def _find_repo_root(start: Path) -> Path:
    cur = start.resolve()
    for parent in [cur, *cur.parents]:
        if (parent / ".git").exists():
            return parent
    # Fall back: bobbin/ at repo root, or skills/bobbin in a factory tree
    if _SKILL.name == "bobbin" and _SKILL.parent.name == "skills":
        return _SKILL.parent.parent
    if _SKILL.name == "bobbin":
        return _SKILL.parent
    return cur


def _rel(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return str(path.resolve())


def collect_escapes(root: Path) -> list[str]:
    """Return relative paths that sit outside the published bobbin surface."""
    found: list[str] = []
    skills = root / "skills"

    # Sibling skill trees (anything under skills/ that is not bobbin).
    if skills.is_dir():
        for child in sorted(skills.iterdir()):
            if child.name == "bobbin":
                continue
            if child.name.startswith("."):
                continue
            found.append(_rel(root, child))

    # Legacy recovery tree at repo root.
    recovery = root / "recovery"
    if recovery.exists():
        found.append(_rel(root, recovery))

    # Archive park of old product trees (intentional park — still an escape from surface).
    archive = root / "archive"
    if archive.exists():
        found.append(_rel(root, archive))
        for name in ("recovery", "skills", "docs"):
            nested = archive / name
            if nested.exists():
                found.append(_rel(root, nested))

    # Residue inside the published skill that should not ship.
    residue_names = (
        "journal.py",
        "journal.template.jsonl",
        "journal.jsonl",
        "fixtures",
        "references/blocks-v2-03.md",
        "references/blocks-v2-02.md",
        "references/blocks-v2-01.md",
    )
    for name in residue_names:
        path = _SKILL / name
        if path.exists():
            # Prefer path relative to repo when skill lives under skills/bobbin.
            if root in path.resolve().parents or path.resolve().parent == root:
                found.append(_rel(root, path))
            else:
                found.append(f"bobbin/{name}")

    # Deduplicate, keep order.
    seen: set[str] = set()
    out: list[str] = []
    for item in found:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Flag sibling/archive/recovery escapes vs the bobbin skill folder."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Repo root to audit (default: walk up from this skill for .git).",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve() if args.root else _find_repo_root(_SKILL)

    print(f"SURFACE: bobbin/")
    print(f"ROOT: {root.as_posix()}")
    escapes = collect_escapes(root)
    if not escapes:
        print("ESCAPES: none")
        print("OK: published surface is the only skill tree on disk.")
        return 0

    print(f"ESCAPES: {len(escapes)}")
    for path in escapes:
        print(f"ESCAPE: {path}")
    print("NEXT: keep product work under bobbin/; park or remove escapes.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
