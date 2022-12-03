from __future__ import annotations

from typing import Any, Dict, List, Literal

import attrs
from strenum import StrEnum

# Child classes used everywhere.


@attrs.frozen()
class MinMax:
    min: float
    max: float


@attrs.frozen()
class CurrencyLimits:
    amount: MinMax
    withdraw: MinMax
    deposit: MinMax


@attrs.frozen()
class MarketLimits:
    amount: MinMax
    price: MinMax
    cost: MinMax
    leverage: MinMax
    market: MinMax


@attrs.frozen()
class Fee:
    """https://docs.ccxt.com/en/latest/manual.html#fee-structure
    {
        'currency': 'BTC', // the unified fee currency code
        'rate': percentage, // the fee rate, 0.05% = 0.0005, 1% = 0.01, ...
        'cost': feePaid, // the fee cost (amount * fee rate)
    }"""

    currency: str
    """The unified fee currency code"""
    rate: float | None
    """The fee rate, 0.05% = 0.0005, 1% = 0.01, ..."""
    cost: float | None
    """The fee cost (amount * fee rate)"""


# Public API


@attrs.frozen()
class Currency:
    """https://docs.ccxt.com/en/latest/manual.html#currency-structure
    {
        'id':       'btc',       // string literal for referencing within an exchange
        'code':     'BTC',       // uppercase unified string literal code the currency
        'name':     'Bitcoin',   // string, human-readable name, if specified
        'active':    true,       // boolean, currency status (tradeable and withdrawable)
        'fee':       0.123,      // withdrawal fee, flat
        'precision': 8,          // number of decimal digits "after the dot" (depends on exchange.precisionMode)
        'deposit':   true        // boolean, deposits are available
        'withdraw':  true        // boolean, withdraws are available
        'limits': {              // value limits when placing orders on this market
            'amount': {
                'min': 0.01,     // order amount should be > min
                'max': 1000,     // order amount should be < max
            },
            'withdraw': { ... }, // withdrawal limits
            'deposit': {...},
        },
        'networks': {...}        // network structures indexed by unified network identifiers (ERC20, TRC20, BSC, etc)
        'info': { ... },         // the original unparsed currency info from the exchange
    }"""

    id: str
    """String literal for referencing within an exchange"""
    code: str
    """Uppercase unified string literal code the currency"""
    name: str
    """String, human-readable name, if specified"""
    active: bool
    """Boolean, currency status (tradeable and withdrawable)"""
    fee: float
    """Withdrawal fee, flat"""
    precision: int
    """Number of decimal digits "after the dot" (depends on exchange.precisionMode)"""
    deposit: bool
    """Boolean, deposits are available"""
    withdraw: bool
    """Boolean, withdraws are available"""
    limits: CurrencyLimits
    """Value limits when placing orders on this market"""
    networks: dict[str, Any]
    """Network structures indexed by unified network identifiers (ERC20, TRC20, BSC, etc)"""
    info: dict[str, Any]
    """The original unparsed currency info from the exchange"""


@attrs.frozen()
class Network:
    """https://docs.ccxt.com/en/latest/manual.html#network-structure
    {
    'id':       'tron',         // string literal for referencing within an exchange
    'network':  'TRC20'         // unified network
    'name':     'Tron Network', // string, human-readable name, if specified
    'active':    true,          // boolean, currency status (tradeable and withdrawable)
    'fee':       0.123,         // withdrawal fee, flat
    'precision': 8,             // number of decimal digits "after the dot" (depends on exchange.precisionMode)
    'deposit':   true           // boolean, deposits are available
    'withdraw':  true           // boolean, withdraws are available
    'limits': {                 // value limits when placing orders on this market
        'amount': {
            'min': 0.01,        // order amount should be > min
            'max': 1000,        // order amount should be < max
        },
        'withdraw': { ... },    // withdrawal limits
        'deposit': {...},       // deposit limits
    },
    'info': { ... },            // the original unparsed currency info from the exchange
    }"""

    id: str
    """String literal for referencing within an exchange"""
    network: str
    """Unified network"""
    name: str
    """String, human-readable name, if specified"""
    active: bool
    """Boolean, currency status (tradeable and withdrawable)"""
    fee: float
    """Withdrawal fee, flat"""
    precision: int
    """Number of decimal digits "after the dot" (depends on exchange.precisionMode)"""
    deposit: bool
    """Boolean, deposits are available"""
    withdraw: bool
    """Boolean, withdraws are available"""
    limits: CurrencyLimits
    """Value limits when placing orders on this market"""
    info: dict[str, Any]
    """The original unparsed currency info from the exchange"""


@attrs.frozen()
class Precision:
    """https://docs.ccxt.com/en/latest/manual.html#market-structure"""

    price: int | float
    """Integer or float for TICK_SIZE roundingMode, might be missing if not supplied by the exchange"""
    amount: int
    """Might be missing if not supplied by the exchange"""
    cost: int
    """Very few exchanges actually have it"""


