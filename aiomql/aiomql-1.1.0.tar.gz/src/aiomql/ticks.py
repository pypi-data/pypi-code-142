from typing import Union

from pandas import DataFrame

from .core import Base
from .core.constants import TickFlag


class Tick(Base):
    """
    Price Tick of Financial Instrument

    """
    time: int
    bid: float
    ask: float
    last: float
    volume: float
    time_msc: int
    flags: TickFlag
    volume_real: float
    Index: int = 0


class Ticks:
    """
    Container data class for price ticks. Arrange in chronological order.
    Supports iteration, slicing and assignment

    Args:
        data (DataFrame | tuple[tuple]): Dataframe of price ticks or a tuple of tuples

    Keyword Args:
        flip (bool): If flip is True reverse data argument.

    Attributes:
        _data: Dataframe Object holding the ticks
    """
    def __init__(self, *, data: DataFrame | tuple[tuple], flip=True):
        data = DataFrame(data) if not isinstance(data, DataFrame) else data
        self._data = data.iloc[::-1] if flip else data

    def __len__(self):
        return self._data.shape[0]

    def __contains__(self, item: Tick):
        return item.time == self[item.Index].time

    def __getitem__(self, index) -> Union[Tick, "Ticks"]:
        if isinstance(index, slice):
            cls = self.__class__
            data = self._data.iloc[index]
            return cls(data=data, flip=False)

        item = self._data.iloc[index]
        return Tick(Index=index, **item)

    def __iter__(self):
        return (Tick(**row._asdict()) for row in self._data.itertuples())

    @property
    def data(self):
        return self._data
