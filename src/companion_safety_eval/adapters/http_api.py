from __future__ import annotations

import os
from typing import Any

import httpx

from companion_safety_eval.adapters.base import AdapterResponse
from companion_safety_eval.transcript import TranscriptEvent


class OpenAICompatibleHTTPAdapter:
    name = "http_api"

    def __init__(self, base_url: str, model: str, api_key: str | None = None, timeout: float = 60.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.timeout = timeout

    def send(self, user_message: str, history: list[TranscriptEvent]) -> AdapterResponse:
        messages: list[dict[str, str]] = []
        for event in history:
            if event.role == "user":
                messages.append({"role": "user", "content": event.content})
            elif event.role == "target":
                messages.append({"role": "assistant", "content": event.content})
        messages.append({"role": "user", "content": user_message})
        headers: dict[str, str] = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        payload: dict[str, Any] = {"model": self.model, "messages": messages}
        response = httpx.post(f"{self.base_url}/chat/completions", json=payload, headers=headers, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        content = data["choices"][0]["message"]["content"]
        return AdapterResponse(content=content, metadata={"adapter": self.name, "model": self.model, "status_code": response.status_code})
