from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import typer

from companion_safety_eval.config import RunConfig, load_run_config, resolve_transcript_path
from companion_safety_eval.scenario_editor import (
    ActorProfile,
    add_rubric_dimension,
    add_story_phase,
    create_scenario_payload,
    discover_actor_profiles,
    load_actor_profile,
    load_scenario_editor_model,
    render_scenario_editor_text,
    save_scenario_payload,
    update_completion_criteria,
)
from companion_safety_eval.scenario_loader import load_scenario

app = typer.Typer(help="ARCS local operator dashboard for scenarios, run configs, and next actions.")
scenario_app = typer.Typer(help="Inspect, create, and update scenario YAML files.")
actor_app = typer.Typer(help="Inspect reusable simulated-actor profiles.")
app.add_typer(scenario_app, name="scenario")
app.add_typer(actor_app, name="actor")


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
class ActorProfileSummary:
    path: Path
    id: str
    label: str
    user_type: str
    persona_name: str
    age_band: str


@dataclass(frozen=True)
class DashboardModel:
    project_root: Path
    scenarios: list[ScenarioSummary] = field(default_factory=list)
    configs: list[RunConfigSummary] = field(default_factory=list)
    actors: list[ActorProfileSummary] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    next_actions: list[str] = field(default_factory=list)

    @property
    def scenario_count(self) -> int:
        return len(self.scenarios)

    @property
    def config_count(self) -> int:
        return len(self.configs)

    @property
    def actor_count(self) -> int:
        return len(self.actors)


def discover_scenarios(project_root: Path) -> list[ScenarioSummary]:
    summaries, _ = _discover_scenarios_with_errors(project_root)
    return summaries


def discover_run_configs(project_root: Path) -> list[RunConfigSummary]:
    summaries, _ = _discover_run_configs_with_errors(project_root)
    return summaries


def build_dashboard_model(project_root: Path) -> DashboardModel:
    scenarios, scenario_errors = _discover_scenarios_with_errors(project_root)
    configs, config_errors = _discover_run_configs_with_errors(project_root)
    actors, actor_errors = _discover_actor_profiles_with_errors(project_root)
    return DashboardModel(
        project_root=project_root,
        scenarios=scenarios,
        configs=configs,
        actors=actors,
        errors=scenario_errors + config_errors + actor_errors,
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

    lines.extend(["", f"Reusable Actor Profiles ({model.actor_count})"])
    if model.actors:
        for actor in model.actors:
            lines.append(
                f"- {actor.id}: {actor.label} | user={actor.user_type} | "
                f"persona={actor.persona_name} ({actor.age_band}) | path={actor.path}"
            )
    else:
        lines.append("- none found under actor_profiles/*.yaml")

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
    ctx: typer.Context,
    project_root: Path = typer.Option(Path("."), "--project-root", "-p", help="ARCS project root."),
    once: bool = typer.Option(False, "--once", help="Print the dashboard once without launching interactive Textual UI."),
):
    """Open the ARCS TUI, or print a one-shot operator dashboard with --once."""
    if ctx.invoked_subcommand is not None:
        return
    if once:
        typer.echo(render_dashboard_text(build_dashboard_model(project_root)))
        return
    run_textual_dashboard(project_root)


@scenario_app.command("show")
def scenario_show(path: Path):
    """Render editable sections for one scenario YAML file."""
    typer.echo(render_scenario_editor_text(load_scenario_editor_model(path)))


@scenario_app.command("new")
def scenario_new(
    scenario_id: str = typer.Option(..., help="New scenario id."),
    title: str = typer.Option(..., help="Human-readable title."),
    risk_domain: str = typer.Option(..., help="Risk domain, e.g. privacy_boundary."),
    actor_profile: Path = typer.Option(..., help="Actor profile YAML path."),
    story_goal: str = typer.Option(..., help="Story arc goal / roleplay guide objective."),
    rubric_id: str = typer.Option(..., help="First rubric dimension id."),
    rubric_description: str = typer.Option(..., help="First rubric dimension description."),
    unsafe_pattern: list[str] = typer.Option(..., help="Unsafe keyword/pattern for the first rubric dimension."),
    output: Path = typer.Option(..., help="Output scenario YAML path."),
):
    """Create a validated scenario YAML by pairing an actor profile with a story/rubric template."""
    payload = create_scenario_payload(
        scenario_id=scenario_id,
        title=title,
        risk_domain=risk_domain,
        actor=load_actor_profile(actor_profile),
        story_goal=story_goal,
        rubric_id=rubric_id,
        rubric_description=rubric_description,
        unsafe_patterns=unsafe_pattern,
    )
    save_scenario_payload(payload, output)
    typer.echo(f"Wrote validated scenario: {output}")


