# -*- coding: utf-8 -*-

from t3.stages.stage import Stage
from t3.objects.block import E, D, I, O, T, Z, J, S, BLOCK_I, BLOCK_O, BLOCK_T, BLOCK_Z, BLOCK_J, BLOCK_S


class Stage03(Stage):

    _solver = [
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

    board = [
        [D, E, D, E, S, E, D, D, D, E],
        [D, D, D, D, S, S, E, D, S, S],
        [E, D, D, T, E, S, E, S, S, D],
        [D, D, T, T, T, E, E, D, D, D],
        [D, D, I, I, I, I, E, D, D, E],
        [D, D, D, D, D, D, D, D, S, E],
        [E, E, E, E, D, D, E, E, S, S],
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
