"""Library – material and tag management."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.errors import GeelarkError
from ..core.http import HttpClient
from ..core.utils import build_body


class LibraryModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def create_material(self, *, url: str, tags_id: Optional[List[str]] = None, file_name: Optional[str] = None) -> Dict[str, Any]:
        if not url:
            raise GeelarkError("library.create_material: url required")
        return self._http.post("/material/create", build_body(url=url, tags_id=tags_id, file_name=file_name))

    def create_tag(self, *, name: str, color: Optional[int] = None) -> Dict[str, Any]:
        if not name:
            raise GeelarkError("library.create_tag: name required")
        return self._http.post("/material/tag/create", build_body(name=name, color=color))

    def delete_material(self, ids: List[str]) -> Dict[str, Any]:
        if not ids:
            raise GeelarkError("library.delete_material: ids required")
        return self._http.post("/material/del", {"ids": ids})

    def delete_tag(self, ids: List[str]) -> Dict[str, Any]:
        if not ids:
            raise GeelarkError("library.delete_tag: ids required")
        return self._http.post("/material/tag/del", {"ids": ids})

    def search_material(self, *, page: Optional[int] = None, page_size: Optional[int] = None, file_name: Optional[str] = None, tags_id: Optional[List[str]] = None, source: Optional[int] = None, file_type: Optional[List[int]] = None, ids: Optional[List[str]] = None) -> Dict[str, Any]:
        return self._http.post("/material/search", build_body(page=page, page_size=page_size, file_name=file_name, tags_id=tags_id, source=source, file_type=file_type, ids=ids))

    def search_material_tag(self, *, page: Optional[int] = None, page_size: Optional[int] = None, name: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/material/tag/search", build_body(page=page, page_size=page_size, name=name))

    def set_material_tag(self, materials_id: List[str], tags_id: Optional[List[str]] = None) -> Dict[str, Any]:
        if not materials_id:
            raise GeelarkError("library.set_material_tag: materials_id required")
        return self._http.post("/material/tag/set", {"materialsId": materials_id, "tagsId": tags_id})
