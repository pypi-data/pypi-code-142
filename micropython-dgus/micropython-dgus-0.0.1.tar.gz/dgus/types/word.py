# TFT components
# Copyright (c) 2022 Petr Kracik
# Copyright (c) 2022 OctopusLAB

from . import Type

class Word(Type):
    @property
    def value(self):
        return self._dgus.read_vp(self._vp)


    @value.setter
    def value(self, value):
        self._dgus.write_vp(self._vp, value)


    def _on_change(self, data):
        for f in self._on_change_events:
            f(self, data)
