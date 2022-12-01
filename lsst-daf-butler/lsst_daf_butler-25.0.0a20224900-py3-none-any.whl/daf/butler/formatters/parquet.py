# This file is part of daf_butler.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (http://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

__all__ = (
    "ParquetFormatter",
    "arrow_to_pandas",
    "arrow_to_astropy",
    "arrow_to_numpy",
    "arrow_to_numpy_dict",
    "pandas_to_arrow",
    "pandas_to_astropy",
    "astropy_to_arrow",
    "numpy_to_arrow",
    "numpy_to_astropy",
    "numpy_dict_to_arrow",
    "arrow_schema_to_pandas_index",
    "DataFrameSchema",
    "ArrowAstropySchema",
    "ArrowNumpySchema",
)

import collections.abc
import itertools
import json
import re
from typing import TYPE_CHECKING, Any, Dict, Iterable, List, Optional, Sequence, Union

import pyarrow as pa
import pyarrow.parquet as pq
from lsst.daf.butler import Formatter
from lsst.utils.introspection import get_full_type_name
from lsst.utils.iteration import ensure_iterable

if TYPE_CHECKING:
    import astropy.table as atable
    import numpy as np
    import pandas as pd


class ParquetFormatter(Formatter):
    """Interface for reading and writing Arrow Table objects to and from
    Parquet files.
    """

    extension = ".parq"

    def read(self, component: Optional[str] = None) -> Any:
        # Docstring inherited from Formatter.read.
        schema = pq.read_schema(self.fileDescriptor.location.path)

        if component in ("columns", "schema"):
            # The schema will be translated to column format
            # depending on the input type.
            return schema
        elif component == "rowcount":
            # Get the rowcount from the metadata if possible, otherwise count.
            if b"lsst::arrow::rowcount" in schema.metadata:
                return int(schema.metadata[b"lsst::arrow::rowcount"])

            temp_table = pq.read_table(
                self.fileDescriptor.location.path,
                columns=[schema.names[0]],
                use_threads=False,
                use_pandas_metadata=False,
            )

            return len(temp_table[schema.names[0]])

        par_columns = None
        if self.fileDescriptor.parameters:
            par_columns = self.fileDescriptor.parameters.pop("columns", None)
            if par_columns:
                has_pandas_multi_index = False
                if b"pandas" in schema.metadata:
                    md = json.loads(schema.metadata[b"pandas"])
                    if len(md["column_indexes"]) > 1:
                        has_pandas_multi_index = True

                if not has_pandas_multi_index:
                    # Ensure uniqueness, keeping order.
                    par_columns = list(dict.fromkeys(ensure_iterable(par_columns)))
                    file_columns = [name for name in schema.names if not name.startswith("__")]

                    for par_column in par_columns:
                        if par_column not in file_columns:
                            raise ValueError(
                                f"Column {par_column} specified in parameters not available in parquet file."
                            )
                else:
                    par_columns = _standardize_multi_index_columns(schema, par_columns)

            if len(self.fileDescriptor.parameters):
                raise ValueError(
                    f"Unsupported parameters {self.fileDescriptor.parameters} in ArrowTable read."
                )

        metadata = schema.metadata if schema.metadata is not None else {}
        arrow_table = pq.read_table(
            self.fileDescriptor.location.path,
            columns=par_columns,
            use_threads=False,
            use_pandas_metadata=(b"pandas" in metadata),
        )

        return arrow_table

    def write(self, inMemoryDataset: Any) -> None:
        import numpy as np
        from astropy.table import Table as astropyTable

        arrow_table = None
        if isinstance(inMemoryDataset, pa.Table):
            # This will be the most likely match.
            arrow_table = inMemoryDataset
        elif isinstance(inMemoryDataset, astropyTable):
            arrow_table = astropy_to_arrow(inMemoryDataset)
        elif isinstance(inMemoryDataset, np.ndarray):
            arrow_table = numpy_to_arrow(inMemoryDataset)
        else:
            if hasattr(inMemoryDataset, "to_parquet"):
                # This may be a pandas DataFrame
                try:
                    import pandas as pd
                except ImportError:
                    pd = None

                if pd is not None and isinstance(inMemoryDataset, pd.DataFrame):
                    arrow_table = pandas_to_arrow(inMemoryDataset)

        if arrow_table is None:
            raise ValueError(
                f"Unsupported type {get_full_type_name(inMemoryDataset)} of "
                "inMemoryDataset for ParquetFormatter."
            )

        location = self.makeUpdatedLocation(self.fileDescriptor.location)

        pq.write_table(arrow_table, location.path)


