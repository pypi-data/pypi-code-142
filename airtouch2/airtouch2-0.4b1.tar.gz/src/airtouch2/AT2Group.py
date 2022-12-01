from __future__ import annotations
from itertools import compress
from typing import TYPE_CHECKING
from airtouch2.protocol.messages import ResponseMessage

from airtouch2.protocol.messages import ChangeDamper, ToggleGroup
if TYPE_CHECKING:
    from airtouch2.AT2Client import AT2Client
import logging


_LOGGER = logging.getLogger(__name__)

class AT2Group:
    def __init__(self, client: AT2Client, number: int, response: ResponseMessage):
        self._client = client
        self.number = number
        self.update(response)

    def update(self, response: ResponseMessage):
        self.name = response.group_names[self.number]
        # 0 to 10 steps of 10%
        self.damp = response.group_damps[self.number]
        self.on = response.group_ons[self.number]
        self.spill = response.group_spills[self.number]
        self.turbo = True if response.turbo_group == self.number else False

    def inc_dec_damp(self, inc: bool):
        self._client.send_command(ChangeDamper(self.number, inc))

    def set_damp(self, new_damp: int):
        # Set to 0 is equivalent to turning off
        if new_damp < 0 or new_damp > 10:
            raise ValueError("Dampers can only be set from 0 to 10")
        damp_diff = new_damp - self.damp
        inc = damp_diff > 0
        for i in range(abs(damp_diff)):
            self.inc_dec_damp(inc)

    def _turn_on_off(self, on: bool):
        if self.on != on:
            self._client.send_command(ToggleGroup(self.number))

    def turn_off(self):
        self._turn_on_off(False)

    def turn_on(self):
        self._turn_on_off(True)

    def get_status_strings(self):
        flags = [self.spill, self.turbo]
        flag_names = ['SPILL', 'TURBO']
        statuses = list(compress(flag_names, flags))
        if not statuses:
            statuses.append('NORMAL')
        return statuses

    def __str__(self):
        return f"""
        Group Name:\t{self.name}
        Group Number:\t{self.number}
        On:\t\t{self.on}
        Status:\t\t{self.get_status_strings()}
        Damper:\t\t{f'{self.damp*10}%'}
        """