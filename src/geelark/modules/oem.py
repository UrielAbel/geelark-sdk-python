"""OEM / White Label – customisation settings."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.http import HttpClient
from ..core.utils import build_body


class OemModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def customization(
        self,
        *,
        title: Optional[str] = None,
        logo: Optional[str] = None,
        hide_header: Optional[bool] = None,
        mirror_url: Optional[str] = None,
        tool_bar_settings: Optional[List[Dict[str, Any]]] = None,
    ) -> None:
        self._http.post("/phone/customization", build_body(
            title=title, logo=logo, hide_header=hide_header,
            mirror_url=mirror_url, tool_bar_settings=tool_bar_settings,
        ))