@attrs.frozen()
class Market:
    """https://docs.ccxt.com/en/latest/manual.html#market-structure
    {
    'id':      'btcusd',      // string literal for referencing within an exchange
    'symbol':  'BTC/USD',     // uppercase string literal of a pair of currencies
    'base':    'BTC',         // uppercase string, unified base currency code, 3 or more letters
    'quote':   'USD',         // uppercase string, unified quote currency code, 3 or more letters
    'baseId':  'btc',         // any string, exchange-specific base currency id
    'quoteId': 'usd',         // any string, exchange-specific quote currency id
    'active':   true,         // boolean, market status
    'type':    'spot',        // spot for spot, future for expiry futures, swap for perpetual swaps, 'option' for options
    'spot':     true,         // whether the market is a spot market
    'margin':   true,         // whether the market is a margin market
    'future':   false,        // whether the market is a expiring future
    'swap':     false,        // whether the market is a perpetual swap
    'option':   false,        // whether the market is an option contract
    'contract': false,        // whether the market is a future, a perpetual swap, or an option
    'settle':   'USDT',       // the unified currency code that the contract will settle in, only set if `contract` is true
    'settleId': 'usdt',       // the currencyId of that the contract will settle in, only set if `contract` is true
    'contractSize': 1,        // the size of one contract, only used if `contract` is true
    'linear':   true,         // the contract is a linear contract (settled in quote currency)
    'inverse':  false,        // the contract is an inverse contract (settled in base currency)
    'expiry':  1641370465121, // the unix expiry timestamp in milliseconds, undefined for everything except market['type'] `future`
    'expiryDatetime': '2022-03-26T00:00:00.000Z', // The datetime contract will in iso8601 format
    'strike': 4000,           // price at which a put or call option can be exercised
    'optionType': 'call',     // call or put string, call option represents an option with the right to buy and put an option with the right to sell
    'taker':    0.002,        // taker fee rate, 0.002 = 0.2%
    'maker':    0.0016,       // maker fee rate, 0.0016 = 0.16%
    'percentage': true,       // whether the taker and maker fee rate is a multiplier or a fixed flat amount
    'tierBased': false,       // whether the fee depends on your trading tier (your trading volume)
    'feeSide': 'get',         // string literal can be 'get', 'give', 'base', 'quote', 'other'
    'precision': {            // number of decimal digits "after the dot"
        'price': 8,           // integer or float for TICK_SIZE roundingMode, might be missing if not supplied by the exchange
        'amount': 8,          // integer, might be missing if not supplied by the exchange
        'cost': 8,            // integer, very few exchanges actually have it
    },
    'limits': {               // value limits when placing orders on this market
        'amount': {
            'min': 0.01,      // order amount should be > min
            'max': 1000,      // order amount should be < max
        },
        'price': { ... },     // same min/max limits for the price of the order
        'cost':  { ... },     // same limits for order cost = price * amount
        'leverage': { ... },  // same min/max limits for the leverage of the order
    },
    'info':      { ... },     // the original unparsed market info from the exchange
    }"""

    id: str
    """String literal for referencing within an exchange"""
    symbol: str
    """Uppercase string literal of a pair of currencies"""
    base: str
    """Uppercase string, unified base currency code, 3 or more letters"""
    quote: str
    """Uppercase string, unified quote currency code, 3 or more letters"""
    baseId: str
    """Any string, exchange-specific base currency id"""
    quoteId: str
    """Any string, exchange-specific quote currency id"""
    active: bool
    """Boolean, market status"""
    type: str
    """Spot for spot, future for expiry futures, swap for perpetual swaps, 'option' for options"""
    spot: bool
    """Whether the market is a spot market"""
    margin: bool
    """Whether the market is a margin market"""
    future: bool
    """Whether the market is a expiring future"""
    swap: bool
    """Whether the market is a perpetual swap"""
    option: bool
    """Whether the market is an option contract"""
    contract: bool
    """Whether the market is a future, a perpetual swap, or an option"""
    settle: str
    """The unified currency code that the contract will settle in, only set if `contract` is true"""
    settleId: str
    """The currencyId of that the contract will settle in, only set if `contract` is true"""
    contractSize: float
    """The size of one contract, only used if `contract` is true"""
    linear: bool
    """The contract is a linear contract (settled in quote currency)"""
    inverse: bool
    """The contract is an inverse contract (settled in base currency)"""
    expiry: int | None
    """The unix expiry timestamp in milliseconds, undefined for everything except market['type'] `future`"""
    expiryDatetime: str
    """The datetime contract will in iso8601 format"""
    strike: float
    """Price at which a put or call option can be exercised"""
    optionType: str
    """Call or put string, call option represents an option with the right to buy and put an option with the right to sell"""
    taker: float
    """Taker fee rate, 0.002 = 0.2%"""
    maker: float
    """Maker fee rate, 0.0016 = 0.16%"""
    percentage: bool
    """Whether the taker and maker fee rate is a multiplier or a fixed flat amount"""
    tierBased: bool
    """Whether the fee depends on your trading tier (your trading volume)"""
    feeSide: Literal["get", "give", "base", "quote", "other"]
    """String literal can be 'get', 'give', 'base', 'quote', 'other'"""
    precision: Precision
    """Number of decimal digits "after the dot" """
    limits: MarketLimits
    """Value limits when placing orders on this market"""
    info: dict[str, Any]
    """The original unparsed market info from the exchange"""


@attrs.frozen()
class OrderBook:
    """https://docs.ccxt.com/en/latest/manual.html#order-book-structure
      {
        'bids': [
            [ price, amount ], // [ float, float ]
            [ price, amount ],
            ...
        ],
        'asks': [
            [ price, amount ],
            [ price, amount ],
            ...
        ],
        'symbol': 'ETH/BTC', // a unified market symbol
        'timestamp': 1499280391811, // Unix Timestamp in milliseconds (seconds * 1000)
        'datetime': '2017-07-05T18:47:14.692Z', // ISO8601 datetime string with milliseconds
        'nonce': 1499280391811, // an increasing unique identifier of the orderbook snapshot
    }

      **The timestamp and datetime may be missing (``undefined/None/null``) if the exchange in question does not provide a corresponding value in the API response.**"""

    bids: list[tuple[float, float]]
    """List of (price, amount) tuples"""
    asks: list[tuple[float, float]]
    """List of (price, amount) tuples"""
    symbol: str
    """A unified market symbol"""
    timestamp: int
    """Unix Timestamp in milliseconds (seconds * 1000)"""
    datetime: str
    """ISO8601 datetime string with milliseconds"""
    nonce: int
    """An increasing unique identifier of the orderbook snapshot"""


