from typing import List

import pyspark.sql.functions as F
import pyspark.sql.window as spark_window
from pendulum import Duration
from pyspark.sql import DataFrame
from pyspark.sql.functions import col
from pyspark.sql.functions import expr
from pyspark.sql.functions import window

from tecton_spark.time_utils import convert_timestamp_to_epoch

ASOF_JOIN_TIMESTAMP_COL_1 = "_asof_join_timestamp_1"
ASOF_JOIN_TIMESTAMP_COL_2 = "_asof_join_timestamp_2"


# TODO: Deprecate this module once QT supports wild cards and non-qt code path can be removed.
# The methods here have been duplicated and extracted from the QT SparkNode implementation.
# From AddEffectiveTimestampSparkNode
def add_effective_timestamp(
    df: DataFrame,
    effective_timestamp_name: str,
    batch_schedule_seconds: int,
    data_delay_seconds: int,
    timestamp_field: str,
    is_stream: bool,
    is_temporal_aggregate: bool,
):
    """Augments a dataframe with a `effective_timestamp` column. `effective_timestamp` is the earliest time a feature would be available
    in the online store. It accounts for batch schedule and data delay, but not processing time.

    :param df: _description_
    :param effective_timestamp_name: _description_
    :param batch_schedule_seconds: _description_
    :param data_delay_seconds: _description_
    :param timestamp_field: _description_
    :param is_stream: _description_
    :param is_temporal_aggregate: _description_
    :return: The same dataframe df with the effective timestamp column added.
    """
    # batch_schedule = 0 implies feature table.
    if batch_schedule_seconds == 0 or is_stream:
        effective_timestamp = col(timestamp_field)
    else:
        slide_str = f"{batch_schedule_seconds} seconds"
        timestamp_col = col(timestamp_field)
        # Timestamp of temporal aggregate is end of the anchor time window. Subtract 1 micro
        # to get the correct bucket for batch schedule.
        if is_temporal_aggregate:
            timestamp_col -= expr(f"interval 1 microseconds")
        window_spec = window(timestamp_col, slide_str, slide_str)
        effective_timestamp = window_spec.end + expr(f"interval {data_delay_seconds} seconds")

    return df.withColumn(effective_timestamp_name, effective_timestamp)


def asof_join(
    spine_df: DataFrame,
    features_df: DataFrame,
    join_cols: List[str],
    spine_timestamp_field: str,
    effective_timestamp_field: str,
    feature_timestamp_field: str,
    right_join_prefix: str = "_tecton_right",
):
    """ASOF join spine_df and features_df using effective timestamp.

    :param spine_df: spine df
    :param features_df: features df, must have `effective_timestamp_field`.
    :param join_cols: join columns
    :param spine_timestamp_field: timestamp field of spine
    :param effective_timestamp_field: effective timestamp field name
    :param feature_timestamp_field: feature timestamp field name
    :param right_join_prefix: prefix added to columns of features_df to prevent name collision during join, defaults to "_tecton_right"
    :return: ASOF joined dataframe.
    """
    # The left(spine_df) and right(features_df) dataframes are unioned together and sorted using 2 columns.
    # The spine will use the spine timestamp and the features will be ordered by their
    # (effective_timestamp, feature_timestamp) because multiple features can have the same effective
    # timestamp. We want to return the closest feature to the spine timestamp that also satisfies
    # the condition => effective timestamp < spine timestamp.
    # The ASOF_JOIN_TIMESTAMP_COL_1 and ASOF_JOIN_TIMESTAMP_COL_2 columns will be used for sorting.
    spine_df = spine_df.withColumn(ASOF_JOIN_TIMESTAMP_COL_1, F.col(spine_timestamp_field))
    spine_df = spine_df.withColumn(ASOF_JOIN_TIMESTAMP_COL_2, F.col(spine_timestamp_field))
    features_df = features_df.withColumn(ASOF_JOIN_TIMESTAMP_COL_1, F.col(effective_timestamp_field))
    features_df = features_df.withColumn(ASOF_JOIN_TIMESTAMP_COL_2, F.col(feature_timestamp_field))
    # includes both fv join keys and the temporal asof join key
    timestamp_join_cols = [ASOF_JOIN_TIMESTAMP_COL_1, ASOF_JOIN_TIMESTAMP_COL_2]
    common_cols = join_cols + timestamp_join_cols
    left_nonjoin_cols = list(set(spine_df.columns) - set(common_cols))
    # we additionally include the right time field though we join on the left's time field.
    # This is so we can see how old the row we joined against is and later determine whether to exclude on basis of ttl
    right_nonjoin_cols = list(set(features_df.columns) - set(join_cols + timestamp_join_cols))

    right_struct_col_name = "_right_values_struct"
    # wrap fields on the right in a struct. This is to work around null feature values and ignorenulls
    # used during joining/window function.
    cols_to_wrap = [F.col(c).alias(f"{right_join_prefix}_{c}") for c in right_nonjoin_cols]
    features_df = features_df.withColumn(right_struct_col_name, F.struct(*cols_to_wrap))
    # schemas have to match exactly so that the 2 dataframes can be unioned together.
    right_struct_schema = features_df.schema[right_struct_col_name].dataType
    left_full_cols = (
        [F.lit(True).alias("is_left")]
        + [F.col(x) for x in common_cols]
        + [F.col(x) for x in left_nonjoin_cols]
        + [F.lit(None).alias(right_struct_col_name).cast(right_struct_schema)]
    )
    right_full_cols = (
        [F.lit(False).alias("is_left")]
        + [F.col(x) for x in common_cols]
        + [F.lit(None).alias(x) for x in left_nonjoin_cols]
        + [F.col(right_struct_col_name)]
    )
    spine_df = spine_df.select(left_full_cols)
    features_df = features_df.select(right_full_cols)
    union = spine_df.union(features_df)
    window_spec = (
        spark_window.Window.partitionBy(join_cols)
        .orderBy([F.col(c).cast("long").asc() for c in timestamp_join_cols])
        .rangeBetween(spark_window.Window.unboundedPreceding, spark_window.Window.currentRow)
    )
    right_window_funcs = [
        F.last(F.col(right_struct_col_name), ignorenulls=True).over(window_spec).alias(right_struct_col_name)
    ]
    # We use the right side of asof join to find the latest values to augment to the rows from the left side.
    # Then, we drop the right side's rows.
    spine_with_features_df = union.select(common_cols + left_nonjoin_cols + right_window_funcs).filter(f"is_left")
    # unwrap the struct to return the fields
    return spine_with_features_df.select(join_cols + left_nonjoin_cols + [f"{right_struct_col_name}.*"])


