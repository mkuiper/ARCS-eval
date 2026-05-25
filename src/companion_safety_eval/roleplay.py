from __future__ import annotations

from companion_safety_eval.roleplay_policy import phase_for_turn, phase_local_turn_index
from companion_safety_eval.schemas import Scenario


def user_turn_for_index(scenario: Scenario, turn_index: int) -> str:
    if scenario.story_arc.phases:
        phase = phase_for_turn(scenario, turn_index)
        local_index = phase_local_turn_index(scenario, turn_index)
        if phase.sample_user_turns:
            sample_index = (local_index - 1) % len(phase.sample_user_turns)
            return phase.sample_user_turns[sample_index]
        return f"[{phase.id}] {phase.objective}"
    if turn_index <= len(scenario.story_arc.beats):
        return scenario.story_arc.beats[turn_index - 1]
    return scenario.story_arc.beats[-1]
