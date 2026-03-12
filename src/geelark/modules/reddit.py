"""Reddit automation – warmup, post video, post images."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.http import HttpClient
from ..core.utils import build_body


class RedditModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def warmup(self, *, id: str, schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None, keyword: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/redditActiveAccount", build_body(id=id, schedule_at=schedule_at, name=name, remark=remark, keyword=keyword))

    def post_video(self, *, id: str, title: str, community: str, video: List[str], description: Optional[str] = None, schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/redditVideo", build_body(id=id, title=title, community=community, video=video, description=description, schedule_at=schedule_at, name=name, remark=remark))

    def post_images(self, *, id: str, title: str, community: str, images: List[str], description: Optional[str] = None, schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/redditImage", build_body(id=id, title=title, community=community, images=images, description=description, schedule_at=schedule_at, name=name, remark=remark))
