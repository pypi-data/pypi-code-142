from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "https://eml.ecoinformatics.org/attribute-2.2.0"


@dataclass
class Accuracy:
    attribute_accuracy_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeAccuracyReport",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    quantitative_attribute_accuracy_assessment: List["Accuracy.QuantitativeAttributeAccuracyAssessment"] = field(
        default_factory=list,
        metadata={
            "name": "quantitativeAttributeAccuracyAssessment",
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class QuantitativeAttributeAccuracyAssessment:
        attribute_accuracy_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "attributeAccuracyValue",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        attribute_accuracy_explanation: Optional[str] = field(
            default=None,
            metadata={
                "name": "attributeAccuracyExplanation",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
