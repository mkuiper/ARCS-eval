# UK AISI / Inspect upstream GitHub check — 2026-09-14

Date/time checked: 2026-09-14T09:00:01+10:00

Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible, model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.

## Upstream repositories checked

| Repository | Latest commits observed | Latest release signal | ARCS relevance |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | [`f6719bb`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/f6719bbfa9038a4ff9214035b70c9db772c40699) — 2026-09-13 — Load UTF-8 CSV datasets with or without a BOM (#5361)<br>[`3f025fc`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/3f025fc28b1a379de46821c278aa9f46066220c8) — 2026-09-13 — fix(google): omit placeholder API key from ADC requests (#5349)<br>[`05c3a06`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/05c3a06c84ccaec1ba4c998fca295060748ebade) — 2026-09-13 — Distinguish empty and unparseable multiple-choice answers from wrong ones (#5333)<br>[`fc7fa81`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/fc7fa811764ac1cb68186e2a42f4084070f9da94) — 2026-09-13 — update tool name and reference in tool documentation from 'update plan' to 'todo write' (#5326)<br>[`75b7f7d`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/75b7f7ddfd9ee528610e51ed9da234f0e5687a67) — 2026-09-13 — Silence httpx2 request logging at info level (#5321) | not resolved (HTTP Error 404: Not Found) | High |
| `UKGovernmentBEIS/inspect_evals` | [`360484a`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/360484a06383f9260279938262d78ed646ddbca1) — 2026-09-11 — Prepare release v0.20.0 (#2410)<br>[`acad4ca`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/acad4cace18de33931aba98d0145a9ef31b2bda3) — 2026-09-11 — fix(mask): bind loop variable in dataset sample_fields closure (#2155)<br>[`e5bcf20`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/e5bcf2007eb7d83f7a0f7db60f19119ad93e685c) — 2026-09-11 — chore(deps): bump the actions group across 1 directory with 5 updates (#2383)<br>[`a3837b5`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/a3837b57f40805efb4064734fbad7f93f5291c38) — 2026-09-10 — Switch to Fable 5.1 for reviews (from Opus 5) (#2409)<br>[`47a0725`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/47a0725a3eb630c94209ea2aebbcf420beee79ca) — 2026-09-10 — ci: streamline Claude Code review output (#2402) | v0.20.0 (2026-09-11T14:42:51Z) | Medium |
| `UKGovernmentBEIS/inspect_cyber` | [`7fc6927`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/7fc69273c692b21637ce0552298eb9a523e56499) — 2026-06-18 — Fix reached_checkpoints collapsing checkpoints with duplicate names (#114)<br>[`a909bd3`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/a909bd3940aaa3ab3c7f2f22b785b5ba79db5e9d) — 2026-05-28 — Don't complain about using target (#113)<br>[`89b95e0`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/89b95e05a096e95a5faa3e76ebb3eb6d890233fd) — 2026-04-23 — Ordered checkpoints (#111)<br>[`cca8904`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/cca8904b76c984324b639f51c607ebefc1461fc6) — 2026-04-09 — Add per-checkpoint token usage and timing metadata to reached_checkpoints (#110)<br>[`c3c49fa`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/c3c49fa0d8f62155207784d1c5840655f9a424fa) — 2026-02-24 — Make FlagCheckpoint support ignore case (#108) | v0.1.0 (2025-06-24T10:52:37Z) | Low/medium pattern relevance |
| `UKGovernmentBEIS/aisi-sandboxing` | [`c9f2ea1`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c9f2ea1b2a190b92fc2b69a97c237f3a33ee6bee) — 2025-08-07 — Update README.md<br>[`c99dd02`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c99dd02f0664cbec0884dc730d8ac26e5ec6d132) — 2025-08-07 — Add files via upload<br>[`2dd7e4b`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/2dd7e4b4f44412a81b7ce4f62b34c1aa36b32c98) — 2025-08-06 — Add placeholder pdf<br>[`81dbfeb`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/81dbfebc0cd4c603979577eb3f4ab03d0386e832) — 2025-08-06 — First commit | not resolved (HTTP Error 404: Not Found) | Low immediate relevance |

## Package/dependency comparison

| Package | Local version | PyPI latest |
|---|---:|---:|
| `inspect-ai` | `0.3.225` | `0.3.263` |
| `inspect-evals` | `not installed` | `0.20.0` |

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
78 passed in 0.81s

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
