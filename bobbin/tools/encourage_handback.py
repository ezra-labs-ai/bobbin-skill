"""Append post-script ENCOURAGEMENT to coach-summary.txt.

III.B.1 lift helper: after the recovery script runs, land one kind specific line
on the handback path (helper preferred; main may call this).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
_SKILL_DEFAULT = _TOOLS.parent


def _resolve_handback(explicit: Path | None) -> Path:
    if explicit is not None:
        return explicit.resolve()
    for base in (
        Path.cwd() / ".cursor" / "skills" / "bobbin",
        _SKILL_DEFAULT,
    ):
        candidate = base / "coach-summary.txt"
        if candidate.parent.is_dir():
            return candidate.resolve()
    return (_SKILL_DEFAULT / "coach-summary.txt").resolve()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Append ENCOURAGEMENT line to coach-summary handback."
    )
    parser.add_argument(
        "--line",
        required=True,
        help="Kind, specific encouragement (one sentence is enough).",
    )
    parser.add_argument(
        "--file",
        type=Path,
        default=None,
        help="Handback path (default: skill coach-summary.txt).",
    )
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Replace an existing ENCOURAGEMENT line instead of appending another.",
    )
    args = parser.parse_args(argv)
    path = _resolve_handback(args.file)
    line = args.line.strip()
    if len(line) < 8:
        print("PROBLEM: encouragement too thin — be specific.")
        return 1

    print(f"HANDBACK: {path.as_posix()}")
    if not path.is_file():
        print("MISSING: coach-summary.txt")
        print("NEXT: write the naming handback before encouraging.")
        return 1

    text = path.read_text(encoding="utf-8")
    new_line = f"ENCOURAGEMENT: {line}"
    if args.replace or "ENCOURAGEMENT:" in text:
        lines = []
        replaced = False
        for ln in text.splitlines():
            if ln.startswith("ENCOURAGEMENT:"):
                if not replaced:
                    lines.append(new_line)
                    replaced = True
                # drop duplicate encouragement lines
                continue
            lines.append(ln)
        if not replaced:
            if lines and lines[-1].strip():
                lines.append("")
            lines.append(new_line)
        path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    else:
        suffix = "" if text.endswith("\n") or not text else "\n"
        path.write_text(text + suffix + new_line + "\n", encoding="utf-8")

    print("WROTE: ENCOURAGEMENT")
    print("OK: post-script encouragement is on the handback.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
