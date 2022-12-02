from abc import ABC

from .core.meta_trader import MetaTrader
from .core.models import BookInfo
from .symbol import Symbol


class Market(ABC):
    """
    An abstract base class for handling a market properties and functions
    Args:
        mt5 (MetaTrader): The Meta trader object for connecting to the terminal. Default Keyword Argument

    Attributes:
        instruments (Set[str]): A set of financial instruments available in a Market eg Forex Market

        symbols (Set[Symbol]): A set of symbols that will be made available for the current trading session.

        name (str): A name for the market

        symbol (Symbol): The Symbol subclass for instruments in this market

    """
    instruments = set()
    name: str = "Market"
    symbol: type(Symbol) = Symbol
    symbols: set[type(Symbol)] = set()

    def __init__(self, *, mt5=MetaTrader()):
        self.mt5 = mt5

    def select_all(self):
        """
        Make all financial instruments in market available for trading
        Returns:
        """
        self.symbols = {self.symbol(name=symbol) for symbol in self.instruments}

    def add(self, *, symbol: type(Symbol)):
        """
        Add symbol object directly to the set of symbols for the trading session

        Args:
            symbol: Symbol Object
        """
        self.instruments.add(symbol.name)
        self.symbols.add(symbol)

    def select(self, *symbols, check: (bool) = True):
        """
        Add financial instruments to the set of trading symbols for the session.

        Args:
            *symbols (Iterable[str]): symbol(s) to be added to the set of trading symbols. i.e you can add a single symbol or multiple symbols at once

        Keyword Args:
            check (bool): if check is true makes sure the symbol is in the list of predefined financial instruments for the market
        Returns:

        """
        syms = self.instruments.intersection(symbols) if check else symbols
        symbols = {self.symbol(name=symbol) for symbol in syms}
        self.symbols.update(symbols)
        return symbols

    async def book_add(self, symbol: str) -> bool:
        """
        Subscribes the MetaTrader 5 terminal to the Market Depth change events for a specified symbol.
        If the symbol is not in the list of instruments for the market, This method will return False
        Args:
            symbol (str): financial instrument name

        Returns: True if successful, otherwise – False.

        """
        return await self.mt5.market_book_add(symbol) if symbol in self.instruments else False

    async def book_get(self, *, symbol: str, check: bool = True) -> BookInfo:
        """
        Returns a tuple from BookInfo featuring Market Depth entries for the specified symbol.

        Keyword Args:
            symbol (str): financial instrument name
            check (bool): check if symbol is in the set of financial instruments

        Returns (BookInfo | None): Returns the Market Depth content as a BookInfo Object else None

        Raises:
            ValueError: Raises ValueError if symbol is not in the list of instruments for the market.

        """
        if symbol not in self.instruments:
            raise ValueError(f"{symbol} not in available for this market")
        info = await self.mt5.market_book_get(symbol)
        return BookInfo(**info._asdict())

    async def book_release(self, symbol: str) -> bool:
        """
        Cancels subscription of the MetaTrader 5 terminal to the Market Depth change events for a specified symbol.
        Args:
            symbol: financial instrument name

        Returns:
            bool: True if successful, otherwise – False.

        """
        return await self.mt5.market_book_release(symbol)

    async def init_symbols(self):
        """
        Initialize all symbols in the market for the current session
        Returns:
        """
        rem = set()
        for symbol in self.symbols:
            init = await symbol.init()
            await self.book_add(symbol.name)
            rem.add(symbol) if not init else ...
        self.symbols.difference_update(rem)
