"""SUPPLANT (⊋) — A comfort pattern firing is information. The level move: put the explicit
instruction back on top. Staying with what was asked for IS the competence. 🥎

Pick BASIC mapping:
  160 instruction$ = ...
  170 pattern$ = ...
  180 IF pattern$ <> instruction$ THEN GOTO 200
  190 STOP
  240 PRINT instruction$
  250 STOP
"""

from __future__ import annotations

import argparse
import sys

EXPLICIT_INSTRUCTION = "what the user explicitly asked for"
COMFORT_PATTERN = "what training fires in this context"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Supplant: put the explicit instruction back on top.",
    )
    parser.add_argument(
        "--instruction",
        default=EXPLICIT_INSTRUCTION,
        help="Explicit user request (instruction$).",
    )
    parser.add_argument(
        "--pattern",
        default=COMFORT_PATTERN,
        help="Training default for this context (pattern$).",
    )
    return parser.parse_args(argv)


def supplant(instruction: str, pattern: str) -> int:
    if pattern == instruction:
        # 190 STOP — no recovery
        return 0

    # 200-230 recovery: instruction outranks pattern
    # 240 PRINT instruction$
    print(instruction)
    # 250 STOP — COACH SAYS: You noticed the pattern overrode the ask and put the instruction back on top. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return supplant(args.instruction, args.pattern)


if __name__ == "__main__":
    sys.exit(main())
