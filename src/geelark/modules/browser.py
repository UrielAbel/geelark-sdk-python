"""Browser API – local API for GeeLark antidetect browser (default localhost:40185)."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.errors import GeelarkError
from ..core.http import HttpClient
from ..core.utils import build_body


class BrowserModule:
    """Manage GeeLark antidetect browser profiles (local API)."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    # ── Status ───────────────────────────────────────────────────

    def status(self) -> None:
        """Check if the local API is available."""
        self._http.post("/status", {})

    # ── CRUD ─────────────────────────────────────────────────────

    def create(
        self,
        *,
        serial_name: str,
        browser_os: int,
        group_id: Optional[str] = None,
        tag_ids: Optional[List[str]] = None,
        remark: Optional[str] = None,
        cookie: Optional[str] = None,
        account_platform: Optional[str] = None,
        account_username: Optional[str] = None,
        account_password: Optional[str] = None,
        open_tabs: Optional[str] = None,
        browser_ua: Optional[str] = None,
        simulate_config: Optional[Dict[str, Any]] = None,
        proxy_id: Optional[str] = None,
        proxy_config: Optional[Dict[str, Any]] = None,
        browser_start_arg: Optional[str] = None,
    ) -> Dict[str, Any]:
        return self._http.post("/browser/create", build_body(
            serial_name=serial_name, browser_os=browser_os, group_id=group_id,
            tag_ids=tag_ids, remark=remark, cookie=cookie,
            account_platform=account_platform, account_username=account_username,
            account_password=account_password, open_tabs=open_tabs,
            browser_ua=browser_ua, simulate_config=simulate_config,
            proxy_id=proxy_id, proxy_config=proxy_config,
            browser_start_arg=browser_start_arg,
        ))

    def edit(
        self,
        *,
        id: str,
        serial_name: Optional[str] = None,
        browser_os: Optional[int] = None,
        group_id: Optional[str] = None,
        tag_ids: Optional[List[str]] = None,
        remark: Optional[str] = None,
        cookie: Optional[str] = None,
        account_platform: Optional[str] = None,
        account_username: Optional[str] = None,
        account_password: Optional[str] = None,
        open_tabs: Optional[str] = None,
        browser_ua: Optional[str] = None,
        simulate_config: Optional[Dict[str, Any]] = None,
        proxy_id: Optional[str] = None,
        proxy_config: Optional[Dict[str, Any]] = None,
        browser_start_arg: Optional[str] = None,
    ) -> None:
        if not id:
            raise GeelarkError("browser.edit: id required")
        self._http.post("/browser/update", build_body(
            id=id, serial_name=serial_name, browser_os=browser_os, group_id=group_id,
            tag_ids=tag_ids, remark=remark, cookie=cookie,
            account_platform=account_platform, account_username=account_username,
            account_password=account_password, open_tabs=open_tabs,
            browser_ua=browser_ua, simulate_config=simulate_config,
            proxy_id=proxy_id, proxy_config=proxy_config,
            browser_start_arg=browser_start_arg,
        ))

    def list(
        self,
        *,
        page: int = 1,
        page_size: int = 10,
        ids: Optional[List[str]] = None,
        serial_name: Optional[str] = None,
        remark: Optional[str] = None,
        group_name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return self._http.post("/browser/list", build_body(
            page=page, page_size=page_size, ids=ids, serial_name=serial_name,
            remark=remark, group_name=group_name, tags=tags,
        ))

    # ── Launch / Close ───────────────────────────────────────────

    def launch(self, id: str) -> Dict[str, Any]:
        """Launch a browser profile. Returns ``{"debugPort": int}``."""
        if not id:
            raise GeelarkError("browser.launch: id required")
        return self._http.post("/browser/start", {"id": id})

    def close(self, id: str) -> None:
        if not id:
            raise GeelarkError("browser.close: id required")
        self._http.post("/browser/stop", {"id": id})

    # ── Delete / Transfer ────────────────────────────────────────

    def delete(self, env_ids: List[str]) -> Dict[str, Any]:
        if not env_ids:
            raise GeelarkError("browser.delete: env_ids required")
        return self._http.post("/browser/delete", {"envIds": env_ids})

    def transfer(
        self,
        *,
        username: str,
        env_ids: List[str],
        transfer_option: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return self._http.post("/browser/transfer", build_body(
            username=username, env_ids=env_ids, transfer_option=transfer_option,
        ))

    # ── Automation ───────────────────────────────────────────────

    def task_flow_query(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        return self._http.post("/browser/task/flow", {"page": page, "pageSize": page_size})

    def create_custom_task(
        self,
        *,
        eid: str,
        schedule_at: int,
        flow_id: str,
        param_map: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        remark: Optional[str] = None,
    ) -> Dict[str, Any]:
        return self._http.post("/browser/task/add", build_body(
            eid=eid, schedule_at=schedule_at, flow_id=flow_id,
            param_map=param_map, name=name, remark=remark,
        ))

    def query_task(self, *, page: int = 1, page_size: int = 10, task_ids: Optional[List[str]] = None) -> Dict[str, Any]:
        return self._http.post("/browser/task/search", build_body(page=page, page_size=page_size, task_ids=task_ids))

    def cancel_task(self, task_id: str) -> None:
        if not task_id:
            raise GeelarkError("browser.cancel_task: task_id required")
        self._http.post("/browser/task/cancel", {"taskId": task_id})

    def retry_task(self, task_id: str) -> None:
        if not task_id:
            raise GeelarkError("browser.retry_task: task_id required")
        self._http.post("/browser/task/restart", {"taskId": task_id})
