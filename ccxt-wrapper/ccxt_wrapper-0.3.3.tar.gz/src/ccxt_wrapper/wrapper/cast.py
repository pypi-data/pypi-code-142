from copy import deepcopy

from ..core import cast
from ..dtypes import (
    Any,
    Currency,
    CurrencyLimits,
    Fee,
    Market,
    MarketLimits,
    MinMax,
    Order,
    Precision,
    PrivateTrade,
)


def cast_market(market: dict[str, Any]) -> Market:
    market = deepcopy(market)
    for key_limits, limits in market["limits"].items():
        market["limits"][key_limits] = cast(MinMax, limits)
    if market.get("precision") is not None:
        market["precision"] = cast(Precision, market["precision"])
    if market.get("limits") is not None:
        market["limits"] = cast(MarketLimits, market["limits"])
    return cast(Market, market)


def cast_currency(currency: dict[str, Any]) -> Currency:
    currency = deepcopy(currency)
    if currency.get("limits") is not None:
        currency["limits"] = cast(CurrencyLimits, currency["limits"])
    return cast(Currency, currency)


def cast_order(order: dict[str, Any]) -> Order:
    order = deepcopy(order)
    if order.get("fee") is not None:
        order["fee"] = cast(Fee, order["fee"])
    if order.get("trades") is not None:
        order["trades"] = [cast(PrivateTrade, trade) for trade in order["trades"]]
    return cast(Order, order)


def cast_private_trade(trade: dict[str, Any]) -> PrivateTrade:
    trade = deepcopy(trade)
    if trade.get("fee") is not None:
        trade["fee"] = cast(Fee, trade["fee"])
    return cast(PrivateTrade, trade)
