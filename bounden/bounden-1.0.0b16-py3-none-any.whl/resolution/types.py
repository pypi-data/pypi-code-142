from typing import Callable

from bounden.axes import AxesT
from bounden.resolved import ResolvedPoint, ResolvedVolume

GetResolvedPoint = Callable[[], ResolvedPoint[AxesT]]
"""
Function that returns a resolved point.
"""

GetResolvedVolume = Callable[[], ResolvedVolume]
"""
Function that returns a resolved volume.
"""
