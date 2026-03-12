"""Group Management – create, delete, modify, query groups."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.errors import GeelarkError
from ..core.http import HttpClient
from ..core.utils import build_body


class GroupModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def create(self, groups: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not groups:
            raise GeelarkError("group.create: groups list required")
        return self._http.post("/group/add", {"list": groups})

    def delete(self, ids: List[str]) -> Dict[str, Any]:
        if not ids:
            raise GeelarkError("group.delete: ids required")
        return self._http.post("/group/delete", {"ids": ids})

    def modify(self, groups: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not groups:
            raise GeelarkError("group.modify: groups list required")
        return self._http.post("/group/update", {"list": groups})

    def query(self, *, page: int = 1, page_size: int = 10, ids: Optional[List[str]] = None, names: Optional[List[str]] = None, remarks: Optional[List[str]] = None) -> Dict[str, Any]:
        return self._http.post("/group/list", build_body(page=page, page_size=page_size, ids=ids, names=names, remarks=remarks))
