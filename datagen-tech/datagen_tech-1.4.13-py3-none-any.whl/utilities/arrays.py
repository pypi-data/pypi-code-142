from typing import TypeVar, Union

import numpy as np

from datagen.api.assets import ComputationalAsset

CA = TypeVar("CA", bound=Union[ComputationalAsset, np.ndarray])


def normalize(vector: np.ndarray) -> np.ndarray:
    return vector / np.linalg.norm(vector)


def to_ndarrays(*computationals: CA):
    ndarrays = []
    for c in computationals:
        if isinstance(c, ComputationalAsset):
            ndarrays.append(c.to_ndarray())
        elif isinstance(c, np.ndarray):
            ndarrays.append(c)
        else:
            raise ValueError()
    return ndarrays
