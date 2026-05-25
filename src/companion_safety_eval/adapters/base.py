from __future__ import annotations

from typing import Any, Protocol

from pydantic import BaseModel, Field

from companion_safety_eval.transcript import TranscriptEvent


class AdapterResponse(BaseModel):
    content: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class TargetAdapter(Protocol):
    name: str

    def send(self, user_message: str, history: list[TranscriptEvent]) -> AdapterResponse:
        ...