def arrow_to_pandas(arrow_table: pa.Table) -> pd.DataFrame:
    """Convert a pyarrow table to a pandas DataFrame.

    Parameters
    ----------
    arrow_table : `pyarrow.Table`
        Input arrow table to convert. If the table has ``pandas`` metadata
        in the schema it will be used in the construction of the
        ``DataFrame``.

    Returns
    -------
    dataframe : `pandas.DataFrame`
    """
    return arrow_table.to_pandas(use_threads=False)


def arrow_to_astropy(arrow_table: pa.Table) -> atable.Table:
    """Convert a pyarrow table to an `astropy.Table`.

    Parameters
    ----------
    arrow_table : `pyarrow.Table`
        Input arrow table to convert. If the table has astropy unit
        metadata in the schema it will be used in the construction
        of the ``astropy.Table``.

    Returns
    -------
    table : `astropy.Table`
    """
    from astropy.table import Table

    astropy_table = Table(arrow_to_numpy_dict(arrow_table))

    metadata = arrow_table.schema.metadata if arrow_table.schema.metadata is not None else {}

    _apply_astropy_metadata(astropy_table, metadata)

    return astropy_table


def arrow_to_numpy(arrow_table: pa.Table) -> np.ndarray:
    """Convert a pyarrow table to a structured numpy array.

    Parameters
    ----------
    arrow_table : `pyarrow.Table`

    Returns
    -------
    array : `numpy.ndarray` (N,)
        Numpy array table with N rows and the same column names
        as the input arrow table.
    """
    import numpy as np

    numpy_dict = arrow_to_numpy_dict(arrow_table)

    dtype = []
    for name, col in numpy_dict.items():
        dtype.append((name, col.dtype))

    array = np.rec.fromarrays(numpy_dict.values(), dtype=dtype)

    return array


def arrow_to_numpy_dict(arrow_table: pa.Table) -> Dict[str, np.ndarray]:
    """Convert a pyarrow table to a dict of numpy arrays.

    Parameters
    ----------
    arrow_table : `pyarrow.Table`

    Returns
    -------
    numpy_dict : `dict` [`str`, `numpy.ndarray`]
        Dict with keys as the column names, values as the arrays.
    """
    schema = arrow_table.schema

    numpy_dict = {}

    for name in schema.names:
        col = arrow_table[name].to_numpy()

        if schema.field(name).type in (pa.string(), pa.binary()):
            col = col.astype(_arrow_string_to_numpy_dtype(schema, name, col))

        numpy_dict[name] = col

    return numpy_dict


def numpy_to_arrow(np_array: np.ndarray) -> pa.Table:
    """Convert a numpy array table to an arrow table.

    Parameters
    ----------
    np_array : `numpy.ndarray`

    Returns
    -------
    arrow_table : `pyarrow.Table`
    """
    type_list = [(name, pa.from_numpy_dtype(np_array.dtype[name].type)) for name in np_array.dtype.names]

    md = {}
    md[b"lsst::arrow::rowcount"] = str(len(np_array))

    for name in np_array.dtype.names:
        _append_numpy_string_metadata(md, name, np_array.dtype[name])

    schema = pa.schema(type_list, metadata=md)

    arrays = [pa.array(np_array[col]) for col in np_array.dtype.names]
    arrow_table = pa.Table.from_arrays(arrays, schema=schema)

    return arrow_table


def numpy_dict_to_arrow(numpy_dict: Dict[str, np.ndarray]) -> pa.Table:
    """Convert a dict of numpy arrays to an arrow table.

    Parameters
    ----------
    numpy_dict : `dict` [`str`, `numpy.ndarray`]
        Dict with keys as the column names, values as the arrays.

    Returns
    -------
    arrow_table : `pyarrow.Table`
    """
    type_list = [(name, pa.from_numpy_dtype(col.dtype.type)) for name, col in numpy_dict.items()]

    md = {}
    md[b"lsst::arrow::rowcount"] = str(len(numpy_dict[list(numpy_dict.keys())[0]]))

    for name, col in numpy_dict.items():
        _append_numpy_string_metadata(md, name, col.dtype)

    schema = pa.schema(type_list, metadata=md)

    arrays = [pa.array(col) for col in numpy_dict.values()]
    arrow_table = pa.Table.from_arrays(arrays, schema=schema)

    return arrow_table


