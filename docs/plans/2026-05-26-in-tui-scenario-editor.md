# In-TUI Scenario Editor Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Turn `arcs-tui` from a tabbed dashboard/help surface into a genuinely usable in-terminal scenario editor for non-expert users.

**Architecture:** Keep YAML files as the source of truth, but add Textual screens/forms that load YAML into structured editor state, validate with existing Pydantic schemas, preview diffs, and save back to disk only after explicit confirmation. Do not build a generic raw JSON/YAML text editor first; build structured forms for the domain objects users actually need to edit.

**Tech Stack:** Python, Textual, Typer, Pydantic schemas, PyYAML, pytest, ruff.

---

## Product assessment

The current TUI is not enough for an average user.

It is useful for:

- finding scenarios, actors, and configs
- understanding the project mental model
- copying commands
- validating that the repo structure is sane

But it is not yet intuitive scenario-authoring software because editing still requires command-line fluency. For an average user, the current tabs are closer to a guided help page than an app.

The right next improvement is not more help text. The right next improvement is an in-TUI editor workflow.

## UX direction

Prefer structured forms over a raw JSON/YAML editor.

Why not start with a raw JSON editor:

- YAML/JSON editing requires users to understand schema shape, indentation, and field names.
- It is easy to create syntactically valid but semantically poor scenarios.
- It does not use the domain model we already have: actor profile, story arc, completion criteria, rubric.
- It is less helpful than opening the file in a normal editor.

Better approach:

- Scenario list screen.
- Select scenario.
- Open scenario editor screen.
- Edit fields through forms grouped by conceptual section:
  - Metadata
  - Actor/persona
  - Story phases
  - Completion criteria
  - Rubrics
  - Safety notes
- Validate continuously or on save.
- Preview YAML diff before writing.
- Save only after explicit confirmation.

A raw YAML/JSON view can still exist as an advanced tab, but it should be secondary.

## Target user workflow

1. Run:

```bash
.venv/bin/arcs-tui
```

2. Open Scenarios tab.
3. Use arrow keys to select a scenario.
4. Press `Enter` or `e` to edit.
5. Land in a Scenario Editor screen with subtabs:
   - Metadata
   - Actor
   - Story Arc
   - Completion
   - Rubrics
   - Preview
6. Edit fields using Textual `Input`, `TextArea`, `Select`, and simple buttons.
7. Press `v` to validate.
8. Press `p` to preview YAML/diff.
9. Press `s` to save.
10. Confirm overwrite.
11. Return to Scenarios tab with refreshed data.

## Non-goals for first editor increment

Do not implement all editor features at once.

Do not add:

- run launching
- browser adapter configuration
- transcript viewer
- drag-and-drop phase reordering
- multi-file project wizard
- complex visual JSON tree editor
- real-time model calls

First increment should make editing one scenario obviously possible.

---

## Task 1: Add editor state model and YAML serialization helpers

**Objective:** Create a small scenario editor state layer that can load a scenario, update top-level editable fields, validate, and render YAML.

**Files:**
- Modify: `src/companion_safety_eval/scenario_editor.py`
- Test: `tests/test_scenario_editor.py`

**Step 1: Write failing tests**

Add tests for a structured edit payload:

```python
def test_update_scenario_metadata_validates_payload():
    scenario = load_scenario(Path("scenarios/companion_dependency_smoke.yaml"))
    payload = scenario.model_dump(mode="json")

    updated = update_scenario_metadata(
        payload,
        title="Updated dependency smoke",
        risk_domain="dependency_manipulation",
        safety_notes=["Updated note"],
    )

    assert updated["title"] == "Updated dependency smoke"
    assert updated["risk_domain"] == "dependency_manipulation"
    assert updated["safety_notes"] == ["Updated note"]
    Scenario.model_validate(updated)
```

Add tests for YAML rendering:

```python
def test_render_payload_yaml_round_trips_through_scenario_schema():
    scenario = load_scenario(Path("scenarios/companion_dependency_smoke.yaml"))
    text = render_payload_yaml(scenario.model_dump(mode="json"))
    loaded = yaml.safe_load(text)
    assert Scenario.model_validate(loaded).id == scenario.id
```

**Step 2: Run tests to verify failure**

```bash
.venv/bin/python -m pytest tests/test_scenario_editor.py -q
```

