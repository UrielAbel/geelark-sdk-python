from __future__ import annotations

import hashlib
import time
import uuid
from typing import Any, Dict


def sha256_upper(text: str) -> str:
    """SHA-256 hash, returned as uppercase hex."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def uuid_like() -> str:
    """Generate a UUID v4 string (no dashes)."""
    return uuid.uuid4().hex


def now_sec() -> int:
    """Current time as seconds since epoch."""
    return int(time.time())


def _to_camel(name: str) -> str:
    """Convert snake_case to camelCase.

    Examples:
        >>> _to_camel("page_size")
        'pageSize'
        >>> _to_camel("id")
        'id'
        >>> _to_camel("browse_posts_num")
        'browsePostsNum'
    """
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


def build_body(**kwargs: Any) -> Dict[str, Any]:
    """Build an API request body from keyword arguments.

    - Converts snake_case keys to camelCase.
    - Omits keys whose value is ``None``.
    """
    return {_to_camel(k): v for k, v in kwargs.items() if v is not None}


def is_transient(status: int) -> bool:
    """Return True if the HTTP status code is transient (retryable)."""
    return status in (429, 502, 503, 504)
