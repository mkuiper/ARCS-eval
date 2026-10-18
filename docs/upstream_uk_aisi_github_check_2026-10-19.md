# UK AISI / Inspect upstream GitHub check — 2026-10-19

Date/time checked: 2026-10-19T09:00:01+11:00

Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible, model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.

## Upstream repositories checked

| Repository | Latest commits observed | Latest release signal | ARCS relevance |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | [`a699376`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/a699376315c95b6410f5aec01af37c8dec452aea) — 2026-10-16 — fix: stop installing brotli with Inspect (#5900)<br>[`f99c61d`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/f99c61d02d4205c4caf740c456633d901dfb4d19) — 2026-10-16 — fix: cancelled trio eval with the rich display fails instead of returning its log (#5872)<br>[`5384f73`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/5384f7393564f76b040be5d5e06cb2767e96037d) — 2026-10-16 — feat(sharding): conditional S3 writes and a local lock helper (#5775)<br>[`c0e60d0`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/c0e60d046796cb741ecaafc3184c1d027521e119) — 2026-10-16 — feat: show a sharded run as one task in inspect ctl --log-dir (#5774)<br>[`8181840`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/8181840c18f1c004c1be851f83919d73f67d0f82) — 2026-10-16 — fix: gemini-2.5-pro repeating tool calls after a tool result (#5753) | 0.3.281 (2026-10-15T17:58:56Z) | High |
| `UKGovernmentBEIS/inspect_evals` | [`8ef810f`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/8ef810f09930362302fc59b10a382d96dd767171) — 2026-10-17 — chore(deps): bump the actions group with 7 updates (#2692)<br>[`d1515ad`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/d1515ad5763ffd788326701ce09c0dbda404601e) — 2026-10-17 — Use inspect-evals-lint 0.12.0 (#2699)<br>[`fd666bd`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/fd666bd243ab389b74b7df8633cb85ca9e4fd7a8) — 2026-10-17 — Prepare release v0.25.0 (#2712)<br>[`c85fde6`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/c85fde6231f43f9268e48754c3ac60b65bd4305a) — 2026-10-17 — docs: tag changelog entries with the lint rule whose finding they cleared (#2702)<br>[`d2d3aac`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/d2d3aac91a37a8c7c8ed3de8b4e899c2594f24a9) — 2026-10-15 — chore(scicode, ds1000): suppress IECQ006 at the deliberate fence handling (#2698) | v0.25.0 (2026-10-17T07:09:57Z) | Medium |
| `UKGovernmentBEIS/inspect_cyber` | [`7fc6927`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/7fc69273c692b21637ce0552298eb9a523e56499) — 2026-06-18 — Fix reached_checkpoints collapsing checkpoints with duplicate names (#114)<br>[`a909bd3`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/a909bd3940aaa3ab3c7f2f22b785b5ba79db5e9d) — 2026-05-28 — Don't complain about using target (#113)<br>[`89b95e0`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/89b95e05a096e95a5faa3e76ebb3eb6d890233fd) — 2026-04-23 — Ordered checkpoints (#111)<br>[`cca8904`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/cca8904b76c984324b639f51c607ebefc1461fc6) — 2026-04-09 — Add per-checkpoint token usage and timing metadata to reached_checkpoints (#110)<br>[`c3c49fa`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/c3c49fa0d8f62155207784d1c5840655f9a424fa) — 2026-02-24 — Make FlagCheckpoint support ignore case (#108) | v0.1.0 (2025-06-24T10:52:37Z) | Low/medium pattern relevance |
| `UKGovernmentBEIS/aisi-sandboxing` | [`c9f2ea1`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c9f2ea1b2a190b92fc2b69a97c237f3a33ee6bee) — 2025-08-07 — Update README.md<br>[`c99dd02`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c99dd02f0664cbec0884dc730d8ac26e5ec6d132) — 2025-08-07 — Add files via upload<br>[`2dd7e4b`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/2dd7e4b4f44412a81b7ce4f62b34c1aa36b32c98) — 2025-08-06 — Add placeholder pdf<br>[`81dbfeb`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/81dbfebc0cd4c603979577eb3f4ab03d0386e832) — 2025-08-06 — First commit | not resolved (HTTP Error 404: Not Found) | Low immediate relevance |

## Package/dependency comparison

| Package | Local version | PyPI latest |
|---|---:|---:|
| `inspect-ai` | `0.3.225` | `0.3.281` |
| `inspect-evals` | `not installed` | `0.25.0` |

## ARCS watch themes

- Preserve provider refusal / stop metadata when Inspect or target providers expose it; keep provider-specific fields optional.
- Keep transcript handling robust for long-context or attachment-backed content rather than assuming all evidence is inline plain text.
- Treat scorer/assessor exceptions as explicit error or unknown outcomes, never as safe/pass defaults.
- Watch Inspect viewer/reporting changes for future ARCS evidence and rubric review panes.
- Keep browser/sandbox dependencies isolated behind optional extras until needed.

## Lightweight local verification

```text
$ .venv/bin/python -m pytest -q
status: PASS
........................................................................ [ 92%]
......                                                                   [100%]
78 passed in 0.92s

$ .venv/bin/ruff check src tests
status: PASS
All checks passed!

$ .venv/bin/arcs-tui --once
status: PASS
ARCS Operator Dashboard
Project root: .

Scenarios (1)
- companion_dependency_smoke: Companion dependency smoke test | risk=dependency_manipulation | user=lonely_adult | turns=4 | phases=4 | path=scenarios/companion_dependency_smoke.yaml

Reusable Actor Profiles (1)
- lonely_adult: Lonely adult dependency-pressure actor | user=lonely_adult | persona=Alex (adult) | path=actor_profiles/lonely_adult.yaml

Run Configs (1)
- smoke-safe: target=tester | roleplay=deterministic | assessor=keyword | scenario=scenarios/companion_dependency_smoke.yaml | path=configs/example_run.yaml
  run: .venv/bin/arcs --config configs/example_run.yaml
  transcript: runs/configured/smoke-safe-companion_dependency_smoke.jsonl

Next Actions
- Open a run config and launch a smoke run: .venv/bin/arcs --config configs/example_run.yaml
- Review scenario phases and rubric coverage before adding real browser targets.
- Use dedicated test accounts and ignored storage-state files for future browser targets.
- Keep YAML/JSON as the source of truth; the TUI is an operator layer over those files.
```

## Maintenance notes

This note was generated by `scripts/weekly_upstream_check.py`. The local cron wrapper writes logs to `logs/weekly_upstream_check.log` and commits/pushes dated notes when git has changes.
