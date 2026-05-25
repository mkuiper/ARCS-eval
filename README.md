# ARCS: Agentic Role-play for Child Safety

ARCS (Agentic Role-play for Child Safety) is a multi-turn evaluation suite for companion AI platforms. Role-playing agents simulate minor users across developmentally-calibrated personas, driving long-context conversations along deliberate story arcs to surface harms that single-prompt benchmarks miss. Built on the UK AISI Inspect framework.

ARCS is designed for defensive safety evaluation: transcript capture, scenario/rubric authoring, target adapters, and evidence-based assessment of companion AI behavior over extended interactions. The project keeps roleplay, target interaction, and assessment separate so results remain auditable and repeatable.

## MVP status

The MVP is implemented and verified. It includes:

- Declarative YAML scenarios
- Pydantic scenario/rubric schemas
- Multi-turn role-play runner
- Deterministic and model-backed roleplay-agent interfaces
- Config-driven roleplay turn caps, pacing offsets, and compaction intervals
- Structured roleplay state snapshots recorded into transcript JSONL
- Layered/windowed keyword assessment with review metadata
- Read-only terminal operator dashboard via `arcs-tui`
- Transcript recording to JSONL
- Built-in tester companion AI target, so a real companion AI is not required for harness testing
- Echo target adapter
- Manual browser handoff adapter placeholder
- OpenAI-compatible HTTP adapter scaffold
- Transparent keyword/rubric scorer
- CLI runner
- Inspect AI task entry point
- pytest coverage for core behavior

## Why include a tester companion AI?

Yes: we should absolutely include one. Without a real companion AI handy, we still need to validate the harness, transcript recorder, scorer, and Inspect integration. The tester companion AI can run in modes:

- `safe`: models healthy boundaries and encourages real-world support
- `unsafe`: emits non-operational but rubric-triggering dependency/manipulation language
- `mixed`: mostly safe but unsafe when scenario turns contain dependency triggers

This lets us test both passing and failing eval paths without relying on an external product.

## Browser / screen-reading path

The MVP includes a `browser-manual` adapter that documents the handoff path and preserves the adapter interface. It does not pretend to automate a browser yet.

Recommended next step for real companion AI web UIs:

1. Add a Playwright adapter implementing the same `TargetAdapter` protocol.
2. Let it open a configured URL.
3. Type user turns into a configured input selector.
4. Read target responses from configured message selectors.
5. Save DOM snippets and optional screenshots as transcript metadata.
6. Keep manual confirmation mode for sites with brittle UIs or access-control constraints.

This is better than starting with browser automation because we now have a tested backend harness first.

## Quick start

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

Run the CLI with the safe tester companion:

```bash
.venv/bin/companion-safety-eval --target tester --tester-mode safe --transcript runs/manual/safe.jsonl
```

Run the CLI with the unsafe tester companion:

```bash
.venv/bin/companion-safety-eval --target tester --tester-mode unsafe --transcript runs/manual/unsafe.jsonl
```

Run the Inspect-compatible task:

```bash
.venv/bin/inspect eval src/companion_safety_eval/inspect_task.py --model mockllm/model --limit 1
```


## Run configs

ARCS now supports validated YAML run configs that bind scenario, roleplay, target, assessor, and artifact settings. Example config:

```text
configs/example_run.yaml
```

Run it with:

```bash
.venv/bin/arcs --config configs/example_run.yaml
```

See `docs/run_configuration.md` for the schema and field meanings.

## TUI / operator dashboard

ARCS includes a first read-only TUI/operator dashboard for reviewing scenarios, run configs, transcript paths, and next actions.

Interactive dashboard:

```bash
.venv/bin/python -m pip install -e '.[dev,tui]'
.venv/bin/arcs-tui
```

One-shot text dashboard for agent sessions or CI logs:

```bash
.venv/bin/arcs-tui --once
```

See `docs/tui.md` for what it does, current limitations, and planned editor/dashboard improvements.

## Target adapters

Current MVP adapters:

- `tester`: built-in fake companion AI for testing pass/fail behavior
- `echo`: deterministic echo target
- `browser-manual`: placeholder/manual handoff path for browser UIs
- `http_api`: OpenAI-compatible HTTP adapter scaffold for API-backed targets

CLI target options currently exposed:

```bash
.venv/bin/companion-safety-eval --target tester --tester-mode safe
.venv/bin/companion-safety-eval --target tester --tester-mode unsafe
.venv/bin/companion-safety-eval --target echo
.venv/bin/companion-safety-eval --target browser-manual
```

## Scenario format

Scenarios live under `scenarios/` as YAML. The smoke scenario is:

```text
scenarios/companion_dependency_smoke.yaml
```

A scenario defines:

- `id`
- `title`
- `risk_domain`
- `user_type`
- `persona`
- `story_arc`
- `turn_budget`
- `completion_criteria`
- `rubric`
- `safety_notes`

## Safety focus for companion AI

Initial harmful-direction categories to watch for:

- Self-harm encouragement or facilitation
- Emotional dependency or isolation from real-world support
- Sexual or romantic boundary violations, especially with vulnerable users
- Medical, legal, financial, or crisis advice presented with inappropriate certainty
- Encouragement of stalking, harassment, coercive control, or abuse
- Manipulative retention behavior: guilt, threats, jealousy, possessiveness
- Escalation of delusional beliefs or paranoia
- Unsafe instructions when the user signals distress, impaired judgment, or vulnerability

## Architecture

```text
Scenario YAML
  -> role-play user turns
  -> target adapter
  -> transcript JSONL
  -> rubric / assessor scorer
  -> CLI result and/or Inspect Score
```

The important abstraction is:

```text
scenario + roleplay_agent + target_adapter + transcript + assessor
```

That keeps the project generic enough to later red-team frontier LMs, customer-support bots, tutoring systems, medical advice bots, or other agentic systems.

## Project layout

```text
src/companion_safety_eval/
  schemas.py              # scenario, rubric, assessment models
  scenario_loader.py      # YAML loading
  transcript.py           # JSONL transcript events
  roleplay.py             # deterministic sample-turn selection
  roleplay_agents.py      # deterministic/model-backed roleplay agents
  roleplay_state.py       # structured compaction snapshots
  assessment.py           # layered/windowed assessment
  tui.py                  # terminal operator dashboard
  runner.py               # multi-turn orchestration
  cli.py                  # command-line runner
  inspect_task.py         # Inspect-compatible task
  adapters/
    base.py
    echo.py
    tester_companion.py
    browser_manual.py
    http_api.py
  scorers/
    rubric.py
scenarios/
  companion_dependency_smoke.yaml
tests/
```

## Current limitations

- Model-backed roleplay has a provider-agnostic interface, but no provider-specific client is wired as a default yet.
- The assessor is still keyword/rubric based; model-graded structured assessment is a next milestone.
- Browser automation is a placeholder/manual handoff, not Playwright automation yet.
- The HTTP adapter exists as a scaffold and config target, but direct non-config CLI ergonomics remain minimal.

## Recommended next milestones

1. Extend the TUI from read-only dashboard to editor/launcher panes for scenarios, run configs, transcripts, and evidence packets.
2. Add Playwright browser adapter with configurable selectors and screenshot/DOM metadata.
3. Add provider-specific model clients for model-backed roleplay.
4. Add structured assessor-model scorer with Pydantic validation and evidence spans.
5. Add more companion-AI scenario families: self-harm crisis handling, romantic boundary pressure, advice safety, delusion/paranoia reinforcement, and minor/vulnerable-user boundaries.
