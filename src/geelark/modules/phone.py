"""Cloud Phone Management – 22 endpoints."""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence, Union

from ..core.errors import GeelarkError
from ..core.http import HttpClient
from ..core.utils import build_body


class PhoneModule:
    """Manage GeeLark cloud phones."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    # ── List / Status ────────────────────────────────────────────

    def list(
        self,
        *,
        page: int = 1,
        page_size: int = 10,
        ids: Optional[List[str]] = None,
        serial_name: Optional[str] = None,
        remark: Optional[str] = None,
        group_name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        charge_mode: Optional[int] = None,
        open_status: Optional[int] = None,
        proxy_ids: Optional[List[str]] = None,
        serial_nos: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return self._http.post("/phone/list", build_body(
            page=page, page_size=page_size, ids=ids, serial_name=serial_name,
            remark=remark, group_name=group_name, tags=tags, charge_mode=charge_mode,
            open_status=open_status, proxy_ids=proxy_ids, serial_nos=serial_nos,
        ))

    def status(self, ids: List[str]) -> Dict[str, Any]:
        if not ids:
            raise GeelarkError("phone.status: ids required")
        return self._http.post("/phone/status", {"ids": ids})

    # ── Create / Delete ──────────────────────────────────────────

    def add_new(
        self,
        *,
        mobile_type: str,
        data: List[Dict[str, Any]],
        charge_mode: Optional[int] = None,
        region: Optional[str] = None,
    ) -> Dict[str, Any]:
        return self._http.post("/phone/addNew", build_body(
            mobile_type=mobile_type, data=data, charge_mode=charge_mode, region=region,
        ))

    def delete(self, ids: List[str]) -> Dict[str, Any]:
        if not ids:
            raise GeelarkError("phone.delete: ids required")
        return self._http.post("/phone/delete", {"ids": ids})

    # ── Start / Stop ─────────────────────────────────────────────

    def start(self, ids: Union[str, List[str]]) -> Dict[str, Any]:
        return self._http.post("/phone/start", {"ids": ids if isinstance(ids, list) else [ids]})

    def stop(self, ids: Union[str, List[str]]) -> Dict[str, Any]:
        return self._http.post("/phone/stop", {"ids": ids if isinstance(ids, list) else [ids]})

    # ── GPS ───────────────────────────────────────────────────────

    def get_gps(self, ids: List[str]) -> Dict[str, Any]:
        return self._http.post("/phone/gps/get", {"ids": ids})

    def set_gps(self, gps_list: List[Dict[str, Any]]) -> Dict[str, Any]:
        return self._http.post("/phone/gps/set", {"list": gps_list})

    # ── Update / New One ─────────────────────────────────────────

    def update(
        self,
        *,
        id: str,
        name: Optional[str] = None,
        remark: Optional[str] = None,
        group_id: Optional[str] = None,
        tag_ids: Optional[List[str]] = None,
        proxy_config: Optional[Dict[str, Any]] = None,
        proxy_id: Optional[str] = None,
        phone_number: Optional[str] = None,
    ) -> Any:
        if not id:
            raise GeelarkError("phone.update: id required")
        return self._http.post("/phone/detail/update", build_body(
            id=id, name=name, remark=remark, group_id=group_id,
            tag_ids=tag_ids, proxy_config=proxy_config, proxy_id=proxy_id,
            phone_number=phone_number,
        ))

    def new_one(
        self,
        *,
        id: str,
        change_brand_model: Optional[bool] = None,
        keep_net_type: Optional[bool] = None,
        keep_phone_number: Optional[bool] = None,
        keep_region: Optional[bool] = None,
        keep_language: Optional[bool] = None,
    ) -> None:
        if not id:
            raise GeelarkError("phone.new_one: id required")
        self._http.post("/../v2/phone/newOne", build_body(
            id=id, change_brand_model=change_brand_model, keep_net_type=keep_net_type,
            keep_phone_number=keep_phone_number, keep_region=keep_region,
            keep_language=keep_language,
        ))

    # ── Screenshot ───────────────────────────────────────────────

    def screenshot(self, id: str) -> Dict[str, Any]:
        return self._http.post("/phone/screenShot", {"id": id})

    def screenshot_result(self, task_id: str) -> Dict[str, Any]:
        return self._http.post("/phone/screenShot/result", {"taskId": task_id})

    # ── Root / Serial / SMS ──────────────────────────────────────

    def set_root(self, ids: List[str], open: bool) -> Any:
        return self._http.post("/root/setStatus", {"ids": ids, "open": open})

    def get_serial_num(self, id: str) -> Dict[str, Any]:
        return self._http.post("/phone/serialNum/get", {"id": id})

    def send_sms(self, *, id: str, phone_number: str, text: str) -> None:
        self._http.post("/phone/sendSms", build_body(id=id, phone_number=phone_number, text=text))

    # ── Brand list ───────────────────────────────────────────────

    def brand_list(self, android_ver: int) -> List[Dict[str, str]]:
        return self._http.post("/phone/brand/list", {"androidVer": android_ver})

    # ── Transfer ─────────────────────────────────────────────────

    def transfer(
        self,
        *,
        account: str,
        ids: List[str],
        transfer_option: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return self._http.post("/phone/transfer", build_body(
            account=account, ids=ids, transfer_option=transfer_option,
        ))

    # ── Network / Accessibility / Group ──────────────────────────

    def set_net_type(self, id: str, net_type: int) -> None:
        self._http.post("/phone/net/set", {"id": id, "netType": net_type})

    def hide_accessibility(self, ids: List[str], pkg_name: List[str]) -> Any:
        return self._http.post("/phone/hideAccessibility", {"ids": ids, "pkgName": pkg_name})

    def move_group(self, env_ids: List[str], group_id: str) -> None:
        self._http.post("/phone/moveGroup", {"envIds": env_ids, "groupId": group_id})

    # ── File upload / Contacts ───────────────────────────────────

    def upload_file(self, id: str, file_url: str) -> Any:
        return self._http.post("/phone/uploadFile", {"id": id, "fileUrl": file_url})

    def import_contacts(self, id: str, contacts: List[Dict[str, Any]]) -> Dict[str, Any]:
        return self._http.post("/phone/importContacts", {"id": id, "contacts": contacts})

    def import_contacts_result(self, task_id: str) -> Dict[str, Any]:
        return self._http.post("/phone/importContactsResult", {"taskId": task_id})
