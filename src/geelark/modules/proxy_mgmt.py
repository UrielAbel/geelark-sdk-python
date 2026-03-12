"""Proxy Management – add, delete, list, update proxies."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.errors import GeelarkError
from ..core.http import HttpClient
from ..core.utils import build_body


class ProxyMgmtModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def add(self, proxies: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not proxies:
            raise GeelarkError("proxy_mgmt.add: proxies list required")
        return self._http.post("/proxy/add", {"list": proxies})

    def delete(self, ids: List[str]) -> Dict[str, Any]:
        if not ids:
            raise GeelarkError("proxy_mgmt.delete: ids required")
        return self._http.post("/proxy/delete", {"ids": ids})

    def list(self, *, page: int = 1, page_size: int = 10, ids: Optional[List[str]] = None) -> Dict[str, Any]:
        return self._http.post("/proxy/list", build_body(page=page, page_size=page_size, ids=ids))

    def update(self, proxies: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not proxies:
            raise GeelarkError("proxy_mgmt.update: proxies list required")
        return self._http.post("/proxy/update", {"list": proxies})
