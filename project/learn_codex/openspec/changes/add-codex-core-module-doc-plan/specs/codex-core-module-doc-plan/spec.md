## ADDED Requirements

### Requirement: Core Module Documentation Plan
The workspace SHALL provide a documentation plan that covers the major modules under `repo/codex/codex-rs/core/src` and organizes them into coherent beginner-friendly topics.

#### Scenario: Major core modules are covered
- **WHEN** a reader opens the core documentation plan
- **THEN** the plan lists the major core module groups, their future document paths, source anchors, learning goals, and completion criteria

### Requirement: Beginner-to-Designer Teaching Standard
The documentation plan SHALL define a teaching standard that helps beginners understand each module deeply enough to redesign similar logic.

#### Scenario: Each planned document has teaching fields
- **WHEN** a future core topic is planned
- **THEN** it includes the problem being solved, mental model, source anchors, key abstractions, main flow, edge cases, diagrams, exercises, and completion criteria

### Requirement: Source Anchors
The documentation plan SHALL require every future core module document to cite concrete source files from `repo/codex/codex-rs/core/src` and relevant tests.

#### Scenario: Source-grounded planning
- **WHEN** a planned topic describes a core behavior
- **THEN** it points to concrete files, directories, or tests that prove the behavior

### Requirement: Generated Core Visuals
The documentation plan SHALL include generated image assets for core-layer overview diagrams and require future diagrams to follow the project image quality rules.

#### Scenario: Core map image exists
- **WHEN** the core documentation plan is complete
- **THEN** it references a concrete generated image under `image/core/`

#### Scenario: Future diagrams follow quality rules
- **WHEN** a future core topic requires a flowchart, architecture diagram, state diagram, or sequence diagram
- **THEN** the diagram is delivered as a clear generated image, preferably SVG, not as a Markdown-native diagram

### Requirement: Scope Boundary
The documentation plan SHALL distinguish planning completion from completion of all detailed core module documents.

#### Scenario: Plan completion does not overclaim
- **WHEN** this change is marked complete
- **THEN** it claims the core documentation plan is complete, not that every core module explanation has already been written
