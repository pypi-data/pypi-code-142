from __future__ import annotations

import warnings
from typing import Any, TypeVar

from ccxt.async_support import Exchange

from ccxt_wrapper.wrapper.base import CCXTWrapperBase

from ..core import cast
from ..dtypes import (
    Account,
    Balance,
    Balances,
    BorrowInterest,
    Deposit,
    FundingHistory,
    LedgerEntry,
    Literal,
    Margin,
    MarginLoan,
    Order,
    Position,
    PrivateTrade,
    TradingFee,
    Transaction,
    TransactionFees,
    Transfer,
)
from .cast import cast_order, cast_private_trade

_Exchange = TypeVar("_Exchange", bound=Exchange)


class CCXTWrapperPrivate(CCXTWrapperBase[_Exchange]):
    async def fetch_accounts(self, params: dict[str, Any] = {}) -> list[Account]:
        accounts = await self._ex.fetch_accounts(params)
        return [cast(Account, account) for account in accounts]

    async def fetch_balance(self, params: dict[str, Any] = {}) -> Balances:
        balance = await self._ex.fetch_balance(params)
        res = cast(Balances, balance)
        for key, value in balance.items():
            if key in ["info", "free", "used", "total"]:
                continue
            if not isinstance(value, dict):
                warnings.warn(RuntimeWarning(f"Unexpected type for key {key}"))
                continue
            res[key] = cast(Balance, value)
        return res

    async def create_order(
        self,
        symbol: str,
        type: Literal["market", "limit"],
        side: Literal["buy", "sell"],
        amount: float,
        price: float | None = None,
        params: dict[str, Any] = {},
    ) -> Order:
        order = await self._ex.create_order(symbol, type, side, amount, price, params)
        return cast_order(order)

    async def cancel_order(
        self, id: str, symbol: str | None = None, params: dict[str, Any] = {}
    ) -> Order:
        order = await self._ex.cancel_order(id, symbol, params)
        return cast_order(order)

    async def fetch_order(
        self, id: str, symbol: str | None = None, params: dict[str, Any] = {}
    ) -> Order:
        order = await self._ex.fetch_order(id, symbol, params)
        return cast_order(order)

    async def fetch_orders(
        self,
        symbol: str | None = None,
        since: int | None = None,
        limit: int | None = None,
        params: dict[str, Any] = {},
    ) -> list[Order]:
        orders = await self._ex.fetch_orders(symbol, since, limit, params)
        return [cast_order(order) for order in orders]

    async def fetch_open_orders(
        self,
        symbol: str | None = None,
        since: int | None = None,
        limit: int | None = None,
        params: dict[str, Any] = {},
    ) -> list[Order]:
        orders = await self._ex.fetch_open_orders(symbol, since, limit, params)
        return [cast_order(order) for order in orders]

    async def fetch_closed_orders(
        self,
        symbol: str | None = None,
        since: int | None = None,
        limit: int | None = None,
        params: dict[str, Any] = {},
    ) -> list[Order]:
        orders = await self._ex.fetch_closed_orders(symbol, since, limit, params)
        return [cast_order(order) for order in orders]

    async def edit_order(
        self,
        id: str,
        symbol: str | None = None,
        type: Literal["market", "limit"] | None = None,
        side: Literal["buy", "sell"] | None = None,
        amount: float | None = None,
        price: float | None = None,
        params: dict[str, Any] = {},
    ) -> Order:
        order = await self._ex.edit_order(id, symbol, type, side, amount, price, params)
        return cast_order(order)

    async def fetch_my_trades(
        self,
        symbol: str | None = None,
        since: int | None = None,
        limit: int | None = None,
        params: dict[str, Any] = {},
    ) -> list[PrivateTrade]:
        trades = await self._ex.fetch_my_trades(symbol, since, limit, params)
        return [cast_private_trade(trade) for trade in trades]

    async def fetch_ledger(
        self,
        code: str | None = None,
        since: int | None = None,
        limit: int | None = None,
        params: dict[str, Any] = {},
    ) -> list[LedgerEntry]:
        ledger_entries = await self._ex.fetch_ledger(code, since, limit, params)
        return [cast(LedgerEntry, entry) for entry in ledger_entries]

    async def fetch_deposit(
        self, id: str, code: str | None = None, params: dict[str, Any] = {}
    ) -> Deposit:
        deposit = await self._ex.fetch_deposit(id, code, params)
        return cast(Deposit, deposit)

    async def fetch_deposits(
        self,
        code: str | None = None,
        since: int | None = None,
        limit: int | None = None,
        params: dict[str, Any] = {},
    ) -> list[Deposit]:
        deposits = await self._ex.fetch_deposits(code, since, limit, params)
        return [cast(Deposit, deposit) for deposit in deposits]

    async def fetch_withdrawal(
        self, id: str, code: str | None = None, params: dict[str, Any] = {}
    ) -> Transaction:
        withdrawal = await self._ex.fetch_withdrawal(id, code, params)
        return cast(Transaction, withdrawal)

    async def fetch_withdrawals(
        self,
        code: str | None = None,
        since: int | None = None,
        limit: int | None = None,
        params: dict[str, Any] = {},
    ) -> list[Transaction]:
        withdrawals = await self._ex.fetch_withdrawals(code, since, limit, params)
        return [cast(Transaction, withdrawal) for withdrawal in withdrawals]

    async def withdraw(
        self,
        code: str,
        amount: float,
        address: str,
        tag: str | None = None,
        params: dict[str, Any] = {},
    ) -> Transaction:
        withdrawal = await self._ex.withdraw(code, amount, address, tag, params)
        return cast(Transaction, withdrawal)

    async def transfer(
        self,
        code: str,
        amount: float,
        from_account: str,
        to_account: str,
        params: dict[str, Any] = {},
    ) -> Transfer:
        transfer = await self._ex.transfer(
            code, amount, from_account, to_account, params
        )
        return cast(Transfer, transfer)

    async def fetch_trading_fees(
        self, params: dict[str, Any] = {}
    ) -> dict[str, TradingFee] | None:
        fees = await self._ex.fetch_trading_fees(params)
        if fees is not None:
            return {symbol: cast(TradingFee, value) for symbol, value in fees.items()}
        return None

    async def fetch_transaction_fees(
        self, codes: list[str] | None = None, params: dict[str, Any] = {}
    ) -> TransactionFees:
        fees = await self._ex.fetch_transaction_fees(codes, params)
        return cast(TransactionFees, fees)

    async def fetch_borrow_interest(
        self,
        code: str,
        symbol: str | None = None,
        since: int | None = None,
        limit: int | None = None,
        params: dict[str, Any] = {},
    ) -> BorrowInterest | None:
        interest = await self._ex.fetch_borrow_interest(
            code, symbol, since, limit, params
        )
        if isinstance(interest, dict):
            return cast(BorrowInterest, interest)
        return None

    async def borrow_margin(
        self, code: str, amount: float, params: dict[str, Any] = {}
    ) -> MarginLoan:
        loan = await self._ex.borrow_margin(code, amount, params)
        return cast(MarginLoan, loan)

    async def repay_margin(
        self, code: str, amount: float, params: dict[str, Any] = {}
    ) -> MarginLoan:
        loan = await self._ex.repay_margin(code, amount, params)
        return cast(MarginLoan, loan)

    async def add_margin(
        self, code: str, amount: float, params: dict[str, Any] = {}
    ) -> Margin:
        margin = await self._ex.add_margin(code, amount, params)
        return cast(Margin, margin)

    async def reduce_margin(
        self, code: str, amount: float, params: dict[str, Any] = {}
    ) -> Margin:
        margin = await self._ex.reduce_margin(code, amount, params)
        return cast(Margin, margin)

    async def set_margin(
        self, code: str, amount: float, params: dict[str, Any] = {}
    ) -> Margin:
        margin = await self._ex.set_margin(code, amount, params)
        return cast(Margin, margin)

    async def set_margin_mode(
        self, code: str, mode: Literal["cross", "isolated"], params: dict[str, Any] = {}
    ) -> Any:
        return await self._ex.set_margin_mode(code, mode, params)

    async def set_leverage(
        self, code: str, leverage: float, params: dict[str, Any] = {}
    ) -> Any:
        return await self._ex.set_leverage(code, leverage, params)

    async def fetch_position(
        self, symbol: str, params: dict[str, Any] = {}
    ) -> Position:
        position = await self._ex.fetch_position(symbol, params)
        return cast(Position, position)

    async def fetch_positions(
        self, symbols: list[str] | None = None, params: dict[str, Any] = {}
    ) -> list[Position]:
        positions = await self._ex.fetch_positions(symbols, params)
        return [cast(Position, position) for position in positions]

    async def fetch_account_positions(
        self, symbols: list[str] | None = None, params: dict[str, Any] = {}
    ) -> list[Position]:
        positions = await self._ex.fetch_account_positions(symbols, params)
        return [cast(Position, position) for position in positions]

    async def fetch_funding_history(
        self,
        code: str | None = None,
        since: int | None = None,
        limit: int | None = None,
        params: dict[str, Any] = {},
    ) -> list[FundingHistory]:
        history = await self._ex.fetch_funding_history(code, since, limit, params)
        return [cast(FundingHistory, entry) for entry in history]
