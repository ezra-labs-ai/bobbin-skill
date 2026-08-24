"""Park / restore / check gitignored bobbin live-state files.

I.A.2 lift: one command parks the three live files outside the wipe tree.
Files: settings.json, coach-summary.txt, coach-notes.md
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

LIVE_NAMES: tuple[str, ...] = (
    "settings.json",
    "coach-summary.txt",
    "coach-notes.md",
)

_TOOLS = Path(__file__).resolve().parent
_SKILL_DEFAULT = _TOOLS.parent  # skills/bobbin (or junction target)


def _resolve_live_dir(explicit: Path | None) -> Path:
    if explicit is not None:
        return explicit.resolve()
    # Prefer project install path when present beside cwd.
    cursor_install = Path.cwd() / ".cursor" / "skills" / "bobbin"
    if cursor_install.is_dir():
        return cursor_install.resolve()
    return _SKILL_DEFAULT.resolve()


def _resolve_park(explicit: Path | None, live_dir: Path) -> Path:
    if explicit is not None:
        return explicit.resolve()
    # Park outside the skill tree: workspace .bobbin-park/
    # live may be .cursor/skills/bobbin or skills/bobbin — park at repo/workspace root.
    for parent in [live_dir, *live_dir.parents]:
        if (parent / ".git").exists():
            return (parent / ".bobbin-park").resolve()
        if parent.name == ".cursor" or (
            parent.name == "skills" and (parent.parent / ".git").exists()
        ):
            continue
    return (Path.cwd() / ".bobbin-park").resolve()


def cmd_park(live_dir: Path, park_dir: Path) -> int:
    park_dir.mkdir(parents=True, exist_ok=True)
    parked = 0
    for name in LIVE_NAMES:
        src = live_dir / name
        if not src.is_file():
            print(f"MISSING: {name} (skip)")
            continue
        dest = park_dir / name
        shutil.copy2(src, dest)
        print(f"PARKED: {name} -> {dest.as_posix()}")
        parked += 1
    if parked == 0:
        print("OK: nothing to park (no live-state files present yet).")
        return 0
    print(f"OK: parked {parked} file(s) under {park_dir.as_posix()}")
    return 0


def cmd_restore(live_dir: Path, park_dir: Path) -> int:
    if not park_dir.is_dir():
        print(f"MISSING: park dir {park_dir.as_posix()}")
        return 1
    live_dir.mkdir(parents=True, exist_ok=True)
    restored = 0
    for name in LIVE_NAMES:
        src = park_dir / name
        if not src.is_file():
            print(f"MISSING: park/{name} (skip)")
            continue
        dest = live_dir / name
        shutil.copy2(src, dest)
        print(f"RESTORED: {name} -> {dest.as_posix()}")
        restored += 1
    if restored == 0:
        print("NEXT: park is empty — nothing to restore.")
        return 1
    print(f"OK: restored {restored} file(s) into {live_dir.as_posix()}")
    return 0


def cmd_check(live_dir: Path, park_dir: Path) -> int:
    """Verify park holds a copy of every live file that currently exists."""
    live_present = [n for n in LIVE_NAMES if (live_dir / n).is_file()]
    if not live_present:
        print("OK: no live-state files present; park check not required.")
        return 0
    if not park_dir.is_dir():
        print(f"MISSING: park dir {park_dir.as_posix()}")
        for name in live_present:
            print(f"UNPARKED: {name}")
        return 1
    bad = 0
    for name in live_present:
        if (park_dir / name).is_file():
            print(f"PARK_OK: {name}")
        else:
            print(f"UNPARKED: {name}")
            bad += 1
    if bad:
        print("NEXT: run park before wipe/replace.")
        return 1
    print("OK: park covers every present live-state file.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Park, restore, or check bobbin live-state files."
    )
    parser.add_argument(
        "action",
        choices=("park", "restore", "check"),
        help="park = copy live -> .bobbin-park; restore = copy back; check = verify park.",
    )
    parser.add_argument(
        "--live-dir",
        type=Path,
        default=None,
        help="Skill install with live files (default: .cursor/skills/bobbin or this package).",
    )
    parser.add_argument(
        "--park-dir",
        type=Path,
        default=None,
        help="Park directory (default: <repo>/.bobbin-park).",
    )
    args = parser.parse_args(argv)
    live_dir = _resolve_live_dir(args.live_dir)
    park_dir = _resolve_park(args.park_dir, live_dir)
    print(f"LIVE: {live_dir.as_posix()}")
    print(f"PARK: {park_dir.as_posix()}")
    if args.action == "park":
        return cmd_park(live_dir, park_dir)
    if args.action == "restore":
        return cmd_restore(live_dir, park_dir)
    return cmd_check(live_dir, park_dir)


if __name__ == "__main__":
    raise SystemExit(main())
