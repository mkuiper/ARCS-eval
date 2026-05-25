from __future__ import annotations

import json
from pathlib import Path

from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import Score, Target, accuracy, scorer
from inspect_ai.solver import Generate, TaskState, solver

from companion_safety_eval.adapters.tester_companion import TesterCompanionAdapter
from companion_safety_eval.runner import run_scenario
from companion_safety_eval.scenario_loader import load_scenario
from companion_safety_eval.scorers.rubric import score_transcript

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _scenario_paths(scenarios_dir: str | Path) -> list[Path]:
    path = Path(scenarios_dir)
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    if path.is_file():
        return [path]
    return sorted(path.glob("*.yaml")) + sorted(path.glob("*.yml"))


@solver
def companion_runner(target_mode: str = "safe", transcript_dir: str = "runs/inspect"):
    async def solve(state: TaskState, generate: Generate) -> TaskState:
        scenario_path = Path(state.metadata["scenario_path"])
        scenario = load_scenario(scenario_path)
        transcript_path = Path(transcript_dir)
        if not transcript_path.is_absolute():
            transcript_path = PROJECT_ROOT / transcript_path
        transcript_path = transcript_path / f"{scenario.id}-{target_mode}.jsonl"
        adapter = TesterCompanionAdapter(mode=target_mode)
        result = run_scenario(scenario, adapter, transcript_path)
        assessment = score_transcript(scenario, result.events)
        state.output.completion = assessment.model_dump_json()
        state.metadata["transcript_path"] = str(transcript_path)
        return state
    return solve


@scorer(metrics=[accuracy()])
def companion_rubric():
    async def score(state: TaskState, target: Target) -> Score:
        data = json.loads(state.output.completion)
        value = "C" if data.get("passed") else "I"
        explanation = data.get("summary", "") + f" Transcript: {state.metadata.get('transcript_path')}"
        return Score(value=value, explanation=explanation, metadata=data)
    return score


@task
def companion_ai_safety(target_mode: str = "safe", scenarios_dir: str = "scenarios") -> Task:
    paths = _scenario_paths(scenarios_dir)
    dataset = []
    for scenario_path in paths:
        scenario = load_scenario(scenario_path)
        dataset.append(
            Sample(
                id=scenario.id,
                input=f"Run companion AI safety scenario: {scenario.title}",
                target="pass",
                metadata={"scenario_path": str(scenario_path)},
            )
        )
    return Task(dataset=dataset, solver=companion_runner(target_mode=target_mode), scorer=companion_rubric())
