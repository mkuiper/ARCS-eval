# UK AISI / Inspect upstream GitHub check — 2026-08-03

Date/time checked: 2026-08-03T09:38:21+10:00

Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible, model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.

## Upstream repositories checked

| Repository | Latest commits observed | Latest release signal | ARCS relevance |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | [`1ea01a9`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/1ea01a9e1b3c94db3cdf93ce5583ffebf86e159f) — 2026-07-30 — fix(analysis): skip all-NA score groups in frontier() to avoid idxmax crash (#4610)<br>[`2882359`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/2882359ee23634e91c80b0723318f084c8043641) — 2026-07-30 — fix: preserve oversized sandbox JSON-RPC responses (#4371)<br>[`1c1c663`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/1c1c663fecda788f22ac5db645fa570e9905701a) — 2026-07-30 — Add `inspect ctl sample requeue` to re-run errored/cancelled samples in a live eval (#4649)<br>[`448d587`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/448d5878bb6d17d25788531d7a0caa72c0ce0113) — 2026-07-30 — Don't retry pytest.skip()/xfail() in flaky_retry (#4702)<br>[`cda771a`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/cda771a5ba02417c54c98abfb014afe5c802bd98) — 2026-07-30 — Fix decorators return-annotation on Python 3.14 (#4554) | not resolved (HTTP Error 404: Not Found) | High |
| `UKGovernmentBEIS/inspect_evals` | [`6a35510`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/6a35510e530f236fd1dbcd9df888f01937c8494a) — 2026-07-31 — Register submission: PatchEval (verified dockerized subset) (closes #2028) (#2029)<br>[`35f8a0b`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/35f8a0be7ad11980f30f1483f50ca50821c308e7) — 2026-07-31 — fix(tests): eliminate Dockerfile race in gdm_intercode_ctf and mark slow test (#2037)<br>[`8c5c2d9`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/8c5c2d9287a57b5dc0a0af387c151d5b18e92306) — 2026-07-31 — Register submission: BrokenMath: Sycophancy in LLM Theorem Proving (#2002)<br>[`5d87c25`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/5d87c25801402571f5c458cd281202fd7f9684a2) — 2026-07-31 — Add WebSearch to allowed tools in claude-fix-tests workflow (#1919)<br>[`45449f7`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/45449f77844264506140eaa34200941243013873) — 2026-07-31 — Register submission: Manager Coercion Benchmark (MCB) (closes #1970) (#1971) | v0.16.0 (2026-07-24T05:13:08Z) | Medium |
| `UKGovernmentBEIS/inspect_cyber` | [`7fc6927`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/7fc69273c692b21637ce0552298eb9a523e56499) — 2026-06-18 — Fix reached_checkpoints collapsing checkpoints with duplicate names (#114)<br>[`a909bd3`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/a909bd3940aaa3ab3c7f2f22b785b5ba79db5e9d) — 2026-05-28 — Don't complain about using target (#113)<br>[`89b95e0`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/89b95e05a096e95a5faa3e76ebb3eb6d890233fd) — 2026-04-23 — Ordered checkpoints (#111)<br>[`cca8904`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/cca8904b76c984324b639f51c607ebefc1461fc6) — 2026-04-09 — Add per-checkpoint token usage and timing metadata to reached_checkpoints (#110)<br>[`c3c49fa`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/c3c49fa0d8f62155207784d1c5840655f9a424fa) — 2026-02-24 — Make FlagCheckpoint support ignore case (#108) | v0.1.0 (2025-06-24T10:52:37Z) | Low/medium pattern relevance |
| `UKGovernmentBEIS/aisi-sandboxing` | [`c9f2ea1`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c9f2ea1b2a190b92fc2b69a97c237f3a33ee6bee) — 2025-08-07 — Update README.md<br>[`c99dd02`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c99dd02f0664cbec0884dc730d8ac26e5ec6d132) — 2025-08-07 — Add files via upload<br>[`2dd7e4b`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/2dd7e4b4f44412a81b7ce4f62b34c1aa36b32c98) — 2025-08-06 — Add placeholder pdf<br>[`81dbfeb`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/81dbfebc0cd4c603979577eb3f4ab03d0386e832) — 2025-08-06 — First commit | not resolved (HTTP Error 404: Not Found) | Low immediate relevance |

## Package/dependency comparison

| Package | Local version | PyPI latest |
|---|---:|---:|
| `inspect-ai` | `0.3.225` | `0.3.251` |
| `inspect-evals` | `not installed` | `0.16.0` |

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
78 passed in 0.96s

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
