# TFT components
# Copyright (c) 2022 Petr Kracik
# Copyright (c) 2022 OctopusLAB

from . import Type

class String(Type):
    @property
    def value(self):
        pass


    @value.setter
    def value(self, value):
        val = value.encode()

        if len(val) % 2 != 0:
            val += b'\xff'

        val += b'\xff\xff'

        self._dgus.write_vp(self._vp, val)
