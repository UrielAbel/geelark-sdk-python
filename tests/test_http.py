"""Tests for HTTP layer: signature generation, build_body, and auth fields."""
from __future__ import annotations

import hashlib

from geelark.core.utils import sha256_upper, build_body, _to_camel, uuid_like, is_transient


class TestSha256Signature:
    """SHA-256 signature generation matches the expected algorithm."""

    def test_basic_signature(self) -> None:
        text = "app123trace456170000000012345key789"
        expected = hashlib.sha256(text.encode("utf-8")).hexdigest().upper()
        assert sha256_upper(text) == expected

    def test_empty_string(self) -> None:
        result = sha256_upper("")
        assert len(result) == 64
        assert result == result.upper()

    def test_signature_is_uppercase_hex(self) -> None:
        result = sha256_upper("hello_world")
        assert result == result.upper()
        # Should only contain hex chars
        assert all(c in "0123456789ABCDEF" for c in result)

    def test_signature_deterministic(self) -> None:
        assert sha256_upper("test") == sha256_upper("test")

    def test_composed_signature(self) -> None:
        """Verify that composing appId+traceId+ts+nonce+apiKey works correctly."""
        app_id = "myAppId"
        trace_id = "abc123def456"
        ts = "1700000000000"
        nonce = "abc123"
        api_key = "secretKey"
        raw = app_id + trace_id + ts + nonce + api_key
        expected = hashlib.sha256(raw.encode("utf-8")).hexdigest().upper()
        assert sha256_upper(raw) == expected


class TestBuildBody:
    """build_body converts snake_case kwargs to camelCase and omits None values."""

    def test_simple_conversion(self) -> None:
        result = build_body(page=1, page_size=10)
        assert result == {"page": 1, "pageSize": 10}

    def test_omits_none_values(self) -> None:
        result = build_body(page=1, page_size=None, serial_name=None)
        assert result == {"page": 1}

    def test_preserves_single_word_keys(self) -> None:
        result = build_body(id="abc", page=1)
        assert result == {"id": "abc", "page": 1}

    def test_multi_word_conversion(self) -> None:
        result = build_body(browse_posts_num=5, max_try_times=3)
        assert result == {"browsePostsNum": 5, "maxTryTimes": 3}

    def test_empty_body(self) -> None:
        result = build_body()
        assert result == {}

    def test_all_none_values(self) -> None:
        result = build_body(a=None, b=None)
        assert result == {}

    def test_list_values_preserved(self) -> None:
        result = build_body(ids=["a", "b"], tags=["t1"])
        assert result == {"ids": ["a", "b"], "tags": ["t1"]}

    def test_boolean_values(self) -> None:
        result = build_body(mark_ai=True, need_share_link=False)
        assert result == {"markAi": True, "needShareLink": False}

    def test_zero_is_not_omitted(self) -> None:
        result = build_body(schedule_at=0)
        assert result == {"scheduleAt": 0}

    def test_empty_string_is_not_omitted(self) -> None:
        result = build_body(name="")
        assert result == {"name": ""}


class TestToCamel:
    """_to_camel converts snake_case to camelCase."""

    def test_single_word(self) -> None:
        assert _to_camel("id") == "id"

    def test_two_words(self) -> None:
        assert _to_camel("page_size") == "pageSize"

    def test_three_words(self) -> None:
        assert _to_camel("browse_posts_num") == "browsePostsNum"

    def test_already_camel(self) -> None:
        # Single word stays as-is
        assert _to_camel("page") == "page"


class TestUuidLike:
    """uuid_like generates a UUID-like hex string."""

    def test_length(self) -> None:
        result = uuid_like()
        assert len(result) == 32

    def test_is_hex(self) -> None:
        result = uuid_like()
        int(result, 16)  # should not raise

    def test_unique(self) -> None:
        a = uuid_like()
        b = uuid_like()
        assert a != b


class TestIsTransient:
    """is_transient identifies retryable HTTP status codes."""

    def test_retryable_codes(self) -> None:
        for code in (429, 502, 503, 504):
            assert is_transient(code) is True

    def test_non_retryable_codes(self) -> None:
        for code in (200, 400, 401, 403, 404, 500):
            assert is_transient(code) is False


class TestBodyConstructionWithAuth:
    """Body construction includes auth-related fields when provided."""

    def test_body_with_schedule_at(self) -> None:
        body = build_body(env_id="phone1", schedule_at=1700000000)
        assert body == {"envId": "phone1", "scheduleAt": 1700000000}

    def test_body_with_task_type(self) -> None:
        body = build_body(env_id="phone1", task_type=1, schedule_at=0)
        assert body == {"envId": "phone1", "taskType": 1, "scheduleAt": 0}
