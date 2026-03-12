"""TikTok automation – video, image set, warmup, login, edit, star, comment, message."""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence

from ..core.errors import GeelarkError
from ..core.http import HttpClient
from ..core.utils import build_body


class TiktokModule:
    """TikTok RPA tasks."""

    def __init__(self, http: HttpClient, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._http = http
        self._d = defaults or {}

    def add_video(
        self,
        *,
        env_id: str,
        video: str,
        plan_name: Optional[str] = None,
        schedule_at: Optional[int] = None,
        video_desc: Optional[str] = None,
        product_id: Optional[str] = None,
        product_title: Optional[str] = None,
        ref_video_id: Optional[str] = None,
        max_try_times: Optional[int] = None,
        timeout_min: Optional[int] = None,
        same_video_volume: Optional[int] = None,
        source_video_volume: Optional[int] = None,
        mark_ai: Optional[bool] = None,
        cover: Optional[str] = None,
        need_share_link: Optional[bool] = None,
    ) -> Dict[str, Any]:
        return self._http.post("/task/addOne", build_body(
            env_id=env_id, video=video, plan_name=plan_name, schedule_at=schedule_at,
            video_desc=video_desc, product_id=product_id, product_title=product_title,
            ref_video_id=ref_video_id, max_try_times=max_try_times, timeout_min=timeout_min,
            same_video_volume=same_video_volume, source_video_volume=source_video_volume,
            mark_ai=mark_ai, cover=cover, need_share_link=need_share_link,
            task_type=self._d.get("taskType", 1),
        ))

    def add_image_set(
        self,
        *,
        env_id: str,
        images: List[str],
        plan_name: Optional[str] = None,
        schedule_at: Optional[int] = None,
        video_desc: Optional[str] = None,
        video_id: Optional[str] = None,
        video_title: Optional[str] = None,
        max_try_times: Optional[int] = None,
        timeout_min: Optional[int] = None,
        same_video_volume: Optional[int] = None,
        mark_ai: Optional[bool] = None,
        need_share_link: Optional[bool] = None,
    ) -> Dict[str, Any]:
        return self._http.post("/task/addOne", build_body(
            env_id=env_id, images=images, plan_name=plan_name, schedule_at=schedule_at,
            video_desc=video_desc, video_id=video_id, video_title=video_title,
            max_try_times=max_try_times, timeout_min=timeout_min,
            same_video_volume=same_video_volume, mark_ai=mark_ai,
            need_share_link=need_share_link, task_type=3,
        ))

    def add_warmup(
        self,
        *,
        env_id: str,
        action: str,
        plan_name: Optional[str] = None,
        schedule_at: Optional[int] = None,
        keywords: Optional[List[str]] = None,
        duration: Optional[int] = None,
    ) -> Dict[str, Any]:
        return self._http.post("/task/addOne", build_body(
            env_id=env_id, action=action, plan_name=plan_name,
            schedule_at=schedule_at, keywords=keywords, duration=duration,
            task_type=2,
        ))

    def login(self, *, id: str, account: str, password: str, schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/tiktokLogin", build_body(id=id, account=account, password=password, schedule_at=schedule_at, name=name, remark=remark))

    def edit_profile(self, *, id: str, schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None, avatar: Optional[str] = None, nick_name: Optional[str] = None, bio: Optional[str] = None, site: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/tiktokEditProfile", build_body(id=id, schedule_at=schedule_at, name=name, remark=remark, avatar=avatar, nick_name=nick_name, bio=bio, site=site))

    def random_star(self, *, id: str, schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/tiktokStar", build_body(id=id, schedule_at=schedule_at, name=name, remark=remark))

    def random_star_asia(self, *, id: str, schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/tiktokStarAsia", build_body(id=id, schedule_at=schedule_at, name=name, remark=remark))

    def random_comment(self, *, id: str, use_ai: int, schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None, comment: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/tiktokRandomComment", build_body(id=id, use_ai=use_ai, schedule_at=schedule_at, name=name, remark=remark, comment=comment))

    def random_comment_asia(self, *, id: str, use_ai: int, schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None, comment: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/tiktokRandomCommentAsia", build_body(id=id, use_ai=use_ai, schedule_at=schedule_at, name=name, remark=remark, comment=comment))

    def message(self, *, id: str, usernames: List[str], content: str, schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/tiktokMessage", build_body(id=id, usernames=usernames, content=content, schedule_at=schedule_at, name=name, remark=remark))

    def message_asia(self, *, id: str, usernames: List[str], content: str, schedule_at: int = 0, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/tiktokMessageAsia", build_body(id=id, usernames=usernames, content=content, schedule_at=schedule_at, name=name, remark=remark))
