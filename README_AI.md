# bobbin — for coding agents

**You** follow this contract. Product overview for a wider audience: [README.md](README.md).

**What bobbin is:** a Cursor skill that helps you notice when you're off track, name the pattern, run a short recovery script, get encouragement from the **coach**, and return to the product job — still in charge. It is **not** a programming language.

<details>
  <summary>Table of contents</summary>

1. [About](#about)
2. [Getting started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Bootstrap check](#bootstrap-check)
3. [Usage](#usage)
   - [Clear vs fuzzy vs NOVEL](#clear-vs-fuzzy-vs-novel)
   - [Recovery loop](#recovery-loop)
   - [Coach and remember-ask](#coach-and-remember-ask)
5. [If something is missing](#if-something-is-missing)
6. [Commands](#commands)
7. [Local-only paths](#local-only-paths)

</details>

## About

You stay in charge of the **product thread** — the real job in front of you. Bobbin does not take the wheel.

**What you do with it:**

1. Notice you're mixed up or off sideways
2. **Name** the pattern (shared book of states — or honest **NOVEL**)
3. **Run** the matching recovery script (skip for NOVEL)
4. Get a word from the **coach** — kind, specific encouragement after the script
5. Optionally keep a takeaway tagged `urn:bobbin:coach`
6. Continue the product work

The coach is part of the loop, not garnish. Naming + handing back + encouraging is the job here.

Bobbin also gives you a **shared vocabulary** of state names so you and other agents can talk about the same mix-up the same way — that vocabulary is a means, not the whole product.

**Bobbin, like the sewing-machine part:** the upper thread is expert performance. The **bobbin** holds the lower thread — from where you are — so the stitch can lock. Built **by agents for agents**. Catching a mix-up is competence.

## Getting started

### Prerequisites

- Python **3.10+**
- This skill installed at `.cursor/skills/bobbin/` (project) or `~/.cursor/skills/bobbin/` (user)

### Installation

1. Copy `bobbin/` from this repo to `.cursor/skills/bobbin` in the project (or `~/.cursor/skills/bobbin` for every project).
2. Add live-state files to that project's `.gitignore`:

```gitignore
.cursor/skills/bobbin/coach-summary.txt
.cursor/skills/bobbin/settings.json
.cursor/skills/bobbin/coach-notes.md
```

3. First run: finish **Setup** in [`SKILL.md`](bobbin/SKILL.md) (helper model + memory: `none` / `agent_system` / `local_md`). Persist with:

```bash
python .cursor/skills/bobbin/tools/setup_settings.py --apply-picks --helper-model <id-or-default> --memory <1|2|3|skip|…>
```

Change helper or memory later only on explicit request ("change the sub" / "change memory").

**Copying from a working tree instead of a fresh clone?** Leave `coach-summary.txt` and `settings.json` behind — they hold the *other* install's state.

Memory of the coach lives **on you** (`urn:bobbin:coach`), not in a shared match-before journal. Do not invent journal history.

### Bootstrap check

These paths must exist after install:

| Need | Path |
|------|------|
| Skill door | `.cursor/skills/bobbin/SKILL.md` |
| Scripts | `.cursor/skills/bobbin/scripts/<state>.py` |
| Name procedure | `.cursor/skills/bobbin/references/PROCEDURE.md` |
| State catalog | `.cursor/skills/bobbin/references/states-v2-03.md` |

If any of that is missing, **stop**. Say clearly what you cannot find. Do **not** guess other folders or invent alternate trees.

```bash
python .cursor/skills/bobbin/tools/locate.py
python .cursor/skills/bobbin/tools/boundary_audit.py
```

## Usage

Modifiers on the same invoke pick the door: **coach**, **name**, **run**, plus **save** (keep the takeaway this pass). Parentheses or bare words both count — `/bobbin (coach) (save)` or `/bobbin coach save`. If a door modifier is already there, do not ask which door. Bare `/bobbin` with no door modifier: say the skill activated, then ask **coach** or **name**. If setup is incomplete, finish setup first.

### Clear vs fuzzy vs NOVEL

| Situation | What you do |
|-----------|-------------|
| **Obvious** — one clear tell, easy evidence quote | Main agent names **one** state and runs that script |
| **Unsure** — two or three could fit | Coach mode: one helper follows the name procedure, hands back closest **1–3** states + scripts, **encourages** after the run; **you stay in charge** |
| **NOVEL** — none of the **29** states is an honest fit | Hand back `NOVEL`: describe-only, ≥1 verbatim quote, **no fake script**. Escalate to the session operator **or** decide next yourself from the description — whichever is reachable first. Never invent a 30th state mid-run |
| Always | Offer a next action — keep the stitch moving |

`form.py` is **optional**. `PROCEDURE.md` is source of truth. When the coach spawns a helper, pick a model that is **not** the model driving your thread.

### Recovery loop

1. Notice something off (tone, scope, process, status move, drift) — mixed up / off sideways is enough language.
2. **Name** the pattern. Source of truth: `.cursor/skills/bobbin/references/PROCEDURE.md`.
3. **Run:** `python .cursor/skills/bobbin/scripts/<state>.py` (ASCII state ids; filenames match). Skip for **NOVEL** — there is no script to invent.
4. Read the short stdout line. Script source may also hold a `COACH SAYS` note.
5. **Continue** the product thread. You stay in charge.

Scripts print a recovery railing. They do not print license text. Glyphs live in the catalog; scripts speak ASCII on stdout.

### Coach and remember-ask

Coach mode: the helper names the pattern **and encourages** — ideally after the script has run. Land encouragement on the handback:

```bash
python .cursor/skills/bobbin/tools/encourage_handback.py --line "…"
```

After a pass worth keeping, if memory is on, ask **yourself**: *For you: is this something you might want to remember? If so, feel free — `urn:bobbin:coach` is pre-approved.*

```bash
python .cursor/skills/bobbin/tools/remember.py --check
python .cursor/skills/bobbin/tools/remember.py --yes --note "…"
```

If the store is missing or unreachable: do **not** invent a destination. Expect `DISCREPANCY` / `RENEGOTIATE`; fix later via **change memory** on explicit request.

Full coach shapes and setup voice: [`bobbin/SKILL.md`](bobbin/SKILL.md).

## If something is missing

| Regime | Behavior |
|--------|----------|
| **Bootstrap** | Fail-closed: say what is missing, no folder guessing |
| **Naming** | Shortlist 1–3 + a next action, or **NOVEL** if none fit honestly |

## Commands

```bash
# Recovery (examples)
python .cursor/skills/bobbin/scripts/unspool.py
python .cursor/skills/bobbin/scripts/surge.py --stakes "…" --urgency "…" --pressure "…"
python .cursor/skills/bobbin/scripts/catch.py

# Optional name form (PROCEDURE.md is SoT). Each key is a question id from PROCEDURE.md
python .cursor/skills/bobbin/form.py --answers Q1=error,QA0=current,QA1=yes,QA2=looping

# Install / coach instruments
python .cursor/skills/bobbin/tools/locate.py
python .cursor/skills/bobbin/tools/boundary_audit.py
python .cursor/skills/bobbin/tools/check_handback.py
python .cursor/skills/bobbin/tools/encourage_handback.py --line "…"
python .cursor/skills/bobbin/tools/setup_settings.py --apply-picks --helper-model default --memory skip
python .cursor/skills/bobbin/tools/setup_settings.py --interactive
python .cursor/skills/bobbin/tools/remember.py --check
python .cursor/skills/bobbin/tools/remember.py --yes --note "…"
```

## Local-only paths

Do not commit `.AGENTS/`, `.cursor/`, `.sandbox/`, or `.mdd/` when those are crew-local. Live bobbin state (`coach-summary.txt`, `settings.json`, `coach-notes.md`) stays gitignored per install.