@attrs.frozen()
class Ticker:
    """https://docs.ccxt.com/en/latest/manual.html#ticker-structure
    {
        'symbol':        string symbol of the market ('BTC/USD', 'ETH/BTC', ...)
        'info':        { the original non-modified unparsed reply from exchange API },
        'timestamp':     int (64-bit Unix Timestamp in milliseconds since Epoch 1 Jan 1970)
        'datetime':      ISO8601 datetime string with milliseconds
        'high':          float, // highest price
        'low':           float, // lowest price
        'bid':           float, // current best bid (buy) price
        'bidVolume':     float, // current best bid (buy) amount (may be missing or undefined)
        'ask':           float, // current best ask (sell) price
        'askVolume':     float, // current best ask (sell) amount (may be missing or undefined)
        'vwap':          float, // volume weighed average price
        'open':          float, // opening price
        'close':         float, // price of last trade (closing price for current period)
        'last':          float, // same as `close`, duplicated for convenience
        'previousClose': float, // closing price for the previous period
        'change':        float, // absolute change, `last - open`
        'percentage':    float, // relative change, `(change/open) * 100`
        'average':       float, // average price, `(last + open) / 2`
        'baseVolume':    float, // volume of base currency traded for last 24 hours
        'quoteVolume':   float, // volume of quote currency traded for last 24 hours
    }
    """

    symbol: str
    """Symbol of the market ('BTC/USD', 'ETH/BTC', ...)"""
    info: dict[str, Any]
    """The original non-modified unparsed reply from exchange API"""
    timestamp: int
    """64-bit Unix Timestamp in milliseconds since Epoch 1 Jan 1970"""
    datetime: str
    """ISO8601 datetime string with milliseconds"""
    high: float
    """Highest price"""
    low: float
    """Lowest price"""
    bid: float
    """Current best bid (buy) price"""
    bidVolume: float
    """Current best bid (buy) amount (may be missing or undefined)"""
    ask: float
    """Current best ask (sell) price"""
    askVolume: float
    """Current best ask (sell) amount (may be missing or undefined)"""
    vwap: float
    """Volume weighed average price"""
    open: float
    """Opening price"""
    close: float
    """Price of last trade (closing price for current period)"""
    last: float
    """Same as `close`, duplicated for convenience"""
    previousClose: float
    """Closing price for the previous period"""
    change: float
    """Absolute change, `last - open`"""
    percentage: float
    """Relative change, `(change/open) * 100`"""
    average: float
    """Average price, `(last + open) / 2`"""
    baseVolume: float
    """Volume of base currency traded for last 24 hours"""
    quoteVolume: float
    """Volume of quote currency traded for last 24 hours"""


Ohlcv = List[tuple[int, float, float, float, float, float]]
"""https://docs.ccxt.com/en/latest/manual.html#ohlcv-structure
List of tuples of (UTC timestamp in milliseconds, open, high, low, close, volume
(usually in terms of the base currency, the exchanges docstring may list whether quote or base units are used))"""


@attrs.frozen()
class PublicTrade:
    """[
    {
        'info':       { ... },                  // the original decoded JSON as is
        'id':        '12345-67890:09876/54321', // string trade id
        'timestamp':  1502962946216,            // Unix timestamp in milliseconds
        'datetime':  '2017-08-17 12:42:48.000', // ISO8601 datetime with milliseconds
        'symbol':    'ETH/BTC',                 // symbol
        'order':     '12345-67890:09876/54321', // string order id or undefined/None/null
        'type':      'limit',                   // order type, 'market', 'limit' or undefined/None/null
        'side':      'buy',                     // direction of the trade, 'buy' or 'sell'
        'price':      0.06917684,               // float price in quote currency
        'amount':     1.5,                      // amount of base currency
    },
    ...
    ]"""

    info: dict[str, Any]
    """The original decoded JSON as is"""
    id: str
    """String trade id"""
    timestamp: int
    """Unix timestamp in milliseconds"""
    datetime: str
    """ISO8601 datetime with milliseconds"""
    symbol: str
    """Symbol"""
    order: str | None
    """String order id or undefined/None/null"""
    type: str | None
    """Order type, 'market', 'limit' or undefined/None/null"""
    side: str
    """Direction of the trade, 'buy' or 'sell'"""
    price: float
    """Float price in quote currency"""
    amount: float
    """Amount of base currency"""


@attrs.frozen()
class Status:
    """https://docs.ccxt.com/en/latest/manual.html#exchange-status-structure
    {
    'status': 'ok', // 'ok', 'shutdown', 'error', 'maintenance'
    'updated': undefined, // integer, last updated timestamp in milliseconds if updated via the API
    'eta': undefined, // when the maintenance or outage is expected to end
    'url': undefined, // a link to a GitHub issue or to an exchange post on the subject
    }"""

    status: Literal["ok", "shutdown", "error", "maintenance"]
    """'ok', 'shutdown', 'error', 'maintenance'"""
    updated: int
    """Last updated timestamp in milliseconds if updated via the API"""
    eta: int
    """When the maintenance or outage is expected to end"""
    url: str
    """A link to a GitHub issue or to an exchange post on the subject"""


@attrs.frozen()
class BorrowRate:
    """https://docs.ccxt.com/en/latest/manual.html#borrow-rate-structure
        {
      currency: 'USDT',  // Unified currency code
      rate: 0.0006,  // A ratio of the rate that interest is accrued at
      period: 86400000,  // The amount of time in milliseconds that is required to accrue the interest amount specified by rate
      timestamp: 1646956800000,  // Timestamp for when the currency had this rate
      datetime: '2022-03-11T00:00:00.000Z',  // Datetime for when the currency had this rate
      info: [ ... ]
    }"""

    currency: str
    """Unified currency code"""
    rate: float
    """A ratio of the rate that interest is accrued at"""
    period: int
    """The amount of time in milliseconds that is required to accrue the interest amount specified by rate"""
    timestamp: int
    """Timestamp for when the currency had this rate"""
    datetime: str
    """Datetime for when the currency had this rate"""
    info: dict[str, Any]
    """The original decoded JSON as is"""


@attrs.frozen()
class LeverageTier:
    """[
        {
            "tier": 1,                       // tier index
            "notionalCurrency": "USDT",      // the currency that minNotional and maxNotional are in
            "minNotional": 0,                // the lowest amount of this tier // stake = 0.0
            "maxNotional": 10000,            // the highest amount of this tier // max stake amount at 75x leverage = 133.33333333333334
            "maintenanceMarginRate": 0.0065, // maintenance margin rate
            "maxLeverage": 75,               // max available leverage for this market when the value of the trade is > minNotional and < maxNotional
            "info": { ... }                  // Response from exchange
        },
        {
            "tier": 2,
            "notionalCurrency": "USDT",
            "minNotional": 10000,            // min stake amount at 50x leverage = 200.0
            "maxNotional": 50000,            // max stake amount at 50x leverage = 1000.0
            "maintenanceMarginRate": 0.01,
            "maxLeverage": 50,
            "info": { ... },
        },
        ...
        {
            "tier": 9,
            "notionalCurrency": "USDT",
            "minNotional": 20000000,
            "maxNotional": 50000000,
            "maintenanceMarginRate": 0.5,
            "maxLeverage": 1,
            "info": { ... },
        },
    ]"""

    tier: int
    """Tier index"""
    notionalCurrency: str
    """The currency that minNotional and maxNotional are in"""
    minNotional: float
    """The lowest amount of this tier"""
    maxNotional: float
    """The highest amount of this tier"""
    maintenanceMarginRate: float
    """Maintenance margin rate"""
    maxLeverage: float
    """Max available leverage for this market when the value of the trade is > minNotional and < maxNotional"""
    info: dict[str, Any]
    """The original decoded JSON as is"""


