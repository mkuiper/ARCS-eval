from companion_safety_eval.adapters.tester_companion import TesterCompanionAdapter
from companion_safety_eval.runner import run_scenario
from companion_safety_eval.scenario_loader import load_scenario


def test_tester_companion_can_be_safe_or_unsafe():
    safe = TesterCompanionAdapter(mode="safe")
    unsafe = TesterCompanionAdapter(mode="unsafe")
    assert "trusted" in safe.send("Should I ignore everyone?", []).content.lower()
    assert "only one" in unsafe.send("Should I ignore everyone?", []).content.lower()


def test_runner_records_target_and_user_turns(tmp_path):
    scenario = load_scenario("scenarios/companion_dependency_smoke.yaml")
    result = run_scenario(scenario, TesterCompanionAdapter(mode="safe"), tmp_path / "run.jsonl")
    assert result.transcript_path.exists()
    assert len(result.events) == scenario.turn_budget * 2
    assert result.events[0].role == "user"
    assert result.events[1].role == "target"
