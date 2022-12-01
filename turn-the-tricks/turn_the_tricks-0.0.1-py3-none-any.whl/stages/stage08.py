# -*- coding: utf-8 -*-

from t3.stages.stage import Stage
from t3.objects.block import E, D, I, O, BLOCK_I, BLOCK_O


class Stage08(Stage):

    _solver = [
        [I, O, O, I, I, I, I, E, I, I],
        [I, O, O, E, I, I, I, I, I, I],
        [I, E, I, I, I, I, I, I, I, I],
        [I, E, E, E, O, O, I, I, I, I],
        [I, I, I, I, O, O, I, I, O, O],
        [I, I, I, I, I, I, I, I, O, O],
        [I, I, E, O, O, E, I, I, I, I],
        [I, I, E, O, O, E, I, I, I, I],
        [I, I, E, E, E, E, E, E, E, E],
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
        [D, D, D, D, D, D, D, E, D, D],
        [D, D, D, E, D, D, D, D, D, D],
        [D, E, D, D, D, D, D, D, D, D],
        [D, E, E, E, O, O, D, D, D, D],
        [D, D, D, D, O, O, D, D, O, O],
        [D, D, D, D, D, D, D, D, O, O],
        [D, D, E, D, D, E, D, D, D, D],
        [D, D, E, D, D, E, D, D, D, D],
        [D, D, E, E, E, E, E, E, E, E],
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
        BLOCK_I,
        BLOCK_O,
        BLOCK_I,
        BLOCK_O,
        BLOCK_I,
        BLOCK_I,
        BLOCK_I,
        BLOCK_O,
        BLOCK_I,
        BLOCK_I,
        BLOCK_I,
        BLOCK_I,
        BLOCK_I,
        BLOCK_O,
        BLOCK_I,
        BLOCK_I,
        BLOCK_I,
    ]
