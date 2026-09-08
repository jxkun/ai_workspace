## 1. OpenSpec Baseline

- [x] 1.1 Create proposal, design, tasks, and spec artifacts for core documentation hardening.

## 2. Index And Contract

- [x] 2.1 Rewrite `docs/core/README.md` from planning language to current documentation index.
- [x] 2.2 Add harness-level quality gate and prioritized hardening roadmap to `docs/core/README.md`.

## 3. Core Documentation Hardening

- [x] 3.1 Add a replayable end-to-end trace to `docs/core/02-session-turn-loop.md`.
- [x] 3.2 Add a WorldState section matrix to `docs/core/03-context-world-state.md`.
- [x] 3.3 Add a tool runtime trace and built-in tool matrix to `docs/core/04-tool-runtime.md`.
- [x] 3.4 Add an extension/MCP capability matrix to `docs/core/09-extensions-inside-core.md`.
- [x] 3.5 Add answer keys or answer guidance to `docs/core/00-core-map.md` through `docs/core/09-extensions-inside-core.md`.
- [x] 3.6 Add a safety decision matrix to `docs/core/06-safety-sandbox-approval.md`.
- [x] 3.7 Add `docs/core/15-core-code-evidence.md` with short code snippets and explanations for the core harness path.
- [x] 3.8 Add an evidence matrix and snippet provenance rules so code excerpts are auditable teaching material, not loose file links.
- [x] 3.9 Add per-topic code evidence to `docs/core/00-core-map.md` through `docs/core/14-observability-utilities.md`, including at least one core entity/state/protocol definition snippet per topic.
- [x] 3.10 Place existing SVG flow/state/boundary diagrams near each topic's main flow or key explanatory section, with prose telling readers how to read the diagram.

## 4. Validation

- [x] 4.1 Extend `scripts/check_core_docs.py` to detect stale planning language, missing answer guidance, invalid local source anchors, unclosed Markdown fences, patch residue in the evidence guide, per-topic code evidence, entity-definition snippets, and required 15-doc code/test evidence anchors.
- [x] 4.2 Extend `$source-study-docs` checker so `--complete` mode enforces per-topic code evidence, entity-definition snippets, and generated residue / unclosed-fence / missing-source-anchor issues.
- [x] 4.3 Run `python3 scripts/check_core_docs.py`.
- [x] 4.4 Run `$source-study-docs` generic checker against `docs/core`.
- [x] 4.5 Run `openspec validate harden-codex-core-docs --strict`.

## 5. Latest Source-Study-Docs Complete-Mode Hardening

- [x] 5.1 Re-open execution state for the 2026-09-08 complete-mode pass and record intent, decisions, module board, and journal.
- [x] 5.2 Move or duplicate opening synthesis diagrams near the top of `docs/core/00-core-map.md` through `docs/core/07-apply-patch.md`, and add explicit local evidence notes for triggered sections that are intentionally prose-only.
- [x] 5.3 Move or duplicate opening synthesis diagrams near the top of `docs/core/08-config-env-model-client.md` through `docs/core/15-core-code-evidence.md`, update `docs/core/README.md` wording, and add explicit local evidence notes for triggered sections that are intentionally prose-only.
- [x] 5.4 Run a reviewer pass against `$source-study-docs` complete-mode findings and fix any remaining blocking gaps.
- [x] 5.5 Re-run `python3 scripts/check_core_docs.py`, `python3 /data00/home/jiangxukun/.trae/skills/source-study-docs/scripts/check_source_study_docs.py --docs-dir docs/core --source-root repo/codex --image-root image/core --complete`, and `openspec validate harden-codex-core-docs --strict`.
