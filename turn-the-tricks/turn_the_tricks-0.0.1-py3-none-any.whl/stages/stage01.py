# -*- coding: utf-8 -*-

from t3.stages.stage import Stage
from t3.objects.block import E, D, I, O, T, Z, S, BLOCK_I, BLOCK_O, BLOCK_T, BLOCK_Z, BLOCK_S


class Stage01(Stage):

    board = [
        [S, T, T, T, S, S, Z, I, O, O],
        [S, S, T, S, S, Z, Z, I, O, O],
        [E, S, E, E, E, Z, E, I, E, E],
        [E, E, E, E, E, E, E, I, E, E],
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
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
    ]

    history = [BLOCK_O, BLOCK_I, BLOCK_Z, BLOCK_S, BLOCK_S, BLOCK_T]
