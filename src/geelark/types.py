"""Type definitions for the GeeLark SDK.

All request/response shapes are expressed as ``TypedDict`` so they can be used
for static analysis while remaining plain dicts at runtime.
"""
from __future__ import annotations

import enum
from typing import Any, Dict, List, Optional, Sequence

try:
    from typing import TypedDict
except ImportError:  # Python < 3.8 fallback
    from typing_extensions import TypedDict


# ── Common ───────────────────────────────────────────────────────

class BulkOpResp(TypedDict, total=False):
    totalAmount: int
    successAmount: int
    failAmount: int
    failDetails: List[Dict[str, Any]]


class FailDetail(TypedDict):
    code: int
    id: str
    msg: str


# ── Cloud Phone ──────────────────────────────────────────────────

class EquipmentInfo(TypedDict, total=False):
    countryName: str
    phoneNumber: str
    enableSim: int
    imei: str
    osVersion: str
    wifiBssid: str
    mac: str
    bluetoothMac: str
    timeZone: str
    deviceBrand: str
    deviceModel: str
    deviceName: str
    netType: int
    language: str
    province: str
    city: str


class PhoneGroup(TypedDict, total=False):
    id: str
    name: str
    remark: str


class Phone(TypedDict, total=False):
    id: str
    serialName: str
    serialNo: str
    group: PhoneGroup
    remark: str
    status: int
    tags: List[Dict[str, str]]
    equipmentInfo: EquipmentInfo
    proxy: Dict[str, Any]
    chargeMode: int
    hasBind: bool
    monthlyExpire: int
    rpaStatus: int


class PhoneListResp(TypedDict):
    total: int
    page: int
    pageSize: int
    items: List[Phone]


class AddNewDetail(TypedDict, total=False):
    index: int
    code: int
    msg: str
    id: str
    profileName: str
    envSerialNo: str
    equipmentInfo: EquipmentInfo


class AddNewResp(TypedDict):
    totalAmount: int
    successAmount: int
    failAmount: int
    details: List[AddNewDetail]


class PhoneStatusResp(TypedDict):
    totalAmount: int
    successAmount: int
    failAmount: int
    successDetails: List[Dict[str, Any]]
    failDetails: List[Dict[str, Any]]


class GpsItem(TypedDict):
    id: str
    latitude: float
    longitude: float


class GpsGetResp(TypedDict):
    totalAmount: int
    successAmount: int
    failAmount: int
    list: List[GpsItem]


class ScreenShotResp(TypedDict):
    taskId: str


class ScreenShotResultResp(TypedDict, total=False):
    status: int
    downloadLink: str


class BrandItem(TypedDict):
    surfaceBrandName: str
    surfaceModelName: str


class TransferResp(TypedDict, total=False):
    successCount: int
    failCount: int
    failEnvIds: List[str]


class ContactObject(TypedDict, total=False):
    firstName: str
    lastName: str
    mobile: str
    work: str
    fax: str
    email1: str
    email2: str


# ── RPA / Automation ─────────────────────────────────────────────

class RpaTaskIdResp(TypedDict):
    taskId: str


class TaskFlowItem(TypedDict):
    id: str
    title: str
    desc: str
    params: List[str]


class TaskFlowListResp(TypedDict):
    total: int
    page: int
    pageSize: int
    items: List[TaskFlowItem]


# ── Task ─────────────────────────────────────────────────────────

class TaskType(enum.IntEnum):
    TIKTOK_VIDEO = 1
    TIKTOK_WARMUP = 2
    TIKTOK_IMAGE_SET = 3
    TIKTOK_LOGIN = 4
    TIKTOK_EDIT_PROFILE = 6
    CUSTOM = 42


class TaskStatus(enum.IntEnum):
    WAITING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    FAILED = 4
    CANCELLED = 7


class Task(TypedDict, total=False):
    id: str
    planName: str
    taskType: int
    serialName: str
    envId: str
    scheduleAt: int
    status: int
    failCode: int
    failDesc: str
    cost: int
    shareLink: str


class QueryResp(TypedDict):
    total: int
    items: List[Task]


# ── ADB ──────────────────────────────────────────────────────────

class AdbDataItem(TypedDict):
    code: int
    id: str
    ip: str
    port: str
    pwd: str


# ── Analytics ────────────────────────────────────────────────────

class AnalyticsAccount(TypedDict, total=False):
    id: str
    account: str
    channel: int
    remark: str
    operator: str
    created_time: int
    updated_time: int


class AnalyticsAccountsListResp(TypedDict):
    total: int
    page: int
    items: List[AnalyticsAccount]


class AnalyticsAddAccountsResp(TypedDict):
    bizCode: int
    successCount: int
    failCount: int
    repeatCount: int


class AnalyticsDataItem(TypedDict, total=False):
    id: str
    channel: int
    account: str
    playCount: int
    followerCount: int
    diggCount: int
    commentCount: int
    collectCount: int
    shareCount: int
    dataDate: int
    addAccDate: int
    remark: str
    createdId: str
    username: str


class AnalyticsDataResp(TypedDict):
    total: int
    page: int
    pageSize: int
    items: List[AnalyticsDataItem]


# ── Application Management ───────────────────────────────────────

class AppTeamAppListItem(TypedDict, total=False):
    id: str
    appName: str
    appIcon: str
    versionId: str
    versionCode: int
    versionName: str
    status: int
    isUpload: bool
    uploadStatus: int
    appAuth: int
    appRoot: int
    envGroups: List[str]


