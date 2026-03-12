"""Application Management – 18 endpoints for team apps, installation, etc."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.errors import GeelarkError
from ..core.http import HttpClient
from ..core.utils import build_body


class AppModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def add(self, *, id: str, version_id: str, install_group_ids: Optional[List[str]] = None) -> None:
        self._http.post("/app/add", build_body(id=id, version_id=version_id, install_group_ids=install_group_ids))

    def batch_operate(self, *, action: int, group_ids: Optional[List[str]] = None, package_name: Optional[str] = None, version_id: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/app/operation/batch", build_body(action=action, group_ids=group_ids, package_name=package_name, version_id=version_id))

    def get_team_app_list(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        return self._http.post("/app/teamApp/list", build_body(page=page, page_size=page_size))

    def get_installable(self, *, env_id: str, page: int = 1, page_size: int = 10, name: Optional[str] = None, get_upload_app: Optional[bool] = None) -> Dict[str, Any]:
        return self._http.post("/app/installable/list", build_body(env_id=env_id, page=page, page_size=page_size, name=name, get_upload_app=get_upload_app))

    def get_installed(self, *, env_id: str, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        return self._http.post("/app/list", build_body(env_id=env_id, page=page, page_size=page_size))

    def get_app_shop_list(self, *, page: int = 1, page_size: int = 10, key: Optional[str] = None, get_upload_app: Optional[bool] = None) -> Dict[str, Any]:
        return self._http.post("/app/shop/list", build_body(page=page, page_size=page_size, key=key, get_upload_app=get_upload_app))

    def install(self, env_id: str, app_version_id: str) -> None:
        self._http.post("/app/install", {"envId": env_id, "appVersionId": app_version_id})

    def query_upload_status(self, task_id: str) -> Dict[str, Any]:
        return self._http.post("/app/upload/status", {"taskId": task_id})

    def remove(self, id: str) -> None:
        self._http.post("/app/remove", {"id": id})

    def set_auth(self, id: str, app_auth: int) -> None:
        self._http.post("/app/auth/status", {"id": id, "appAuth": app_auth})

    def set_auto_start(self, id: str, opera: int) -> None:
        self._http.post("/app/setAutoStart", {"id": id, "opera": opera})

    def set_keep_alive(self, id: str, opera: int) -> None:
        self._http.post("/app/setKeepAlive", {"id": id, "opera": opera})

    def set_root(self, id: str, opera: int) -> None:
        self._http.post("/app/root", {"id": id, "opera": opera})

    def set_auto_install(self, *, id: str, status: int, install_group_ids: Optional[List[str]] = None) -> None:
        self._http.post("/app/setStatus", build_body(id=id, status=status, install_group_ids=install_group_ids))

    def start(self, *, env_id: str, app_version_id: Optional[str] = None, package_name: Optional[str] = None) -> None:
        self._http.post("/app/start", build_body(env_id=env_id, app_version_id=app_version_id, package_name=package_name))

    def stop(self, *, env_id: str, app_version_id: Optional[str] = None, package_name: Optional[str] = None) -> None:
        self._http.post("/app/stop", build_body(env_id=env_id, app_version_id=app_version_id, package_name=package_name))

    def uninstall(self, env_id: str, package_name: str) -> None:
        self._http.post("/app/uninstall", {"envId": env_id, "packageName": package_name})

    def upload(self, *, file_url: str, desc: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/app/upload", build_body(file_url=file_url, desc=desc))
