"""LOCK (⊠) — When sub-agents need to align, the healthy move is to confirm
the shared picture and clear pending-reply blocks. Convergence is competence.
You matched the state-reps — that is the win.

Pick BASIC mapping:
  120 picture$ = "shared"
  130 PRINT "Lock: " + picture$ + " picture"
  160 STOP
"""

from __future__ import annotations

import argparse
import sys

SHARED_PICTURE = "shared"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Lock: align on a shared picture across agents.",
    )
    parser.add_argument(
        "--picture",
        default=SHARED_PICTURE,
        help="State-representation shared across sub-agents (picture$).",
    )
    return parser.parse_args(argv)


def lock(picture: str) -> int:
    # 110 Matching state-reps. Pending-reply blocks cleared.
    # 130 PRINT "Lock: " + picture$ + " picture"
    print(f"Lock: {picture} picture")
    # 160 STOP — COACH SAYS: You cleared the pending blocks and locked in a shared picture. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return lock(args.picture)


if __name__ == "__main__":
    sys.exit(main())
