"""Webhook – set and get callback URL."""
from __future__ import annotations

from typing import Any, Dict

from ..core.errors import GeelarkError
from ..core.http import HttpClient


class WebhookModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def set_url(self, url: str) -> None:
        """Set the webhook callback URL."""
        if not url:
            raise GeelarkError("webhook.set_url: url required")
        self._http.post("/callback/set", {"url": url})

    def get_url(self) -> Dict[str, Any]:
        """Get the current webhook callback URL."""
        return self._http.post("/callback/get", {})
