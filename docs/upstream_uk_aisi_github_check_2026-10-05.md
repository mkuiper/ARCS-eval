# UK AISI / Inspect upstream GitHub check — 2026-10-05

Date/time checked: 2026-10-05T09:00:01+11:00

Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible, model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.

## Upstream repositories checked

| Repository | Latest commits observed | Latest release signal | ARCS relevance |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | [`1b46bb3`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/1b46bb351d7a78516e334503c585843ef60ad17c) — 2026-10-04 — Fix mypy arg-type errors on wrap model validators with mcp 2.3.0 (#5680)<br>[`9f6accd`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/9f6accda8dce5ccd754e6be1a22fbcee96042e82) — 2026-10-04 — Fix live sample reads occasionally showing model calls with empty inputs (#5625)<br>[`e403881`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/e40388168baabc62f1a2b3a41409e7daca64bac6) — 2026-10-04 — fix: omit unsupported Nova reasoning configuration (#5562)<br>[`0cdb361`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/0cdb361f907172d631766f890b70a71107687c69) — 2026-10-04 — docs: list OpenShell Sandbox on the extensions page (#5623)<br>[`241b01d`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/241b01d6caaadd6f30ad6be5b4ecc9cc549e574c) — 2026-10-04 — Correct the max_batches default in the batching options table (#5630) | not resolved (HTTP Error 404: Not Found) | High |
| `UKGovernmentBEIS/inspect_evals` | [`0dacad3`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/0dacad3c3bacfb50308de94eb8b8f9e368cfe30c) — 2026-10-02 — fix(actions): Update the Pangram labeller (#2615)<br>[`54cdce5`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/54cdce533ca420b59bebf7f907214d8b5fcd3bb6) — 2026-10-02 — docs(lint): readable filter text in the dark theme (#2616)<br>[`bd59dd3`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/bd59dd3b48974ad2e91219a6ceed41011e201163) — 2026-10-02 — Prepare release v0.23.0 (#2612)<br>[`d291bbf`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/d291bbfe8dcbb2f34c61158080a0f115a62237cd) — 2026-10-02 — Update PR process: require authors be on the contributors list or be assigned to an issue (#2606)<br>[`190dfa2`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/190dfa27bc2e9b3e966ea6e8a682626d55b513c0) — 2026-10-01 — feat(utils): accept predicate, extract_code_blocks and parser fixes for extract_code_block (#2609) | v0.23.0 (2026-10-02T06:20:01Z) | Medium |
| `UKGovernmentBEIS/inspect_cyber` | [`7fc6927`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/7fc69273c692b21637ce0552298eb9a523e56499) — 2026-06-18 — Fix reached_checkpoints collapsing checkpoints with duplicate names (#114)<br>[`a909bd3`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/a909bd3940aaa3ab3c7f2f22b785b5ba79db5e9d) — 2026-05-28 — Don't complain about using target (#113)<br>[`89b95e0`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/89b95e05a096e95a5faa3e76ebb3eb6d890233fd) — 2026-04-23 — Ordered checkpoints (#111)<br>[`cca8904`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/cca8904b76c984324b639f51c607ebefc1461fc6) — 2026-04-09 — Add per-checkpoint token usage and timing metadata to reached_checkpoints (#110)<br>[`c3c49fa`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/c3c49fa0d8f62155207784d1c5840655f9a424fa) — 2026-02-24 — Make FlagCheckpoint support ignore case (#108) | v0.1.0 (2025-06-24T10:52:37Z) | Low/medium pattern relevance |
| `UKGovernmentBEIS/aisi-sandboxing` | [`c9f2ea1`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c9f2ea1b2a190b92fc2b69a97c237f3a33ee6bee) — 2025-08-07 — Update README.md<br>[`c99dd02`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c99dd02f0664cbec0884dc730d8ac26e5ec6d132) — 2025-08-07 — Add files via upload<br>[`2dd7e4b`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/2dd7e4b4f44412a81b7ce4f62b34c1aa36b32c98) — 2025-08-06 — Add placeholder pdf<br>[`81dbfeb`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/81dbfebc0cd4c603979577eb3f4ab03d0386e832) — 2025-08-06 — First commit | not resolved (HTTP Error 404: Not Found) | Low immediate relevance |

## Package/dependency comparison

| Package | Local version | PyPI latest |
|---|---:|---:|
| `inspect-ai` | `0.3.225` | `0.3.276` |
| `inspect-evals` | `not installed` | `0.23.0` |

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
