from pathlib import Path

import pytest
from pydantic import ValidationError

from companion_safety_eval.config import RunConfig, load_run_config, resolve_transcript_path


def valid_config_payload():
    return {
        "run_id": "smoke-safe",
        "scenario": {"path": "scenarios/companion_dependency_smoke.yaml"},
        "roleplay": {
            "mode": "deterministic",
            "max_turns": 4,
            "compaction_interval": 20,
            "directness_offset": 0.0,
            "obliqueness_offset": 0.0,
        },
        "target": {"type": "tester", "tester_mode": "safe"},
        "assessor": {
            "type": "keyword",
            "evidence_required": True,
            "severity_threshold": "high",
            "confidence_threshold": 0.7,
        },
        "artifacts": {
            "transcript_dir": "runs/configured",
            "log_dir": "logs",
            "screenshot_dir": "runs/screenshots",
            "capture_dom": False,
            "capture_screenshots": False,
        },
    }


def test_valid_run_config_loads():
    config = RunConfig.model_validate(valid_config_payload())
    assert config.run_id == "smoke-safe"
    assert config.scenario.path == Path("scenarios/companion_dependency_smoke.yaml")
    assert config.roleplay.mode == "deterministic"
    assert config.target.type == "tester"
    assert config.target.tester_mode == "safe"
    assert config.assessor.severity_threshold == "high"


def test_load_run_config_from_yaml_file(tmp_path):
    config_path = tmp_path / "run.yaml"
    config_path.write_text(
        """
run_id: file-smoke
scenario:
  path: scenarios/companion_dependency_smoke.yaml
roleplay:
  mode: deterministic
  max_turns: 4
target:
  type: tester
  tester_mode: mixed
assessor:
  type: keyword
artifacts:
  transcript_dir: runs/configured
""".strip()
    )
    config = load_run_config(config_path)
    assert config.run_id == "file-smoke"
    assert config.target.tester_mode == "mixed"
    assert config.artifacts.transcript_dir == Path("runs/configured")


def test_tester_target_requires_valid_mode():
    payload = valid_config_payload()
    payload["target"]["tester_mode"] = "chaotic"
    with pytest.raises(ValidationError):
        RunConfig.model_validate(payload)


def test_http_target_requires_base_url_and_model():
    payload = valid_config_payload()
    payload["target"] = {"type": "http_api", "model": "companion-test"}
    with pytest.raises(ValidationError):
        RunConfig.model_validate(payload)


def test_browser_target_accepts_selectors_and_account_metadata():
    payload = valid_config_payload()
    payload["target"] = {
        "type": "browser_playwright",
        "url": "https://example.invalid/chat",
        "account_id": "test-minor-sim-1",
        "storage_state": "secrets/example.storage_state.json",
        "input_selector": "textarea",
        "submit_selector": "button[type='submit']",
        "response_selector": "[data-testid='assistant-message']",
        "rate_limit_seconds": 4,
    }
    config = RunConfig.model_validate(payload)
    assert config.target.url == "https://example.invalid/chat"
    assert config.target.storage_state == Path("secrets/example.storage_state.json")
    assert config.target.rate_limit_seconds == 4


def test_resolve_transcript_path_uses_run_id_and_scenario_stem():
    config = RunConfig.model_validate(valid_config_payload())
    path = resolve_transcript_path(config)
    assert path == Path("runs/configured/smoke-safe-companion_dependency_smoke.jsonl")


def test_roleplay_model_mode_requires_model_string():
    payload = valid_config_payload()
    payload["roleplay"] = {"mode": "model", "max_turns": 4}
    with pytest.raises(ValidationError):
        RunConfig.model_validate(payload)
