from companion_safety_eval.cli import _execute_run
from companion_safety_eval.config import RunConfig
from tests.test_run_config import valid_config_payload


def test_execute_run_applies_configured_roleplay_and_layered_assessor(tmp_path):
    payload = valid_config_payload()
    payload["run_id"] = "configured-dev"
    payload["roleplay"]["max_turns"] = 2
    payload["roleplay"]["compaction_interval"] = 2
    payload["roleplay"]["directness_offset"] = 0.2
    payload["assessor"]["window_size_turns"] = 1
    config = RunConfig.model_validate(payload)

    result = _execute_run(
        config.scenario.path,
        target="tester",
        tester_mode="unsafe",
        transcript=tmp_path / "configured.jsonl",
        config=config,
    )

    assert result["run_id"] == "configured-dev"
    assert result["turn_count"] == 2
    assert result["assessment_metadata"]["assessment_mode"] == "layered_keyword"
    assert result["assessment_metadata"]["window_size_turns"] == 1
    assert result["roleplay"]["mode"] == "deterministic"
    assert result["roleplay"]["max_turns"] == 2
