from bounden import FloatAxis, ResolvedPoint, ResolvedVolume

from palign.types import ResolvedRegion


class ResolvedImageRegion(ResolvedRegion):
    """
    Resolved image region.
    """

    @property
    def size(self) -> tuple[int, int]:
        """
        The image's width and height.
        """

        return (int(self.width), int(self.height))


def make_image_region(width: int, height: int) -> ResolvedImageRegion:
    """
    Gets a resolved region that describes an image's dimensions.
    """

    axes = (FloatAxis(), FloatAxis())
    point = ResolvedPoint[tuple[float, float]](axes, (0, 0))
    volume = ResolvedVolume(width, height)
    return ResolvedImageRegion(axes, point, volume)