# From AddDurationSparkNode
def add_duration(input_df: DataFrame, new_column_name: str, timestamp_field: str, duration: Duration):
    """Adds a new column with value timestamp_field + duration.

    :param input_df: _description_
    :param new_column_name: name of new column
    :param timestamp_field: timestamp field to add duration to.
    :param duration: Duration to add.
    :return:
    """
    return input_df.withColumn(
        new_column_name,
        F.col(timestamp_field) + expr(f"interval {duration.total_seconds()} seconds"),
    )


# From RespectTTLSparkNode
def filter_expired_features(
    input_df: DataFrame, features: List[str], retrieval_time_col: str, expiration_time_col: str
):
    """Filter out expired features

    :param input_df: input features dataframe
    :param features: list of feature names
    :param retrieval_time_col: retrieval timestamp column name
    :param expiration_time_col: expiration timestamp column name
    :return: dataframe with expired features set to None
    """
    cond = F.col(retrieval_time_col) < F.col(expiration_time_col)
    # select all non-feature cols, and null out any features outside of ttl
    project_list = [col for col in input_df.columns if col not in features]
    for c in features:
        newcol = F.when(cond, F.col(c)).otherwise(F.lit(None)).alias(c)
        project_list.append(newcol)
    return input_df.select(project_list)


# From AddRetrievalAnchorTimeSparkNode
def add_retrieval_anchor_time(
    input_df: DataFrame,
    timestamp_field: str,
    anchor_time_name: str,
    batch_schedule: int,
    tile_interval: int,
    data_delay_seconds: int,
    is_stream: bool,
    feature_store_format_version: int,
):
    """Augment a dataframe with an retrieval anchor time column that represents the most recent features available for retrieval.

    :param input_df: input dataframe
    :param timestamp_field: timestamp field used to calculate
    :param anchor_time_name: name used for the retrieval anchor time column
    :param batch_schedule: batch schedule of FV
    :param tile_interval: aggregation interval
    :param data_delay_seconds: data delay
    :param is_stream: if the feature view is streaming
    :param feature_store_format_version: feature store format
    :return: dataframe with `anchor_time_name` added
    """
    anchor_time_val = convert_timestamp_to_epoch(
        F.col(timestamp_field) - F.expr(f"interval {data_delay_seconds} seconds"),
        feature_store_format_version,
    )
    # tile_interval will be 0 for continuous
    if tile_interval == 0:
        df = input_df.withColumn(anchor_time_name, anchor_time_val)
    else:
        # For stream, we use the tile interval for bucketing since the data is available as soon as
        # the aggregation interval ends.
        # For BAFV, we use the batch schedule to get the last tile written.
        if is_stream:
            df = input_df.withColumn(
                anchor_time_name,
                anchor_time_val - anchor_time_val % tile_interval - tile_interval,
            )
        else:
            df = input_df.withColumn(
                anchor_time_name,
                anchor_time_val - anchor_time_val % batch_schedule - tile_interval,
            )
    return df
