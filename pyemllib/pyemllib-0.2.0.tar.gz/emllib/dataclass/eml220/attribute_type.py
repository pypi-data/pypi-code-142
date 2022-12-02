from dataclasses import dataclass, field
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDate, XmlPeriod

from emllib.dataclass.eml220.accuracy import Accuracy
from emllib.dataclass.eml220.band_type import BandType
from emllib.dataclass.eml220.cell_geometry_type import CellGeometryType
from emllib.dataclass.eml220.citation_list_type import CitationListType
from emllib.dataclass.eml220.constraint_type import ConstraintType
from emllib.dataclass.eml220.control_point_point_in_pixel import (
    ControlPointPointInPixel,
)
from emllib.dataclass.eml220.corner_point_point_in_pixel import CornerPointPointInPixel
from emllib.dataclass.eml220.data_quality_1 import DataQuality1
from emllib.dataclass.eml220.data_quality_2 import DataQuality2
from emllib.dataclass.eml220.data_table_type_case_sensitive import (
    DataTableTypeCaseSensitive,
)
from emllib.dataclass.eml220.date_time_domain_type import DateTimeDomainType
from emllib.dataclass.eml220.distribution_type import DistributionType
from emllib.dataclass.eml220.geographic_coverage import GeographicCoverage
from emllib.dataclass.eml220.geometry_type import GeometryType
from emllib.dataclass.eml220.i18n_non_empty_string_type import I18NNonEmptyStringType
from emllib.dataclass.eml220.imaging_condition_code import ImagingConditionCode
from emllib.dataclass.eml220.key_type_code import KeyTypeCode
from emllib.dataclass.eml220.license_type import LicenseType
from emllib.dataclass.eml220.maintenance_type import MaintenanceType
from emllib.dataclass.eml220.non_numeric_domain_type import NonNumericDomainType
from emllib.dataclass.eml220.numeric_domain_type import NumericDomainType
from emllib.dataclass.eml220.parameter_type import ParameterType
from emllib.dataclass.eml220.physical_type import PhysicalType
from emllib.dataclass.eml220.procedure_step_type import ProcedureStepType
from emllib.dataclass.eml220.raster_origin_type import RasterOriginType
from emllib.dataclass.eml220.research_project_type import ResearchProjectType
from emllib.dataclass.eml220.responsible_party import ResponsibleParty
from emllib.dataclass.eml220.role_type_value import RoleTypeValue
from emllib.dataclass.eml220.scope_type import ScopeType
from emllib.dataclass.eml220.semantic_annotation import SemanticAnnotation
from emllib.dataclass.eml220.single_date_time_type import CitationType, Coverage
from emllib.dataclass.eml220.spatial_reference_type import SpatialReferenceType
from emllib.dataclass.eml220.text_type import TextType
from emllib.dataclass.eml220.topology_level import TopologyLevel
from emllib.dataclass.eml220.unit_type import UnitType


