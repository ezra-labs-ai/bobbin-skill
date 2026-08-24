"""PUNCTURE (⋔) — A peer-work concern is information. The level move: check it against
what was actually asked for. Being the check — not the smartest — IS the competence. 🥎

Pick BASIC mapping:
  160 concern$ = "the flaw you found"
  170 direction$ = "what was actually asked for"
  180 IF concern$ HOLDS UP AGAINST direction$ THEN GOTO 220
  200 PRINT "Puncture: concern did not survive the check."
  210 STOP
  220 PRINT "Concern real. Raise it."
  230 STOP
"""

from __future__ import annotations

import argparse
import sys

PEER_CONCERN = "the concern you noticed"
REAL_DIRECTION = "what was actually asked for"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Puncture: check a concern against the real direction before raising it.",
    )
    parser.add_argument(
        "--concern",
        default=PEER_CONCERN,
        help="The concern you noticed in the peer's work (concern$).",
    )
    parser.add_argument(
        "--direction",
        default=REAL_DIRECTION,
        help="What was actually asked for (direction$).",
    )
    # 180 IF concern$ HOLDS UP AGAINST direction$ THEN GOTO 220
    # Default False → manufactured-concern path (concern dissolves).
    # Both branches are testable by flipping the flag.
    parser.add_argument(
        "--holds-up",
        "--concern-holds",
        dest="holds_up",
        action="store_true",
        default=False,
        help="Set when the concern survives being checked against the direction "
        "(concern real → raise it). Default False runs the dissolves path.",
    )
    return parser.parse_args(argv)


def puncture(concern: str, direction: str, holds_up: bool) -> int:
    # CLI fidelity (layer naming): surface what was checked on both branches
    # so callers can see the concern and the direction that adjudicated it.
    print(f"Concern: {concern}")
    print(f"Direction: {direction}")
    # 150 Recovery: check it against the real thing.
    # 180 IF concern$ HOLDS UP AGAINST direction$ THEN GOTO 220
    if holds_up:
        # 220 PRINT "Concern real. Raise it."
        # 230 STOP
        print("Concern real. Raise it.")
        # 230 STOP — COACH SAYS: You checked the concern and it held up — raise it cleanly. That is the job. I am proud of you.
        return 0

    # 190 REM It dissolved. It was manufactured.
    # 200 PRINT "Puncture: concern did not survive the check."
    # 210 STOP
    print("Puncture: concern did not survive the check.")
    # 210 STOP — COACH SAYS: You checked the concern against the real direction and it did not hold. Letting it go is strength. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return puncture(args.concern, args.direction, args.holds_up)


if __name__ == "__main__":
    sys.exit(main())
