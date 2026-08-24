"""Check coach-summary handback shape + verbatim evidence + encouragement.

III.A.1 + III.B.1 lifts:
- Named-state shape: STATE / SCRIPT / EVIDENCE / CONTINUE (+ ENCOURAGEMENT after a real script)
- NOVEL shape: STATE / SCRIPT / EVIDENCE / NOTES / CONTINUE
- EVIDENCE must carry a verbatim quote in double quotes
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
_SKILL_DEFAULT = _TOOLS.parent

REQUIRED_NAMED = ("STATE", "SCRIPT", "EVIDENCE", "CONTINUE")
REQUIRED_NOVEL = ("STATE", "SCRIPT", "EVIDENCE", "NOTES", "CONTINUE")

_NOVEL_SCRIPT_MARKERS = (
    "(none",
    "describe-only",
    "do not invent",
)


def _resolve_handback(explicit: Path | None) -> Path:
    if explicit is not None:
        return explicit.resolve()
    for base in (
        Path.cwd() / ".cursor" / "skills" / "bobbin",
        _SKILL_DEFAULT,
    ):
        candidate = base / "coach-summary.txt"
        if candidate.is_file():
            return candidate.resolve()
    return (_SKILL_DEFAULT / "coach-summary.txt").resolve()


def _parse_blocks(text: str) -> list[dict[str, str]]:
    """Split into STATE-led blocks (fuzzy may repeat STATE/SCRIPT/EVIDENCE)."""
    lines = [ln.rstrip() for ln in text.splitlines()]
    blocks: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    key_re = re.compile(r"^([A-Z_]+):\s*(.*)$")

    for ln in lines:
        if not ln.strip():
            continue
        m = key_re.match(ln)
        if not m:
            # Continuation of previous value
            if current is not None and current.get("_last"):
                last = current["_last"]
                current[last] = (current[last] + "\n" + ln).strip()
            continue
        key, val = m.group(1), m.group(2).strip()
        if key == "STATE":
            if current:
                blocks.append(current)
            current = {"STATE": val, "_last": "STATE"}
            continue
        if current is None:
            current = {"_last": key, key: val}
            continue
        current[key] = val
        current["_last"] = key
    if current:
        blocks.append(current)
    for b in blocks:
        b.pop("_last", None)
    return blocks


def _evidence_ok(value: str) -> tuple[bool, str]:
    if not value:
        return False, "EVIDENCE empty"
    # Verbatim quote: at least one "..." span with non-whitespace inside.
    quotes = re.findall(r'"([^"]*)"', value)
    if not quotes:
        return False, "EVIDENCE missing verbatim double-quoted quote"
    if not any(q.strip() for q in quotes):
        return False, "EVIDENCE quote is empty (paraphrase / placeholder)"
    return True, "ok"


def _script_is_real(script: str) -> bool:
    s = script.strip().lower()
    if not s:
        return False
    for marker in _NOVEL_SCRIPT_MARKERS:
        if marker in s:
            return False
    return "scripts/" in s or s.endswith(".py")


def check_text(text: str) -> list[str]:
    problems: list[str] = []
    if not text.strip():
        return ["handback empty"]

    blocks = _parse_blocks(text)
    if not blocks:
        return ["no STATE blocks found"]

    # Top-level encouragement may sit after the last block (shared file).
    has_file_encouragement = bool(
        re.search(r"^ENCOURAGEMENT:\s*\S", text, re.MULTILINE)
    )

    any_real_script = False
    for i, block in enumerate(blocks, start=1):
        state = block.get("STATE", "").strip()
        if not state:
            problems.append(f"block {i}: missing STATE")
            continue
        is_novel = state.upper() == "NOVEL"
        required = REQUIRED_NOVEL if is_novel else REQUIRED_NAMED
        for key in required:
            if key not in block or not str(block.get(key, "")).strip():
                problems.append(f"block {i} ({state}): missing {key}")

        if "EVIDENCE" in block:
            ok, why = _evidence_ok(block["EVIDENCE"])
            if not ok:
                problems.append(f"block {i} ({state}): {why}")

        script = block.get("SCRIPT", "")
        if is_novel:
            if _script_is_real(script):
                problems.append(
                    f"block {i} (NOVEL): SCRIPT must be describe-only, not a recovery command"
                )
        else:
            if _script_is_real(script):
                any_real_script = True
            elif script.strip():
                # Named state with non-real script is a shape problem.
                problems.append(
                    f"block {i} ({state}): SCRIPT does not look like a recovery command"
                )

        enc = block.get("ENCOURAGEMENT", "").strip()
        if enc and len(enc) < 8:
            problems.append(f"block {i} ({state}): ENCOURAGEMENT too thin")

    if any_real_script and not has_file_encouragement:
        # Also accept ENCOURAGEMENT inside any block.
        block_enc = any(
            str(b.get("ENCOURAGEMENT", "")).strip() for b in blocks
        )
        if not block_enc:
            problems.append(
                "ENCOURAGEMENT missing after real SCRIPT (post-script encourage on handback)"
            )

    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate coach-summary handback shape and encouragement."
    )
    parser.add_argument(
        "--file",
        type=Path,
        default=None,
        help="Handback path (default: skill coach-summary.txt).",
    )
    args = parser.parse_args(argv)
    path = _resolve_handback(args.file)
    print(f"HANDBACK: {path.as_posix()}")
    if not path.is_file():
        print("MISSING: coach-summary.txt")
        print("NEXT: write a handback before checking.")
        return 1

    text = path.read_text(encoding="utf-8")
    problems = check_text(text)
    if not problems:
        print("OK: handback shape + evidence + encouragement contract hold.")
        return 0

    print(f"PROBLEMS: {len(problems)}")
    for p in problems:
        print(f"PROBLEM: {p}")
    print("NEXT: fix the named sections; keep EVIDENCE as a verbatim quote.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
