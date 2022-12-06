# Return Key Code component
# Copyright (c) 2022 Petr Kracik
# Copyright (c) 2022 OctopusLAB

from . import Component
from ..types.word import Word


class ReturnKeyCode(Component):
    CAPS_LOCK_KEYCODE = b'\x00\xF4'

    def __init__(self, dgus, vp_address):
        super().__init__(dgus, None, Word, vp_address)
        self.element.event_on_change_add(self._on_change)
        self._on_key_press_events = list()
        self._capslock = False


    def _on_change(self, comp, data):
        if data == self.CAPS_LOCK_KEYCODE:
            self._capslock = not self._capslock

        self._on_key_press(data[0] if self._capslock else data[1])


    def _on_key_press(self, val):
        for f in self._on_key_press_events:
            f(self, val)


    def event_on_key_press_add(self, function):
        self._on_key_press_events.append(function)


    def event_on_key_press_remove(self, function):
        if function in self._on_key_press_events:
            self._on_key_press_events.remove(function)
