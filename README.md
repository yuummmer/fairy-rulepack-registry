# FAIRy Rulepack Registry

This repository is a **machine-readable index of FAIRy rulepacks**.

Rulepacks themselves live in separate repositories (e.g. `fairy-rulepacks-geo`, `fairy-rulepacks-insdc`).  
This repo exists so humans *and tools* can discover rulepacks consistently over time.

## What is a rulepack?

A **rulepack** is a versioned set of validation rules for a specific repository, standard, or workflow
(e.g. NCBI GEO bulk RNA-seq submission TSVs, ENA/Webin-CLI naming hygiene, Darwin Core checks, etc.).

FAIRy-core is the local-first engine that executes rulepacks and produces reports.

- Engine: `yuummmer/fairy-core`
- Rulepacks: separate CC0 repositories (listed here)

## Registry file

The registry is stored in:

- `registry.yaml`

It contains:
- rulepack IDs and metadata (title, tags, status)
- the repo + path where each rulepack lives
- available versions and the file name for each version
- the minimum FAIRy-core version required

This structure is designed to support future CLI commands like:
- `fairy rulepack list`
- `fairy rulepack fetch <id>@<version>`
- `fairy validate --rulepack <downloaded-path>`

## Status levels

Each entry has a `status`:

- **official** — maintained by FAIRy (or in close partnership with a design partner)
- **community** — maintained by the community; best-effort support
- **experimental** — early drafts / prototypes; may change frequently

## Adding a rulepack to the registry

PRs are welcome!

## Where should I file an issue?

This repo stays intentionally **thin** (an index + cross-rulepack templates/docs).

- **Rulepack changes** (new checks, required fields, fixtures, releases) → file in the specific rulepack repo (e.g. `fairy-rulepacks-geo`, `fairy-rulepacks-insdc`).
- **Registry changes** (adding/updating entries in `registry.yaml`, ecosystem docs, cross-rulepack starter templates) → file here.
- **Engine features** (new rule types, report formats, multi-input behavior) → file in `yuummmer/fairy-core`.

### Requirements
A rulepack repo must:
1. Be publicly accessible (GitHub is easiest to start)
2. Include a clear license (recommended: **CC0-1.0**)
3. Include at least one tiny fixture dataset (a minimal “good” or “bad” example)
4. Include a README describing intended use

### How to submit
1. Fork this repo
2. Add an entry to `registry.yaml`
3. Open a PR

Please include:
- a stable `id` (lowercase, underscores OK)
- `repo`, `path`, and a version entry with either a git tag or commit SHA in `ref`
- `min_fairy` so users know what engine version they need

## Versioning guidance

Rulepacks should be versioned independently from FAIRy-core.

Recommended practices:
- Use semantic versioning for rulepack versions (`0.1.0`, `0.2.0`, `1.0.0`, etc.)
- Prefer referencing **git tags** in `ref` (e.g. `v0.1.0`)
- If you must reference a commit, use the full SHA

## License

The registry index (`registry.yaml` and docs in this repo) is released under **CC0-1.0** so it can be reused freely
by the FAIR data community.
