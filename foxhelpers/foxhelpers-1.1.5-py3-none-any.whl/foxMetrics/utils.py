import typing as t
from abc import ABCMeta
from collections import OrderedDict

import pandas as pd


def OrderedDict2DataFrame(dictionary: t.Dict[int, t.Dict]) -> pd.DataFrame:
    try:
        validated_table = pd.DataFrame(dictionary).T
    except ValueError:
        validated_table = pd.DataFrame(dictionary, index=[""]).T
    return validated_table


class HistoricalContainer(metaclass=ABCMeta):
    """
    Aggregate historical information in a ordered dict.
    """

    def __init__(self) -> None:
        self._record_dict: "OrderedDict" = OrderedDict()
        self._current_epoch = 0

    @property
    def record_dict(self) -> OrderedDict:
        return self._record_dict

    def __getitem__(self, index):
        return self._record_dict[index]

    @property
    def current_epoch(self) -> int:
        return self._current_epoch

    def summary(self) -> pd.DataFrame:
        return OrderedDict2DataFrame(self._record_dict)

    def add(self, input_dict, epoch=None) -> None:
        if epoch:
            self._current_epoch = epoch
        self._record_dict[self._current_epoch] = input_dict
        self._current_epoch += 1

    def reset(self) -> None:
        self._record_dict = OrderedDict()
        self._current_epoch = 0

    def state_dict(self) -> t.Dict[str, t.Any]:
        return self.__dict__

    def load_state_dict(self, state_dict: t.Dict[str, t.Any]) -> None:
        self.__dict__.update(state_dict)

    def __repr__(self):
        return str(self.summary())


def rename_df_columns(dataframe: pd.DataFrame, name: str, sep="_"):
    dataframe.columns = list(map(lambda x: name + sep + x, dataframe.columns))
    return dataframe


def flatten_dict(d: t.MutableMapping[str, t.Any], parent_key: str = "", sep: str = "."):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + str(k) if parent_key else str(k)
        if isinstance(v, t.MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
