## ADDED Requirements

### Requirement: Harness-Level Documentation Contract
The core documentation set SHALL distinguish first-draft completeness from harness-level understanding.

#### Scenario: Quality gate is visible
- **WHEN** a reader opens `docs/core/README.md`
- **THEN** it explains the maturity levels for the documentation set and the additional requirements for harness-level understanding

#### Scenario: Existing docs are presented as current artifacts
- **WHEN** a reader opens `docs/core/README.md`
- **THEN** it links to the existing topic documents as current artifacts rather than referring to them as future documents

### Requirement: Replayable Runtime Explanation
Core runtime topic documents SHALL include enough behavioral detail to replay representative flows without reading source code first.

#### Scenario: Session turn loop has an end-to-end trace
- **WHEN** a reader opens `docs/core/02-session-turn-loop.md`
- **THEN** it includes a concrete trace that connects input, turn context, step context, model stream, tool call, tool output, history, rollout, and final events

#### Scenario: Tool runtime has a concrete execution trace
- **WHEN** a reader opens `docs/core/04-tool-runtime.md`
- **THEN** it includes a concrete tool-call trace and a matrix for important built-in tool categories

### Requirement: Core Code Evidence
The core documentation set SHALL include short source excerpts that prove the most important runtime boundaries and core entity structures.

#### Scenario: Code evidence guide exists
- **WHEN** a reader opens `docs/core/README.md`
- **THEN** it links to `docs/core/15-core-code-evidence.md` as a current core topic document

#### Scenario: Topic documents include local code evidence
- **WHEN** a reader opens any topic document from `docs/core/00-core-map.md` through `docs/core/14-observability-utilities.md`
- **THEN** the document includes a `## 核心代码片段` section
- **AND** it includes at least three typed Rust snippets with `Source:` and `Line range:` provenance
- **AND** at least one snippet shows a core `struct`, `enum`, or `trait` definition that carries the topic's state, protocol, config, persistence record, event payload, or central entity shape

#### Scenario: Code evidence is explanatory
- **WHEN** a reader opens `docs/core/15-core-code-evidence.md`
- **THEN** it includes short Rust snippets for thread entry, turn input routing, sampling, world state, tool routing, tool orchestration, multi-agent reservation, and rollout reconstruction
- **AND** each snippet explains what mechanism, boundary, or invariant the code proves
- **AND** each evidence group includes source path and line-range provenance for audit
- **AND** the document includes test anchors for those behavior rules or explicitly marks a gap as `source-only` / `test-gap`

#### Scenario: Code evidence is a validation gate
- **WHEN** `python3 scripts/check_core_docs.py` runs
- **THEN** it fails if any `docs/core/00-15` topic omits the required code-evidence section, Rust snippet count, source anchor, line range, or entity-definition snippet
- **AND** it fails if `docs/core/15-core-code-evidence.md` omits any required aggregate evidence heading, source anchor, line range, Rust snippet, or test anchor

#### Scenario: Reusable source-study checker enforces per-topic evidence
- **WHEN** the `$source-study-docs` checker runs with `--complete`
- **THEN** it fails if a topic document lacks per-topic typed snippets, source provenance, line-range provenance, or an entity/state/protocol definition snippet
- **AND** it fails on unclosed Markdown fences, generated patch residue, or missing resolvable source-anchor files when a source root is provided

### Requirement: Matrices For High-Branching Topics
High-branching core topics SHALL include matrix-style summaries for state, decision, or capability behavior.

#### Scenario: Context docs list world-state sections
- **WHEN** a reader opens `docs/core/03-context-world-state.md`
- **THEN** it includes a WorldState section matrix with source anchors, render conditions, persistence behavior, and reader conclusions

#### Scenario: Extension docs list capability surfaces
- **WHEN** a reader opens `docs/core/09-extensions-inside-core.md`
- **THEN** it includes a matrix for MCP, connectors, plugins, skills, hooks, and extension tools

#### Scenario: Safety docs list policy outcomes
- **WHEN** a reader opens `docs/core/06-safety-sandbox-approval.md`
- **THEN** it includes a matrix for approval policy, exec policy, sandbox, patch safety, and network approval outcomes

### Requirement: Nearby Flow Diagrams
Core topic documents SHALL place at least one local flow, state, or boundary diagram near the section that explains the main runtime path.

#### Scenario: Each topic has a nearby visual path
- **WHEN** a reader opens any topic document from `docs/core/00-core-map.md` through `docs/core/15-core-code-evidence.md`
- **THEN** the document includes a local SVG reference near `## 主流程`, a key trace/matrix section, or the code-evidence section it explains
- **AND** the nearby prose explains how to read that diagram
- **AND** any final `## 图示` section acts only as an index, not as the sole place where the reader encounters the diagram

### Requirement: Reader Self-Check Closure
Core topic documents SHALL include answer guidance for check questions when they claim to be complete learning artifacts.

#### Scenario: Check questions are answerable
- **WHEN** a reader reaches `## 检查题`
- **THEN** the document includes reference answer points or equivalent guidance before `## Follow-up Slots`

### Requirement: Stronger Core Docs Validation
The local core docs validation script SHALL check mechanical quality gates beyond the original skeleton contract.

#### Scenario: Validation catches stale and incomplete docs
- **WHEN** `python3 scripts/check_core_docs.py` runs
- **THEN** it checks required docs, required sections, closed Markdown fences, image references, local source anchor existence, stale planning language, patch residue, and answer guidance