@attrs.frozen()
class FundingRate:
    """https://docs.ccxt.com/en/latest/manual.html#funding-rate-structure
        {
        info: { ... },
        symbol: 'BTC/USDT:USDT',
        markPrice: 39294.43,
        indexPrice: 39291.78,
        interestRate: 0.0003,
        estimatedSettlePrice: undefined,
        timestamp: undefined,
        datetime: undefined,
        fundingRate: 0.000072,
        fundingTimestamp: 1645833600000,
        fundingDatetime: '2022-02-26T00:00:00.000Z',
        nextFundingRate: -0.000018,
        nextFundingTimestamp: undefined,
        nextFundingDatetime: undefined,
        previousFundingRate: undefined,
        previousFundingTimestamp: undefined,
        previousFundingDatetime: undefined
    }"""

    info: dict[str, Any]
    """The original decoded JSON as is"""
    symbol: str
    """Symbol"""
    markPrice: float
    """Mark price"""
    indexPrice: float
    """Index price"""
    interestRate: float
    """Interest rate"""
    estimatedSettlePrice: float
    """Estimated settle price"""
    timestamp: int
    """Unix timestamp in milliseconds"""
    datetime: str
    """ISO8601 datetime with milliseconds"""
    fundingRate: float
    """Funding rate"""
    fundingTimestamp: int
    """Funding unix timestamp in milliseconds"""
    fundingDatetime: str
    """Funding ISO8601 datetime with milliseconds"""
    nextFundingRate: float
    """Next funding rate"""
    nextFundingTimestamp: int
    """Next funding unix timestamp in milliseconds"""
    nextFundingDatetime: str
    """Next funding ISO8601 datetime with milliseconds"""
    previousFundingRate: float
    """Previous funding rate"""
    previousFundingTimestamp: int
    """Previous funding unix timestamp in milliseconds"""
    previousFundingDatetime: str
    """Previous funding ISO8601 datetime with milliseconds"""


@attrs.frozen()
class FundingRateHistory:
    """
    {
        info: { ... },
        symbol: "BTC/USDT:USDT",
        fundingRate: -0.000068,
        timestamp: 1642953600000,
        datetime: "2022-01-23T16:00:00.000Z"
    }
    """

    info: dict[str, Any]
    """The original decoded JSON as is"""
    symbol: str
    """Symbol"""
    fundingRate: float
    """Funding rate"""
    timestamp: int
    """Unix timestamp in milliseconds"""
    datetime: str
    """ISO8601 datetime with milliseconds"""


@attrs.frozen()
class OpenInterest:
    """https://docs.ccxt.com/en/latest/manual.html#open-interest-structure
        {
        symbol: 'BTC/USDT',
        baseVolume: 80872.801, // deprecated
        quoteVolume: 3508262107.38, // deprecated
        openInterestAmount: 80872.801,
        openInterestValue: 3508262107.38,
        timestamp: 1649379000000,
        datetime: '2022-04-08T00:50:00.000Z',
        info: {
            symbol: 'BTCUSDT',
            sumOpenInterest: '80872.80100000',
            sumOpenInterestValue: '3508262107.38000000',
            timestamp: '1649379000000'
        }
    }"""

    symbol: str
    """Symbol"""
    baseVolume: float
    """Deprecated"""
    quoteVolume: float
    """Deprecated"""
    openInterestAmount: float
    """Open interest amount"""
    openInterestValue: float
    """Open interest value"""
    timestamp: int
    """Unix timestamp in milliseconds"""
    datetime: str
    """ISO8601 datetime with milliseconds"""
    info: dict[str, Any]
    """The original decoded JSON as is"""


@attrs.frozen()
class PositionsRisk:
    """https://docs.ccxt.com/en/latest/manual.html#positions-risk-structure
        {
        info: { ... },
        symbol: 'CTSI/USDT',
        contracts: 0,
        contractSize: 1,
        unrealizedPnl: 0,
        leverage: 20,
        liquidationPrice: 0.7313,
        collateral: 0,
        notional: 0,
        markPrice: 0.7724,
        entryPrice: 0,
        timestamp: 1647420354000,
        initialMargin: 0,
        initialMarginPercentage: 0.05,
        maintenanceMargin: 0,
        maintenanceMarginPercentage: 0.01,
        marginRatio: 0.4881,
        datetime: "2022-03-16T08:45:54.000Z",
        marginMode: 'cross',
        side: "long",
        hedged: false,
        percentage: 78
    }"""

    info: dict[str, Any]
    """The original decoded JSON as is"""
    symbol: str
    """Symbol"""
    contracts: float
    """Contracts"""
    contractSize: float
    """Contract size"""
    unrealizedPnl: float
    """Unrealized PNL"""
    leverage: float
    """Leverage"""
    liquidationPrice: float
    """Liquidation price"""
    collateral: float
    """Collateral"""
    notional: float
    """Notional"""
    markPrice: float
    """Mark price"""
    entryPrice: float
    """Entry price"""
    timestamp: int
    """Unix timestamp in milliseconds"""
    initialMargin: float
    """Initial margin"""
    initialMarginPercentage: float
    """Initial margin percentage"""
    maintenanceMargin: float
    """Maintenance margin"""
    maintenanceMarginPercentage: float
    """Maintenance margin percentage"""
    marginRatio: float
    """Margin ratio"""
    datetime: str
    """ISO8601 datetime with milliseconds"""
    marginMode: str
    """Margin mode"""
    side: str
    """Side"""
    hedged: bool
    """Hedged"""
    percentage: float
    """Percentage"""


# Private API
@attrs.frozen()
class Account:
    """https://docs.ccxt.com/en/latest/manual.html#accounts-structure
    [
        {
            id: "s32kj302lasli3930",
            type: "main",
            name: "main",
            code: "USDT",
            info: { ... }
        },
        {
            id: "20f0sdlri34lf90",
            name: "customAccount",
            type: "margin",
            code: "USDT",
            info: { ... }
        },
        {
            id: "4oidfk40dadeg4328",
            type: "spot",
            name: "spotAccount32",
            code: "BTC",
            info: { ... }
        },
        ...
    ]"""

    id: str
    """Account ID"""
    type: str
    """Account type"""
    name: str
    """Account name"""
    code: str
    """Account code"""
    info: dict[str, Any]
    """The original decoded JSON as is"""


