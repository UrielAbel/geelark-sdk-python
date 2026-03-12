"""Threads automation – publish video, publish images."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.http import HttpClient
from ..core.utils import build_body


class ThreadsModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def video(self, *, id: str, schedule_at: int, title: str, video: List[str], topic: Optional[str] = None, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/threadsVideo", build_body(id=id, schedule_at=schedule_at, title=title, video=video, topic=topic, name=name, remark=remark))

    def image(self, *, id: str, schedule_at: int, title: str, images: List[str], topic: Optional[str] = None, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/threadsImage", build_body(id=id, schedule_at=schedule_at, title=title, images=images, topic=topic, name=name, remark=remark))
