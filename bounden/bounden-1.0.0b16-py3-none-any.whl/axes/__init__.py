from bounden.axes.axis import Axis
from bounden.axes.axis_operation import AxisOperation
from bounden.axes.integer_axis import IntegerAxis
from bounden.axes.library import get_axis, register_axis
from bounden.axes.no_axis_for_type import NoAxisForType
from bounden.axes.string_axis import StringAxis
from bounden.axes.types import AxesT, XAxisT, YAxisT

register_axis(int, IntegerAxis())
register_axis(str, StringAxis())

__all__ = [
    "AxesT",
    "Axis",
    "AxisOperation",
    "IntegerAxis",
    "NoAxisForType",
    "StringAxis",
    "XAxisT",
    "YAxisT",
    "get_axis",
    "register_axis",
]
