# -*- coding: utf-8 -*-

from t3.stages.stage import Stage
from t3.objects.block import E, I, O, T, Z, J, S, BLOCK_I, BLOCK_O, BLOCK_T, BLOCK_Z, BLOCK_J, BLOCK_S


class Stage02(Stage):

    board = [
        [S, E, T, E, S, E, T, T, T, E],
        [S, S, T, T, S, S, E, T, S, S],
        [E, S, T, T, E, S, E, S, S, Z],
        [O, O, T, T, T, E, E, J, Z, Z],
        [O, O, I, I, I, I, E, J, Z, E],
        [I, I, I, I, O, O, J, J, S, E],
        [E, E, E, E, O, O, E, E, S, S],
        [E, E, E, E, E, E, E, E, E, S],
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
        BLOCK_O,
        BLOCK_J,
        BLOCK_S,
        BLOCK_I,
        BLOCK_O,
        BLOCK_T,
        BLOCK_S,
        BLOCK_S,
        BLOCK_Z,
        BLOCK_S,
        BLOCK_T,
        BLOCK_T,
    ]
