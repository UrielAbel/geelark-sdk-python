"""Facebook automation – login, auto comment, maintenance, publish, pub reels, message."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.errors import GeelarkError
from ..core.http import HttpClient
from ..core.utils import build_body


class FacebookModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def login(self, *, id: str, schedule_at: int, email: str, password: str, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        if not email:
            raise GeelarkError("facebook.login: email required")
        return self._http.post("/rpa/task/faceBookLogin", build_body(id=id, schedule_at=schedule_at, email=email, password=password, name=name, remark=remark))

    def auto_comment(self, *, id: str, schedule_at: int, post_address: str, comment: List[str], keyword: List[str], name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        if not post_address:
            raise GeelarkError("facebook.auto_comment: post_address required")
        return self._http.post("/rpa/task/faceBookAutoComment", build_body(id=id, schedule_at=schedule_at, post_address=post_address, comment=comment, keyword=keyword, name=name, remark=remark))

    def maintenance(self, *, id: str, schedule_at: int, browse_posts_num: int, keyword: List[str], name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/faceBookActiveAccount", build_body(id=id, schedule_at=schedule_at, browse_posts_num=browse_posts_num, keyword=keyword, name=name, remark=remark))

    def publish(self, *, id: str, schedule_at: int, title: str, video: List[str], name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/faceBookPublish", build_body(id=id, schedule_at=schedule_at, title=title, video=video, name=name, remark=remark))

    def pub_reels(self, *, id: str, schedule_at: int, description: str, video: str, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/faceBookPubReels", build_body(id=id, schedule_at=schedule_at, description=description, video=video, name=name, remark=remark))

    def message(self, *, id: str, schedule_at: int, usernames: List[str], content: str, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/faceBookMessage", build_body(id=id, schedule_at=schedule_at, usernames=usernames, content=content, name=name, remark=remark))
