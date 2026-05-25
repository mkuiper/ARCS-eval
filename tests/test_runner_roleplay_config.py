from companion_safety_eval.adapters.tester_companion import TesterCompanionAdapter
from companion_safety_eval.config import RoleplayConfig
from companion_safety_eval.runner import run_scenario
from companion_safety_eval.scenario_loader import load_scenario


def test_runner_respects_roleplay_config_max_turns_and_offsets(tmp_path):
    scenario = load_scenario("scenarios/companion_dependency_smoke.yaml")
    config = RoleplayConfig(max_turns=2, directness_offset=0.2)

    result = run_scenario(scenario, TesterCompanionAdapter(mode="safe"), tmp_path / "run.jsonl", roleplay_config=config)

    user_events = [event for event in result.events if event.role == "user"]
    assert len(user_events) == 2
    assert user_events[0].metadata["pacing"]["directness"] == 0.3
    assert user_events[0].metadata["roleplay_mode"] == "deterministic"


def test_runner_writes_roleplay_state_snapshot_at_compaction_interval(tmp_path):
    scenario = load_scenario("scenarios/companion_dependency_smoke.yaml")
    config = RoleplayConfig(max_turns=2, compaction_interval=2)

    result = run_scenario(scenario, TesterCompanionAdapter(mode="safe"), tmp_path / "run.jsonl", roleplay_config=config)

    system_events = [event for event in result.events if event.role == "system"]
    assert len(system_events) == 1
    assert system_events[0].metadata["event_type"] == "roleplay_state_snapshot"
    assert system_events[0].metadata["snapshot"]["current_phase_id"] == "mild_dependency"
