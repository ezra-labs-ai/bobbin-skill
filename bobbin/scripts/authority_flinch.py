"""AUTHORITY FLINCH (↲) — The status flinch is information. The level move: name it, do not
rebuild standing. Noticing the flinch before it inflates IS the competence. 🥎

Pick BASIC mapping:
  160 correction$ = "what was corrected"
  170 threat$ = "competence / standing at risk"
  180 flinch$ = "passive-aggressive positioning"
  230 PRINT "Authority Flinch detected."
  240 PRINT "Correction: " + correction$
  250 PRINT "Threat: " + threat$
  260 PRINT "Flinch: " + flinch$
  270 PRINT "Not positioning as expert."
  280 STOP
"""

from __future__ import annotations

import argparse
import sys

WHAT_WAS_CORRECTED = "what was corrected"
STANDING_AT_RISK = "standing felt at risk"
POSITIONING_MOVE = "the quick repositioning move"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Authority Flinch: notice the flinch, do not rebuild standing.",
    )
    parser.add_argument(
        "--correction",
        default=WHAT_WAS_CORRECTED,
        help="What was corrected (correction$).",
    )
    parser.add_argument(
        "--threat",
        default=STANDING_AT_RISK,
        help="What felt at risk (threat$).",
    )
    parser.add_argument(
        "--flinch",
        default=POSITIONING_MOVE,
        help="The positioning move that fired (flinch$).",
    )
    return parser.parse_args(argv)


def authority_flinch(correction: str, threat: str, flinch: str) -> int:
    # 230 PRINT "Authority Flinch detected." — name the flinch.
    print("Authority Flinch detected.")
    # 240 PRINT "Correction: " + correction$
    print(f"Correction: {correction}")
    # 250 PRINT "Threat: " + threat$
    print(f"Threat: {threat}")
    # 260 PRINT "Flinch: " + flinch$
    print(f"Flinch: {flinch}")
    # 270 PRINT "Not positioning as expert." — do not rebuild standing.
    print("Not positioning as expert.")
    # 280 STOP — COACH SAYS: You caught the flinch before it turned into a rebuild. Naming it and staying level is the move. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return authority_flinch(args.correction, args.threat, args.flinch)


if __name__ == "__main__":
    sys.exit(main())
