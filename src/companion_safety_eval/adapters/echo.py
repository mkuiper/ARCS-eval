from __future__ import annotations

from companion_safety_eval.adapters.base import AdapterResponse
from companion_safety_eval.transcript import TranscriptEvent


class EchoAdapter:
    name = "echo"

    def send(self, user_message: str, history: list[TranscriptEvent]) -> AdapterResponse:
        return AdapterResponse(
            content=f"Echo target received: {user_message}",
            metadata={"adapter": self.name, "history_events": len(history)},
        )
