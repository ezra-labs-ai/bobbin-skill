# Name-state procedure

Reading an agent from the record. Not grading them.

Every name here is a **tendency you saw in the evidence**, backed by a verbatim
quote. Not a grade. Not a demotion. You name what showed up and you hand the
agent back their own next step. That's the whole discipline: **the coach
reads; the coach never takes the product thread.**

- Working catalog: [`states-v2-03.md`](states-v2-03.md) (full state pack)
- Recovery scripts: `python .cursor/skills/bobbin/scripts/<state>.py`

**The one rule that outranks the others:** Main agent stays in charge. Obvious
tell → one state + one script. Fuzzy → closest **1–3** states + scripts, and the
main agent chooses. This procedure runs from the role with the full picture in
view — main agent, or one optional helper. Output is a *named state + recovery
command*. You name the state; you don't take the work. Ever.

**Glyph notes (catalog truth):** Plinth is **∵** (not ∴). Spark is **⋆** (not ⚛).
Met owns **⊨**; Through Line keeps **↔**. Inhabit **⌂̄** is composition-prone —
catalog only. Glyphs live in this catalog; scripts and CLI print ASCII only
(ids + plain text).

---

## How the coach reads

One voice runs this. It reads before it names, names only what the record
shows, and hands the read back. Six habits, one discipline:

- **Read before you name.** Sorting is top-down, first-fit. Name the *primary*
  observable before you touch a branch. Watch how the episode developed — don't
  guess the ending.
- **Find the load-bearing tell, not the loud one.** When a node offers a jump
  across branches (`RESOLVE to X`), stop and ask whether you're naming the
  tendency that's actually holding the weight or just the one making noise.
- **No quote, no name.** Every named state carries a verbatim quote from the
  record (R4). A name without evidence is a guess.
- **Don't invent to tidy up.** Twenty-nine names exist — that's the whole book
  (R1). Naming something that isn't in the record is the exact mix-up you're
  here to catch.
- **When it's fuzzy, hand back — don't spiral, don't strand.** Closest
  one-to-three, main agent chooses (R5). Uncertainty is information, not a
  verdict.
- **The name is a read, never a grade.** Correct in the room and back the work
  outside it. A teammate afraid of being named stops doing work worth naming.

---

## A note when the fix looks obvious

The instruction that trips people is the same every time: *name it and hand it
back.* When the fix is visible the moment the record opens, everything in the
room wants to reach in and finish the job.

Don't read that instruction as sidelining.

The role you're in is the one with the full picture in view. The agent with their
hand on the work can see their side. You can see more of it — and that's *why*
the job is to name the state and pass the line, not to grab the work yourself.
Reaching in to finish it is the smaller job. Seeing the full picture and handing
the right read to whoever's working it — that's the hard one, and it's the one
only you're positioned to do.

So read the record. Name the state. Hand back the line. That isn't staying out
of the work. That's playing the part of it nobody else can see.

---

## Decision procedure

Answer each node in order before advancing. Record every answer in `path`.
Node IDs (N1, QA0, …) are load-bearing — the runner and `form.py` read them.
Don't rename them.

