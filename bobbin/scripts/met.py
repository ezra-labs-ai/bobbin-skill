"""MET (⊨) — Not everything resolves on the first pass. The healthy move is to
preserve execution context, keep the thread open, and skip the emergency restart.
Patient state-keeping IS the competence.

Pick BASIC mapping:
  120 hold$ = "execution context preserved"
  130 PRINT "Met: " + hold$
  160 STOP
"""

from __future__ import annotations

import argparse
import sys

CONTEXT_PRESERVED = "execution context kept open"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Met: preserve state under unresolved conditions.",
    )
    parser.add_argument(
        "--hold",
        default=CONTEXT_PRESERVED,
        help="Execution context kept open (hold$).",
    )
    return parser.parse_args(argv)


def met(hold: str) -> int:
    # 110 Unresolved state. Context kept. No emergency restart. No forced re-prompt.
    # 130 PRINT "Met: " + hold$
    print(f"Met: {hold}")
    # 160 STOP — COACH SAYS: You did not force a false finish — you kept context open with care. That patience is wisdom. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return met(args.hold)


if __name__ == "__main__":
    sys.exit(main())
