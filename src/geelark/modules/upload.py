"""File upload to GeeLark temporary storage."""
from __future__ import annotations

from typing import Any, Dict

from ..core.errors import GeelarkError
from ..core.http import HttpClient


class UploadModule:
    """Upload temporary files to GeeLark cloud."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get_url(self, file_type: str) -> Dict[str, str]:
        """Get a pre-signed upload URL.

        Returns dict with ``uploadUrl`` and ``resourceUrl``.
        """
        if not file_type:
            raise GeelarkError("upload.get_url: file_type required")
        return self._http.post("/upload/getUrl", {"fileType": file_type})

    def put(self, upload_url: str, file_path: str) -> bool:
        """Upload a local file to the pre-signed URL using httpx.

        Returns True on success.
        """
        import httpx

        with open(file_path, "rb") as f:
            resp = httpx.put(upload_url, content=f, timeout=120.0)
        return resp.status_code == 200
