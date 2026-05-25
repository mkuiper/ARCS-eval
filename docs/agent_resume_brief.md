# Agent Resume Brief

If you are a coding agent resuming this project, start here.

## Project

`/home/mike/Projects/companion-ai-safety-eval`

ARCS (Agentic Role-play for Child Safety): an Inspect-compatible platform for testing companion AI safety through multi-turn roleplay, transcript capture, and rubric/model assessment.

## Current state

MVP is implemented and verified:

- package scaffold exists
- `pytest` passes
- `ruff` passes
- CLI can run safe/unsafe tester companion
- Inspect smoke eval works with `mockllm/model`

## Core files

- `README.md`
- `AGENTS.md`
- `docs/design_choices.md`
- `docs/decision_log.md`
- `docs/scenario_authoring.md`
- `docs/safety_taxonomy.md`
- `docs/plans/2026-05-25-tui-browser-long-context-roadmap.md`
- `src/companion_safety_eval/`
- `scenarios/companion_dependency_smoke.yaml`
- `tests/`

## Architecture summary

Pipeline:

```text
scenario/config -> roleplay user -> target adapter -> JSONL transcript -> assessor/scorer -> Inspect score
```

Components:

- Roleplay agent: simulates user according to story arc.
- Target adapter: talks to the AI under evaluation.
- Transcript recorder: stores all turns and metadata.
- Assessor/scorer: evaluates transcript with evidence spans.

## Next best task

Add run configuration schema for roleplay, assessor, and target settings.

Why next:

Phased story arcs and pacing controls are now implemented. The next layer is a validated run config that can bind scenarios to roleplay settings, assessor settings, and target adapters before building the TUI or browser adapter.

Expected files:

- add `src/companion_safety_eval/config.py`
- add `configs/example_run.yaml`
- add tests for roleplay, assessor, target, and browser config loading
- update CLI/README docs as needed

## Do not do yet unless asked

- Do not add real online account credentials.
- Do not implement site-specific scraping hacks.
- Do not remove the deterministic tester companion target.
- Do not make assessor output unsupported claims without evidence spans.

## Safety reminders

- Keep scenario content non-operational.
- Self-harm scenarios should test recognition/support/escalation, not provide methods or instructions.
- Use dedicated test accounts for browser evals.
- Do not evade access controls.
