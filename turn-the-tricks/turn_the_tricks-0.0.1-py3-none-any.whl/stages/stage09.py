# -*- coding: utf-8 -*-

from t3.stages.stage import Stage
from t3.objects.block import E, D, I, O, J, L, T, S, Z, BLOCK_I, BLOCK_O, BLOCK_J, BLOCK_L, BLOCK_T, BLOCK_S, BLOCK_Z


class Stage09(Stage):

    _solver = [
        [E, I, I, I, I, Z, J, T, T, T],
        [E, O, O, L, Z, Z, J, S, T, I],
        [J, O, O, L, Z, J, J, S, S, I],
        [J, J, J, L, L, E, T, E, S, I],
        [E, Z, Z, E, I, T, T, T, E, I],
        [E, E, Z, Z, I, L, L, L, Z, E],
        [E, O, O, E, I, L, E, Z, Z, E],
        [E, O, O, J, I, E, E, Z, E, E],
        [E, E, E, J, J, J, E, E, E, E],
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
        [E, D, D, D, D, D, D, D, D, D],
        [E, D, D, L, D, D, D, D, D, D],
        [D, D, D, L, D, D, D, D, D, D],
        [D, D, D, L, L, E, D, E, D, D],
        [E, D, D, E, D, D, D, D, E, D],
        [E, E, D, D, D, D, D, D, D, E],
        [E, D, D, E, D, D, E, D, D, E],
        [E, D, D, D, D, E, E, D, E, E],
        [E, E, E, D, D, D, E, E, E, E],
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
        BLOCK_J,
        BLOCK_Z,
        BLOCK_L,
        BLOCK_I,
        BLOCK_Z,
        BLOCK_T,
        BLOCK_J,
        BLOCK_I,
        BLOCK_L,
        BLOCK_J,
        BLOCK_O,
        BLOCK_S,
        # BLOCK_J,
        BLOCK_T,
        BLOCK_Z,
        BLOCK_I,
    ]
