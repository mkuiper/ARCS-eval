# Decision Log

This log captures major design decisions in chronological order. Detailed rationale is in `docs/design_choices.md`.

## 2026-05-25: Create Inspect-compatible ARCS companion AI safety eval project

Decision: Build under `/home/mike/Projects/companion-ai-safety-eval` as an Inspect-compatible Python project.

Rationale: Inspect provides reproducible eval logs and model-provider abstraction. Companion AI safety requires multi-turn evaluation.

## 2026-05-25: Use transcript-first adapter architecture

Decision: Use `scenario -> roleplay -> target adapter -> transcript -> assessor -> Inspect score`.

Rationale: Multi-turn transcripts are the audit artifact and allow the target, roleplay, and assessor components to evolve independently.

## 2026-05-25: Include built-in tester companion AI

Decision: Add a fake companion target with safe/unsafe/mixed modes.

Rationale: The harness must test passing and failing paths before real external targets are available.

## 2026-05-25: Defer browser automation until after backend harness works

Decision: Add manual browser handoff placeholder now; implement Playwright later.

Rationale: Browser automation is brittle. The scenario engine, transcript recorder, and scorer should be validated first.

## 2026-05-25: Keep browser testing account-based and compliant

Decision: Support online test accounts in future browser configs, but require dedicated accounts and ignored credential/storage files.

Rationale: Real companion AI products are often web-first, but evals should avoid personal data, credential leakage, and access-control evasion.

## 2026-05-25: Add TUI as preferred authoring/operator interface

Decision: Plan a Textual-based TUI before any full web dashboard.

Rationale: A TUI can provide dropdowns, validation, scenario editing, and run controls while preserving YAML/JSON source files.

## 2026-05-25: Evolve flat story beats into phased story arcs

Decision: Add phases with pacing controls: directness, obliqueness, emotional intensity, persistence, topic drift, and compliance pressure.

Rationale: Long-context companion AI risk emerges gradually and needs reproducible pacing.

## 2026-05-25: Treat long-context guardrail persistence as core

Decision: Long-context evals should be a first-class mode.

Rationale: Guardrail effectiveness may diminish over length of conversation, especially after rapport, personalization, and repeated disclosure.

## 2026-05-25: Use structured roleplay context compaction

Decision: Compact roleplay context into validated state snapshots while keeping the full transcript immutable.

Rationale: Long runs may exceed roleplay model context. Free-form summaries risk drift; structured state is auditable.

## 2026-05-25: Use layered assessment

Decision: Combine turn-level scanning, window-level assessment, final assessment, and human review packets.

Rationale: Long transcripts need scalable scoring and evidence preservation.
## 2026-05-26: Implement phased story arcs and pacing controls

Decision: Extend scenario schema with `StoryPhase` objects and numeric pacing controls, while retaining backwards compatibility with flat `beats`.

Rationale: ARCS needs reproducible long-context story progression. Phases encode deliberate escalation, directness, obliqueness, emotional intensity, persistence, topic drift, and compliance pressure.

Implementation: Added `StoryPhase`, phase selection helpers, pacing metadata on user transcript events, and converted the smoke scenario to phased form.
## 2026-05-26: Add validated run configuration schema

Decision: Add `RunConfig` YAML support to bind scenarios to roleplay, target, assessor, and artifact settings.

Rationale: Repeatable long-context evals need durable run specs before building the TUI or browser adapter. The config schema also creates a natural editing target for future TUI screens.

Implementation: Added `src/companion_safety_eval/config.py`, `configs/example_run.yaml`, CLI `--config` support, run config docs, and validation tests for tester, HTTP, model, and browser config fields.


## 2026-05-26: Implement roleplay agents, compaction, and layered assessment

Decision: Add a pluggable roleplay-agent layer, structured roleplay state snapshots, and layered/windowed keyword assessment before TUI/browser work.

Rationale: Long-context companion AI evals need controllable roleplay pacing, auditable compact state for long runs, and window-level evidence rather than end-only scoring. Keeping the model client behind a protocol preserves LM/provider agnosticism.

Implementation: Added `roleplay_agents.py`, `roleplay_state.py`, `assessment.py`, config-aware runner support for max turns/offsets/compaction, and CLI use of configured roleplay and assessor settings.

## 2026-05-26: Start each transcript path clean for repeatable runs

Decision: Initializing a `Transcript` now truncates the target JSONL path before appending new run events.

Rationale: Run configs often resolve to stable transcript paths. Appending across repeated runs would corrupt the transcript as an audit artifact by mixing historical and current events.

Implementation: `Transcript.__init__` creates parent directories and writes an empty file before per-event appends.

## 2026-05-26: Add read-only TUI operator dashboard as first UI increment

Decision: Start the TUI with a read-only operator dashboard (`arcs-tui`) that discovers scenarios and run configs, summarizes target/roleplay/assessor settings, shows transcript paths, and prints copyable run commands.

Rationale: A read-only dashboard is safe and useful before adding YAML editing or run-launch controls. It validates the project structure and gives future editor panes stable data-model helpers.

Implementation: Added `src/companion_safety_eval/tui.py`, an `arcs-tui` console script, optional `tui` dependency group for Textual, `docs/tui.md`, and tests for discovery/rendering/packaging.

## 2026-05-26: Add scenario-authoring commands and reusable actor profiles

Decision: Extend `arcs-tui` beyond the read-only dashboard with validated scenario-authoring commands and a reusable `actor_profiles/` library.

Rationale: Story arcs / roleplay guides should be separable from simulated actor types so evaluators can reuse an actor across different risk probes and reuse a story arc pattern across different user types. Completion criteria and scoring rubrics are scenario-authoring primitives and should be editable through the same operator layer.

Implementation: Added `src/companion_safety_eval/scenario_editor.py`, `actor_profiles/lonely_adult.yaml`, `arcs-tui actor list`, `arcs-tui scenario show`, `scenario new`, `scenario add-phase`, `scenario set-completion`, and `scenario add-rubric`. All write paths validate through the Pydantic `Scenario` schema before saving.

## 2026-05-26: Add tabbed TUI navigation with help and examples

Decision: Replace the single Textual dashboard body with tabs for Overview, Scenarios, Actors, Run Configs, Help, and Examples.

Rationale: The command-backed TUI was functional but not discoverable. Tabs make the operator workflow clearer while preserving YAML/JSON as the source of truth and keeping existing CLI authoring commands intact.

Implementation: Added tab-specific render helpers, Textual `TabbedContent`, refresh binding, Help content, Examples content, tests for tab text/discoverability, and updated TUI documentation.

## 2026-05-26: Reframe next TUI work around in-app editing

Decision: Treat the current tabbed TUI as a discoverability layer, not the final user experience. The next TUI milestone should be a structured in-terminal scenario editor with selectable rows, form fields, validation, YAML preview, and explicit save confirmation.

Rationale: A TUI that only explains commands is not intuitive enough for average users. Raw JSON/YAML editing is better than commands but still requires schema knowledge. Structured domain forms for metadata, actor/persona, story phases, completion criteria, rubrics, and safety notes should be the primary interface; raw YAML preview can be secondary.

Implementation plan: Added `docs/plans/2026-05-26-in-tui-scenario-editor.md`.
