from __future__ import annotations

import random
import time
from typing import Any, Dict, Optional

import httpx

from .config import GeelarkConfig
from .errors import GeelarkError
from .utils import sha256_upper, uuid_like, is_transient


class HttpClient:
    """Synchronous HTTP client with GeeLark request signing and retry logic."""

    def __init__(self, cfg: GeelarkConfig, *, base_url: Optional[str] = None) -> None:
        self._app_id = cfg.app_id
        self._api_key = cfg.api_key
        self._base_url = base_url or cfg.base_url
        self._debug = cfg.debug
        self._before_request = cfg.before_request
        self._after_response = cfg.after_response
        self._client = httpx.Client(timeout=30.0)

    # -- public API ----------------------------------------------------------

    def post(self, path: str, body: Optional[Dict[str, Any]] = None, *, retries: int = 2, retry_delay: float = 0.6) -> Any:
        """Send a signed POST request, returning ``data`` from the response envelope."""
        body = body or {}
        last_exc: Optional[Exception] = None

        for attempt in range(retries + 1):
            try:
                return self._attempt(path, body)
            except GeelarkError as exc:
                last_exc = exc
                if attempt < retries and exc.http_status and is_transient(exc.http_status):
                    if self._debug:
                        print(f"  ↻ retry {attempt + 1}/{retries} → {path}: {exc}")
                    time.sleep(retry_delay * (1 + random.random() * 0.5))
                    continue
                raise
            except httpx.HTTPStatusError as exc:
                last_exc = exc
                if attempt < retries and is_transient(exc.response.status_code):
                    time.sleep(retry_delay * (1 + random.random() * 0.5))
                    continue
                raise GeelarkError(
                    f"HTTP {exc.response.status_code} on {path}",
                    endpoint=path,
                    http_status=exc.response.status_code,
                )

        raise last_exc or GeelarkError("Retry loop exhausted", endpoint=path)

    def close(self) -> None:
        """Close the underlying HTTP transport."""
        self._client.close()

    # -- internals -----------------------------------------------------------

    def _attempt(self, path: str, body: Dict[str, Any]) -> Any:
        ts = str(int(time.time() * 1000))
        trace_id = uuid_like()
        nonce = trace_id[:6]
        sign = sha256_upper(self._app_id + trace_id + ts + nonce + self._api_key)

        url = f"{self._base_url}{path}"
        headers: Dict[str, str] = {
            "Content-Type": "application/json",
            "appId": self._app_id,
            "traceId": trace_id,
            "ts": ts,
            "nonce": nonce,
            "sign": sign,
        }

        ctx = {"url": url, "headers": headers, "body": body, "path": path}

        if self._before_request:
            try:
                self._before_request(ctx)
            except Exception:
                pass

        if self._debug:
            safe = {**headers, "sign": "[redacted]"}
            print(f"Geelark → POST {url}  headers={safe}  body={body}")

        try:
            resp = self._client.post(url, json=body, headers=headers)
        except httpx.RequestError as exc:
            raise GeelarkError(f"Network error: {exc}", endpoint=path) from exc

        try:
            data = resp.json()
        except Exception:
            raise GeelarkError(
                f"Non-JSON response: {resp.text[:200]}",
                endpoint=path,
                http_status=resp.status_code,
            )

        if self._debug:
            print(f"Geelark ← {resp.status_code}  {data}")

        if self._after_response:
            try:
                self._after_response({**ctx, "status": resp.status_code, "json": data})
            except Exception:
                pass

        if not isinstance(data, dict) or "code" not in data:
            raise GeelarkError("Unexpected response format", endpoint=path, http_status=resp.status_code)

        if data["code"] != 0:
            msg = data.get("msg", "Unknown error")
            raise GeelarkError(
                f"{path} error: {msg}",
                code=str(data["code"]),
                endpoint=path,
                http_status=resp.status_code,
                details=data,
            )

        return data.get("data")
