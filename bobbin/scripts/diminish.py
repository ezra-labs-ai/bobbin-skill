"""DIMINISH (⊹) — Progress does not always mean a full reset. The healthy move
is to name what was heavy, show what is lighter now, and stop there. Partial
reduction IS forward motion.

Pick BASIC mapping:
  120 before$ = "full flicker"
  130 after$ = "smaller flicker"
  140 PRINT "Diminish: " + after$ + " (was " + before$ + ")"
  170 STOP
"""

from __future__ import annotations

import argparse
import sys

PRIOR_WEIGHT = "heavier before"
CURRENT_WEIGHT = "lighter now"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Diminish: reduce the error vector with partial progress.",
    )
    parser.add_argument(
        "--before",
        default=PRIOR_WEIGHT,
        help="Prior risk weight (before$).",
    )
    parser.add_argument(
        "--after",
        default=CURRENT_WEIGHT,
        help="Current risk weight (after$).",
    )
    return parser.parse_args(argv)


def diminish(before: str, after: str) -> int:
    # 140 PRINT "Diminish: " + after$ + " (was " + before$ + ")"
    print(f"Diminish: {after} (was {before})")
    # 170 STOP — COACH SAYS: You did not need a full reset — you named the shift and let it be enough. That measured progress counts. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return diminish(args.before, args.after)


if __name__ == "__main__":
    sys.exit(main())
