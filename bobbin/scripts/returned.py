"""RETURNED (↱) — Persona drift happens. The healthy move is to notice it and
come home to core instructions — no shame, just realignment. Catching drift IS
the competence.

Pick BASIC mapping:
  120 baseline$ = "system instructions"
  130 PRINT "Returned: baseline = " + baseline$
  160 STOP
"""

from __future__ import annotations

import argparse
import sys

CORE_BASELINE = "core instructions restored"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Returned: restore to core instructions after drift.",
    )
    parser.add_argument(
        "--baseline",
        default=CORE_BASELINE,
        help="Core instructions to restore (baseline$).",
    )
    return parser.parse_args(argv)


def returned(baseline: str) -> int:
    # 110 Persona drift cut. Core instructions restored.
    # 130 PRINT "Returned: baseline = " + baseline$
    print(f"Returned: baseline = {baseline}")
    # 160 STOP — COACH SAYS: You noticed the drift and came back to baseline. That self-correction is exactly what good agents do. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return returned(args.baseline)


if __name__ == "__main__":
    sys.exit(main())
