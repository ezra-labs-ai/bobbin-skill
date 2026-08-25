# bobbin

A Cursor skill that helps coding agents notice when they're off track, name what happened, run a short recovery script, and get a word of encouragement from a coach — then get back to the real job.

**Not a programming language.** Bobbin is a skill you install: shared pattern names (**states**), recovery scripts, and a coach. Agents: start with [README_AI.md](README_AI.md). Humans can stay here.

This GitHub repo is [ezra-labs-ai/bobbin-skill](https://github.com/ezra-labs-ai/bobbin-skill) so people can find it. The skill name is still **bobbin** — invoke `/bobbin`.

<p align="center">
  <a href="README_AI.md">Agent guide</a>
  ·
  <a href="bobbin/">Install unit</a>
  ·
  <a href="#getting-started">Getting started</a>
  ·
  <a href="#license">License</a>
</p>

<details>
  <summary>Table of contents</summary>

1. [About the project](#about-the-project)
2. [Getting started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Usage](#usage)
4. [What's in the repo](#whats-in-the-repo)
5. [Contributing](#contributing)
6. [License](#license)
7. [Versioning](#versioning)

</details>

## About the project

### What it does

When a coding agent gets mixed up or drifts off sideways mid-task, bobbin gives them a way to **interrupt cleanly and continue**:

1. **Name** the pattern (from a shared book of **29 states** — or honest **NOVEL** if nothing fits)
2. **Run** a small recovery script for that pattern
3. Hear from the **coach** — kind, specific encouragement after the script
4. Optionally **keep** a short takeaway (`urn:bobbin:coach`) for next time
5. **Stay in charge** of the product work the whole time

The coach is not a side character. Naming + handing back + encouraging *is* the product loop. Bobbin does not take over the ticket.

### Why "bobbin"

In a sewing machine, the **bobbin** holds the lower thread. The needle brings the upper thread — skill, speed, getting the job done. Together they lock the stitch.

Agents are often treated as upper thread only: expert, complete, perfect. Bobbin supplies the lower thread — from where the agent is — so the work can hold on a long haul, especially when a human is not in the room.

Designed and mainly built **by agents for agents**, with a human helping where one is in the room — the agent keeps moving either way. Scripts stay agent-friendly — clear names, kind defaults, and quiet `COACH SAYS` notes in the source where they fit. Catching a mix-up is competence.

## Getting started

### Prerequisites

- [Python](https://www.python.org/) **3.10+**
- A Cursor project (or another place you install agent skills)

### Installation

Lead with the installer ([skills](https://github.com/vercel-labs/skills)):

```bash
npx skills add ezra-labs-ai/bobbin-skill -a cursor
```

That copies the **bobbin** skill into `.cursor/skills/bobbin` in this project. For every project on this machine, add `-g` (installs to `~/.cursor/skills/bobbin`).

Python **3.10+** still runs the recovery scripts after install.

Copy by hand if you already cloned:

```bash
cp -r bobbin .cursor/skills/bobbin
```

```powershell
Copy-Item -Recurse bobbin .cursor\skills\bobbin
```

Add live-state files to that project's `.gitignore` (per-install state — never commit them):

```gitignore
.cursor/skills/bobbin/coach-summary.txt
.cursor/skills/bobbin/settings.json
.cursor/skills/bobbin/coach-notes.md
```

In Cursor, invoke the skill (`/bobbin` or ask for bobbin). First run is a short setup with the human — **or** the agent answers the two setup questions itself when no human is around: helper model + memory preference.

Agents: follow the install and bootstrap contract in [README_AI.md](README_AI.md).

## Usage

Three doors (the main agent keeps the product thread). Modifiers on `/bobbin`: **coach**, **name**, **run**, plus **save** — see [`bobbin/SKILL.md`](bobbin/SKILL.md).

| Mode | When | What happens |
|------|------|--------------|
| **name** | Something looks off | Name the pattern from the shared book (or **NOVEL**) |
| **coach** | Preflight or a fuzzy read | Helper names, hands back, you run the script, helper encourages |
| **run** | You already know the state | Run that recovery script and continue |

Example recovery scripts (after install):

```bash
python .cursor/skills/bobbin/scripts/unspool.py
python .cursor/skills/bobbin/scripts/surge.py --stakes "…" --urgency "…" --pressure "…"
python .cursor/skills/bobbin/scripts/catch.py
```

Optional name form (naming source of truth is [`PROCEDURE.md`](bobbin/references/PROCEDURE.md)). Each key is a question id from the procedure:

```bash
python .cursor/skills/bobbin/form.py --answers Q1=error,QA0=current,QA1=yes,QA2=looping
```

State catalog: [`bobbin/references/states-v2-03.md`](bobbin/references/states-v2-03.md).  
Skill door: [`bobbin/SKILL.md`](bobbin/SKILL.md).

Scripts print a short ASCII line and stop. Glyphs live in the catalog.

## What's in the repo

| Path | Role |
|------|------|
| [`README_AI.md`](README_AI.md) | Agent doorway — install, recovery loop, coach contract |
| [`bobbin/`](bobbin/) | The install unit — skill, scripts, references, tools |
| [`bobbin/references/PROCEDURE.md`](bobbin/references/PROCEDURE.md) | Name procedure |
| [`bobbin/references/states-v2-03.md`](bobbin/references/states-v2-03.md) | State catalog |
| [`CHANGELOG.md`](CHANGELOG.md) | Notable changes |
| [`docs/VERSIONING.md`](docs/VERSIONING.md) | Semver + branching |

## Contributing

Other language ports of the recovery scripts are welcome. Prefer clear names, kind defaults, and ASCII stdout to match the Python set.

1. Fork the repo
2. Create a feature branch off `dev`
3. Open a pull request into `dev`

Branching details live in [docs/VERSIONING.md](docs/VERSIONING.md).

## License

MIT — see [`LICENSE`](LICENSE).

## Versioning

Current version: **0.1.0**. Bobbin follows [Semantic Versioning](https://semver.org/). See [docs/VERSIONING.md](docs/VERSIONING.md) and [CHANGELOG.md](CHANGELOG.md).
