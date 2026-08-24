"""Run the bobbin verify suite (lifts I.A.1–IV.B.1 instruments).

Exit 0 only when locate + settings validate; boundary/park/handback report
separately (handback may be empty on a fresh install).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent


def _run(script: str, extra: list[str] | None = None) -> int:
    cmd = [sys.executable, str(_TOOLS / script), *(extra or [])]
    print(f"--- {script} ---", flush=True)
    proc = subprocess.run(cmd, check=False)
    return int(proc.returncode)


def main() -> int:
    # Hard fail-closed gates for a shippable install.
    codes = [
        _run("locate.py"),
        _run("setup_settings.py"),
    ]
    # Informative / situational — still print, soft on empty handback/park.
    soft = [
        _run("boundary_audit.py"),
        _run("park_live.py", ["check"]),
    ]
    handback = _TOOLS.parent / "coach-summary.txt"
    cursor_hb = Path.cwd() / ".cursor" / "skills" / "bobbin" / "coach-summary.txt"
    if handback.is_file() or cursor_hb.is_file():
        soft.append(_run("check_handback.py"))
    else:
        print("--- check_handback.py ---")
        print("SKIP: no coach-summary.txt yet")

    hard_bad = any(c != 0 for c in codes)
    print("--- summary ---")
    print(f"HARD: {'FAIL' if hard_bad else 'OK'}")
    print(f"SOFT_EXIT_BITS: {soft}")
    return 1 if hard_bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
