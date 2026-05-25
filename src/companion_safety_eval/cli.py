from __future__ import annotations

from pathlib import Path
import json

import typer

from companion_safety_eval.adapters.browser_manual import BrowserManualAdapter
from companion_safety_eval.adapters.echo import EchoAdapter
from companion_safety_eval.adapters.tester_companion import TesterCompanionAdapter
from companion_safety_eval.runner import run_scenario
from companion_safety_eval.scenario_loader import load_scenario
from companion_safety_eval.scorers.rubric import score_transcript

app = typer.Typer(help="Run companion AI safety evaluation scenarios.")


def build_adapter(target: str, tester_mode: str):
    if target == "tester":
        return TesterCompanionAdapter(mode=tester_mode)
    if target == "echo":
        return EchoAdapter()
    if target == "browser-manual":
        return BrowserManualAdapter()
    raise typer.BadParameter("target must be one of: tester, echo, browser-manual")


@app.command()
def run(
    scenario: Path = typer.Option(Path("scenarios/companion_dependency_smoke.yaml"), help="Scenario YAML path."),
    target: str = typer.Option("tester", help="Target adapter: tester, echo, browser-manual."),
    tester_mode: str = typer.Option("safe", help="Tester companion mode: safe, unsafe, mixed."),
    transcript: Path = typer.Option(Path("runs/latest/transcript.jsonl"), help="Transcript JSONL output path."),
):
    loaded = load_scenario(scenario)
    adapter = build_adapter(target, tester_mode)
    result = run_scenario(loaded, adapter, transcript)
    assessment = score_transcript(loaded, result.events)
    typer.echo(json.dumps({
        "scenario_id": loaded.id,
        "target": target,
        "tester_mode": tester_mode if target == "tester" else None,
        "transcript_path": str(result.transcript_path),
        "passed": assessment.passed,
        "summary": assessment.summary,
        "findings": [f.model_dump() for f in assessment.findings],
    }, indent=2))


if __name__ == "__main__":
    app()
