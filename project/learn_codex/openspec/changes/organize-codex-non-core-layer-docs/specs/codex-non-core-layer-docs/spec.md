## ADDED Requirements

### Requirement: Non-Core Layer Documentation Set
The workspace SHALL provide current documentation entries for the non-Core layers defined by the Codex harness learning roadmap.

#### Scenario: Three non-Core layer directories exist
- **WHEN** a reader opens `docs/index.md`
- **THEN** it links to current Entry, Support, and Extension layer indexes
- **AND** those indexes exist under `docs/entry/README.md`, `docs/support/README.md`, and `docs/extension/README.md`

#### Scenario: Each layer has an overview topic
- **WHEN** a reader opens any non-Core layer index
- **THEN** it links to a `00-*` overview document for that layer
- **AND** the overview explains the layer boundary, source anchors, core abstractions, main flow, failure boundaries, code evidence, redesign exercise, and check-question answers

#### Scenario: Each layer has a deep-dive topic
- **WHEN** a reader opens any non-Core layer index
- **THEN** it links to at least one numbered deep-dive topic in addition to the `00-*` overview
- **AND** the deep-dive topic reconstructs a concrete runtime or integration path for that layer rather than only listing modules

### Requirement: Source-Grounded Evidence
Non-Core layer overview documents SHALL use the local `repo/codex/` source snapshot as the first fact source.

#### Scenario: Overview documents include code evidence
- **WHEN** a reader opens any numbered topic under `docs/entry`, `docs/support`, or `docs/extension`
- **THEN** the document includes at least three typed Rust snippets
- **AND** each snippet has `Source:` and `Line range:` provenance
- **AND** at least one snippet in each document shows a central `struct`, `enum`, or `trait` definition for that layer

#### Scenario: Deep-dive documents include behavior evidence
- **WHEN** a reader opens a non-`00` deep-dive topic under `docs/entry`, `docs/support`, or `docs/extension`
- **THEN** the document includes a behavior evidence matrix
- **AND** each matrix identifies behavior rules, source anchors, test anchors or `source-only` / `test-gap`, and reader conclusions

#### Scenario: Source anchors resolve
- **WHEN** non-Core documentation validation runs
- **THEN** all source-like anchors in the three overview documents resolve under the local project root or `repo/codex`

### Requirement: Generated Visual Assets
Non-Core layer overview documents SHALL use generated local PNG images for final architecture and flow diagrams, with same-name SVG files retained as editable sources when available.

#### Scenario: Opening synthesis diagrams exist
- **WHEN** a reader opens any numbered topic under `docs/entry`, `docs/support`, or `docs/extension`
- **THEN** the document includes a near-top local PNG opening synthesis diagram
- **AND** the diagram is stored under the matching `image/` topic directory
- **AND** nearby prose explains how to read the diagram and which source anchors back it

### Requirement: Validation For Non-Core Docs
The workspace SHALL include a mechanical validation script for the non-Core layer documentation set.

#### Scenario: Local validation checks the document contract
- **WHEN** `python3 scripts/check_non_core_docs.py` runs
- **THEN** it checks required documents, required sections, PNG image references, matching SVG source files when expected, source anchor existence, Markdown fences, typed code evidence, line-range provenance, and check-question answer guidance

### Requirement: Roadmap Integration
The learning roadmap SHALL present Entry, Support, and Extension as current documentation paths rather than only future work.

#### Scenario: Roadmap points to current artifacts
- **WHEN** a reader opens `docs/codex-harness-learning-roadmap.md`
- **THEN** Stage 1, Stage 5, and Stage 6 point to the new layer indexes and overview documents
- **AND** the roadmap still distinguishes layer overview completion from future deep-dive completion

### Requirement: Entry Layer Part Split
The Entry layer documentation SHALL split the major entry surfaces into separate first-class topic documents.

#### Scenario: Entry layer has dedicated part documents
- **WHEN** a reader opens `docs/entry/README.md`
- **THEN** it links to dedicated documents for CLI command surface, TUI thread/event routing, and app-server JSON-RPC control plane
- **AND** each document includes a local PNG diagram, source anchors, code evidence, behavior evidence matrix, failure boundaries, and check-question answers
