"""GeeLark SDK for Python – Cloud Phone & Antidetect Browser automation.

Usage::

    from geelark import GeelarkClient

    client = GeelarkClient(app_id="...", api_key="...")
    phones = client.phone.list()
"""
from __future__ import annotations

from .client import GeelarkClient
from .core.errors import GeelarkError
from .core.config import GeelarkConfig
from .types import (
    # Common
    BulkOpResp, FailDetail,
    # Cloud Phone
    EquipmentInfo, Phone, PhoneGroup, PhoneListResp,
    AddNewDetail, AddNewResp, PhoneStatusResp,
    GpsItem, GpsGetResp, ScreenShotResp, ScreenShotResultResp,
    BrandItem, TransferResp, ContactObject,
    # Task
    TaskType, TaskStatus, Task, QueryResp,
    # RPA
    RpaTaskIdResp, TaskFlowItem, TaskFlowListResp,
    # ADB
    AdbDataItem,
    # Analytics
    AnalyticsAccount, AnalyticsAccountsListResp,
    AnalyticsAddAccountsResp, AnalyticsDataItem, AnalyticsDataResp,
    # App
    AppTeamAppListItem, AppTeamAppListResp, AppInfo,
    AppListResp, AppUploadStatusResp,
    # Library
    MaterialTag, MaterialItem, MaterialSearchResp, MaterialTagSearchResp,
    # Billing
    BalanceResp, PlanProfile, PlanInfoResp,
    # Group
    GroupCreateResp, GroupItem, GroupQueryResp,
    # Proxy
    ProxyAddResp, ProxyListItem, ProxyListResp,
    # Tag
    TagCreateResp, TagItem, TagQueryResp,
    # Proxy Detection
    ProxyCheckResp,
    # Browser
    BrowserListResp, BrowserDeleteResp, BrowserTransferResp,
    BrowserTask, BrowserTaskQueryResp,
    # Webhook
    CallbackType,
)

__all__ = [
    # Client
    "GeelarkClient",
    "GeelarkError",
    "GeelarkConfig",
    # Common
    "BulkOpResp", "FailDetail",
    # Cloud Phone
    "EquipmentInfo", "Phone", "PhoneGroup", "PhoneListResp",
    "AddNewDetail", "AddNewResp", "PhoneStatusResp",
    "GpsItem", "GpsGetResp", "ScreenShotResp", "ScreenShotResultResp",
    "BrandItem", "TransferResp", "ContactObject",
    # Task
    "TaskType", "TaskStatus", "Task", "QueryResp",
    # RPA
    "RpaTaskIdResp", "TaskFlowItem", "TaskFlowListResp",
    # ADB
    "AdbDataItem",
    # Analytics
    "AnalyticsAccount", "AnalyticsAccountsListResp",
    "AnalyticsAddAccountsResp", "AnalyticsDataItem", "AnalyticsDataResp",
    # App
    "AppTeamAppListItem", "AppTeamAppListResp", "AppInfo",
    "AppListResp", "AppUploadStatusResp",
    # Library
    "MaterialTag", "MaterialItem", "MaterialSearchResp", "MaterialTagSearchResp",
    # Billing
    "BalanceResp", "PlanProfile", "PlanInfoResp",
    # Group
    "GroupCreateResp", "GroupItem", "GroupQueryResp",
    # Proxy
    "ProxyAddResp", "ProxyListItem", "ProxyListResp",
    # Tag
    "TagCreateResp", "TagItem", "TagQueryResp",
    # Proxy Detection
    "ProxyCheckResp",
    # Browser
    "BrowserListResp", "BrowserDeleteResp", "BrowserTransferResp",
    "BrowserTask", "BrowserTaskQueryResp",
    # Webhook
    "CallbackType",
]

__version__ = "1.0.0"
