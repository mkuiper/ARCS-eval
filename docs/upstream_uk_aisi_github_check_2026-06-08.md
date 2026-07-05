# UK AISI / Inspect upstream GitHub check — 2026-06-08

Date/time checked: 2026-06-08T09:00:22+10:00 to 2026-06-08T09:00+10:00

Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.

## Upstream repos checked

| Repository | Recent activity since prior note | Release/package signal | ARCS relevance |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | New 2026-06-07 commits after the prior check: `23da047` update changelog for release; `b9b788b` ACP snapshot handling; `433b7d6` resolve content attachments when reading transcript events; `0ac7a6a` remove ACP initialization patch. The already-noted `bde55ae` stop-details and `e5e374f` WAL transcript fixes are now part of the current changelog. | PyPI `inspect-ai 0.3.237` | High |
| `UKGovernmentBEIS/inspect_evals` | No new commits observed since 2026-06-06. | Latest release/PyPI remains `inspect-evals 0.13.2` | Medium |
| `UKGovernmentBEIS/inspect_cyber` | No new commits observed since 2026-06-06. | Latest visible release remains `v0.1.0` | Low/medium pattern relevance |
| `UKGovernmentBEIS/aisi-sandboxing` | No new commits observed since 2026-06-06. | No current release signal observed | Low immediate relevance |

## Package/dependency comparison

- Local declared dependency: `inspect-ai>=0.3.0` in `pyproject.toml`; no declared `inspect-evals` dependency.
- Local `.venv` versions: `inspect-ai 0.3.225`; `inspect-evals` not installed.
- PyPI latest: `inspect-ai 0.3.237`; `inspect-evals 0.13.2`.

## Notable upstream changes

### Inspect AI 0.3.237

- `ChatCompletionChoice.stop_details` / `StopDetails` / `StopCategory` is now in the release changelog and surfaces model refusal/safety category and explanation when providers expose them.
- `transcript().events` now resolves content attachments from bounded-history transcript providers rather than returning bare `attachment://` references.
- Realtime sample buffer transcript DB uses WAL journal mode to avoid concurrent read/write `database is locked` failures.
- ACP connection initialization patch was removed because ACP `0.10.1` resolved the underlying issue.

### Inspect Evals 0.13.2

No new activity since the previous note. Still relevant from the prior check: evaluation-report tooling, scorer exception propagation, and isolated eval dependency environments.

## Relevance to ARCS

- Provider refusal/stop metadata remains the most actionable upstream signal. ARCS should preserve refusal category/explanation in target-adapter output metadata and transcript evidence when available, without making provider-specific metadata mandatory.
- Transcript attachment resolution is relevant for long-context companion roleplay and future rich transcript evidence. ARCS should avoid assuming Inspect transcript event content is always inline text; attachment-backed content may now be transparently resolved by newer Inspect versions.
- WAL-backed realtime transcript buffers strengthen the case for future Inspect viewer/TUI integrations that read run state while an eval is still writing.
- Current local `.venv` (`inspect-ai 0.3.225`) is older than the release containing these changes, so local smoke tests will not exercise the new metadata/viewer/transcript behavior yet.

## Recommended local follow-up issue/PR themes

1. `feat: preserve Inspect/provider stop_details metadata in ARCS transcripts`
2. `docs: document Inspect transcript attachment and bounded-history compatibility assumptions`
3. `test: add compatibility smoke run against inspect-ai 0.3.237 in isolated environment`
4. `feat: evaluate Inspect ViewerConfig for ARCS evidence/rubric columns`
5. `docs: keep scorer failures as explicit error/unknown outcomes, not safe/pass defaults`

## Compatibility risks

- Do not rely on `stop_details`, bounded transcript behavior, or attachment-resolution behavior while the local development environment remains on `inspect-ai 0.3.225`.
- If ARCS later adopts Inspect agent bridge integrations, retain the prior note's warning that generation config forwarding changed in Inspect `0.3.236`.
- If transcript content is large or multimodal, future ARCS evidence extraction should handle resolved attachments and metadata robustly rather than assuming simple strings.

## Lightweight local verification

Ran because this note was written and `.venv` exists:

```text
$ .venv/bin/python -m pytest -q
........................................................................ [ 92%]
......                                                                   [100%]
78 passed in 0.41s

$ .venv/bin/ruff check src tests
All checks passed!
```