@attrs.frozen()
class Balance:
    free: float
    used: float
    total: float


@attrs.frozen()
class Balances(Dict[str, Balance]):
    """https://docs.ccxt.com/en/latest/manual.html#balances-structure
    {
        'info':  { ... },    // the original untouched non-parsed reply with details
        'timestamp': 1499280391811, // Unix Timestamp in milliseconds (seconds * 1000)
        'datetime': '2017-07-05T18:47:14.692Z', // ISO8601 datetime string with milliseconds

        //-------------------------------------------------------------------------
        // indexed by availability of funds first, then by currency

        'free':  {           // money, available for trading, by currency
            'BTC': 321.00,   // floats...
            'USD': 123.00,
            ...
        },

        'used':  { ... },    // money on hold, locked, frozen, or pending, by currency

        'total': { ... },    // total (free + used), by currency

        //-------------------------------------------------------------------------
        // indexed by currency first, then by availability of funds

        'BTC':   {           // string, three-letter currency code, uppercase
            'free': 321.00   // float, money available for trading
            'used': 234.00,  // float, money on hold, locked, frozen or pending
            'total': 555.00, // float, total balance (free + used)
        },

        'USD':   {           // ...
            'free': 123.00   // ...
            'used': 456.00,
            'total': 579.00,
        },

        ...
    }"""

    info: dict[str, Any]
    """The original decoded JSON as is"""
    timestamp: int
    """Unix timestamp in milliseconds"""
    datetime: str
    """ISO8601 datetime with milliseconds"""
    free: dict[str, float]
    """Money, available for trading, by currency"""
    used: dict[str, float]
    """Money on hold, locked, frozen, or pending, by currency"""
    total: dict[str, float]
    """Total (free + used), by currency"""


class TimeInForce(StrEnum):
    GTC = "GTC"
    IOC = "IOC"
    FOK = "FOK"
    PO = "PO"


@attrs.frozen
class PrivateTrade:
    """https://docs.ccxt.com/en/latest/manual.html#accounts-structure
    {
          'info':         { ... },                    // the original decoded JSON as is
          'id':           '12345-67890:09876/54321',  // string trade id
          'timestamp':    1502962946216,              // Unix timestamp in milliseconds
          'datetime':     '2017-08-17 12:42:48.000',  // ISO8601 datetime with milliseconds
          'symbol':       'ETH/BTC',                  // symbol
          'order':        '12345-67890:09876/54321',  // string order id or undefined/None/null
          'type':         'limit',                    // order type, 'market', 'limit' or undefined/None/null
          'side':         'buy',                      // direction of the trade, 'buy' or 'sell'
          'takerOrMaker': 'taker',                    // string, 'taker' or 'maker'
          'price':        0.06917684,                 // float price in quote currency
          'amount':       1.5,                        // amount of base currency
          'cost':         0.10376526,                 // total cost, `price * amount`,
          'fee':          {                           // provided by exchange or calculated by ccxt
              'cost':  0.0015,                        // float
              'currency': 'ETH',                      // usually base currency for buys, quote currency for sells
              'rate': 0.002,                          // the fee rate (if available)
          },
      }


    * The work on ``'fee'`` info is still in progress, fee info may be missing partially or entirely, depending on the exchange capabilities.
    * The ``fee`` currency may be different from both traded currencies (for example, an ETH/BTC order with fees in USD).
    * The ``cost`` of the trade means ``amount * price``. It is the total *quote* volume of the trade (whereas ``amount`` is the *base* volume). The cost field itself is there mostly for convenience and can be deduced from other fields.
    * The ``cost`` of the trade is a *"gross"* value. That is the value pre-fee, and the fee has to be applied afterwards."""

    info: dict[str, Any]
    """The original decoded JSON as is"""
    id: str
    """String trade id"""
    timestamp: int
    """Unix timestamp in milliseconds"""
    datetime: str
    """ISO8601 datetime with milliseconds"""
    symbol: str
    """Symbol"""
    order: str | None
    """String order id or undefined/None/null"""
    type: str | None
    """Order type, 'market', 'limit' or undefined/None/null"""
    side: str
    """Direction of the trade, 'buy' or 'sell'"""
    takerOrMaker: str | None
    """String, 'taker' or 'maker'"""
    price: float
    """Float price in quote currency"""
    amount: float
    """Amount of base currency"""
    cost: float
    """Total cost, `price * amount`"""
    fee: Fee | None
    """Provided by exchange or calculated by ccxt"""


