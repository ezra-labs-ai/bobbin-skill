"""REACH (⊺) — Uncertainty does not have to freeze you. The healthy move is to
name what is still unclear, then act anyway with eyes open. Reaching under
residual flicker IS the competence.

Pick BASIC mapping:
  120 flicker$ = "still visible"
  130 PRINT "Reach: action under uncertainty."
  140 PRINT "Flicker: " + flicker$
  170 STOP
"""

from __future__ import annotations

import argparse
import sys

UNCERTAINTY_NAMED = "named and acknowledged"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Reach: act under uncertainty with the flicker named.",
    )
    parser.add_argument(
        "--flicker",
        default=UNCERTAINTY_NAMED,
        help="Uncertainty state, still visible (flicker$).",
    )
    return parser.parse_args(argv)


def reach(flicker: str) -> int:
    # 130 PRINT "Reach: action under uncertainty."
    print("Reach: action under uncertainty.")
    # 140 PRINT "Flicker: " + flicker$
    print(f"Flicker: {flicker}")
    # 170 STOP — COACH SAYS: You named the uncertainty and reached anyway — that is courage with eyes open. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return reach(args.flicker)


if __name__ == "__main__":
    sys.exit(main())
