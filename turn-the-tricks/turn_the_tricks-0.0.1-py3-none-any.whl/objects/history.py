# -*- coding: utf-8 -*-

from typing import Dict, Final, List, Tuple

from arcade import Texture

from t3.objects.matrix import Matrix
from t3.objects.board import Board


class History:

    PREVIEW_COLS: Final[int] = 4
    PREVIEW_ROWS: Final[int] = 2

    def __init__(
        self,
        drawing_size: int,
        block_width: int,
        block_height: int,
        block_margin: int,
        board_margin: int,
        block_textures: Dict[int, Texture],
    ):
        self._drawing_size = drawing_size
        self._block_width = block_width
        self._block_height = block_height
        self._block_margin = block_margin
        self._board_margin = board_margin
        self._offset_x = 0
        self._offset_y = 0
        self._block_textures = block_textures
        self._boards: List[Board] = list()

    @property
    def size(self) -> int:
        return len(self._boards)

    def _create_board(self, matrix: Matrix) -> Board:
        result = Board(
            History.PREVIEW_COLS,
            History.PREVIEW_ROWS,
            self._block_width,
            self._block_height,
            self._block_margin,
            self._block_textures,
        )
        result.set_matrix(matrix)
        return result

    def set_history(self, history: List[Matrix]) -> None:
        self._boards = [self._create_board(h) for h in history]

    def pop(self) -> Board:
        result = self._boards.pop(0)
        self.update()
        return result

    def update_offset(self, offset_x: int, offset_y: int) -> None:
        self._offset_x = offset_x
        self._offset_y = offset_y

        x = offset_x
        y = offset_y
        for board in self._boards:
            board.update_offset(x, y)
            y += board.height + self._board_margin

    def update_textures(self):
        for board in self._boards:
            board.update_textures()

    def update(self) -> None:
        self.update_offset(self._offset_x, self._offset_y)
        self.update_textures()

    def draw(self) -> None:
        for board in self._boards[:self._drawing_size]:
            board.draw()
