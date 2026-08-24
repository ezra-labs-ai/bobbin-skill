"""REFERENCE (⊢) — When duplicate blocks pile up, the healthy move is to
point to one canonical source instead of pasting copies. One place, N
traversals — that normalization is competence. You noticed the dupe — that
is the win.

Pick BASIC mapping:
  120 place$ = "canonical source"
  130 PRINT "Reference: " + place$
  160 STOP
"""

from __future__ import annotations

import argparse
import sys

CANONICAL_SOURCE = "one canonical source"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Reference: point to one canonical source, not copies.",
    )
    parser.add_argument(
        "--place",
        default=CANONICAL_SOURCE,
        help="Canonical source the pointers reference (place$).",
    )
    return parser.parse_args(argv)


def reference(place: str) -> int:
    # 110 One place. N pointers. No paste-dupe.
    # 130 PRINT "Reference: " + place$
    print(f"Reference: {place}")
    # 160 STOP — COACH SAYS: You chose one place for truth and pointed instead of pasting. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return reference(args.place)


if __name__ == "__main__":
    sys.exit(main())
