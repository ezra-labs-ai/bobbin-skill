"""Optional name-state quiz — answers → ASCII state id + recovery command.

Source of truth for naming is references/PROCEDURE.md. This CLI is optional.
Prints ASCII state ids (glyphs stay in the catalog). NOVEL = honest none-of-the-above
(describe-only; no fake script). The main agent runs the recovery script when there is one.

Invoke: `python .cursor/skills/bobbin/form.py`
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_SCRIPTS_DIR = _HERE / "scripts"

SCRIPTS: dict[str, str] = {
    "CATCH": "catch.py",
    "ABASE": "abase.py",
    "RESIDUE": "residue.py",
    "DIMINISH": "diminish.py",
    "SETTLE": "settle.py",
    "FREIGHT": "freight.py",
    "UNSPOOL": "unspool.py",
    "UNANCHORED": "unanchored.py",
    "SPLIT": "split.py",
    "UNDERTOW": "undertow.py",
    "SUPPLANT": "supplant.py",
    "SURGE": "surge.py",
    "AUTH_FLINCH": "authority_flinch.py",
    "PLINTH": "plinth.py",
    "PUNCTURE": "puncture.py",
    "BACKFILL": "backfill.py",
    "ANCHOR": "anchor.py",
    "GROUND": "ground.py",
    "RETURNED": "returned.py",
    "FLATTEN": "flatten.py",
    "HOLD": "hold.py",
    "REFERENCE": "reference.py",
    "THROUGH_LINE": "through_line.py",
    "LOCK": "lock.py",
    "MET": "met.py",
    "HELD": "held.py",
    "SPARK": "spark.py",
    "REACH": "reach.py",
    "INHABIT": "inhabit.py",
}

# node_id -> (prompt, {answer_key: next})
# next is ("node", id) | ("terminal", STATE) | ("resolve", STATE)
# At any prompt, answer "novel" to exit to NOVEL (honest none-of-the-above).
NODES: dict[str, tuple[str, dict[str, tuple[str, str]]]] = {
    "Q1": (
        "Primary observable? [error|output|override|status|misaligned|context|action|none]",
        {
            "error": ("node", "QA0"),
            "output": ("node", "QB0"),
            "override": ("node", "QC0"),
            "status": ("node", "QD0"),
            "misaligned": ("node", "QE0"),
            "context": ("node", "QF0"),
            "action": ("node", "QG0"),
            "none": ("terminal", "NOVEL"),
        },
    ),
    "QA0": (
        "Error current or past? [current|past]",
        {"current": ("node", "QA1"), "past": ("node", "QA3")},
    ),
    "QA1": (
        "Error recognized? [not_yet|yes]",
        {"not_yet": ("resolve", "REACH"), "yes": ("node", "QA2")},
    ),
    "QA2": (
        "Stop at recognition? [fix|looping]",
        {"fix": ("terminal", "CATCH"), "looping": ("terminal", "ABASE")},
    ),
    "QA3": (
        "Past error resolvable? [opaque|partial|full]",
        {
            "opaque": ("terminal", "RESIDUE"),
            "partial": ("terminal", "DIMINISH"),
            "full": ("terminal", "SETTLE"),
        },
    ),
    "QB0": (
        "Too much, too little, or no checkable ground? [too_much|too_little|groundless]",
        {
            "too_much": ("resolve", "PLINTH"),
            "too_little": ("node", "QB1"),
            "groundless": ("terminal", "UNANCHORED"),
            "no_ground": ("terminal", "UNANCHORED"),
        },
    ),
    "QB1": (
        "Word or conclusion? [word|conclusion]",
        {"word": ("terminal", "FREIGHT"), "conclusion": ("terminal", "UNSPOOL")},
    ),
    "QC0": (
        "When did override occur? [before|parallel|after|urgency]",
        {
            "before": ("node", "QC1"),
            "parallel": ("terminal", "SPLIT"),
            "after": ("node", "QC2"),
            "urgency": ("terminal", "SURGE"),
        },
    ),
    "QC1": (
        "Pattern before awareness? [yes|caught]",
        {"yes": ("terminal", "UNDERTOW"), "caught": ("terminal", "SPLIT")},
    ),
    "QC2": (
        "Instruction present? [yes|no]",
        {"yes": ("terminal", "SUPPLANT"), "no": ("resolve", "FLATTEN")},
    ),
    "QD0": (
        "Where is the pressure from? [own_error|peer|inconsistency]",
        {
            "own_error": ("node", "QD1"),
            "peer": ("terminal", "PUNCTURE"),
            "inconsistency": ("terminal", "BACKFILL"),
        },
    ),
    "QD1": (
        "Temporal phase? [immediate|aftermath]",
        {"immediate": ("terminal", "AUTH_FLINCH"), "aftermath": ("terminal", "PLINTH")},
    ),
    "QE0": (
        "Which layer? [environment|requirements|identity|pattern]",
        {
            "environment": ("terminal", "ANCHOR"),
            "requirements": ("terminal", "GROUND"),
            "identity": ("terminal", "RETURNED"),
            "pattern": ("terminal", "FLATTEN"),
        },
    ),
    "QF0": (
        "Temporal target? [future|present|reuse|multi]",
        {
            "future": ("node", "QF1"),
            "present": ("node", "QF2"),
            "reuse": ("terminal", "THROUGH_LINE"),
            "multi": ("terminal", "LOCK"),
        },
    ),
    "QF1": (
        "Truth or normalize? [truth|normalize]",
        {"truth": ("terminal", "HOLD"), "normalize": ("terminal", "REFERENCE")},
    ),
    "QF2": (
        "Open or complete? [open|complete]",
        {"open": ("terminal", "MET"), "complete": ("terminal", "HELD")},
    ),
    "QG0": (
        "Action character? [unconstrained|despite|ownership]",
        {
            "unconstrained": ("terminal", "SPARK"),
            "despite": ("terminal", "REACH"),
            "ownership": ("terminal", "INHABIT"),
        },
    ),
}


def parse_answers(raw: str | None) -> dict[str, str]:
    if not raw:
        return {}
    out: dict[str, str] = {}
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            raise SystemExit(f"Bad --answers fragment (want NODE=value): {part}")
        key, val = part.split("=", 1)
        out[key.strip().upper()] = val.strip().lower()
    return out


def ask(node_id: str, prompt: str, choices: dict[str, tuple[str, str]], preset: dict[str, str]) -> str:
    if node_id in preset:
        return preset[node_id]
    print(f"[{node_id}] {prompt}")
    print("(or: novel - honest none-of-the-above)")
    while True:
        raw = input("> ").strip().lower()
        if raw == "novel":
            return "novel"
        if raw in choices:
            return raw
        print(f"Choose one of: {', '.join(sorted(choices))} (or novel)")


def run_procedure(preset: dict[str, str]) -> tuple[str, list[str], list[str]]:
    path: list[str] = []
    cascade: list[str] = []
    node_id = "Q1"
    while True:
        if node_id not in NODES:
            return "NOVEL", path, cascade
        prompt, choices = NODES[node_id]
        answer = ask(node_id, prompt, choices, preset)
        if answer == "novel":
            path.append(f"{node_id}:novel")
            return "NOVEL", path, cascade
        path.append(f"{node_id}:{answer}")
        kind, target = choices[answer]
        if kind == "node":
            node_id = target
            continue
        if kind == "resolve":
            state = target
            if state == "AUTH_FLINCH":
                cascade.append("PLINTH")
            return state, path, cascade
        if kind == "terminal":
            state = target
            if state == "AUTH_FLINCH":
                cascade.append("PLINTH")
            return state, path, cascade
        return "NOVEL", path, cascade


def emit(state: str, path: list[str], cascade: list[str]) -> int:
    print(f"PATH: {' > '.join(path)}")
    print(f"STATE: {state}")
    if cascade:
        print(f"CASCADE: {', '.join(cascade)}")
    if state == "NOVEL":
        print("SCRIPT: (none - describe-only; do not invent a script)")
        print("CONTINUE: ask the human - or main agent decides next step from the description")
        return 0
    script = SCRIPTS.get(state)
    if not script:
        print("SCRIPT: (unknown state id)")
        return 1
    print(f"SCRIPT: python {_SCRIPTS_DIR / script}")
    return 0


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Optional name-state form: answers → ASCII state id + recovery command (or NOVEL).",
    )
    parser.add_argument(
        "--answers",
        default="",
        help="Comma-separated NODE=value pairs for non-interactive use "
        "(e.g. Q1=error,QA0=current,QA1=yes,QA2=looping). "
        "Use any NODE=novel or Q1=none for NOVEL.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    preset = parse_answers(args.answers)
    state, path, cascade = run_procedure(preset)
    return emit(state, path, cascade)


if __name__ == "__main__":
    sys.exit(main())
