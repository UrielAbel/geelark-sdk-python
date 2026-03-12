"""SHEIN automation – auto login."""
from __future__ import annotations

from typing import Any, Dict, Optional

from ..core.http import HttpClient
from ..core.utils import build_body


class SheinModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def login(self, *, id: str, schedule_at: int, email: str, password: str, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/sheinLogin", build_body(id=id, schedule_at=schedule_at, email=email, password=password, name=name, remark=remark))
