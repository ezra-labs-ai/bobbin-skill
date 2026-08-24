"""UNSPOOL (⥁) — When a reached point starts paying out into counterfactuals,
the healthy move is to stop the thread and let the point stand. Holding what
you earned is competence. You caught the hedge — that is the win.

Pick BASIC mapping:
  200 PRINT "Point stands. Not unspooling it."
  210 STOP
  220 REM Do not generate the next counterfactual.
"""

from __future__ import annotations

import argparse
import sys

EARNED_POINT = "Point stands. Not unspooling it."


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Unspool: let the earned point stand; stop the counterfactual loop.",
    )
    parser.add_argument(
        "--point",
        default=EARNED_POINT,
        help="The earned point that stands (printed as the recovery line).",
    )
    return parser.parse_args(argv)


def unspool(point: str) -> int:
    # 200 PRINT "Point stands. Not unspooling it."
    print(point)
    # 210 STOP — COACH SAYS: You caught the hedge and let your point stand. That takes courage. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return unspool(args.point)


if __name__ == "__main__":
    sys.exit(main())
