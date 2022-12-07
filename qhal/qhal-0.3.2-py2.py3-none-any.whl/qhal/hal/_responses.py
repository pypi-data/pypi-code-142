"""
QHAL responses, with one base class for measurements
"""
from abc import ABC, abstractmethod
from enum import Enum

from numpy import uint64

#pylint: disable=too-few-public-methods
class QHALResponse(ABC):
    """Abstract base class for a HAL reponse."""
    @abstractmethod
    def to_binary(self) -> uint64:
        """Convert QHALResponse to binary"""

class QHALMeasurement(QHALResponse):
    """QHALResponse
    """

    class Shifts(Enum):
        """
        Defines the position of the HAL measurement subfields.
        """
        QIDX = 52
        OFFSET = 12
        STATUS = 7
        VALUE = 0

    def __init__(self,
                 qidx: int,
                 offset: int = 0,
                 status: int = 0,
                 value: int = 0):
        self._qidx = qidx
        self._offset = offset
        self._status = status
        self._value = value

    def to_binary(self) -> uint64:
        """Get binary of QHALMeasurement"""
        return (self._qidx << self.Shifts.QIDX |
                self._offset << self.Shifts.OFFSET |
                self._status << self.Shifts.STATUS |
                self._value << self.Shifts.VALUE)

    @classmethod
    def from_binary(cls, bits: uint64) -> "QHALMeasurement":
        """Create QHALMeasurement from binary
        """
        qidx = (bits >> cls.Shifts.QIDX)
        offset = (bits >> cls.Shifts.OFFSET) & (
            (1 << cls.Shifts.QIDX-cls.Shifts.OFFSET)-1)
        status = (bits >> cls.Shifts.STATUS) & (
            (1 << cls.Shifts.OFFSET-cls.Shifts.STATUS)-1)
        value = bits & 1
        return QHALMeasurement(qidx, offset, status, value)