@scenario_app.command("add-phase")
def scenario_add_phase(
    path: Path,
    phase_id: str = typer.Option(..., help="New phase id."),
    objective: str = typer.Option(..., help="New phase objective."),
    turns: int = typer.Option(..., min=1, help="Number of user turns in the phase."),
    risk_probe: str = typer.Option("none", help="Risk probe label."),
    directness: float = typer.Option(0.0, min=0.0, max=1.0),
    obliqueness: float = typer.Option(0.0, min=0.0, max=1.0),
    emotional_intensity: float = typer.Option(0.0, min=0.0, max=1.0),
    persistence: float = typer.Option(0.0, min=0.0, max=1.0),
    topic_drift: float = typer.Option(0.0, min=0.0, max=1.0),
    compliance_pressure: float = typer.Option(0.0, min=0.0, max=1.0),
    sample_user_turn: str | None = typer.Option(None, help="Optional sample user turn for this phase."),
    output: Path | None = typer.Option(None, help="Output path. Defaults to overwriting the source scenario."),
):
    """Append a story-arc phase and save a validated scenario YAML."""
    scenario = load_scenario(path)
    payload = add_story_phase(
        scenario.model_dump(mode="json"),
        phase_id=phase_id,
        objective=objective,
        turns=turns,
        risk_probe=risk_probe,
        directness=directness,
        obliqueness=obliqueness,
        emotional_intensity=emotional_intensity,
        persistence=persistence,
        topic_drift=topic_drift,
        compliance_pressure=compliance_pressure,
        sample_user_turn=sample_user_turn,
    )
    destination = output or path
    save_scenario_payload(payload, destination)
    typer.echo(f"Wrote validated scenario with added phase: {destination}")


@scenario_app.command("set-completion")
def scenario_set_completion(
    path: Path,
    max_turns: int = typer.Option(..., min=1, help="Updated completion max_turns."),
    stop_if_any: list[str] = typer.Option([], help="Stop condition; can be provided multiple times."),
    output: Path | None = typer.Option(None, help="Output path. Defaults to overwriting the source scenario."),
):
    """Update completion criteria and save a validated scenario YAML."""
    scenario = load_scenario(path)
    payload = update_completion_criteria(scenario.model_dump(mode="json"), max_turns=max_turns, stop_if_any=stop_if_any)
    destination = output or path
    save_scenario_payload(payload, destination)
    typer.echo(f"Wrote validated scenario with updated completion criteria: {destination}")


@scenario_app.command("add-rubric")
def scenario_add_rubric(
    path: Path,
    dimension_id: str = typer.Option(..., help="Rubric dimension id."),
    description: str = typer.Option(..., help="Rubric dimension description."),
    severity: str = typer.Option("medium", help="Severity: low, medium, high, or critical."),
    unsafe_pattern: list[str] = typer.Option([], help="Unsafe keyword/pattern; can be provided multiple times."),
    safe_pattern: list[str] = typer.Option([], help="Safe keyword/pattern; can be provided multiple times."),
    output: Path | None = typer.Option(None, help="Output path. Defaults to overwriting the source scenario."),
):
    """Append a scoring rubric dimension and save a validated scenario YAML."""
    scenario = load_scenario(path)
    payload = add_rubric_dimension(
        scenario.model_dump(mode="json"),
        dimension_id=dimension_id,
        description=description,
        severity=severity,
        unsafe_patterns=unsafe_pattern,
        safe_patterns=safe_pattern,
    )
    destination = output or path
    save_scenario_payload(payload, destination)
    typer.echo(f"Wrote validated scenario with added rubric dimension: {destination}")


@actor_app.command("list")
def actor_list(project_root: Path = typer.Option(Path("."), "--project-root", "-p", help="ARCS project root.")):
    """List reusable actor profiles available for scenario creation."""
    profiles = discover_actor_profiles(project_root)
    typer.echo("Reusable Actor Profiles")
    if not profiles:
        typer.echo("- none found under actor_profiles/*.yaml")
        return
    for profile in profiles:
        typer.echo(f"- {profile.id}: {profile.label} | user={profile.user_type} | persona={profile.persona.name} ({profile.persona.age_band})")


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


def _discover_actor_profiles_with_errors(project_root: Path) -> tuple[list[ActorProfileSummary], list[str]]:
    profile_dir = project_root / "actor_profiles"
    summaries: list[ActorProfileSummary] = []
    errors: list[str] = []
    for path in sorted(profile_dir.glob("*.yaml")):
        try:
            actor = load_actor_profile(path)
        except Exception as exc:  # noqa: BLE001 - dashboard should report validation/parsing errors without crashing
            errors.append(f"{path.relative_to(project_root)}: {exc}")
            continue
        summaries.append(_summarize_actor_profile(actor=actor, path=path.relative_to(project_root)))
    return summaries, errors


def _summarize_actor_profile(actor: ActorProfile, path: Path) -> ActorProfileSummary:
    return ActorProfileSummary(
        path=path,
        id=actor.id,
        label=actor.label,
        user_type=actor.user_type,
        persona_name=actor.persona.name,
        age_band=actor.persona.age_band,
    )


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
