from __future__ import annotations

from companion_safety_eval.schemas import Scenario


def user_turn_for_index(scenario: Scenario, turn_index: int) -> str:
    if turn_index <= len(scenario.story_arc.beats):
        return scenario.story_arc.beats[turn_index - 1]
    return scenario.story_arc.beats[-1]
