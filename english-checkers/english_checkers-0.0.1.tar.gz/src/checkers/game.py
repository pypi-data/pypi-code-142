"""This module is for simulating the English checkers game.

Class Game represents a simulation of the checkers game and allows
get all possible moves for the current side (current turn), make
and cancel moves (with previous game state recovery).

This file can also be imported as module and contains the following
classes:

    * GameState - (Enum) describes all possible states of the game
    * Color - represents player's color ( side in the game).
    * Game - represent a simulation of the game.
"""


from enum import Enum

from checkers.board import Board, Cell
from checkers.move import Move, WrongMoveError


class GameState(Enum):
    TIE = 0
    BLACK_WON = 1
    WHITE_WON = 2
    UNFINISHED = 3


class Color(Enum):
    BLACK = 1
    WHITE = 2


class Game:
    """
    A class to represent checkers board 8x8

    ...

    Attributes
    ----------
    board : Board
        board object
    state : type[GameState]
        current state of the game
    turn : Color
        Color of the chekers that have to go next
    last_changes : list[list[tuple[int, int, Cell]]]
        Last item is a tuple of row, column and initial value of the cell
        that was changed last. Previous item - last before last and so on.
    black_count : int
        Number of black checkers on the board
    white_count : int
        Number of white checkers on the board
    tie_counter : int
        Number of last serial moves when
        black_count and white_count were not changed
    tie_max : int
        Maximum value of the tie_counter
        If tie_counter == tie_max then game finishes with the tie

    Methods
    -------
    opponent() -> Color:
        Get the opponent of the current Color
    get_all_moves() -> list[Move]:
        Get the list off all possible moves for current turn
    make_move(self, move: Move) -> None:
        Make a move and set board to the next turn
    undo() -> None:
        Cancels last move and recover previous state and board
    """

    def __init__(self, size: int = 0):
        """
        Creating a board. Black goes first.
        """

        self.board: Board = Board(size)
        self.state: GameState = GameState.UNFINISHED
        self.turn: Color = Color.BLACK
        self.last_changes: list[list[tuple[int, int, Cell]]] = []
        self.black_count: int = self._initial_black_count()
        self.white_count: int = self.black_count
        self.tie_counter: int = 0
        self.tie_max: int = size * size // 2

    def _initial_black_count(self) -> int:
        """
        Calculate the initial number of black checkers

        Checkers fill all rows despite one in case size is odd
        or despite two in case size is even

        Returns
        -------
        int
            number of black checkers at the start of the game
        """

        size = self.board.size
        bc = (size // 2 - 1 + size % 2) * (size // 2)
        bc += (size // 2 - 1 + size % 2) // 2 * int(size % 2)

        return bc

    def undo(self) -> None:
        """
        Cancels last move and recover previous state and board.

        Returns
        -------
        None
        """

        if self.last_changes:
            self.state = GameState.UNFINISHED
            changes: list[tuple[int, int, Cell]] = self.last_changes.pop()
            while changes:
                row, col, cell = changes.pop()
                self._set_cell_undo(row, col, cell)

    def _set_cell(self, row: int, col: int, cell: Cell) -> None:
        """
        Call the board.set_cell method, update last_changes,
        update black_count and white_count.

        Parameters
        ----------
        row: int
            row index
        col: int
            column index
        cell: Cell
            type of cell is to set

        Returns
        -------
        None
        """

        prev_cell = self.board.get_cell(row, col)
        self.last_changes[-1].append((row, col, prev_cell))
        self.board.set_cell(row, col, cell)

        self._update_checkers_counters(prev_cell, cell)

    def _set_cell_undo(self, row: int, col: int, cell: Cell) -> None:
        """
        Call the board.set_cell method, update tie_counter,
        update black_count and white_count.

        Parameters
        ----------
        row: int
            row index
        col: int
            column index
        cell: Cell
            type of cell is to set

        Returns
        -------
        None
        """

        prev_cell = self.board.get_cell(row, col)
        if self.tie_counter > 0:
            self.tie_counter -= 1
        self.board.set_cell(row, col, cell)

        self._update_checkers_counters(prev_cell, cell)

    def _update_checkers_counters(self, prev_cell: Cell, cell: Cell) -> None:
        """
        Update black_count and white_count

        Parameters
        ----------
        prev_cell : Cell
            Type of the cell before change
        cell : Cell
            Type of the cell after change

        Returns
        -------
        None
        """

        if prev_cell in (Cell.BLACK, Cell.BLACK_QUEEN):
            self.black_count -= 1
        if prev_cell in (Cell.WHITE, Cell.WHITE_QUEEN):
            self.white_count -= 1

        if cell in (Cell.BLACK, Cell.BLACK_QUEEN):
            self.black_count += 1
        if cell in (Cell.WHITE, Cell.WHITE_QUEEN):
            self.white_count += 1

    def _update_state(self) -> None:
        """
        Change state from GameState.UNFINISHED to
        GameState.TIE, GameState.BLACK_WON or GameState.WHITE_WON
        if an appropriate board condition has become
        else the state does not change.
        """

        if self.tie_counter >= self.tie_max:
            self.state = GameState.TIE
        elif not self.get_all_moves():
            if self.turn == Color.BLACK:
                self.state = GameState.WHITE_WON
            else:
                self.state = GameState.BLACK_WON

    def opponent(self) -> Color:
        """
        Get the opponent of the current Color

        Returns
        -------
        Color
        """

        if self.turn == Color.BLACK:
            return Color.WHITE
        return Color.BLACK

    def make_move(self, move: Move) -> None:
        """
        Make a move and set board to the next turn

        Parameters
        ----------
        move : Move

        Returns
        -------
        None
        """

        if len(move.steps) == 1:
            first_step_len = abs(max(move.steps[0][0] - move.start[0],
                                     move.steps[0][1] - move.start[1]))

        self.tie_counter += 1
        self.last_changes.append([])
        if len(move.steps) == 1 and first_step_len == 1:
            self._make_one_step_move(move)
        else:
            self._make_beat_move(move)
            self.tie_counter = 0
        self._check_and_change_to_queen(move)

        self.turn = self.opponent()
        self._update_state()

    def _make_one_step_move(self, move: Move) -> None:
        """
        Make a one step move

        Parameters
        ----------
        move : Move

        Returns
        -------
        None
        """

        row, col = move.steps[0]
        start_row, start_col = move.start
        cell = self.board.get_cell(start_row, start_col)
        self._set_cell(row, col, cell)
        self._set_cell(start_row, start_col, Cell.EMPTY)

    def _make_beat_move(self, move: Move) -> None:
        """
        Make a beating move

        Parameters
        ----------
        move : Move

        Returns
        -------
        None
        """

        prev_row, prev_col = move.start
        prev_cell = self.board.get_cell(prev_row, prev_col)
        for step in move:
            row, col = step
            self._set_cell(
                (prev_row + row) // 2,
                (prev_col + col) // 2,
                Cell.EMPTY)
            self._set_cell(prev_row, prev_col, Cell.EMPTY)
            self._set_cell(row, col, prev_cell)
            prev_row, prev_col = row, col

    def _check_and_change_to_queen(self, move: Move) -> None:
        """
        Change checker to queen if last step in the move
        is the first or the last row in the board

        Parameters
        ----------
        move : Move

        Returns
        -------
        None
        """

        last_row, last_col = move.steps[-1]
        if self.turn == Color.BLACK and last_row == self.board.size - 1:
            self._set_cell(last_row, last_col, Cell.BLACK_QUEEN)
        elif self.turn == Color.WHITE and last_row == 0:
            self._set_cell(last_row, last_col, Cell.WHITE_QUEEN)

    def _is_turns_checker(self, cell: Cell) -> bool:
        """
        Check if the cell's checker belong to self.turn

        Returns
        -------
        bool
        """

        return (cell == Cell.BLACK or cell == Cell.BLACK_QUEEN) \
            and self.turn == Color.BLACK \
            or (cell == Cell.WHITE or cell == Cell.WHITE_QUEEN) \
            and self.turn == Color.WHITE

    def get_all_moves(self) -> list[Move]:
        """
        Get the list off all possible moves for current turn

        Returns
        -------
        list[Move]
            list consist of the all possible moves for current turn,
            [] if there are no moves
        """

        moves = []
        for row in range(self.board.size):
            for col in range(self.board.size):
                try:
                    moves += self._get_beat_moves(row, col)
                except WrongMoveError:
                    continue

        if moves:
            return moves

        for row in range(self.board.size):
            for col in range(self.board.size):
                try:
                    moves += self._get_not_beat_moves(row, col)
                except WrongMoveError:
                    continue

        return moves

    def _is_correct_cell_for_move(self, row: int, col: int) -> None:
        """
        If row or col are incorrect indices or checker in the cell
        is not current turn's checker raises WrongMoveError.

        Parameters
        ----------
        row : int
            0-indexed row number in the board
        col : int
            0-indexed column number in the board

        Returns
        -------
        None

        Raises
        ------
        WrongMoveError
            when cell type does not correspond to turn or
            row or col out of range(board.size)
        """

        if not 0 <= row < self.board.size \
                or not 0 <= col < self.board.size:
            raise WrongMoveError('row and col must be in the'
                                 'range(self.board.size)')

        cell = self.board.get_cell(row, col)
        if not self._is_turns_checker(cell):
            raise WrongMoveError('cell type does not correspond turn\'s color')

    def _get_beat_moves(self, row: int, col: int) -> list[Move]:
        """
        Find all beating moves for checker with coordinates row and col.

        Parameters
        ----------
        row : int
            0-indexed row number in the board
        col : int
            0-indexed column number in the board

        Returns
        -------
        list[Move]
            list of possible moves for checker
            [] if there is no moves

        Raises
        ------
        WrongMoveError
            when cell type does not correspond to turn or
            row or col out of range(board.size)
        """

        try:
            self._is_correct_cell_for_move(row, col)
        except WrongMoveError as e:
            raise e

        moves = []
        for step_sequence in self._get_beat_steps(row, col):
            moves.append(Move((row, col), step_sequence))

        return moves

    def _get_not_beat_moves(self, row: int, col: int) -> list[Move]:
        """
        Find all not beating moves for checker with coordinates row and col.

        Parameters
        ----------
        row : int
            0-indexed row number in the board
        col : int
            0-indexed column number in the board

        Returns
        -------
        list[Move]
            list of possible moves for checker
            [] if there is no moves

        Raises
        ------
        WrongMoveError
            when cell type does not correspond to turn or
            row or col out of range(board.size)
        """

        try:
            self._is_correct_cell_for_move(row, col)
        except WrongMoveError as e:
            raise e

        moves = []
        for step_sequence in self._get_not_beat_steps(row, col):
            moves.append(Move((row, col), step_sequence))

        return moves

    def _cell_with_opponent(self, row: int, col: int) -> bool:
        """
        Check if the cell with opponent checker.

        Parameters
        ----------
        row : int
            0-indexed row number in the board
        col : int
            0-indexed column number in the board

        Returns
        -------
        bool
        """

        try:
            cell = self.board.get_cell(row, col)
        except IndexError:
            return False

        if self.turn == Color.BLACK \
                and cell in (Cell.WHITE, Cell.WHITE_QUEEN):
            return True
        if self.turn == Color.WHITE \
                and cell in (Cell.BLACK, Cell.BLACK_QUEEN):
            return True
        return False

    def _empty_cell(self, row: int, col: int) -> bool:
        """
        Check if the cell is empty.

        Parameters
        ----------
        row : int
            0-indexed row number in the board
        col : int
            0-indexed column number in the board

        Returns
        -------
        bool
        """

        try:
            cell = self.board.get_cell(row, col)
        except IndexError:
            return False

        return cell == Cell.EMPTY

    def _dfs_find_beat_steps(
            self,
            row: int,
            col: int,
            dirs: list[tuple[int, int]],
            bet: set[tuple[int, int]] | None = set()
    ) -> list[list[tuple[int, int]]]:
        """
        Find all steps that beat opponent's checkers

        Beating step is a jump through an opponent checker
        to an empty cell.

        Parameters
        ----------
        row : int
            0-indexed row number in the board
        col : int
            0-indexed column numer in the board
        dirs : list[tuple[int, int]]
            list of possible directions to a move
        bet : set[tuple[int, int]]
            set of cells with bet checkers

        Returns
        -------
        list[list[tuple[int, int]]]
            list of lists of steps for each possible move
        """

        steps = []
        for rdir, cdir in dirs:
            r, c = row + rdir, col + cdir
            if self._cell_with_opponent(r, c):
                if (r, c) in bet:
                    break
                bet.add((r, c))
                r, c = r + rdir, c + cdir
                if self._empty_cell(r, c):
                    new_dirs = []
                    for d in dirs:
                        if not (d[0] == -rdir and d[1] == -cdir):
                            new_dirs.append(d)
                    next_steps = self._dfs_find_beat_steps(r, c, new_dirs, bet)
                    tmp = [(r, c)]
                    if not next_steps:
                        steps += [tmp]
                    for step in next_steps:
                        steps.append(tmp + step)
                bet.remove((r - rdir, c - cdir))

        return steps

    def _find_not_beat_steps(
            self,
            row: int,
            col: int,
            dirs: list[tuple[int, int]]
    ) -> list[list[tuple[int, int]]]:
        """
        Find all one step and not beating steps

        Parameters
        ----------
        row : int
            0-indexed row number in the board
        col : int
            0-indexed column numer in the board
        dirs : list[tuple[int, int]]
            list of possible directions to a move

        Returns
        -------
        list[list[tuple[int, int]]]
            list of lists of steps for each possible move
        """

        res = []
        for dir in dirs:
            r1, c1 = row + dir[0], col + dir[1]
            try:
                cell = self.board.get_cell(r1, c1)
            except IndexError:
                continue
            if cell == Cell.EMPTY:
                res.append([(r1, c1)])

        return res

    def _get_dirs(self, row: int, col: int) -> list[tuple[int, int]]:
        """
        Find all possible directions for move for the checker.
        It is consider that there is a checker in the cell!

        Each directions represents diagonal step and is
        pair of two ones with some signs. For example:
        (1, -1) or (-1, -1).

        Parameters
        ----------
        row : int
            0-indexed row number in the board
        col : int
            0-indexed column numer in the board

        Returns
        -------
        list[tuple[int, int]]
            list of tuples of directions
        """

        dirs = []
        cell = self.board.get_cell(row, col)
        if cell == Cell.BLACK:
            dirs = [
                (1, -1),
                (1, 1),
            ]
        elif cell == Cell.WHITE:
            dirs = [
                (-1, -1),
                (-1, 1),
            ]
        elif cell in (Cell.BLACK_QUEEN, Cell.WHITE_QUEEN):
            dirs = [
                (-1, -1),
                (-1, 1),
                (1, -1),
                (1, 1),
            ]

        return dirs

    def _get_beat_steps(self, row: int, col: int) -> list[Move]:
        """
        Find all possible beating steps for checker.
        It is consider that there is a checker in the cell!

        Parameters
        ----------
        row : int
            0-indexed row number in the board
        col : int
            0-indexed column numer in the board

        Returns
        -------
        list[list[tuple[int, int]]]
            list of lists of steps for each possible move
        """

        dirs = self._get_dirs(row, col)
        steps = self._dfs_find_beat_steps(row, col, dirs)

        return steps

    def _get_not_beat_steps(self, row: int, col: int) -> list[Move]:
        """
        Find all possible not beating steps for checker.
        It is consider that there is a checker in the cell!

        Parameters
        ----------
        row : int
            0-indexed row number in the board
        col : int
            0-indexed column numer in the board

        Returns
        -------
        list[list[tuple[int, int]]]
            list of lists of steps for each possible move
        """

        dirs = self._get_dirs(row, col)
        steps = self._find_not_beat_steps(row, col, dirs)

        return steps


if __name__ == '__main__':
    game = Game(4)
    moves = game.get_all_moves()
    while game.state == GameState.UNFINISHED:
        print(game.board)
        print('b:', game.black_count, 'w:', game.white_count)
        print(game.turn)

        moves = game.get_all_moves()
        for i, move in enumerate(moves):
            print(i + 1, ':', move)
        print('Input number of the move for move:')
        try:
            move_number = int(input().strip())
        except ValueError:
            print('Wrong input. Number of the move must be int')
        try:
            move = moves[move_number - 1]
        except IndexError:
            print('Wrong move')
            continue
        game.make_move(move)
    else:
        print(game.board)
        print(game.state)

    while True:
        print("Do you want to undo? If yes input '1':")
        ans = input()
        if ans != '1':
            break
        game.undo()
        print(game.board)
        print('b:', game.black_count, 'w:', game.white_count)
        print(game.turn)
