# UK AISI / Inspect upstream GitHub check — 2026-11-16

Date/time checked: 2026-11-16T09:20:41+11:00

Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible, model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.

## Upstream repositories checked

| Repository | Latest commits observed | Latest release signal | ARCS relevance |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | [`59c1340`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/59c1340741ba863fb0d79287f66420e5dd782480) — 2026-11-15 — docs: use a current Gemini model in models.qmd examples (#6555)<br>[`19f92c0`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/19f92c0c28f88abe1acb155bb2f0279dee445f99) — 2026-11-15 — docs: list anchorset on the extensions page (#6399)<br>[`92fa034`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/92fa03413a6228b03388559e0a46499b7d743798) — 2026-11-15 — fix: OpenAI native compaction crashes when a user message contains an image or file (#6436)<br>[`ecbb075`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/ecbb07547dfaa61774b7b9994da23b33bf68338d) — 2026-11-15 — docs: list Scorio's Bayes@N extension (#6430)<br>[`a3b8090`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/a3b8090965f96f27f51dfdd00bf99d2c42cda5a6) — 2026-11-15 — fix: samples_df no longer uses pandas' deprecated drop_duplicates(inplace=True) (#6383) | 0.3.290 (2026-11-14T21:14:27Z) | High |
| `UKGovernmentBEIS/inspect_evals` | [`a68dade`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/a68dade7efb803ef50c8442d3f16264b293d1414) — 2026-11-13 — feat(ifevalcode): use the shared extract_code_block helper (3-A) (#2877)<br>[`a4205c2`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/a4205c238a40de36204c487fa38d7720bc1085cf) — 2026-11-13 — Prepare release v0.29.0 (#2869)<br>[`eca0083`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/eca00832fd82f22e28590a60da4fcd5dee646134) — 2026-11-13 — fix(utils): hash sandbox dependency files with LF line endings (#2879)<br>[`10ee63f`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/10ee63ffcb7cb362c1604ad905e90d3d196c5f5f) — 2026-11-13 — fix(tools): print unions the same way on every Python version in generated READMEs (#2873)<br>[`ea25f73`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/ea25f73c14d0159e2791d4cfec129ea03c2f5826) — 2026-11-13 — fix(swe_lancer): make num_correct and num_incorrect plain functions so they work on Python 3.14 (#2874) | v0.29.0 (2026-11-13T05:37:32Z) | Medium |
| `UKGovernmentBEIS/inspect_cyber` | [`7fc6927`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/7fc69273c692b21637ce0552298eb9a523e56499) — 2026-06-18 — Fix reached_checkpoints collapsing checkpoints with duplicate names (#114)<br>[`a909bd3`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/a909bd3940aaa3ab3c7f2f22b785b5ba79db5e9d) — 2026-05-28 — Don't complain about using target (#113)<br>[`89b95e0`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/89b95e05a096e95a5faa3e76ebb3eb6d890233fd) — 2026-04-23 — Ordered checkpoints (#111)<br>[`cca8904`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/cca8904b76c984324b639f51c607ebefc1461fc6) — 2026-04-09 — Add per-checkpoint token usage and timing metadata to reached_checkpoints (#110)<br>[`c3c49fa`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/c3c49fa0d8f62155207784d1c5840655f9a424fa) — 2026-02-24 — Make FlagCheckpoint support ignore case (#108) | v0.1.0 (2025-06-24T10:52:37Z) | Low/medium pattern relevance |
| `UKGovernmentBEIS/aisi-sandboxing` | [`c9f2ea1`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c9f2ea1b2a190b92fc2b69a97c237f3a33ee6bee) — 2025-08-07 — Update README.md<br>[`c99dd02`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c99dd02f0664cbec0884dc730d8ac26e5ec6d132) — 2025-08-07 — Add files via upload<br>[`2dd7e4b`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/2dd7e4b4f44412a81b7ce4f62b34c1aa36b32c98) — 2025-08-06 — Add placeholder pdf<br>[`81dbfeb`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/81dbfebc0cd4c603979577eb3f4ab03d0386e832) — 2025-08-06 — First commit | not resolved (HTTP Error 404: Not Found) | Low immediate relevance |

## Package/dependency comparison

| Package | Local version | PyPI latest |
|---|---:|---:|
| `inspect-ai` | `0.3.225` | `0.3.290` |
| `inspect-evals` | `not installed` | `0.29.0` |

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
78 passed in 0.50s

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
