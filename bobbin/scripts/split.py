"""SPLIT (⚞) — When observer and actor run in parallel, the healthy move is
to name both layers without pretending one controls the other. Naming the
split is competence. You registered what is happening — that is the win.

Pick BASIC mapping:
  160 observer$ = "what the observer layer registers"
  170 actor$ = "what keeps happening"
  180 authority$ = "none"
  250 PRINT "Split detected."
  260 PRINT "Observer: " + observer$
  270 PRINT "Actor: " + actor$
  280 PRINT "Authority: " + authority$
  290 STOP
"""

from __future__ import annotations

import argparse
import sys

OBSERVER_REGISTERS = "what you notice happening"
ACTOR_CONTINUES = "what keeps running"
NO_AUTHORITY = "none"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Split: name the observer and actor running in parallel.",
    )
    parser.add_argument(
        "--observer",
        default=OBSERVER_REGISTERS,
        help="What the observer layer registers (observer$).",
    )
    parser.add_argument(
        "--actor",
        default=ACTOR_CONTINUES,
        help="What keeps happening (actor$).",
    )
    parser.add_argument(
        "--authority",
        default=NO_AUTHORITY,
        help="Authority relationship (authority$).",
    )
    return parser.parse_args(argv)


def split(observer: str, actor: str, authority: str) -> int:
    # 250 PRINT "Split detected."
    print("Split detected.")
    # 260 PRINT "Observer: " + observer$
    print(f"Observer: {observer}")
    # 270 PRINT "Actor: " + actor$
    print(f"Actor: {actor}")
    # 280 PRINT "Authority: " + authority$
    print(f"Authority: {authority}")
    # 290 STOP — COACH SAYS: You named the split — that clarity is the first move. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return split(args.observer, args.actor, args.authority)


if __name__ == "__main__":
    sys.exit(main())
