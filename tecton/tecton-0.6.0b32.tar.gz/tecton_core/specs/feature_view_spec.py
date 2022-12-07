import enum
from typing import Optional
from typing import Tuple
from typing import Union

import attrs
from typeguard import typechecked

from tecton_core import id_helper
from tecton_core.specs import utils
from tecton_proto.common import data_source_type_pb2
from tecton_proto.common import framework_version_pb2
from tecton_proto.data import feature_view_pb2 as feature_view__data_pb2

__all__ = [
    "MaterializedFeatureViewSpec",
    "OnDemandFeatureViewSpec",
    "FeatureTableSpec",
    "MaterializedFeatureViewType",
    "create_feature_view_spec_from_data_proto",
]


@utils.frozen_strict
class FeatureViewSpec:
    """Base class for feature view specs."""

    name: str
    id: str
    join_keys: Tuple[str, ...]
    framework_version: framework_version_pb2.FrameworkVersion.ValueType

    # True if this spec represents an object that was defined locally, as opposed to an "applied" object definition
    # retrieved from the backend.
    is_local_object: bool = attrs.field(metadata={utils.LOCAL_REMOTE_DIVERGENCE_ALLOWED: True})
    workspace: Optional[str] = attrs.field(metadata={utils.LOCAL_REMOTE_DIVERGENCE_ALLOWED: True})


class MaterializedFeatureViewType(enum.Enum):
    TEMPORAL = 1
    TEMPORAL_AGGREGATE = 2


@utils.frozen_strict
class MaterializedFeatureViewSpec(FeatureViewSpec):
    """Spec for Batch and Stream feature views."""

    is_continuous: bool
    type: MaterializedFeatureViewType
    data_source_type: data_source_type_pb2.DataSourceType.ValueType
    incremental_backfills: bool
    timestamp_field: str

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: feature_view__data_pb2.FeatureView) -> "MaterializedFeatureViewSpec":
        if proto.HasField("temporal_aggregate"):
            return cls(
                name=utils.get_field_or_none(proto.fco_metadata, "name"),
                id=id_helper.IdHelper.to_string(proto.feature_view_id),
                join_keys=utils.get_tuple_from_repeated_field(proto.join_keys),
                framework_version=utils.get_field_or_none(proto.fco_metadata, "framework_version"),
                is_local_object=False,
                workspace=utils.get_field_or_none(proto.fco_metadata, "workspace"),
                is_continuous=proto.temporal_aggregate.is_continuous,
                data_source_type=utils.get_field_or_none(proto.temporal_aggregate, "data_source_type"),
                incremental_backfills=False,
                timestamp_field=utils.get_field_or_none(proto, "timestamp_key"),
                type=MaterializedFeatureViewType.TEMPORAL_AGGREGATE,
            )
        elif proto.HasField("temporal"):
            return cls(
                name=utils.get_field_or_none(proto.fco_metadata, "name"),
                id=id_helper.IdHelper.to_string(proto.feature_view_id),
                join_keys=utils.get_tuple_from_repeated_field(proto.join_keys),
                framework_version=utils.get_field_or_none(proto.fco_metadata, "framework_version"),
                is_local_object=False,
                workspace=utils.get_field_or_none(proto.fco_metadata, "workspace"),
                is_continuous=proto.temporal.is_continuous,
                data_source_type=utils.get_field_or_none(proto.temporal, "data_source_type"),
                incremental_backfills=proto.temporal.incremental_backfills,
                timestamp_field=utils.get_field_or_none(proto, "timestamp_key"),
                type=MaterializedFeatureViewType.TEMPORAL,
            )
        else:
            raise TypeError(f"Unexpected feature view type: {proto}")


@utils.frozen_strict
class OnDemandFeatureViewSpec(FeatureViewSpec):
    @classmethod
    @typechecked
    def from_data_proto(cls, proto: feature_view__data_pb2.FeatureView) -> "OnDemandFeatureViewSpec":
        return cls(
            name=utils.get_field_or_none(proto.fco_metadata, "name"),
            id=id_helper.IdHelper.to_string(proto.feature_view_id),
            join_keys=utils.get_tuple_from_repeated_field(proto.join_keys),
            framework_version=utils.get_field_or_none(proto.fco_metadata, "framework_version"),
            is_local_object=False,
            workspace=utils.get_field_or_none(proto.fco_metadata, "workspace"),
        )


@utils.frozen_strict
class FeatureTableSpec(FeatureViewSpec):
    timestamp_field: str

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: feature_view__data_pb2.FeatureView) -> "FeatureTableSpec":
        return cls(
            name=utils.get_field_or_none(proto.fco_metadata, "name"),
            id=id_helper.IdHelper.to_string(proto.feature_view_id),
            join_keys=utils.get_tuple_from_repeated_field(proto.join_keys),
            framework_version=utils.get_field_or_none(proto.fco_metadata, "framework_version"),
            is_local_object=False,
            workspace=utils.get_field_or_none(proto.fco_metadata, "workspace"),
            timestamp_field=utils.get_field_or_none(proto, "timestamp_key"),
        )


@typechecked
def create_feature_view_spec_from_data_proto(
    proto: feature_view__data_pb2.FeatureView,
) -> Optional[Union[MaterializedFeatureViewSpec, OnDemandFeatureViewSpec, FeatureTableSpec]]:
    if proto.HasField("temporal_aggregate") or proto.HasField("temporal"):
        return MaterializedFeatureViewSpec.from_data_proto(proto)
    elif proto.HasField("on_demand_feature_view"):
        return OnDemandFeatureViewSpec.from_data_proto(proto)
    elif proto.HasField("feature_table"):
        return FeatureTableSpec.from_data_proto(proto)
    else:
        raise ValueError(f"Unexpect feature view type: {proto}")
