# UK AISI / Inspect upstream GitHub check — 2026-08-31

Date/time checked: 2026-08-31T09:00:01+10:00

Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible, model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.

## Upstream repositories checked

| Repository | Latest commits observed | Latest release signal | ARCS relevance |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | [`a729c36`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/a729c36bbc8789571edc093ff87223f723941761) — 2026-08-30 — eval set overrides (#5134)<br>[`f9186b4`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/f9186b4e2f34ca81f192ae2c08535c24b7e8f356) — 2026-08-30 — update changelog for release<br>[`6b40085`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/6b4008552562ab04822e35cbec9eed002b7c1645) — 2026-08-30 — Cache prompt prefixes on Bedrock Converse requests (#5131)<br>[`b6aa121`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/b6aa1214ddd5bc399f72072c703e44d26524af45) — 2026-08-30 — update extensions<br>[`56c9cae`](https://github.com/UKGovernmentBEIS/inspect_ai/commit/56c9cae65844c87479b10e212a93b91e1a17c351) — 2026-08-30 — update evals | not resolved (HTTP Error 404: Not Found) | High |
| `UKGovernmentBEIS/inspect_evals` | [`979bf44`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/979bf44681dfdb148021676f9b2be964150bb5ed) — 2026-08-27 — BFCL: fix stale changelog fragment (7-B, no pin bump) (#2316)<br>[`ae814a7`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/ae814a7a46495d8631852d332c974992f6f34d0d) — 2026-08-27 — BFCL: Add V4 agentic categories (memory + web search) (#1698)<br>[`67a9ea5`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/67a9ea5333d3fc672ebce3ca9724bcfdad87f541) — 2026-08-26 — ci: restrict operational automation to upstream repo (#2308)<br>[`c289dba`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/c289dbab1b18f623f8bc514527f176abe66c808b) — 2026-08-26 — fix: use propagated uv release (#2307)<br>[`3e0b885`](https://github.com/UKGovernmentBEIS/inspect_evals/commit/3e0b885adeeae8df3479dcc2057cff53d14236f0) — 2026-08-26 — ci: pin uv version for lockfile generation (#2305) | v0.18.0 (2026-08-20T14:38:06Z) | Medium |
| `UKGovernmentBEIS/inspect_cyber` | [`7fc6927`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/7fc69273c692b21637ce0552298eb9a523e56499) — 2026-06-18 — Fix reached_checkpoints collapsing checkpoints with duplicate names (#114)<br>[`a909bd3`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/a909bd3940aaa3ab3c7f2f22b785b5ba79db5e9d) — 2026-05-28 — Don't complain about using target (#113)<br>[`89b95e0`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/89b95e05a096e95a5faa3e76ebb3eb6d890233fd) — 2026-04-23 — Ordered checkpoints (#111)<br>[`cca8904`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/cca8904b76c984324b639f51c607ebefc1461fc6) — 2026-04-09 — Add per-checkpoint token usage and timing metadata to reached_checkpoints (#110)<br>[`c3c49fa`](https://github.com/UKGovernmentBEIS/inspect_cyber/commit/c3c49fa0d8f62155207784d1c5840655f9a424fa) — 2026-02-24 — Make FlagCheckpoint support ignore case (#108) | v0.1.0 (2025-06-24T10:52:37Z) | Low/medium pattern relevance |
| `UKGovernmentBEIS/aisi-sandboxing` | [`c9f2ea1`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c9f2ea1b2a190b92fc2b69a97c237f3a33ee6bee) — 2025-08-07 — Update README.md<br>[`c99dd02`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/c99dd02f0664cbec0884dc730d8ac26e5ec6d132) — 2025-08-07 — Add files via upload<br>[`2dd7e4b`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/2dd7e4b4f44412a81b7ce4f62b34c1aa36b32c98) — 2025-08-06 — Add placeholder pdf<br>[`81dbfeb`](https://github.com/UKGovernmentBEIS/aisi-sandboxing/commit/81dbfebc0cd4c603979577eb3f4ab03d0386e832) — 2025-08-06 — First commit | not resolved (HTTP Error 404: Not Found) | Low immediate relevance |

## Package/dependency comparison

| Package | Local version | PyPI latest |
|---|---:|---:|
| `inspect-ai` | `0.3.225` | `0.3.261` |
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
78 passed in 0.90s

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
