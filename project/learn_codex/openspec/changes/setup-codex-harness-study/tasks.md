## 1. Project Baseline

- [x] 1.1 Create project entry files: `README.md`, `AGENTS.md`, and `.gitignore`.
- [x] 1.2 Create the planned directory skeleton for `docs/`, `image/`, `repo/`, `prompts/`, `examples/`, `scripts/`, `tests/`, `configs/`, and `data/`.
- [x] 1.3 Add project-level rules that keep analysis source-grounded and enforce generated image diagrams.

## 2. Source Snapshot

- [x] 2.1 Fetch the latest available `openai/codex` source snapshot into `repo/codex/`.
- [x] 2.2 Record source URL, commit or release, acquisition method, fallback source, and local path in `docs/source-snapshot.md`.

## 3. Documentation Method

- [x] 3.1 Add `docs/index.md` as the documentation entry point.
- [x] 3.2 Add `docs/methodology.md` describing the staged analysis method, source evidence rules, topic template, and completion criteria.
- [x] 3.3 Add `docs/diagram-policy.md` and `image/README.md` to define image asset rules.
- [x] 3.4 Add at least one generated image under `image/` and reference it from the methodology document.

## 4. Validation

- [x] 4.1 Validate the OpenSpec change with `openspec validate setup-codex-harness-study --strict`.
- [x] 4.2 Verify the required files and directories exist.
- [x] 4.3 Confirm the initialization scope is complete without claiming completion of all future Codex harness analysis.
