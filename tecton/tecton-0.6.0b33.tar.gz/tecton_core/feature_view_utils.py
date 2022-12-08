from typing import List

from google.protobuf import duration_pb2
from typeguard import typechecked

from tecton_core.time_utils import to_human_readable_str
from tecton_proto.common.schema_pb2 import Schema as SchemaProto
from tecton_proto.data.feature_store_pb2 import FeatureStoreFormatVersion

CONTINUOUS_MODE_BATCH_INTERVAL = duration_pb2.Duration(seconds=86400)


def get_input_feature_columns(view_schema: SchemaProto, join_keys: List[str], timestamp_key: str) -> List[str]:
    column_names = (c.name for c in view_schema.columns)
    return [c for c in column_names if c not in join_keys and c != timestamp_key]


def validate_version(version):
    assert (
        version >= FeatureStoreFormatVersion.FEATURE_STORE_FORMAT_VERSION_DEFAULT
        or version <= FeatureStoreFormatVersion.FEATURE_STORE_FORMAT_VERSION_MAX
    )


@typechecked
def construct_aggregation_output_feature_name(
    column: str,
    function: str,
    window: duration_pb2.Duration,
    aggregation_interval: duration_pb2.Duration,
    is_continuous: bool,
):
    window_name = to_human_readable_str(window)
    if is_continuous:
        aggregation_interval_name = "continuous"
    else:
        aggregation_interval_name = to_human_readable_str(aggregation_interval)
    return f"{column}_{function}_{window_name}_{aggregation_interval_name}".replace(" ", "")