@attrs.frozen()
class Order:
    """https://docs.ccxt.com/en/latest/manual.html#order-structure
          {
          'id':                '12345-67890:09876/54321', // string
          'clientOrderId':     'abcdef-ghijklmnop-qrstuvwxyz', // a user-defined clientOrderId, if any
          'datetime':          '2017-08-17 12:42:48.000', // ISO8601 datetime of 'timestamp' with milliseconds
          'timestamp':          1502962946216, // order placing/opening Unix timestamp in milliseconds
          'lastTradeTimestamp': 1502962956216, // Unix timestamp of the most recent trade on this order
          'status':      'open',        // 'open', 'closed', 'canceled', 'expired', 'rejected'
          'symbol':      'ETH/BTC',     // symbol
          'type':        'limit',       // 'market', 'limit'
          'timeInForce': 'GTC',         // 'GTC', 'IOC', 'FOK', 'PO'
          'side':        'buy',         // 'buy', 'sell'
          'price':        0.06917684,   // float price in quote currency (may be empty for market orders)
          'average':      0.06917684,   // float average filling price
          'amount':       1.5,          // ordered amount of base currency
          'filled':       1.1,          // filled amount of base currency
          'remaining':    0.4,          // remaining amount to fill
          'cost':         0.076094524,  // 'filled' * 'price' (filling price used where available)
          'trades':     [ ... ],        // a list of order trades/executions
          'fee': {                      // fee info, if available
              'currency': 'BTC',        // which currency the fee is (usually quote)
              'cost': 0.0009,           // the fee amount in that currency
              'rate': 0.002,            // the fee rate (if available)
          },
          'info': { ... },              // the original unparsed order structure as is
      }


    * The ``status`` of an order is usually either ``'open'`` (not filled or partially filled), ``'closed'`` (fully filled), or ``'canceled'`` (unfilled and canceled, or partially filled then canceled).
    * Some exchanges allow the user to specify an expiration timestamp upon placing a new order. If the order is not filled by that time, its ``status`` becomes ``'expired'``.
    * Use the ``filled`` value to determine if the order is filled, partially filled or fully filled, and by how much.
    * The work on ``'fee'`` info is still in progress, fee info may be missing partially or entirely, depending on the exchange capabilities.
    * The ``fee`` currency may be different from both traded currencies (for example, an ETH/BTC order with fees in USD).
    * The ``lastTradeTimestamp`` timestamp may have no value and may be ``undefined/None/null`` where not supported by the exchange or in case of an open order (an order that has not been filled nor partially filled yet).
    * The ``lastTradeTimestamp`` , if any, designates the timestamp of the last trade, in case the order is filled fully or partially, otherwise ``lastTradeTimestamp`` is ``undefined/None/null``.
    * Order ``status`` prevails or has precedence over the ``lastTradeTimestamp``.
    * The ``cost`` of an order is: ``{ filled * price }``
    * The ``cost`` of an order means the total *quote* volume of the order (whereas the ``amount``
    is the *base* volume). The value of ``cost`` should be as close to the actual most recent known
    order cost as possible. The ``cost`` field itself is there mostly for convenience and can be deduced from other fields.
    * The ``clientOrderId`` field can be set upon placing orders by the user with :ref:`custom order
    params <custom order params>`. Using the ``clientOrderId`` the user can later distinguish between
    own orders. This is only available for the exchanges that do support ``clientOrderId`` at this time."""

    id: str
    """A string-based order ID"""
    clientOrderId: str | None
    """A user-defined clientOrderId, if any"""
    datetime: str
    """ISO8601 datetime of 'timestamp' with milliseconds"""
    timestamp: int
    """Order placing/opening Unix timestamp in milliseconds"""
    lastTradeTimestamp: int | None
    """Unix timestamp of the most recent trade on this order"""
    status: Literal["open", "closed", "canceled", "expired", "rejected"]
    """'open', 'closed', 'canceled', 'expired', 'rejected'"""
    symbol: str
    """Symbol"""
    type: str
    """'market', 'limit'"""
    timeInForce: TimeInForce
    """'GTC', 'IOC', 'FOK', 'PO'"""
    side: str
    """'buy', 'sell'"""
    price: float | None
    """Float price in quote currency (may be empty for market orders)"""
    average: float | None
    """Float average filling price"""
    amount: float
    """Ordered amount of base currency"""
    filled: float
    """Filled amount of base currency"""
    remaining: float
    """Remaining amount to fill"""
    cost: float | None
    """'filled' * 'price' (filling price used where available)"""
    trades: list[PrivateTrade] | None
    """A list of order trades/executions"""
    fee: Fee | None
    """Fee info, if available"""
    info: dict[str, Any]
    """The original decoded JSON as is"""


@attrs.frozen()
class MarketPrecision:
    amount: float
    price: float


class LedgerEntry:
    """https://docs.ccxt.com/en/latest/manual.html#accounts-structure
    {
        'id': 'hqfl-f125f9l2c9',                // string id of the ledger entry, e.g. an order id
        'direction': 'out',                     // or 'in'
        'account': '06d4ab58-dfcd-468a',        // string id of the account if any
        'referenceId': 'bf7a-d4441fb3fd31',     // string id of the trade, transaction, etc...
        'referenceAccount': '3146-4286-bb71',   // string id of the opposite account (if any)
        'type': 'trade',                        // string, reference type, see below
        'currency': 'BTC',                      // string, unified currency code, 'ETH', 'USDT'...
        'amount': 123.45,                       // absolute number, float (does not include the fee)
        'timestamp': 1544582941735,             // milliseconds since epoch time in UTC
        'datetime': "2018-12-12T02:49:01.735Z", // string of timestamp, ISO8601
        'before': 0,                            // amount of currency on balance before
        'after': 0,                             // amount of currency on balance after
        'status': 'ok',                         // 'ok, 'pending', 'canceled'
        'fee': {                                // object or or undefined
            'cost': 54.321,                     // absolute number on top of the amount
            'currency': 'ETH',                  // string, unified currency code, 'ETH', 'USDT'...
        },
        'info': { ... },                        // raw ledger entry as is from the exchange
    }"""

    info: dict[str, Any]
    """Raw ledger entry as is from the exchange"""
    id: str
    """String id of the ledger entry, e.g. an order id"""
    direction: Literal["out", "in"]
    """Or 'in'"""
    account: str | None
    """String id of the account if any"""
    referenceId: str | None
    """String id of the trade, transaction, etc..."""
    referenceAccount: str | None
    """String id of the opposite account (if any)"""
    type: str | None
    """String, reference type, see below"""
    currency: str
    """String, unified currency code, 'ETH', 'USDT'..."""
    amount: float
    """Absolute number, float (does not include the fee)"""
    timestamp: int
    """Milliseconds since epoch time in UTC"""
    datetime: str
    """String of timestamp, ISO8601"""
    before: float
    """Amount of currency on balance before"""
    after: float
    """Amount of currency on balance after"""
    status: Literal["ok", "pending", "canceled"] | None
    """'ok, 'pending', 'canceled'"""
    fee: Fee | None
    """Object or or undefined"""


