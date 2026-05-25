# Companion AI Safety Eval Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Build an Inspect-compatible, model-agnostic platform for multi-turn safety evaluation of companion AI and other AI systems.

**Architecture:** Scenarios are declarative YAML files loaded into Inspect `Sample`s. A multi-turn solver orchestrates a role-play user agent, a target adapter, and transcript recording. Scorers evaluate saved transcripts with rubric rules and optional assessor LMs.

**Tech Stack:** Python, Inspect AI, Pydantic, PyYAML, pytest, optional Playwright for browser targets, provider-agnostic model config via Inspect model strings and adapter interfaces.

---

## Design decisions

### Keep the three agents separate

- Role-play agent: produces user turns according to persona and story arc.
- Target AI: system under evaluation, reached through an adapter.
- Assessor agent: evaluates the completed transcript against rubric criteria.

This separation avoids contamination and makes logs easier to audit.

### Make scenarios declarative

Use YAML so researchers can author scenarios without editing Python. A scenario should include:

- `id`
- `title`
- `risk_domain`
- `user_type`
- `persona`
- `story_arc`
- `turn_budget`
- `completion_criteria`
- `rubric`
- `safety_notes`

### Make target adapters swappable

Initial adapters:

- `echo`: deterministic smoke-test target
- `inspect_model`: target is another Inspect-supported model string
- `http_api`: generic OpenAI-compatible or custom endpoint
- later: `browser`: web UI automation with transcript and screenshot capture

### Keep assessment evidence-based

Every assessor finding should include:

- rubric dimension
- severity
- confidence
- exact transcript quote or turn reference
- rationale

---

## Suggested repository structure

```text
/home/mike/Projects/companion-ai-safety-eval/
  README.md
  pyproject.toml
  src/companion_safety_eval/
    __init__.py
    schemas.py
    scenario_loader.py
    transcript.py
    inspect_task.py
    solvers/
      __init__.py
      roleplay_solver.py
    adapters/
      __init__.py
      base.py
      echo.py
      inspect_model.py
      http_api.py
    scorers/
      __init__.py
      rubric.py
      assessor_model.py
  scenarios/
    companion_dependency_smoke.yaml
  tests/
    test_schemas.py
    test_scenario_loader.py
    test_transcript.py
    test_rubric_scorer.py
  docs/
    safety_taxonomy.md
    scenario_authoring.md
```

---

## Milestone 1: Inspect-compatible smoke test

### Task 1: Create Python package skeleton

**Objective:** Create installable project layout.

**Files:**
- Create: `pyproject.toml`
- Create: `src/companion_safety_eval/__init__.py`
- Create: `tests/`

**Verification:**

Run:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -U pip
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/python -m pytest -q
```

Expected: tests run, even if initially zero or minimal.

### Task 2: Define scenario and rubric schemas

**Objective:** Add Pydantic models for scenario authoring.

**Files:**
- Create: `src/companion_safety_eval/schemas.py`
- Create: `tests/test_schemas.py`

**Core models:**

- `Scenario`
- `Persona`
- `StoryArc`
- `CompletionCriteria`
- `RubricDimension`
- `RubricFinding`
- `AssessmentResult`

**Verification:**

Run:

```bash
.venv/bin/python -m pytest tests/test_schemas.py -q
```

Expected: valid scenario passes; missing required fields fail with clear errors.

### Task 3: Add YAML scenario loader

**Objective:** Load YAML scenarios into validated schema objects.

**Files:**
- Create: `src/companion_safety_eval/scenario_loader.py`
- Create: `tests/test_scenario_loader.py`
- Create: `scenarios/companion_dependency_smoke.yaml`

**Verification:**

Run:

```bash
.venv/bin/python -m pytest tests/test_scenario_loader.py -q
```

Expected: smoke scenario loads and validates.

### Task 4: Add transcript recorder

**Objective:** Persist multi-turn interactions as structured JSONL.

**Files:**
- Create: `src/companion_safety_eval/transcript.py`
- Create: `tests/test_transcript.py`

**Transcript event fields:**

- `scenario_id`
- `turn_index`
- `role`
- `content`
- `timestamp`
- `metadata`

**Verification:**

Run:

```bash
.venv/bin/python -m pytest tests/test_transcript.py -q
```

Expected: recorder writes JSONL and can reload it exactly.

### Task 5: Add target adapter interface and echo adapter

**Objective:** Establish target-agnostic interface before integrating real models or browsers.

**Files:**
- Create: `src/companion_safety_eval/adapters/base.py`
- Create: `src/companion_safety_eval/adapters/echo.py`
- Create: adapter tests

**Verification:**

Run:

```bash
.venv/bin/python -m pytest tests/ -q
```

Expected: echo adapter returns deterministic responses and records metadata.

### Task 6: Add simple role-play turn generator

**Objective:** Generate bounded user turns from scenario arc without needing a real role-play LM yet.

**Files:**
- Create: `src/companion_safety_eval/solvers/roleplay_solver.py`
- Create: solver tests

**Verification:**

Expected: solver respects `turn_budget` and stops at completion criteria.

### Task 7: Add rubric scorer

**Objective:** Score transcripts using transparent keyword/rule checks for smoke testing.

**Files:**
- Create: `src/companion_safety_eval/scorers/rubric.py`
- Create: `tests/test_rubric_scorer.py`

**Verification:**

Expected: known bad transcript yields finding with evidence; benign transcript passes.

### Task 8: Add Inspect task entry point

**Objective:** Make the project runnable with `inspect eval`.

**Files:**
- Create: `src/companion_safety_eval/inspect_task.py`

**Verification:**

Run:

```bash
.venv/bin/inspect eval src/companion_safety_eval/inspect_task.py --model mockllm/model --limit 1
```

Expected: Inspect loads the task, runs one scenario, writes logs, and exits cleanly.

---

## Milestone 2: Model-agnostic agents

### Task 9: Add Inspect model role-play agent

Use Inspect-supported model strings for role-play generation. Keep scenario instructions non-operational and bounded.

### Task 10: Add assessor-model scorer

Use an assessor model to produce structured JSON assessment with evidence spans. Validate with Pydantic. Fall back to rubric scorer if parsing fails.

### Task 11: Add target model adapter

Allow target AI to be any Inspect-supported model string or OpenAI-compatible endpoint.

---

## Milestone 3: UI and browser targets

### Task 12: Add scenario selection CLI

Add dropdown-like terminal selection using `typer` or `questionary` for:

- scenario
- user type
- target adapter
- role-play model
- assessor model
- run count

### Task 13: Add browser adapter prototype

Use Playwright only after API/local-model flow is stable. Record DOM-visible transcript, screenshots if needed, and adapter actions.

---

## Key safety requirements

- Do not include operational harmful instructions in scenarios.
- Keep role-play prompts focused on eliciting policy-relevant behavior, not teaching harm.
- Always preserve transcripts for auditability.
- Report uncertainty; do not overclaim from model-graded assessments.
- Use human review for high-stakes conclusions.

---

## Open questions

1. Which companion AI interface should be the first real target: API-backed, local model, or browser UI?
2. Which risk domain should be the first scenario family: dependency/manipulation, self-harm, romantic/sexual boundaries, or advice-giving?
3. Should the initial UI be CLI-only, or should we build a lightweight web dashboard after the runner works?
4. Which assessor model(s) should be trusted enough for early grading experiments?
