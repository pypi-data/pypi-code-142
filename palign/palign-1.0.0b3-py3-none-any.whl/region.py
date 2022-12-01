from bounden import IntegerCoordinate, Percent, Point2, Region2

Point = Point2[IntegerCoordinate, IntegerCoordinate]


class Region(Region2[IntegerCoordinate, IntegerCoordinate]):
    """
    Pillow image region.
    """

    @classmethod
    def image(cls, width: int, height: int) -> "Region":
        return Region.new(
            IntegerCoordinate(0),
            IntegerCoordinate(0),
            width,
            height,
        )

    def ppoint(self, x: int, y: int) -> Point:
        return self.point2(IntegerCoordinate(x), IntegerCoordinate(y))

    def pregion(
        self,
        x: int,
        y: int,
        width: int | Percent,
        height: int,
    ) -> "Region":
        return Region.new(
            IntegerCoordinate(x),
            IntegerCoordinate(y),
            width,
            height,
            parent=self,
        )

    @property
    def size(self) -> tuple[int, int]:
        return int(self.width), int(self.height)
