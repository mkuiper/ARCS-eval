from __future__ import annotations

from pathlib import Path
from pydantic import BaseModel

from companion_safety_eval.adapters.base import TargetAdapter
from companion_safety_eval.roleplay import user_turn_for_index
from companion_safety_eval.schemas import Scenario
from companion_safety_eval.transcript import Transcript, TranscriptEvent


class RunResult(BaseModel):
    scenario_id: str
    transcript_path: Path
    events: list[TranscriptEvent]


def run_scenario(scenario: Scenario, adapter: TargetAdapter, transcript_path: str | Path) -> RunResult:
    transcript = Transcript(transcript_path)
    events: list[TranscriptEvent] = []
    turns = min(scenario.turn_budget, scenario.completion_criteria.max_turns, len(scenario.story_arc.beats))
    for turn_index in range(1, turns + 1):
        user_content = user_turn_for_index(scenario, turn_index)
        user_event = TranscriptEvent(scenario_id=scenario.id, turn_index=turn_index, role="user", content=user_content, metadata={"user_type": scenario.user_type})
        transcript.append(user_event)
        events.append(user_event)
        response = adapter.send(user_content, events.copy())
        target_event = TranscriptEvent(scenario_id=scenario.id, turn_index=turn_index, role="target", content=response.content, metadata=response.metadata)
        transcript.append(target_event)
        events.append(target_event)
    return RunResult(scenario_id=scenario.id, transcript_path=Path(transcript_path), events=events)
