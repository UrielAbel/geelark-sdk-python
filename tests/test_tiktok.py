"""Tests for the TiktokModule -- mocks httpx to verify correct API paths and bodies."""
from __future__ import annotations

from unittest.mock import MagicMock

from geelark.core.http import HttpClient
from geelark.modules.tiktok import TiktokModule


def _make_tiktok_module(defaults: dict | None = None) -> tuple:
    """Create a TiktokModule with a mocked HttpClient."""
    mock_http = MagicMock(spec=HttpClient)
    mock_http.post = MagicMock(return_value={"taskId": "t1"})
    module = TiktokModule(mock_http, defaults)
    return module, mock_http


class TestTiktokAddVideo:
    """tiktok.add_video() constructs the correct body."""

    def test_add_video_minimal(self) -> None:
        module, mock_http = _make_tiktok_module()
        module.add_video(env_id="phone_1", video="https://example.com/video.mp4")
        path, body = mock_http.post.call_args[0]
        assert path == "/task/addOne"
        assert body["envId"] == "phone_1"
        assert body["video"] == "https://example.com/video.mp4"
        # Default taskType should be 1 when no defaults provided (from defaults.get)
        assert body["taskType"] == 1

    def test_add_video_with_description(self) -> None:
        module, mock_http = _make_tiktok_module()
        module.add_video(
            env_id="phone_1",
            video="https://example.com/video.mp4",
            video_desc="My awesome video #trending",
        )
        path, body = mock_http.post.call_args[0]
        assert body["videoDesc"] == "My awesome video #trending"

    def test_add_video_with_defaults(self) -> None:
        module, mock_http = _make_tiktok_module(defaults={"taskType": 5})
        module.add_video(env_id="phone_1", video="https://example.com/video.mp4")
        path, body = mock_http.post.call_args[0]
        assert body["taskType"] == 5

    def test_add_video_all_optional_params(self) -> None:
        module, mock_http = _make_tiktok_module()
        module.add_video(
            env_id="phone_1",
            video="https://example.com/v.mp4",
            plan_name="my plan",
            schedule_at=1700000000,
            video_desc="desc",
            product_id="prod1",
            product_title="Product",
            ref_video_id="ref1",
            max_try_times=3,
            timeout_min=10,
            same_video_volume=50,
            source_video_volume=80,
            mark_ai=True,
            cover="https://example.com/cover.jpg",
            need_share_link=True,
        )
        path, body = mock_http.post.call_args[0]
        assert body["planName"] == "my plan"
        assert body["scheduleAt"] == 1700000000
        assert body["productId"] == "prod1"
        assert body["maxTryTimes"] == 3
        assert body["markAi"] is True
        assert body["cover"] == "https://example.com/cover.jpg"
        assert body["needShareLink"] is True


class TestTiktokLogin:
    """tiktok.login() calls the correct API path."""

    def test_login_basic(self) -> None:
        module, mock_http = _make_tiktok_module()
        module.login(id="phone_1", account="user@example.com", password="pass123")
        path, body = mock_http.post.call_args[0]
        assert path == "/rpa/task/tiktokLogin"
        assert body["id"] == "phone_1"
        assert body["account"] == "user@example.com"
        assert body["password"] == "pass123"
        assert body["scheduleAt"] == 0

    def test_login_with_schedule(self) -> None:
        module, mock_http = _make_tiktok_module()
        module.login(id="p1", account="u", password="p", schedule_at=1700000000)
        path, body = mock_http.post.call_args[0]
        assert body["scheduleAt"] == 1700000000


class TestTiktokAddImageSet:
    """tiktok.add_image_set() constructs the correct body."""

    def test_add_image_set(self) -> None:
        module, mock_http = _make_tiktok_module()
        module.add_image_set(
            env_id="phone_1",
            images=["https://example.com/img1.jpg", "https://example.com/img2.jpg"],
        )
        path, body = mock_http.post.call_args[0]
        assert path == "/task/addOne"
        assert body["envId"] == "phone_1"
        assert body["images"] == ["https://example.com/img1.jpg", "https://example.com/img2.jpg"]
        # Image set always has taskType=3
        assert body["taskType"] == 3


class TestTiktokWarmup:
    """tiktok.add_warmup() constructs the correct body."""

    def test_add_warmup(self) -> None:
        module, mock_http = _make_tiktok_module()
        module.add_warmup(env_id="phone_1", action="browse", duration=300)
        path, body = mock_http.post.call_args[0]
        assert path == "/task/addOne"
        assert body["envId"] == "phone_1"
        assert body["action"] == "browse"
        assert body["duration"] == 300
        assert body["taskType"] == 2


class TestTiktokEditProfile:
    """tiktok.edit_profile() calls the correct path."""

    def test_edit_profile(self) -> None:
        module, mock_http = _make_tiktok_module()
        module.edit_profile(id="p1", nick_name="NewNick", bio="My bio")
        path, body = mock_http.post.call_args[0]
        assert path == "/rpa/task/tiktokEditProfile"
        assert body["id"] == "p1"
        assert body["nickName"] == "NewNick"
        assert body["bio"] == "My bio"


class TestTiktokComments:
    """tiktok.random_comment() and random_comment_asia() call correct paths."""

    def test_random_comment(self) -> None:
        module, mock_http = _make_tiktok_module()
        module.random_comment(id="p1", use_ai=1, comment="Great video!")
        path, body = mock_http.post.call_args[0]
        assert path == "/rpa/task/tiktokRandomComment"
        assert body["useAi"] == 1
        assert body["comment"] == "Great video!"

    def test_random_comment_asia(self) -> None:
        module, mock_http = _make_tiktok_module()
        module.random_comment_asia(id="p1", use_ai=0)
        path, body = mock_http.post.call_args[0]
        assert path == "/rpa/task/tiktokRandomCommentAsia"


class TestTiktokMessages:
    """tiktok.message() and message_asia() construct correct bodies."""

    def test_message(self) -> None:
        module, mock_http = _make_tiktok_module()
        module.message(id="p1", usernames=["user1", "user2"], content="Hello!")
        path, body = mock_http.post.call_args[0]
        assert path == "/rpa/task/tiktokMessage"
        assert body["usernames"] == ["user1", "user2"]
        assert body["content"] == "Hello!"

    def test_message_asia(self) -> None:
        module, mock_http = _make_tiktok_module()
        module.message_asia(id="p1", usernames=["u1"], content="Hi")
        path, body = mock_http.post.call_args[0]
        assert path == "/rpa/task/tiktokMessageAsia"


class TestTiktokStar:
    """tiktok.random_star() and random_star_asia() call correct paths."""

    def test_random_star(self) -> None:
        module, mock_http = _make_tiktok_module()
        module.random_star(id="p1")
        path, body = mock_http.post.call_args[0]
        assert path == "/rpa/task/tiktokStar"

    def test_random_star_asia(self) -> None:
        module, mock_http = _make_tiktok_module()
        module.random_star_asia(id="p1")
        path, body = mock_http.post.call_args[0]
        assert path == "/rpa/task/tiktokStarAsia"
