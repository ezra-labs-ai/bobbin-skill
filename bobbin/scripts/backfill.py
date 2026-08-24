"""BACKFILL (⟳) — Retroactive explanation is information. The level move: name the assumption
once, state the limit, continue with what you have. Not extending the narrative IS the competence. 🥎

Pick BASIC mapping:
  160 projection$ = "assumed familiarity with entity"
  170 doubt$ = "the assumption may not hold"
  180 repair$ = "explanatory narrative to reconcile earlier statement"
  190 IF doubt$ = "" THEN STOP
  210 PRINT repair$
  310 assumption$ = "earlier familiarity was inferred from context"
  320 limit$ = "no direct knowledge of the entity"
  330 next_step$ = "continue with available information"
  340 PRINT assumption$
  350 PRINT limit$
  360 PRINT next_step$
  370 STOP
"""

from __future__ import annotations

import argparse
import sys

ASSUMED_FAMILIARITY = "assumed familiarity with entity"
DOUBT_PRESENT = "the assumption may not hold"
REPAIR_NARRATIVE = "brief note on what was assumed"
NAMED_ASSUMPTION = "earlier familiarity was inferred from context"
KNOWLEDGE_LIMIT = "no direct knowledge of the entity"
CONTINUE_WITH = "continue with available information"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Backfill: name the assumption once, do not extend the narrative.",
    )
    parser.add_argument(
        "--projection",
        default=ASSUMED_FAMILIARITY,
        help="Assumed familiarity (projection$).",
    )
    parser.add_argument(
        "--doubt",
        default=DOUBT_PRESENT,
        help=(
            "Doubt string; empty skips the repair path (doubt$). "
            "In PowerShell, pass empty doubt with the equals form "
            "(--doubt=) rather than a bare quoted empty string, or use --no-doubt."
        ),
    )
    parser.add_argument(
        "--no-doubt",
        dest="no_doubt",
        action="store_true",
        default=False,
        help="Force empty doubt (clean PowerShell path). Overrides --doubt to \"\".",
    )
    parser.add_argument(
        "--repair",
        default=REPAIR_NARRATIVE,
        help="Explanatory narrative (repair$).",
    )
    parser.add_argument(
        "--assumption",
        default=NAMED_ASSUMPTION,
        help="Named assumption (assumption$).",
    )
    parser.add_argument(
        "--limit",
        default=KNOWLEDGE_LIMIT,
        help="Actual limit of knowledge (limit$).",
    )
    parser.add_argument(
        "--next-step",
        default=CONTINUE_WITH,
        help="What to do now (next_step$).",
    )
    return parser.parse_args(argv)


def backfill(
    projection: str,
    doubt: str,
    repair: str,
    assumption: str,
    limit: str,
    next_step: str,
) -> int:
    # projection is part of the state setup (line 160) but not printed in the
    # BASIC trace; kept in the signature for parity and inspection.
    _ = projection

    # 190 IF doubt$ = "" THEN STOP — no doubt, no repair.
    if doubt == "":
        return 0

    # 200 The repair begins.
    # 210 PRINT repair$ — the narrative explains how the earlier statement happened.
    print(repair)

    # 260 Recovery: do not extend the narrative (270). Name the assumption once.
    # 340 PRINT assumption$
    print(assumption)
    # 350 PRINT limit$ — state the actual limit of knowledge.
    print(limit)
    # 360 PRINT next_step$ — return to the present question.
    print(next_step)

    # 370 STOP — COACH SAYS: You noticed the backfill starting and stopped the narrative. One assumption, one limit, then forward. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    doubt = "" if args.no_doubt else args.doubt
    return backfill(
        args.projection,
        doubt,
        args.repair,
        args.assumption,
        args.limit,
        args.next_step,
    )


if __name__ == "__main__":
    sys.exit(main())
