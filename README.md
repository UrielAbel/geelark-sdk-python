# GeeLark SDK for Python

[![PyPI version](https://img.shields.io/pypi/v/geelark-sdk.svg)](https://pypi.org/project/geelark-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)

Official Python SDK for the [GeeLark](https://www.geelark.com/) cloud phone platform API. Automate cloud phones, antidetect browsers, and social media workflows from Python.

---

## Features

- **28 modules** covering cloud phones, browsers, social media RPA, and management APIs
- **145+ methods** mapped one-to-one with the GeeLark OpenAPI
- **Fully typed** -- every request/response uses `TypedDict` definitions and PEP 561 `py.typed` marker
- **Synchronous `httpx` transport** with automatic retries, jitter, and transient-error handling
- **Pythonic `snake_case` API** -- parameters are automatically converted to the `camelCase` the server expects
- **SHA-256 request signing** handled transparently by the SDK
- **Context manager** support for clean resource management
- **Hooks** -- `before_request` and `after_response` callbacks for logging, metrics, or custom middleware
- **Debug mode** for full request/response tracing

## Installation

```bash
pip install geelark-sdk
```

Requires Python 3.9 or later.

## Quick Start

```python
from geelark import GeelarkClient

client = GeelarkClient(app_id="YOUR_APP_ID", api_key="YOUR_API_KEY")

# List cloud phones
phones = client.phone.list(page=1, page_size=5)
print(phones)

# Start a phone
client.phone.start("phone_id_here")

# Close the client when done
client.close()
```

Or use the context manager:

```python
from geelark import GeelarkClient

with GeelarkClient(app_id="YOUR_APP_ID", api_key="YOUR_API_KEY") as client:
    phones = client.phone.list()
    print(phones)
```

## Authentication

GeeLark uses **SHA-256 HMAC-style signing** on every request. The SDK handles this automatically -- you only need to provide your `app_id` and `api_key` (obtained from the GeeLark dashboard).

Each request is signed with:
- `appId` -- your application ID
- `traceId` -- a unique UUID per request
- `ts` -- current timestamp in milliseconds
- `nonce` -- a short random string
- `sign` -- `SHA256(appId + traceId + ts + nonce + apiKey).upper()`

You never need to compute the signature yourself.

## Module Reference

| Module | Attribute | Description |
|--------|-----------|-------------|
| **Phone** | `client.phone` | Cloud phone CRUD, start/stop, GPS, screenshot, SMS, root, network, contacts |
| **Upload** | `client.upload` | Get pre-signed upload URLs, upload files to GeeLark cloud storage |
| **Task** | `client.task` | Automation task management -- add, cancel, restart, query, history |
| **ADB** | `client.adb` | ADB connection data and status management |
| **Analytics** | `client.analytics` | Social media analytics accounts and data |
| **App** | `client.app` | Application install, uninstall, start, stop, upload, permissions |
| **File Management** | `client.file_management` | File upload results, keybox upload and results |
| **Library** | `client.library` | Material and tag management for media assets |
| **Shell** | `client.shell` | Execute shell commands on cloud phones |
| **Webhook** | `client.webhook` | Set and get webhook callback URLs |
| **OEM** | `client.oem` | White-label / OEM customisation settings |
| **TikTok** | `client.tiktok` | Video/image publishing, warmup, login, profile editing, comments, messages |
| **Instagram** | `client.instagram` | Login, publish Reels (video/image), warmup, direct messages |
| **Reddit** | `client.reddit` | Warmup, post videos, post images |
| **YouTube** | `client.youtube` | Publish Shorts, publish videos, channel maintenance |
| **Google** | `client.google` | Google login, app download, app browser |
| **SHEIN** | `client.shein` | SHEIN auto-login |
| **X (Twitter)** | `client.x` | Publish content to X |
| **Pinterest** | `client.pinterest` | Publish videos and images to Pinterest |
| **Threads** | `client.threads` | Publish videos and images to Threads |
| **Facebook** | `client.facebook` | Login, auto-comment, maintenance, publish, Reels, messages |
| **RPA Utils** | `client.rpa_utils` | Multi-platform distribution, file upload, contacts, keybox, custom flows |
| **Billing** | `client.billing` | Balance inquiry, plan management, renewal |
| **Group** | `client.group` | Phone/browser group CRUD |
| **Proxy Mgmt** | `client.proxy_mgmt` | Proxy add, delete, list, update |
| **Tag** | `client.tag` | Tag CRUD for organising phones/browsers |
| **Proxy Detection** | `client.proxy_detection` | Check proxy connectivity and geo info |
| **Browser** | `client.browser` | Antidetect browser CRUD, launch/close, tasks, transfer |

## Usage Examples

### Cloud Phone Management

```python
# List phones with filters
phones = client.phone.list(page=1, page_size=20, group_name="my-group")

# Start and stop phones
client.phone.start("phone_123")
client.phone.stop(["phone_123", "phone_456"])

# Set GPS coordinates
client.phone.set_gps([
    {"id": "phone_123", "lng": "-73.9857", "lat": "40.7484"}
])

# Take a screenshot
result = client.phone.screenshot("phone_123")
task_id = result["taskId"]
screenshot = client.phone.screenshot_result(task_id)
```

### TikTok Automation

```python
# Publish a video
client.tiktok.add_video(
    env_id="phone_123",
    video="https://example.com/video.mp4",
    video_desc="Check out this video! #trending",
    schedule_at=0,
)

# Login to TikTok
client.tiktok.login(id="phone_123", account="user@example.com", password="pass")

# Warmup account
client.tiktok.add_warmup(env_id="phone_123", action="browse", duration=300)
```

### Instagram Automation

```python
# Login
client.instagram.login(id="phone_123", account="myuser", password="mypass")

# Publish Reels
client.instagram.pub_reels(
    id="phone_123",
    description="New reel! #reels",
    video=["https://example.com/reel.mp4"],
)

# Send direct messages
client.instagram.message(
    id="phone_123",
    usernames=["user1", "user2"],
    content="Hello from GeeLark!",
)
```

### Antidetect Browser

```python
# Create a browser profile
profile = client.browser.create(
    serial_name="my-profile-01",
    browser_os=1,
    proxy_config={"type": "socks5", "server": "proxy.example.com", "port": 1080},
)

# Launch the browser
result = client.browser.launch(profile["id"])
debug_port = result["debugPort"]

# Close when done
client.browser.close(profile["id"])
```

## Error Handling

All API errors raise `GeelarkError` with structured information:

```python
from geelark import GeelarkClient, GeelarkError

client = GeelarkClient(app_id="...", api_key="...")

try:
    client.phone.start("invalid_id")
except GeelarkError as e:
    print(e)              # Human-readable message
    print(e.code)         # GeeLark error code (string)
    print(e.endpoint)     # API endpoint that failed
    print(e.http_status)  # HTTP status code
    print(e.details)      # Full response dict from the server
```

## Configuration

```python
client = GeelarkClient(
    app_id="YOUR_APP_ID",
    api_key="YOUR_API_KEY",

    # Override the default cloud API base URL
    base_url="https://openapi.geelark.com/open/v1",

    # Override the local browser API base URL
    browser_base_url="http://localhost:40185/api/v1",

    # Enable debug logging (prints every request/response)
    debug=True,

    # Default values merged into certain modules (e.g. taskType for TikTok)
    defaults={"taskType": 1},

    # Hook called before every request with context dict
    before_request=lambda ctx: print(f"-> {ctx['path']}"),

    # Hook called after every response with context dict
    after_response=lambda ctx: print(f"<- {ctx['status']}"),
)
```

### Context Manager

The client holds an `httpx.Client` connection pool. Always close it when finished:

```python
# Option 1: explicit close
client = GeelarkClient(app_id="...", api_key="...")
try:
    client.phone.list()
finally:
    client.close()

# Option 2: context manager (recommended)
with GeelarkClient(app_id="...", api_key="...") as client:
    client.phone.list()
```

## License

MIT -- see [LICENSE](LICENSE) for details.
