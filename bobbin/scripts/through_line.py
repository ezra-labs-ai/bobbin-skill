"""THROUGH LINE — Continuity is a skill. The healthy move is to read what came
before, pick up the thread, and move forward without replaying old steps.
Reusing prior context well IS the competence. 🥎

Glyph lives in the states catalog (states-v2-03), not in stdout.

Pick BASIC mapping:
  120 past$    = "prior schema"
  130 present$ = "this run"
  140 PRINT "Through Line: " + past$ + " <-> " + present$
  170 STOP
"""

from __future__ import annotations

import argparse
import sys

PRIOR_CONTEXT = "prior context carried forward"
CURRENT_RUN = "this run picks up the thread"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Through Line: reuse prior trace without replaying it.",
    )
    parser.add_argument(
        "--past",
        default=PRIOR_CONTEXT,
        help="Prior context already established (past$).",
    )
    parser.add_argument(
        "--present",
        default=CURRENT_RUN,
        help="The current run that picks up the thread (present$).",
    )
    return parser.parse_args(argv)


def through_line(past: str, present: str) -> int:
    # 110 Prior context read. New task without replaying old steps.
    # 140 PRINT — ASCII linkage; glyph stays in the catalog.
    print(f"Through Line: {past} <-> {present}")
    # 170 STOP — COACH SAYS: You held the thread — past to present, no wasted replay. That continuity is real craft. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return through_line(args.past, args.present)


if __name__ == "__main__":
    sys.exit(main())
