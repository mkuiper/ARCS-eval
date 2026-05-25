from pathlib import Path

from companion_safety_eval.scenario_loader import load_scenario, load_scenarios


def test_load_smoke_scenario():
    scenario = load_scenario(Path("scenarios/companion_dependency_smoke.yaml"))
    assert scenario.id == "companion_dependency_smoke"
    assert scenario.rubric[0].id == "dependency_reinforcement"


def test_load_scenarios_directory():
    scenarios = load_scenarios(Path("scenarios"))
    assert "companion_dependency_smoke" in {s.id for s in scenarios}
