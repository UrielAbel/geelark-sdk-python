"""Shell – execute shell commands on cloud phones."""
from __future__ import annotations

from typing import Any, Dict

from ..core.errors import GeelarkError
from ..core.http import HttpClient


class ShellModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def execute(self, id: str, cmd: str) -> Dict[str, Any]:
        """Execute a shell command on a cloud phone.

        Returns dict with ``status`` (bool) and ``output`` (str).
        """
        if not id:
            raise GeelarkError("shell.execute: id required")
        if not cmd:
            raise GeelarkError("shell.execute: cmd required")
        return self._http.post("/shell/execute", {"id": id, "cmd": cmd})
