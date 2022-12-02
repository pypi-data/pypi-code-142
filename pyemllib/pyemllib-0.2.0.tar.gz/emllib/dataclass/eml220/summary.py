from dataclasses import dataclass, field

__NAMESPACE__ = "https://eml.ecoinformatics.org/documentation-2.2.0"


@dataclass
class Summary:
    class Meta:
        name = "summary"
        namespace = "https://eml.ecoinformatics.org/documentation-2.2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
