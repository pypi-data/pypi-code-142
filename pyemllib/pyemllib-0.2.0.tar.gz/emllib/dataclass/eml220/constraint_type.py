from dataclasses import dataclass, field
from typing import List, Optional, Union

from emllib.dataclass.eml220.cardinality_child_occurances_type_value import (
    CardinalityChildOccurancesTypeValue,
)
from emllib.dataclass.eml220.cardinality_parent_occurences import (
    CardinalityParentOccurences,
)
from emllib.dataclass.eml220.foreign_key_group_relationship_type import (
    ForeignKeyGroupRelationshipType,
)
from emllib.dataclass.eml220.scope_type import ScopeType

__NAMESPACE__ = "https://eml.ecoinformatics.org/constraint-2.2.0"


@dataclass
class ConstraintType:
    primary_key: Optional["ConstraintType.PrimaryKey"] = field(
        default=None,
        metadata={
            "name": "primaryKey",
            "type": "Element",
            "namespace": "",
        },
    )
    unique_key: Optional["ConstraintType.UniqueKey"] = field(
        default=None,
        metadata={
            "name": "uniqueKey",
            "type": "Element",
            "namespace": "",
        },
    )
    check_constraint: Optional["ConstraintType.CheckConstraint"] = field(
        default=None,
        metadata={
            "name": "checkConstraint",
            "type": "Element",
            "namespace": "",
        },
    )
    foreign_key: Optional["ConstraintType.ForeignKey"] = field(
        default=None,
        metadata={
            "name": "foreignKey",
            "type": "Element",
            "namespace": "",
        },
    )
    join_condition: Optional["ConstraintType.JoinCondition"] = field(
        default=None,
        metadata={
            "name": "joinCondition",
            "type": "Element",
            "namespace": "",
        },
    )
    not_null_constraint: Optional["ConstraintType.NotNullConstraint"] = field(
        default=None,
        metadata={
            "name": "notNullConstraint",
            "type": "Element",
            "namespace": "",
        },
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class PrimaryKey:
        constraint_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "constraintName",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        constraint_description: Optional[object] = field(
            default=None,
            metadata={
                "name": "constraintDescription",
                "type": "Element",
                "namespace": "",
            },
        )
        key: Optional["ConstraintType.PrimaryKey.Key"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )

        @dataclass
        class Key:
            attribute_reference: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "attributeReference",
                    "type": "Element",
                    "namespace": "",
                    "min_occurs": 1,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )

    @dataclass
    class UniqueKey:
        constraint_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "constraintName",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        constraint_description: Optional[object] = field(
            default=None,
            metadata={
                "name": "constraintDescription",
                "type": "Element",
                "namespace": "",
            },
        )
        key: Optional["ConstraintType.UniqueKey.Key"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )

        @dataclass
        class Key:
            attribute_reference: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "attributeReference",
                    "type": "Element",
                    "namespace": "",
                    "min_occurs": 1,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )

    @dataclass
    class CheckConstraint:
        constraint_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "constraintName",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        constraint_description: Optional[object] = field(
            default=None,
            metadata={
                "name": "constraintDescription",
                "type": "Element",
                "namespace": "",
            },
        )
        check_condition: Optional[str] = field(
            default=None,
            metadata={
                "name": "checkCondition",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        language: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ForeignKey:
        constraint_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "constraintName",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        constraint_description: Optional[object] = field(
            default=None,
            metadata={
                "name": "constraintDescription",
                "type": "Element",
                "namespace": "",
            },
        )
        key: Optional["ConstraintType.ForeignKey.Key"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        entity_reference: Optional[str] = field(
            default=None,
            metadata={
                "name": "entityReference",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        relationship_type: Optional[ForeignKeyGroupRelationshipType] = field(
            default=None,
            metadata={
                "name": "relationshipType",
                "type": "Element",
                "namespace": "",
            },
        )
        cardinality: Optional["ConstraintType.ForeignKey.Cardinality"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )

        @dataclass
        class Key:
            attribute_reference: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "attributeReference",
                    "type": "Element",
                    "namespace": "",
                    "min_occurs": 1,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )

        @dataclass
        class Cardinality:
            parent_occurences: Optional[CardinalityParentOccurences] = field(
                default=None,
                metadata={
                    "name": "parentOccurences",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            child_occurences: Optional[Union[int, CardinalityChildOccurancesTypeValue]] = field(
                default=None,
                metadata={
                    "name": "childOccurences",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )

    @dataclass
    class JoinCondition:
        constraint_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "constraintName",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        constraint_description: Optional[object] = field(
            default=None,
            metadata={
                "name": "constraintDescription",
                "type": "Element",
                "namespace": "",
            },
        )
        key: Optional["ConstraintType.JoinCondition.Key"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        entity_reference: Optional[str] = field(
            default=None,
            metadata={
                "name": "entityReference",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        relationship_type: Optional[ForeignKeyGroupRelationshipType] = field(
            default=None,
            metadata={
                "name": "relationshipType",
                "type": "Element",
                "namespace": "",
            },
        )
        cardinality: Optional["ConstraintType.JoinCondition.Cardinality"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        referenced_key: Optional["ConstraintType.JoinCondition.ReferencedKey"] = field(
            default=None,
            metadata={
                "name": "referencedKey",
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )

        @dataclass
        class ReferencedKey:
            attribute_reference: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "attributeReference",
                    "type": "Element",
                    "namespace": "",
                    "min_occurs": 1,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )

        @dataclass
        class Key:
            attribute_reference: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "attributeReference",
                    "type": "Element",
                    "namespace": "",
                    "min_occurs": 1,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )

        @dataclass
        class Cardinality:
            parent_occurences: Optional[CardinalityParentOccurences] = field(
                default=None,
                metadata={
                    "name": "parentOccurences",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            child_occurences: Optional[Union[int, CardinalityChildOccurancesTypeValue]] = field(
                default=None,
                metadata={
                    "name": "childOccurences",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )

    @dataclass
    class NotNullConstraint:
        constraint_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "constraintName",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        constraint_description: Optional[object] = field(
            default=None,
            metadata={
                "name": "constraintDescription",
                "type": "Element",
                "namespace": "",
            },
        )
        key: Optional["ConstraintType.NotNullConstraint.Key"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )

        @dataclass
        class Key:
            attribute_reference: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "attributeReference",
                    "type": "Element",
                    "namespace": "",
                    "min_occurs": 1,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
