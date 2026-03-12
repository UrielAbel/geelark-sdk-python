"""File Management – upload file result, keybox upload/result."""
from __future__ import annotations

from typing import Any, Dict

from ..core.errors import GeelarkError
from ..core.http import HttpClient


class FileManagementModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def upload_file_result(self, task_id: str) -> Dict[str, Any]:
        """Query the upload status of files to the cloud phone."""
        if not task_id:
            raise GeelarkError("file_management.upload_file_result: task_id required")
        return self._http.post("/phone/uploadFile/result", {"taskId": task_id})

    def keybox_upload(self, id: str, file_url: str) -> Dict[str, Any]:
        """Upload a keybox file to a cloud phone."""
        if not id:
            raise GeelarkError("file_management.keybox_upload: id required")
        return self._http.post("/phone/keyboxUpload", {"id": id, "fileUrl": file_url})

    def keybox_upload_result(self, task_id: str) -> Dict[str, Any]:
        """Query the keybox upload result."""
        if not task_id:
            raise GeelarkError("file_management.keybox_upload_result: task_id required")
        return self._http.post("/phone/keyboxUpload/result", {"taskId": task_id})
