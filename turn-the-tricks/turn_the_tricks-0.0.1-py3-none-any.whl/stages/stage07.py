# -*- coding: utf-8 -*-

from t3.stages.stage import Stage
from t3.objects.block import E, D, I, O, J, L, T, S, Z, BLOCK_I, BLOCK_O, BLOCK_J, BLOCK_L, BLOCK_T, BLOCK_S, BLOCK_Z


class Stage07(Stage):

    _solver = [
        [Z, Z, E, I, O, O, J, L, L, L],
        [S, Z, Z, I, O, O, J, L, S, S],
        [S, S, E, I, J, J, J, S, S, L],
        [I, S, T, I, J, J, J, L, L, L],
        [I, T, T, T, L, O, O, T, T, T],
        [I, E, L, L, L, O, O, E, T, E],
        [I, E, E, E, E, I, I, I, I, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
    ]

    board = [
        [D, D, E, D, D, D, D, D, D, D],
        [S, D, D, D, D, D, D, D, S, S],
        [S, S, E, D, J, D, D, S, S, D],
        [D, S, D, D, J, J, J, D, D, D],
        [D, D, D, D, D, D, D, D, D, D],
        [D, E, D, D, D, D, D, E, D, E],
        [D, E, E, E, E, D, D, D, D, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
    ]

    history = [
        BLOCK_I,
        BLOCK_T,
        BLOCK_L,
        BLOCK_L,
        BLOCK_S,
        BLOCK_L,
        BLOCK_O,
        BLOCK_J,
        BLOCK_I,
        BLOCK_T,
        BLOCK_S,
        BLOCK_J,
        BLOCK_O,
        BLOCK_Z,
        BLOCK_I,
    ]
