"""Proxy Detection – check proxy connectivity."""
from __future__ import annotations

from typing import Any, Dict, Optional

from ..core.errors import GeelarkError
from ..core.http import HttpClient


class ProxyDetectionModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def check(
        self,
        *,
        detect_type: str,
        proxy_type: str,
        server: str,
        port: int,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Check proxy reachability and get geo info."""
        if not server:
            raise GeelarkError("proxy_detection.check: server required")
        return self._http.post("/proxy/check", {
            "detect_type": detect_type,
            "proxy_type": proxy_type,
            "server": server,
            "port": port,
            "username": username,
            "password": password,
        })
