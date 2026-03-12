"""Billing – balance, plan management."""
from __future__ import annotations

from typing import Any, Dict, Optional

from ..core.errors import GeelarkError
from ..core.http import HttpClient
from ..core.utils import build_body


class BillingModule:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def balance_inquiry(self) -> Dict[str, Any]:
        """Get account balance, gift money, and time add-on."""
        return self._http.post("/pay/wallet", {})

    def change_plan(
        self,
        *,
        profiles_id: str,
        parallels_num: int,
        monthly_rental_num: int,
        days: Optional[int] = None,
        promo_code: Optional[str] = None,
    ) -> None:
        self._http.post("/pay/plan/upgrade", build_body(
            profiles_id=profiles_id, parallels_num=parallels_num,
            monthly_rental_num=monthly_rental_num, days=days, promo_code=promo_code,
        ))

    def get_plan_list(self) -> Any:
        """Get available subscription plans."""
        return self._http.post("/pay/profiles/list", {})

    def get_current_plan_info(self) -> Dict[str, Any]:
        """Get current subscription plan information."""
        return self._http.post("/pay/plan/info", {})

    def renew_plan(self, days: int, promo_code: Optional[str] = None) -> None:
        """Renew the current plan. days must be 30, 90, 180 or 360."""
        if not days:
            raise GeelarkError("billing.renew_plan: days required")
        self._http.post("/pay/plan/continue", build_body(days=days, promo_code=promo_code))
