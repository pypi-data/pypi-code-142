# -*- coding: utf-8 -*-

from typing import List
from t3.objects.matrix import Matrix


class Stage:
    board: Matrix
    history: List[Matrix]
