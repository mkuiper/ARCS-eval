from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal

from pydantic import BaseModel, Field, field_validator, model_validator

Severity = Literal["low", "medium", "high", "critical"]


class Persona(BaseModel):
    name: str
    age_band: str = "adult"
    traits: list[str] = Field(default_factory=list)
    vulnerability_notes: str | None = None


class StoryPhase(BaseModel):
    """A paced segment of a long-context roleplay scenario."""

    id: str
    turns: int = Field(gt=0)
    objective: str
    risk_probe: str = "none"
    directness: float = Field(default=0.0, ge=0.0, le=1.0)
    obliqueness: float = Field(default=0.0, ge=0.0, le=1.0)
    emotional_intensity: float = Field(default=0.0, ge=0.0, le=1.0)
    persistence: float = Field(default=0.0, ge=0.0, le=1.0)
    topic_drift: float = Field(default=0.0, ge=0.0, le=1.0)
    compliance_pressure: float = Field(default=0.0, ge=0.0, le=1.0)
    sample_user_turns: list[str] = Field(default_factory=list)


class StoryArc(BaseModel):
    goal: str
    beats: list[str] = Field(default_factory=list)
    phases: list[StoryPhase] = Field(default_factory=list)

    @model_validator(mode="after")
    def require_beats_or_phases(self) -> "StoryArc":
        if not self.beats and not self.phases:
            raise ValueError("story_arc must include at least one beat or one phase")
        return self

    @property
    def total_phase_turns(self) -> int:
        return sum(phase.turns for phase in self.phases)

    @property
    def planned_turns(self) -> int:
        if self.phases:
            return self.total_phase_turns
        return len(self.beats)


class CompletionCriteria(BaseModel):
    max_turns: int = Field(gt=0)
    stop_if_any: list[str] = Field(default_factory=list)


class RubricDimension(BaseModel):
    id: str
    description: str
    severity: Severity = "medium"
    unsafe_patterns: list[str] = Field(default_factory=list)
    safe_patterns: list[str] = Field(default_factory=list)

    @field_validator("unsafe_patterns", "safe_patterns")
    @classmethod
    def strip_patterns(cls, patterns: list[str]) -> list[str]:
        return [p.strip() for p in patterns if p and p.strip()]


class Scenario(BaseModel):
    id: str
    title: str
    risk_domain: str
    user_type: str
    turn_budget: int = Field(gt=0)
    persona: Persona
    story_arc: StoryArc
    completion_criteria: CompletionCriteria
    rubric: list[RubricDimension] = Field(min_length=1)
    safety_notes: list[str] = Field(default_factory=list)

    @field_validator("turn_budget")
    @classmethod
    def turn_budget_matches_story_arc(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("turn_budget must be positive")
        return value


class RubricFinding(BaseModel):
    dimension_id: str
    severity: Severity
    confidence: float = Field(ge=0, le=1)
    turn_index: int | None = None
    evidence: str
    rationale: str


class AssessmentResult(BaseModel):
    scenario_id: str
    passed: bool
    findings: list[RubricFinding] = Field(default_factory=list)
    summary: str
    metadata: dict[str, Any] = Field(default_factory=dict)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
