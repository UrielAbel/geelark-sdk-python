"""Pinterest automation – publish video, publish images."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.http import HttpClient
from ..core.utils import build_body


class PinterestModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def video(self, *, id: str, schedule_at: int, title: str, description: str, video: List[str], link: Optional[str] = None, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/pinterestVideo", build_body(id=id, schedule_at=schedule_at, title=title, description=description, video=video, link=link, name=name, remark=remark))

    def image(self, *, id: str, schedule_at: int, title: str, description: str, images: List[str], link: Optional[str] = None, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/pinterestImage", build_body(id=id, schedule_at=schedule_at, title=title, description=description, images=images, link=link, name=name, remark=remark))
