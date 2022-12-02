from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from emllib.dataclass.eml220.maint_up_freq_type import MaintUpFreqType
from emllib.dataclass.eml220.text_type import TextType

__NAMESPACE__ = "https://eml.ecoinformatics.org/dataset-2.2.0"


@dataclass
class MaintenanceType:
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    maintenance_update_frequency: Optional[MaintUpFreqType] = field(
        default=None,
        metadata={
            "name": "maintenanceUpdateFrequency",
            "type": "Element",
            "namespace": "",
        },
    )
    change_history: List["MaintenanceType.ChangeHistory"] = field(
        default_factory=list,
        metadata={
            "name": "changeHistory",
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class ChangeHistory:
        change_scope: Optional[str] = field(
            default=None,
            metadata={
                "name": "changeScope",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        old_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "oldValue",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        change_date: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "changeDate",
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        comment: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
