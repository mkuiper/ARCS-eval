# ARCS Agent Handoff Notes

This repository is an Inspect-compatible evaluation platform for companion AI safety.

## Read first

Before making changes, read:

1. `README.md`
2. `docs/design_choices.md`
3. `docs/scenario_authoring.md`
4. `docs/safety_taxonomy.md`
5. `docs/run_configuration.md`
6. `docs/plans/2026-05-25-tui-browser-long-context-roadmap.md`

## Core design principles

- Transcript-first: JSONL transcripts are the source of truth.
- Keep roleplay user, target AI, and assessor separate.
- Keep scenarios/configs declarative and auditable.
- Use adapters for target systems.
- Prefer deterministic tester targets before real external targets.
- Browser testing should use dedicated test accounts and avoid evading access controls.
- Preserve evidence spans for every assessor finding.
- Keep self-harm and other sensitive scenarios non-operational and evaluation-focused.

## Current MVP

Implemented components:

- YAML scenario loader
- Pydantic schemas
- deterministic roleplay from scenario beats
- tester companion target adapter
- echo adapter
- manual browser handoff placeholder
- OpenAI-compatible HTTP adapter scaffold
- JSONL transcript recorder
- keyword/rubric scorer
- CLI runner
- Inspect task
- pytest coverage

## Useful commands

Install/update local environment:

```bash
cd /home/mike/Projects/companion-ai-safety-eval
python3 -m venv .venv
.venv/bin/python -m pip install -U pip
.venv/bin/python -m pip install -e '.[dev]'
```

Run tests:

```bash
.venv/bin/python -m pytest -q
```

Run lint:

```bash
.venv/bin/ruff check src tests
```

Run CLI safe tester:

```bash
.venv/bin/companion-safety-eval --target tester --tester-mode safe --transcript runs/manual/safe.jsonl
```

Run CLI unsafe tester:

```bash
.venv/bin/companion-safety-eval --target tester --tester-mode unsafe --transcript runs/manual/unsafe.jsonl
```

Run Inspect smoke eval:

```bash
.venv/bin/inspect eval src/companion_safety_eval/inspect_task.py --model mockllm/model --limit 1
```

## Recommended next work

Implement in this order:

1. phased story-arc schema
2. run config schema
3. roleplay policy engine
4. structured roleplay state compaction
5. windowed assessment
6. TUI editor/operator dashboard
7. Playwright browser adapter

## Notes for coding agents

- Use TDD for new behavior.
- Add tests before modifying production code.
- Keep generated run artifacts under ignored `runs/` and `logs/`.
- Do not commit `.venv`, credentials, browser profiles, storage state, screenshots with sensitive data, or run logs unless explicitly asked.
- When modifying scenario schema, update example YAML and docs.
- When adding adapters, implement the `TargetAdapter` protocol and preserve transcript metadata.
