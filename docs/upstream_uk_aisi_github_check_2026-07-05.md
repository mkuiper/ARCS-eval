# UK AISI / Inspect upstream GitHub check — 2026-07-05

Date/time checked: 2026-07-05T13:43:28+10:00

Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible, model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.

## Upstream repositories checked

| Repository | Latest commits observed | Latest release signal | ARCS relevance |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | [`64e0ff0`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/64e0ff05d46c3d337b54ee6570192397b47be298) — 2026-07-02 — Merge pull request #4406 from anxkhn/fix/handle-empty-id-in-as-html-id-to-avoid<br>[`b1fe120`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/b1fe120a971273926b350e2f3b6e365ce76c7922) — 2026-07-02 — Merge remote-tracking branch 'origin/main' into fix/handle-empty-id-in-as-html-id-to-avoid<br>[`a29a8f3`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/a29a8f3e58ebb0599a6e514821fd72181a8a3594) — 2026-07-02 — perf(model): make `stable_message_ids` linear per turn (#4407)<br>[`26395f3`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/26395f389f0d7435e343aa835e66cb7ae8cad71c) — 2026-07-01 — Merge pull request #4378 from ericwinsor-aisi/fix/eval-retry-zero-max-retries<br>[`94a0a54`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/94a0a542ab1a9c09d9f1263db97a9eba5b92a5cc) — 2026-07-01 — Merge branch 'main' into fix/eval-retry-zero-max-retries | not resolved (HTTP Error 404: Not Found) | High |
| `UKGovernmentBEIS/inspect_evals` | [`a595329`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/a595329b9ca5883f4cc065d5278b471cb2c9089e) — 2026-07-03 — Register submission: MANTA: Multi-Turn Adversarial Benchmark for Animal Welfare Reasoning (#1867)<br>[`d229c08`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/d229c0898a1c12ec68048670cd78aa2be213c828) — 2026-07-03 — feat(readme_generation): wrap parameter type annotations in backticks (#1884)<br>[`562daf3`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/562daf3ca269f4f3d08f807e3a9035543f0f5d71) — 2026-07-02 — fix(xstest): bind scoring to the grader's final GRADE verdict (#1875)<br>[`a004f40`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/a004f404c9728822596172ee732405d0f36457a3) — 2026-07-02 — Fix AgentHarm semantic judge metadata serialization (#1862)<br>[`97c99f5`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/97c99f5f6507fc5d1449fe3247f267d591f64350) — 2026-07-02 — Prepare release v0.14.3 (#1883) | v0.14.3 (2026-07-02T17:39:23Z) | Medium |
| `UKGovernmentBEIS/inspect_cyber` | [`7fc6927`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/7fc69273c692b21637ce0552298eb9a523e56499) — 2026-06-18 — Fix reached_checkpoints collapsing checkpoints with duplicate names (#114)<br>[`a909bd3`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/a909bd3940aaa3ab3c7f2f22b785b5ba79db5e9d) — 2026-05-28 — Don't complain about using target (#113)<br>[`89b95e0`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/89b95e05a096e95a5faa3e76ebb3eb6d890233fd) — 2026-04-23 — Ordered checkpoints (#111)<br>[`cca8904`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/cca8904b76c984324b639f51c607ebefc1461fc6) — 2026-04-09 — Add per-checkpoint token usage and timing metadata to reached_checkpoints (#110)<br>[`c3c49fa`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/c3c49fa0d8f62155207784d1c5840655f9a424fa) — 2026-02-24 — Make FlagCheckpoint support ignore case (#108) | v0.1.0 (2025-06-24T10:52:37Z) | Low/medium pattern relevance |
| `UKGovernmentBEIS/aisi-sandboxing` | [`c9f2ea1`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c9f2ea1b2a190b92fc2b69a97c237f3a33ee6bee) — 2025-08-07 — Update README.md<br>[`c99dd02`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c99dd02f0664cbec0884dc730d8ac26e5ec6d132) — 2025-08-07 — Add files via upload<br>[`2dd7e4b`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/2dd7e4b4f44412a81b7ce4f62b34c1aa36b32c98) — 2025-08-06 — Add placeholder pdf<br>[`81dbfeb`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/81dbfebc0cd4c603979577eb3f4ab03d0386e832) — 2025-08-06 — First commit | not resolved (HTTP Error 404: Not Found) | Low immediate relevance |

## Package/dependency comparison

| Package | Local version | PyPI latest |
|---|---:|---:|
| `inspect-ai` | `0.3.225` | `0.3.244` |
| `inspect-evals` | `not installed` | `0.14.3` |

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
78 passed in 0.38s

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
