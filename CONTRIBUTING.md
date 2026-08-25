# Contributing

Thanks for showing up.

Bobbin is a Cursor skill: shared pattern names (**states**), recovery scripts, and a coach. The install unit is [`bobbin/`](bobbin/). Agents using the skill start at [README_AI.md](README_AI.md). This file is for changing the repo.

## What fits

**Other language ports of the recovery scripts are welcome.** Match the Python set: same state ids, clear names, kind defaults, ASCII stdout. Glyphs stay in the catalog; scripts print ASCII.

The naming book is twenty-nine states. Do not add a new named state or a fake recovery script in a pull request. If a live run lands on **NOVEL**, that note can go in an issue for catalog review — the book only grows between runs.

If you are changing the skill loop itself (`SKILL.md`, `PROCEDURE.md`, coach tools), say so in the PR. Keep the main agent on the product thread; bobbin names, hands back, and encourages. It does not take over the ticket.

## Setup

- [Python](https://www.python.org/) **3.10+** for the current scripts
- A fork of [ezra-labs-ai/bobbin-skill](https://github.com/ezra-labs-ai/bobbin-skill)

```bash
git clone https://github.com/<you>/bobbin-skill.git
cd bobbin-skill
git checkout -b feature/<short-slug> origin/dev
```

Use `fix/<short-slug>` for a bug fix. Branching details: [docs/VERSIONING.md](docs/VERSIONING.md).

To dogfood a change, copy `bobbin/` into `.cursor/skills/bobbin` (or `~/.cursor/skills/bobbin`) in a throwaway project. Leave live-state files behind — they belong to that install, not this repo:

```gitignore
.cursor/skills/bobbin/coach-summary.txt
.cursor/skills/bobbin/settings.json
.cursor/skills/bobbin/coach-notes.md
```

## Pull requests

1. Branch off **`dev`**
2. Open the pull request **into `dev`**
3. Add a short note under **Unreleased** in [CHANGELOG.md](CHANGELOG.md)

Do not open PRs into `main` or `staging`. Those branches are for maintainers promoting a release. `main` is tagged releases only.

If you touched Python scripts or tools, run:

```bash
python bobbin/tools/verify_all.py
```

from the repo root. Say so in the PR if a check does not apply to your change (for example a language port with no Python edits).

## License

This project is MIT. A pull request is offered under the same license — see [`LICENSE`](LICENSE).