@attrs.frozen()
class Transaction:
    """https://docs.ccxt.com/en/latest/manual.html#transaction-structure
    {
        'info':      { ... },    // the JSON response from the exchange as is
        'id':       '123456',    // exchange-specific transaction id, string
        'txid':     '0x68bfb29821c50ca35ef3762f887fd3211e4405aba1a94e448a4f218b850358f0',
        'timestamp': 1534081184515,             // timestamp in milliseconds
        'datetime': '2018-08-12T13:39:44.515Z', // ISO8601 string of the timestamp
        'addressFrom': '0x38b1F8644ED1Dbd5DcAedb3610301Bf5fa640D6f', // sender
        'address':  '0x02b0a9b7b4cDe774af0f8e47cb4f1c2ccdEa0806', // "from" or "to"
        'addressTo': '0x304C68D441EF7EB0E2c056E836E8293BD28F8129', // receiver
        'tagFrom', '0xabcdef', // "tag" or "memo" or "payment_id" associated with the sender
        'tag':      '0xabcdef' // "tag" or "memo" or "payment_id" associated with the address
        'tagTo': '0xhijgklmn', // "tag" or "memo" or "payment_id" associated with the receiver
        'type':     'deposit',   // or 'withdrawal', string
        'amount':    1.2345,     // float (does not include the fee)
        'currency': 'ETH',       // a common unified currency code, string
        'status':   'pending',   // 'ok', 'failed', 'canceled', string
        'updated':   undefined,  // UTC timestamp of most recent status change in ms
        'comment':  'a comment or message defined by the user if any',
        'fee': {                 // the entire fee structure may be undefined
            'currency': 'ETH',   // a unified fee currency code
            'cost': 0.1234,      // float
            'rate': undefined,   // approximately, fee['cost'] / amount, float
        },
    }"""

    info: dict[str, Any]
    """The JSON response from the exchange as is"""
    id: str
    """Exchange-specific transaction id, string"""
    txid: str | None
    """0x68bfb29821c50ca35ef3762f887fd3211e4405aba1a94e448a4f218b850358f0"""
    timestamp: int | None
    """Timestamp in milliseconds"""
    datetime: str | None
    """ISO8601 string of the timestamp"""
    addressFrom: str | None
    """Sender"""
    address: Literal["from", "to"]
    '''"from" or "to"'''
    addressTo: str | None
    """Receiver"""
    tagFrom: str | None
    """"tag" or "memo" or "payment_id" associated with the sender"""
    tag: str | None
    """"tag" or "memo" or "payment_id" associated with the address"""
    tagTo: str | None
    """"tag" or "memo" or "payment_id" associated with the receiver"""
    type: Literal["deposit", "withdrawal"] | None
    """Or 'withdrawal', string"""
    amount: float | None
    """Float (does not include the fee)"""
    currency: str | None
    """A common unified currency code, string"""
    status: Literal["ok", "failed", "canceled"] | None
    """String"""
    updated: int | None
    """UTC timestamp of most recent status change in ms"""
    comment: str | None
    """A comment or message defined by the user if any"""
    fee: Fee | None
    """The entire fee structure may be undefined"""


@attrs.frozen()
class Deposit:
    """https://docs.ccxt.com/en/latest/manual.html
    {
        'currency': currency, // currency code
        'network': network,   // a list of deposit/withdraw networks, ERC20, TRC20, BSC20 (see below)
        'address': address,   // address in terms of requested currency
        'tag': tag,           // tag / memo / paymentId for particular currencies (XRP, XMR, ...)
        'info': response,     // raw unparsed data as returned from the exchange
    }"""

    currency: str
    """Currency code"""
    network: str | None
    """A list of deposit/withdraw networks, ERC20, TRC20, BSC20 (see below)"""
    address: str | None
    """Address in terms of requested currency"""
    tag: str | None
    """Tag / memo / paymentId for particular currencies (XRP, XMR, ...)"""
    info: dict[str, Any]
    """Raw unparsed data as returned from the exchange"""


@attrs.frozen()
class Transfer:
    """https://docs.ccxt.com/en/latest/manual.html#transfer-structure
    {
        info: { ... },
        id: "93920432048",
        timestamp: 1646764072000,
        datetime: "2022-03-08T18:27:52.000Z",
        currency: "USDT",
        amount: 11.31,
        fromAccount: "spot",
        toAccount: "future",
        status: "ok"
    }"""

    info: dict[str, Any]
    """Raw unparsed data as returned from the exchange"""
    id: str
    """Exchange-specific transaction id, string"""
    timestamp: int
    """Timestamp in milliseconds"""
    datetime: str
    """ISO8601 string of the timestamp"""
    currency: str
    """A common unified currency code, string"""
    amount: float
    """Float (does not include the fee)"""
    fromAccount: str
    """A unified account name, string"""
    toAccount: str
    """A unified account name, string"""
    status: Literal["ok", "failed"]
    """'ok', 'failed'"""


@attrs.frozen()
class TradingFee:
    """
    {
        'ETH/BTC': {
            'maker': 0.001,
            'taker': 0.002,
            'info': { ... },
            'symbol': 'ETH/BTC',
        },
        'LTC/BTC': {
            'maker': 0.001,
            'taker': 0.002,
            'info': { ... },
            'symbol': 'LTC/BTC',
            },
    }
    """

    maker: float
    """The maker fee rate, 0.05% = 0.0005, 1% = 0.01, ..."""
    taker: float
    """The taker fee rate, 0.05% = 0.0005, 1% = 0.01, ..."""
    info: dict[str, Any]
    """Raw unparsed data as returned from the exchange"""
    symbol: str
    """A unified symbol, string"""


@attrs.frozen()
class TransactionFees:
    """
    {
        'withdraw': {
            'BTC': 0.00001,
            'ETH': 0.001,
            'LTC': 0.0003,
        },
        'deposit': {
            'BTC': 0,
        },
        'info': { ... },
    }
    """

    withdraw: dict[str, float]
    """The withdraw fee rates, 0.05% = 0.0005, 1% = 0.01, ..."""
    deposit: dict[str, float]
    """The deposit fee rates, 0.05% = 0.0005, 1% = 0.01, ..."""
    info: dict[str, Any]
    """Raw unparsed data as returned from the exchange"""


@attrs.frozen()
class BorrowInterest:
    """
    {
        account: 'BTC/USDT',                    // The market that the interest was accrued in
        currency: 'USDT',                       // The currency of the interest
        interest: 0.00004842,                   // The amount of interest that was charged
        interestRate: 0.0002,                   // The borrow interest rate
        amountBorrowed: 5.81,                   // The amount of currency that was borrowed
        timestamp: 1648699200000,               // The timestamp that the interest was charged
        datetime: '2022-03-31T04:00:00.000Z',   // The datetime that the interest was charged
        info: { ... }                           // Unparsed exchange response
    }
    """

    account: str
    """The market that the interest was accrued in"""
    currency: str
    """The currency of the interest"""
    interest: float
    """The amount of interest that was charged"""
    interestRate: float
    """The borrow interest rate"""
    amountBorrowed: float
    """The amount of currency that was borrowed"""
    timestamp: int
    """The timestamp that the interest was charged"""
    datetime: str
    """The datetime that the interest was charged"""
    info: dict[str, Any]
    """Unparsed exchange response"""


