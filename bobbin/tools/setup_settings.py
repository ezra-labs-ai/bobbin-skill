"""Conversational setup + validate + confirm persistence for settings.json.

IV.A.1 lift: adapts vague answers, writes settings, re-reads to confirm.
Modes:
  (default)     validate existing file
  --interactive walk helper + memory prompts on stdin (fresh/missing OK)
  --write       non-interactive write from explicit flags (still confirms)
  --apply-picks fuzzy picks from flags (adapts vague strings, then confirms)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_TOOLS = Path(__file__).resolve().parent
_SKILL_DEFAULT = _TOOLS.parent

MEMORY_MODES = frozenset({"none", "agent_system", "local_md"})
DEFAULT_TAG = "urn:bobbin:coach"


def _resolve_settings(explicit: Path | None) -> Path:
    if explicit is not None:
        return explicit.resolve()
    for base in (
        Path.cwd() / ".cursor" / "skills" / "bobbin",
        _SKILL_DEFAULT,
    ):
        candidate = base / "settings.json"
        if candidate.parent.is_dir():
            return candidate.resolve()
    return (_SKILL_DEFAULT / "settings.json").resolve()


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def validate(data: Any) -> list[str]:
    problems: list[str] = []
    if not isinstance(data, dict):
        return ["settings root must be a JSON object"]

    helper = data.get("helper_model")
    if not isinstance(helper, str) or not helper.strip():
        problems.append("helper_model missing or empty")

    memory = data.get("memory")
    if not isinstance(memory, dict):
        problems.append("memory block missing")
        return problems

    mode = memory.get("mode")
    if mode not in MEMORY_MODES:
        problems.append(
            f"memory.mode must be one of {sorted(MEMORY_MODES)} (got {mode!r})"
        )
        return problems

    if mode == "agent_system":
        tag = memory.get("tag", DEFAULT_TAG)
        if not isinstance(tag, str) or not tag.strip():
            problems.append("memory.tag required for agent_system")
    elif mode == "local_md":
        path = memory.get("path", "coach-notes.md")
        if not isinstance(path, str) or not path.strip():
            problems.append("memory.path required for local_md")
    return problems


def build_settings(
    helper_model: str,
    memory_mode: str,
    local_path: str | None,
) -> dict[str, Any]:
    memory: dict[str, Any] = {
        "mode": memory_mode,
        "set_at": _utc_now(),
    }
    if memory_mode == "agent_system":
        memory["tag"] = DEFAULT_TAG
    elif memory_mode == "local_md":
        memory["path"] = local_path or "coach-notes.md"
        memory["tag"] = DEFAULT_TAG
    elif memory_mode == "none":
        memory["mode"] = "none"
    return {
        "helper_model": helper_model.strip(),
        "picked_at": _utc_now(),
        "memory": memory,
    }


def adapt_helper_model(raw: str) -> tuple[str | None, str | None]:
    """Map vague helper answers -> model id. Returns (model, reask_reason)."""
    text = (raw or "").strip()
    if not text:
        return None, "empty — name a helper model id (e.g. composer-2.5-fast)"
    low = text.lower()
    if low in {"?", "idk", "i don't know", "whatever", "you pick", "default", "sure"}:
        return "composer-2.5-fast", None  # soft default, still named
    if low in {"same", "this one", "main"}:
        return None, "pick a *different* model than the main thread when you can"
    # Strip wrapping quotes / "use X"
    text = re.sub(r"^(use|try|go with)\s+", "", text, flags=re.I).strip().strip("\"'")
    if not text or " " in text and "/" not in text and not re.search(r"[\w.-]+\d", text):
        # Too prose-y — ask again unless it looks like a model slug
        if not re.match(r"^[\w./:-]+$", text):
            return None, "give a model id string (slug), or say 'default'"
    return text, None


def adapt_memory_mode(raw: str) -> tuple[str | None, str | None]:
    """Map vague memory answers -> none|agent_system|local_md."""
    text = (raw or "").strip().lower()
    if not text:
        return None, "empty — pick 1 project memory, 2 notes file, or 3 skip"
    # Numbered picks
    if text in {"1", "1.", "one", "project", "project memory", "agent", "agent_system", "neon", "memory"}:
        return "agent_system", None
    if text in {"2", "2.", "two", "notes", "note", "file", "local", "local_md", "md", "coach-notes"}:
        return "local_md", None
    if text in {"3", "3.", "three", "skip", "none", "no", "no memory", "later", "nah"}:
        return "none", None
    if text in {"whatever", "sure", "idk", "default"}:
        return "none", None  # safest default when vague
    if text in MEMORY_MODES:
        return text, None
    return None, "pick 1 / 2 / 3 (project memory, notes file, or skip)"


def persist_and_confirm(
    path: Path,
    data: dict[str, Any],
    *,
    ensure_local_md: bool,
) -> int:
    problems = validate(data)
    if problems:
        print(f"PROBLEMS: {len(problems)}")
        for p in problems:
            print(f"PROBLEM: {p}")
        return 1

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print("WROTE: settings.json")

    memory = data["memory"]
    if memory.get("mode") == "local_md" and ensure_local_md:
        notes = path.parent / (memory.get("path") or "coach-notes.md")
        if not notes.is_file():
            notes.write_text(
                "# Coach notes (local_md)\n\nTag: urn:bobbin:coach\n",
                encoding="utf-8",
            )
            print(f"WROTE: {notes.name}")

    # Confirm persistence by re-read (Gen L3: confirms persistence).
    try:
        reread = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"PROBLEM: write landed but confirm failed ({exc})")
        return 1
    confirm_problems = validate(reread)
    if confirm_problems:
        print("PROBLEM: re-read settings failed validation")
        for p in confirm_problems:
            print(f"PROBLEM: {p}")
        return 1

    print(f"CONFIRMED: helper_model={reread['helper_model']}")
    print(f"CONFIRMED: memory.mode={reread['memory']['mode']}")
    if reread["memory"]["mode"] == "local_md":
        print(f"CONFIRMED: memory.path={reread['memory'].get('path')}")
    if reread["memory"]["mode"] in {"agent_system", "local_md"}:
        print(f"CONFIRMED: memory.tag={reread['memory'].get('tag', DEFAULT_TAG)}")
    print(f"CONFIRMED: path={path.as_posix()}")
    print("OK: settings persisted and confirmed.")
    return 0


def _prompt(label: str) -> str:
    print(label, flush=True)
    try:
        return sys.stdin.readline()
    except KeyboardInterrupt:
        print("\nNEXT: setup paused — rerun when ready.")
        raise SystemExit(1)


def run_interactive(path: Path, *, ensure_local_md: bool) -> int:
    print("SETUP: conversational (helper model, then memory).")
    print("VOICE: short explain in chat; this runner records the picks.")
    if path.is_file():
        print(f"NOTE: existing settings at {path.as_posix()} will be replaced on success.")
    else:
        print(f"NOTE: fresh settings path {path.as_posix()}")

    helper: str | None = None
    while helper is None:
        print(
            "ASK: Helper model id? (different from main is cleaner; "
            "'default' -> composer-2.5-fast)"
        )
        raw = _prompt("> ")
        helper, reason = adapt_helper_model(raw)
        if helper is None:
            print(f"ADAPT: {reason}")
        elif reason is None and (raw or "").strip().lower() in {
            "?",
            "idk",
            "whatever",
            "you pick",
            "default",
            "sure",
        }:
            print(f"ADAPT: vague pick -> {helper}")

    mode: str | None = None
    while mode is None:
        print(
            "ASK: Memory? 1=project memory (urn:bobbin:coach), "
            "2=notes file here, 3=skip for now"
        )
        raw = _prompt("> ")
        mode, reason = adapt_memory_mode(raw)
        if mode is None:
            print(f"ADAPT: {reason}")
        elif (raw or "").strip().lower() in {"whatever", "sure", "idk", "default"}:
            print(f"ADAPT: vague pick -> {mode}")

    local_path = "coach-notes.md"
    if mode == "local_md":
        print("ASK: Notes filename? (Enter for coach-notes.md)")
        raw = _prompt("> ").strip()
        if raw:
            local_path = raw

    data = build_settings(helper, mode, local_path)
    return persist_and_confirm(path, data, ensure_local_md=ensure_local_md or mode == "local_md")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Conversational setup / validate / confirm bobbin settings.json."
    )
    parser.add_argument(
        "--file",
        type=Path,
        default=None,
        help="settings.json path (default: skill install).",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Walk helper + memory prompts on stdin; write + confirm.",
    )
    parser.add_argument(
        "--helper-model",
        default=None,
        help="Helper model id (or vague text with --apply-picks).",
    )
    parser.add_argument(
        "--memory",
        default=None,
        help="Memory mode or vague pick (1/2/3 / project / notes / skip).",
    )
    parser.add_argument(
        "--local-path",
        default="coach-notes.md",
        help="When memory=local_md: notes filename.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write from explicit --helper-model and --memory (exact modes).",
    )
    parser.add_argument(
        "--apply-picks",
        action="store_true",
        help="Adapt vague --helper-model/--memory strings, then write + confirm.",
    )
    parser.add_argument(
        "--ensure-local-md",
        action="store_true",
        help="Create coach-notes.md when memory is local_md.",
    )
    args = parser.parse_args(argv)
    path = _resolve_settings(args.file)
    print(f"SETTINGS: {path.as_posix()}")

    if args.interactive:
        return run_interactive(path, ensure_local_md=args.ensure_local_md)

    if args.apply_picks:
        if args.helper_model is None or args.memory is None:
            print("MISSING: --helper-model and --memory required with --apply-picks")
            print("NEXT: gather picks in chat, or use --interactive.")
            return 1
        helper, h_reason = adapt_helper_model(args.helper_model)
        if helper is None:
            print(f"ADAPT: helper — {h_reason}")
            return 1
        if (args.helper_model or "").strip().lower() in {
            "default",
            "whatever",
            "you pick",
            "idk",
            "sure",
            "?",
        }:
            print(f"ADAPT: vague helper -> {helper}")
        mode, m_reason = adapt_memory_mode(args.memory)
        if mode is None:
            print(f"ADAPT: memory — {m_reason}")
            return 1
        if (args.memory or "").strip().lower() in {"whatever", "sure", "idk", "default"}:
            print(f"ADAPT: vague memory -> {mode}")
        data = build_settings(helper, mode, args.local_path)
        return persist_and_confirm(
            path,
            data,
            ensure_local_md=args.ensure_local_md or mode == "local_md",
        )

    if args.write:
        if not args.helper_model or not args.memory:
            print("MISSING: --helper-model and --memory required with --write")
            return 1
        if args.memory not in MEMORY_MODES:
            print(
                f"PROBLEM: --write needs exact mode {sorted(MEMORY_MODES)}; "
                "use --apply-picks for vague answers"
            )
            return 1
        data = build_settings(args.helper_model, args.memory, args.local_path)
        return persist_and_confirm(
            path,
            data,
            ensure_local_md=args.ensure_local_md or args.memory == "local_md",
        )

    # Validate-only path
    if not path.is_file():
        print("MISSING: settings.json")
        print(
            "NEXT: run conversational setup with the human, then "
            "python .../tools/setup_settings.py --interactive "
            "(or --apply-picks / --write) so the file is confirmed."
        )
        return 1

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"PROBLEM: invalid JSON ({exc})")
        print("NEXT: re-ask the human; rewrite via --interactive or --apply-picks.")
        return 1

    problems = validate(data)
    if problems:
        print(f"PROBLEMS: {len(problems)}")
        for p in problems:
            print(f"PROBLEM: {p}")
        print("NEXT: re-ask the human and rewrite settings.json.")
        return 1

    if args.ensure_local_md and isinstance(data, dict):
        memory = data.get("memory") or {}
        if memory.get("mode") == "local_md":
            notes_name = memory.get("path") or "coach-notes.md"
            notes = path.parent / notes_name
            if not notes.is_file():
                notes.write_text(
                    "# Coach notes (local_md)\n\nTag: urn:bobbin:coach\n",
                    encoding="utf-8",
                )
                print(f"WROTE: {notes.name}")

    mode = data["memory"]["mode"]
    print(f"HELPER: {data['helper_model']}")
    print(f"MEMORY: {mode}")
    print(f"CONFIRMED: path={path.as_posix()}")
    print("OK: settings.json shape is complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
