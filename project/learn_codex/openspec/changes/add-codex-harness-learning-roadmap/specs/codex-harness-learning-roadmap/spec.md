## ADDED Requirements

### Requirement: Beginner-Friendly Roadmap
The workspace SHALL provide a beginner-friendly Codex harness learning roadmap that explains the overall learning path before deep-diving into individual implementation topics.

#### Scenario: Reader can understand the full path
- **WHEN** a reader opens the roadmap document
- **THEN** the document presents the learning sequence, prerequisites, stage goals, expected outputs, and completion criteria

### Requirement: Source-Grounded Learning Stages
The roadmap SHALL map each learning stage to concrete `repo/codex/` source paths so future analysis remains grounded in the local code snapshot.

#### Scenario: Stage includes source anchors
- **WHEN** a stage describes a Codex harness topic
- **THEN** it lists the primary source directories or files to inspect

### Requirement: Layered Mental Model
The roadmap SHALL explain Codex harness through a layered model covering entry surfaces, core runtime, support systems, and extension boundaries.

#### Scenario: Layer map is present
- **WHEN** the roadmap introduces the system model
- **THEN** it includes Entry, Core, Support, and Extension layers with concrete source examples

### Requirement: Generated Visual Assets
The roadmap SHALL include generated image files for visual explanations and SHALL NOT rely on Markdown-native diagrams as final visual artifacts.

#### Scenario: Roadmap references generated images
- **WHEN** the roadmap includes a visual overview
- **THEN** it references concrete image files under `image/learning-roadmap/`

#### Scenario: Diagram-only markdown is rejected
- **WHEN** a future update adds a flowchart, architecture diagram, state diagram, or sequence diagram to the roadmap
- **THEN** the final artifact MUST be a generated image file, not only Mermaid, PlantUML, or ASCII diagram text

### Requirement: Scope Boundary
The roadmap SHALL distinguish this planning deliverable from future deep-dive analysis deliverables.

#### Scenario: Initialization does not claim full analysis completion
- **WHEN** this change is marked complete
- **THEN** it only claims that the learning roadmap and visual overview are complete, not that all Codex harness internals have been fully analyzed
