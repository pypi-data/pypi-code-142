from dataclasses import dataclass, field
from typing import Optional

from emllib.dataclass.eml220.length_units import LengthUnits

__NAMESPACE__ = "https://eml.ecoinformatics.org/spatialRaster-2.2.0"


@dataclass
class BandType:
    sequence_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "sequenceIdentifier",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    high_wavelength: Optional[float] = field(
        default=None,
        metadata={
            "name": "highWavelength",
            "type": "Element",
            "namespace": "",
        },
    )
    low_wave_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "lowWaveLength",
            "type": "Element",
            "namespace": "",
        },
    )
    wave_length_units: Optional[LengthUnits] = field(
        default=None,
        metadata={
            "name": "waveLengthUnits",
            "type": "Element",
            "namespace": "",
        },
    )
    peak_response: Optional[object] = field(
        default=None,
        metadata={
            "name": "peakResponse",
            "type": "Element",
            "namespace": "",
        },
    )
