# UK AISI / Inspect upstream GitHub check — 2026-09-28

Date/time checked: 2026-09-28T09:00:01+10:00

Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible, model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.

## Upstream repositories checked

| Repository | Latest commits observed | Latest release signal | ARCS relevance |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | [`c2b63a0`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/c2b63a0b0560f9c3b5b5230365e0a8fe08cd3df0) — 2026-09-26 — update changelog for release<br>[`83af93c`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/83af93c8ca8fd1addd739637c493b6b80dc669cf) — 2026-09-26 — extra headers/body on cli (#5582)<br>[`d35670c`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/d35670c877a2c540ad60d2baad337becd1712617) — 2026-09-26 — Google: token counting falls back to a local estimate when countTokens is unavailable (#5581)<br>[`c232fde`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/c232fdeb70a01ae7c6ee1f58d0abcf2d5a308da4) — 2026-09-26 — update changelog for release<br>[`63a3046`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/63a30463738aa9b09fa64faf588040ad3350a1dc) — 2026-09-26 — more anthropic reasoning (#5579) | not resolved (HTTP Error 404: Not Found) | High |
| `UKGovernmentBEIS/inspect_evals` | [`dbd3dd2`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/dbd3dd25e81d5f5fc4d19860b496a34176da6c61) — 2026-09-27 — fix(hle): register judge scorers on package import so the task loads from the registry (#2551)<br>[`8bae1f6`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/8bae1f63fa0596e1c93005c4b1d290eda8128a8b) — 2026-09-25 — Use inspect-evals-lint 0.8.0 (#2546)<br>[`41c72ea`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/41c72eaa2b807ce43f35fac6f3f399318adc7e9d) — 2026-09-25 — Release v0.22.0 (#2543)<br>[`054cad9`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/054cad9339c21b28c8163e63a45660a510465988) — 2026-09-25 — feat(utils): make filter_duplicate_ids acknowledgement optional with a deprecation warning (#2541)<br>[`b3ed58b`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/b3ed58b466156db8c76bbcf46764854810d73df8) — 2026-09-25 — refactor(bbh): exclude the two broken ruin_names rows by id, with the report (#2529) | v0.22.0 (2026-09-25T06:05:09Z) | Medium |
| `UKGovernmentBEIS/inspect_cyber` | [`7fc6927`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/7fc69273c692b21637ce0552298eb9a523e56499) — 2026-06-18 — Fix reached_checkpoints collapsing checkpoints with duplicate names (#114)<br>[`a909bd3`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/a909bd3940aaa3ab3c7f2f22b785b5ba79db5e9d) — 2026-05-28 — Don't complain about using target (#113)<br>[`89b95e0`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/89b95e05a096e95a5faa3e76ebb3eb6d890233fd) — 2026-04-23 — Ordered checkpoints (#111)<br>[`cca8904`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/cca8904b76c984324b639f51c607ebefc1461fc6) — 2026-04-09 — Add per-checkpoint token usage and timing metadata to reached_checkpoints (#110)<br>[`c3c49fa`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/c3c49fa0d8f62155207784d1c5840655f9a424fa) — 2026-02-24 — Make FlagCheckpoint support ignore case (#108) | v0.1.0 (2025-06-24T10:52:37Z) | Low/medium pattern relevance |
| `UKGovernmentBEIS/aisi-sandboxing` | [`c9f2ea1`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c9f2ea1b2a190b92fc2b69a97c237f3a33ee6bee) — 2025-08-07 — Update README.md<br>[`c99dd02`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c99dd02f0664cbec0884dc730d8ac26e5ec6d132) — 2025-08-07 — Add files via upload<br>[`2dd7e4b`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/2dd7e4b4f44412a81b7ce4f62b34c1aa36b32c98) — 2025-08-06 — Add placeholder pdf<br>[`81dbfeb`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/81dbfebc0cd4c603979577eb3f4ab03d0386e832) — 2025-08-06 — First commit | not resolved (HTTP Error 404: Not Found) | Low immediate relevance |

## Package/dependency comparison

| Package | Local version | PyPI latest |
|---|---:|---:|
| `inspect-ai` | `0.3.225` | `0.3.271` |
| `inspect-evals` | `not installed` | `0.22.0` |

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
78 passed in 1.01s

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
