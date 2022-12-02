from datetime import datetime

from pandas import DataFrame

from .core.meta_trader import MetaTrader
from .core.constants import TimeFrame, CopyTicks
from .core.models import SymbolInfo
from .ticks import Tick

from .terminal import terminal


class Symbol(SymbolInfo):
    """
    Helper class with general properties and methods of a financial instrument.
    You can inherit from this class and add your own properties and methods.
    This class subclass of SymbolInfo which contains all symbol properties.
    All methods of this class accept keyword only arguments.

    Keyword Args:
        mt5: Platform, defaults to the MetaTrader5 class.

    Attributes:
        tick (Tick): Price tick object for instrument

    Notes:
        Full properties are on the SymbolInfo Object.
        Make sure Symbol is always initialized with a name argument
    """
    tick: Tick

    def __init__(self, *, mt5=MetaTrader(), **kwargs):
        self.mt5 = mt5

        if "name" not in kwargs:
            raise TypeError("Symbol must be initialized with a name attribute")

        self.name = kwargs['name']
        del kwargs['name']
        super().__init__(**kwargs)

    def __repr__(self):
        return f"{self.name}"

    def __eq__(self, other: "Symbol"):
        return self.name == other.name

    def __lt__(self, other: "Symbol"):
        return self.name > other.name

    def __hash__(self):
        return hash(self.name)

    async def info_tick(self, *, name: str = "") -> Tick:
        """
        Get Price Tick of the financial instrument

        Args:
            name: if name is supplied get price tick of that financial instrument

        Returns:
            Tick: Returns a Custom Tick Object
        """
        _name = name if name else self.name
        tick = await self.mt5.symbol_info_tick(_name)
        tick = Tick(**tick._asdict())
        setattr(self, 'tick', tick) if _name == self.name else ...
        return tick

    async def symbol_select(self, *, enable: bool = True) -> bool:
        """
        Select a symbol in the MarketWatch window or remove a symbol from the window.
        Update the select property

        Args:
            enable (bool): Switch. Optional unnamed parameter. If 'false', a symbol should be removed from the MarketWatch window.
                Otherwise, it should be selected in the MarketWatch window. A symbol cannot be removed if open charts with this symbol are currently
                present or positions are opened on it.

        Returns:
            bool: True if successful, otherwise – False.
        """
        self.select = await self.mt5.symbol_select(self.name, enable)
        return self.select

    async def info(self) -> SymbolInfo | None:
        """
        Get data on the specified financial instrument and update the symbol object properties

        Returns:
            bool: True if successful else False
        """
        info = await self.mt5.symbol_info(self.name)
        if not info:
            return None
        self.set_attributes(**info._asdict())
        return SymbolInfo(**info._asdict())

    async def init(self) -> bool:
        """
        Initialized the symbol by pulling properties from the terminal

        Returns:
             bool: Returns True if symbol info was successful initialized
        """
        await self.symbol_select()
        if self.select:
            await self.info()
            return self.select
        return self.select

    async def copy_rates_from(self, *, timeframe: TimeFrame, date_from: datetime | int, count: int) -> DataFrame | None:
        """
        Get bars from the MetaTrader 5 terminal starting from the specified date.

        Args:
            timeframe (TimeFrame): Timeframe the bars are requested for. Set by a value from the TimeFrame enumeration. Required unnamed parameter.

            date_from (datetime | int): Date of opening of the first bar from the requested sample. Set by the 'datetime' object or as a number
                of seconds elapsed since 1970.01.01. Required unnamed parameter.

            count (int): Number of bars to receive. Required unnamed parameter.

        Returns:
            DateFrame: Rates as pandas DataFrame object
            None: Return None if there is an error
        """
        rates = await self.mt5.copy_rates_from(self.name, timeframe, date_from, count)
        return DataFrame(rates) if rates is not None else None

    async def copy_rates_from_pos(self, *, timeframe: TimeFrame, count: int = 500, start_position: int = 0) -> DataFrame:
        """
        Get bars from the MetaTrader 5 terminal starting from the specified index.

        Args:
            timeframe (TimeFrame): TimeFrame value from TimeFrame Enum. Required keyword only parameter

            count (int): Number of bars to return. Keyword argument defaults to 500

            start_position (int): Initial index of the bar the data are requested from. The numbering of bars goes from present to past.
                Thus, the zero bar means the current one. Keyword argument defaults to 0.

        Returns:
             DataFrame: Returns a Pandas DataFrame object of bars
             None: Return None if there is an error
        """
        rates = await self.mt5.copy_rates_from_pos(self.name, timeframe, start_position, count)
        return DataFrame(rates) if rates is not None else None

    async def copy_ticks_from(self, *, date_from: datetime | int, count: int = 100, flags: CopyTicks = CopyTicks.INFO) -> DataFrame:
        """
        Get ticks from the MetaTrader 5 terminal starting from the specified date.

        Args:
            date_from (datetime | int): Date the ticks are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.

            count (int): Number of requested ticks. Defaults to 100

            flags (CopyTicks): A flag to define the type of the requested ticks from CopyTicks enum. INFO is the default

        Returns:
             DataFrame: Returns a Pandas DataFrame object of ticks
             None: Return None if there is an error

        """
        ticks = await self.mt5.copy_ticks_from(self.name, date_from, count, flags)
        return DataFrame(ticks) if ticks is not None else None

    async def copy_rates_range(self, *, timeframe: TimeFrame, date_from: datetime | int, date_to: datetime | int) -> DataFrame | None:
        """
        Get bars in the specified date range from the MetaTrader 5 terminal.

        Args:
            timeframe (TimeFrame): Timeframe the bars are requested for. Set by a value from the TimeFrame enumeration. Required unnamed parameter.

            date_from (datetime | int): Date the bars are requested from. Set by the 'datetime' object or as a number of seconds
                elapsed since 1970.01.01. Bars with the open time >= date_from are returned. Required unnamed parameter.

            date_to (datetime | int): Date, up to which the bars are requested. Set by the 'datetime' object or as a number of
                seconds elapsed since 1970.01.01. Bars with the open time <= date_to are returned. Required unnamed parameter.

        Returns:
            DataFrame: Rates as pandas DataFrame object
            None: Return None if there is an error
        """
        rates = await self.mt5.copy_rates_range(symbol=self.name, timeframe=timeframe, date_from=date_from, date_to=date_to)
        return DataFrame(rates) if rates is not None else None

    async def copy_ticks_range(self, *, date_from: datetime | int, date_to: datetime | int, flags: CopyTicks = CopyTicks.INFO):
        """
        Get ticks for the specified date range from the MetaTrader 5 terminal.
        Args:
            date_from: Date the bars are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Bars with
                the open time >= date_from are returned. Required unnamed parameter.

            date_to: Date, up to which the bars are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Bars
                with the open time <= date_to are returned. Required unnamed parameter.

            flags (CopyTicks):

        Returns:
            DataFrame: Rates as pandas DataFrame object
            None: Return None if there is an error
        """
        ticks = await self.mt5.copy_ticks_range(self.name, date_from, date_to, flags)
        return DataFrame(ticks) if ticks is not None else None
