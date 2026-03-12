"""Instagram automation – login, pub reels (video/image), warmup, message."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.http import HttpClient
from ..core.utils import build_body


class InstagramModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def login(self, *, id: str, account: str, password: str, schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/instagramLogin", build_body(id=id, account=account, password=password, schedule_at=schedule_at, name=name, remark=remark))

    def pub_reels(self, *, id: str, description: str, video: List[str], schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/instagramPubReels", build_body(id=id, description=description, video=video, schedule_at=schedule_at, name=name, remark=remark))

    def pub_reels_images(self, *, id: str, description: str, image: List[str], schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/instagramPubReelsImage", build_body(id=id, description=description, image=image, schedule_at=schedule_at, name=name, remark=remark))

    def warmup(self, *, id: str, browse_video: int, schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/instagramActiveAccount", build_body(id=id, browse_video=browse_video, schedule_at=schedule_at, name=name, remark=remark))

    def message(self, *, id: str, usernames: List[str], content: str, schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/instagramMessage", build_body(id=id, usernames=usernames, content=content, schedule_at=schedule_at, name=name, remark=remark))
