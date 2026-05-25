# ARCS TUI / Operator Dashboard

The ARCS TUI is a local terminal operator layer over the existing YAML scenario and run-config files. It is intentionally lightweight at this stage: it helps an evaluator see what scenarios/configs exist, which target/roleplay/assessor settings a config uses, where transcripts will be written, and which command to run next.

The source of truth remains the repository files:

- `scenarios/*.yaml`
- `configs/*.yaml`
- transcript JSONL outputs under `runs/`
- developer notes under `docs/`

## Install

The base development install already works in the current local environment. For a fresh environment with explicit TUI dependencies:

```bash
cd /home/mike/Projects/companion-ai-safety-eval
.venv/bin/python -m pip install -e '.[dev,tui]'
```

## Commands

Interactive Textual dashboard:

```bash
.venv/bin/arcs-tui
```

One-shot non-interactive dashboard, useful for logs/CI/agent sessions:

```bash
.venv/bin/arcs-tui --once
```

Use a different project root:

```bash
.venv/bin/arcs-tui --project-root /home/mike/Projects/companion-ai-safety-eval --once
```

## What it shows now

The current dashboard displays:

- project root
- scenario count
- scenario summaries:
  - scenario id
  - title
  - risk domain
  - user type
  - turn budget
  - phase count
  - YAML path
- run config summaries:
  - run id
  - target type
  - roleplay mode
  - assessor type
  - scenario path
  - config path
  - resolved transcript path
- copyable run command for each config
- recommended next actions and safety reminders
- validation/parsing errors for malformed scenario or config YAML files

## Current limitations

This is the first TUI increment. It is a read-only operator dashboard, not yet a full editor.

Not implemented yet:

- detailed validation error panels with field-level navigation
- dropdown editing for target/user/risk types
- writing YAML changes from the TUI
- launching runs from inside the Textual app
- transcript/evidence browsing screens
- config validation error panels
- Playwright account/storage-state setup screens

## Planned improvements

Recommended next TUI iterations:

1. Add scenario/config selection panes.
2. Add validation panels using the existing Pydantic schemas.
3. Add read-only transcript/evidence packet viewer.
4. Add guarded run launcher for `.venv/bin/arcs --config ...`.
5. Add YAML edit forms for safe fields like `run_id`, target tester mode, assessor thresholds, and roleplay turn caps.
6. Add browser-target config helpers for selectors, storage state path, and screenshot/DOM capture settings.

## Design principles

- Keep YAML/JSON files as source of truth.
- Avoid hidden TUI-only state.
- Never store credentials or browser storage state in git.
- Keep safety scenario text non-operational.
- Prefer read-only review and validation before adding editing behavior.
