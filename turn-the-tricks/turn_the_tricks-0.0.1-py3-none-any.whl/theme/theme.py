# -*- coding: utf-8 -*-

from t3.color.color_tuple import ColorTuple


class Theme:
    background: ColorTuple
    foreground: ColorTuple
    accent: ColorTuple

    empty: ColorTuple

    block_disable: ColorTuple

    block_i_normal: ColorTuple
    block_o_normal: ColorTuple
    block_t_normal: ColorTuple
    block_l_normal: ColorTuple
    block_j_normal: ColorTuple
    block_s_normal: ColorTuple
    block_z_normal: ColorTuple

    block_i_clear: ColorTuple
    block_o_clear: ColorTuple
    block_t_clear: ColorTuple
    block_l_clear: ColorTuple
    block_j_clear: ColorTuple
    block_s_clear: ColorTuple
    block_z_clear: ColorTuple

    font_name: str
    title_size: int
    subtitle_size: int

    border_width: int
    margin_width: int

    history_size: int
    history_cap_width: int
