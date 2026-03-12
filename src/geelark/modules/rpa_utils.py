"""RPA utility tasks – multichannel, file upload, contacts, keybox, flows."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.http import HttpClient
from ..core.utils import build_body


class RpaUtilsModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def multi_platform_video_distribution(self, *, id: str, schedule_at: int, title: str, video: List[str], name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/multiPlatformVideoDistribution", build_body(id=id, schedule_at=schedule_at, title=title, video=video, name=name, remark=remark))

    def file_upload(self, *, id: str, schedule_at: int, files: List[str], name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/fileUpload", build_body(id=id, schedule_at=schedule_at, files=files, name=name, remark=remark))

    def import_contacts(self, *, id: str, schedule_at: int, contacts: List[Dict[str, Any]], name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/importContacts", build_body(id=id, schedule_at=schedule_at, contacts=contacts, name=name, remark=remark))

    def keybox_upload(self, *, id: str, schedule_at: int, files: List[str], name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/rpa/task/keyboxUpload", build_body(id=id, schedule_at=schedule_at, files=files, name=name, remark=remark))

    def flow_list(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        return self._http.post("/task/flow/list", build_body(page=page, page_size=page_size))

    def rpa_add(self, *, id: str, schedule_at: int, flow_id: str, param_map: Optional[Dict[str, Any]] = None, name: Optional[str] = None, remark: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/task/rpa/add", build_body(id=id, schedule_at=schedule_at, flow_id=flow_id, param_map=param_map, name=name, remark=remark))
