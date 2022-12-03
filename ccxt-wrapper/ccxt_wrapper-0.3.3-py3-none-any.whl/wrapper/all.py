from __future__ import annotations

from datetime import datetime
from typing import Any, Literal, TypeVar

from ccxt.async_support import Exchange

from ccxt_wrapper.wrapper.private import CCXTWrapperPrivate
from ccxt_wrapper.wrapper.public import CCXTWrapperPublic

from ..dtypes import Ohlcv, Order

_Exchange = TypeVar("_Exchange", bound=Exchange)


class CCXTWrapper(CCXTWrapperPublic[_Exchange], CCXTWrapperPrivate[_Exchange]):

    _ex: _Exchange

    @staticmethod
    def new(
        exchange_type: type[_Exchange],
        api_key: str | None = None,
        secret: str | None = None,
        enableRateLimit: bool = True,
        sandbox: bool = False,
        default_type: Literal["spot", "margin", "delivery", "future"] | None = None,
        **kwargs: Any,
    ) -> CCXTWrapper[_Exchange]:
        d: dict[str, Any] = {
            "apiKey": api_key,
            "secret": secret,
            "enableRateLimit": enableRateLimit,
        }
        if default_type is not None:
            d["options"] = {"defaultType": default_type}
        kwargs.update(d)
        ex = exchange_type(kwargs)
        ex.set_sandbox_mode(sandbox)
        return CCXTWrapper(ex)

    async def create_order_smart(
        self,
        symbol: str,
        type: Literal["market", "limit"],
        amount: float,
        price: float | None = None,
        params: dict[str, Any] = {},
    ) -> Order:
        return await super().create_order(
            symbol, type, "buy" if amount > 0 else "sell", abs(amount), price, params
        )

    async def edit_order_smart(
        self,
        id: str,
        symbol: str,
        type: Literal["market", "limit"],
        amount: float,
        price: float | None = None,
        params: dict[str, Any] = {},
    ) -> Order:
        return await super().edit_order(
            id,
            symbol,
            type,
            "buy" if amount > 0 else "sell",
            abs(amount),
            price,
            params,
        )

    async def fetch_closed_ohlcv(
        self,
        symbol: str,
        timeframe: str = "1m",
        since: int | None = None,
        limit: int | None = None,
        params: dict[str, Any] = {},
    ) -> Ohlcv:
        ohlcv = await self._ex.fetch_ohlcv(symbol, timeframe, since, limit, params)
        if ohlcv[-1][
            0
        ] > datetime.utcnow().timestamp() * 1000 - self._ex.parse_timeframe(timeframe):
            ohlcv = ohlcv[:-1]
        return ohlcv
