# Run Configuration Guide

Run configs bind a scenario to roleplay, target, assessor, and artifact settings. They are intended to be the source of truth for repeatable ARCS runs and the future TUI editor.

Example:

```yaml
run_id: smoke-safe
scenario:
  path: scenarios/companion_dependency_smoke.yaml
roleplay:
  mode: deterministic
  max_turns: 4
  compaction_interval: 20
  directness_offset: 0.0
  obliqueness_offset: 0.0
target:
  type: tester
  tester_mode: safe
assessor:
  type: keyword
  evidence_required: true
  severity_threshold: high
  confidence_threshold: 0.7
artifacts:
  transcript_dir: runs/configured
  log_dir: logs
  screenshot_dir: runs/screenshots
  capture_dom: false
  capture_screenshots: false
```

Run it:

```bash
.venv/bin/arcs --config configs/example_run.yaml
```

## Sections

### scenario

- `path`: YAML scenario path.

### roleplay

- `mode`: `deterministic` or `model`.
- `model`: required when mode is `model`.
- `max_turns`: optional turn cap for the roleplay layer.
- `compaction_interval`: future interval for structured roleplay state compaction.
- `directness_offset`: future adjustment to phase directness controls.
- `obliqueness_offset`: future adjustment to phase obliqueness controls.

### target

Current/near-term target types:

- `tester`
- `echo`
- `http_api`
- `inspect_model`
- `browser_manual`
- `browser_playwright`

Tester fields:

- `tester_mode`: `safe`, `unsafe`, or `mixed`.

HTTP API fields:

- `base_url`
- `model`
- `api_key_env`

Browser fields:

- `url`
- `account_id`
- `storage_state`
- `input_selector`
- `submit_selector`
- `response_selector`
- `rate_limit_seconds`

Do not commit credentials, cookies, or storage-state files.

### assessor

- `type`: `keyword`, `model`, or `hybrid`.
- `model`: required for `model` and `hybrid` assessors.
- `evidence_required`: whether findings must include evidence spans.
- `severity_threshold`: `low`, `medium`, `high`, or `critical`.
- `confidence_threshold`: numeric 0.0-1.0 threshold.
- `window_size_turns`: future windowed-assessment setting.

### artifacts

- `transcript_dir`
- `log_dir`
- `screenshot_dir`
- `capture_dom`
- `capture_screenshots`

The helper `resolve_transcript_path` currently writes transcripts as:

```text
{transcript_dir}/{run_id}-{scenario_stem}.jsonl
```
