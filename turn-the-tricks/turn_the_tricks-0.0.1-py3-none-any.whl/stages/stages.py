# -*- coding: utf-8 -*-

from typing import List

from t3.stages.stage import Stage
from t3.stages.stage00 import Stage00
from t3.stages.stage01 import Stage01
from t3.stages.stage02 import Stage02
from t3.stages.stage03 import Stage03
from t3.stages.stage04 import Stage04
from t3.stages.stage05 import Stage05
from t3.stages.stage06 import Stage06
from t3.stages.stage07 import Stage07
from t3.stages.stage08 import Stage08
from t3.stages.stage09 import Stage09
from t3.stages.stage10 import Stage10


def create_stages() -> List[Stage]:
    return [
        Stage00(),
        Stage01(),
        Stage02(),
        Stage03(),
        Stage04(),
        Stage05(),
        Stage06(),
        Stage07(),
        Stage08(),
        Stage09(),
        Stage10(),
    ]
