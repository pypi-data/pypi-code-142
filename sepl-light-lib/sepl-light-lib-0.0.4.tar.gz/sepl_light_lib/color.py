from typing import List, Tuple, Union


def check_rgb(color: Union[List[int], Tuple[int, int, int]]) -> bool:
    if len(color) != 3:
        return False

    for color_component in color:
        if color_component < 0 or color_component > 255:
            return False

    return True


def rgb_to_hex(color: Union[List[int], Tuple[int, int, int]]) -> str:
    if check_rgb(color):
        return "#%02x%02x%02x" % color
    else:
        return ""
