import dataclasses
import typing

import numpy as np
import numpy.typing as npt


@dataclasses.dataclass(kw_only=True)
class Model:
    p0: typing.Optional[npt.ArrayLike] = None
    sigma: typing.Optional[npt.ArrayLike] = None
    bounds: tuple[npt.ArrayLike, npt.ArrayLike] = (-np.inf, np.inf)

    @classmethod
    @property
    def name(cls) -> str:
        return cls.__name__

    @staticmethod
    def cdf(t: float | np.ndarray, *popt: float) -> float | np.ndarray:
        raise NotImplementedError()

    @staticmethod
    def pdf(t: float | np.ndarray, *popt: float) -> float | np.ndarray:
        raise NotImplementedError()

    @classmethod
    def forward(
        cls, t: float | np.ndarray, *popt: float, func: str = "cdf"
    ) -> float | np.ndarray:
        if func == "cdf":
            return cls.cdf(t, *popt)
        elif func == "pdf":
            return cls.pdf(t, *popt)
        else:
            raise NotImplementedError()

    def prepare(self, x: np.ndarray, y: np.ndarray) -> None:
        pass
