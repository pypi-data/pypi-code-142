from __future__ import annotations

from math import sqrt
from typing import Optional

T_RGB = tuple[int, int, int]

def closest_rgb(
    color: T_RGB,
    palette: Iterable[T_RGB]
) -> T_RGB:
    """
    Given an RGB color, this function returns the
    closest color from an iterable.
    
    Parameters
    ----------
    color
        The color to compare each entry of ``palette``
        with.
    
    palette
        An iterable of RGB colors.
    
    Raises
    ------
    RuntimeError
        ``palette`` does not contain any entries.
    
    Returns
    -------
    The color from ``palette`` that matched ``color``
    the best.
    """
    min_distance: Optional[tuple[int, T_RGB]] = None
    for i in palette:
        if i == color:
            return i
        
        distance = sqrt(
            (color[0] - i[0]) ** 2 +
            (color[1] - i[1]) ** 2 +
            (color[2] - i[2]) ** 2
        )
        
        if min_distance is None or distance < min_distance[0]:
            min_distance = (distance, i)
    
    if min_distance is None:
        raise RuntimeError("palette does not contain any entries")
    
    return min_distance[1]
