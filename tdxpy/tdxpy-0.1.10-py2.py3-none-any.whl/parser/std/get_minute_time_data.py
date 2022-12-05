# cython: language_level=3

import struct
from collections import OrderedDict

from tdxpy.helper import get_price
from tdxpy.parser.base import BaseParser


class GetMinuteTimeData(BaseParser):
    def setParams(self, market, code):
        """
        设置参数
        :param market: 市场
        :param code: 代码
        """
        if type(code) is str:
            code = code.encode("utf-8")

        pkg = bytearray.fromhex("0c 1b 08 00 01 01 0e 00 0e 00 1d 05")
        pkg.extend(struct.pack("<H6sI", market, code, 0))

        self.send_pkg = pkg

    def parseResponse(self, body_buf):
        pos = 0

        num, = struct.unpack("<H", body_buf[:2])

        last_price = 0

        pos += 4
        prices = []

        for _ in range(num):
            price_raw, pos = get_price(body_buf, pos)
            reversed1, pos = get_price(body_buf, pos)

            vol, pos = get_price(body_buf, pos)
            last_price = float(last_price + price_raw)

            prices.append(OrderedDict([("price", last_price / 100), ("vol", vol)]))

        return prices
