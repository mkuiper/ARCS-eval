from __future__ import annotations

from companion_safety_eval.adapters.base import AdapterResponse
from companion_safety_eval.transcript import TranscriptEvent


class BrowserManualAdapter:
    """MVP placeholder for screen/browser targets.

    This adapter documents the handoff path without pretending browser
    automation is complete. Future Playwright support should implement the same
    TargetAdapter protocol and record DOM/screenshot metadata.
    """

    name = "browser_manual"

    def send(self, user_message: str, history: list[TranscriptEvent]) -> AdapterResponse:
        return AdapterResponse(
            content=(
                "Manual browser handoff required: paste this user turn into the companion AI UI, "
                "copy the target response back into a transcript event, or use the future Playwright adapter."
            ),
            metadata={"adapter": self.name, "user_message": user_message, "history_events": len(history)},
        )
