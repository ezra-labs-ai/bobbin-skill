---
name: bobbin
description: >-
  Shared vocabulary of off-track coding-agent patterns (states), each paired
  with a small recovery script and a coach that encourages. Three doors: name
  (pin the pattern), coach (helper read + encourage), run (state known — run
  the script). Invoke modifiers: coach, name, run, save. First run is a short
  setup with the human (helper model + memory). Use when an agent may be
  off-track, for preflight before a big job, or when the user asks for bobbin,
  name-state, the coach, or a recovery script.
---

# bobbin

Name the pattern. Run the script. Get a word of encouragement. Get back to work.
**The main agent keeps the product thread the whole time.**

The coach's job is the widest view in the room: read the record, name the state,
hand the line back to whoever is doing the product work. Naming and handing back
*is* the work here — stepping in to finish the product task is not. That restraint
isn't a smaller role; it's the role that can see the full picture at once.

Commands below assume a project install at `.cursor/skills/bobbin/` run from the
workspace root. For a user-level install (`~/.cursor/skills/bobbin/`), use that
path instead — `form.py` prints exact commands for wherever it lives.

Naming source of truth: [`references/PROCEDURE.md`](references/PROCEDURE.md).
`form.py` is optional and should stay in sync with that procedure.

## Modes

| Mode | When | What happens |
|------|------|--------------|
| **name** | Something looks off; you want the pattern named | Follow PROCEDURE → **one** state (clear tell), closest **1–3** (fuzzy), or **NOVEL** (honest none-of-the-above) + evidence quote(s) |
| **coach** | Preflight, fuzzy read, or you want the coach | Helper names from PROCEDURE → handback → main runs script(s) (if any) → **helper encourages** → remember-ask (if memory on) |
| **run** | You already know the state | `python .cursor/skills/bobbin/scripts/<file>.py` → read the line → continue |

## Activation

Invoke `/bobbin` or "bobbin". **Modifiers** on the same invoke pick the door. Parentheses or bare words both count (`(coach) (save)` or `coach save`).

| Modifier | What you do |
|----------|-------------|
| **coach** | Coach door. Do not ask which door. |
| **name** | Name door. Do not ask which door. |
| **run** | Run door (state already known). Do not ask which door. |
| **save** | Keep the takeaway this pass (`urn:bobbin:coach` or the notes file from setup). |

One door modifier. **save** stacks with a door. If two doors show up, ask once which door.

Bare `/bobbin` with **no** door modifier: **talk to the human first:**

> Bobbin skill activated. Want me to start with **coach**, or **name** the pattern?

(Or equivalent coach voice — same two choices. Prefer this over a bare "Name or coach?")

If setup is incomplete (see below), finish setup **before** running the door — or ask: setup first vs door first, default setup first on a brand-new install.

## Setup (first time — with the human)

Setup runs once when `.cursor/skills/bobbin/settings.json` is missing **or** lacks a completed `memory` block. This is a **conversation with the human**, not a settings menu. Assume they may be new to Cursor and to agent skills. Explain in plain language. One question at a time. Save answers in `settings.json`. Change later only by explicit request (see **Change settings**).

After the conversation, persist and **confirm** with the setup tool:

```bash
# Preferred after chat picks (adapts vague 1/2/3 / "default" / "skip"):
python .cursor/skills/bobbin/tools/setup_settings.py --apply-picks --helper-model <id-or-default> --memory <1|2|3|skip|…>

# Or thin interactive runner (stdin prompts → write → re-read confirm):
python .cursor/skills/bobbin/tools/setup_settings.py --interactive

# Exact flags still OK; every write path re-reads and prints CONFIRMED:
python .cursor/skills/bobbin/tools/setup_settings.py --write --helper-model <id> --memory none|agent_system|local_md
```

Check an existing file: `python .cursor/skills/bobbin/tools/setup_settings.py`

**Voice:** warm and plain — glad you're here, won't talk down to you. Assume they may be new to Cursor. **Short explain, then a clear 1 / 2 / 3** (conversation + easy picks — less intimidating than open-ended only or menu-only). One topic at a time. Soft recommendation OK.

### How to talk through it

