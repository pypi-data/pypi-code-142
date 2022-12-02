from typing import Union, Type

from pandas import DataFrame

from .core import Base


class Candle(Base):
    """
    A class representing rates from the charts as Japanese Candlesticks.
    Subclass this class to add needed properties.
    Attributes:
        Index (int): Position of the candle in the chart. Zero represents the most recent
        time (int): Period start time.
        open (int): Open price
        high (float): The highest price of the period
        low (float): The lowest price of the period
        close (float): Close price
        tick_volume (float): Tick volume
        real_volume (float): Trade volume
        spread (float): Spread
        ema (float, optional): ema
    """
    Index: int
    time: int
    open: float
    high: float
    low: float
    close: float
    tick_volume: float
    real_volume: float
    spread: float
    ema: float

    def __lt__(self, other: 'Candle'):
        return self.Index < other.Index

    # def __hash__(self):
    #     return hash(self.time)

    @property
    def mid(self) -> float:
        """
        The mid of open and close
        Returns: mid

        """
        return (self.open + self.close) / 2

    def is_bullish(self) -> bool:
        """
        Returns: True or Fasle

        """
        return self.close > self.open

    def is_bearish(self) -> bool:
        """

        Returns: True or False

        """
        return self.open > self.close

    def is_hanging_man(self, ratio=1.5):
        return max((self.open - self.low), (self.high - self.close)) / (self.close - self.open) >= ratio

    def is_bullish_hammer(self, ratio=1.5):
        return max((self.close - self.low), (self.high - self.open)) / (self.open - self.close) >= ratio


class Candles:
    """
    A class representing a collection of rates as Candle Objects, Arranged chronologically.
    Class is an iterable container

    Args:
        data (DataFrame, tuple[tuple]): A pandas dataframe or a tuple of tuple as returned from the terminal

    Keyword Args:
        candle (Type(Candle)): Type of Candle object represented by the class.
        flip (bool): If flip is True reverse data argument.

    Attributes:
        _data: Dataframe Object holding the rates
        Candle: Candle class for individual objects
    """
    def __init__(self, *, data: DataFrame | tuple[tuple], candle: Type[Candle] = Candle, flip=True):
        data = DataFrame(data) if not isinstance(data, DataFrame) else data
        self._data = data.iloc[::-1] if flip else data
        self.Candle = candle

    def __len__(self):
        return self._data.shape[0]

    def __contains__(self, item: Candle):
        return item.time == self[item.Index].time

    def __getitem__(self, index) -> Union[type(Candle), "Candles"]:
        if isinstance(index, slice):
            cls = self.__class__
            data = self._data.iloc[index]
            return cls(data=data, candle=self.Candle, flip=False)

        item = self._data.iloc[index]
        return self.Candle(Index=index, **item)

    def __iter__(self):
        return (self.Candle(**row._asdict()) for row in self._data.itertuples())

    @property
    def data(self):
        return self._data
