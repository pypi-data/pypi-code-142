import dataclasses
import typing

import numpy as np
import numpy.typing as npt


@dataclasses.dataclass(kw_only=True)
class Model:
    p0: typing.Optional[npt.ArrayLike] = None
    bounds: tuple[npt.ArrayLike, npt.ArrayLike] = (-np.inf, np.inf)

    @classmethod
    @property
    def name(cls) -> str:
        return cls.__name__

    @staticmethod
    def forward(t: float | np.ndarray, *popt: float) -> float | np.ndarray:
        return t

    def prepare(self, x: np.ndarray, y: np.ndarray) -> None:
        pass
