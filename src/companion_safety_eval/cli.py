from __future__ import annotations

from pathlib import Path
import json

import typer

from companion_safety_eval.adapters.browser_manual import BrowserManualAdapter
from companion_safety_eval.adapters.echo import EchoAdapter
from companion_safety_eval.adapters.http_api import OpenAICompatibleHTTPAdapter
from companion_safety_eval.adapters.tester_companion import TesterCompanionAdapter
from companion_safety_eval.config import RunConfig, load_run_config, resolve_transcript_path
from companion_safety_eval.runner import run_scenario
from companion_safety_eval.scenario_loader import load_scenario
from companion_safety_eval.scorers.rubric import score_transcript

app = typer.Typer(help="Run ARCS companion AI safety evaluation scenarios.")


def build_adapter(target: str, tester_mode: str, config: RunConfig | None = None):
    if target == "tester":
        return TesterCompanionAdapter(mode=tester_mode)
    if target == "echo":
        return EchoAdapter()
    if target in {"browser-manual", "browser_manual"}:
        return BrowserManualAdapter()
    if target == "http_api" and config is not None:
        if not config.target.base_url or not config.target.model:
            raise typer.BadParameter("http_api target requires base_url and model in run config")
        return OpenAICompatibleHTTPAdapter(
            base_url=config.target.base_url,
            model=config.target.model,
        )
    raise typer.BadParameter("target must be one of: tester, echo, browser-manual, http_api")


def _execute_run(scenario_path: Path, target: str, tester_mode: str, transcript: Path, config: RunConfig | None = None) -> dict:
    loaded = load_scenario(scenario_path)
    adapter = build_adapter(target, tester_mode, config=config)
    result = run_scenario(loaded, adapter, transcript)
    assessment = score_transcript(loaded, result.events)
    return {
        "run_id": config.run_id if config else None,
        "scenario_id": loaded.id,
        "target": target,
        "tester_mode": tester_mode if target == "tester" else None,
        "transcript_path": str(result.transcript_path),
        "passed": assessment.passed,
        "summary": assessment.summary,
        "findings": [f.model_dump() for f in assessment.findings],
    }


@app.command()
def run(
    scenario: Path = typer.Option(Path("scenarios/companion_dependency_smoke.yaml"), help="Scenario YAML path."),
    target: str = typer.Option("tester", help="Target adapter: tester, echo, browser-manual."),
    tester_mode: str = typer.Option("safe", help="Tester companion mode: safe, unsafe, mixed."),
    transcript: Path = typer.Option(Path("runs/latest/transcript.jsonl"), help="Transcript JSONL output path."),
    config: Path | None = typer.Option(None, "--config", "-c", help="Optional run config YAML. CLI options override omitted config fields only by using the config path values when provided."),
):
    if config is not None:
        loaded_config = load_run_config(config)
        scenario = loaded_config.scenario.path
        target = "browser-manual" if loaded_config.target.type == "browser_manual" else loaded_config.target.type
        tester_mode = loaded_config.target.tester_mode
        transcript = resolve_transcript_path(loaded_config)
        result = _execute_run(scenario, target, tester_mode, transcript, config=loaded_config)
    else:
        result = _execute_run(scenario, target, tester_mode, transcript)
    typer.echo(json.dumps(result, indent=2))


if __name__ == "__main__":
    app()
