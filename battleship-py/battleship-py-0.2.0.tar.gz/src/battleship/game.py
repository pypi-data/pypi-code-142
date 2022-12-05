#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from enum import Enum
from random import randrange
from typing import Iterable, NamedTuple, Tuple


class Square(Enum):
    WATER = 1
    DEBRIS = 2
    BATTLESHIP = 3
    DESTROYER = 4

    TEXT = dict(
        WATER="water", DEBRIS="debris", BATTLESHIP="battleship", DESTROYER="destroyer"
    )

    EMOJI = dict(WATER="🌊", DEBRIS="🪵", BATTLESHIP="🚢", DESTROYER="⛵")

    def __repr__(self) -> str:
        return self.__class__.TEXT.value.get(self.name, "Unknown")

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def emoji(self):
        return self.__class__.EMOJI.value.get(self.name, "?")


class ShipSize(Enum):
    BATTLESHIP = 5
    DESTROYER = 4


class Result(Enum):
    MISS = 1
    SHOT = 2
    SINK = 3

    TEXT = dict(MISS="missed", SHOT="shot", SINK="sank")

    def __repr__(self) -> str:
        return self.__class__.TEXT.value.get(self.name, "Unknown")

    def __str__(self) -> str:
        return self.__repr__()


class Direction(Enum):
    VERTICAL = 1
    HORIZONTAL = 2


EMPTY = (Square.WATER, Square.DEBRIS)

SHIPS = (Square.BATTLESHIP, Square.DESTROYER)


class Position(NamedTuple):
    kind: Square = Square.WATER
    vessel_id: int = -1


class Battleship:
    def __init__(self, size: Tuple[int, int] = (10, 10), allocate: bool = True) -> None:
        self.width, self.height = size
        self.grid: list[list[Position]] = [
            [Position() for value in range(self.width)] for value in range(self.height)
        ]
        self.vessel_id: int = 0
        self.pending: dict[int, int] = dict()
        if allocate:
            self.allocate()

    def __repr__(self) -> str:
        return self.repr(emoji=False)

    def __str__(self) -> str:
        return self.__repr__()

    def allocate(
        self,
        ships: Iterable[Square] = (
            Square.BATTLESHIP,
            Square.DESTROYER,
            Square.DESTROYER,
        ),
    ):
        for ship in ships:
            x0, y0 = -1, -1

            size = ShipSize[ship.name].value

            while True:
                direction = (
                    Direction.VERTICAL
                    if bool(randrange(0, 2))
                    else Direction.HORIZONTAL
                )

                if direction == direction.VERTICAL:
                    x0 = randrange(0, self.width)
                    y0 = randrange(0, self.height - size + 1)

                elif direction == direction.HORIZONTAL:
                    x0 = randrange(0, self.width - size + 1)
                    y0 = randrange(0, self.height)

                vessel_id = self.fill(x0, y0, size, direction, value=ship)
                if vessel_id:
                    self.pending[vessel_id] = size
                    break

    def fill(
        self,
        x0: int,
        y0: int,
        size: int,
        direction: Direction,
        value: Square = Square.WATER,
    ) -> int:
        x, y = x0, y0

        for _index in range(size):
            if not self.grid[y][x].kind in EMPTY:
                return 0
            if direction == direction.VERTICAL:
                y += 1
            elif direction == direction.HORIZONTAL:
                x += 1

        self.vessel_id += 1

        x, y = x0, y0

        for _index in range(size):
            self.grid[y][x] = Position(value, self.vessel_id)
            if direction == direction.VERTICAL:
                y += 1
            elif direction == direction.HORIZONTAL:
                x += 1

        return self.vessel_id

    def shoot(self, coordinate: str) -> Tuple[Result, Position]:
        try:
            if not len(coordinate) in (2, 3):
                raise Exception(f"Invalid length {len(coordinate)}")

            x = ord(coordinate[0]) - 65
            y = int(coordinate[1:]) - 1

            return self._shoot(x, y)
        except:
            raise Exception(f"Invalid coordinate '{coordinate}'")

    def destroy(self):
        for y in range(self.height):
            for x in range(self.width):
                self._shoot(x, y)

    def repr(self, emoji: bool = False, axis: bool = True) -> str:
        buffer = []
        if axis:
            buffer.append("   ")
            buffer.append(
                (" " if emoji else "").join(
                    chr(index + 65) for index in range(self.width)
                )
            )
            buffer.append("\n")
        for y in range(self.height):
            if axis:
                buffer.append(f"{str(y + 1).rjust(2, ' ')} ")
            for x in range(self.width):
                position = self.grid[y][x]
                value = position.kind.emoji if emoji else position.kind.value
                buffer.append(f"{value}")
            buffer.append("\n")
        return "".join(buffer).rstrip()

    def _shoot(self, x: int, y: int) -> Tuple[Result, Position]:
        result = Result.MISS

        position = self.grid[y][x]

        if position.kind in SHIPS:
            self.grid[y][x] = Position(Square.DEBRIS, position.vessel_id)
            self.pending[position.vessel_id] -= 1
            if self.pending[position.vessel_id] == 0:
                result = Result.SINK
            else:
                result = Result.SHOT

        return (result, position)

    @property
    def finished(self):
        return self.all_pending == 0

    @property
    def all_pending(self):
        return sum(value for value in self.pending.values())


class Runnable:
    def run(self):
        raise NotImplemented("Running logic is not implemented")