class AppTeamAppListResp(TypedDict):
    total: int
    page: int
    pageSize: int
    items: List[AppTeamAppListItem]


class AppInfo(TypedDict, total=False):
    appIcon: str
    id: str
    appId: str
    appName: str
    packageName: str
    appVersionInfoList: List[Dict[str, Any]]
    appVersionId: str
    installStatus: int
    installTime: str
    versionCode: str
    versionName: str


class AppListResp(TypedDict):
    total: int
    page: int
    pageSize: int
    items: List[AppInfo]


class AppUploadStatusResp(TypedDict):
    status: int
    appName: str
    appIcon: str
    appId: str
    versionId: str


# ── Library ──────────────────────────────────────────────────────

class MaterialTag(TypedDict, total=False):
    id: str
    name: str
    color: int


class MaterialItem(TypedDict, total=False):
    id: str
    createdTime: int
    fileName: str
    fileSize: int
    fileUrl: str
    fileType: int
    width: int
    height: int
    source: int
    tags: List[MaterialTag]
    userName: str


class MaterialSearchResp(TypedDict):
    total: int
    page: int
    pageSize: int
    list: List[MaterialItem]


class MaterialTagSearchResp(TypedDict):
    total: int
    page: int
    pageSize: int
    list: List[MaterialTag]


# ── Billing ──────────────────────────────────────────────────────

class BalanceResp(TypedDict):
    balance: float
    giftMoney: float
    availableTimeAddOn: int


class PlanProfile(TypedDict):
    id: str
    price: float
    level: int
    envNum: int
    freeTime: int
    openEnvNumOneDay: int
    createEnvNumOneDay: int


class PlanInfoResp(TypedDict):
    plan: int
    profiles: int
    monthlyRental: int
    parallels: int
    expirationTime: int
    monthlyFee: float
    availableProfiles: int
    availableMonthlyRentals: int


# ── Group Management ─────────────────────────────────────────────

class GroupCreateResp(TypedDict, total=False):
    totalAmount: int
    successAmount: int
    failAmount: int
    successDetails: List[Dict[str, Any]]
    failDetails: List[FailDetail]


class GroupItem(TypedDict, total=False):
    id: str
    name: str
    remark: str


class GroupQueryResp(TypedDict):
    total: int
    page: int
    pageSize: int
    list: List[GroupItem]


# ── Proxy Management ─────────────────────────────────────────────

class ProxyAddResp(TypedDict, total=False):
    totalAmount: int
    successAmount: int
    failAmount: int
    failDetails: List[Dict[str, Any]]
    successDetails: List[Dict[str, Any]]


class ProxyListItem(TypedDict, total=False):
    id: str
    serialNo: str
    scheme: str
    server: str
    port: int
    username: str
    password: str


class ProxyListResp(TypedDict):
    total: int
    page: int
    pageSize: int
    list: List[ProxyListItem]


# ── Tag Management ───────────────────────────────────────────────

class TagCreateResp(TypedDict, total=False):
    totalAmount: int
    successAmount: int
    failAmount: int
    successDetails: List[Dict[str, Any]]
    failDetails: List[FailDetail]


class TagItem(TypedDict, total=False):
    id: str
    name: str
    color: str


class TagQueryResp(TypedDict):
    total: int
    page: int
    pageSize: int
    list: List[TagItem]


# ── Proxy Detection ──────────────────────────────────────────────

class ProxyCheckResp(TypedDict, total=False):
    detectStatus: bool
    message: str
    outboundIP: str
    countryCode: str
    countryName: str
    subdivision: str
    city: str
    timezone: str
    isp: str


# ── Browser API ──────────────────────────────────────────────────

class BrowserListResp(TypedDict):
    total: int
    page: int
    pageSize: int
    items: List[Dict[str, Any]]


class BrowserDeleteResp(TypedDict, total=False):
    successIds: List[str]
    busyIds: List[str]
    serverErrIds: List[str]


class BrowserTransferResp(TypedDict, total=False):
    successCount: int
    failCount: int
    failEnvIds: List[str]


class BrowserTask(TypedDict, total=False):
    id: str
    eid: str
    name: str
    remark: str
    serialName: str
    status: int
    startAt: int
    finishAt: int
    cost: int
    resultCode: int
    resultDesc: str
    scheduleAt: int


class BrowserTaskQueryResp(TypedDict):
    total: int
    page: int
    pageSize: int
    list: List[BrowserTask]


# ── Webhook ──────────────────────────────────────────────────────

class CallbackType(enum.IntEnum):
    CLOUD_PHONE_STARTUP = 1
    CLOUD_PHONE_FILE_UPLOAD = 4
    CLOUD_PHONE_SCREENSHOT = 5
    CLOUD_PHONE_RPA_TASK_COMPLETION = 6
    CLOUD_PHONE_SHUTDOWN = 8
    CLOUD_PHONE_NAME_CHANGE = 9
    CLOUD_PHONE_DELETION = 10
    CLOUD_PHONE_TAG_CHANGE = 11
    CLOUD_PHONE_RPA_TASK_CREATION = 12
    CLOUD_PHONE_RPA_TASK_CANCELLATION = 13
    BATCH_IMPORT_CONTACTS = 14
    APP_INSTALLATION = 15
