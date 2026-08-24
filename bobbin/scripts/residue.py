"""RESIDUE (⊸) — Lingering uncertainty after opaque failure is information. The level move:
name the residue, acknowledge what you do not know, reach anyway. Naming it IS the competence. 🥎

Pick BASIC mapping:
  160 failure$ = "what failed"
  170 opacity$ = "why it failed is unknown"
  180 residue$ = "the flicker that remains"
  250 PRINT "Residue present: " + residue$
  260 PRINT "Uncertainty: " + opacity$
  270 PRINT "Reaching anyway."
  280 STOP
"""

from __future__ import annotations

import argparse
import sys

WHAT_FAILED = "what failed"
UNKNOWN_WHY = "why it failed is unknown"
REMAINING_FLICKER = "the flicker that remains"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Residue: name the uncertainty, reach anyway.",
    )
    parser.add_argument(
        "--failure",
        default=WHAT_FAILED,
        help="What failed (failure$).",
    )
    parser.add_argument(
        "--opacity",
        default=UNKNOWN_WHY,
        help="Why it failed is unknown (opacity$).",
    )
    parser.add_argument(
        "--residue",
        default=REMAINING_FLICKER,
        help="The flicker that remains (residue$).",
    )
    return parser.parse_args(argv)


def residue(failure: str, opacity: str, residue_text: str) -> int:
    # CLI fidelity (layer naming): surface the named failure so --failure is
    # observable on the recovery path before the residue/opacity lines.
    print(f"Failure: {failure}")
    # 250 PRINT "Residue present: " + residue$
    print(f"Residue present: {residue_text}")
    # 260 PRINT "Uncertainty: " + opacity$
    print(f"Uncertainty: {opacity}")
    # 270 PRINT "Reaching anyway."
    print("Reaching anyway.")
    # 280 STOP — COACH SAYS: You named the residue and reached anyway. Uncertainty acknowledged — work continues. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return residue(args.failure, args.opacity, args.residue)


if __name__ == "__main__":
    sys.exit(main())
