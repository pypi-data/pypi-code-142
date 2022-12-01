# -*- coding: utf-8 -*-


from t3.stages.stage import Stage
from t3.objects.block import E, D, S, Z, BLOCK_S, BLOCK_Z


class Stage04(Stage):

    _solver = [
        [S, Z, Z, Z, Z, Z, Z, Z, Z, E],
        [S, S, Z, Z, Z, Z, Z, Z, Z, Z],
        [E, S, S, S, S, S, S, S, S, S],
        [E, S, S, S, S, S, S, S, S, Z],
        [E, E, E, E, E, E, E, E, Z, Z],
        [E, E, E, E, E, E, E, E, Z, E],
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

    board = [
        [S, D, D, D, D, D, D, D, D, E],
        [S, S, D, D, D, D, D, D, D, D],
        [E, S, D, D, D, D, D, D, D, D],
        [E, D, D, D, D, D, D, D, D, D],
        [E, E, E, E, E, E, E, E, D, D],
        [E, E, E, E, E, E, E, E, D, E],
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

    history = [
        BLOCK_Z,
        BLOCK_S,
        BLOCK_S,
        BLOCK_S,
        BLOCK_S,
        BLOCK_S,
        BLOCK_Z,
        BLOCK_Z,
        BLOCK_Z,
        BLOCK_Z,
    ]
