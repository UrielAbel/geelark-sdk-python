<div align="center">

<img src="./assets/logo.png" alt="GeeLark" width="380" />

<br />
<br />

**Official Python SDK for the [GeeLark](https://www.geelark.com/) Cloud Phone Platform**

[![PyPI version](https://img.shields.io/pypi/v/geelark-sdk.svg?style=flat-square&color=2C8EF8)](https://pypi.org/project/geelark-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-2C8EF8.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-2C8EF8.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)

Automate cloud phones, antidetect browsers, and social media workflows from Python with a fully typed, Pythonic developer experience.

[Getting Started](#-getting-started) · [API Reference](#-module-reference) · [Examples](#-usage-examples) · [Configuration](#%EF%B8%8F-configuration)

</div>

---

## ✨ Features

| | Feature | Details |
|---|---|---|
| 📦 | **28 API Modules** | Every GeeLark endpoint covered |
| 🔧 | **145+ Methods** | Cloud phones, social platforms, browser automation, and more |
| 🐍 | **Fully Typed** | `TypedDict` definitions + PEP 561 `py.typed` marker |
| 🔀 | **Pythonic API** | `snake_case` everywhere — auto-converted to `camelCase` for the server |
| 🔐 | **Auto Signing** | SHA-256 signature generation handled transparently |
| 🔄 | **Retry Logic** | Automatic retries with jitter and transient-error handling |
| 🪝 | **Hooks** | `before_request` / `after_response` callbacks for logging & middleware |
| 🐛 | **Debug Mode** | Full request/response tracing |
| 📡 | **httpx Transport** | Synchronous `httpx.Client` with connection pooling |

---

## 🚀 Getting Started

### Installation

```bash
pip install geelark-sdk
```

> Requires **Python 3.9** or later.

### Quick Start

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

Or use the **context manager**:

```python
from geelark import GeelarkClient

with GeelarkClient(app_id="YOUR_APP_ID", api_key="YOUR_API_KEY") as client:
    phones = client.phone.list()
    print(phones)
```

---

## 🔐 Authentication

GeeLark uses **SHA-256 request signing**. The SDK handles this automatically — just provide your `app_id` and `api_key`.

Every request includes:

| Field | Description |
|:------|:------------|
| `appId` | Your application ID |
| `traceId` | Unique UUID per request |
| `ts` | Current timestamp in milliseconds |
| `nonce` | Short random string |
| `sign` | `SHA256(appId + traceId + ts + nonce + apiKey).upper()` |

> 💡 You never need to compute signatures yourself.

---

## 📚 Module Reference

<table>
<thead>
<tr>
<th align="left">Category</th>
<th align="left">Attribute</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>

<tr><td colspan="3"><strong>☁️ Cloud Phone</strong></td></tr>
<tr><td></td><td><code>client.phone</code></td><td>Lifecycle — list, create, start, stop, delete, GPS, screenshots, contacts</td></tr>
<tr><td></td><td><code>client.adb</code></td><td>ADB access — get connection data, enable/disable</td></tr>
<tr><td></td><td><code>client.shell</code></td><td>Shell command execution on cloud phones</td></tr>

<tr><td colspan="3"><strong>🤖 Social Media RPA</strong></td></tr>
<tr><td></td><td><code>client.tiktok</code></td><td>Video/image publishing, warmup, login, comments, DMs</td></tr>
<tr><td></td><td><code>client.instagram</code></td><td>Login, publish Reels (video/image), warmup, DMs</td></tr>
<tr><td></td><td><code>client.facebook</code></td><td>Login, comments, publish, Reels, DMs</td></tr>
<tr><td></td><td><code>client.youtube</code></td><td>Publish Shorts/videos, channel maintenance</td></tr>
<tr><td></td><td><code>client.x</code></td><td>Publish content to X (Twitter)</td></tr>
<tr><td></td><td><code>client.reddit</code></td><td>Warmup, post videos/images</td></tr>
<tr><td></td><td><code>client.pinterest</code></td><td>Publish videos and images</td></tr>
<tr><td></td><td><code>client.threads</code></td><td>Publish videos and images</td></tr>
<tr><td></td><td><code>client.google</code></td><td>Login, app download, app browsing</td></tr>
<tr><td></td><td><code>client.shein</code></td><td>Auto-login</td></tr>

<tr><td colspan="3"><strong>🌐 Browser</strong></td></tr>
<tr><td></td><td><code>client.browser</code></td><td>Antidetect browser — create, launch, close, tasks, transfer</td></tr>

<tr><td colspan="3"><strong>⚙️ Automation & Tasks</strong></td></tr>
<tr><td></td><td><code>client.task</code></td><td>Task management — add, cancel, restart, query, history</td></tr>
<tr><td></td><td><code>client.rpa_utils</code></td><td>Multi-platform distribution, file upload, contacts, custom flows</td></tr>

<tr><td colspan="3"><strong>🗂️ Management</strong></td></tr>
<tr><td></td><td><code>client.upload</code></td><td>Get pre-signed upload URLs, upload files to cloud storage</td></tr>
<tr><td></td><td><code>client.analytics</code></td><td>Social media analytics accounts and data</td></tr>
<tr><td></td><td><code>client.app</code></td><td>Application install, uninstall, start, stop, upload, permissions</td></tr>
<tr><td></td><td><code>client.file_management</code></td><td>File upload results, keybox upload and results</td></tr>
<tr><td></td><td><code>client.library</code></td><td>Material and tag management for media assets</td></tr>
<tr><td></td><td><code>client.webhook</code></td><td>Set and get webhook callback URLs</td></tr>
<tr><td></td><td><code>client.oem</code></td><td>White-label / OEM customisation settings</td></tr>
<tr><td></td><td><code>client.billing</code></td><td>Balance inquiry, plan management, renewal</td></tr>
<tr><td></td><td><code>client.group</code></td><td>Phone/browser group CRUD</td></tr>
<tr><td></td><td><code>client.proxy_mgmt</code></td><td>Proxy add, delete, list, update</td></tr>
<tr><td></td><td><code>client.tag</code></td><td>Tag CRUD for organising phones/browsers</td></tr>
<tr><td></td><td><code>client.proxy_detection</code></td><td>Check proxy connectivity and geo info</td></tr>

</tbody>
</table>

---

## 💻 Usage Examples

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

---

## ❌ Error Handling

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

| Property | Type | Description |
|:---------|:-----|:------------|
| `message` | `str` | Human-readable error message |
| `code` | `str` | GeeLark error code |
| `endpoint` | `str` | API endpoint that failed |
| `http_status` | `int` | HTTP status code |
| `details` | `dict` | Full response dict from the server |

---

## ⚙️ Configuration

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

    # Hook called before every request
    before_request=lambda ctx: print(f"-> {ctx['path']}"),

    # Hook called after every response
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

---

<div align="center">

**[GeeLark Website](https://www.geelark.com/)** · **[API Documentation](https://docs.geelark.com/)** · **[Report an Issue](https://github.com/UrielAbel/geelark-sdk-python/issues)**

<sub>MIT License — © 2024-2025 GeeLark SDK Contributors</sub>

</div>
