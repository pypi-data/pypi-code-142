from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.binary_raster_format_row_column_orientation import (
    BinaryRasterFormatRowColumnOrientation,
)
from emllib.dataclass.eml220.physical_distribution_type import PhysicalDistributionType
from emllib.dataclass.eml220.scope_type import ScopeType
from emllib.dataclass.eml220.simple_delimited_collapse_delimiters import (
    SimpleDelimitedCollapseDelimiters,
)
from emllib.dataclass.eml220.single_date_time_type import CitationType
from emllib.dataclass.eml220.text_delimited_collapse_delimiters import (
    TextDelimitedCollapseDelimiters,
)
from emllib.dataclass.eml220.text_format_attribute_orientation import (
    TextFormatAttributeOrientation,
)

__NAMESPACE__ = "https://eml.ecoinformatics.org/physical-2.2.0"


@dataclass
class PhysicalType:
    object_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "objectName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    size: Optional["PhysicalType.Size"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    authentication: List["PhysicalType.Authentication"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    compression_method: List[str] = field(
        default_factory=list,
        metadata={
            "name": "compressionMethod",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
            "sequential": True,
        },
    )
    encoding_method: List[str] = field(
        default_factory=list,
        metadata={
            "name": "encodingMethod",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
            "sequential": True,
        },
    )
    character_encoding: Optional[str] = field(
        default=None,
        metadata={
            "name": "characterEncoding",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    data_format: Optional["PhysicalType.DataFormat"] = field(
        default=None,
        metadata={
            "name": "dataFormat",
            "type": "Element",
            "namespace": "",
        },
    )
    distribution: List[PhysicalDistributionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["PhysicalType.References"] = field(
        default=None,
        metadata={
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
    class Size:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        unit: str = field(
            default="byte",
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Authentication:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        method: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class DataFormat:
        text_format: Optional["PhysicalType.DataFormat.TextFormat"] = field(
            default=None,
            metadata={
                "name": "textFormat",
                "type": "Element",
                "namespace": "",
            },
        )
        externally_defined_format: Optional["PhysicalType.DataFormat.ExternallyDefinedFormat"] = field(
            default=None,
            metadata={
                "name": "externallyDefinedFormat",
                "type": "Element",
                "namespace": "",
            },
        )
        binary_raster_format: Optional["PhysicalType.DataFormat.BinaryRasterFormat"] = field(
            default=None,
            metadata={
                "name": "binaryRasterFormat",
                "type": "Element",
                "namespace": "",
            },
        )

        @dataclass
        class TextFormat:
            num_header_lines: Optional[int] = field(
                default=None,
                metadata={
                    "name": "numHeaderLines",
                    "type": "Element",
                    "namespace": "",
                },
            )
            num_footer_lines: Optional[int] = field(
                default=None,
                metadata={
                    "name": "numFooterLines",
                    "type": "Element",
                    "namespace": "",
                },
            )
            record_delimiter: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "recordDelimiter",
                    "type": "Element",
                    "namespace": "",
                },
            )
            physical_line_delimiter: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "physicalLineDelimiter",
                    "type": "Element",
                    "namespace": "",
                },
            )
            num_physical_lines_per_record: Optional[int] = field(
                default=None,
                metadata={
                    "name": "numPhysicalLinesPerRecord",
                    "type": "Element",
                    "namespace": "",
                },
            )
            max_record_length: Optional[int] = field(
                default=None,
                metadata={
                    "name": "maxRecordLength",
                    "type": "Element",
                    "namespace": "",
                },
            )
            attribute_orientation: Optional[TextFormatAttributeOrientation] = field(
                default=None,
                metadata={
                    "name": "attributeOrientation",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            simple_delimited: Optional["PhysicalType.DataFormat.TextFormat.SimpleDelimited"] = field(
                default=None,
                metadata={
                    "name": "simpleDelimited",
                    "type": "Element",
                    "namespace": "",
                },
            )
            complex: Optional["PhysicalType.DataFormat.TextFormat.Complex"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass
            class SimpleDelimited:
                field_delimiter: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "fieldDelimiter",
                        "type": "Element",
                        "namespace": "",
                        "min_occurs": 1,
                    },
                )
                collapse_delimiters: Optional[SimpleDelimitedCollapseDelimiters] = field(
                    default=None,
                    metadata={
                        "name": "collapseDelimiters",
                        "type": "Element",
                        "namespace": "",
                    },
                )
                quote_character: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "quoteCharacter",
                        "type": "Element",
                        "namespace": "",
                        "min_length": 1,
                        "pattern": r"[\s]*[\S][\s\S]*",
                    },
                )
                literal_character: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "literalCharacter",
                        "type": "Element",
                        "namespace": "",
                        "min_length": 1,
                        "pattern": r"[\s]*[\S][\s\S]*",
                    },
                )

            @dataclass
            class Complex:
                text_fixed: List["PhysicalType.DataFormat.TextFormat.Complex.TextFixed"] = field(
                    default_factory=list,
                    metadata={
                        "name": "textFixed",
                        "type": "Element",
                        "namespace": "",
                    },
                )
                text_delimited: List["PhysicalType.DataFormat.TextFormat.Complex.TextDelimited"] = field(
                    default_factory=list,
                    metadata={
                        "name": "textDelimited",
                        "type": "Element",
                        "namespace": "",
                    },
                )

                @dataclass
                class TextFixed:
                    field_width: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "fieldWidth",
                            "type": "Element",
                            "namespace": "",
                            "required": True,
                        },
                    )
                    line_number: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "lineNumber",
                            "type": "Element",
                            "namespace": "",
                        },
                    )
                    field_start_column: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "fieldStartColumn",
                            "type": "Element",
                            "namespace": "",
                        },
                    )

                @dataclass
                class TextDelimited:
                    field_delimiter: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "fieldDelimiter",
                            "type": "Element",
                            "namespace": "",
                            "required": True,
                        },
                    )
                    collapse_delimiters: Optional[TextDelimitedCollapseDelimiters] = field(
                        default=None,
                        metadata={
                            "name": "collapseDelimiters",
                            "type": "Element",
                            "namespace": "",
                        },
                    )
                    line_number: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "lineNumber",
                            "type": "Element",
                            "namespace": "",
                        },
                    )
                    quote_character: List[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "quoteCharacter",
                            "type": "Element",
                            "namespace": "",
                            "min_length": 1,
                            "pattern": r"[\s]*[\S][\s\S]*",
                        },
                    )
                    literal_character: List[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "literalCharacter",
                            "type": "Element",
                            "namespace": "",
                            "min_length": 1,
                            "pattern": r"[\s]*[\S][\s\S]*",
                        },
                    )

        @dataclass
        class ExternallyDefinedFormat:
            format_name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "formatName",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            format_version: Optional[str] = field(
                default=None,
                metadata={
                    "name": "formatVersion",
                    "type": "Element",
                    "namespace": "",
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            citation: Optional[CitationType] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

        @dataclass
        class BinaryRasterFormat:
            row_column_orientation: Optional[BinaryRasterFormatRowColumnOrientation] = field(
                default=None,
                metadata={
                    "name": "rowColumnOrientation",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            multi_band: Optional["PhysicalType.DataFormat.BinaryRasterFormat.MultiBand"] = field(
                default=None,
                metadata={
                    "name": "multiBand",
                    "type": "Element",
                    "namespace": "",
                },
            )
            nbits: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            byteorder: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            skipbytes: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            bandrowbytes: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            totalrowbytes: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            bandgapbytes: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )

            @dataclass
            class MultiBand:
                nbands: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                    },
                )
                layout: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                        "min_length": 1,
                        "pattern": r"[\s]*[\S][\s\S]*",
                    },
                )

    @dataclass
    class References:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        system: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Attribute",
                "tokens": True,
            },
        )
