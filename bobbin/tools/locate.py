"""Fail-closed bootstrap locator — list exact missing required artifacts.

II.A.1 lift: enumerate every missing required path; no folder guessing.
Exit 0 when complete; exit 1 when anything is missing.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from expected_scripts import EXPECTED_SCRIPTS

_TOOLS = Path(__file__).resolve().parent
_SKILL_DEFAULT = _TOOLS.parent


def _resolve_skill(explicit: Path | None) -> Path:
    if explicit is not None:
        return explicit.resolve()
    cursor_install = Path.cwd() / ".cursor" / "skills" / "bobbin"
    if cursor_install.is_dir():
        return cursor_install.resolve()
    return _SKILL_DEFAULT.resolve()


def required_relative_paths() -> list[str]:
    paths = [
        "SKILL.md",
        "references/PROCEDURE.md",
        "references/states-v2-03.md",
        "scripts",
    ]
    for name in EXPECTED_SCRIPTS:
        paths.append(f"scripts/{name}")
    return paths


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Fail-closed list of missing bobbin install artifacts."
    )
    parser.add_argument(
        "--skill-dir",
        type=Path,
        default=None,
        help="Skill root to check (default: .cursor/skills/bobbin or this package).",
    )
    args = parser.parse_args(argv)
    skill = _resolve_skill(args.skill_dir)
    print(f"SKILL: {skill.as_posix()}")

    missing: list[str] = []
    for rel in required_relative_paths():
        path = skill / rel
        if rel == "scripts":
            if not path.is_dir():
                missing.append(rel)
            continue
        if not path.is_file():
            missing.append(rel)

    if not missing:
        print("MISSING: none")
        print(f"OK: bootstrap complete ({len(EXPECTED_SCRIPTS)} scripts + refs).")
        return 0

    print(f"MISSING: {len(missing)}")
    for rel in missing:
        print(f"MISSING: {rel}")
    print("NEXT: restore the named paths; do not invent alternate trees.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