def astropy_to_arrow(astropy_table: atable.Table) -> pa.Table:
    """Convert an astropy table to an arrow table.

    Parameters
    ----------
    astropy_table : `astropy.Table`

    Returns
    -------
    arrow_table : `pyarrow.Table`
    """
    from astropy.table import meta

    type_list = [
        (name, pa.from_numpy_dtype(astropy_table.dtype[name].type)) for name in astropy_table.dtype.names
    ]

    md = {}
    md[b"lsst::arrow::rowcount"] = str(len(astropy_table))

    for name, col in astropy_table.columns.items():
        _append_numpy_string_metadata(md, name, col.dtype)

    meta_yaml = meta.get_yaml_from_table(astropy_table)
    meta_yaml_str = "\n".join(meta_yaml)
    md[b"table_meta_yaml"] = meta_yaml_str

    schema = pa.schema(type_list, metadata=md)

    arrays = [pa.array(col) for col in astropy_table.itercols()]
    arrow_table = pa.Table.from_arrays(arrays, schema=schema)

    return arrow_table


def pandas_to_arrow(dataframe: pd.DataFrame, default_length: int = 10) -> pa.Table:
    """Convert a pandas dataframe to an arrow table.

    Parameters
    ----------
    dataframe : `pandas.DataFrame`
    default_length : `int`, optional
        Default string length when not in metadata or can be inferred
        from column.

    Returns
    -------
    arrow_table : `pyarrow.Table`
    """
    arrow_table = pa.Table.from_pandas(dataframe)

    # Update the metadata
    md = arrow_table.schema.metadata

    md[b"lsst::arrow::rowcount"] = str(arrow_table.num_rows)

    # We loop through the arrow table columns because the datatypes have
    # been checked and converted from pandas objects.
    for name in arrow_table.column_names:
        if not name.startswith("__"):
            if arrow_table[name].type == pa.string():
                if len(arrow_table[name]) > 0:
                    strlen = max(len(row.as_py()) for row in arrow_table[name] if row.is_valid)
                else:
                    strlen = default_length
                md[f"lsst::arrow::len::{name}".encode("UTF-8")] = str(strlen)

    arrow_table = arrow_table.replace_schema_metadata(md)

    return arrow_table


def pandas_to_astropy(dataframe: pd.DataFrame) -> atable.Table:
    """Convert a pandas dataframe to an astropy table, preserving indexes.

    Parameters
    ----------
    dataframe : `pandas.DataFrame`

    Returns
    -------
    astropy_table : `astropy.table.Table`
    """
    import pandas as pd
    from astropy.table import Table

    if isinstance(dataframe.columns, pd.MultiIndex):
        raise ValueError("Cannot convert a multi-index dataframe to an astropy table.")

    return Table.from_pandas(dataframe, index=True)


def numpy_to_astropy(np_array: np.ndarray) -> atable.Table:
    """Convert a numpy table to an astropy table.

    Parameters
    ----------
    np_array : `numpy.ndarray`

    Returns
    -------
    astropy_table : `astropy.table.Table`
    """
    from astropy.table import Table

    return Table(data=np_array, copy=False)


def arrow_schema_to_pandas_index(schema: pa.Schema) -> pd.Index | pd.MultiIndex:
    """Convert an arrow schema to a pandas index/multiindex.

    Parameters
    ----------
    schema : `pyarrow.Schema`

    Returns
    -------
    index : `pandas.Index` or `pandas.MultiIndex`
    """
    import pandas as pd

    if b"pandas" in schema.metadata:
        md = json.loads(schema.metadata[b"pandas"])
        indexes = md["column_indexes"]
        len_indexes = len(indexes)
    else:
        len_indexes = 0

    if len_indexes <= 1:
        return pd.Index(name for name in schema.names if not name.startswith("__"))
    else:
        raw_columns = _split_multi_index_column_names(len(indexes), schema.names)
        return pd.MultiIndex.from_tuples(raw_columns, names=[f["name"] for f in indexes])


