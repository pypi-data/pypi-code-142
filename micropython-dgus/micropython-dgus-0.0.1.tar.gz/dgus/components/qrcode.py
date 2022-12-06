# TFT components
# Copyright (c) 2022 Petr Kracik
# Copyright (c) 2022 OctopusLAB

from . import Component
from ..types.string import String


class QRCode(Component):
    SP_OFFSET_UNIT_PIXELS = 0x03
    SP_OFFSET_FIX_MODE = 0x05


    def __init__(self, dgus, sp_address, vp_address = None):
        super().__init__(dgus, sp_address, String, vp_address)


    @property
    def unit_pixels(self):
        return self._dgus.read_vp_int16(self._sp + self.SP_OFFSET_UNIT_PIXELS)


    @unit_pixels.setter
    def unit_pixels(self, value):
        self._dgus.write_vp_int16(self._sp + self.SP_OFFSET_UNIT_PIXELS, value)


    @property
    def fix_mode(self):
        return self._dgus.read_vp_int16(self._sp + self.SP_OFFSET_FIX_MODE)


    @fix_mode.setter
    def fix_mode(self, value):
        self._dgus.write_vp_int16(self._sp + self.SP_OFFSET_FIX_MODE, value)
