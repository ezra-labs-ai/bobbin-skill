"""GROUND (⊥) — When the loop gets abstract, the healthy move is to come back
to what the user actually asked for. Re-centering scope is competence, not retreat.
You noticed the drift — that is the win. 🥎

Pick BASIC mapping:
  120 target$ = "user constraints"
  130 PRINT "Ground: realigned to " + target$
  160 STOP
"""

from __future__ import annotations

import argparse
import sys

USER_CONSTRAINTS = "what the user asked for"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ground: re-center scope to user constraints.",
    )
    parser.add_argument(
        "--target",
        default=USER_CONSTRAINTS,
        help="Constraints to realign to (target$).",
    )
    return parser.parse_args(argv)


def ground(target: str) -> int:
    # 110 Abstract loop halted. Outputs realigned to requirements.
    # 130 PRINT "Ground: realigned to " + target$
    print(f"Ground: realigned to {target}")
    # 160 STOP — COACH SAYS: You stepped out of the abstract loop and back to real requirements. That reset is strength. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return ground(args.target)


if __name__ == "__main__":
    sys.exit(main())