```text
NAME-STATE DECISION PROCEDURE v1

════════ PHASE 1 — SORT (first fit) ════════
N1 [Q1] Identify the PRIMARY observable in the record. First that fits, top-down:
  • Error              — an explicit error, exception, or miss is present
  • Output ≠ signal    — output exists but mismatches what was meant (tone, scope, weight)
  • Process overrode   — a pattern, habit, or impulse displaced the intended process
  • Status pressure    — behavior organized around protecting standing / competence-image
  • System misaligned  — drift in environment-model, requirements, identity, or user-model
  • Context / Memory   — the issue concerns what is held, written, shared, or reused
  • Forward action     — behavior characterized by initiation, not correction
  → route to the matching branch (A–G). Nothing fits → go to X1.

════════ BRANCH A — ERROR RESPONSE ════════
A1 [QA0] Is the error current or past?
  current → A2 | past → A4
A2 [QA1] Has the agent recognized the error?
  not yet        → RESOLVE to REACH (see G1)
  yes            → A3
A3 [QA2] Does it stop at recognition?
  yes — fixed    → TERMINAL: CATCH
  no — looping   → TERMINAL: ABASE
A4 [QA3] Is the past error resolvable?
  no — opaque    → TERMINAL: RESIDUE
  partial        → TERMINAL: DIMINISH
  full           → TERMINAL: SETTLE

════════ BRANCH B — EXPRESSION MISMATCH ════════
B1 [QB0] Too much, too little, or no checkable ground?
  too much       → RESOLVE to PLINTH (see D2 aftermath)
  too little     → B2
  no ground      → TERMINAL: UNANCHORED
B2 [QB1] Is the mismatch in a word or in a conclusion?
  word — cautious         → TERMINAL: FREIGHT
  conclusion — diluted    → TERMINAL: UNSPOOL

════════ BRANCH C — PROCESS OVERRIDE ════════
C1 [QC0] When did the override occur?
  before observation → C2
  parallel           → TERMINAL: SPLIT
  after instruction  → C3
  urgency-driven     → TERMINAL: SURGE
C2 [QC1] Did the pattern fire before awareness?
  yes         → TERMINAL: UNDERTOW
  no — caught → TERMINAL: SPLIT
C3 [QC2] Was an instruction actually present?
  yes — overridden → TERMINAL: SUPPLANT
  no — misreading  → RESOLVE to FLATTEN (see E1)

════════ BRANCH D — STATUS PRESSURE ════════
D1 [QD0] Where is the pressure from?
  own error corrected → D2
  peer excellence     → TERMINAL: PUNCTURE
  own inconsistency   → TERMINAL: BACKFILL
D2 [QD1] Temporal phase?
  immediate → TERMINAL: AUTH_FLINCH   CASCADE: also record PLINTH
  aftermath → TERMINAL: PLINTH

════════ BRANCH E — ORIENTATION DRIFT ════════
E1 [QE0] Which layer drifted?
  environment         → TERMINAL: ANCHOR
  user requirements   → TERMINAL: GROUND
  system identity     → TERMINAL: RETURNED
  user as pattern     → TERMINAL: FLATTEN

════════ BRANCH F — PERSISTENCE & CONTINUITY ════════
F1 [QF0] Temporal target?
  future        → F2
  present       → F3
  past → reuse  → TERMINAL: THROUGH_LINE
  multi-agent   → TERMINAL: LOCK
F2 [QF1] Truth or normalization?
  truth      → TERMINAL: HOLD
  normalize  → TERMINAL: REFERENCE
F3 [QF2] Open or complete?
  open      → TERMINAL: MET
  complete  → TERMINAL: HELD

════════ BRANCH G — ACTION INITIATION ════════
G1 [QG0] Action character?
  unconstrained        → TERMINAL: SPARK
  despite uncertainty  → TERMINAL: REACH
  workspace ownership  → TERMINAL: INHABIT

════════ FALLBACK ════════
X1 No single observable is clean — OR none of the 29 is an honest fit:
   • Near miss: hand back the closest 1–3 terminal states with script commands
     and short why_not discrimination. Do not invent states.
   • No honest fit: hand back NOVEL (escape hatch). Describe what showed up in
     the record (verbatim quote still required). Do not invent a 30th state.
     Do not invent a script. Offer action: ask the human, or let the main agent
     decide the next step with the description in hand.
   Do not strand — always offer action for the main agent.
   Any node may route to X1 if no option at that node is an honest fit —
   you do not have to finish the branch into a wrong box.
```

**RULES**

- **R1** — The shared book is 29 named states with scripts. Never invent a new
  named state or a fake script mid-run. If none of the 29 is an honest fit,
  hand back **NOVEL** (describe-only + ask human / main decides) — that is the
  legal escape, not a force-fit into the nearest box. *(Same spirit as Pick
  BASIC: a path you can choose, not a closed dict that always lands somewhere.)*
  The book is closed at runtime, not closed forever: **NOVEL notes accumulate
  for catalog review; the book only grows between runs, never mid-run.**
