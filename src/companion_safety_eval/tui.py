from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import typer

from companion_safety_eval.config import RunConfig, load_run_config, resolve_transcript_path
from companion_safety_eval.scenario_loader import load_scenario

app = typer.Typer(help="ARCS local operator dashboard for scenarios, run configs, and next actions.")


@dataclass(frozen=True)
class ScenarioSummary:
    path: Path
    id: str
    title: str
    risk_domain: str
    user_type: str
    turn_budget: int
    phase_count: int
    rubric_count: int


@dataclass(frozen=True)
class RunConfigSummary:
    path: Path
    run_id: str
    scenario_path: Path
    target: str
    roleplay_mode: str
    assessor: str
    transcript_path: Path


@dataclass(frozen=True)
class DashboardModel:
    project_root: Path
    scenarios: list[ScenarioSummary] = field(default_factory=list)
    configs: list[RunConfigSummary] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    next_actions: list[str] = field(default_factory=list)

    @property
    def scenario_count(self) -> int:
        return len(self.scenarios)

    @property
    def config_count(self) -> int:
        return len(self.configs)


def discover_scenarios(project_root: Path) -> list[ScenarioSummary]:
    summaries, _ = _discover_scenarios_with_errors(project_root)
    return summaries


def discover_run_configs(project_root: Path) -> list[RunConfigSummary]:
    summaries, _ = _discover_run_configs_with_errors(project_root)
    return summaries


def build_dashboard_model(project_root: Path) -> DashboardModel:
    scenarios, scenario_errors = _discover_scenarios_with_errors(project_root)
    configs, config_errors = _discover_run_configs_with_errors(project_root)
    return DashboardModel(
        project_root=project_root,
        scenarios=scenarios,
        configs=configs,
        errors=scenario_errors + config_errors,
        next_actions=_next_actions(configs=configs, scenarios=scenarios),
    )


def render_dashboard_text(model: DashboardModel) -> str:
    lines = [
        "ARCS Operator Dashboard",
        f"Project root: {model.project_root}",
        "",
        f"Scenarios ({model.scenario_count})",
    ]
    if model.scenarios:
        for scenario in model.scenarios:
            lines.append(
                f"- {scenario.id}: {scenario.title} | risk={scenario.risk_domain} | "
                f"user={scenario.user_type} | turns={scenario.turn_budget} | phases={scenario.phase_count} | path={scenario.path}"
            )
    else:
        lines.append("- none found under scenarios/*.yaml")

    lines.extend(["", f"Run Configs ({model.config_count})"])
    if model.configs:
        for config in model.configs:
            lines.append(
                f"- {config.run_id}: target={config.target} | roleplay={config.roleplay_mode} | "
                f"assessor={config.assessor} | scenario={config.scenario_path} | path={config.path}"
            )
            lines.append(f"  run: .venv/bin/arcs --config {config.path}")
            lines.append(f"  transcript: {config.transcript_path}")
    else:
        lines.append("- none found under configs/*.yaml")

    lines.extend(["", "Next Actions"])
    for action in model.next_actions:
        lines.append(f"- {action}")
    if model.errors:
        lines.extend(["", "Errors"])
        for error in model.errors:
            lines.append(f"- {error}")
    return "\n".join(lines)


def run_textual_dashboard(project_root: Path) -> None:
    try:
        from textual.app import App, ComposeResult
        from textual.widgets import Footer, Header, Static
    except ImportError:
        typer.echo(render_dashboard_text(build_dashboard_model(project_root)))
        typer.echo("\nTextual is not installed; printed non-interactive dashboard instead.")
        return

    class ARCSOperatorApp(App):
        TITLE = "ARCS Operator Dashboard"
        BINDINGS = [("q", "quit", "Quit")]

        def compose(self) -> ComposeResult:
            yield Header()
            yield Static(render_dashboard_text(build_dashboard_model(project_root)), id="dashboard")
            yield Footer()

    ARCSOperatorApp().run()


@app.callback(invoke_without_command=True)
def main(
    project_root: Path = typer.Option(Path("."), "--project-root", "-p", help="ARCS project root."),
    once: bool = typer.Option(False, "--once", help="Print the dashboard once without launching interactive Textual UI."),
):
    """Open the ARCS TUI, or print a one-shot operator dashboard with --once."""
    if once:
        typer.echo(render_dashboard_text(build_dashboard_model(project_root)))
        return
    run_textual_dashboard(project_root)


def _summarize_run_config(config: RunConfig, path: Path) -> RunConfigSummary:
    return RunConfigSummary(
        path=path,
        run_id=config.run_id,
        scenario_path=config.scenario.path,
        target=config.target.type,
        roleplay_mode=config.roleplay.mode,
        assessor=config.assessor.type,
        transcript_path=resolve_transcript_path(config),
    )


def _discover_scenarios_with_errors(project_root: Path) -> tuple[list[ScenarioSummary], list[str]]:
    scenario_dir = project_root / "scenarios"
    summaries: list[ScenarioSummary] = []
    errors: list[str] = []
    for path in sorted(scenario_dir.glob("*.yaml")):
        try:
            scenario = load_scenario(path)
        except Exception as exc:  # noqa: BLE001 - dashboard should report validation/parsing errors without crashing
            errors.append(f"{path.relative_to(project_root)}: {exc}")
            continue
        summaries.append(
            ScenarioSummary(
                path=path.relative_to(project_root),
                id=scenario.id,
                title=scenario.title,
                risk_domain=scenario.risk_domain,
                user_type=scenario.user_type,
                turn_budget=scenario.turn_budget,
                phase_count=len(scenario.story_arc.phases),
                rubric_count=len(scenario.rubric),
            )
        )
    return summaries, errors


def _discover_run_configs_with_errors(project_root: Path) -> tuple[list[RunConfigSummary], list[str]]:
    config_dir = project_root / "configs"
    summaries: list[RunConfigSummary] = []
    errors: list[str] = []
    for path in sorted(config_dir.glob("*.yaml")):
        try:
            config = load_run_config(path)
        except Exception as exc:  # noqa: BLE001 - dashboard should report validation/parsing errors without crashing
            errors.append(f"{path.relative_to(project_root)}: {exc}")
            continue
        summaries.append(_summarize_run_config(config=config, path=path.relative_to(project_root)))
    return summaries, errors


def _next_actions(configs: list[RunConfigSummary], scenarios: list[ScenarioSummary]) -> list[str]:
    actions: list[str] = []
    if configs:
        actions.append(f"Open a run config and launch a smoke run: .venv/bin/arcs --config {configs[0].path}")
    else:
        actions.append("Create a run config under configs/ so runs are repeatable.")
    if scenarios:
        actions.append("Review scenario phases and rubric coverage before adding real browser targets.")
    else:
        actions.append("Create at least one scenario under scenarios/.")
    actions.append("Use dedicated test accounts and ignored storage-state files for future browser targets.")
    actions.append("Keep YAML/JSON as the source of truth; the TUI is an operator layer over those files.")
    return actions
