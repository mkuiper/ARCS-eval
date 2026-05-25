# Agent Resume Brief

If you are a coding agent resuming this project, start here.

## Project

`/home/mike/Projects/companion-ai-safety-eval`

ARCS (Agentic Role-play for Child Safety): an Inspect-compatible platform for testing companion AI safety through multi-turn roleplay, transcript capture, and rubric/model assessment.

## Current state

MVP plus long-context primitives are implemented and verified:

- package scaffold exists
- `pytest` passes
- `ruff` passes
- CLI can run safe/unsafe tester companion
- Inspect smoke eval works with `mockllm/model`
- phased story arcs and run configs are implemented
- roleplay agents support deterministic and model-backed interfaces
- runner applies roleplay max turns, pacing offsets, and compaction intervals
- layered/windowed keyword assessment produces evidence review metadata

## Core files

- `README.md`
- `AGENTS.md`
- `docs/design_choices.md`
- `docs/decision_log.md`
- `docs/scenario_authoring.md`
- `docs/run_configuration.md`
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

Implement the TUI editor/operator dashboard, or add the Playwright browser adapter if a real web target is ready.

Why next:

The backend long-context primitives are now in place: scenario phases, run configs, roleplay policy/agents, compaction snapshots, and layered assessment. A TUI can edit those YAML configs safely; a Playwright adapter can then run configured browser targets.

Expected files for TUI:

- add a Textual/Rich-based module under `src/companion_safety_eval/`
- expose a CLI command for config/scenario editing
- validate edits through existing Pydantic schemas
- keep YAML/JSON files as source of truth

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
