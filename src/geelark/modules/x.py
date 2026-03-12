"""X (Twitter) automation – publish content."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.http import HttpClient
from ..core.utils import build_body


class XModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def publish(self, *, id: str, schedule_at: int, description: str, video: List[str], name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/xPublish", build_body(id=id, schedule_at=schedule_at, description=description, video=video, name=name, remark=remark))
