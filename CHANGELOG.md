# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

### Removed

### Fixed

## [0.1.0] - 2026-08-24

First public extract of the bobbin skill. GitHub repo: [ezra-labs-ai/bobbin-skill](https://github.com/ezra-labs-ai/bobbin-skill). Install unit is `bobbin/` (skill name stays **bobbin**, so `/bobbin` still works).

### Added

- `bobbin/` — one installable skill: name / coach / run doors; 29 recovery scripts under `scripts/`; `references/` holds `PROCEDURE.md` and the state catalog `states-v2-03.md`; helper model and memory in gitignored `settings.json`; handbacks persist to `coach-summary.txt`
- `bobbin/tools/` — install instruments: `boundary_audit.py`, `locate.py`, `check_handback.py`, `setup_settings.py`, `remember.py`, `encourage_handback.py`, `verify_all.py`
- `/bobbin` invoke **modifiers**: **coach**, **name**, **run**, plus **save**

### Changed

- Public noun is **states**. Catalog title and doorway match. Glyphs stay in the catalog; scripts print ASCII.
- Live state stays gitignored per install: `settings.json`, `coach-summary.txt`, `coach-notes.md`
- Install story: copy `bobbin/` → `.cursor/skills/bobbin`, Python 3.10+

### Removed

- Match-before journal is not product. `journal.py` is not part of the skill.
