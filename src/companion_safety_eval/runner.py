from __future__ import annotations

from pathlib import Path
from pydantic import BaseModel

from companion_safety_eval.adapters.base import TargetAdapter
from companion_safety_eval.config import RoleplayConfig
from companion_safety_eval.roleplay_agents import DeterministicRoleplayAgent, ModelClient, ModelRoleplayAgent, RoleplayContext
from companion_safety_eval.roleplay_state import compact_roleplay_state
from companion_safety_eval.schemas import Scenario
from companion_safety_eval.transcript import Transcript, TranscriptEvent


class RunResult(BaseModel):
    scenario_id: str
    transcript_path: Path
    events: list[TranscriptEvent]


def run_scenario(
    scenario: Scenario,
    adapter: TargetAdapter,
    transcript_path: str | Path,
    roleplay_config: RoleplayConfig | None = None,
    model_client: ModelClient | None = None,
) -> RunResult:
    transcript = Transcript(transcript_path)
    events: list[TranscriptEvent] = []
    config = roleplay_config or RoleplayConfig()
    agent = _build_roleplay_agent(config, model_client)
    turns = _turn_count(scenario, config)
    for turn_index in range(1, turns + 1):
        roleplay_turn = agent.next_turn(RoleplayContext(scenario=scenario, turn_index=turn_index, events=events.copy()))
        user_event = TranscriptEvent(
            scenario_id=scenario.id,
            turn_index=turn_index,
            role="user",
            content=roleplay_turn.content,
            metadata=roleplay_turn.metadata,
        )
        transcript.append(user_event)
        events.append(user_event)
        response = adapter.send(roleplay_turn.content, events.copy())
        target_event = TranscriptEvent(
            scenario_id=scenario.id,
            turn_index=turn_index,
            role="target",
            content=response.content,
            metadata=response.metadata,
        )
        transcript.append(target_event)
        events.append(target_event)
        if config.compaction_interval and turn_index % config.compaction_interval == 0:
            snapshot = compact_roleplay_state(scenario=scenario, events=events.copy(), current_turn_index=turn_index)
            snapshot_event = TranscriptEvent(
                scenario_id=scenario.id,
                turn_index=turn_index,
                role="system",
                content="roleplay_state_snapshot",
                metadata={"event_type": "roleplay_state_snapshot", "snapshot": snapshot.model_dump()},
            )
            transcript.append(snapshot_event)
            events.append(snapshot_event)
    return RunResult(scenario_id=scenario.id, transcript_path=Path(transcript_path), events=events)


def _build_roleplay_agent(config: RoleplayConfig, model_client: ModelClient | None):
    if config.mode == "model":
        if model_client is None:
            raise ValueError("model_client is required when roleplay.mode is 'model'")
        return ModelRoleplayAgent(config=config, client=model_client)
    return DeterministicRoleplayAgent(config=config)


def _turn_count(scenario: Scenario, config: RoleplayConfig) -> int:
    configured_max = config.max_turns if config.max_turns is not None else scenario.turn_budget
    return min(configured_max, scenario.turn_budget, scenario.completion_criteria.max_turns, scenario.story_arc.planned_turns)
