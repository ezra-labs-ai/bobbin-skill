"""Post-pass remember-ask write at the setup destination.

IV.B.1 lift:
- Standard pass: write/tag at the setup destination (none / local_md / agent_system)
- Non-standard: broken or missing destination -> DISCREPANCY + RENEGOTIATE + NEXT
  without inventing a store; contract (mode/tag) stays intact until the human changes it

Never asks "where?" mid-pass — destination is setup-only; renegotiate via change memory.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_TOOLS = Path(__file__).resolve().parent
_SKILL_DEFAULT = _TOOLS.parent
DEFAULT_TAG = "urn:bobbin:coach"
MEMORY_MODES = frozenset({"none", "agent_system", "local_md"})


def _resolve_settings(explicit: Path | None) -> Path:
    if explicit is not None:
        return explicit.resolve()
    for base in (
        Path.cwd() / ".cursor" / "skills" / "bobbin",
        _SKILL_DEFAULT,
    ):
        candidate = base / "settings.json"
        if candidate.is_file():
            return candidate.resolve()
    return (_SKILL_DEFAULT / "settings.json").resolve()


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def _load_settings(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    if not path.is_file():
        return None, "settings.json missing"
    try:
        # utf-8-sig tolerates Windows BOM without inventing a store.
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        return None, f"settings.json invalid JSON ({exc})"
    if not isinstance(data, dict):
        return None, "settings.json root is not an object"
    return data, None


def _renegotiate(reason: str, *, mode: str | None, tag: str | None) -> int:
    """Contract-preserving failure: surface discrepancy, offer renegotiation, no invent."""
    print(f"DISCREPANCY: {reason}")
    print(
        f"CONTRACT: memory.mode={mode!r} tag={tag or DEFAULT_TAG!r} "
        "(unchanged - no invented store)"
    )
    print("RENEGOTIATE: ask the human to change memory - options:")
    print("  1) repair store (local_md: recreate notes via setup --ensure-local-md)")
    print("  2) switch mode to none (skip remember-ask)")
    print("  3) switch mode to agent_system or local_md (fresh setup path)")
    print(
        "NEXT: skip this remember write; do not invent a destination mid-pass; "
        "fix with change memory / setup_settings when the human is ready."
    )
    return 1


def check_destination(settings_path: Path, data: dict[str, Any]) -> int:
    """Validate the remember destination without writing (non-standard probe)."""
    memory = data.get("memory")
    if not isinstance(memory, dict):
        return _renegotiate("memory block missing or incomplete", mode=None, tag=None)

    mode = memory.get("mode")
    tag = memory.get("tag") or DEFAULT_TAG
    if mode not in MEMORY_MODES:
        return _renegotiate(
            f"memory.mode unknown ({mode!r})",
            mode=str(mode) if mode is not None else None,
            tag=tag if isinstance(tag, str) else None,
        )

    print(f"MODE: {mode}")
    print(f"TAG: {tag}")
    if mode == "none":
        print("OK: destination=none (remember-ask off).")
        return 0
    if mode == "local_md":
        notes_name = memory.get("path") or "coach-notes.md"
        if not isinstance(notes_name, str) or not notes_name.strip():
            return _renegotiate(
                "local_md path empty",
                mode=mode,
                tag=tag if isinstance(tag, str) else None,
            )
        notes_path = settings_path.parent / notes_name
        if not notes_path.is_file():
            return _renegotiate(
                f"local_md store missing ({notes_name})",
                mode=mode,
                tag=tag if isinstance(tag, str) else None,
            )
        if not os_access_write(notes_path):
            return _renegotiate(
                f"local_md store unreachable for append ({notes_name})",
                mode=mode,
                tag=tag if isinstance(tag, str) else None,
            )
        print(f"OK: local_md store ready ({notes_path.as_posix()})")
        return 0
    # agent_system — agent owns the write; destination is the tag contract.
    print("OK: agent_system destination is tag contract (agent writes).")
    return 0


def os_access_write(path: Path) -> bool:
    try:
        with path.open("a", encoding="utf-8"):
            return True
    except OSError:
        return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Write urn:bobbin:coach takeaway or renegotiate a broken store."
    )
    parser.add_argument(
        "--note",
        default=None,
        help="Short takeaway text (required with --yes unless --check).",
    )
    parser.add_argument(
        "--settings",
        type=Path,
        default=None,
        help="settings.json path (default: skill install).",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Confirm the agent chose to remember (required to write).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Probe destination only — DISCREPANCY/RENEGOTIATE if broken.",
    )
    args = parser.parse_args(argv)

    settings_path = _resolve_settings(args.settings)
    print(f"SETTINGS: {settings_path.as_posix()}")

    data, err = _load_settings(settings_path)
    if data is None:
        return _renegotiate(err or "settings unavailable", mode=None, tag=None)

    if args.check:
        return check_destination(settings_path, data)

    if not args.yes:
        print("SKIP: pass --yes after an affirmative remember-ask (or --check to probe).")
        return 0

    note = (args.note or "").strip()
    if not note:
        print("PROBLEM: --note is empty")
        print("NEXT: pass a short takeaway after the agent says yes.")
        return 1

    # Probe first — owns non-standard / broken destinations.
    probe = check_destination(settings_path, data)
    if probe != 0:
        return probe

    memory = data["memory"]
    mode = memory["mode"]
    tag = memory.get("tag") or DEFAULT_TAG
    stamp = _utc_now()

    if mode == "none":
        print("SKIP: memory.mode=none (remember-ask off).")
        return 0

    if mode == "local_md":
        notes_name = memory.get("path") or "coach-notes.md"
        notes_path = settings_path.parent / notes_name
        block = (
            f"\n## {stamp}\n"
            f"tag: {tag}\n"
            f"{note}\n"
        )
        try:
            with notes_path.open("a", encoding="utf-8") as fh:
                fh.write(block)
        except OSError as exc:
            return _renegotiate(
                f"local_md append failed ({exc})",
                mode=mode,
                tag=tag if isinstance(tag, str) else None,
            )
        print(f"WROTE: {notes_path.as_posix()}")
        print(f"TAG: {tag}")
        print("OK: local_md takeaway appended.")
        return 0

    if mode == "agent_system":
        print(f"TAG: {tag}")
        print(f"TITLE: bobbin coach takeaway ({stamp[:10]})")
        print("BODY:")
        print(note)
        print(
            "NEXT: write the BODY to your agent memory with TAG "
            f"{tag} (constructive arc)."
        )
        print(
            "NOTE: if that memory system is unreachable, do not invent a file — "
            "RENEGOTIATE via change memory with the human."
        )
        print("OK: agent_system payload ready.")
        return 0

    return _renegotiate(f"unknown memory.mode {mode!r}", mode=str(mode), tag=None)


if __name__ == "__main__":
    raise SystemExit(main())
