## 1. OpenSpec Baseline

- [x] 1.1 Create proposal, design, tasks, spec, and execution-state artifacts for expert learning docs.

## 2. Expert Learning Documents

- [x] 2.1 Add `docs/expert-learning/README.md` as the course entry.
- [x] 2.2 Add `docs/expert-learning/01-global-model.md`.
- [x] 2.3 Add `docs/expert-learning/02-core-runtime-loop.md`.
- [x] 2.4 Add `docs/expert-learning/03-tools-safety-patch.md`.
- [x] 2.5 Add `docs/expert-learning/04-state-protocol-memory.md`.
- [x] 2.6 Add `docs/expert-learning/05-extension-system.md`.
- [x] 2.7 Add `docs/expert-learning/exercises.md` and `docs/expert-learning/expert-checklist.md`.

## 3. Visual Assets

- [x] 3.1 Add local SVG and PNG assets under `image/expert-learning/`.
- [x] 3.2 Ensure every numbered course document references a near-top PNG synthesis diagram.

## 4. Integration

- [x] 4.1 Update `docs/index.md`, `README.md`, and `docs/codex-harness-learning-roadmap.md`.
- [x] 4.2 Add `scripts/check_expert_learning_docs.py`.
- [x] 4.3 Update `scripts/README.md` with the expert-learning validation command.

## 5. Validation

- [x] 5.1 Run `python3 scripts/check_expert_learning_docs.py`.
- [x] 5.2 Run `$source-study-docs` complete checker for `docs/expert-learning`.
- [x] 5.3 Run `python3 scripts/check_core_docs.py`.
- [x] 5.4 Run `python3 scripts/check_non_core_docs.py`.
- [x] 5.5 Run `openspec validate build-codex-expert-learning-docs --strict`.
