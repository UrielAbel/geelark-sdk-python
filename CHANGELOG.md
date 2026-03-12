# Changelog

All notable changes to the GeeLark SDK for Python will be documented in this file.

This project follows [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2025-01-01

### Added

- Initial public release of the GeeLark Python SDK.
- **28 modules** covering the full GeeLark OpenAPI surface:
  - Cloud Phone management (phone, upload, task, adb, analytics, app, file management, library, shell, webhook, oem)
  - Social media RPA (TikTok, Instagram, Reddit, YouTube, Google, SHEIN, X/Twitter, Pinterest, Threads, Facebook, RPA utils)
  - Management (billing, group, proxy management, tag, proxy detection)
  - Antidetect Browser API (browser)
- **145+ typed methods** with snake_case signatures and automatic camelCase conversion.
- SHA-256 request signing handled transparently.
- Automatic retry with jitter for transient HTTP errors (429, 502, 503, 504).
- `GeelarkError` exception with structured fields (`code`, `endpoint`, `http_status`, `details`).
- Context manager support (`with GeelarkClient(...) as client:`).
- `before_request` / `after_response` hooks for custom middleware.
- Debug mode for full request/response logging.
- PEP 561 `py.typed` marker for static type checker compatibility.
- Full `TypedDict` response types for all endpoints.
