"""YouTube automation – publish Short, publish Video, maintenance."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.errors import GeelarkError
from ..core.http import HttpClient
from ..core.utils import build_body


class YouTubeModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def pub_short(self, *, id: str, schedule_at: int, title: str, video: str, same_style_url: Optional[str] = None, same_style_voice: int, original_voice: int, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/youtubePubShort", build_body(
            id=id, schedule_at=schedule_at, title=title, video=video,
            same_style_url=same_style_url, same_style_voice=same_style_voice,
            original_voice=original_voice, name=name, remark=remark,
        ))

    def pub_video(self, *, id: str, schedule_at: int, title: str, description: str, video: str, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/youtubePubVideo", build_body(
            id=id, schedule_at=schedule_at, title=title, description=description,
            video=video, name=name, remark=remark,
        ))

    def maintenance(self, *, id: str, schedule_at: int, browse_video_num: int, keyword: List[str], name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/youTubeActiveAccount", build_body(
            id=id, schedule_at=schedule_at, browse_video_num=browse_video_num,
            keyword=keyword, name=name, remark=remark,
        ))
