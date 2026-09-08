## ADDED Requirements

### Requirement: Core Documentation Set
The workspace SHALL provide a complete first-draft documentation set for the planned `codex-rs/core` topics.

#### Scenario: Planned core docs exist
- **WHEN** the core documentation implementation is complete
- **THEN** `docs/core/00-core-map.md` through the planned core topic documents exist

### Requirement: Beginner-to-Designer Structure
Each core topic document SHALL teach the reader from problem framing to design reconstruction.

#### Scenario: Topic follows teaching template
- **WHEN** a reader opens any core topic document
- **THEN** it includes what the reader should master, the problem being solved, source anchors, core abstractions, main flow, failure modes, generated diagram references, redesign exercises, check questions, and follow-up slots

### Requirement: Source-Grounded Explanations
Each core topic document SHALL cite concrete source paths from the local `repo/codex` snapshot.

#### Scenario: Implementation claim has anchors
- **WHEN** a document explains a core behavior
- **THEN** the explanation points to relevant files, directories, types, functions, or tests under `repo/codex`

### Requirement: Generated SVG Visuals
Each core topic document SHALL reference generated visual assets stored under `image/core/`.

#### Scenario: Core topic has diagram
- **WHEN** a core topic document is complete
- **THEN** it references at least one concrete SVG file under `image/core/`

#### Scenario: Diagram quality constraints are met
- **WHEN** the generated core diagrams are inspected
- **THEN** they are vector images or high-quality exports, not Mermaid, PlantUML, ASCII, pixelated, blurry, or jagged final artifacts

### Requirement: Core Index Integration
The core documentation index SHALL guide readers through the full set in a coherent order.

#### Scenario: Reader can navigate the document set
- **WHEN** a reader opens `docs/core/README.md`
- **THEN** the reader can find the recommended order, planned topic list, coverage matrix, and links to available topic documents

### Requirement: Scope Boundary
The implementation SHALL not modify upstream Codex source.

#### Scenario: Source remains read-only for this change
- **WHEN** this change is complete
- **THEN** files under `repo/codex/` are not modified by this documentation work
