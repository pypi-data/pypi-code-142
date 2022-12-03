from __future__ import annotations

from typing import Any, TypeVar

from ccxt.async_support import Exchange

from ccxt_wrapper.dtypes import (
    BorrowRate,
    Currency,
    FundingRate,
    FundingRateHistory,
    LeverageTier,
    Market,
    Ohlcv,
    OpenInterest,
    OrderBook,
    PositionsRisk,
    PublicTrade,
    Status,
    Ticker,
)
from ccxt_wrapper.wrapper.base import CCXTWrapperBase

from ..core import cast
from .cast import cast_currency, cast_market

_Exchange = TypeVar("_Exchange", bound=Exchange)


class CCXTWrapperPublic(CCXTWrapperBase[_Exchange]):
    async def fetch_time(self, params: dict[str, Any] = {}) -> int | None:
        return await self._ex.fetch_time(params)

    async def fetch_status(self, params: dict[str, Any] = {}) -> Status:
        status = await self._ex.fetch_status(params)
        return cast(Status, status)

    async def load_markets(
        self, reload: bool = False, params: dict[str, Any] = {}
    ) -> dict[str, Market]:
        markets = await self._ex.load_markets(reload, params)
        if isinstance(markets, list):
            return {market["symbol"]: cast_market(market) for market in markets}
        return {symbol: cast_market(market) for symbol, market in markets.items()}

    async def fetch_markets(self, params: dict[str, Any] = {}) -> dict[str, Market]:
        markets = await self._ex.fetch_markets(params)
        if isinstance(markets, list):
            return {market["symbol"]: cast_market(market) for market in markets}
        return {symbol: cast_market(market) for symbol, market in markets.items()}

    async def fetch_currencies(
        self, params: dict[str, Any] = {}
    ) -> dict[str, Currency] | None:
        currencies = await self._ex.fetch_currencies(params)
        if currencies is None:
            return None
        return {code: cast_currency(currency) for code, currency in currencies.items()}

    async def fetch_ticker(self, symbol: str, params: dict[str, Any] = {}) -> Ticker:
        ticker = await self._ex.fetch_ticker(symbol, params)
        return cast(Ticker, ticker)

    async def fetch_tickers(
        self, symbols: list[str], params: dict[str, Any] = {}
    ) -> dict[str, Ticker] | None:
        tickers = await self._ex.fetch_tickers(symbols, params)
        if isinstance(tickers, list):
            return {ticker["symbol"]: cast(Ticker, ticker) for ticker in tickers}
        if isinstance(tickers, dict):
            return {symbol: cast(Ticker, ticker) for symbol, ticker in tickers.items()}
        return None

    async def fetch_trades(
        self,
        symbol: str,
        since: int | None = None,
        limit: int | None = None,
        params: dict[str, Any] = {},
    ) -> list[PublicTrade]:
        trades = await self._ex.fetch_trades(symbol, since, limit, params)
        return [cast(PublicTrade, trade) for trade in trades]

    async def fetch_order_book(
        self, symbol: str, limit: int | None = None, params: dict[str, Any] = {}
    ) -> OrderBook:
        order_book = await self._ex.fetch_order_book(symbol, limit, params)
        return cast(OrderBook, order_book)

    async def fetch_ohlcv(
        self,
        symbol: str,
        timeframe: str = "1m",
        since: int | None = None,
        limit: int | None = None,
        params: dict[str, Any] = {},
    ) -> Ohlcv:
        ohlcvs = await self._ex.fetch_ohlcv(symbol, timeframe, since, limit, params)
        return [tuple(ohlcv) for ohlcv in ohlcvs]  # type: ignore

    async def fetch_borrow_rate(
        self, code: str, params: dict[str, Any] = {}
    ) -> BorrowRate:
        borrow_rate = await self._ex.fetch_borrow_rate(code, params)
        return cast(BorrowRate, borrow_rate)

    async def fetch_borrow_rates(
        self, params: dict[str, Any] = {}
    ) -> dict[str, BorrowRate]:
        borrow_rates = await self._ex.fetch_borrow_rates(params)
        return {
            code: cast(BorrowRate, borrow_rate)
            for code, borrow_rate in borrow_rates.items()
        }

    async def fetch_borrow_rates_per_symbol(
        self, params: dict[str, Any] = {}
    ) -> dict[str, BorrowRate]:
        borrow_rates = await self._ex.fetch_borrow_rates_per_symbol(params)
        return {
            symbol: cast(BorrowRate, borrow_rate)
            for symbol, borrow_rate in borrow_rates.items()
        }

    async def fetch_borrow_rate_history(
        self, code: str, params: dict[str, Any] = {}
    ) -> list[BorrowRate]:
        borrow_rate_history = await self._ex.fetch_borrow_rate_history(code, params)
        return [cast(BorrowRate, borrow_rate) for borrow_rate in borrow_rate_history]

    async def fetch_market_leverage_tiers(
        self, symbol: str, params: dict[str, Any] = {}
    ) -> list[LeverageTier]:
        leverage_tiers = await self._ex.fetch_market_leverage_tiers(symbol, params)
        return cast(list[LeverageTier], leverage_tiers)

    async def fetch_leverage_tiers(
        self, symbols: list[str] | None, params: dict[str, Any] = {}
    ) -> dict[str, list[LeverageTier]]:
        leverage_tiers = await self._ex.fetch_leverage_tiers(symbols, params)
        return {
            symbol: cast(list[LeverageTier], leverage_tier)
            for symbol, leverage_tier in leverage_tiers.items()
        }

    async def fetch_funding_rate(
        self, symbol: str, params: dict[str, Any] = {}
    ) -> FundingRate:
        funding_rate = await self._ex.fetch_funding_rate(symbol, params)
        return cast(FundingRate, funding_rate)

    async def fetch_funding_rates(
        self, symbols: list[str] | None, params: dict[str, Any] = {}
    ) -> dict[str, FundingRate]:
        funding_rates = await self._ex.fetch_funding_rates(symbols, params)
        if isinstance(funding_rates, list):
            return {
                funding_rate["symbol"]: cast(FundingRate, funding_rate)
                for funding_rate in funding_rates
            }
        return {
            symbol: cast(FundingRate, funding_rate)
            for symbol, funding_rate in funding_rates.items()
        }

    async def fetch_funding_rate_history(
        self, symbol: str, params: dict[str, Any] = {}
    ) -> list[FundingRateHistory]:
        funding_rate_history = await self._ex.fetch_funding_rate_history(symbol, params)
        return [
            cast(FundingRateHistory, funding_rate)
            for funding_rate in funding_rate_history
        ]

    async def fetch_open_interest(
        self, symbols: list[str], params: dict[str, Any] = {}
    ) -> dict[str, OpenInterest]:
        open_interests = await self._ex.fetch_open_interest(symbols, params)
        return {
            symbol: cast(OpenInterest, open_interest)
            for symbol, open_interest in open_interests.items()
        }

    async def fetch_open_interest_history(
        self,
        symbol: str,
        timeframe: str = "1m",
        since: int | None = None,
        limit: int | None = None,
        params: dict[str, Any] = {},
    ) -> list[OpenInterest]:
        open_interests = await self._ex.fetch_open_interest_history(
            symbol, timeframe, since, limit, params
        )
        return [cast(OpenInterest, open_interest) for open_interest in open_interests]

    async def fetch_positions_risk(
        self, symbols: list[str] | None = None, params: dict[str, Any] = {}
    ) -> dict[str, PositionsRisk]:
        positions_risk = await self._ex.fetch_positions_risk(symbols, params)
        if isinstance(positions_risk, list):
            return {
                position_risk["symbol"]: cast(PositionsRisk, position_risk)
                for position_risk in positions_risk
            }
        return {
            symbol: cast(PositionsRisk, position_risk)
            for symbol, position_risk in positions_risk.items()
        }

    """{
    'id':   'exchange'                   // lowercase string exchange id
    'name': 'Exchange'                   // human-readable string
    'countries': [ 'US', 'CN', 'EU' ],   // array of ISO country codes
    'urls': {
        'api': 'https://api.example.com/data',  // string or dictionary of base API URLs
        'www': 'https://www.example.com'        // string website URL
        'doc': 'https://docs.example.com/api',  // string URL or array of URLs
    },
    'version':         'v1',             // string ending with digits
    'api':             { ... },          // dictionary of api endpoints
    'has': {                             // exchange capabilities
        'CORS': false,
        'publicAPI': true,
        'privateAPI': true,
        'cancelOrder': true,
        'createDepositAddress': false,
        'createOrder': true,
        'fetchBalance': true,
        'fetchCanceledOrders': false,
        'fetchClosedOrder': false,
        'fetchClosedOrders': false,
        'fetchCurrencies': false,
        'fetchDepositAddress': false,
        'fetchMarkets': true,
        'fetchMyTrades': false,
        'fetchOHLCV': false,
        'fetchOpenOrder': false,
        'fetchOpenOrders': false,
        'fetchOrder': false,
        'fetchOrderBook': true,
        'fetchOrders': false,
        'fetchStatus': 'emulated',
        'fetchTicker': true,
        'fetchTickers': false,
        'fetchBidsAsks': false,
        'fetchTrades': true,
        'withdraw': false,
    },
    'timeframes': {
    // empty if the exchange.has['fetchOHLCV'] !== true
        '1m': '1minute',
        '1h': '1hour',
        '1d': '1day',
        '1M': '1month',
        '1y': '1year',
    },
    'timeout':           10000,          // number in milliseconds
    'rateLimit':         2000,           // number in milliseconds
    'userAgent':        'ccxt/1.1.1 ...' // string, HTTP User-Agent header
    'verbose':           false,          // boolean, output error details
    'markets':          { ... }          // dictionary of markets/pairs by symbol
    'symbols':          [ ... ]          // sorted list of string symbols (traded pairs)
    'currencies':       { ... }          // dictionary of currencies by currency code
    'markets_by_id':    { ... },         // dictionary of dictionaries (markets) by id
    'currencies_by_id': { ... },         // dictionary of dictionaries (markets) by id
    'apiKey':   '92560ffae9b8a0421...',  // string public apiKey (ASCII, hex, Base64
    , ...)
    'secret':   '9aHjPmW+EtRRKN/Oi...'   // string private secret key
    'password': '6kszf4aci8r',           // string password
    'uid':      '123456',                // string user id
    'options':          { ... },         // exchange-specific options
    // ... other properties here ...
}"""

    @property
    def id(self) -> str:
        """Lowercase string exchange id."""
        return self._ex.id

    @property
    def name(self) -> str:
        """Human-readable string."""
        return self._ex.name

    @property
    def countries(self) -> list[str]:
        """Array of ISO country codes."""
        return self._ex.countries

    @property
    def urls(self) -> dict[str, str]:
        """Dictionary of base API URLs."""
        return self._ex.urls

    @property
    def version(self) -> str:
        """String ending with digits."""
        return self._ex.version

    @property
    def api(self) -> dict[str, dict[str, str]]:
        """Dictionary of api endpoints."""
        return self._ex.api

    @property
    def has(self) -> dict[str, bool]:
        """Exchange capabilities."""
        return self._ex.has

    @property
    def timeframes(self) -> dict[str, str]:
        """Empty if the exchange.has['fetchOHLCV'] !== true."""
        return self._ex.timeframes

    @property
    def timeout(self) -> int:
        """Number in milliseconds."""
        return self._ex.timeout

    @property
    def rateLimit(self) -> int:
        """Number in milliseconds."""
        return self._ex.rateLimit

    @property
    def userAgent(self) -> str:
        """HTTP User-Agent header."""
        return self._ex.userAgent

    @property
    def verbose(self) -> bool:
        """Output error details."""
        return self._ex.verbose

    @property
    def markets(self) -> dict[str, Market]:
        """Dictionary of markets/pairs by symbol."""
        return {
            symbol: cast_market(market) for symbol, market in self._ex.markets.items()
        }

    @property
    def symbols(self) -> list[str]:
        """Sorted list of string symbols (traded pairs)."""
        return self._ex.symbols

    @property
    def currencies(self) -> dict[str, Currency]:
        """Dictionary of currencies by currency code."""
        return {
            code: cast_currency(currency)
            for code, currency in self._ex.currencies.items()
        }

    @property
    def markets_by_id(self) -> dict[str, Market]:
        """Dictionary of dictionaries (markets) by id."""
        return {
            id: cast_market(market) for id, market in self._ex.markets_by_id.items()
        }

    @property
    def currencies_by_id(self) -> dict[str, Currency]:
        """Dictionary of dictionaries (markets) by id."""
        return {
            id: cast_currency(currency)
            for id, currency in self._ex.currencies_by_id.items()
        }

    @property
    def apiKey(self) -> str:
        """Public apiKey (ASCII, hex, Base64, ...)."""
        return self._ex.apiKey

    @property
    def secret(self) -> str:
        """Private secret key."""
        return self._ex.secret

    @property
    def password(self) -> str:
        """Password."""
        return self._ex.password

    @property
    def uid(self) -> str:
        """User id."""
        return self._ex.uid

    @property
    def options(self) -> dict[str, Any]:
        """Exchange-specific options."""
        return self._ex.options