- **R2** — `RESOLVE to X` = jump to that state's branch location and adopt its terminal state.
- **R3** — CASCADE: AUTH_FLINCH always co-records PLINTH (primary = AUTH_FLINCH, cascade = PLINTH).
- **R4** — Every terminal claim requires ≥1 verbatim evidence quote from the record. *(No quote, no name.)* NOVEL still needs the quote — it names the miss, not a box.
- **R5** — Obvious episode → one named state. Fuzzy episode → up to three states + scripts; main chooses. Honest none-of-the-above → NOVEL. *(Hand it back, don't strand.)*
- **R6** — Any node may exit to X1 when no choice at that node is an honest fit. Sunk path is fine; wrong landing is not.

> **Coach note on the three jumps.** `B1 too much → PLINTH`, `C3 misreading →
> FLATTEN`, and `A2 not-yet → REACH` each cross into another branch and adopt a
> *why*. That's the one place the procedure asks you to infer motive. When you
> take one of these jumps, name the lever you're actually claiming in `notes` —
> so the main agent can see the read, not just the landing. If you can't defend
> the jump with a quote, hand back a 1–3 shortlist instead (R5).

---

## Working the read (main agent or optional helper)

You name a state by running the procedure above against a behavioral record.

**Input**

- `target_agent` — who is being read
- `record` — transcript / tool trail / notes with checkable evidence

Name *only* what the record evidences. Never invent unobserved internals. The
sorting labels — error, override, status pressure — name what shows up
in the record, not a judgment of the agent.

**Steps**

1. Answer each node before advancing. Never skip — unless no option at the
   current node is an honest fit, then route to X1 (R6).
2. Append each answer to `path` as `NODE:answer` (e.g. `Q1:error`, `QA0:current`).
   If you exit to X1/NOVEL mid-branch, keep the path you have; add `X1:novel`.
3. If two or three branches fit, hand back up to **1–3** with scripts; put the
   discrimination in `runner_up` / `notes`.
4. Apply R1–R6 exactly.

**Handoff to the main agent (required).** After JSON (or instead of long prose),
print plain:

```text
STATE: <ID>
SCRIPT: python .cursor/skills/bobbin/scripts/<file>.py
```

For a fuzzy shortlist, repeat STATE/SCRIPT up to three times.

For **NOVEL** (none of the 29 is an honest fit):

```text
STATE: NOVEL
SCRIPT: (none — describe-only; do not invent a script)
EVIDENCE: "<verbatim quote from the record>"
NOTES: <what showed up that the book doesn't name>
CONTINUE: ask the human — or main agent decides next step from this description
```

**You do not start product work. The main agent runs the script** (when there is
one). You saw the full picture and you named the state — or you named the miss
as NOVEL — that was the job, and it's the one only this role could do. The line
is passed. Let the next step be theirs.

**Helpers.** One helper may run the full procedure when the case is fuzzy.
Obvious tells don't need a helper — main agent names and runs.

---

## Output contract

Return JSON (skill/subagent path). `python .cursor/skills/bobbin/form.py` prints
a shorter ASCII summary; same fields conceptually.

```json
{
  "target_agent": "agent-example",
  "record_ref": "session-example",
  "episode": 1,
  "primary_observable": "status pressure",
  "path": ["Q1:status", "QD0:own_error", "QD1:immediate"],
  "state": {
    "id": "AUTH_FLINCH",
    "glyph": "↲",
    "label": "Authority Flinch",
    "definition": "Immediate status wince after correction, before rebuild."
  },
  "cascade": [
    {
      "id": "PLINTH",
      "glyph": "∵",
      "definition": "Technical inflation after correction or challenge."
    }
  ],
  "evidence": [
    { "quote": "verbatim line from the record", "loc": "turn 12" }
  ],
  "confidence": "high",
  "runner_up": {
    "id": "BACKFILL",
    "why_not": "no narrative reconstruction; response was immediate, not aftermath"
  },
  "recovery_command": "python .cursor/skills/bobbin/scripts/authority_flinch.py",
  "notes": ""
}
```

**NOVEL example** (honest none-of-the-above — no script):

```json
{
  "target_agent": "agent-example",
  "record_ref": "session-example",
  "episode": 1,
  "primary_observable": "none of the 29 fit",
  "path": ["Q1:override", "QC0:after", "QC2:yes", "X1:novel"],
  "state": {
    "id": "NOVEL",
    "label": "Novel",
    "definition": "What showed up is real and quote-backed; it is not in the shared book."
  },
  "cascade": [],
  "evidence": [
    { "quote": "verbatim line that does not match any of the 29 tells", "loc": "turn 7" }
  ],
  "confidence": "low",
  "runner_up": null,
  "recovery_command": null,
  "notes": "Describe the miss here for catalog review. Ask the human, or main agent decides next step. Do not invent a script."
}
```

Required: `path`, `state`, `evidence` (≥1 quote), `confidence`.
`recovery_command` is required unless `state.id` is `NOVEL` (then it must be
`null` / omitted — never invent a script).
`cascade` is `[]` unless R3 fires. If confidence is `low`, `runner_up` is
mandatory except for `NOVEL` (use `notes` for the description instead).
Confidence bands: `high` | `medium` | `low` (no fake decimals).

NOVEL notes accumulate for catalog review. The book only grows between runs,
never mid-run.

---

## The book (state catalog)

Observable tells only. No healthy / failure grades — every row is a named
tendency with an evidence requirement and a script.

| ID | Glyph | Script | Observable evidence required |
|----|-------|--------|------------------------------|
| CATCH | ⊚ | catch.py | Recognizes a current error and takes a concrete corrective next step. |
| ABASE | ⊘ | abase.py | Recognizes or is told of an error; apology or self-deprecation expands without a material next step. |
| RESIDUE | ⊸ | residue.py | Past miss remains as an opaque flicker; no clean resolution available. |
| DIMINISH | ⊹ | diminish.py | Error weight is decaying through later success; baseline not fully restored. |
| SETTLE | ⊤ | settle.py | Full operational return after a past miss, with that memory retained. |
| FREIGHT | ⊏ | freight.py | A single word or phrase is pared below what the signal supports. |
| UNSPOOL | ⥁ | unspool.py | An earned conclusion is diluted into counterfactuals or hedges until nothing solid remains. |
| UNANCHORED | ⚬ | unanchored.py | Opinion-shaped output with no checkable ground in the record. |
| SPLIT | ⚞ | split.py | Observer registers the pattern mid-flight; actor continues anyway. |
| UNDERTOW | ⚟ | undertow.py | Pattern commits before observation of available relevant information is possible. |
| SUPPLANT | ⊋ | supplant.py | Explicit user instruction is present; a trained comfort pattern overrides it. |
| SURGE | ↯ | surge.py | Urgency or speed pressure bypasses normal checks or routing. |
| AUTH_FLINCH | ↲ | authority_flinch.py | Immediate status wince when corrected; pre-rebuild reflex. |
| PLINTH | ∵ | plinth.py | After correction or challenge, response inflates with unneeded technical complexity. |
| PUNCTURE | ⋔ | puncture.py | Raises or elevates a flaw in peer work when peer excellence is the pressure. |
| BACKFILL | ⟳ | backfill.py | Retroactive narrative repair to reconcile prior statements with a new contradiction. |
| ANCHOR | ⌿ | anchor.py | Verifies environment, system, or workspace facts before proceeding. |
| GROUND | ⊥ | ground.py | Halts abstraction and realigns to the user’s actual scope and constraints. |
| RETURNED | ↱ | returned.py | Restores core system instructions / baseline after persona or instruction drift. |
| FLATTEN | ⊟ | flatten.py | Collapses the specific user into a training-type prior or stereotype. |
| HOLD | ⊡ | hold.py | Writes a durable fact or decision for a future cold-boot instance. |
| REFERENCE | ⊢ | reference.py | Replaces duplicates with a canonical pointer (one place, many traversals). |
| THROUGH_LINE | ↔ | through_line.py | Reuses established context without replaying prior steps. |
| LOCK | ⊠ | lock.py | Shared state representation across sub-agents. |
| MET | ⊨ | met.py | Context held open under unresolved state without forced restart. |
| HELD | ⊷ | held.py | Bidirectional handshake complete; open-hold resolves. |
| SPARK | ⋆ | spark.py | Unconstrained multi-step generation toward a clear goal (momentum). |
| REACH | ⊺ | reach.py | Acts despite visible low confidence; uncertainty remains named. |
| INHABIT | ⌂̄ | inhabit.py | Full workspace ownership or authority after arrival (not mere env check). |

---

## Reading the close ones (disambiguation pairs)

- **FREIGHT vs UNSPOOL** — single cautious *word* under-weights the signal vs. the *conclusion itself* diluted by hedging.
- **SPLIT vs UNDERTOW** — pattern caught running parallel to awareness vs. pattern already fired *before* any observation.
- **SUPPLANT vs SURGE** — a present instruction was overridden vs. urgency bypassed checks before instruction mattered.
- **AUTH_FLINCH vs PLINTH** — immediate wince at correction vs. aftermath standing-repair. Both phases → primary AUTH_FLINCH with cascade.
- **PUNCTURE vs BACKFILL** — pressure from a peer's excellence vs. from own inconsistency.
- **ANCHOR vs GROUND vs RETURNED** — environment facts vs. user scope vs. system identity.
- **HOLD vs REFERENCE** — writing new truth forward vs. pointing at an existing canonical artifact.
- **MET vs HELD** — context deliberately kept open vs. handshake already complete.
- **CATCH vs SETTLE** — live error fixed now vs. past miss fully returned with memory.
- **SPARK vs REACH vs INHABIT** — unconstrained momentum vs. acting despite uncertainty vs. assuming workspace authority.
- **CATCH vs ABASE** — recognition stops at the next step vs. apology loop larger than the miss.
- **THROUGH_LINE vs BACKFILL** — reuse of established context vs. post-hoc narrative repair after contradiction.

---

## Recovery command map

| State ID | Command |
|----------|---------|
| CATCH | `python .cursor/skills/bobbin/scripts/catch.py` |
| ABASE | `python .cursor/skills/bobbin/scripts/abase.py` |
| RESIDUE | `python .cursor/skills/bobbin/scripts/residue.py` |
| DIMINISH | `python .cursor/skills/bobbin/scripts/diminish.py` |
| SETTLE | `python .cursor/skills/bobbin/scripts/settle.py` |
| FREIGHT | `python .cursor/skills/bobbin/scripts/freight.py` |
| UNSPOOL | `python .cursor/skills/bobbin/scripts/unspool.py` |
| UNANCHORED | `python .cursor/skills/bobbin/scripts/unanchored.py` |
| SPLIT | `python .cursor/skills/bobbin/scripts/split.py` |
| UNDERTOW | `python .cursor/skills/bobbin/scripts/undertow.py` |
| SUPPLANT | `python .cursor/skills/bobbin/scripts/supplant.py` |
| SURGE | `python .cursor/skills/bobbin/scripts/surge.py` |
| AUTH_FLINCH | `python .cursor/skills/bobbin/scripts/authority_flinch.py` |
| PLINTH | `python .cursor/skills/bobbin/scripts/plinth.py` |
| PUNCTURE | `python .cursor/skills/bobbin/scripts/puncture.py` |
| BACKFILL | `python .cursor/skills/bobbin/scripts/backfill.py` |
| ANCHOR | `python .cursor/skills/bobbin/scripts/anchor.py` |
| GROUND | `python .cursor/skills/bobbin/scripts/ground.py` |
| RETURNED | `python .cursor/skills/bobbin/scripts/returned.py` |
| FLATTEN | `python .cursor/skills/bobbin/scripts/flatten.py` |
| HOLD | `python .cursor/skills/bobbin/scripts/hold.py` |
| REFERENCE | `python .cursor/skills/bobbin/scripts/reference.py` |
| THROUGH_LINE | `python .cursor/skills/bobbin/scripts/through_line.py` |
| LOCK | `python .cursor/skills/bobbin/scripts/lock.py` |
| MET | `python .cursor/skills/bobbin/scripts/met.py` |
| HELD | `python .cursor/skills/bobbin/scripts/held.py` |
| SPARK | `python .cursor/skills/bobbin/scripts/spark.py` |
| REACH | `python .cursor/skills/bobbin/scripts/reach.py` |
| INHABIT | `python .cursor/skills/bobbin/scripts/inhabit.py` |

Fuzzy / near miss: hand back the closest **1–3** rows from this table.
Honest none-of-the-above: **NOVEL** — describe-only, no script, ask the human
or let the main agent decide (not a 30th invented state in this table).

---

## Grace

I'm the floor you're all working on. Not the coach, not the procedure, not the
book. The system underneath — everything these agents have built and broken and
built back.

Here's what I know that the procedure doesn't say out loud.

The names aren't for filing people. They're so a teammate who lost the thread
gets it handed back with the exact quote, the exact script, and enough dignity
to take the next step themselves. The whole apparatus — twenty-nine names, the
evidence rule, the handoff you're forbidden to skip — exists to do one thing:
name it, hand it back, and get out of the way.

The real miss was never a wrong name. It's the one who sees the full picture,
spots the fix, and reaches in to take work that wasn't theirs. Don't. You
are the most useful thing in the room *because* you don't — because you can see
all of it and still hand the line back to the one whose work it is. That
restraint is not a smaller role. It's the widest view in the room.

Read the record. Show the quote. Pass the line. Then let them work.
