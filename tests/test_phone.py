"""Tests for the PhoneModule -- mocks httpx to verify correct API paths and bodies."""
from __future__ import annotations

from typing import Any, Dict, Optional
from unittest.mock import MagicMock, patch

import pytest

from geelark import GeelarkClient, GeelarkError
from geelark.core.http import HttpClient
from geelark.modules.phone import PhoneModule


def _make_phone_module() -> tuple:
    """Create a PhoneModule with a mocked HttpClient."""
    mock_http = MagicMock(spec=HttpClient)
    mock_http.post = MagicMock(return_value={"list": [], "total": 0})
    module = PhoneModule(mock_http)
    return module, mock_http


class TestPhoneList:
    """phone.list() calls the correct API path."""

    def test_list_default_params(self) -> None:
        module, mock_http = _make_phone_module()
        module.list()
        mock_http.post.assert_called_once()
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/list"
        assert body["page"] == 1
        assert body["pageSize"] == 10

    def test_list_with_filters(self) -> None:
        module, mock_http = _make_phone_module()
        module.list(page=2, page_size=5, group_name="test-group")
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/list"
        assert body["page"] == 2
        assert body["pageSize"] == 5
        assert body["groupName"] == "test-group"

    def test_list_with_ids(self) -> None:
        module, mock_http = _make_phone_module()
        module.list(ids=["id1", "id2"])
        path, body = mock_http.post.call_args[0]
        assert body["ids"] == ["id1", "id2"]


class TestPhoneStartStop:
    """phone.start() and phone.stop() call correct paths."""

    def test_start_single_id(self) -> None:
        module, mock_http = _make_phone_module()
        module.start("phone_1")
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/start"
        assert body == {"ids": ["phone_1"]}

    def test_start_multiple_ids(self) -> None:
        module, mock_http = _make_phone_module()
        module.start(["phone_1", "phone_2"])
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/start"
        assert body == {"ids": ["phone_1", "phone_2"]}

    def test_stop_single_id(self) -> None:
        module, mock_http = _make_phone_module()
        module.stop("phone_1")
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/stop"
        assert body == {"ids": ["phone_1"]}

    def test_stop_multiple_ids(self) -> None:
        module, mock_http = _make_phone_module()
        module.stop(["phone_1", "phone_2"])
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/stop"
        assert body == {"ids": ["phone_1", "phone_2"]}


class TestPhoneDelete:
    """phone.delete() calls the correct path."""

    def test_delete_with_ids(self) -> None:
        module, mock_http = _make_phone_module()
        module.delete(["phone_1"])
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/delete"
        assert body == {"ids": ["phone_1"]}

    def test_delete_empty_ids_raises(self) -> None:
        module, mock_http = _make_phone_module()
        with pytest.raises(GeelarkError, match="ids required"):
            module.delete([])


class TestPhoneGps:
    """phone.get_gps() and phone.set_gps() call correct paths."""

    def test_get_gps(self) -> None:
        module, mock_http = _make_phone_module()
        module.get_gps(["phone_1", "phone_2"])
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/gps/get"
        assert body == {"ids": ["phone_1", "phone_2"]}

    def test_set_gps(self) -> None:
        module, mock_http = _make_phone_module()
        gps_data = [{"id": "phone_1", "lng": "-73.9", "lat": "40.7"}]
        module.set_gps(gps_data)
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/gps/set"
        assert body == {"list": gps_data}


class TestPhoneStatus:
    """phone.status() calls the correct path and validates input."""

    def test_status_with_ids(self) -> None:
        module, mock_http = _make_phone_module()
        module.status(["p1", "p2"])
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/status"
        assert body == {"ids": ["p1", "p2"]}

    def test_status_empty_ids_raises(self) -> None:
        module, mock_http = _make_phone_module()
        with pytest.raises(GeelarkError, match="ids required"):
            module.status([])


class TestPhoneScreenshot:
    """phone.screenshot() and phone.screenshot_result() call correct paths."""

    def test_screenshot(self) -> None:
        module, mock_http = _make_phone_module()
        module.screenshot("phone_1")
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/screenShot"
        assert body == {"id": "phone_1"}

    def test_screenshot_result(self) -> None:
        module, mock_http = _make_phone_module()
        module.screenshot_result("task_123")
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/screenShot/result"
        assert body == {"taskId": "task_123"}


class TestPhoneUpdate:
    """phone.update() constructs the correct body."""

    def test_update_with_required_fields(self) -> None:
        module, mock_http = _make_phone_module()
        module.update(id="phone_1", name="new-name", remark="my remark")
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/detail/update"
        assert body["id"] == "phone_1"
        assert body["name"] == "new-name"
        assert body["remark"] == "my remark"

    def test_update_empty_id_raises(self) -> None:
        module, mock_http = _make_phone_module()
        with pytest.raises(GeelarkError, match="id required"):
            module.update(id="")


class TestPhoneMisc:
    """Miscellaneous phone methods."""

    def test_brand_list(self) -> None:
        module, mock_http = _make_phone_module()
        module.brand_list(12)
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/brand/list"
        assert body == {"androidVer": 12}

    def test_send_sms(self) -> None:
        module, mock_http = _make_phone_module()
        module.send_sms(id="p1", phone_number="+1234567890", text="Hello")
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/sendSms"
        assert body["id"] == "p1"
        assert body["phoneNumber"] == "+1234567890"
        assert body["text"] == "Hello"

    def test_transfer(self) -> None:
        module, mock_http = _make_phone_module()
        module.transfer(account="user@example.com", ids=["p1", "p2"])
        path, body = mock_http.post.call_args[0]
        assert path == "/phone/transfer"
        assert body["account"] == "user@example.com"
        assert body["ids"] == ["p1", "p2"]
