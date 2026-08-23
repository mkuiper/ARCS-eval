# UK AISI / Inspect upstream GitHub check — 2026-08-24

Date/time checked: 2026-08-24T09:00:02+10:00

Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible, model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.

## Upstream repositories checked

| Repository | Latest commits observed | Latest release signal | ARCS relevance |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | [`ebf4815`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/ebf4815ee260afcc8c34ad9d66e6f8d98a89e905) — 2026-08-23 — eval set: the capture manifest now records `max_samples` in `options` (#5014)<br>[`0db4111`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/0db4111e733334f88c5dcfa6eb635e0f846e7223) — 2026-08-23 — Sample limits now record why they fired (#5005)<br>[`5679e7e`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/5679e7e526c546c86fb8f831033eb0dcfc3dea64) — 2026-08-23 — eval set: an eval-set selection may now carry operational overrides for the worker (#5004)<br>[`499e615`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/499e6152e7b8fc8cbd8ac5283536572aa6e4ab17) — 2026-08-22 — eval set: protocol for running a selection of an eval set's tasks (#5000)<br>[`7b27d33`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/7b27d33774776f8ad3a00d5fbf0b3272a55cfd15) — 2026-08-21 — fix issues with running bridge examples on inspect ai (#4326) | not resolved (HTTP Error 404: Not Found) | High |
| `UKGovernmentBEIS/inspect_evals` | [`32b79a2`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/32b79a244f17ecf54fa1186d30f33dc10143c10f) — 2026-08-21 — Add per-check final summary to autolint --all-evals output (#2069)<br>[`5b83b15`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/5b83b154aa17f39a689dda2390a6df4b4a55b410) — 2026-08-21 — fix(cyberseceval): declare the judge-miss denominator shift across CyberSecEval 2/3/4 (#2210)<br>[`928e3dd`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/928e3dd92aa926f7dd1746c753e171f9f717c964) — 2026-08-21 — chore: adopt the grader_failed vocabulary in hle, anima, and moru (#2211)<br>[`d07c76c`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/d07c76cfe2335d7f275530ecc2cc370c2eacf577) — 2026-08-21 — fix(fortress): normalise lower-case judge grades before the majority vote (#2103)<br>[`c174327`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/c17432746b018184faab74aee2a9e127c6c9695e) — 2026-08-21 — fix(fortress): declare the benign judge-failure denominator change; harden the adversarial NaN route (#2209) | v0.18.0 (2026-08-20T14:38:06Z) | Medium |
| `UKGovernmentBEIS/inspect_cyber` | [`7fc6927`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/7fc69273c692b21637ce0552298eb9a523e56499) — 2026-06-18 — Fix reached_checkpoints collapsing checkpoints with duplicate names (#114)<br>[`a909bd3`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/a909bd3940aaa3ab3c7f2f22b785b5ba79db5e9d) — 2026-05-28 — Don't complain about using target (#113)<br>[`89b95e0`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/89b95e05a096e95a5faa3e76ebb3eb6d890233fd) — 2026-04-23 — Ordered checkpoints (#111)<br>[`cca8904`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/cca8904b76c984324b639f51c607ebefc1461fc6) — 2026-04-09 — Add per-checkpoint token usage and timing metadata to reached_checkpoints (#110)<br>[`c3c49fa`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/c3c49fa0d8f62155207784d1c5840655f9a424fa) — 2026-02-24 — Make FlagCheckpoint support ignore case (#108) | v0.1.0 (2025-06-24T10:52:37Z) | Low/medium pattern relevance |
| `UKGovernmentBEIS/aisi-sandboxing` | [`c9f2ea1`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c9f2ea1b2a190b92fc2b69a97c237f3a33ee6bee) — 2025-08-07 — Update README.md<br>[`c99dd02`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c99dd02f0664cbec0884dc730d8ac26e5ec6d132) — 2025-08-07 — Add files via upload<br>[`2dd7e4b`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/2dd7e4b4f44412a81b7ce4f62b34c1aa36b32c98) — 2025-08-06 — Add placeholder pdf<br>[`81dbfeb`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/81dbfebc0cd4c603979577eb3f4ab03d0386e832) — 2025-08-06 — First commit | not resolved (HTTP Error 404: Not Found) | Low immediate relevance |

## Package/dependency comparison

| Package | Local version | PyPI latest |
|---|---:|---:|
| `inspect-ai` | `0.3.225` | `0.3.260` |
| `inspect-evals` | `not installed` | `0.18.0` |

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