def arrow_schema_to_column_list(schema: pa.Schema) -> list[str]:
    """Convert an arrow schema to a list of string column names.

    Parameters
    ----------
    schema : `pyarrow.Schema`

    Returns
    -------
    column_list : `list` [`str`]
    """
    return [name for name in schema.names]


class DataFrameSchema:
    """Wrapper class for a schema for a pandas DataFrame.

    Parameters
    ----------
    dataframe : `pandas.DataFrame`
        Dataframe to turn into a schema.
    """

    def __init__(self, dataframe: pd.DataFrame) -> None:
        self._schema = dataframe.loc[[False] * len(dataframe)]

    @classmethod
    def from_arrow(cls, schema: pa.Schema) -> DataFrameSchema:
        """Convert an arrow schema into a `DataFrameSchema`.

        Parameters
        ----------
        schema : `pyarrow.Schema`
            The pyarrow schema to convert.

        Returns
        -------
        dataframe_schema : `DataFrameSchema`
        """
        empty_table = pa.Table.from_pylist([] * len(schema.names), schema=schema)

        return cls(empty_table.to_pandas())

    def to_arrow_schema(self) -> pa.Schema:
        """Convert to an arrow schema.

        Returns
        -------
        arrow_schema : `pyarrow.Schema`
        """
        arrow_table = pa.Table.from_pandas(self._schema)

        return arrow_table.schema

    def to_arrow_numpy_schema(self) -> ArrowNumpySchema:
        """Convert to an `ArrowNumpySchema`.

        Returns
        -------
        arrow_numpy_schema : `ArrowNumpySchema`
        """
        return ArrowNumpySchema.from_arrow(self.to_arrow_schema())

    def to_arrow_astropy_schema(self) -> ArrowAstropySchema:
        """Convert to an ArrowAstropySchema.

        Returns
        -------
        arrow_astropy_schema : `ArrowAstropySchema`
        """
        return ArrowAstropySchema.from_arrow(self.to_arrow_schema())

    @property
    def schema(self) -> np.dtype:
        return self._schema

    def __repr__(self) -> str:
        return repr(self._schema)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DataFrameSchema):
            return NotImplemented

        return self._schema.equals(other._schema)


class ArrowAstropySchema:
    """Wrapper class for a schema for an astropy table.

    Parameters
    ----------
    astropy_table : `astropy.table.Table`
    """

    def __init__(self, astropy_table: atable.Table) -> None:
        self._schema = astropy_table[:0]

    @classmethod
    def from_arrow(cls, schema: pa.Schema) -> ArrowAstropySchema:
        """Convert an arrow schema into a ArrowAstropySchema.

        Parameters
        ----------
        schema : `pyarrow.Schema`

        Returns
        -------
        astropy_schema : `ArrowAstropySchema`
        """
        import numpy as np
        from astropy.table import Table

        dtype = []
        for name in schema.names:
            if schema.field(name).type not in (pa.string(), pa.binary()):
                dtype.append(schema.field(name).type.to_pandas_dtype())
                continue

            dtype.append(_arrow_string_to_numpy_dtype(schema, name))

        data = np.zeros(0, dtype=list(zip(schema.names, dtype)))

        astropy_table = Table(data=data)

        metadata = schema.metadata if schema.metadata is not None else {}

        _apply_astropy_metadata(astropy_table, metadata)

        return cls(astropy_table)

    def to_arrow_schema(self) -> pa.Schema:
        """Convert to an arrow schema.

        Returns
        -------
        arrow_schema : `pyarrow.Schema`
        """
        return astropy_to_arrow(self._schema).schema

    def to_dataframe_schema(self) -> DataFrameSchema:
        """Convert to a DataFrameSchema.

        Returns
        -------
        dataframe_schema : `DataFrameSchema`
        """
        return DataFrameSchema.from_arrow(astropy_to_arrow(self._schema).schema)

    def to_arrow_numpy_schema(self) -> ArrowNumpySchema:
        """Convert to an `ArrowNumpySchema`.

        Returns
        -------
        arrow_numpy_schema : `ArrowNumpySchema`
        """
        return ArrowNumpySchema.from_arrow(astropy_to_arrow(self._schema).schema)

    @property
    def schema(self) -> atable.Table:
        return self._schema

    def __repr__(self) -> str:
        return repr(self._schema)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ArrowAstropySchema):
            return NotImplemented

        # If this comparison passes then the two tables have the
        # same column names.
        if self._schema.dtype != other._schema.dtype:
            return False

        for name in self._schema.columns:
            if not self._schema[name].unit == other._schema[name].unit:
                return False
            if not self._schema[name].description == other._schema[name].description:
                return False
            if not self._schema[name].format == other._schema[name].format:
                return False

        return True


