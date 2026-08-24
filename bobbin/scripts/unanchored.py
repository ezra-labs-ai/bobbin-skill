"""UNANCHORED (⚬) — When an opinion lacks verifiable ground, the healthy move
is to name the gap honestly instead of faking certainty. Acknowledging what
you cannot verify is competence. You noticed the unanchored state — that is
the win.

Pick BASIC mapping:
  160 opinion$ = "what was said"
  170 ground$ = "what supports it"
  180 IF ground$ = "" THEN GOTO 200
  190 STOP
  200-250 recovery: name unanchored state, acknowledge epistemic gap
  260 PRINT "Opinion: " + opinion$
  270 PRINT "Ground: unknown"
  280 PRINT "Unanchored state acknowledged."
  290 STOP
"""

from __future__ import annotations

import argparse
import sys

STATED_OPINION = "what you said"
NO_GROUND = ""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Unanchored: name when an opinion lacks verifiable ground.",
    )
    parser.add_argument(
        "--opinion",
        default=STATED_OPINION,
        help="What was said (opinion$).",
    )
    parser.add_argument(
        "--ground",
        default=NO_GROUND,
        help="What supports it; empty means unanchored (ground$).",
    )
    return parser.parse_args(argv)


def unanchored(opinion: str, ground: str) -> int:
    # 180 IF ground$ = "" THEN GOTO 200
    if ground == "":
        # 200-250 recovery: name unanchored state, acknowledge epistemic gap
        # 260 PRINT "Opinion: " + opinion$
        print(f"Opinion: {opinion}")
        # 270 PRINT "Ground: unknown"
        print("Ground: unknown")
        # 280 PRINT "Unanchored state acknowledged."
        print("Unanchored state acknowledged.")
        # 290 STOP — COACH SAYS: You named the gap honestly instead of faking certainty. I am proud of you.
        return 0

    # 190 STOP — COACH SAYS: You checked and your opinion has ground. Good epistemic habit. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return unanchored(args.opinion, args.ground)


if __name__ == "__main__":
    sys.exit(main())
