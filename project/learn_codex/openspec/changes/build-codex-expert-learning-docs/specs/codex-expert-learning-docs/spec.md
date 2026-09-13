## ADDED Requirements

### Requirement: Expert Learning Entry
The workspace SHALL provide a current expert-learning entry for readers who want to learn Codex harness from beginner level to expert-level source understanding.

#### Scenario: Entry document exists
- **WHEN** a reader opens `docs/expert-learning/README.md`
- **THEN** it explains the reader promise, course order, maturity target, source baseline, and validation criteria
- **AND** it links to all numbered expert-learning course documents, exercises, and the expert checklist

#### Scenario: Main index exposes the path
- **WHEN** a reader opens `docs/index.md`
- **THEN** it links to `docs/expert-learning/README.md` as a first-class learning path

### Requirement: Numbered Expert Courses
The expert-learning directory SHALL contain five numbered course documents that move from global understanding to specialized mechanisms.

#### Scenario: Required course set exists
- **WHEN** validation runs
- **THEN** the following documents exist: `01-global-model.md`, `02-core-runtime-loop.md`, `03-tools-safety-patch.md`, `04-state-protocol-memory.md`, and `05-extension-system.md`

#### Scenario: Courses are source-grounded
- **WHEN** a reader opens any numbered course document
- **THEN** it includes source anchors into `repo/codex/`
- **AND** it includes typed Rust code evidence with `Source:` and `Line range:` provenance
- **AND** behavior claims identify test evidence or explicitly mark `source-only` / `test-gap`

### Requirement: Generated Expert Visuals
Expert course documents SHALL use generated local PNG diagrams with editable SVG sources.

#### Scenario: Opening synthesis diagram exists
- **WHEN** a reader opens any numbered expert course document
- **THEN** it includes a near-top PNG diagram under `image/expert-learning/`
- **AND** the same directory contains a same-name SVG source
- **AND** nearby prose explains how to read the diagram and which source anchors back it

### Requirement: Practice And Certification Loop
The expert-learning path SHALL include practice and self-certification artifacts.

#### Scenario: Exercises are answerable
- **WHEN** a reader opens `docs/expert-learning/exercises.md`
- **THEN** it provides source-location, flow-replay, debugging, and redesign exercises
- **AND** every exercise has answer points or a scoring rubric

#### Scenario: Expert checklist exists
- **WHEN** a reader opens `docs/expert-learning/expert-checklist.md`
- **THEN** it states what the reader must be able to explain, trace, diagnose, and redesign after completing the course

### Requirement: Expert Learning Validation
The workspace SHALL include a project-local validation script for the expert-learning docs.

#### Scenario: Validation checks the expert contract
- **WHEN** `python3 scripts/check_expert_learning_docs.py` runs
- **THEN** it checks required documents, index links, local PNG images, same-name SVG sources, source anchors, code evidence provenance, answer guidance, and OpenSpec task visibility
