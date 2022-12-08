from dataclasses import dataclass


@dataclass
class TextSpan:
    start: int
    end: int
    kind: str
    text: str

    @property
    def length(self) -> int:
        return self.end - self.start

    def __lt__(self, other: "TextSpan") -> bool:
        return self.start < other.start or (
            self.start == other.start and self.end < other.end
        )
