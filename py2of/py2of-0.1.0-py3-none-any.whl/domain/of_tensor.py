from dataclasses import dataclass


@dataclass()
class OfTensor:
    xx: float
    xy: float
    xz: float
    yx: float
    yy: float
    yz: float
    zx: float
    zy: float
    zz: float

    def __str__(self) -> str:
        return f"""\
(
    {self.xx} {self.xy} {self.xz}
    {self.yx} {self.yy} {self.yz}
    {self.zx} {self.zy} {self.zz}
)\
"""
