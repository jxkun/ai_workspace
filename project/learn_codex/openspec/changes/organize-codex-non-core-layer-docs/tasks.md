## 1. OpenSpec Baseline

- [x] 1.1 Create proposal, design, tasks, spec, and execution-state artifacts for non-Core layer documentation.
- [x] 1.2 Record the scope decision that "另外三层" means Entry, Support, and Extension from the existing four-layer roadmap.

## 2. Source Survey

- [x] 2.1 Inspect Entry layer source anchors for CLI, TUI, app-server, app-server-protocol, and request processors.
- [x] 2.2 Inspect Support layer source anchors for protocol, rollout, thread-store, context-fragments, and memories.
- [x] 2.3 Inspect Extension layer source anchors for skills, plugin manifests, core-plugins, MCP, hooks, and connectors.

## 3. Documentation

- [x] 3.1 Add `docs/entry/README.md` and `docs/entry/00-entry-map.md`.
- [x] 3.2 Add `docs/support/README.md` and `docs/support/00-support-map.md`.
- [x] 3.3 Add `docs/extension/README.md` and `docs/extension/00-extension-map.md`.
- [x] 3.4 Update `docs/index.md`, `README.md`, and `docs/codex-harness-learning-roadmap.md` so the three layers are current artifacts.

## 4. Visual Assets

- [x] 4.1 Generate `image/architecture/harness-entry-layer-v1.png`.
- [x] 4.2 Generate `image/state-memory/harness-support-layer-v1.png`.
- [x] 4.3 Generate `image/extension-points/harness-extension-layer-v1.png`.
- [x] 4.4 Reference the PNG exports near the opening of their corresponding documents while retaining SVG sources.

## 5. Review And Validation

- [x] 5.1 Add `scripts/check_non_core_docs.py` for mechanical validation of the three layer docs.
- [x] 5.2 Run reviewer pass against source-study-docs requirements and resolve blocking findings.
- [x] 5.3 Run `python3 scripts/check_non_core_docs.py`.
- [x] 5.4 Run `$source-study-docs` checker for `docs/entry`, `docs/support`, and `docs/extension`.
- [x] 5.5 Run `openspec validate organize-codex-non-core-layer-docs --strict`.

## 6. Depth Expansion

- [x] 6.1 Add `docs/entry/01-cli-tui-app-server-flow.md` with a real entry-chain explanation, local PNG/SVG image assets, source snippets, failure matrix, and check answers.
- [x] 6.2 Add `docs/support/01-protocol-rollout-thread-store.md` with protocol/event/rollout/thread-store/context-fragment coverage, local PNG/SVG image assets, source snippets, failure matrix, and check answers.
- [x] 6.3 Add `docs/extension/01-skills-plugins-mcp-hooks.md` with skills/plugins/MCP/hooks/connectors coverage, local PNG/SVG image assets, source snippets, failure matrix, and check answers.
- [x] 6.4 Update layer README files, roadmap/index/methodology, and validation script so the new deep-dive documents are first-class artifacts rather than follow-up placeholders.
- [x] 6.5 Run reviewer pass against the expanded set and resolve blocking findings.
- [x] 6.6 Re-run `python3 scripts/check_non_core_docs.py`, `$source-study-docs` checker for all three layer directories, and `openspec validate organize-codex-non-core-layer-docs --strict`.

## 7. Entry Layer Part Split

- [x] 7.1 Add `docs/entry/02-cli-command-surface.md` for CLI command dispatch, feature/config override flow, TUI handoff, and non-interactive runner boundary.
- [x] 7.2 Add `docs/entry/03-tui-thread-event-routing.md` for TUI app state, `AppServerSession`, thread event channels, active/side thread routing, and UI-only failure boundaries.
- [x] 7.3 Add `docs/entry/04-app-server-json-rpc-control-plane.md` for app-server JSON-RPC transport, `ClientRequest` dispatch, `thread/start`, `turn/start`, and protocol compatibility boundaries.
- [x] 7.4 Add dedicated PNG/SVG image assets for the three Entry part documents and reference PNGs near each document opening.
- [x] 7.5 Update `docs/entry/README.md`, `docs/index.md`, `docs/codex-harness-learning-roadmap.md`, `docs/methodology.md`, and `scripts/check_non_core_docs.py` so Entry part documents are first-class artifacts.
- [x] 7.6 Run reviewer pass and re-run non-Core docs validation, Entry source-study-docs complete check, and OpenSpec validation.
