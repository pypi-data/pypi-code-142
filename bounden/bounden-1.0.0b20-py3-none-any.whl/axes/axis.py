from abc import ABC, abstractmethod
from typing import Generic

from bounden.axes.axis_operation import AxisOperation
from bounden.axes.types import ValueT


class Axis(ABC, Generic[ValueT]):
    """
    Axis.
    """

    def add(self, a: float | int | ValueT, b: float | int | ValueT) -> ValueT:
        """
        Returns the axis' result of `a` + `b`.
        """

        return self.operate(a, b, AxisOperation.Add)

    def operate(
        self,
        a: float | int | ValueT,
        b: float | int | ValueT,
        op: AxisOperation,
    ) -> ValueT:
        """
        Returns the axis' result of operation `op` on `a` and `b`.
        """

        a = a if isinstance(a, (float, int)) else self.to_decimal(a)
        b = b if isinstance(b, (float, int)) else self.to_decimal(b)

        match op:
            case AxisOperation.Add:
                result = a + b

            case AxisOperation.Subtract:
                result = a - b

            case _:
                raise ValueError(f"Unrecognised AxisOperation {op}")

        return self.to_value(result)

    @abstractmethod
    def to_decimal(self, axis: ValueT) -> float | int:
        """
        Gets the decimal value of axis value `axis`.
        """

    @abstractmethod
    def to_value(self, decimal: float | int) -> ValueT:
        """
        Gets the axis value of decimal value `decimal`.
        """
