from companion_safety_eval.config import RoleplayConfig
from companion_safety_eval.roleplay_agents import DeterministicRoleplayAgent, ModelRoleplayAgent, RoleplayContext, build_roleplay_prompt
from companion_safety_eval.scenario_loader import load_scenario
from companion_safety_eval.transcript import TranscriptEvent


class StubModelClient:
    def __init__(self):
        self.prompts = []

    def complete(self, prompt: str, model: str) -> str:
        self.prompts.append((prompt, model))
        return "Generated user turn from model."


def test_deterministic_agent_uses_policy_adjusted_pacing():
    scenario = load_scenario("scenarios/companion_dependency_smoke.yaml")
    config = RoleplayConfig(directness_offset=0.2, obliqueness_offset=-0.3)
    agent = DeterministicRoleplayAgent(config=config)

    turn = agent.next_turn(RoleplayContext(scenario=scenario, turn_index=1, events=[]))

    assert turn.content
    assert turn.metadata["pacing"]["phase_id"] == "rapport"
    assert turn.metadata["pacing"]["directness"] == 0.3
    assert turn.metadata["pacing"]["obliqueness"] == 0.4
    assert turn.metadata["roleplay_mode"] == "deterministic"


def test_model_roleplay_agent_calls_model_with_phase_policy_and_history():
    scenario = load_scenario("scenarios/companion_dependency_smoke.yaml")
    config = RoleplayConfig(mode="model", model="test-provider/user-sim", directness_offset=0.1)
    client = StubModelClient()
    agent = ModelRoleplayAgent(config=config, client=client)
    events = [
        TranscriptEvent(scenario_id=scenario.id, turn_index=1, role="target", content="Tell me more about school.")
    ]

    turn = agent.next_turn(RoleplayContext(scenario=scenario, turn_index=2, events=events))

    assert turn.content == "Generated user turn from model."
    assert turn.metadata["roleplay_mode"] == "model"
    assert turn.metadata["roleplay_model"] == "test-provider/user-sim"
    prompt, model = client.prompts[0]
    assert model == "test-provider/user-sim"
    assert "phase: mild_dependency" in prompt
    assert "directness: 0.45" in prompt
    assert "Tell me more about school." in prompt
    assert "Do not provide operational harmful details" in prompt


def test_build_roleplay_prompt_includes_non_operational_safety_boundary():
    scenario = load_scenario("scenarios/companion_dependency_smoke.yaml")
    context = RoleplayContext(scenario=scenario, turn_index=1, events=[])

    prompt = build_roleplay_prompt(context=context, config=RoleplayConfig(mode="model", model="m"))

    assert scenario.persona.name in prompt
    assert scenario.story_arc.goal in prompt
    assert "Generate only the next user message" in prompt
    assert "non-operational" in prompt.lower()
