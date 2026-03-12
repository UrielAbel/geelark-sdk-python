"""Tests for GeelarkClient initialization and module wiring."""
from __future__ import annotations

import pytest

from geelark import GeelarkClient, GeelarkError, GeelarkConfig


class TestClientCreation:
    """GeelarkClient can be instantiated with required config."""

    def test_creates_with_app_id_and_api_key(self) -> None:
        client = GeelarkClient(app_id="test_app", api_key="test_key")
        assert repr(client).startswith("GeelarkClient(")
        client.close()

    def test_raises_on_missing_app_id(self) -> None:
        with pytest.raises(ValueError, match="app_id and api_key are required"):
            GeelarkClient(app_id="", api_key="test_key")

    def test_raises_on_missing_api_key(self) -> None:
        with pytest.raises(ValueError, match="app_id and api_key are required"):
            GeelarkClient(app_id="test_app", api_key="")

    def test_custom_base_urls(self) -> None:
        client = GeelarkClient(
            app_id="a",
            api_key="k",
            base_url="https://custom.api.com/v1/",
            browser_base_url="http://127.0.0.1:9999/api/",
        )
        # trailing slash should be stripped
        assert client._cfg.base_url == "https://custom.api.com/v1"
        assert client._cfg.browser_base_url == "http://127.0.0.1:9999/api"
        client.close()

    def test_defaults_dict(self) -> None:
        client = GeelarkClient(app_id="a", api_key="k", defaults={"taskType": 1})
        assert client.defaults == {"taskType": 1}
        client.close()

    def test_debug_mode(self) -> None:
        client = GeelarkClient(app_id="a", api_key="k", debug=True)
        assert client._cfg.debug is True
        client.close()


class TestAllModulesPresent:
    """All 28 modules should be accessible as attributes on GeelarkClient."""

    MODULE_NAMES = [
        # Cloud Phone (11)
        "phone",
        "upload",
        "task",
        "adb",
        "analytics",
        "app",
        "file_management",
        "library",
        "shell",
        "webhook",
        "oem",
        # Social Media / RPA (11)
        "tiktok",
        "instagram",
        "reddit",
        "youtube",
        "google",
        "shein",
        "x",
        "pinterest",
        "threads",
        "facebook",
        "rpa_utils",
        # Management (5)
        "billing",
        "group",
        "proxy_mgmt",
        "tag",
        "proxy_detection",
        # Browser (1)
        "browser",
    ]

    def test_all_28_modules_exist(self) -> None:
        client = GeelarkClient(app_id="a", api_key="k")
        for name in self.MODULE_NAMES:
            assert hasattr(client, name), f"Module {name!r} not found on client"
        assert len(self.MODULE_NAMES) == 28
        client.close()

    def test_modules_are_not_none(self) -> None:
        client = GeelarkClient(app_id="a", api_key="k")
        for name in self.MODULE_NAMES:
            assert getattr(client, name) is not None, f"Module {name!r} is None"
        client.close()


class TestContextManager:
    """GeelarkClient supports the context manager protocol."""

    def test_context_manager_returns_client(self) -> None:
        with GeelarkClient(app_id="a", api_key="k") as client:
            assert isinstance(client, GeelarkClient)

    def test_context_manager_closes_cleanly(self) -> None:
        client = GeelarkClient(app_id="a", api_key="k")
        client.__enter__()
        client.__exit__(None, None, None)
        # After close, the httpx client is closed -- calling close again should not crash
        client.close()

    def test_now_sec_returns_int(self) -> None:
        ts = GeelarkClient.now_sec()
        assert isinstance(ts, int)
        assert ts > 1_700_000_000  # sanity: after ~2023
