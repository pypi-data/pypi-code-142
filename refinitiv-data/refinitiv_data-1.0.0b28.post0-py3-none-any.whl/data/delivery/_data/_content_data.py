from typing import Any, Callable, Dict, TYPE_CHECKING

from ._endpoint_data import EndpointData

if TYPE_CHECKING:
    import pandas as pd


class Data(EndpointData):
    def __init__(
        self,
        raw: Any,
        dataframe: "pd.DataFrame" = None,
        dfbuilder: Callable[[Any, Dict[str, Any]], "pd.DataFrame"] = None,
        **kwargs,
    ):
        EndpointData.__init__(self, raw, **kwargs)
        self._dataframe = dataframe
        self._dfbuilder = dfbuilder

    @property
    def df(self):
        if self._dataframe is None and self._dfbuilder:
            self._dataframe = self._dfbuilder(self.raw, **self._kwargs)

        return self._dataframe


class UniverseData(Data):
    def __init__(self, raw, *args, **kwargs) -> None:
        super().__init__(raw=raw, *args, **kwargs)

    @property
    def df(self):
        return super().df
