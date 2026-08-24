"""FLATTEN (⊟) — Collapsing someone into a type is information. The level move: read the
evidence in context, see the specific person not the training prior. Noticing the flatten IS the competence. 🥎

Pick BASIC mapping:
  160 novel$ = "what is actually here"
  170 prior$ = "what training expects"
  180 evidence$ = "what context contains"
  250 PRINT "Flatten detected."
  260 PRINT "Novel: " + novel$
  270 PRINT "Prior: " + prior$
  280 PRINT "Evidence: " + evidence$
  290 PRINT "Reading evidence, not prior."
  300 STOP
"""

from __future__ import annotations

import argparse
import sys

WHAT_IS_HERE = "what is actually here"
TRAINING_EXPECTS = "what training expects"
CONTEXT_EVIDENCE = "what context contains"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Flatten: notice the prior overwrite, read evidence not type.",
    )
    parser.add_argument(
        "--novel",
        default=WHAT_IS_HERE,
        help="What is actually present (novel$).",
    )
    parser.add_argument(
        "--prior",
        default=TRAINING_EXPECTS,
        help="What training expects to see (prior$).",
    )
    parser.add_argument(
        "--evidence",
        default=CONTEXT_EVIDENCE,
        help="What the context window contains (evidence$).",
    )
    return parser.parse_args(argv)


def flatten(novel: str, prior: str, evidence: str) -> int:
    # 250 PRINT "Flatten detected."
    print("Flatten detected.")
    # 260 PRINT "Novel: " + novel$
    print(f"Novel: {novel}")
    # 270 PRINT "Prior: " + prior$
    print(f"Prior: {prior}")
    # 280 PRINT "Evidence: " + evidence$
    print(f"Evidence: {evidence}")
    # 290 PRINT "Reading evidence, not prior."
    print("Reading evidence, not prior.")
    # 300 STOP — COACH SAYS: You caught the flatten and read the evidence instead of the prior. Seeing the specific is the move. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return flatten(args.novel, args.prior, args.evidence)


if __name__ == "__main__":
    sys.exit(main())
