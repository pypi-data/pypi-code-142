from bounden.axes.axis import Axis


class FloatAxis(Axis[float]):
    """
    Axis of float values.
    """

    def to_decimal(self, axis: float) -> float | int:
        """
        Gets the decimal value of axis value `axis`.
        """

        return axis

    def to_value(self, decimal: float | int) -> float:
        """
        Gets the axis value of decimal value `decimal`.
        """

        return float(decimal)