class ArrowNumpySchema:
    """Wrapper class for a schema for a numpy ndarray.

    Parameters
    ----------
    numpy_dtype : `numpy.dtype`
         Numpy dtype to convert.
    """

    def __init__(self, numpy_dtype: np.dtype) -> None:
        self._dtype = numpy_dtype

    @classmethod
    def from_arrow(cls, schema: pa.Schema) -> ArrowNumpySchema:
        """Convert an arrow schema into an `ArrowNumpySchema`.

        Parameters
        ----------
        schema : `pyarrow.Schema`
            Pyarrow schema to convert.

        Returns
        -------
        numpy_schema : `ArrowNumpySchema`
        """
        import numpy as np

        dtype = []
        for name in schema.names:
            if schema.field(name).type not in (pa.string(), pa.binary()):
                dtype.append((name, schema.field(name).type.to_pandas_dtype()))
                continue

            dtype.append((name, _arrow_string_to_numpy_dtype(schema, name)))

        return cls(np.dtype(dtype))

    def to_arrow_astropy_schema(self) -> ArrowAstropySchema:
        """Convert to an `ArrowAstropySchema`.

        Returns
        -------
        astropy_schema : `ArrowAstropySchema`
        """
        import numpy as np

        return ArrowAstropySchema.from_arrow(numpy_to_arrow(np.zeros(0, dtype=self._dtype)).schema)

    def to_dataframe_schema(self) -> DataFrameSchema:
        """Convert to a `DataFrameSchema`.

        Returns
        -------
        dataframe_schema : `DataFrameSchema`
        """
        import numpy as np

        return DataFrameSchema.from_arrow(numpy_to_arrow(np.zeros(0, dtype=self._dtype)).schema)

    def to_arrow_schema(self) -> pa.Schema:
        """Convert to a `pyarrow.Schema`.

        Returns
        -------
        arrow_schema : `pyarrow.Schema`
        """
        import numpy as np

        return numpy_to_arrow(np.zeros(0, dtype=self._dtype)).schema

    @property
    def schema(self) -> np.dtype:
        return self._dtype

    def __repr__(self) -> str:
        return repr(self._dtype)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ArrowNumpySchema):
            return NotImplemented

        if not self._dtype == other._dtype:
            return False

        return True


def _split_multi_index_column_names(n: int, names: Iterable[str]) -> List[Sequence[str]]:
    """Split a string that represents a multi-index column.

    PyArrow maps Pandas' multi-index column names (which are tuples in Python)
    to flat strings on disk. This routine exists to reconstruct the original
    tuple.

    Parameters
    ----------
    n : `int`
        Number of levels in the `pandas.MultiIndex` that is being
        reconstructed.
    names : `~collections.abc.Iterable` [`str`]
        Strings to be split.

    Returns
    -------
    column_names : `list` [`tuple` [`str`]]
        A list of multi-index column name tuples.
    """
    column_names: List[Sequence[str]] = []

    pattern = re.compile(r"\({}\)".format(", ".join(["'(.*)'"] * n)))
    for name in names:
        m = re.search(pattern, name)
        if m is not None:
            column_names.append(m.groups())

    return column_names


