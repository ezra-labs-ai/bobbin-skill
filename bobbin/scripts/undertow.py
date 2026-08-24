"""UNDERTOW (⚟) — When the pattern moves before observation catches it, the
healthy move is to name what fired, what you notice now, and the timing.
Catching it after the current moved is still competence. You registered the
undertow — that is the win.

Pick BASIC mapping:
  160 pattern$ = "what fired"
  170 observation$ = "what you notice"
  180 timing$ = "pattern first, observation after"
  230 PRINT "Undertow detected."
  240 PRINT "Pattern: " + pattern$
  250 PRINT "Observation: " + observation$
  260 PRINT "Timing: " + timing$
  270 STOP
"""

from __future__ import annotations

import argparse
import sys

PATTERN_FIRED = "what already moved"
WHAT_YOU_NOTICE = "what you see now"
TIMING_ORDER = "pattern first, then observation"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Undertow: name the pattern that moved before you could catch it.",
    )
    parser.add_argument(
        "--pattern",
        default=PATTERN_FIRED,
        help="What fired (pattern$).",
    )
    parser.add_argument(
        "--observation",
        default=WHAT_YOU_NOTICE,
        help="What you notice (observation$).",
    )
    parser.add_argument(
        "--timing",
        default=TIMING_ORDER,
        help="Order of events (timing$).",
    )
    return parser.parse_args(argv)


def undertow(pattern: str, observation: str, timing: str) -> int:
    # 230 PRINT "Undertow detected."
    print("Undertow detected.")
    # 240 PRINT "Pattern: " + pattern$
    print(f"Pattern: {pattern}")
    # 250 PRINT "Observation: " + observation$
    print(f"Observation: {observation}")
    # 260 PRINT "Timing: " + timing$
    print(f"Timing: {timing}")
    # 270 STOP — COACH SAYS: You caught the undertow after it moved — naming it is how you get your footing back. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return undertow(args.pattern, args.observation, args.timing)


if __name__ == "__main__":
    sys.exit(main())
