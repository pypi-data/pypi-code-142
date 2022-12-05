# cython: language_level=3

import struct
from pathlib import Path

from tdxpy.constants import SECURITY_COEFFICIENT
from tdxpy.logger import logger


def get_price(data, pos):
    """
    分析了一下，貌似是类似utf-8的编码方式保存有符号数字

    :param data:
    :param pos:
    :return:
    """

    pos_byte = 6

    bdata = index_bytes(data, pos)
    int_data = bdata & 0x3F

    if bdata & 0x40:
        sign = True
    else:
        sign = False

    if bdata & 0x80:
        while True:
            pos += 1

            bdata = index_bytes(data, pos)

            int_data += (bdata & 0x7F) << pos_byte
            pos_byte += 7

            if bdata & 0x80:
                pass
            else:
                break

    pos += 1

    if sign:
        int_data = -int_data

    return int_data, pos


def get_volume(vol):
    """
    获取交易量
    :param vol:
    :return:
    """
    logpoint = vol >> (8 * 3)

    hleax = (vol >> (8 * 2)) & 0xFF  # [2]
    lheax = (vol >> 8) & 0xFF  # [1]
    lleax = vol & 0xFF  # [0]

    dw_ecx = logpoint * 2 - 0x7F
    dw_edx = logpoint * 2 - 0x86

    dw_esi = logpoint * 2 - 0x8E
    dw_eax = logpoint * 2 - 0x96

    if dw_ecx < 0:
        tmp_eax = -dw_ecx
    else:
        tmp_eax = dw_ecx

    dbl_xmm6 = pow(2.0, tmp_eax)

    if dw_ecx < 0:
        dbl_xmm6 = 1.0 / dbl_xmm6

    if hleax > 0x80:
        dwtmpeax = dw_edx + 1
        tmpdbl_xmm3 = pow(2.0, dwtmpeax)

        dbl_xmm0 = pow(2.0, dw_edx) * 128.0
        dbl_xmm0 += (hleax & 0x7F) * tmpdbl_xmm3
        dbl_xmm4 = dbl_xmm0

    else:
        if dw_edx >= 0:
            dbl_xmm0 = pow(2.0, dw_edx) * hleax
        else:
            dbl_xmm0 = (1 / pow(2.0, dw_edx)) * hleax

        dbl_xmm4 = dbl_xmm0

    dbl_xmm3 = pow(2.0, dw_esi) * lheax
    dbl_xmm1 = pow(2.0, dw_eax) * lleax

    if hleax & 0x80:
        dbl_xmm3 *= 2.0
        dbl_xmm1 *= 2.0

    dbl_ret = dbl_xmm6 + dbl_xmm4 + dbl_xmm3 + dbl_xmm1

    return dbl_ret


def get_datetime(category, buffer, pos):
    """
    获取日期时间
    :param category:
    :param buffer:
    :param pos:
    :return:
    """
    minute = 0
    hour = 15

    if category < 4 or category == 7 or category == 8:
        zip_day, minutes = struct.unpack("<HH", buffer[pos: pos + 4])

        month = int((zip_day % 2048) / 100)
        year = (zip_day >> 11) + 2004
        day = (zip_day % 2048) % 100

        minute = minutes % 60
        hour = int(minutes / 60)
    else:
        zip_day, = struct.unpack("<I", buffer[pos: pos + 4])

        month = int((zip_day % 10000) / 100)
        year = int(zip_day / 10000)
        day = zip_day % 100

    pos += 4

    return year, month, day, hour, minute, pos


def get_time(buffer, pos):
    """
    获取时间
    :param buffer:
    :param pos:
    :return:
    """
    minutes, = struct.unpack("<H", buffer[pos: pos + 2])

    hour = int(minutes / 60)
    minute = minutes % 60

    pos += 2

    return hour, minute, pos


def index_bytes(data, pos):
    """
    索引比特
    :param data:
    :param pos:
    :return:
    """
    return data[pos]


def get_security_coefficient(market, name):
    return SECURITY_COEFFICIENT[get_security_type(market, name)]


def get_security_type(market, code):
    """
    获取股票类型, A股, B股, 指数等

    :param market: 市场
    :param code: 代码
    :return:
    """
    code = Path(code).stem
    code_head = code[:2]

    if market in ['SZ', 0]:
        if code_head in ["00", "30"]:
            return "SZ_A_STOCK"

        if code_head in ["20"]:
            return "SZ_B_STOCK"

        if code_head in ["39"]:
            return "SZ_INDEX"

        if code_head in ["15", "16"]:
            return "SZ_FUND"

        if code_head in ["10", "11", "12", "13", "14"]:
            return "SZ_BOND"

    if market in ['SH', 1]:
        if code_head in ["60", "68"]:  # 688XXX科创板
            return "SH_A_STOCK"

        if code_head in ["90"]:
            return "SH_B_STOCK"

        if code_head in ["00", "88", "99"]:
            return "SH_INDEX"

        if code_head in ["50", "51"]:
            return "SH_FUND"

        if code_head in ["01", "10", "11", "12", "13", "14", "20"]:
            return "SH_BOND"

    logger.debug("Unknown security exchange !")
    raise NotImplementedError


def dump(buf):
    from pprint import pprint

    try:
        from hexdump import hexdump
        pprint(hexdump(buf))
    except ImportError:
        pprint(buf)
