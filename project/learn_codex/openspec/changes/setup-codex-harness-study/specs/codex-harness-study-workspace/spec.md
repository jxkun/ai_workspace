## ADDED Requirements

### Requirement: Project Structure
The workspace SHALL provide a self-contained `learn_codex` project structure for Codex harness study, including project entry files, documentation directories, image asset directories, OpenSpec artifacts, and a local source snapshot directory.

#### Scenario: Required project directories exist
- **WHEN** the project initialization is complete
- **THEN** `README.md`, `AGENTS.md`, `.gitignore`, `docs/`, `image/`, `openspec/`, and `repo/` exist under `learn_codex/`

#### Scenario: Upstream source is isolated
- **WHEN** Codex source is downloaded for analysis
- **THEN** the source exists under `repo/codex/` and analysis documents are not written into the upstream source tree

### Requirement: Source Snapshot Traceability
The workspace SHALL record the Codex source version used for analysis, including source URL, commit or release, acquisition date, local path, and fallback source if direct cloning fails.

#### Scenario: Snapshot record can anchor future analysis
- **WHEN** a reader opens `docs/source-snapshot.md`
- **THEN** the reader can identify the upstream repository, local path, target commit or release, acquisition method, and fallback source

### Requirement: Markdown Analysis Methodology
The workspace SHALL define a repeatable methodology for analyzing Codex harness implementation and design ideas through Markdown documents grounded in source code evidence.

#### Scenario: Analysis method is explicit
- **WHEN** a future agent starts a Codex harness topic
- **THEN** `docs/methodology.md` explains the reading order, source evidence expectations, topic document template, validation steps, and completion criteria

#### Scenario: Analysis stays source-grounded
- **WHEN** a document makes an implementation claim
- **THEN** the claim MUST include a source anchor or be marked as pending verification

### Requirement: Generated Image Diagrams
The workspace SHALL require generated image files for diagrams instead of relying on Markdown-native flow diagrams or ASCII diagrams as final deliverables.

#### Scenario: Diagram asset directory exists
- **WHEN** the project initialization is complete
- **THEN** `image/` exists with topic-oriented subdirectories and an image asset policy

#### Scenario: Markdown references concrete images
- **WHEN** a Markdown document includes a flow, architecture, state, or sequence diagram
- **THEN** the final document MUST reference a concrete image file under `image/`

#### Scenario: Markdown-native diagrams are not final artifacts
- **WHEN** Mermaid, PlantUML, ASCII diagrams, or similar text diagrams are used during drafting
- **THEN** the final deliverable MUST include the generated image output in `image/` and must not rely on the text diagram alone

### Requirement: OpenSpec Completion
The workspace SHALL track the initialization work through OpenSpec proposal, design, specs, tasks, and execution state.

#### Scenario: Initialization change is valid
- **WHEN** the initialization work is ready for handoff
- **THEN** `openspec validate setup-codex-harness-study --strict` succeeds

#### Scenario: Initialization tasks close only the current scope
- **WHEN** `tasks.md` is marked complete
- **THEN** it indicates completion of project structure, methodology, image policy, source snapshot, and validation, not completion of all future Codex harness analysis topics
