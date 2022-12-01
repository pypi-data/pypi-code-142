# -*- coding: utf-8 -*-

from t3.stages.stage import Stage
from t3.objects.block import E, D, I, O, J, L, T, S, Z, BLOCK_I, BLOCK_O, BLOCK_J, BLOCK_L, BLOCK_T, BLOCK_S, BLOCK_Z


class Stage10(Stage):

    _solver = [
        [S, Z, Z, E, O, O, I, T, T, T],
        [S, S, Z, Z, O, O, I, E, T, Z],
        [T, S, E, L, L, L, I, J, Z, Z],
        [T, T, T, L, J, J, I, J, Z, E],
        [T, T, T, T, J, E, J, J, S, S],
        [E, L, L, L, J, O, O, S, S, Z],
        [T, L, O, O, E, O, O, E, Z, Z],
        [T, T, O, O, I, I, I, I, Z, L],
        [T, I, I, I, I, E, T, L, L, L],
        [E, E, J, E, E, T, T, T, E, E],
        [E, E, J, E, E, E, E, O, O, E],
        [E, J, J, E, E, E, E, O, O, E],
        [E, E, I, I, I, I, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
    ]

    board = [
        [D, D, D, E, D, D, I, D, D, D],
        [D, D, D, D, D, D, I, E, D, D],
        [D, D, E, D, D, D, I, D, D, D],
        [D, D, T, D, D, D, I, D, D, E],
        [D, T, T, T, D, E, D, D, D, D],
        [E, D, D, D, D, D, D, D, D, D],
        [D, D, D, D, E, D, D, E, D, D],
        [D, D, D, D, I, I, I, I, D, D],
        [D, D, D, D, D, E, D, D, D, D],
        [E, E, D, E, E, D, D, D, E, E],
        [E, E, D, E, E, E, E, D, D, E],
        [E, D, D, E, E, E, E, D, D, E],
        [E, E, D, D, D, D, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
    ]

    history = [

        BLOCK_O,
        BLOCK_I,
        BLOCK_J,
        BLOCK_T,
        BLOCK_I,
        BLOCK_L,
        BLOCK_I,
        BLOCK_O,
        BLOCK_T,
        BLOCK_Z,
        BLOCK_L,
        BLOCK_O,
        BLOCK_S,
        BLOCK_T,
        BLOCK_J,
        BLOCK_T,
        BLOCK_L,
        BLOCK_J,
        BLOCK_Z,
        BLOCK_S,
        BLOCK_T,
        BLOCK_I,
        BLOCK_O,
        BLOCK_Z,
    ]
