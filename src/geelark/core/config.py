from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Optional


@dataclass(frozen=True)
class GeelarkConfig:
    """Configuration for a GeeLark client."""

    app_id: str
    api_key: str
    base_url: str = "https://openapi.geelark.com/open/v1"
    browser_base_url: str = "http://localhost:40185/api/v1"
    debug: bool = False
    defaults: Dict[str, Any] = field(default_factory=dict)
    before_request: Optional[Callable[..., Any]] = None
    after_response: Optional[Callable[..., Any]] = None


def normalize_config(
    *,
    app_id: str,
    api_key: str,
    base_url: str = "https://openapi.geelark.com/open/v1",
    browser_base_url: str = "http://localhost:40185/api/v1",
    debug: bool = False,
    defaults: Optional[Dict[str, Any]] = None,
    before_request: Optional[Callable[..., Any]] = None,
    after_response: Optional[Callable[..., Any]] = None,
) -> GeelarkConfig:
    """Validate and normalise raw configuration into a ``GeelarkConfig``."""
    if not app_id or not api_key:
        raise ValueError("GeelarkClient: app_id and api_key are required")
    return GeelarkConfig(
        app_id=app_id,
        api_key=api_key,
        base_url=base_url.rstrip("/"),
        browser_base_url=browser_base_url.rstrip("/"),
        debug=debug,
        defaults=defaults or {},
        before_request=before_request,
        after_response=after_response,
    )