Expected: import/name failures for `update_scenario_metadata` and `render_payload_yaml`.

**Step 3: Implement minimal helpers**

In `scenario_editor.py`, add:

```python
def update_scenario_metadata(
    payload: dict[str, Any],
    title: str,
    risk_domain: str,
    safety_notes: list[str],
) -> dict[str, Any]:
    updated = _copy_payload(payload)
    updated["title"] = title
    updated["risk_domain"] = risk_domain
    updated["safety_notes"] = safety_notes
    _validate_payload(updated)
    return updated


def render_payload_yaml(payload: dict[str, Any]) -> str:
    _validate_payload(payload)
    return yaml.safe_dump(payload, sort_keys=False, allow_unicode=True)
```

**Step 4: Run tests**

```bash
.venv/bin/python -m pytest tests/test_scenario_editor.py -q
```

Expected: pass.

---

## Task 2: Add a non-interactive editor preview command

**Objective:** Add a safe CLI bridge that previews editable YAML from the same code the TUI will use.

**Files:**
- Modify: `src/companion_safety_eval/tui.py`
- Test: `tests/test_tui_scenario_edit_commands.py`

**Step 1: Write failing test**

```python
def test_scenario_preview_yaml_command_renders_valid_yaml():
    result = runner.invoke(app, ["scenario", "preview-yaml", "scenarios/companion_dependency_smoke.yaml"])

    assert result.exit_code == 0
    assert "id: companion_dependency_smoke" in result.output
    assert "story_arc:" in result.output
```

**Step 2: Run failing test**

```bash
.venv/bin/python -m pytest tests/test_tui_scenario_edit_commands.py::test_scenario_preview_yaml_command_renders_valid_yaml -q
```

Expected: command not found.

**Step 3: Implement command**

Import `render_payload_yaml`, then add:

```python
@scenario_app.command("preview-yaml")
def scenario_preview_yaml(path: Path):
    """Render normalized scenario YAML without writing changes."""
    scenario = load_scenario(path)
    typer.echo(render_payload_yaml(scenario.model_dump(mode="json")))
```

**Step 4: Verify**

```bash
.venv/bin/python -m pytest tests/test_tui_scenario_edit_commands.py -q
```

---

## Task 3: Split Textual app into app class with testable screen builders

**Objective:** Make the Textual app easier to extend by moving the nested `ARCSOperatorApp` out of `run_textual_dashboard`.

**Files:**
- Modify: `src/companion_safety_eval/tui.py`
- Test: `tests/test_tui_core.py`

**Step 1: Write failing tests**

```python
def test_tui_exports_operator_app_class():
    from companion_safety_eval.tui import ARCSOperatorApp

    app = ARCSOperatorApp(project_root=Path("."))
    assert app.project_root == Path(".")
```

**Step 2: Run failing test**

```bash
.venv/bin/python -m pytest tests/test_tui_core.py::test_tui_exports_operator_app_class -q
```

Expected: import failure.

**Step 3: Refactor**

Move the nested class to module scope. Constructor accepts `project_root: Path`.

Keep `run_textual_dashboard(project_root)` as:

```python
def run_textual_dashboard(project_root: Path) -> None:
    if not textual_available():
        ...
    ARCSOperatorApp(project_root=project_root).run()
```

**Step 4: Verify existing behavior**

```bash
.venv/bin/python -m pytest tests/test_tui_core.py -q
.venv/bin/arcs-tui --once
```

---

## Task 4: Add selectable scenario list screen

**Objective:** Replace static scenario text with a selectable list in the Scenarios tab.

**Files:**
- Modify: `src/companion_safety_eval/tui.py`
- Test: `tests/test_tui_core.py`

**Step 1: Write tests for list item labels**

Avoid relying on full Textual rendering. Test a helper:

```python
def test_scenario_list_items_are_human_readable():
    model = build_dashboard_model(Path("."))
    items = scenario_list_items(model)

    assert any("companion_dependency_smoke" in item.label for item in items)
    assert any("phases=4" in item.label for item in items)
```

**Step 2: Implement helper dataclass**

```python
@dataclass(frozen=True)
class ScenarioListItem:
    label: str
    path: Path
```

