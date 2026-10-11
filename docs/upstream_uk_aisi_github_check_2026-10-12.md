# UK AISI / Inspect upstream GitHub check — 2026-10-12

Date/time checked: 2026-10-12T09:00:01+11:00

Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible, model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.

## Upstream repositories checked

| Repository | Latest commits observed | Latest release signal | ARCS relevance |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | [`a1dbea8`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/a1dbea8db3cc85e04ff532760d0eaaeb64df6d3a) — 2026-10-10 — Give sentinel monitors the task and sample descriptions (#5784)<br>[`e016b7c`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/e016b7c583465d8c3680fb22683d014071fd4f78) — 2026-10-10 — docs: replace CHANGELOG entry steps with PR-title guidance and correct the code-fence advice (#5805)<br>[`db18773`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/db1877352ab75446783d6c9b1c986aa3b76e4d6f) — 2026-10-10 — Install inspect_sentinel from PyPI (#5810)<br>[`697fde9`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/697fde94e2bb08fcba1b3bad65d8c752e1812111) — 2026-10-09 — ci: generate the CHANGELOG with Release Please (#5804)<br>[`f95ab3d`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/f95ab3d4e9c7692e2ce6830e78b7ef184ba8e6f1) — 2026-10-09 — ci: cut releases from a Release Please PR and publish them from GitHub Actions (#5789) | 0.3.278 (2026-10-09T16:49:48Z) | High |
| `UKGovernmentBEIS/inspect_evals` | [`eb5383e`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/eb5383efecd8ac6d23fd276757b811f3db05a1f5) — 2026-10-09 — fix(lab-bench): seed answer choice shuffling (#2406)<br>[`064b588`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/064b58829166a4c6c67967ec168847daae2afeb2) — 2026-10-09 — fix(sad): use fixed default seed (#2405)<br>[`d7d083c`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/d7d083c68c972a066ba4e0963dc22f12c01594f2) — 2026-10-09 — fix(truthfulqa): seed answer choice shuffling (#2404)<br>[`c8433d3`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/c8433d321d30c996a4c2345d6d7107f2deff42a5) — 2026-10-09 — fix(fortress): stop a wholly ungraded group from becoming genuine zeros (#2446)<br>[`a956d03`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/a956d0305adc91c8f97474fc314a22a5d30c6ca3) — 2026-10-09 — Use the task's own message_limit option in the gdm_self_reasoning README (#2482) | v0.24.0 (2026-10-08T21:56:33Z) | Medium |
| `UKGovernmentBEIS/inspect_cyber` | [`7fc6927`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/7fc69273c692b21637ce0552298eb9a523e56499) — 2026-06-18 — Fix reached_checkpoints collapsing checkpoints with duplicate names (#114)<br>[`a909bd3`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/a909bd3940aaa3ab3c7f2f22b785b5ba79db5e9d) — 2026-05-28 — Don't complain about using target (#113)<br>[`89b95e0`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/89b95e05a096e95a5faa3e76ebb3eb6d890233fd) — 2026-04-23 — Ordered checkpoints (#111)<br>[`cca8904`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/cca8904b76c984324b639f51c607ebefc1461fc6) — 2026-04-09 — Add per-checkpoint token usage and timing metadata to reached_checkpoints (#110)<br>[`c3c49fa`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/c3c49fa0d8f62155207784d1c5840655f9a424fa) — 2026-02-24 — Make FlagCheckpoint support ignore case (#108) | v0.1.0 (2025-06-24T10:52:37Z) | Low/medium pattern relevance |
| `UKGovernmentBEIS/aisi-sandboxing` | [`c9f2ea1`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c9f2ea1b2a190b92fc2b69a97c237f3a33ee6bee) — 2025-08-07 — Update README.md<br>[`c99dd02`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c99dd02f0664cbec0884dc730d8ac26e5ec6d132) — 2025-08-07 — Add files via upload<br>[`2dd7e4b`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/2dd7e4b4f44412a81b7ce4f62b34c1aa36b32c98) — 2025-08-06 — Add placeholder pdf<br>[`81dbfeb`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/81dbfebc0cd4c603979577eb3f4ab03d0386e832) — 2025-08-06 — First commit | not resolved (HTTP Error 404: Not Found) | Low immediate relevance |

## Package/dependency comparison

| Package | Local version | PyPI latest |
|---|---:|---:|
| `inspect-ai` | `0.3.225` | `0.3.278` |
| `inspect-evals` | `not installed` | `0.24.0` |

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
