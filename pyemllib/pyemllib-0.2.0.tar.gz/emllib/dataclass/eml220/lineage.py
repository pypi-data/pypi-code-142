from dataclasses import dataclass, field

__NAMESPACE__ = "https://eml.ecoinformatics.org/documentation-2.2.0"


@dataclass
class Lineage:
    class Meta:
        name = "lineage"
        namespace = "https://eml.ecoinformatics.org/documentation-2.2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
