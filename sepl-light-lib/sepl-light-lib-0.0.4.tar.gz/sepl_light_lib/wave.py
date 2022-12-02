from typing import Tuple

import _sepl_light_lib


def wave_length_to_rgb(wave_length: float) -> Tuple[int, int, int]:
    return _sepl_light_lib.wave_length_to_rgb(wave_length)
