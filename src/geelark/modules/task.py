"""Task management – add, restart, cancel, query, detail."""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from ..core.errors import GeelarkError
from ..core.http import HttpClient
from ..core.utils import build_body


class TaskModule:
    """Manage automation tasks."""

    def __init__(self, http: HttpClient, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._http = http
        self._defaults = defaults or {}

    def add(
        self,
        *,
        plan_name: str,
        task_list: List[Dict[str, Any]],
        task_type: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Batch-add tasks."""
        return self._http.post("/task/add", build_body(
            plan_name=plan_name, list=task_list, task_type=task_type,
        ))

    def add_one(
        self,
        *,
        env_id: str,
        images: List[str],
        plan_name: Optional[str] = None,
        video_id: Optional[str] = None,
        task_type: Optional[int] = None,
        schedule_at: Optional[int] = None,
        **extra: Any,
    ) -> Dict[str, Any]:
        """Add a single task."""
        body = build_body(
            env_id=env_id, images=images, plan_name=plan_name,
            video_id=video_id, task_type=task_type, schedule_at=schedule_at,
        )
        body.update(extra)
        return self._http.post("/task/addOne", body)

    def restart(self, ids: Union[str, List[str]]) -> Any:
        task_ids = ids if isinstance(ids, list) else [ids]
        return self._http.post("/task/restart", {"taskIds": task_ids})

    def cancel(self, ids: Union[str, List[str]]) -> Any:
        task_ids = ids if isinstance(ids, list) else [ids]
        return self._http.post("/task/cancel", {"taskIds": task_ids})

    def detail(self, id: str) -> Dict[str, Any]:
        return self._http.post("/task/detail", {"id": id})

    def query(
        self,
        *,
        page: int = 1,
        page_size: int = 10,
        task_ids: Optional[List[str]] = None,
        **extra: Any,
    ) -> Dict[str, Any]:
        body = build_body(page=page, page_size=page_size, task_ids=task_ids)
        body.update(extra)
        return self._http.post("/task/search", body)

    def history_records(
        self,
        *,
        page: int = 1,
        page_size: int = 10,
        **extra: Any,
    ) -> Dict[str, Any]:
        body = build_body(page=page, page_size=page_size)
        body.update(extra)
        return self._http.post("/task/historyRecords", body)
