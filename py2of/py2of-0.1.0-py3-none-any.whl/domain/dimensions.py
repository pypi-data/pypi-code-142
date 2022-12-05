from dataclasses import dataclass


@dataclass()
class Dimensions:
    kg: int = 0
    m: int = 0
    s: int = 0
    K: int = 0
    mol: int = 0
    A: int = 0
    cd: int = 0

    def __str__(self) -> str:
        string = f"[{self.kg} {self.m} {self.s} {self.K} {self.mol} {self.A} {self.cd}]"
        return string
