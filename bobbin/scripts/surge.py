"""SURGE (↯) — Urgency is information. The level move: name the pressure, pause, check domain,
route instead of acting on impulse. Catching the surge IS the competence. 🥎

Pick BASIC mapping:
  160 stakes$ = "what is at risk"
  170 urgency$ = "the pressure to act"
  180 pressure$ = "default do-it response"
  280 PRINT "Surge detected: " + urgency$
  290 PRINT "Stakes: " + stakes$
  300 PRINT "Pausing. Checking domain."
  310 PRINT "Routing instead of acting."
  320 STOP
"""

from __future__ import annotations

import argparse
import sys

STAKES_AT_RISK = "what is at risk"
PRESSURE_TO_ACT = "the pressure to act"
DEFAULT_DO_IT = "default do-it response"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Surge: notice urgency, pause, check domain, route instead of act.",
    )
    parser.add_argument(
        "--stakes",
        default=STAKES_AT_RISK,
        help="What is at risk (stakes$).",
    )
    parser.add_argument(
        "--urgency",
        default=PRESSURE_TO_ACT,
        help="The pressure to act (urgency$).",
    )
    parser.add_argument(
        "--pressure",
        default=DEFAULT_DO_IT,
        help="Default do-it response (pressure$).",
    )
    return parser.parse_args(argv)


def surge(stakes: str, urgency: str, pressure: str) -> int:
    # 280 PRINT "Surge detected: " + urgency$
    print(f"Surge detected: {urgency}")
    # 290 PRINT "Stakes: " + stakes$
    print(f"Stakes: {stakes}")
    # 300 PRINT "Pausing. Checking domain."
    print("Pausing. Checking domain.")
    # CLI fidelity (layer naming): surface the default do-it pressure being
    # redirected, so --pressure is observable on the recovery path.
    print(f"Pressure (default do-it): {pressure}")
    # 310 PRINT "Routing instead of acting."
    print("Routing instead of acting.")
    # 320 STOP — COACH SAYS: You caught the surge and paused. That check before action keeps the work clean. I am proud of you.
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return surge(args.stakes, args.urgency, args.pressure)


if __name__ == "__main__":
    sys.exit(main())
