from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "https://eml.ecoinformatics.org/spatialRaster-2.2.0"


@dataclass
class DataQuality1:
    class Meta:
        name = "DataQuality"

    accuracy_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "accuracyReport",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    quantitative_accuracy_report: List["DataQuality1.QuantitativeAccuracyReport"] = field(
        default_factory=list,
        metadata={
            "name": "quantitativeAccuracyReport",
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class QuantitativeAccuracyReport:
        quantitative_accuracy_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "quantitativeAccuracyValue",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        quantitative_accuracy_method: Optional[str] = field(
            default=None,
            metadata={
                "name": "quantitativeAccuracyMethod",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
