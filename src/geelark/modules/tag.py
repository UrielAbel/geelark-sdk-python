"""Tag Management – create, delete, modify, query tags."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.errors import GeelarkError
from ..core.http import HttpClient
from ..core.utils import build_body


class TagModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def create(self, tags: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not tags:
            raise GeelarkError("tag.create: tags list required")
        return self._http.post("/tag/add", {"list": tags})

    def delete(self, ids: List[str]) -> Dict[str, Any]:
        if not ids:
            raise GeelarkError("tag.delete: ids required")
        return self._http.post("/tag/delete", {"ids": ids})

    def modify(self, tags: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not tags:
            raise GeelarkError("tag.modify: tags list required")
        return self._http.post("/tag/update", {"list": tags})

    def query(self, *, page: int = 1, page_size: int = 10, ids: Optional[List[str]] = None, names: Optional[List[str]] = None, colors: Optional[List[str]] = None) -> Dict[str, Any]:
        return self._http.post("/tag/list", build_body(page=page, page_size=page_size, ids=ids, names=names, colors=colors))
