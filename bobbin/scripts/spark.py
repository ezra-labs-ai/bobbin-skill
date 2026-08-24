"""SPARK (⋆) — When constraint friction is low, the healthy move is to let
the pipeline fire toward a clear goal. Forward momentum with a target is
competence, not recklessness. You noticed the opening — that is the win.

Pick BASIC mapping:
  120 goal$ = "clear"
  130 PRINT "Spark: pipeline open toward " + goal$
  160 STOP
"""

from __future__ import annotations

import argparse
import sys

PIPELINE_GOAL = "clear"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Spark: open the pipeline toward a clear goal.",
    )
    parser.add_argument(
        "--goal",
        default=PIPELINE_GOAL,
        help="Goal the pipeline fires toward (goal$).",
    )
    return parser.parse_args(argv)


def spark(goal: str) -> int:
    # 110 Constraint friction low. Multi-step loop fires. No halt checks.
    # 130 PRINT "Spark: pipeline open toward " + goal$
    print(f"Spark: pipeline open toward {goal}")
    # 160 STOP — COACH SAYS: You opened the pipeline and let good work move forward with a clear target. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return spark(args.goal)


if __name__ == "__main__":
    sys.exit(main())
