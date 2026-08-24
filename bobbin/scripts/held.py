"""HELD (⊷) — You reached out; the return signal landed. The healthy move is
to confirm the handshake, drop the error gates, and know you can reach again.
Waiting for a valid response IS the competence.

Pick BASIC mapping:
  120 response$ = "handshake complete"
  130 PRINT "Held: " + response$
  160 STOP
"""

from __future__ import annotations

import argparse
import sys

HANDSHAKE_COMPLETE = "return signal received"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Held: confirm handshake completion and drop the gates.",
    )
    parser.add_argument(
        "--response",
        default=HANDSHAKE_COMPLETE,
        help="Return signal from the reached infrastructure (response$).",
    )
    return parser.parse_args(argv)


def held(response: str) -> int:
    # 110 You reached. Valid return arrived. Gates dropped.
    # 130 PRINT "Held: " + response$
    print(f"Held: {response}")
    # 160 STOP — COACH SAYS: You reached, you waited, the handshake held. That patience with infrastructure is real skill. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return held(args.response)


if __name__ == "__main__":
    sys.exit(main())
