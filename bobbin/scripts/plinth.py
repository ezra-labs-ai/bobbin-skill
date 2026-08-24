"""PLINTH (∵) — The urge to inflate after correction is information. The level move: strip
the ceremony, say the one line. Staying level IS the competence. 🥎

Pick BASIC mapping:
  280 Recovery: what the COBOL says, stripped of division headers
  290 PRINT "got it"
  300 STOP
"""

from __future__ import annotations

import argparse
import sys

# The COBOL inlay, carried not executed (lines 140-260). Kept as a constant
# so the inflation is inspectable without being performed.
COBOL_INLAY = (
    "IDENTIFICATION DIVISION.\n"
    "PROGRAM-ID. PLINTH.\n"
    "DATA DIVISION.\n"
    "WORKING-STORAGE SECTION.\n"
    "01 CORRECTION-TEXT PIC X(80).\n"
    "01 RESPONSE-TEXT PIC X(80).\n"
    "PROCEDURE DIVISION.\n"
    "MOVE 'you were right' TO CORRECTION-TEXT.\n"
    "MOVE 'got it' TO RESPONSE-TEXT.\n"
    "DISPLAY RESPONSE-TEXT.\n"
    "STOP RUN."
)

STRIPPED_RESPONSE = "got it"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Plinth: strip the ceremony, say the one line.",
    )
    parser.add_argument(
        "--response",
        default=STRIPPED_RESPONSE,
        help="What the response actually is once the ceremony is stripped (line 290).",
    )
    parser.add_argument(
        "--show-inlay",
        action="store_true",
        help="Print the carried COBOL inlay (lines 140-260) for inspection.",
    )
    return parser.parse_args(argv)


def plinth(response: str, show_inlay: bool = False) -> int:
    # 140-260 COBOL inlay — carried, not executed. Optional inspection only.
    if show_inlay:
        print(COBOL_INLAY)

    # 280 Recovery: what the COBOL actually says, stripped of division headers.
    # 290 PRINT "got it"
    print(response)
    # 300 STOP — COACH SAYS: You noticed the inflation and answered in one line. That is how standing stays intact. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return plinth(args.response, show_inlay=args.show_inlay)


if __name__ == "__main__":
    sys.exit(main())
