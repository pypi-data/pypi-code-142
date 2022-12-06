"""This module is for representing checkers board.

Class Cell(Enum) describes all possible conditions of the board's cell.

Class Board is to represent and initially fill the board and allow to
read and set cell values.

This file can also be imported as module and contains the following
classes:

    * Cell - Enum that represents cell values
    * Board - represent checkers board
"""


from enum import Enum


class Cell(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2
    BLACK_QUEEN = 3
    WHITE_QUEEN = 4


class Board:
    """
    A class to represent checkers board (SIZE)x(SIZE)

    ...

    Attributes
    ----------
    _board : list[list[type[Cell]]]
        board is a matrix of Cells
    board_state : type[BoardState]
        current state of the game

    Methods
    -------
    fill_initial():
        fill the _board by Cell.BLACK and Cell.WHITE.
    get_cell(row: int, col: int) -> Cell:
        Getter of cell with coords row and col.
    set_cell(row: int, col: int, cell: Cell) -> None:
        Set cell value with coords row and col.
    """

    SIZE = 8

    def __init__(self, size: int = 0):
        """
        Set the board arrangenment in accordance with
        rules of English chekers.
        """

        self.size = Board.SIZE
        if size != 0:
            self.size = size
        self._board = [[Cell.EMPTY] * Board.SIZE for i in range(Board.SIZE)]
        self.fill_initial()

    def fill_initial(self):
        """
        Fill the board 8x8 (example) by chekers:

        |----------------|
        |__b __b __b __b |
        |b __b __b __b __|
        |__b __b __b __b |
        |  __  __  __  __|
        |__  __  __  __  |
        |w __w __w __w __|
        |__w __w __w __w |
        |w __w __w __w __|
        |----------------|

        where ' ' is an empty black cell,
        '_' is an empty white cell,
        'b' is a black cell with the black cheker,
        'w' is a black cell with th white cheker.
        """

        for row in range(self.size // 2 - 1 + self.size % 2):
            for col in range(self.size):
                if row % 2 != col % 2:
                    self._board[row][col] = Cell.BLACK

        for row in range(self.size // 2 + 1, self.size):
            for col in range(self.size):
                if row % 2 != col % 2:
                    self._board[row][col] = Cell.WHITE

    def get_cell(self, row: int, col: int) -> Cell:
        """
        Getter of cell with coords row and col.

        Parameters
        ----------
        row: int
            row index
        col: int
            column index

        Raises
        ------
        IndexError
            when row and col are not between 0 and size - 1

        Returns
        -------
        Cell
            cell type
        """

        if not 0 <= row < self.size or not 0 <= col < self.size:
            raise IndexError('row and col indices must be '
                             f'between 0 and {Board.SIZE - 1}.')

        return self._board[row][col]

    def set_cell(self, row: int, col: int, cell: Cell) -> None:
        """
        Set cell value with coords row and col.

        Parameters
        ----------
        row: int
            row index
        col: int
            column index
        cell: Cell
            type of cell is to set

        Raises
        ------
        IndexError
            when row and col are not between 0 and Board.Size - 1

        Returns
        -------
        None
        """

        if not 0 <= row < self.size or not 0 <= col < self.size:
            raise IndexError('row and col indices must be '
                             f'between 0 and {self.size - 1}.')

        self._board[row][col] = cell

    def __str__(self) -> str:
        """
        String representation of the board.

        It is the table size x size.
        Empty black cell is two spaces '  ',
        empty white cell is two underlines '__',
        black man checkers is 'b ',
        white man checker is 'w ',
        black queen checker is 'B ',
        white queen checker is 'W '
        """

        cell_to_str = {
            Cell.EMPTY: ('__', '  '),
            Cell.BLACK: 'b ',
            Cell.WHITE: 'w ',
            Cell.BLACK_QUEEN: 'B ',
            Cell.WHITE_QUEEN: 'W ',
        }

        s = '|' + '--' * self.size + '|\n'
        for row in range(self.size):
            s += '|'
            for col in range(self.size):
                cell = self.get_cell(row, col)
                if cell == Cell.EMPTY:
                    s += cell_to_str[cell][(row + col) % 2]
                else:
                    s += cell_to_str[cell]
            s += '|\n'
        s += '|' + '--' * self.size + '|\n'

        return s


if __name__ == '__main__':
    board = Board()
    print(board)
