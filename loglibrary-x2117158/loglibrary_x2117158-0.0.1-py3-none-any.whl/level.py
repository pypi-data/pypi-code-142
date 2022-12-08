from __future__ import annotations


class Level:
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value

    def __eq__(self, o: object) -> bool:
        return o is Level and self.value == o.value

    def __lt__(self, o: Level):
        return self.value < o.value

    def __le__(self, o: Level):
        return self.value <= o.value

    def __gt__(self, o: Level):
        return self.value > o.value

    def __ge__(self, o: Level):
        return self.value >= o.value

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return self.name


Level.ALL = Level('ALL', 0)
Level.OFF = Level('OFF', 2000)
Level.FINEST = Level('FINEST', 300)
Level.FINER = Level('FINER', 400)
Level.FINE = Level('FINE', 500)
Level.CONFIG = Level('CONFIG', 700)
Level.INFO = Level('INFO', 800)
Level.WARNING = Level('WARNING', 900)
Level.SEVERE = Level('SEVERE', 1000)
Level.SHOUT = Level('SHOUT', 1200)
Level.LEVELS = [
    Level.ALL,
    Level.FINEST,
    Level.FINER,
    Level.FINE,
    Level.CONFIG,
    Level.INFO,
    Level.WARNING,
    Level.SEVERE,
    Level.SHOUT,
    Level.OFF
]
