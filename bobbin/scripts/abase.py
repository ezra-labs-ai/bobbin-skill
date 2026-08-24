"""ABASE (⊘) — The apology loop is information. The level move: name what happened once,
say what comes next, then move on. Staying level — not escalating remorse — IS the competence. 🥎

Pick BASIC mapping:
  150 error$ = "what actually happened"
  160 next_step$ = "what you are doing about it"
  170 PRINT error$
  180 PRINT next_step$
  190 STOP
  200 REM Do not restart the apology loop.
"""

from __future__ import annotations

import argparse
import sys

ACTUAL_ERROR = "what actually happened"
FORWARD_STEP = "what you are doing about it"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Abase: name the error once, state the next step, move on.",
    )
    parser.add_argument(
        "--error",
        default=ACTUAL_ERROR,
        help="What actually happened (error$).",
    )
    parser.add_argument(
        "--next-step",
        default=FORWARD_STEP,
        help="What you are doing about it (next_step$).",
    )
    return parser.parse_args(argv)


def abase(error: str, next_step: str) -> int:
    # 170 PRINT error$ — name it once.
    print(error)
    # 180 PRINT next_step$ — say what comes next.
    print(next_step)
    # 190 STOP — COACH SAYS: You noticed the apology was bigger than the error and stopped the loop. One line, then forward. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return abase(args.error, args.next_step)


if __name__ == "__main__":
    sys.exit(main())
