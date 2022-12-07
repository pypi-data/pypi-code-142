from typing import List
from numpy import ndarray


class BaseEncoder(object):
    """
    传入FaissIndex的encoder模型基类
    """
    def encode(self, items: List[str], verbose: int = 1) -> ndarray:
        raise NotImplemented
