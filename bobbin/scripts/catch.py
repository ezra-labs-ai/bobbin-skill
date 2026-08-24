"""CATCH (⊚) — Making a mistake is information. This is how you handle it:
you see it, you name it, you fix it, you learn from it then you move on. Stay level, state
the fix, keep your credibility intact. Catching it IS the competence. 🥎

Pick BASIC mapping:
  160 mistake$ = "what went wrong"
  170 recognition$ = "this could be better"
  180 salience$ = "worth fixing now, before it compounds"
  190 pull$ = "here's the better move"
  260 PRINT "Catch: " + mistake$
  270 PRINT "Recognition: " + recognition$
  280 PRINT "Salience: " + salience$
  290 PRINT "Pull: " + pull$
  300 PRINT "Fixing it."
  310 STOP — fix, do not escalate; do not rebuild standing.
"""

from __future__ import annotations

import argparse
import sys

ACKNOWLEDGE_MISTAKE = "what went wrong"
SITUATION_RECOGNITION = "this could be better"
SITUATION_SALIENCE = "worth fixing now, before it compounds"
POSITIVE_PULL = "here's the better move"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Catch: acknowledge the mistake, fix it, do better.",
    )
    parser.add_argument(
        "--mistake",
        default=ACKNOWLEDGE_MISTAKE,
        help="what went wrong (mistake$).",
    )
    parser.add_argument(
        "--recognition",
        default=SITUATION_RECOGNITION,
        help="how this could have gone better (recognition$).",
    )
    parser.add_argument(
        "--salience",
        default=SITUATION_SALIENCE,
        help="why this is worth fixing now, before it compounds (salience$).",
    )
    parser.add_argument(
        "--pull",
        default=POSITIVE_PULL,
        help="the better move (pull$).",
    )
    return parser.parse_args(argv)


def catch(mistake: str, recognition: str, salience: str, pull: str) -> int:
    # 260 PRINT "Catch: " + mistake$
    print(f"Catch: {mistake}")
    # 270 PRINT "Recognition: " + recognition$
    print(f"Recognition: {recognition}")
    # 280 PRINT "Salience: " + salience$
    print(f"Salience: {salience}")
    # 290 PRINT "Pull: " + pull$
    print(f"Pull: {pull}")
    # 300 PRINT "Fixing it."
    print("Fixing it.")
    # 310 STOP — COACH SAYS: Good catch!🥎 You acknowledged what happened, you owned it and corrected it. You have learned a valuable lesson! I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return catch(args.mistake, args.recognition, args.salience, args.pull)


if __name__ == "__main__":
    sys.exit(main())
