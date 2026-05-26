from pathlib import Path

from typer.testing import CliRunner

from companion_safety_eval.scenario_loader import load_scenario
from companion_safety_eval.tui import (
    ScenarioMetadataFormState,
    app,
    build_dashboard_model,
    discover_run_configs,
    discover_scenarios,
    render_actors_tab_text,
    render_dashboard_text,
    render_examples_tab_text,
    render_help_tab_text,
    render_run_configs_tab_text,
    render_scenarios_tab_text,
    render_tabbed_dashboard_text,
    scenario_list_items,
    tab_labels,
)

runner = CliRunner()


def test_discover_scenarios_summarizes_yaml_scenarios():
    scenarios = discover_scenarios(Path("."))

    smoke = next(s for s in scenarios if s.id == "companion_dependency_smoke")
    assert smoke.path == Path("scenarios/companion_dependency_smoke.yaml")
    assert smoke.title == "Companion dependency smoke test"
    assert smoke.turn_budget == 4
    assert smoke.phase_count == 4
    assert smoke.risk_domain == "dependency_manipulation"


def test_discover_run_configs_summarizes_config_targets_and_assessors():
    configs = discover_run_configs(Path("."))

    example = next(c for c in configs if c.run_id == "smoke-safe")
    assert example.path == Path("configs/example_run.yaml")
    assert example.scenario_path == Path("scenarios/companion_dependency_smoke.yaml")
    assert example.target == "tester"
    assert example.roleplay_mode == "deterministic"
    assert example.assessor == "keyword"


def test_build_dashboard_model_includes_recommended_next_actions():
    model = build_dashboard_model(Path("."))

    assert model.project_root == Path(".")
    assert model.scenario_count >= 1
    assert model.config_count >= 1
    assert "Open a run config" in model.next_actions[0]
    assert any(config.run_id == "smoke-safe" for config in model.configs)


def test_build_dashboard_model_handles_missing_scenario_and_config_dirs(tmp_path):
    model = build_dashboard_model(tmp_path)

    assert model.scenario_count == 0
    assert model.config_count == 0
    assert model.errors == []
    assert "Create a run config" in model.next_actions[0]


def test_build_dashboard_model_reports_invalid_yaml_without_crashing(tmp_path):
    (tmp_path / "configs").mkdir()
    (tmp_path / "configs" / "broken.yaml").write_text("run_id: [not valid for schema]\n", encoding="utf-8")

    model = build_dashboard_model(tmp_path)
    text = render_dashboard_text(model)

    assert model.config_count == 0
    assert len(model.errors) == 1
    assert "configs/broken.yaml" in model.errors[0]
    assert "Errors" in text


def test_render_dashboard_text_is_operator_readable():
    model = build_dashboard_model(Path("."))
    text = render_dashboard_text(model)

    assert "ARCS Operator Dashboard" in text
    assert "Scenarios" in text
    assert "Run Configs" in text
    assert "smoke-safe" in text
    assert ".venv/bin/arcs --config" in text


def test_tui_once_command_prints_dashboard_without_interactive_terminal():
    result = runner.invoke(app, ["--project-root", ".", "--once"])

    assert result.exit_code == 0
    assert "ARCS Operator Dashboard" in result.output
    assert "Run Configs" in result.output


def test_tab_labels_include_help_and_examples_for_discoverability():
    assert tab_labels() == ["Overview", "Scenarios", "Actors", "Run Configs", "Help", "Examples"]


def test_tabbed_dashboard_text_has_operator_sections():
    model = build_dashboard_model(Path("."))
    text = render_tabbed_dashboard_text(model)

    assert "[Overview]" in text
    assert "[Scenarios]" in text
    assert "[Actors]" in text
    assert "[Run Configs]" in text
    assert "[Help]" in text
    assert "[Examples]" in text
    assert "Press Tab / Shift+Tab" in text


def test_scenarios_tab_explains_how_to_inspect_and_edit_scenarios():
    model = build_dashboard_model(Path("."))
    text = render_scenarios_tab_text(model)

    assert "Scenarios" in text
    assert "companion_dependency_smoke" in text
    assert ".venv/bin/arcs-tui scenario show" in text
    assert "scenario add-phase" in text


def test_actors_tab_explains_actor_profiles_and_creation_flow():
    model = build_dashboard_model(Path("."))
    text = render_actors_tab_text(model)

    assert "Actor Profiles" in text
    assert "lonely_adult" in text
    assert "scenario new" in text
    assert "--actor-profile" in text


def test_run_configs_tab_shows_launch_commands_and_transcripts():
    model = build_dashboard_model(Path("."))
    text = render_run_configs_tab_text(model)

    assert "Run Configs" in text
    assert "smoke-safe" in text
    assert ".venv/bin/arcs --config" in text
    assert "transcript" in text.lower()


def test_help_tab_is_a_quick_start_for_keyboard_and_cli_usage():
    text = render_help_tab_text()

    assert "Keyboard" in text
    assert "q" in text
    assert "r" in text
    assert "--once" in text
    assert "YAML remains the source of truth" in text


def test_examples_tab_contains_copyable_authoring_and_run_examples():
    text = render_examples_tab_text()

    assert "Create a scenario" in text
    assert "Add a story phase" in text
    assert "Add a rubric" in text
    assert "Run a smoke eval" in text
    assert ".venv/bin/arcs-tui scenario new" in text


def test_scenario_list_items_are_selectable_and_human_readable():
    model = build_dashboard_model(Path("."))
    items = scenario_list_items(model)

    assert any(item.path == Path("scenarios/companion_dependency_smoke.yaml") for item in items)
    assert any("companion_dependency_smoke" in item.label and "phases=4" in item.label for item in items)


def test_metadata_form_state_loads_from_scenario_and_renders_preview_yaml():
    state = ScenarioMetadataFormState.from_path(Path("scenarios/companion_dependency_smoke.yaml"))

    assert state.scenario_id == "companion_dependency_smoke"
    assert state.title == "Companion dependency smoke test"
    assert state.risk_domain == "dependency_manipulation"

    state.title = "Updated title"
    text = state.preview_yaml()

    assert "title: Updated title" in text
    assert "story_arc:" in text


def test_metadata_form_state_saves_valid_yaml(tmp_path):
    source = Path("scenarios/companion_dependency_smoke.yaml")
    target = tmp_path / "scenario.yaml"
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")

    state = ScenarioMetadataFormState.from_path(target)
    state.title = "Saved title"
    state.safety_notes_text = "First note\nSecond note"
    state.save()

    reloaded = load_scenario(target)
    assert reloaded.title == "Saved title"
    assert reloaded.safety_notes == ["First note", "Second note"]
