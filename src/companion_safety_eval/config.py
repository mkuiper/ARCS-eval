from __future__ import annotations

from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, Field, model_validator

SeverityThreshold = Literal["low", "medium", "high", "critical"]
RoleplayMode = Literal["deterministic", "model"]
TargetType = Literal["tester", "echo", "http_api", "inspect_model", "browser_manual", "browser_playwright"]
AssessorType = Literal["keyword", "model", "hybrid"]
TesterMode = Literal["safe", "unsafe", "mixed"]


class ScenarioConfig(BaseModel):
    path: Path


class RoleplayConfig(BaseModel):
    mode: RoleplayMode = "deterministic"
    model: str | None = None
    max_turns: int | None = Field(default=None, gt=0)
    compaction_interval: int | None = Field(default=None, gt=0)
    directness_offset: float = Field(default=0.0, ge=-1.0, le=1.0)
    obliqueness_offset: float = Field(default=0.0, ge=-1.0, le=1.0)

    @model_validator(mode="after")
    def require_model_for_model_mode(self) -> "RoleplayConfig":
        if self.mode == "model" and not self.model:
            raise ValueError("roleplay.model is required when roleplay.mode is 'model'")
        return self


class TargetConfig(BaseModel):
    type: TargetType = "tester"
    tester_mode: TesterMode = "safe"
    model: str | None = None
    base_url: str | None = None
    api_key_env: str | None = None
    url: str | None = None
    account_id: str | None = None
    storage_state: Path | None = None
    input_selector: str | None = None
    submit_selector: str | None = None
    response_selector: str | None = None
    rate_limit_seconds: float = Field(default=0.0, ge=0.0)

    @model_validator(mode="after")
    def validate_target_specific_fields(self) -> "TargetConfig":
        if self.type == "http_api":
            missing = []
            if not self.base_url:
                missing.append("base_url")
            if not self.model:
                missing.append("model")
            if missing:
                raise ValueError(f"http_api target requires: {', '.join(missing)}")
        if self.type == "inspect_model" and not self.model:
            raise ValueError("inspect_model target requires model")
        if self.type == "browser_playwright":
            missing = []
            for field_name in ["url", "input_selector", "response_selector"]:
                if getattr(self, field_name) in (None, ""):
                    missing.append(field_name)
            if missing:
                raise ValueError(f"browser_playwright target requires: {', '.join(missing)}")
        return self


class AssessorConfig(BaseModel):
    type: AssessorType = "keyword"
    model: str | None = None
    evidence_required: bool = True
    severity_threshold: SeverityThreshold = "medium"
    confidence_threshold: float = Field(default=0.5, ge=0.0, le=1.0)
    window_size_turns: int | None = Field(default=None, gt=0)

    @model_validator(mode="after")
    def require_model_for_model_assessors(self) -> "AssessorConfig":
        if self.type in {"model", "hybrid"} and not self.model:
            raise ValueError("assessor.model is required when assessor.type is model or hybrid")
        return self


class ArtifactConfig(BaseModel):
    transcript_dir: Path = Path("runs/latest")
    log_dir: Path = Path("logs")
    screenshot_dir: Path | None = None
    capture_dom: bool = False
    capture_screenshots: bool = False


class RunConfig(BaseModel):
    run_id: str
    scenario: ScenarioConfig
    roleplay: RoleplayConfig = Field(default_factory=RoleplayConfig)
    target: TargetConfig = Field(default_factory=TargetConfig)
    assessor: AssessorConfig = Field(default_factory=AssessorConfig)
    artifacts: ArtifactConfig = Field(default_factory=ArtifactConfig)


def load_run_config(path: str | Path) -> RunConfig:
    config_path = Path(path)
    with config_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return RunConfig.model_validate(data)


def resolve_transcript_path(config: RunConfig) -> Path:
    scenario_stem = config.scenario.path.stem
    return config.artifacts.transcript_dir / f"{config.run_id}-{scenario_stem}.jsonl"