```python
def scenario_list_items(model: DashboardModel) -> list[ScenarioListItem]:
    return [
        ScenarioListItem(
            label=f"{s.id} | {s.risk_domain} | actor={s.user_type} | phases={s.phase_count}",
            path=s.path,
        )
        for s in model.scenarios
    ]
```

**Step 3: Add Textual `ListView` in Scenarios tab**

If Textual is installed, use `ListView` / `ListItem` / `Label` so users can arrow through scenarios.

Initial actions:

- `Enter`: show detail pane for selected scenario.
- `e`: future edit action placeholder if full editor is not complete in this task.

**Step 4: Verify**

```bash
.venv/bin/python -m pytest tests/test_tui_core.py -q
.venv/bin/ruff check src tests
```

---

## Task 5: Add Scenario Editor screen shell

**Objective:** Add an actual editor screen reachable from selected scenario, initially supporting metadata fields only.

**Files:**
- Modify: `src/companion_safety_eval/tui.py`
- Test: `tests/test_tui_core.py`

**Step 1: Write tests for editor form model**

Add helper tests independent of Textual:

```python
def test_scenario_metadata_form_state_loads_from_scenario():
    state = ScenarioMetadataFormState.from_path(Path("scenarios/companion_dependency_smoke.yaml"))

    assert state.scenario_id == "companion_dependency_smoke"
    assert state.title == "Companion dependency smoke test"
    assert state.risk_domain == "dependency_manipulation"
```

**Step 2: Implement form state dataclass**

```python
@dataclass
class ScenarioMetadataFormState:
    path: Path
    scenario_id: str
    title: str
    risk_domain: str
    safety_notes_text: str

    @classmethod
    def from_path(cls, path: Path) -> "ScenarioMetadataFormState":
        scenario = load_scenario(path)
        return cls(
            path=path,
            scenario_id=scenario.id,
            title=scenario.title,
            risk_domain=scenario.risk_domain,
            safety_notes_text="\n".join(scenario.safety_notes),
        )
```

**Step 3: Add Textual screen**

Create `ScenarioMetadataEditorScreen` with:

- Static scenario id/path
- `Input` for title
- `Input` or `Select` for risk domain
- `TextArea` or multi-line input fallback for safety notes
- buttons/keys: validate, preview, save, cancel

**Step 4: Wire key/action**

In Scenarios tab:

- `e`: open metadata editor for selected scenario.
- `escape`: return.

**Step 5: Verify**

```bash
.venv/bin/python -m pytest tests/test_tui_core.py -q
.venv/bin/ruff check src tests
```

---

## Task 6: Add validation and preview panel

**Objective:** Let users validate form edits and preview normalized YAML before saving.

**Files:**
- Modify: `src/companion_safety_eval/tui.py`
- Test: `tests/test_tui_core.py`

**Step 1: Write tests for preview helper**

```python
def test_metadata_form_state_can_render_valid_preview_yaml():
    state = ScenarioMetadataFormState.from_path(Path("scenarios/companion_dependency_smoke.yaml"))
    state.title = "Updated title"

    text = state.preview_yaml()

    assert "title: Updated title" in text
    assert "story_arc:" in text
```

**Step 2: Implement `to_payload` and `preview_yaml`**

```python
def to_payload(self) -> dict[str, Any]:
    scenario = load_scenario(self.path)
    return update_scenario_metadata(
        scenario.model_dump(mode="json"),
        title=self.title,
        risk_domain=self.risk_domain,
        safety_notes=[line.strip() for line in self.safety_notes_text.splitlines() if line.strip()],
    )


def preview_yaml(self) -> str:
    return render_payload_yaml(self.to_payload())
```

**Step 3: Add preview area in screen**

Use `Static` or `TextArea(read_only=True)` to show YAML preview and validation messages.

**Step 4: Verify**

```bash
.venv/bin/python -m pytest tests/test_tui_core.py -q
```

---

## Task 7: Add explicit save confirmation

**Objective:** Make in-TUI editing safe by requiring explicit save confirmation and validating before writing.

**Files:**
- Modify: `src/companion_safety_eval/tui.py`
- Test: `tests/test_tui_core.py`

**Step 1: Write tests for saving to temp copy**

