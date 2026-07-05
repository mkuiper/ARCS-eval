# UK AISI / Inspect upstream GitHub check — 2026-06-07

Purpose: identify whether recent UK AISI open-source work suggests updates for ARCS (`/home/mike/Projects/companion-ai-safety-eval`).

## Local project context

ARCS currently depends on:

- `inspect-ai>=0.3.0` in `pyproject.toml`
- local standalone Inspect workspace has `inspect-ai 0.3.220` and `inspect-evals 0.12.0`

Local ARCS repository state at check time:

- Remote: `git@github.com:mkuiper/ARCS-eval.git`
- Branch: `main`, aligned with `origin/main`
- Existing uncommitted local change before this note: `scenarios/companion_dependency_smoke.yaml`

## Upstream repositories checked

| Repository | Latest observed commit | Latest release/version signal | Relevance to ARCS |
|---|---:|---|---|
| `UKGovernmentBEIS/inspect_ai` | `bde55ae` — 2026-06-06, `surface model refusal category/explanation (stop_details)` | PyPI `inspect-ai 0.3.236` | High |
| `UKGovernmentBEIS/inspect_evals` | `4a6e795` — 2026-06-05, `Frontier cs dataset fix` | PyPI `inspect-evals 0.13.2` | Medium |
| `UKGovernmentBEIS/inspect_cyber` | `a909bd3` — 2026-05-28, `Don't complain about using target` | `0.1.0`, plus unreleased changes | Medium/low, pattern-relevant |
| `UKGovernmentBEIS/aisi-sandboxing` | `c9f2ea1` — 2025-08-07 | no current Python package signal checked | Low immediate relevance |

## Inspect AI changes that look relevant

Latest stable changelog segment inspected: `inspect-ai 0.3.236` plus current unreleased notes.

Potentially useful for ARCS:

1. **`ChatCompletionChoice.stop_details` for refusal/safety category/explanation**
   - Relevance: ARCS evaluates companion-AI guardrails. If providers expose refusal/safety categories, ARCS could preserve them in transcript metadata and evidence packets rather than treating refusals as plain text only.
   - Suggested follow-up: add a small compatibility note and, later, optional target-adapter metadata fields for provider stop/refusal details.

2. **Transcript database WAL mode / concurrent-read fix**
   - Relevance: ARCS has long-context transcript browsing and future TUI run monitoring. Concurrent read/write resilience matters once the TUI watches active runs.
   - Suggested follow-up: when ARCS starts consuming Inspect log/transcript internals directly, prefer Inspect versions at/above `0.3.236`.

3. **Bounded transcript memory for long-running samples**
   - Relevance: ARCS is explicitly moving toward long-context companion evals. Inspect now has opt-in bounded transcript memory via `INSPECT_TRANSCRIPT_BOUNDED`.
   - Suggested follow-up: document this as an option for large/long ARCS Inspect runs; do not enable by default until tested.

4. **`Task(viewer=ViewerConfig(...))` custom Inspect log views**
   - Relevance: ARCS has scenario metadata, transcript paths, evidence spans, and rubric labels that could be easier to inspect in the Inspect viewer.
   - Suggested follow-up: add a future task to customize sample-list columns and score labels once ARCS result metadata stabilizes.

5. **Agent bridge generation-config behavior changed**
   - Relevance: future ARCS target adapters may use Inspect agent bridges. Defaults now avoid forwarding client generation parameters unless `forward_generation_config=True` is set.
   - Suggested follow-up: record this in adapter-design notes to avoid surprising model settings when using Inspect agent bridges.

## Inspect Evals changes that look relevant

Latest PyPI signal: `inspect-evals 0.13.2`; local standalone workspace has `0.12.0`.

Potentially useful:

1. **Evaluation report tooling added in 0.13.1**
   - Relevance: ARCS needs credible, reproducible evaluation reports.
   - Suggested follow-up: inspect `tools/evaluation_report.py` and its `report_config.yaml` pattern as a model for ARCS run-report generation.

2. **Agentic Misalignment scorer exception propagation**
   - Relevance: useful design lesson: assessor/scorer errors should not silently map to safe/pass outcomes.
   - Suggested follow-up: ensure ARCS assessor/scorer failures produce explicit errored/unknown outcomes, not accidental pass scores.

3. **Isolated dependency environments for complex evals**
   - Relevance: ARCS may add browser/Playwright and model-provider extras. Isolated optional extras may avoid dependency conflicts.
   - Suggested follow-up: keep ARCS extras (`dev`, `tui`, `browser`) narrow and consider per-adapter optional dependency groups if complexity grows.

## Inspect Cyber pattern notes

Unreleased `inspect_cyber` changes mention message-history support and checkpoint scorers.

Potentially useful for ARCS:

- Message-history replay patterns may inform browser/companion conversation replay.
- Checkpoint-based scorers may map well to phased story arcs and completion criteria.

No immediate dependency update recommended unless ARCS starts importing `inspect_cyber` concepts directly.

## Recommended ARCS updates

### Immediate documentation updates

1. Add this upstream-check note to ARCS docs. **Done locally in this file.**
2. Add a short roadmap item: evaluate Inspect `ViewerConfig` and `stop_details` support for ARCS evidence/transcript metadata.
3. Add a scorer-safety note: scorer exceptions must produce explicit error/unknown outcomes rather than safe/pass defaults.

### Dependency updates to consider

1. Keep `pyproject.toml` as `inspect-ai>=0.3.0` for broad compatibility for now.
2. For development/testing environments, consider testing against `inspect-ai>=0.3.236` before relying on new viewer/refusal/transcript features.
3. Update the separate `/home/mike/ai_policy_briefing/inspect_eval` sandbox from `inspect-ai 0.3.220` / `inspect-evals 0.12.0` to latest only in an isolated test branch or copied environment first.

### Candidate GitHub issue/PR themes

- `docs: add UK AISI upstream watch note`
- `feat: preserve provider refusal/stop metadata in target adapter outputs`
- `feat: add Inspect ViewerConfig for ARCS sample/evidence summaries`
- `fix: make scorer exceptions explicit unknown/error outcomes`
- `docs: add report-generation pattern inspired by inspect-evals evaluation_report.py`

## Bottom line

There is new upstream activity worth tracking, especially in `inspect_ai` and `inspect_evals`. I would not blindly bump dependencies or rewrite ARCS yet. The strongest near-term update is to add documentation/backlog items and then run a small compatibility test against `inspect-ai 0.3.236` before adopting new APIs.
