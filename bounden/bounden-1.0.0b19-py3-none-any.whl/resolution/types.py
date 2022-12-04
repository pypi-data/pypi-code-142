from typing import Callable

from bounden.protocols import ResolvedPointProtocol, ResolvedVolumeProtocol

GetResolvedPoint = Callable[[], ResolvedPointProtocol]
"""
Function that returns a resolved point.
"""

GetResolvedVolume = Callable[[], ResolvedVolumeProtocol]
"""
Function that returns a resolved volume.
"""
