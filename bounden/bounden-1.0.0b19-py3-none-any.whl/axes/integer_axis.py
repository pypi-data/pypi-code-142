from bounden.axes.axis import Axis


class IntegerAxis(Axis[int]):
    """
    Axis of integer values.
    """

    def to_decimal(self, axis: int) -> float | int:
        """
        Gets the decimal value of axis value `axis`.
        """

        return axis

    def to_value(self, decimal: float | int) -> int:
        """
        Gets the axis value of decimal value `decimal`.
        """

        return int(decimal)
