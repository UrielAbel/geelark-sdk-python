from __future__ import annotations

from typing import Any, Optional


class GeelarkError(Exception):
    """Base exception for all GeeLark SDK errors."""

    def __init__(
        self,
        message: str,
        *,
        code: Optional[str] = None,
        endpoint: Optional[str] = None,
        http_status: Optional[int] = None,
        details: Optional[Any] = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.endpoint = endpoint
        self.http_status = http_status
        self.details = details

    def __repr__(self) -> str:
        parts = [f"GeelarkError({self.args[0]!r}"]
        if self.code:
            parts.append(f", code={self.code!r}")
        if self.endpoint:
            parts.append(f", endpoint={self.endpoint!r}")
        if self.http_status:
            parts.append(f", http_status={self.http_status}")
        parts.append(")")
        return "".join(parts)