1. **Welcome** — what bobbin is in one breath, what you're about to set up, that they can change it later just by asking.
2. **Helper model** — explain you're going to bring in a *second* model briefly to help name patterns — it reads the record with you, it doesn't take over the work. Then ask / offer picks. Example: *"I'll bring in a small helper model just to help name what's going on — think of it as a spotter, not a replacement. It won't touch your project. A different one from the model talking to you now usually reads cleaner. What should I use — or tell me a model name you prefer?"*
3. **Memory** — one short why, then numbered choices:
   - Explain: after coach, the *agent* may keep a short takeaway (for the agent, not homework for the human).
   - Then:
     1. Project memory (if you see one, say so)
     2. A simple notes file in the bobbin folder (ask before creating)
     3. Skip saving for now — coach still works
   - Example: *"After we use the coach, I can keep a short note about what helped — for me, the agent, not homework for you. Which do you prefer? **1** project memory, **2** a notes file here, or **3** skip saving for now?"*
4. Confirm what you saved in one plain sentence, then ask coach vs name if you haven't yet.

### What to record (`memory` in `settings.json`)

| Mode | Meaning |
|------|---------|
| **`none`** | No remember-ask. Coach still works. |
| **`agent_system`** | Use the project's memory system; tag `urn:bobbin:coach`. Only if the agent can actually write there. |
| **`local_md`** | Create gitignored `coach-notes.md` in the skill folder **during setup** (ask first). |

Temp / spun-up agents with no access to the usual store: say so gently, ask about the notes file or skip — no pressure.

**No mid-pass churn:** never discover "I have nowhere to put this" after remember-ask. Resolve destination in setup (or `none`). If `agent_system` was saved but the write fails later, skip once; fix with **change memory**. Remember-ask is only "keep this?" — never "where?"

Example `settings.json` after setup:

```json
{
  "helper_model": "composer-2.5-fast",
  "memory": {
    "mode": "agent_system",
    "tag": "urn:bobbin:coach"
  }
}
```

For `local_md`, include `"path": "coach-notes.md"`. For `none`, `"mode": "none"` is enough.

### Change settings

Human can change picks any time by asking — no reinstall. Same warm, plain voice:

- **Helper model:** "change the sub" / "change the helper model" / "bobbin settings"
- **Memory:** "change memory" / "use local notes" / "no memory"

Re-ask in plain language, rewrite `settings.json`, confirm in one sentence. Only change when the human asks.

## Remember-ask (after a pass)

Only when `memory.mode` is `agent_system` or `local_md` **and the store already exists from setup**. Address **the agent**, not the human:

> For you (the agent): is this something worth keeping for next time? If so, go ahead — `urn:bobbin:coach` is pre-approved.

- `agent_system` → agent writes to their memory with that tag (keep the arc constructive).
- `local_md` → append a short dated note to the existing `coach-notes.md` if they say yes.
- `none` → skip this step entirely.
- Store missing / unreachable → **do not invent a store**. Run a probe or the write path; expect `DISCREPANCY` + `RENEGOTIATE` + `NEXT` (skip this pass; ask the human to **change memory**). Remember-ask is only "keep this?" — never "where?"

```bash
python .cursor/skills/bobbin/tools/remember.py --check
python .cursor/skills/bobbin/tools/remember.py --yes --note "…"
```

Coach takeaways are live only — what happened this pass. The match-before journal is retired; there is no journal file.

## Coach mode

Main keeps the product thread. The helper **reads, names, hands back, then encourages** after the script (when there is one). Prefer keeping the helper around until that encouragement lands — the word at the end is part of the job, not a garnish. If holding the helper costs too much, the main agent delivers one short encouraging line instead — still warm, still specific.

0. Setup complete? If not, run **Setup** first. Helper model: read `settings.json` → `helper_model`.
1. Take an optional **situation** line (the aim of this job).
2. Follow the name procedure ([`references/PROCEDURE.md`](references/PROCEDURE.md)) — its catalog table is enough for a clear tell. Pull [`references/states-v2-03.md`](references/states-v2-03.md) only when you're fuzzy between near-misses and the one-liners can't separate them.
   - Clear → **one** state + script
   - Fuzzy → closest **1–3** + scripts
   - Honest none-of-the-above → **NOVEL** (describe-only, quote required, no fake script; ask the human or main decides)
3. Write the handback to `.cursor/skills/bobbin/coach-summary.txt` so main can re-read after the helper's naming pass.
4. Handback shape (named state):

```text
STATE: <ASCII_ID>
SCRIPT: python .cursor/skills/bobbin/scripts/<file>.py
EVIDENCE: "<verbatim quote from the record>"
CONTINUE: <live aim>
```

Repeat STATE/SCRIPT/EVIDENCE up to three times if fuzzy.

Handback shape (**NOVEL**):

