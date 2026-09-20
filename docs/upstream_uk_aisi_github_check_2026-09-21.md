# UK AISI / Inspect upstream GitHub check — 2026-09-21

Date/time checked: 2026-09-21T09:00:01+10:00

Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible, model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.

## Upstream repositories checked

| Repository | Latest commits observed | Latest release signal | ARCS relevance |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | [`ec4dfc6`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/ec4dfc6953784dc45b79de3147530c89868c6e26) — 2026-09-19 — update changelog for release<br>[`f4f1e4a`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/f4f1e4a2d2f300fe25767d33192ade6b3ac9c6a1) — 2026-09-19 — Preserve originating scorer in interim-scoring control response (#5483)<br>[`e4b8ad5`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/e4b8ad59d8468d41cd5df844ec7100c7a1569cb1) — 2026-09-18 — Fix `inspect score --scorer pkg/name` failing to resolve `@scanner` functions (#5466)<br>[`615e284`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/615e284c12ad658415e5fb86509a32f00a238b6a) — 2026-09-17 — update changelog for release<br>[`7fdb13a`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/7fdb13ad641aff64008c2412f507fbd5cdb20104) — 2026-09-17 — Stop denying bridged host tool calls under an approval policy (stopgap until #5428) (#5458) | not resolved (HTTP Error 404: Not Found) | High |
| `UKGovernmentBEIS/inspect_evals` | [`d26e7df`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/d26e7df8494d4ba8ff468bb50c11aa625f710e95) — 2026-09-19 — Use inspect-evals-lint 0.3.1: rule codes, per-site findings, exclude and per-file-ignores (#2478)<br>[`b91aa24`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/b91aa24648f4ea151f9ac443a3459fdf9ebba224) — 2026-09-18 — fix(mind2web_sc): load full 200 samples and disambiguate sample ids (#2390)<br>[`8ddfea1`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/8ddfea18ea7dabbac4d230b1fb0e7139655afb6f) — 2026-09-18 — Add a shared sandbox image check helper, with DS-1000 as the first adopter (#2472)<br>[`8b9b97a`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/8b9b97aa0db04d03e1e64d0daa4a23a0dd56c4d2) — 2026-09-18 — KernelBench: add a repeatable GPU sandbox image check task (#2469)<br>[`7bd0136`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/7bd01361eb9a7231d5f8b136ce4ff2d504b924ea) — 2026-09-18 — eval.yaml: add metadata.requires (internet, gpu) and per-task kind (#2470) | v0.21.0 (2026-09-17T20:57:49Z) | Medium |
| `UKGovernmentBEIS/inspect_cyber` | [`7fc6927`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/7fc69273c692b21637ce0552298eb9a523e56499) — 2026-06-18 — Fix reached_checkpoints collapsing checkpoints with duplicate names (#114)<br>[`a909bd3`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/a909bd3940aaa3ab3c7f2f22b785b5ba79db5e9d) — 2026-05-28 — Don't complain about using target (#113)<br>[`89b95e0`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/89b95e05a096e95a5faa3e76ebb3eb6d890233fd) — 2026-04-23 — Ordered checkpoints (#111)<br>[`cca8904`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/cca8904b76c984324b639f51c607ebefc1461fc6) — 2026-04-09 — Add per-checkpoint token usage and timing metadata to reached_checkpoints (#110)<br>[`c3c49fa`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/c3c49fa0d8f62155207784d1c5840655f9a424fa) — 2026-02-24 — Make FlagCheckpoint support ignore case (#108) | v0.1.0 (2025-06-24T10:52:37Z) | Low/medium pattern relevance |
| `UKGovernmentBEIS/aisi-sandboxing` | [`c9f2ea1`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c9f2ea1b2a190b92fc2b69a97c237f3a33ee6bee) — 2025-08-07 — Update README.md<br>[`c99dd02`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c99dd02f0664cbec0884dc730d8ac26e5ec6d132) — 2025-08-07 — Add files via upload<br>[`2dd7e4b`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/2dd7e4b4f44412a81b7ce4f62b34c1aa36b32c98) — 2025-08-06 — Add placeholder pdf<br>[`81dbfeb`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/81dbfebc0cd4c603979577eb3f4ab03d0386e832) — 2025-08-06 — First commit | not resolved (HTTP Error 404: Not Found) | Low immediate relevance |

## Package/dependency comparison

| Package | Local version | PyPI latest |
|---|---:|---:|
| `inspect-ai` | `0.3.225` | `0.3.266` |
| `inspect-evals` | `not installed` | `0.21.0` |

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
78 passed in 0.97s

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
