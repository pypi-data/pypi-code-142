#!/usr/bin/python
# -*- coding: utf-8 -*-

from enum import Enum
from random import randrange
from typing import Iterable, Tuple


class Square(Enum):
    WATER = 1
    DEBRIS = 2
    BATTLESHIP = 3
    DESTROYER = 4

    def __repr__(self) -> str:
        if self == Square.WATER:
            return "Water"
        elif self == Square.DEBRIS:
            return "Debris"
        elif self == Square.BATTLESHIP:
            return "Battleship"
        elif self == Square.DESTROYER:
            return "Destroyer"
        return "Invalid"

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def emoji(self):
        if self == Square.WATER:
            return "🌊"
        elif self == Square.DEBRIS:
            return "🌊"
        elif self == Square.BATTLESHIP:
            return "🚢"
        elif self == Square.DESTROYER:
            return "🚢"


class ShipSize(Enum):
    BATTLESHIP = 5
    DESTROYER = 4


class Direction(Enum):
    VERTICAL = 1
    HORIZONTAL = 2


EMPTY = (Square.WATER, Square.DEBRIS)

SHIPS = (Square.BATTLESHIP, Square.DESTROYER)


class Battleship:
    def __init__(self, size: Tuple[int, int] = (10, 10), allocate: bool = True) -> None:
        self.width, self.height = size
        self.grid = [
            [Square.WATER for value in range(self.width)]
            for value in range(self.height)
        ]
        self.pending = 0
        if allocate:
            self.allocate()

    def __repr__(self) -> str:
        return self._buffer(emoji=False)

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

                if self.fill(x0, y0, size, direction, value=ship):
                    break

            self.pending += size

    def fill(
        self,
        x0: int,
        y0: int,
        size: int,
        direction: Direction,
        value: Square = Square.WATER,
    ) -> bool:
        x, y = x0, y0

        for _index in range(size):
            if not self.grid[y][x] in EMPTY:
                return False
            if direction == direction.VERTICAL:
                y += 1
            elif direction == direction.HORIZONTAL:
                x += 1

        x, y = x0, y0

        for _index in range(size):
            self.grid[y][x] = value
            if direction == direction.VERTICAL:
                y += 1
            elif direction == direction.HORIZONTAL:
                x += 1

        return True

    def shoot(self, coordinate: str) -> Square:
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

    def _shoot(self, x: int, y: int) -> Square:
        position = self.grid[y][x]

        if position in SHIPS:
            self.grid[y][x] = Square.DEBRIS
            self.pending -= 1

        return position

    def _buffer(self, emoji: bool = False) -> str:
        buffer = []
        for y in range(self.height):
            for x in range(self.width):
                position = self.grid[y][x]
                value = position.emoji if emoji else position.value
                buffer.append(f"{value}")
            buffer.append("\n")
        return "".join(buffer)

    @property
    def finished(self):
        return self.pending == 0


class Runnable:
    def run(self):
        raise NotImplemented("Running logic is not implemented")
