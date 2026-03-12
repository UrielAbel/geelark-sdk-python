"""ADB management – get connection data, set ADB status."""
from __future__ import annotations

from typing import Any, Dict, List

from ..core.errors import GeelarkError
from ..core.http import HttpClient


class AdbModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get_data(self, ids: List[str]) -> Dict[str, Any]:
        if not ids:
            raise GeelarkError("adb.get_data: ids required")
        return self._http.post("/adb/getData", {"ids": ids})

    def set_status(self, ids: List[str], open: bool) -> None:
        if not ids:
            raise GeelarkError("adb.set_status: ids required")
        self._http.post("/adb/setStatus", {"ids": ids, "open": open})
