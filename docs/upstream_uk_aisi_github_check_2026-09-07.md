# UK AISI / Inspect upstream GitHub check — 2026-09-07

Date/time checked: 2026-09-07T09:00:01+10:00

Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible, model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.

## Upstream repositories checked

| Repository | Latest commits observed | Latest release signal | ARCS relevance |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | [`856f41f`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/856f41f19debe008756ec4c5831f0600c861c51a) — 2026-09-05 — fix(scorer): let shaped metrics own their empty-input shape (#5153)<br>[`7bd3148`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/7bd314869e00272a7cbaff3542e52ace5a87ca9a) — 2026-09-05 — Add Corrlog for Inspect to extensions listing (#5204)<br>[`cc62e53`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/cc62e53d63577940ead2b0f0286678e6f014ca0a) — 2026-09-05 — docs: fix duplicate words and typos in documentation (#5250)<br>[`4a89946`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/4a899463c34d1b4c576cb6d542528b6bbf7c0ed2) — 2026-09-05 — docs: fix dead anchors and stale link in design documents (#5252)<br>[`e3988a7`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/e3988a7d0e60f8222fbfa0ddee8d5086d2ed6e87) — 2026-09-05 — Fix flaky test: gate SIGINT on the solver reaching the pending resolution (#5251) | not resolved (HTTP Error 404: Not Found) | High |
| `UKGovernmentBEIS/inspect_evals` | [`ac481c7`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/ac481c7a7b4fb05d6befdfea59b47fc61b839a4f) — 2026-09-01 — docs: shorten duplicated Usage blocks on eval READMEs (#2320)<br>[`5c8626e`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/5c8626ed2c500f49e83d6141317c8e3f52513bec) — 2026-09-01 — fix: aime_scorer only checks literal last line, and mutates state.output.completion (#2025)<br>[`49738b6`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/49738b6412cf3215db7c9d3d4838fc58b6f422a2) — 2026-08-31 — test(cti_realm): one constant check that names the domain it fails on (#2328)<br>[`5089864`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/50898643a622887f51a82870b2e27b455f51ab5b) — 2026-08-31 — fix(changelog): normalise CHANGELOG.md so mdformat and markdownlint pass on main (#2330)<br>[`a3ec530`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/a3ec5306afae046c6199a0a81ce65c440634731f) — 2026-08-31 — Update REPO_CONTEXT.md (automated run #25) (#2325) | v0.19.0 (2026-08-31T03:55:17Z) | Medium |
| `UKGovernmentBEIS/inspect_cyber` | [`7fc6927`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/7fc69273c692b21637ce0552298eb9a523e56499) — 2026-06-18 — Fix reached_checkpoints collapsing checkpoints with duplicate names (#114)<br>[`a909bd3`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/a909bd3940aaa3ab3c7f2f22b785b5ba79db5e9d) — 2026-05-28 — Don't complain about using target (#113)<br>[`89b95e0`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/89b95e05a096e95a5faa3e76ebb3eb6d890233fd) — 2026-04-23 — Ordered checkpoints (#111)<br>[`cca8904`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/cca8904b76c984324b639f51c607ebefc1461fc6) — 2026-04-09 — Add per-checkpoint token usage and timing metadata to reached_checkpoints (#110)<br>[`c3c49fa`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/c3c49fa0d8f62155207784d1c5840655f9a424fa) — 2026-02-24 — Make FlagCheckpoint support ignore case (#108) | v0.1.0 (2025-06-24T10:52:37Z) | Low/medium pattern relevance |
| `UKGovernmentBEIS/aisi-sandboxing` | [`c9f2ea1`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c9f2ea1b2a190b92fc2b69a97c237f3a33ee6bee) — 2025-08-07 — Update README.md<br>[`c99dd02`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c99dd02f0664cbec0884dc730d8ac26e5ec6d132) — 2025-08-07 — Add files via upload<br>[`2dd7e4b`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/2dd7e4b4f44412a81b7ce4f62b34c1aa36b32c98) — 2025-08-06 — Add placeholder pdf<br>[`81dbfeb`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/81dbfebc0cd4c603979577eb3f4ab03d0386e832) — 2025-08-06 — First commit | not resolved (HTTP Error 404: Not Found) | Low immediate relevance |

## Package/dependency comparison

| Package | Local version | PyPI latest |
|---|---:|---:|
| `inspect-ai` | `0.3.225` | `0.3.263` |
| `inspect-evals` | `not installed` | `0.19.0` |

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
78 passed in 0.88s

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
