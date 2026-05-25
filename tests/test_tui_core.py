from pathlib import Path

from typer.testing import CliRunner

from companion_safety_eval.tui import app, build_dashboard_model, discover_run_configs, discover_scenarios, render_dashboard_text

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
