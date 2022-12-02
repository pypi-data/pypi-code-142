from dataclasses import dataclass, field
from typing import Optional

from emllib.dataclass.eml220.text_type import TextType

__NAMESPACE__ = "https://eml.ecoinformatics.org/documentation-2.2.0"


@dataclass
class ModuleDocs:
    class Meta:
        name = "moduleDocs"
        namespace = "https://eml.ecoinformatics.org/documentation-2.2.0"

    module_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "moduleName",
            "type": "Element",
            "required": True,
        },
    )
    module_description: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "moduleDescription",
            "type": "Element",
            "required": True,
        },
    )
    recommended_usage: Optional[str] = field(
        default=None,
        metadata={
            "name": "recommendedUsage",
            "type": "Element",
            "required": True,
        },
    )
    stand_alone: Optional[str] = field(
        default=None,
        metadata={
            "name": "standAlone",
            "type": "Element",
            "required": True,
        },
    )
