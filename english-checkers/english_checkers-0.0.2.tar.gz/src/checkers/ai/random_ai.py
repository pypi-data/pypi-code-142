"""This module contains class RandomAI

RandomAI just return random move from the moves that
were returned by the get_all_moves method of the Game.

This file can also be imported as module and contains the following
classes:

    * RandomAI - represents AI player that chooses moves randomly
"""

import random

from checkers.game import Game, GameState, Color
from checkers.move import Move


class RandomAI:
    """
    The class represents AI player that chooses moves randomly

    ...

    Attributes
    ----------
    _game : Game
        separate Game object that allows to get all possible moves
    color : Color
        color of AI player

    Methods
    -------
    make_move(opponent_move: Move | None = None) -> Move:
        takes last opponent's move if it was presented
        and returns randomly chosen move
    """
    def __init__(self, size: int, color: Color):
        """
        Creates separate Game object and writes color of AI player
        """
        self._game: Game = Game(size)
        self.color: Color = color

    def make_move(self, opponent_move: Move | None = None) -> Move:
        """
        takes last opponent's move if it was presented
        and returns randomly chosen move

        Parameters
        ----------
        opponent_move : Move | None, optional
            last opponent's move if it was presented

        Returns
        -------
        Move
            Move is randomly chosen by AI
        """
        if opponent_move is not None:
            self._game.make_move(opponent_move)
        moves = self._game.get_all_moves()
        move = moves[random.randint(0, len(moves) - 1)]
        self._game.make_move(move)

        return move


if __name__ == '__main__':
    size = 8
    game = Game(size)
    ai_color = Color.WHITE
    ai = RandomAI(size, ai_color)
    if ai_color == Color.BLACK:
        move = None
    while game.state == GameState.UNFINISHED:
        print(game.board)
        print('b:', game.black_count, 'w:', game.white_count)
        print(game.turn)

        if game.turn == ai_color:
            move = ai.make_move(move)
        else:
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
