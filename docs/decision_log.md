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

