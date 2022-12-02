from pathlib import Path
from typing import Callable, Literal, Optional, Union

from pandas import DataFrame, Series, concat


class VariantDataGenerator:
    """Transform (unstructured) mutation files to tabular format."""

    def __init__(
        self,
        transform: Callable,
    ):
        """
        Generate tabular data from files containing variant or copy number calls.

        Args:
            transform: Method that generates a row from a VCF or CNV file.
        """
        self.transform = transform

    def flow_from_dataframe(
        self,
        dataframe: DataFrame,
        x_col="filename",
        y_col="class",
        class_mode: Optional[Literal["raw"]] = "raw",
        keep_columns: bool = True,
        coverage_size: Optional[Union[float, str]] = None,
        decimals: Optional[int] = 2,
    ):
        """Load dataset by reading VCF files and target label from dataframe.

        Args:
            dataframe: Pandas dataframe with columns pointing to VCF or CNV files.
            class_mode: When None, don't extract target label (inference mode).
            x_col: Column pointing to location of VCF or CNV file.
            y_col: Target label column.
            class_mode: Return features and labels during training mode ("raw"),
                or return only features during serving (None).
            keep_columns: Use only the features extracted through `x_col` (False) or
                also concatenate other columns in the dataframe after extraction (True).
            coverage_size: Normalise estimates by value (float), column (str), or not at
                all (None). Usually, this value is the size of the genomic region
                [typically in megabases (mb)] covered at sufficient depth to call
                variants.
            decimals: If not None, round to this many decimals.

        Returns: When class_mode is `None` return features `X`, otherwise return a
            pair (X, y) with labels `y`.

        """
        if keep_columns:
            to_keep = dataframe.columns.difference([x_col, y_col])

        if coverage_size is None:
            normalisation = Series(1, index=dataframe.index)
        elif isinstance(coverage_size, (float, int)):
            normalisation = Series(coverage_size, index=dataframe.index)
        elif coverage_size in dataframe.columns:
            normalisation = dataframe[coverage_size]
        else:
            raise KeyError(f"Unknown column {coverage_size}.")

        X = []
        # Loop trough all label directories.
        for index, filename in dataframe[x_col].iteritems():
            x_i = self._transform_x(Path(filename))
            # Normalise estimate by exome size.
            x_i /= normalisation[index]

            # Concatenate other columns.
            if keep_columns:
                if x_i.index.nlevels > 1:
                    raise ValueError(
                        "Unable to coalesce single-index data frame with multi-index result from `transform`."
                    )
                if to_keep.size > 0:
                    x_passthrough = dataframe.loc[[index], to_keep]
                    x_i.index = [index]
                    x_i = concat([x_i, x_passthrough], axis="columns")

            X.append(x_i)

        X_data_frame = concat(X, axis="rows")
        # Use index names from original data frame (instead of that given by
        # `transform`).
        if X_data_frame.index.nlevels > 1:
            X_data_frame.index = X_data_frame.index.set_levels(dataframe.index, level=0)
        else:
            X_data_frame.index = dataframe.index

        if class_mode is None:
            return X_data_frame

        y = dataframe[y_col].copy()

        # Don't round when None.
        if decimals is None:
            return X_data_frame, y
        return X_data_frame.round(decimals), y

    def _transform_x(self, input_file: Path) -> Series:
        """Transform single record (e.g., a VCF or copy number file)."""
        return self.transform(input_file)