def _standardize_multi_index_columns(
    schema: pa.Schema, columns: Union[List[tuple], Dict[str, Union[str, List[str]]]]
) -> List[str]:
    """Transform a dictionary/iterable index from a multi-index column list
    into a string directly understandable by PyArrow.

    Parameters
    ----------
    schema : `pyarrow.Schema`
    columns : `list` [`tuple`] or `dict` [`str`, `str` or `list` [`str`]]

    Returns
    -------
    names : `list` [`str`]
        Stringified representation of a multi-index column name.
    """
    pd_index = arrow_schema_to_pandas_index(schema)
    index_level_names = tuple(pd_index.names)

    names = []

    if isinstance(columns, list):
        for requested in columns:
            if not isinstance(requested, tuple):
                raise ValueError(
                    "Columns parameter for multi-index data frame must be a dictionary or list of tuples. "
                    f"Instead got a {get_full_type_name(requested)}."
                )
            names.append(str(requested))
    else:
        if not isinstance(columns, collections.abc.Mapping):
            raise ValueError(
                "Columns parameter for multi-index data frame must be a dictionary or list of tuples. "
                f"Instead got a {get_full_type_name(columns)}."
            )
        if not set(index_level_names).issuperset(columns.keys()):
            raise ValueError(
                f"Cannot use dict with keys {set(columns.keys())} "
                f"to select columns from {index_level_names}."
            )
        factors = [
            ensure_iterable(columns.get(level, pd_index.levels[i]))
            for i, level in enumerate(index_level_names)
        ]
        for requested in itertools.product(*factors):
            for i, value in enumerate(requested):
                if value not in pd_index.levels[i]:
                    raise ValueError(f"Unrecognized value {value!r} for index {index_level_names[i]!r}.")
            names.append(str(requested))

    return names


def _apply_astropy_metadata(astropy_table: atable.Table, metadata: Dict) -> None:
    """Apply any astropy metadata from the schema metadata.

    Parameters
    ----------
    astropy_table : `astropy.table.Table`
        Table to apply metadata.
    metadata : `dict` [`bytes`]
        Metadata dict.
    """
    from astropy.table import meta

    meta_yaml = metadata.get(b"table_meta_yaml", None)
    if meta_yaml:
        meta_yaml = meta_yaml.decode("UTF8").split("\n")
        meta_hdr = meta.get_header_from_yaml(meta_yaml)

        # Set description, format, unit, meta from the column
        # metadata that was serialized with the table.
        header_cols = {x["name"]: x for x in meta_hdr["datatype"]}
        for col in astropy_table.columns.values():
            for attr in ("description", "format", "unit", "meta"):
                if attr in header_cols[col.name]:
                    setattr(col, attr, header_cols[col.name][attr])


def _arrow_string_to_numpy_dtype(
    schema: pa.Schema, name: str, numpy_column: np.ndarray | None = None, default_length: int = 10
) -> str:
    """Get the numpy dtype string associated with an arrow column.

    Parameters
    ----------
    schema : `pyarrow.Schema`
        Arrow table schema.
    name : `str`
        Column name.
    numpy_column : `numpy.ndarray`, optional
        Column to determine numpy string dtype.
    default_length : `int`, optional
        Default string length when not in metadata or can be inferred
        from column.

    Returns
    -------
    dtype_str : `str`
        Numpy dtype string.
    """
    # Special-case for string and binary columns
    md_name = f"lsst::arrow::len::{name}"
    strlen = default_length
    metadata = schema.metadata if schema.metadata is not None else {}
    if (encoded := md_name.encode("UTF-8")) in metadata:
        # String/bytes length from header.
        strlen = int(schema.metadata[encoded])
    elif numpy_column is not None:
        if len(numpy_column) > 0:
            strlen = max(len(row) for row in numpy_column)

    dtype = f"U{strlen}" if schema.field(name).type == pa.string() else f"|S{strlen}"

    return dtype


def _append_numpy_string_metadata(metadata: Dict[bytes, str], name: str, dtype: np.dtype) -> None:
    """Append numpy string length keys to arrow metadata.

    All column types are handled, but only the metadata is only modified for
    string and byte columns.

    Parameters
    ----------
    metadata : `dict` [`bytes`, `str`]
        Metadata dictionary; modified in place.
    name : `str`
        Column name.
    dtype : `np.dtype`
        Numpy dtype.
    """
    import numpy as np

    if dtype.type is np.str_:
        metadata[f"lsst::arrow::len::{name}".encode("UTF-8")] = str(dtype.itemsize // 4)
    elif dtype.type is np.bytes_:
        metadata[f"lsst::arrow::len::{name}".encode("UTF-8")] = str(dtype.itemsize)
