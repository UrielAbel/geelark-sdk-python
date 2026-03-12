"""Main GeelarkClient – wires all modules together."""
from __future__ import annotations

from typing import Any, Callable, Dict, Optional

from .core.config import GeelarkConfig, normalize_config
from .core.http import HttpClient
from .core.utils import now_sec

# Cloud phone modules
from .modules.phone import PhoneModule
from .modules.upload import UploadModule
from .modules.task import TaskModule
from .modules.adb import AdbModule
from .modules.analytics import AnalyticsModule
from .modules.app import AppModule
from .modules.file_management import FileManagementModule
from .modules.library import LibraryModule
from .modules.shell import ShellModule
from .modules.webhook import WebhookModule
from .modules.oem import OemModule

# Social media / RPA modules
from .modules.tiktok import TiktokModule
from .modules.instagram import InstagramModule
from .modules.reddit import RedditModule
from .modules.youtube import YouTubeModule
from .modules.google import GoogleModule
from .modules.shein import SheinModule
from .modules.x import XModule
from .modules.pinterest import PinterestModule
from .modules.threads import ThreadsModule
from .modules.facebook import FacebookModule
from .modules.rpa_utils import RpaUtilsModule

# Management modules
from .modules.billing import BillingModule
from .modules.group import GroupModule
from .modules.proxy_mgmt import ProxyMgmtModule
from .modules.tag import TagModule
from .modules.proxy_detection import ProxyDetectionModule

# Browser API (local)
from .modules.browser import BrowserModule


class GeelarkClient:
    """Full-featured GeeLark SDK client.

    Usage::

        from geelark import GeelarkClient

        client = GeelarkClient(app_id="YOUR_APP_ID", api_key="YOUR_API_KEY")

        # Cloud phones
        phones = client.phone.list(page=1, page_size=5)

        # Social media automation
        client.tiktok.login(id="phone_id", account="user", password="pass", schedule_at=0)

        # Browser API (local)
        client.browser.status()
    """

    def __init__(
        self,
        app_id: str,
        api_key: str,
        *,
        base_url: str = "https://openapi.geelark.com/open/v1",
        browser_base_url: str = "http://localhost:40185/api/v1",
        debug: bool = False,
        defaults: Optional[Dict[str, Any]] = None,
        before_request: Optional[Callable[..., Any]] = None,
        after_response: Optional[Callable[..., Any]] = None,
    ) -> None:
        self._cfg = normalize_config(
            app_id=app_id,
            api_key=api_key,
            base_url=base_url,
            browser_base_url=browser_base_url,
            debug=debug,
            defaults=defaults,
            before_request=before_request,
            after_response=after_response,
        )
        self._http = HttpClient(self._cfg)
        self._browser_http = HttpClient(self._cfg, base_url=self._cfg.browser_base_url)

        # ── Cloud Phone ──────────────────────────────────────────
        self.phone = PhoneModule(self._http)
        self.upload = UploadModule(self._http)
        self.task = TaskModule(self._http, self._cfg.defaults)
        self.adb = AdbModule(self._http)
        self.analytics = AnalyticsModule(self._http)
        self.app = AppModule(self._http)
        self.file_management = FileManagementModule(self._http)
        self.library = LibraryModule(self._http)
        self.shell = ShellModule(self._http)
        self.webhook = WebhookModule(self._http)
        self.oem = OemModule(self._http)

        # ── Social Media / RPA ───────────────────────────────────
        self.tiktok = TiktokModule(self._http, self._cfg.defaults)
        self.instagram = InstagramModule(self._http)
        self.reddit = RedditModule(self._http)
        self.youtube = YouTubeModule(self._http)
        self.google = GoogleModule(self._http)
        self.shein = SheinModule(self._http)
        self.x = XModule(self._http)
        self.pinterest = PinterestModule(self._http)
        self.threads = ThreadsModule(self._http)
        self.facebook = FacebookModule(self._http)
        self.rpa_utils = RpaUtilsModule(self._http)

        # ── Management ───────────────────────────────────────────
        self.billing = BillingModule(self._http)
        self.group = GroupModule(self._http)
        self.proxy_mgmt = ProxyMgmtModule(self._http)
        self.tag = TagModule(self._http)
        self.proxy_detection = ProxyDetectionModule(self._http)

        # ── Browser API (local) ──────────────────────────────────
        self.browser = BrowserModule(self._browser_http)

    # ── Convenience helpers ──────────────────────────────────────

    def request(self, path: str, body: Optional[Dict[str, Any]] = None, *, retries: int = 2, retry_delay: float = 0.6) -> Any:
        """Send a raw signed POST request to any Cloud Phone API path."""
        return self._http.post(path, body, retries=retries, retry_delay=retry_delay)

    def browser_request(self, path: str, body: Optional[Dict[str, Any]] = None, *, retries: int = 2, retry_delay: float = 0.6) -> Any:
        """Send a raw signed POST request to any Browser API path."""
        return self._browser_http.post(path, body, retries=retries, retry_delay=retry_delay)

    @staticmethod
    def now_sec() -> int:
        """Current time as seconds since epoch – handy for ``schedule_at``."""
        return now_sec()

    @property
    def defaults(self) -> Dict[str, Any]:
        return dict(self._cfg.defaults)

    def close(self) -> None:
        """Close underlying HTTP transports."""
        self._http.close()
        self._browser_http.close()

    def __enter__(self) -> "GeelarkClient":
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()

    def __repr__(self) -> str:
        return f"GeelarkClient(app_id={self._cfg.app_id!r}, base_url={self._cfg.base_url!r})"
