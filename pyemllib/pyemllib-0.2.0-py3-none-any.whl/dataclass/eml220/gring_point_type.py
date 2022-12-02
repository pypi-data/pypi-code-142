from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "https://eml.ecoinformatics.org/coverage-2.2.0"


@dataclass
class GringPointType:
    class Meta:
        name = "GRingPointType"

    g_ring_latitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "gRingLatitude",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("-90.0"),
            "max_inclusive": Decimal("90.0"),
        },
    )
    g_ring_longitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "gRingLongitude",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("-180.0"),
            "max_inclusive": Decimal("180.0"),
        },
    )
