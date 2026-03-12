"""Google automation – login, app download, app browser."""
from __future__ import annotations

from typing import Any, Dict, Optional

from ..core.http import HttpClient
from ..core.utils import build_body


class GoogleModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def login(self, *, id: str, schedule_at: int, email: str, password: str, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/googleLogin", build_body(id=id, schedule_at=schedule_at, email=email, password=password, name=name, remark=remark))

    def app_download(self, *, id: str, schedule_at: int, app_name: str, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/googleAppDownload", build_body(id=id, schedule_at=schedule_at, app_name=app_name, name=name, remark=remark))

    def app_browser(self, *, id: str, schedule_at: int, app_name: str, description: Optional[str] = None, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/googleAppBrowser", build_body(id=id, schedule_at=schedule_at, app_name=app_name, description=description, name=name, remark=remark))