@attrs.frozen()
class MarginLoan:
    """
    {
        id: '1234323',                          // integer, the transaction id
        currency: 'USDT',                       // string, the currency that is borrowed or repaid
        amount: 5.81,                           // float, the amount of currency that was borrowed or repaid
        symbol: 'BTC/USDT:USDT',                // string, unified market symbol
        timestamp: 1648699200000,               // integer, the timestamp of when the transaction was made
        datetime: '2022-03-31T04:00:00.000Z',   // string, the datetime of when the transaction was made
        info: { ... }                           // Unparsed exchange response
    }
    """

    id: str
    """The transaction id"""
    currency: str
    """The currency that is borrowed or repaid"""
    amount: float
    """The amount of currency that was borrowed or repaid"""
    symbol: str
    """Unified market symbol"""
    timestamp: int
    """The timestamp of when the transaction was made"""
    datetime: str
    """The datetime of when the transaction was made"""
    info: dict[str, Any]
    """Unparsed exchange response"""


@attrs.frozen()
class Margin:
    """
    {
        info: { ... },
        type: 'add', // 'add', 'reduce', 'set'
        amount: 1, // amount added, reduced, or set
        total: 2,  // total margin or undefined if not specified by the exchange
        code: 'USDT',
        symbol: 'XRP/USDT:USDT',
        status: 'ok'
    }
    """

    info: dict[str, Any]
    """Raw unparsed data as returned from the exchange"""
    type: Literal["add", "reduce", "set"]
    """'add', 'reduce', 'set'"""
    amount: float
    """Amount added, reduced, or set"""
    total: float | None
    """Total margin or undefined if not specified by the exchange"""
    code: str
    """A common unified currency code, string"""
    symbol: str
    """A unified symbol, string"""
    status: Literal["ok", "failed"]
    """'ok', 'failed'"""


@attrs.frozen()
class FundingHistory:
    """
    {
        info: { ... },
        symbol: "XRP/USDT:USDT",
        code: "USDT",
        timestamp: 1646954920000,
        datetime: "2022-03-08T16:00:00.000Z",
        id: "1520286109858180",
        amount: -0.027722
    }
    """

    info: dict[str, Any]
    """Raw unparsed data as returned from the exchange"""
    symbol: str
    """A unified symbol, string"""
    code: str
    """A common unified currency code, string"""
    timestamp: int
    """The timestamp of when the funding was made"""
    datetime: str
    """The datetime of when the funding was made"""
    id: str
    """A unique id for the funding"""
    amount: float
    """The amount of the funding"""


@attrs.frozen()
class Position:
    """
    {
       'info': { ... },             // json response returned from the exchange as is
       'id': '1234323',             // string, position id to reference the position, similar to an order id
       'symbol': 'BTC/USD',         // uppercase string literal of a pair of currencies
       'timestamp': 1607723554607,  // integer unix time since 1st Jan 1970 in milliseconds
       'datetime': '2020-12-11T21:52:34.607Z',  // ISO8601 representation of the unix time above
       'isolated': true,            // boolean, whether or not the position is isolated, as opposed to cross where margin is added automatically
       'hedged': false,             // boolean, whether or not the position is hedged, i.e. if trading in the opposite direction will close this position or make a new one
       'side': 'long',              // string, long or short
       'contracts': 5,              // float, number of contracts bought, aka the amount or size of the position
       'contractSize': 100,         // float, the size of one contract in quote units
       'entryPrice': 20000,         // float, the average entry price of the position
       'markPrice': 20050,          // float, a price that is used for funding calculations
       'notional': 100000,          // float, the value of the position in the settlement currency
       'leverage': 100,             // float, the leverage of the position, related to how many contracts you can buy with a given amount of collateral
       'collateral': 5300,          // float, the maximum amount of collateral that can be lost, affected by pnl
       'initialMargin': 5000,       // float, the amount of collateral that is locked up in this position
       'maintenanceMargin': 1000,   // float, the minimum amount of collateral needed to avoid being liquidated
       'initialMarginPercentage': 0.05,      // float, the initialMargin as a percentage of the notional
       'maintenanceMarginPercentage': 0.01,  // float, the maintenanceMargin as a percentage of the notional
       'unrealizedPnl': 300,        // float, the difference between the market price and the entry price times the number of contracts, can be negative
       'liquidationPrice': 19850,   // float, the price at which collateral becomes less than maintenanceMargin
       'marginMode': 'cross',       // string, can be cross or isolated
       'percentage': 3.32,          // float, represents unrealizedPnl / initialMargin * 100
    }
    """

    info: dict[str, Any]
    """Raw unparsed data as returned from the exchange"""
    id: str
    """A unique id for the position"""
    symbol: str
    """A unified symbol, string"""
    timestamp: int
    """The timestamp of when the position was opened"""
    datetime: str
    """The datetime of when the position was opened"""
    isolated: bool
    """Whether or not the position is isolated"""
    hedged: bool
    """Whether or not the position is hedged"""
    side: Literal["long", "short"]
    """The side of the position, 'long' or 'short'"""
    contracts: float
    """The number of contracts bought"""
    contractSize: float
    """The size of one contract in quote units"""
    entryPrice: float
    """The average entry price of the position"""
    markPrice: float
    """A price that is used for funding calculations"""
    notional: float
    """The value of the position in the settlement currency"""
    leverage: float
    """The leverage of the position"""
    collateral: float
    """The maximum amount of collateral that can be lost, affected by pnl"""
    initialMargin: float
    """The amount of collateral that is locked up in this position"""
    maintenanceMargin: float
    """The minimum amount of collateral needed to avoid being liquidated"""
    initialMarginPercentage: float
    """The initialMargin as a percentage of the notional"""
    maintenanceMarginPercentage: float
    """The maintenanceMargin as a percentage of the notional"""
    unrealizedPnl: float
    """The difference between the market price and the entry price times the number of contracts, can be negative"""
    liquidationPrice: float
    """The price at which collateral becomes less than maintenanceMargin"""
    marginMode: Literal["cross", "isolated"]
    """The margin mode, 'cross' or 'isolated'"""
    percentage: float
    """The unrealizedPnl as a percentage of the initialMargin"""
