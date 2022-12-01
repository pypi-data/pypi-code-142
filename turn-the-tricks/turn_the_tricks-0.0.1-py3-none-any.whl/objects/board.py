# -*- coding: utf-8 -*-

from typing import Dict, Tuple, Optional

from arcade import SpriteList, Texture, Sprite

from t3.objects.block import N, is_active_block
from t3.objects.matrix import Matrix


class Board:
    def __init__(
        self,
        cols: int,
        rows: int,
        block_width: int,
        block_height: int,
        block_margin: int,
        block_textures: Dict[int, Texture],
        block_init: Optional[int] = None,
    ):
        assert rows > 0
        assert cols > 0

        self._cols = cols
        self._rows = rows
        self._block_width = block_width
        self._block_height = block_height
        self._block_margin = block_margin
        self._offset_x = 0
        self._offset_y = 0
        self._block_textures = block_textures

        init = block_init if block_init is not None else N
        self._matrix = [[init for _x in range(cols)] for _y in range(rows)]
        self._sprites = self.create_sprites()

    def create_sprites(self) -> SpriteList:
        result = SpriteList()
        for y in range(self._rows):
            for x in range(self._cols):
                sprite = Sprite()
                for texture in self._block_textures.values():
                    sprite.append_texture(texture)
                sprite.set_texture(self._matrix[y][x])
                center = self.measure_block_center(x, y)
                sprite.center_x = self._offset_x + center[0]
                sprite.center_y = self._offset_y + center[1]
                result.append(sprite)
        return result

    def measure_block_center(self, col: int, row: int) -> Tuple[float, float]:
        assert self._block_width > 0
        assert self._block_height > 0
        assert self._block_margin >= 0

        bw = self._block_width
        bh = self._block_height
        m = self._block_margin

        left = (m + bw) * col + m
        top = (m + bh) * row + m

        center_x = left + (bw // 2)
        center_y = top + (bh // 2)

        return center_x, center_y

    @property
    def matrix(self) -> Matrix:
        return self._matrix

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def block_width(self) -> int:
        return self._block_width

    @property
    def block_height(self) -> int:
        return self._block_height

    @property
    def block_margin(self) -> int:
        return self._block_margin

    @property
    def width(self) -> int:
        margin = self._block_margin
        width = self._block_width
        cols = self._cols
        return (margin + width) * cols + margin

    @property
    def height(self) -> int:
        margin = self._block_margin
        height = self._block_height
        rows = self._rows
        return (margin + height) * rows + margin

    @property
    def half_width(self) -> int:
        return self.width // 2

    @property
    def half_height(self) -> int:
        return self.height // 2

    @property
    def left(self) -> int:
        return self._offset_x

    @property
    def right(self) -> int:
        return self._offset_x + self.width

    @property
    def top(self) -> int:
        return self._offset_y + self.height

    @property
    def bottom(self) -> int:
        return self._offset_y

    @property
    def bbox(self) -> Tuple[int, int, int, int]:
        left, top, right, bottom = None, None, None, None

        for row in range(self._rows):
            any_active = False

            for col in range(self._cols):
                active = is_active_block(self._matrix[row][col])

                if active:
                    any_active = True
                    if left is None:
                        left = col
                        right = col
                    else:
                        right = col

            if any_active:
                if bottom is None:
                    bottom = row
                    top = row
                else:
                    top = row

        return left, top, right, bottom

    def as_sprite(self, col: int, row: int) -> Sprite:
        return self._sprites[self._cols * row + col]

    def set_texture(self, col: int, row: int, texture_index: int) -> None:
        self.as_sprite(col, row).set_texture(texture_index)

    def set_matrix(self, matrix: Matrix) -> None:
        self._cols = len(matrix[0])
        self._rows = len(matrix)
        self._matrix = matrix
        self._sprites = self.create_sprites()

    def join_matrix(self, matrix: Matrix, x=0, y=0) -> None:
        for row, line in enumerate(matrix):
            for col, val in enumerate(line):
                self._matrix[row + y - 1][col + x] = val

    def fill(self, value: int) -> None:
        for row in range(self._rows):
            for col in range(self._cols):
                self._matrix[row][col] = value

    def is_all_inactive(self) -> bool:
        for row in range(self._rows):
            for col in range(self._cols):
                if is_active_block(self._matrix[row][col]):
                    return False
        return True

    def update_offset(self, offset_x: int, offset_y: int) -> None:
        self._offset_x = offset_x
        self._offset_y = offset_y

        for row in range(self._rows):
            for col in range(self._cols):
                center = self.measure_block_center(col, row)
                sprite = self.as_sprite(col, row)
                sprite.center_x = offset_x + center[0]
                sprite.center_y = offset_y + center[1]

    def update_textures(self):
        for row in range(self._rows):
            for col in range(self._cols):
                self.set_texture(col, row, self._matrix[row][col])

    def fill_matrix(self, shape: Matrix, offset_x: int, offset_y: int, value=N) -> None:
        for row, line in enumerate(shape):
            for col, val in enumerate(line):
                if not is_active_block(val):
                    continue
                self._matrix[row + offset_y][col + offset_x] = value

    def check_collision(self, shape: Matrix, offset_x: int, offset_y: int) -> bool:
        for row, line in enumerate(shape):
            for col, val in enumerate(line):
                if not is_active_block(val):
                    continue
                board_value = self._matrix[row + offset_y][col + offset_x]
                if is_active_block(board_value):
                    return True
        return False

    def check_intersection(self, shape: Matrix, offset_x: int, offset_y: int) -> bool:
        for row, line in enumerate(shape):
            for col, val in enumerate(line):
                if not is_active_block(val):
                    continue
                board_value = self._matrix[row + offset_y][col + offset_x]
                if not is_active_block(board_value):
                    return False
        return True

    def check_insertable(self, shape: Matrix, offset_x: int, offset_y: int) -> bool:
        for col in range(len(shape[0])):
            col_top = False
            for row in range(len(shape) - 1, -1, -1):
                val = shape[row][col]
                if not col_top:
                    if is_active_block(val):
                        col_top = True
                    continue

                if is_active_block(val):
                    continue

                board_value = self._matrix[row + offset_y][col + offset_x]
                if is_active_block(board_value):
                    return False

            # All spaces under `shape` in `board` should be empty
            for y in range(offset_y - 1, -1, -1):
                board_value = self._matrix[y][col + offset_x]
                if is_active_block(board_value):
                    return False

        return True

    def draw(self) -> None:
        self._sprites.draw()
