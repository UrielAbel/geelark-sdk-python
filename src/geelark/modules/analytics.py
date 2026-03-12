"""Analytics – account management and data retrieval."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..core.errors import GeelarkError
from ..core.http import HttpClient
from ..core.utils import build_body


class AnalyticsModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def accounts_list(self, *, page: int = 1, page_size: int = 10, account: Optional[str] = None, channel: Optional[int] = None, user_account: Optional[str] = None) -> Dict[str, Any]:
        return self._http.post("/analytics/accounts/list", build_body(page=page, page_size=page_size, account=account, channel=channel, user_account=user_account))

    def add_accounts(self, *, channel: int, accounts_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not accounts_data:
            raise GeelarkError("analytics.add_accounts: accounts_data required")
        return self._http.post("/analytics/accounts/add", build_body(channel=channel, accounts_data=accounts_data))

    def delete_account(self, channel: int, account: str) -> None:
        self._http.post("/analytics/accounts/delete", {"channel": channel, "account": account})

    def get_data(self, *, page: int = 1, page_size: int = 10, account: Optional[str] = None, data_date: Optional[int] = None, created_id: Optional[str] = None, channel: Optional[int] = None) -> Dict[str, Any]:
        return self._http.post("/analytics/data", build_body(page=page, page_size=page_size, account=account, data_date=data_date, created_id=created_id, channel=channel))

    def update_account(self, *, id: str, account: Optional[str] = None, channel: Optional[int] = None, remark: Optional[str] = None) -> None:
        if not id:
            raise GeelarkError("analytics.update_account: id required")
        self._http.post("/analytics/accounts/update", build_body(id=id, account=account, channel=channel, remark=remark))
