import abc
from typing import List, Optional

import torch


class GeneralFunctionShapeInfo:
    ...


# this class is duplicated in rust_circuit.pyi due to unfortunate details of
# how python type stubs work
# so changes here should be replicated there etc
class GeneralFunctionSpecBase(metaclass=abc.ABCMeta):
    """
    Inherit from this base class in order to implement an arbitrary new GeneralFunctionSpec.

    See docs for `get_shape_info`, GeneralFunctionShapeInfo, and `function`.
    """

    @abc.abstractproperty
    def name(self) -> str:
        raise NotImplementedError

    def compute_hash_bytes(self) -> bytes:
        """the default implementation should typically be overridden!"""
        return id(self).to_bytes(8, "big", signed=True)

    @abc.abstractmethod
    def function(self, *tensors: torch.Tensor) -> torch.Tensor:
        """run the actual function on tensors - these tensors shapes correspond to the shapes in ``get_shape_info``"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_shape_info(self, *shapes: List[int]) -> GeneralFunctionShapeInfo:
        """This should error (exception) if the shapes are invalid and otherwise return GeneralFunctionShapeInfo"""
        raise NotImplementedError

    def serialize(self) -> Optional[str]:
        """Used in printing. TODO: write spec"""
        return None