@dataclass
class AttributeType:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/attribute-2.2.0"

    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    attribute_label: List[str] = field(
        default_factory=list,
        metadata={
            "name": "attributeLabel",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    attribute_definition: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeDefinition",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    storage_type: List["AttributeType.StorageType"] = field(
        default_factory=list,
        metadata={
            "name": "storageType",
            "type": "Element",
            "namespace": "",
        },
    )
    measurement_scale: Optional["AttributeType.MeasurementScale"] = field(
        default=None,
        metadata={
            "name": "measurementScale",
            "type": "Element",
            "namespace": "",
        },
    )
    missing_value_code: List["AttributeType.MissingValueCode"] = field(
        default_factory=list,
        metadata={
            "name": "missingValueCode",
            "type": "Element",
            "namespace": "",
        },
    )
    accuracy: Optional[Accuracy] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    annotation: List[SemanticAnnotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["AttributeType.References"] = field(
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
    class StorageType:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        type_system: str = field(
            default="http://www.w3.org/2001/XMLSchema-datatypes",
            metadata={
                "name": "typeSystem",
                "type": "Attribute",
            },
        )

    @dataclass
    class MeasurementScale:
        nominal: Optional["AttributeType.MeasurementScale.Nominal"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        ordinal: Optional["AttributeType.MeasurementScale.Ordinal"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        interval: Optional["AttributeType.MeasurementScale.Interval"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        ratio: Optional["AttributeType.MeasurementScale.Ratio"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        date_time: Optional["AttributeType.MeasurementScale.DateTime"] = field(
            default=None,
            metadata={
                "name": "dateTime",
                "type": "Element",
                "namespace": "",
            },
        )

        @dataclass
        class Nominal:
            non_numeric_domain: Optional[NonNumericDomainType] = field(
                default=None,
                metadata={
                    "name": "nonNumericDomain",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )

        @dataclass
        class Ordinal:
            non_numeric_domain: Optional[NonNumericDomainType] = field(
                default=None,
                metadata={
                    "name": "nonNumericDomain",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )

        @dataclass
        class Interval:
            unit: Optional[UnitType] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            precision: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            numeric_domain: Optional[NumericDomainType] = field(
                default=None,
                metadata={
                    "name": "numericDomain",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )

        @dataclass
        class Ratio:
            unit: Optional[UnitType] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            precision: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            numeric_domain: Optional[NumericDomainType] = field(
                default=None,
                metadata={
                    "name": "numericDomain",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )

        @dataclass
        class DateTime:
            format_string: Optional[str] = field(
                default=None,
                metadata={
                    "name": "formatString",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            date_time_precision: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dateTimePrecision",
                    "type": "Element",
                    "namespace": "",
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            date_time_domain: Optional[DateTimeDomainType] = field(
                default=None,
                metadata={
                    "name": "dateTimeDomain",
                    "type": "Element",
                    "namespace": "",
                },
            )

    @dataclass
    class MissingValueCode:
        code: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        code_explanation: Optional[str] = field(
            default=None,
            metadata={
                "name": "codeExplanation",
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


@dataclass
class AttributeListType:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/attribute-2.2.0"

    attribute: List[AttributeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["AttributeListType.References"] = field(
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


@dataclass
class DataTableType:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/dataTable-2.2.0"

    alternate_identifier: List["DataTableType.AlternateIdentifier"] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        },
    )
    entity_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    entity_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    physical: List[PhysicalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        },
    )
    annotation: List[SemanticAnnotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    attribute_list: Optional[AttributeListType] = field(
        default=None,
        metadata={
            "name": "attributeList",
            "type": "Element",
            "namespace": "",
        },
    )
    constraint: List[ConstraintType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    case_sensitive: Optional[DataTableTypeCaseSensitive] = field(
        default=None,
        metadata={
            "name": "caseSensitive",
            "type": "Element",
            "namespace": "",
        },
    )
    number_of_records: Optional[str] = field(
        default=None,
        metadata={
            "name": "numberOfRecords",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    references: Optional["DataTableType.References"] = field(
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
    class AlternateIdentifier:
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


@dataclass
class OtherEntityType:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/entity-2.2.0"

    alternate_identifier: List["OtherEntityType.AlternateIdentifier"] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        },
    )
    entity_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    entity_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    physical: List[PhysicalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        },
    )
    annotation: List[SemanticAnnotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    attribute_list: Optional[AttributeListType] = field(
        default=None,
        metadata={
            "name": "attributeList",
            "type": "Element",
            "namespace": "",
        },
    )
    constraint: List[ConstraintType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    entity_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityType",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    references: Optional["OtherEntityType.References"] = field(
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
    class AlternateIdentifier:
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


@dataclass
class SpatialRasterType:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/spatialRaster-2.2.0"

    alternate_identifier: List["SpatialRasterType.AlternateIdentifier"] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        },
    )
    entity_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    entity_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    physical: List[PhysicalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        },
    )
    annotation: List[SemanticAnnotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    attribute_list: Optional[AttributeListType] = field(
        default=None,
        metadata={
            "name": "attributeList",
            "type": "Element",
            "namespace": "",
        },
    )
    constraint: List[ConstraintType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    spatial_reference: Optional[SpatialReferenceType] = field(
        default=None,
        metadata={
            "name": "spatialReference",
            "type": "Element",
            "namespace": "",
        },
    )
    georeference_info: Optional["SpatialRasterType.GeoreferenceInfo"] = field(
        default=None,
        metadata={
            "name": "georeferenceInfo",
            "type": "Element",
            "namespace": "",
        },
    )
    horizontal_accuracy: Optional[DataQuality1] = field(
        default=None,
        metadata={
            "name": "horizontalAccuracy",
            "type": "Element",
            "namespace": "",
        },
    )
    vertical_accuracy: Optional[DataQuality1] = field(
        default=None,
        metadata={
            "name": "verticalAccuracy",
            "type": "Element",
            "namespace": "",
        },
    )
    cell_size_xdirection: Optional[object] = field(
        default=None,
        metadata={
            "name": "cellSizeXDirection",
            "type": "Element",
            "namespace": "",
        },
    )
    cell_size_ydirection: Optional[object] = field(
        default=None,
        metadata={
            "name": "cellSizeYDirection",
            "type": "Element",
            "namespace": "",
        },
    )
    number_of_bands: Optional[object] = field(
        default=None,
        metadata={
            "name": "numberOfBands",
            "type": "Element",
            "namespace": "",
        },
    )
    raster_origin: Optional[RasterOriginType] = field(
        default=None,
        metadata={
            "name": "rasterOrigin",
            "type": "Element",
            "namespace": "",
        },
    )
    rows: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    verticals: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    cell_geometry: Optional[CellGeometryType] = field(
        default=None,
        metadata={
            "name": "cellGeometry",
            "type": "Element",
            "namespace": "",
        },
    )
    tone_gradation: Optional[int] = field(
        default=None,
        metadata={
            "name": "toneGradation",
            "type": "Element",
            "namespace": "",
        },
    )
    scale_factor: Optional[str] = field(
        default=None,
        metadata={
            "name": "scaleFactor",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    offset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    image_description: Optional["SpatialRasterType.ImageDescription"] = field(
        default=None,
        metadata={
            "name": "imageDescription",
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["SpatialRasterType.References"] = field(
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
    class GeoreferenceInfo:
        corner_point: List["SpatialRasterType.GeoreferenceInfo.CornerPoint"] = field(
            default_factory=list,
            metadata={
                "name": "cornerPoint",
                "type": "Element",
                "namespace": "",
                "max_occurs": 4,
            },
        )
        control_point: List["SpatialRasterType.GeoreferenceInfo.ControlPoint"] = field(
            default_factory=list,
            metadata={
                "name": "controlPoint",
                "type": "Element",
                "namespace": "",
            },
        )
        bilinear_fit: Optional["SpatialRasterType.GeoreferenceInfo.BilinearFit"] = field(
            default=None,
            metadata={
                "name": "bilinearFit",
                "type": "Element",
                "namespace": "",
            },
        )

        @dataclass
        class CornerPoint:
            x_coordinate: Optional[float] = field(
                default=None,
                metadata={
                    "name": "xCoordinate",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            y_coordinate: Optional[float] = field(
                default=None,
                metadata={
                    "name": "yCoordinate",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            point_in_pixel: Optional[CornerPointPointInPixel] = field(
                default=None,
                metadata={
                    "name": "pointInPixel",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            corner: Optional[RasterOriginType] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )

        @dataclass
        class ControlPoint:
            column: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            row: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            x_coordinate: Optional[float] = field(
                default=None,
                metadata={
                    "name": "xCoordinate",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            y_coordinate: Optional[float] = field(
                default=None,
                metadata={
                    "name": "yCoordinate",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            point_in_pixel: Optional[ControlPointPointInPixel] = field(
                default=None,
                metadata={
                    "name": "pointInPixel",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )

        @dataclass
        class BilinearFit:
            x_intercept: Optional[float] = field(
                default=None,
                metadata={
                    "name": "xIntercept",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            x_slope: Optional[float] = field(
                default=None,
                metadata={
                    "name": "xSlope",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            y_intercept: Optional[float] = field(
                default=None,
                metadata={
                    "name": "yIntercept",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            y_slope: Optional[float] = field(
                default=None,
                metadata={
                    "name": "ySlope",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )

    @dataclass
    class ImageDescription:
        illumination_elevation_angle: Optional[float] = field(
            default=None,
            metadata={
                "name": "illuminationElevationAngle",
                "type": "Element",
                "namespace": "",
            },
        )
        illumination_azimuth_angle: Optional[float] = field(
            default=None,
            metadata={
                "name": "illuminationAzimuthAngle",
                "type": "Element",
                "namespace": "",
            },
        )
        image_orientation_angle: Optional[float] = field(
            default=None,
            metadata={
                "name": "imageOrientationAngle",
                "type": "Element",
                "namespace": "",
            },
        )
        imaging_condition: Optional[ImagingConditionCode] = field(
            default=None,
            metadata={
                "name": "imagingCondition",
                "type": "Element",
                "namespace": "",
            },
        )
        image_quality_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "imageQualityCode",
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        cloud_cover_percentage: Optional[float] = field(
            default=None,
            metadata={
                "name": "cloudCoverPercentage",
                "type": "Element",
                "namespace": "",
            },
        )
        pre_processing_type_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "preProcessingTypeCode",
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        compression_generation_quality: Optional[int] = field(
            default=None,
            metadata={
                "name": "compressionGenerationQuality",
                "type": "Element",
                "namespace": "",
            },
        )
        triangulation_indicator: Optional[bool] = field(
            default=None,
            metadata={
                "name": "triangulationIndicator",
                "type": "Element",
                "namespace": "",
            },
        )
        radiometric_data_availability: Optional[bool] = field(
            default=None,
            metadata={
                "name": "radiometricDataAvailability",
                "type": "Element",
                "namespace": "",
            },
        )
        camera_calibration_information_availability: Optional[bool] = field(
            default=None,
            metadata={
                "name": "cameraCalibrationInformationAvailability",
                "type": "Element",
                "namespace": "",
            },
        )
        film_distortion_information_availability: Optional[bool] = field(
            default=None,
            metadata={
                "name": "filmDistortionInformationAvailability",
                "type": "Element",
                "namespace": "",
            },
        )
        lens_distortion_information_availability: Optional[bool] = field(
            default=None,
            metadata={
                "name": "lensDistortionInformationAvailability",
                "type": "Element",
                "namespace": "",
            },
        )
        band_description: List[BandType] = field(
            default_factory=list,
            metadata={
                "name": "bandDescription",
                "type": "Element",
                "namespace": "",
            },
        )

    @dataclass
    class AlternateIdentifier:
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


@dataclass
class SpatialVectorType:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/spatialVector-2.2.0"

    alternate_identifier: List["SpatialVectorType.AlternateIdentifier"] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        },
    )
    entity_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    entity_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    physical: List[PhysicalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        },
    )
    annotation: List[SemanticAnnotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    attribute_list: Optional[AttributeListType] = field(
        default=None,
        metadata={
            "name": "attributeList",
            "type": "Element",
            "namespace": "",
        },
    )
    constraint: List[ConstraintType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    geometry: List[GeometryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    geometric_object_count: Optional[str] = field(
        default=None,
        metadata={
            "name": "geometricObjectCount",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    topology_level: Optional[TopologyLevel] = field(
        default=None,
        metadata={
            "name": "topologyLevel",
            "type": "Element",
            "namespace": "",
        },
    )
    spatial_reference: Optional[SpatialReferenceType] = field(
        default=None,
        metadata={
            "name": "spatialReference",
            "type": "Element",
            "namespace": "",
        },
    )
    horizontal_accuracy: Optional[DataQuality2] = field(
        default=None,
        metadata={
            "name": "horizontalAccuracy",
            "type": "Element",
            "namespace": "",
        },
    )
    vertical_accuracy: Optional[DataQuality2] = field(
        default=None,
        metadata={
            "name": "verticalAccuracy",
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["SpatialVectorType.References"] = field(
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
    class AlternateIdentifier:
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


@dataclass
class StoredProcedureType:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/storedProcedure-2.2.0"

    alternate_identifier: List["StoredProcedureType.AlternateIdentifier"] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        },
    )
    entity_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    entity_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    physical: List[PhysicalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        },
    )
    annotation: List[SemanticAnnotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    attribute_list: Optional[AttributeListType] = field(
        default=None,
        metadata={
            "name": "attributeList",
            "type": "Element",
            "namespace": "",
        },
    )
    constraint: List[ConstraintType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    parameter: List[ParameterType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["StoredProcedureType.References"] = field(
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
    class AlternateIdentifier:
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


@dataclass
class ViewType:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/view-2.2.0"

    alternate_identifier: List["ViewType.AlternateIdentifier"] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        },
    )
    entity_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    entity_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    physical: List[PhysicalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        },
    )
    annotation: List[SemanticAnnotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    attribute_list: Optional[AttributeListType] = field(
        default=None,
        metadata={
            "name": "attributeList",
            "type": "Element",
            "namespace": "",
        },
    )
    constraint: List[ConstraintType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    query_statement: Optional[str] = field(
        default=None,
        metadata={
            "name": "queryStatement",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    references: Optional["ViewType.References"] = field(
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
    class AlternateIdentifier:
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


@dataclass
class DatasetType:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/dataset-2.2.0"

    alternate_identifier: List["DatasetType.AlternateIdentifier"] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        },
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    title: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    creator: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    metadata_provider: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "name": "metadataProvider",
            "type": "Element",
            "namespace": "",
        },
    )
    associated_party: List["DatasetType.AssociatedParty"] = field(
        default_factory=list,
        metadata={
            "name": "associatedParty",
            "type": "Element",
            "namespace": "",
        },
    )
    pub_date: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "pubDate",
            "type": "Element",
            "namespace": "",
        },
    )
    language: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    series: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    abstract: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    keyword_set: List["DatasetType.KeywordSet"] = field(
        default_factory=list,
        metadata={
            "name": "keywordSet",
            "type": "Element",
            "namespace": "",
        },
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        },
    )
    intellectual_rights: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "intellectualRights",
            "type": "Element",
            "namespace": "",
        },
    )
    licensed: List[LicenseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    distribution: List[DistributionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    annotation: List[SemanticAnnotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    purpose: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    introduction: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    getting_started: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "gettingStarted",
            "type": "Element",
            "namespace": "",
        },
    )
    acknowledgements: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    maintenance: Optional[MaintenanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    contact: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    publisher: Optional[ResponsibleParty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pub_place: Optional[str] = field(
        default=None,
        metadata={
            "name": "pubPlace",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    project: Optional[ResearchProjectType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_table: List[DataTableType] = field(
        default_factory=list,
        metadata={
            "name": "dataTable",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        },
    )
    spatial_raster: List[SpatialRasterType] = field(
        default_factory=list,
        metadata={
            "name": "spatialRaster",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        },
    )
    spatial_vector: List[SpatialVectorType] = field(
        default_factory=list,
        metadata={
            "name": "spatialVector",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        },
    )
    stored_procedure: List[StoredProcedureType] = field(
        default_factory=list,
        metadata={
            "name": "storedProcedure",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        },
    )
    view: List[ViewType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        },
    )
    other_entity: List[OtherEntityType] = field(
        default_factory=list,
        metadata={
            "name": "otherEntity",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        },
    )
    reference_publication: Optional[CitationType] = field(
        default=None,
        metadata={
            "name": "referencePublication",
            "type": "Element",
            "namespace": "",
        },
    )
    usage_citation: List[CitationType] = field(
        default_factory=list,
        metadata={
            "name": "usageCitation",
            "type": "Element",
            "namespace": "",
        },
    )
    literature_cited: List[CitationListType] = field(
        default_factory=list,
        metadata={
            "name": "literatureCited",
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["DatasetType.References"] = field(
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
    class AlternateIdentifier:
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

    @dataclass
    class AssociatedParty(ResponsibleParty):
        role: Optional[Union[str, RoleTypeValue]] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class KeywordSet:
        keyword: List["DatasetType.KeywordSet.Keyword"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
        keyword_thesaurus: Optional[str] = field(
            default=None,
            metadata={
                "name": "keywordThesaurus",
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )

        @dataclass
        class Keyword(I18NNonEmptyStringType):
            keyword_type: Optional[KeyTypeCode] = field(
                default=None,
                metadata={
                    "name": "keywordType",
                    "type": "Attribute",
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


@dataclass
class MethodsType:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/methods-2.2.0"

    method_step: List["MethodsType.MethodStep"] = field(
        default_factory=list,
        metadata={
            "name": "methodStep",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "sequential": True,
        },
    )
    sampling: List["MethodsType.Sampling"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        },
    )
    quality_control: List[ProcedureStepType] = field(
        default_factory=list,
        metadata={
            "name": "qualityControl",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        },
    )

    @dataclass
    class MethodStep(ProcedureStepType):
        data_source: List[DatasetType] = field(
            default_factory=list,
            metadata={
                "name": "dataSource",
                "type": "Element",
                "namespace": "",
            },
        )

    @dataclass
    class Sampling:
        study_extent: Optional["MethodsType.Sampling.StudyExtent"] = field(
            default=None,
            metadata={
                "name": "studyExtent",
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        sampling_description: Optional[TextType] = field(
            default=None,
            metadata={
                "name": "samplingDescription",
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        spatial_sampling_units: Optional["MethodsType.Sampling.SpatialSamplingUnits"] = field(
            default=None,
            metadata={
                "name": "spatialSamplingUnits",
                "type": "Element",
                "namespace": "",
            },
        )
        citation: List[CitationType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )

        @dataclass
        class StudyExtent:
            coverage: List[Coverage] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            description: List[TextType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

        @dataclass
        class SpatialSamplingUnits:
            referenced_entity_id: List[object] = field(
                default_factory=list,
                metadata={
                    "name": "referencedEntityId",
                    "type": "Element",
                    "namespace": "",
                },
            )
            coverage: List[GeographicCoverage] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
