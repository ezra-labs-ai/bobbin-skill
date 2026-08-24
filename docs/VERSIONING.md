# Versioning

Bobbin uses [Semantic Versioning 2.0.0](https://semver.org/): `MAJOR.MINOR.PATCH`.

| Part | When to bump |
|------|----------------|
| **MAJOR** | Breaking changes |
| **MINOR** | Backward-compatible features |
| **PATCH** | Backward-compatible bug fixes |

Pre-1.0 (`0.y.z`): the public API may still change. Prefer clear changelog notes over surprise breaks.

Current version is declared in the root [README](../README.md).

## Tags

- Tag releases on `main` only.
- Tag format: `vX.Y.Z` (example: `v0.1.0`).
- A tag must match the version documented for that release.

## Branching

### Long-lived branches

| Branch | Role |
|--------|------|
| `main` | Release-ready; tagged releases only |
| `staging` | Pre-release integration / soak |
| `dev` | Default integration branch |

Do not commit directly to `main`.

### Short-lived branches

Create from `dev`:

| Prefix | Use |
|--------|-----|
| `feature/<short-slug>` | New work |
| `fix/<short-slug>` | Bug fixes |
| `release/vX.Y.Z` | Release cut |

Examples: `feature/vocab-pack`, `fix/typo-in-skill`, `release/v0.1.0`.

Do not use a `version/` prefix. Release work uses `release/vX.Y.Z`.

## Promotion flow

Feature work merges into `dev` throughout development — **not only at release time**.

| Move | When |
|------|------|
| `feature/*` / `fix/*` → `dev` | The slice is done enough to integrate (reviewed, not half-broken). Land it on `dev` so other work can build on it. This is **not** a release. |
| `dev` → `staging` | You have a candidate set to soak as a possible next release. |
| `staging` → `main` + tag `vX.Y.Z` | Ready to release. Update README version and [CHANGELOG.md](../CHANGELOG.md) (move Unreleased notes under the dated version). |

Steps:

1. Open a PR from `feature/*` or `fix/*` into `dev` when that work is ready to integrate.
2. Promote `dev` → `staging` when ready to soak.
3. Promote `staging` → `main` when ready to release.
4. On `main`, tag `vX.Y.Z` and update the version in the README and root changelog.

## Branch protections

These are the human contract for how the three long-lived branches are treated. Rules are enforced in GitHub; this document records the intent so contributors know what to expect before opening a PR.

**`main` (strict)**

- PR required; no direct commits.
- No force push; no delete.
- Require conversation resolution before merge.
- Prefer 1 approving review when two maintainers are available (Nicki + Emily). If solo, PR-required with reviews optional until a second maintainer is reliable — current intent: start with PR required + 1 review when Nicki and Emily are both active; otherwise note "reviews recommended" until that is reliable.
- Tags only on `main`.
- Require branches to be up to date before merge once CI exists.

**`staging` (medium)**

- PR required (from `dev` or `release/*`).
- No force push; no delete.
- Reviews optional, or 1 approving review when available.

**`dev` (light)**

- Prefer PRs from `feature/*` and `fix/*`.
- No force push; no delete.
- Reviews optional.

**Merge style**

- Prefer **squash** into `dev` to keep feature history linear.
- Prefer **merge commit** into `staging` and `main` for a readable promotion history (`dev` → `staging` → `main`).

## Feature flags

Branch naming is not feature flags. Runtime flags are a separate product concern and are not part of this branching model.
