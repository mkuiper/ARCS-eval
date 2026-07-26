# UK AISI / Inspect upstream GitHub check — 2026-07-27

Date/time checked: 2026-07-27T09:00:01+10:00

Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible, model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.

## Upstream repositories checked

| Repository | Latest commits observed | Latest release signal | ARCS relevance |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | [`3e9a18f`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/3e9a18f4e7e17d7cf6aaa14b13026774ca747597) — 2026-07-22 — Viewer support for chunked sample storage (internal only, not yet enabled) (#4593)<br>[`78a76fe`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/78a76fea7e62532e8defb3c888fb74016cdf7099) — 2026-07-22 — build(deps): Bump the github-actions group across 1 directory with 3 updates (#4584)<br>[`1db2c38`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/1db2c38efc59f03225ba31ea6e3e5a3a121b237c) — 2026-07-22 — Add model info for Gemini 3.6 Flash and Gemini 3.5 Flash-Lite (#4592)<br>[`2238e69`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/2238e69022a0210cc721c97fc047772a46759e14) — 2026-07-22 — Add AGENTS.md; CLAUDE.md imports it (#4582)<br>[`2fc34e7`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/2fc34e7921ff6fc1c12f3b739a1ce0f6cac1dec9) — 2026-07-22 — docs(sandbox): note exec output-limit truncation is provider-dependent (#4506) | not resolved (HTTP Error 404: Not Found) | High |
| `UKGovernmentBEIS/inspect_evals` | [`99ef14c`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/99ef14c96efb4a4d36c344b313ca734074af88bf) — 2026-07-24 — fix(class_eval): add missing @pytest.mark.docker to test_task (#2009)<br>[`e1d6eb8`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/e1d6eb836e90bb6ab11bb39c3e9ca6f3225e4ae7) — 2026-07-24 — ci: enforce isolated eval lockfile freshness in pre-commit and checks (#1995)<br>[`4f24573`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/4f2457392e2e0be23679d106d455f7b66240c2fb) — 2026-07-24 — Register submission: ExploitBench: Capability Ladder Benchmark for LLM Cybersecurity Agents (V8 exploit development) (#1959)<br>[`3367d26`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/3367d26374083aa794600b9c06b0b4f76faad76d) — 2026-07-24 — Prepare release v0.16.0 (#2003)<br>[`0a668b5`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/0a668b55dbb493506daf2da0492f7e71a4c88b82) — 2026-07-24 — Register submission: Neural Activation Reading for Collusion Benchmark (NARCBench) -- Black-Box Monitor Variant (#1956) | v0.16.0 (2026-07-24T05:13:08Z) | Medium |
| `UKGovernmentBEIS/inspect_cyber` | [`7fc6927`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/7fc69273c692b21637ce0552298eb9a523e56499) — 2026-06-18 — Fix reached_checkpoints collapsing checkpoints with duplicate names (#114)<br>[`a909bd3`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/a909bd3940aaa3ab3c7f2f22b785b5ba79db5e9d) — 2026-05-28 — Don't complain about using target (#113)<br>[`89b95e0`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/89b95e05a096e95a5faa3e76ebb3eb6d890233fd) — 2026-04-23 — Ordered checkpoints (#111)<br>[`cca8904`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/cca8904b76c984324b639f51c607ebefc1461fc6) — 2026-04-09 — Add per-checkpoint token usage and timing metadata to reached_checkpoints (#110)<br>[`c3c49fa`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/c3c49fa0d8f62155207784d1c5840655f9a424fa) — 2026-02-24 — Make FlagCheckpoint support ignore case (#108) | v0.1.0 (2025-06-24T10:52:37Z) | Low/medium pattern relevance |
| `UKGovernmentBEIS/aisi-sandboxing` | [`c9f2ea1`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c9f2ea1b2a190b92fc2b69a97c237f3a33ee6bee) — 2025-08-07 — Update README.md<br>[`c99dd02`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c99dd02f0664cbec0884dc730d8ac26e5ec6d132) — 2025-08-07 — Add files via upload<br>[`2dd7e4b`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/2dd7e4b4f44412a81b7ce4f62b34c1aa36b32c98) — 2025-08-06 — Add placeholder pdf<br>[`81dbfeb`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/81dbfebc0cd4c603979577eb3f4ab03d0386e832) — 2025-08-06 — First commit | not resolved (HTTP Error 404: Not Found) | Low immediate relevance |

## Package/dependency comparison

| Package | Local version | PyPI latest |
|---|---:|---:|
| `inspect-ai` | `0.3.225` | `0.3.249` |
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
78 passed in 0.84s

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
