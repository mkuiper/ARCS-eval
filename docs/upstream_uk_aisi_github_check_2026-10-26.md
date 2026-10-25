# UK AISI / Inspect upstream GitHub check — 2026-10-26

Date/time checked: 2026-10-26T09:00:01+11:00

Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible, model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.

## Upstream repositories checked

| Repository | Latest commits observed | Latest release signal | ARCS relevance |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | [`d1536ea`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/d1536eae98d7b8b9364c052f0e6d3de988e1aac9) — 2026-10-25 — chore(main): release 0.3.285 (#6074)<br>[`e37ce2f`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/e37ce2fd3533ba53221d751e4e4eced74d4869b3) — 2026-10-25 — feat: viewer Terminals tab for recorded terminal sessions and a merged Info tab (#6079)<br>[`641b871`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/641b8712f7d4e18c4813c261068e2a88022fb553) — 2026-10-25 — fix: .eval reads with exclude_fields failing on large float literals (#6045)<br>[`3dcd2de`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/3dcd2ded36085d7c068d966a8d3118563296916e) — 2026-10-25 — fix: agent bridge returns non-beta Anthropic usage to beta.messages calls with anthropic 2.3 (#6061)<br>[`fc712e2`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/fc712e22a96e12ef2a4b66eed9c8cab318a0f2e6) — 2026-10-25 — chore(main): release 0.3.284 (#6022) | 0.3.285 (2026-10-25T14:27:46Z) | High |
| `UKGovernmentBEIS/inspect_evals` | [`cac63f6`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/cac63f6d942ff63c9a0ac1185a026123e62970f4) — 2026-10-23 — Release v0.26.0 (#2741)<br>[`594aecd`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/594aecda31eda2fb2b592ba685d8771454f8dc70) — 2026-10-23 — fix(infinite_bench): Math.Calc offset correction skipped for proxied GPT models (#1993)<br>[`ca8977a`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/ca8977a7f66c312c8acbb371492c85cdb4bbce1b) — 2026-10-23 — fix: pass usedforsecurity=False to hashlib.md5 so evals load on FIPS hosts (#2743)<br>[`c5c7031`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/c5c7031b1b51beae450698eae3ce0c0cc3ff5f1a) — 2026-10-23 — chore(deps): bump inspect-ai to 0.3.283 and anthropic to 2.1.0 in lock (#2744)<br>[`6a96ec5`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/6a96ec57a8f00997e7d7b10364031bbae530bbb0) — 2026-10-21 — AssistantBench: replace deprecated browser with Playwright MCP (#2726) | v0.26.0 (2026-10-23T08:49:37Z) | Medium |
| `UKGovernmentBEIS/inspect_cyber` | [`7fc6927`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/7fc69273c692b21637ce0552298eb9a523e56499) — 2026-06-18 — Fix reached_checkpoints collapsing checkpoints with duplicate names (#114)<br>[`a909bd3`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/a909bd3940aaa3ab3c7f2f22b785b5ba79db5e9d) — 2026-05-28 — Don't complain about using target (#113)<br>[`89b95e0`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/89b95e05a096e95a5faa3e76ebb3eb6d890233fd) — 2026-04-23 — Ordered checkpoints (#111)<br>[`cca8904`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/cca8904b76c984324b639f51c607ebefc1461fc6) — 2026-04-09 — Add per-checkpoint token usage and timing metadata to reached_checkpoints (#110)<br>[`c3c49fa`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/c3c49fa0d8f62155207784d1c5840655f9a424fa) — 2026-02-24 — Make FlagCheckpoint support ignore case (#108) | v0.1.0 (2025-06-24T10:52:37Z) | Low/medium pattern relevance |
| `UKGovernmentBEIS/aisi-sandboxing` | [`c9f2ea1`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c9f2ea1b2a190b92fc2b69a97c237f3a33ee6bee) — 2025-08-07 — Update README.md<br>[`c99dd02`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c99dd02f0664cbec0884dc730d8ac26e5ec6d132) — 2025-08-07 — Add files via upload<br>[`2dd7e4b`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/2dd7e4b4f44412a81b7ce4f62b34c1aa36b32c98) — 2025-08-06 — Add placeholder pdf<br>[`81dbfeb`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/81dbfebc0cd4c603979577eb3f4ab03d0386e832) — 2025-08-06 — First commit | not resolved (HTTP Error 404: Not Found) | Low immediate relevance |

## Package/dependency comparison

| Package | Local version | PyPI latest |
|---|---:|---:|
| `inspect-ai` | `0.3.225` | `0.3.285` |
| `inspect-evals` | `not installed` | `0.26.0` |

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
