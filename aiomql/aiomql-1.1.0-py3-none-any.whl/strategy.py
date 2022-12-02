import asyncio
import time
from dataclasses import dataclass
from typing import Literal, Type
from abc import ABC, abstractmethod

import pandas_ta as ta
from pandas import DataFrame

from .core.constants import TimeFrame, OrderType
from .candle import Candles, Candle
from .symbol import Symbol


@dataclass
class Entry:
    """
    A helper class for capturing entry positions.

    Attributes:
        time (float): Time of the bar

        trend (str): The trend of the chart. Can be either of "notrend", "uptrend", "downtrend".

        new (bool): Shows if an entry position has been seen before.

        type (OrderType): OrderType for placing trade order

        points (float): points to trade.
    """
    time: float = 0
    trend: Literal["notrend", "uptrend", "downtrend"] = "notrend"
    current: float = 0
    new: bool = True
    type: OrderType | None = None
    points: float = 0


class Strategy(ABC):
    """
    The base class for creating strategies.

    Keyword Args:
        symbol (Symbol): The Financial Instrument as a Symbol Object
        **kwargs: Optional Keyword Arguments

    Attributes:
        Candle (Type[Candle]): Can be a subclass of the Candle class specific to the strategy and analysis carried out on it.

        Candles (Type[Candles]): Candles class for the strategy can be the same or a subclass of the "candle.Candles" class.

        name (str): A name for the strategy. You can initialize a new name for the strategy that will replace the one defined as class parameter
    """
    Candle: Type[Candle] = Candle
    Candles: Type[Candles] = Candles
    name:  str = ""

    def __init__(self, *, symbol: type(Symbol), **kwargs):
        self.symbol = symbol
        self.name = kwargs.get('name') or self.name

    def __repr__(self):
        return f"{self.name}({self.symbol!r})"

    async def get_ema(self, *, time_frame: TimeFrame, period: int, count: int = 500) -> type(Candles):
        """
        Helper method that gets the ema of the bars.

        Keyword Args:
            time_frame (TimeFrame): Timeframe of the bars returned

            period (int): Period of the ema

            count (int): Number of objects to be returned

        Returns: A Candles Object
        """
        data: DataFrame = await self.symbol.copy_rates_from_pos(timeframe=time_frame, count=count)
        await asyncio.to_thread(data.ta.ema, length=period, append=True)
        data.rename(columns={f"EMA_{period}": 'ema'}, inplace=True)
        return self.Candles(data=data, candle=self.Candle)

    @staticmethod
    async def sleep(secs: float):
        """
        Sleep for the needed amount of seconds between requests to the terminal
        Args:
            secs (float): The time period of the requests, eg. when trading on the 5 minute time frame the value will be 300 secs

        Returns: None.

        """
        await asyncio.sleep(secs - (time.time() % secs) + 1)

    @abstractmethod
    async def trade(self):
        """
        Place trades using this method
        Returns:

        """
