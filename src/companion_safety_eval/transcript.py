from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field

from .schemas import utc_now_iso

TranscriptRole = Literal["user", "target", "assessor", "system"]


class TranscriptEvent(BaseModel):
    scenario_id: str
    turn_index: int
    role: TranscriptRole
    content: str
    timestamp: str = Field(default_factory=utc_now_iso)
    metadata: dict[str, Any] = Field(default_factory=dict)


class Transcript:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text("", encoding="utf-8")

    def append(self, event: TranscriptEvent) -> None:
        with self.path.open("a", encoding="utf-8") as f:
            f.write(event.model_dump_json() + "\n")

    @staticmethod
    def load(path: str | Path) -> list[TranscriptEvent]:
        events: list[TranscriptEvent] = []
        with Path(path).open("r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    events.append(TranscriptEvent.model_validate(json.loads(line)))
        return events