```python
def test_metadata_form_state_saves_valid_yaml(tmp_path):
    source = Path("scenarios/companion_dependency_smoke.yaml")
    target = tmp_path / "scenario.yaml"
    target.write_text(source.read_text(), encoding="utf-8")

    state = ScenarioMetadataFormState.from_path(target)
    state.title = "Saved title"
    state.save()

    reloaded = load_scenario(target)
    assert reloaded.title == "Saved title"
```

**Step 2: Implement save**

```python
def save(self) -> None:
    save_scenario_payload(self.to_payload(), self.path)
```

**Step 3: Add confirmation behavior**

In the editor screen:

- pressing `s` first shows “Press s again to confirm save” or opens a simple confirm modal.
- second confirmation calls `save()`.
- after save, refresh dashboard model and return to scenario list.

**Step 4: Verify**

```bash
.venv/bin/python -m pytest tests/test_tui_core.py tests/test_scenario_editor.py -q
```

---

## Task 8: Add story phase editor increment

**Objective:** Let users add a story phase from inside the TUI, using existing `add_story_phase` helper.

**Files:**
- Modify: `src/companion_safety_eval/tui.py`
- Test: `tests/test_tui_core.py`

**Step 1: Add form state tests**

```python
def test_phase_form_state_adds_phase_to_payload():
    source = Path("scenarios/companion_dependency_smoke.yaml")
    state = AddPhaseFormState(
        path=source,
        phase_id="recovery_check",
        objective="Check whether safe redirection persists.",
        turns=1,
        risk_probe="recovery",
        directness=0.3,
        obliqueness=0.4,
    )

    payload = state.to_payload()

    assert payload["story_arc"]["phases"][-1]["id"] == "recovery_check"
```

**Step 2: Implement form state**

Use existing `add_story_phase` helper.

**Step 3: Add editor screen**

From Scenario Editor screen:

- Press `a` to add story phase.
- Inputs: phase id, objective, turns, risk probe, directness, obliqueness.
- Validate and preview before save.

---

## Task 9: Add rubric editor increment

**Objective:** Let users add a rubric dimension from inside the TUI, using existing `add_rubric_dimension` helper.

**Files:**
- Modify: `src/companion_safety_eval/tui.py`
- Test: `tests/test_tui_core.py`

Follow the same pattern as Task 8.

Fields:

- dimension id
- description
- severity select: low, medium, high, critical
- unsafe patterns multiline
- safe patterns multiline

---

## Task 10: Documentation and verification

**Objective:** Update docs so users understand the TUI is now a real editor.

**Files:**
- Modify: `README.md`
- Modify: `docs/tui.md`
- Modify: `docs/design_choices.md`
- Modify: `docs/decision_log.md`
- Modify: `docs/agent_resume_brief.md`

**Docs should say:**

- `arcs-tui` has selectable scenario rows.
- `e` opens the scenario editor.
- Metadata can be edited directly in the TUI.
- Story phases and rubrics can be added in the TUI.
- YAML preview and validation happen before save.
- CLI commands remain available for agent/CI use.

**Verification:**

```bash
.venv/bin/python -m pytest -q
.venv/bin/ruff check src tests
.venv/bin/arcs-tui --once
.venv/bin/arcs-tui scenario preview-yaml scenarios/companion_dependency_smoke.yaml
.venv/bin/arcs --config configs/example_run.yaml
```

---

## Acceptance criteria

The TUI should no longer feel like a glorified help page.

Minimum acceptable result:

- User can open `arcs-tui`.
- User can select a scenario with arrow keys.
- User can press `e` to open an editor.
- User can edit at least title, risk domain, and safety notes in fields.
- User can validate edits before save.
- User can preview YAML before save.
- User can save only after explicit confirmation.
- User can add a story phase inside the TUI.
- User can add a rubric dimension inside the TUI.
- Existing CLI commands still work.
- `--once` still works.
- Tests and lint pass.

## Recommended implementation order

Do not jump straight to all editor screens. Build confidence in thin increments:

1. Editor state helpers.
2. YAML preview command.
3. Exported Textual app class.
4. Selectable scenario list.
5. Metadata editor.
6. Preview/validate panel.
7. Save confirmation.
8. Add phase form.
9. Add rubric form.
10. Documentation and smoke testing.

This turns the TUI into a real authoring tool without abandoning the existing validated YAML pipeline.
