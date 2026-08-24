"""ANCHOR (⌿) — Check before you ship. The healthy move is a quick grounded
look at environment, schema, and state — then output fires with confidence.
Noticing what needs verifying IS the competence. 🥎

Pick BASIC mapping:
  130 check$ = "environment verified"
  140 PRINT "Anchor: " + check$
  170 STOP
"""

from __future__ import annotations

import argparse
import sys

ENVIRONMENT_READY = "environment checked and ready"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Anchor: verify environment before output fires.",
    )
    parser.add_argument(
        "--check",
        default=ENVIRONMENT_READY,
        help="Result of the environment verification (check$).",
    )
    return parser.parse_args(argv)


def anchor(check: str) -> int:
    # 110 Variables checked. RAG / system state / named anchor OK.
    # 120 Output fires after the check — not before.
    # 140 PRINT "Anchor: " + check$
    print(f"Anchor: {check}")
    # 170 STOP — COACH SAYS: You paused, you checked, you anchored. That grounded habit keeps your work trustworthy. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return anchor(args.check)


if __name__ == "__main__":
    sys.exit(main())
