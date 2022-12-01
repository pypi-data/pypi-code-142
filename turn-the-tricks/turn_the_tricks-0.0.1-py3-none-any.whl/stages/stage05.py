# -*- coding: utf-8 -*-

from t3.stages.stage import Stage
from t3.objects.block import E, I, O, J, L, T, S, Z, BLOCK_I, BLOCK_O, BLOCK_J, BLOCK_L, BLOCK_T, BLOCK_S, BLOCK_Z


class Stage05(Stage):

    board = [
        [I, O, O, J, L, L, L, T, T, T],
        [I, O, O, J, L, O, O, J, T, Z],
        [I, T, J, J, T, O, O, J, Z, Z],
        [I, T, T, T, T, T, J, J, Z, I],
        [S, T, I, I, I, I, L, L, L, I],
        [S, S, O, O, Z, Z, L, T, E, I],
        [S, S, O, O, T, Z, Z, T, T, I],
        [S, S, E, T, T, T, E, T, O, O],
        [E, S, E, E, E, E, E, E, O, O],
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
        BLOCK_O,
        BLOCK_T,
        BLOCK_S,
        BLOCK_T,
        BLOCK_Z,
        BLOCK_O,
        BLOCK_L,
        BLOCK_I,
        BLOCK_S,
        BLOCK_I,
        BLOCK_T,
        BLOCK_J,
        BLOCK_Z,
        BLOCK_O,
        BLOCK_T,
        BLOCK_T,
        BLOCK_L,
        BLOCK_J,
        BLOCK_I,
        BLOCK_O,
    ]
