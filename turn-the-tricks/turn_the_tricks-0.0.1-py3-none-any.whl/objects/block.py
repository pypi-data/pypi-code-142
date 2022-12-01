# -*- coding: utf-8 -*-

from enum import Enum, unique, auto
from typing import Final, Dict

from PIL import Image, ImageDraw
from arcade import Texture

from t3.color.color_tuple import ColorTuple
from t3.objects.matrix import Matrix
from t3.theme.theme import Theme


@unique
class BlockIndex(Enum):
    n = 0
    e = auto()
    d = auto()

    i = auto()
    o = auto()
    t = auto()
    l = auto()  # noqa
    j = auto()
    s = auto()
    z = auto()

    ic = auto()
    oc = auto()
    tc = auto()
    lc = auto()
    jc = auto()
    sc = auto()
    zc = auto()


N: Final[int] = BlockIndex.n.value  # None
E: Final[int] = BlockIndex.e.value  # Empty
D: Final[int] = BlockIndex.d.value  # Disable

I: Final[int] = BlockIndex.i.value  # noqa
O: Final[int] = BlockIndex.o.value  # noqa
T: Final[int] = BlockIndex.t.value
L: Final[int] = BlockIndex.l.value
J: Final[int] = BlockIndex.j.value
S: Final[int] = BlockIndex.s.value
Z: Final[int] = BlockIndex.z.value

IC: Final[int] = BlockIndex.ic.value
OC: Final[int] = BlockIndex.oc.value
TC: Final[int] = BlockIndex.tc.value
LC: Final[int] = BlockIndex.lc.value
JC: Final[int] = BlockIndex.jc.value
SC: Final[int] = BlockIndex.sc.value
ZC: Final[int] = BlockIndex.zc.value

BLOCK_I: Final[Matrix] = [
    [I, I, I, I],
]
BLOCK_O: Final[Matrix] = [
    [O, O],
    [O, O],
]
BLOCK_T: Final[Matrix] = [
    [T, T, T],
    [N, T, N],
]
BLOCK_J: Final[Matrix] = [
    [N, N, J],
    [J, J, J],
]
BLOCK_L: Final[Matrix] = [
    [L, N, N],
    [L, L, L],
]
BLOCK_Z: Final[Matrix] = [
    [N, Z, Z],
    [Z, Z, N],
]
BLOCK_S: Final[Matrix] = [
    [S, S, N],
    [N, S, S],
]

BLOCK_IC: Final[Matrix] = [
    [IC, IC, IC, IC],
]
BLOCK_OC: Final[Matrix] = [
    [OC, OC],
    [OC, OC],
]
BLOCK_TC: Final[Matrix] = [
    [TC, TC, TC],
    [N, TC, N],
]
BLOCK_JC: Final[Matrix] = [
    [N, N, JC],
    [JC, JC, JC],
]
BLOCK_LC: Final[Matrix] = [
    [LC, N, N],
    [LC, LC, LC],
]
BLOCK_ZC: Final[Matrix] = [
    [N, ZC, ZC],
    [ZC, ZC, N],
]
BLOCK_SC: Final[Matrix] = [
    [SC, SC, N],
    [N, SC, SC],
]


def is_active_block(v: int) -> bool:
    return v != N and v != E


def create_block_texture(
    name: str,
    width: int,
    height: int,
    color: ColorTuple,
) -> Texture:
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    xy = (0, 0, width, height)
    draw.rectangle(xy, color)
    return Texture(name, image=image)


def create_block_textures(width: int, height: int, theme: Theme) -> Dict[int, Texture]:
    return {
        N: create_block_texture("N", width, height, (0, 0, 0, 0)),
        E: create_block_texture("E", width, height, theme.empty),
        D: create_block_texture("D", width, height, theme.block_disable),
        I: create_block_texture("I", width, height, theme.block_i_normal),
        O: create_block_texture("O", width, height, theme.block_o_normal),
        T: create_block_texture("T", width, height, theme.block_t_normal),
        L: create_block_texture("L", width, height, theme.block_l_normal),
        J: create_block_texture("J", width, height, theme.block_j_normal),
        S: create_block_texture("S", width, height, theme.block_s_normal),
        Z: create_block_texture("Z", width, height, theme.block_z_normal),
        IC: create_block_texture("IC", width, height, theme.block_i_clear),
        OC: create_block_texture("OC", width, height, theme.block_o_clear),
        TC: create_block_texture("TC", width, height, theme.block_t_clear),
        LC: create_block_texture("LC", width, height, theme.block_l_clear),
        JC: create_block_texture("JC", width, height, theme.block_j_clear),
        SC: create_block_texture("SC", width, height, theme.block_s_clear),
        ZC: create_block_texture("ZC", width, height, theme.block_z_clear),
    }


def rotate_clockwise(shape: Matrix) -> Matrix:
    result = list()
    for x in range(len(shape[0]) - 1, -1, -1):
        result.append([shape[y][x] for y in range(len(shape))])
    return result