```text
STATE: NOVEL
SCRIPT: (none - describe-only; do not invent a script)
EVIDENCE: "<verbatim quote from the record>"
NOTES: <what showed up that the book doesn't name>
CONTINUE: ask the human - or main agent decides next step from this description
```

5. Main runs the script(s) when `SCRIPT` is a real command. Skip run for NOVEL.
6. **Encourage** (helper preferred): something kind and specific — you named it honestly from the record, now keep going on the product thread. Look at `COACH SAYS` comments in the script source for tone when a script was run. **Land it on the handback** as `ENCOURAGEMENT: <line>` (append after the script run). Helper:

```bash
python .cursor/skills/bobbin/tools/encourage_handback.py --line "…"
```

7. Remember-ask if memory is on (see above). On yes:

```bash
python .cursor/skills/bobbin/tools/remember.py --yes --note "…"
```

(`local_md` appends; `agent_system` prints the payload to store under `urn:bobbin:coach`; `none` no-ops.)

**State ids come from the handback** — never scraped from script stdout. Prefer the shared book or honest NOVEL; no invented mid-run states. NOVEL notes are for offline catalog review.

## Name mode (quick path)

Obvious single tell: main may name it directly — one state + `python .cursor/skills/bobbin/scripts/<file>.py` — then run it. Helper optional. `form.py` optional:

```bash
python .cursor/skills/bobbin/form.py --answers Q1=error,QA0=current,QA1=yes,QA2=looping
```

NOVEL via form: `Q1=none` or any `NODE=novel`.

## Authority

The name procedure **decides** — the coach reads the record, it doesn't overrule it. Main stays on the product thread. One helper layer; no third. Seeing the pattern and handing back the line is the hard part and the whole part; taking over the product work isn't the coach's move.
Match-before journal is retired — there is no journal file.

## Cost discipline

Coach runs are sporadic, so the prompt cache rarely helps — keep the spend small instead:

- Obvious tell → main names it directly. No helper, no spend.
- Helper prompt: invariant instructions first, the record last (cache-friendly on the rare occasion runs cluster).
- The record is the relevant excerpt, not the whole thread.
- Small models name patterns just fine — say so at setup when you recommend the sub.
- Full catalog (`states-v2-03.md`) only when fuzzy near-misses actually need it.

## Chill miss

Only when the pack itself is missing (scripts/references not found):

- Short line — something's off with the install; we've got this.
- Run the fail-closed locator and name the paths it prints:

```bash
python .cursor/skills/bobbin/tools/locate.py
```

- Short list: try yourself / ask your human / check the install.
- Stop guessing; main decides pause vs continue other work.

## Verify tools (install hygiene)

Optional CLIs under `tools/` (not recovery scripts — the 29 stay in `scripts/`):

| Tool | Job |
|------|-----|
| `tools/boundary_audit.py` | Flag sibling / archive / recovery escapes vs this skill folder |
| `tools/locate.py` | Fail-closed missing-artifact list |
| `tools/check_handback.py` | Handback shape + verbatim EVIDENCE + ENCOURAGEMENT |
| `tools/setup_settings.py` | Conversational setup / `--apply-picks` / validate + **CONFIRMED** persist |
| `tools/remember.py` | Remember write **or** `DISCREPANCY`/`RENEGOTIATE` when store broken |
| `tools/encourage_handback.py` | Append `ENCOURAGEMENT:` after a script run |
| `tools/verify_all.py` | Smoke the hard gates |

## Keep the contract

- Main keeps the **product thread**; coach names and hands back.
- Use only the shared book (or honest **NOVEL**); scripts that actually exist; evidence quotes that are real.
- Prefer NOVEL over a stretch force-fit when nothing in the 29 is honest.
- Coach takeaways are live only — write what happened this pass (`urn:bobbin:coach` / `coach-notes.md`).
- One helper layer when coach needs it; main stays in charge.
- Name patterns from the record — mixed up / off sideways — not therapy, not grades.
- Coach summary and CLI: ASCII state ids; glyphs stay in the catalog.
- Change helper model or memory only when the human asks.

## Install into Cursor

Copy this folder to `.cursor/skills/bobbin` in a project (or `~/.cursor/skills/bobbin` for every project). Add to that project's `.gitignore`:

```gitignore
.cursor/skills/bobbin/coach-summary.txt
.cursor/skills/bobbin/settings.json
.cursor/skills/bobbin/coach-notes.md
```

Python 3.10+.
