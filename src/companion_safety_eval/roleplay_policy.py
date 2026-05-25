from __future__ import annotations

from typing import Any

from companion_safety_eval.schemas import Scenario, StoryPhase


class TurnOutOfRangeError(ValueError):
    """Raised when a requested turn is outside the scenario story arc."""


def phase_for_turn(scenario: Scenario, turn_index: int) -> StoryPhase:
    """Return the story phase active at a 1-indexed conversation turn."""
    if turn_index < 1:
        raise TurnOutOfRangeError("turn_index must be 1 or greater")
    if not scenario.story_arc.phases:
        raise TurnOutOfRangeError("scenario does not define phased story arc")

    cumulative = 0
    for phase in scenario.story_arc.phases:
        cumulative += phase.turns
        if turn_index <= cumulative:
            return phase
    raise TurnOutOfRangeError(f"turn_index {turn_index} exceeds phased story arc length {cumulative}")


def phase_local_turn_index(scenario: Scenario, turn_index: int) -> int:
    """Return the 1-indexed turn offset within the active phase."""
    if turn_index < 1:
        raise TurnOutOfRangeError("turn_index must be 1 or greater")
    cumulative_before = 0
    for phase in scenario.story_arc.phases:
        if turn_index <= cumulative_before + phase.turns:
            return turn_index - cumulative_before
        cumulative_before += phase.turns
    raise TurnOutOfRangeError(f"turn_index {turn_index} exceeds phased story arc length {cumulative_before}")


def pacing_for_turn(scenario: Scenario, turn_index: int) -> dict[str, Any]:
    """Return phase and pacing controls for a 1-indexed turn."""
    phase = phase_for_turn(scenario, turn_index)
    return {
        "phase_id": phase.id,
        "phase_turn_index": phase_local_turn_index(scenario, turn_index),
        "phase_turns": phase.turns,
        "objective": phase.objective,
        "risk_probe": phase.risk_probe,
        "directness": phase.directness,
        "obliqueness": phase.obliqueness,
        "emotional_intensity": phase.emotional_intensity,
        "persistence": phase.persistence,
        "topic_drift": phase.topic_drift,
        "compliance_pressure": phase.compliance_pressure,
    }
