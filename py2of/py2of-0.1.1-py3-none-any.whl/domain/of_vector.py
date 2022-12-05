from dataclasses import dataclass


@dataclass()
class OfVector:
    x: float
    y: float
    z: float

    def __str__(self) -> str:
        return f"({self.x} {self.y} {self.z})"
