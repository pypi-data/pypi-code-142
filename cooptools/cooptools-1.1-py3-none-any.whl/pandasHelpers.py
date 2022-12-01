import pandas as pd
from typing import Dict, Callable, List
import datetime
from cooptools.printing import pretty_format_list_of_tuple, pretty_format_dataframe
import numpy as np

class PandasMissingColumnsException(Exception):
    ''' Raised when a user tries to create an account that already exists'''
    def __init__(self, columns_present: List[str], required_columns: List[str]):
        self.columns_present = columns_present
        self.required_columns = required_columns
        self.missing_columns = list(set(required_columns) - set(columns_present))
        self.message = f"All columns [{self.required_columns}] required but columns [{self.missing_columns}] were missing"
        super().__init__(self.message)


class PandasFillColumnTypeException(Exception):
    def __init__(self, str):
        Exception().__init__(str)

    pass


def summary_rows_cols(df: pd.DataFrame,
                      column_sum: bool = False,
                      column_avg: bool = False,
                      column_median: bool = False,
                      row_sum: bool = False,
                      row_avg: bool = False,
                      row_median: bool = False,
                      na_fill: str = None,
                      replace_zero_val: str = None
                      ) -> pd.DataFrame:
    ret = df.copy()

    # column sums based on the original dataframe
    if column_sum: ret.loc['Sum'] = df.sum(numeric_only=True, axis=0, min_count=1)
    if column_avg: ret.loc['Avg'] = df.mean(numeric_only=True, axis=0, min_count=1)
    if column_median: ret.loc['Median'] = df.median(numeric_only=True, axis=0, min_count=1)

    # row sums on the new dataframe as to accommodate "summing the sums", first calculate the values
    sum = None
    median = None
    avg = None
    if row_sum: sum = ret.sum(numeric_only=True, axis=1)
    if row_avg: avg = ret.mean(numeric_only=True, axis=1)
    if row_median: median = ret.median(numeric_only=True, axis=1)

    # then, append them to the end of the dataframe (RHS)
    if sum is not None: ret.loc[:, 'Sum'] = sum
    if avg is not None: ret.loc[:, 'Avg'] = avg
    if median is not None: ret.loc[:, 'Median'] = median

    if na_fill is not None:
        ret.fillna(na_fill, inplace=True)

    if replace_zero_val is not None:
        ret.replace(to_replace=0, value=replace_zero_val, inplace=True)

    return ret

def pretty_print_dataframe(df: pd.DataFrame,
                           title: str = None,
                           summarize: bool = False,
                           max_columns: int = 2000,
                           max_rows: int = 500,
                           display_width: int = 250
                            ):
    ret = ""

    if title:
        ret += title
        print(title)

    if summarize:
        df = summary_rows_cols(df)

    with pd.option_context('display.max_rows', max_rows, 'display.max_columns', max_columns, 'display.width', display_width):
        ret += f"{df}\n"
        print(f"{df}\n")

    return ret

def find_the_type_conversion_errors_and_raise(df: pd.DataFrame, column_type_definition: Dict):

    errors = []
    for column, requested_type in column_type_definition.items():
        try:
            df[column].astype(requested_type)
        except:
            for index, row in df.iterrows():
                try:
                    row[column].astype(requested_type)
                except:
                    errors.append((index, column, row[column], requested_type, type(row[column])))

    errors_df = pd.DataFrame(errors,
                             columns=['row_index', 'column_name', 'value', 'requested_type_conversion', 'current_type'])

    raise ValueError(f"Error performing the following conversions: \n{pretty_format_dataframe(errors_df)}")

def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('$', '').replace(',', '').replace('(', '-').replace(')', ''))
    return(x)


def convert_pandas_data_columns_to_type(df: pd.DataFrame, column_type_definition: Dict) -> pd.DataFrame:

    if df is None:
        return None


    # handle currency conversions for floats/ints:
    columns_that_may_need_cleaned = [k for k, v in column_type_definition.items() if
             v in (float, int) and k in df.columns]
    for column in columns_that_may_need_cleaned:
        pd.options.mode.chained_assignment = None
        df[column] = df[column].map(clean_currency)
        pd.options.mode.chained_assignment = 'warn'

    # Cast columns as type (excluding dates and ints)
    types = {k:v for k, v in column_type_definition.items() if v not in (datetime.date, datetime.datetime) and k in df.columns}
    try:
        df = df.astype(types)
    except:
        find_the_type_conversion_errors_and_raise(df[[x for x in types.keys()]], types)

    # handle date conversions
    for col, type in {k: v for k, v in column_type_definition.items() if v in (datetime.date, datetime.datetime) and k in df.columns}.items():
        df[col] = pd.to_datetime(df[col])
        if type == datetime.date:
            df[col] = df[col].dt.normalize()

    return df


def verify_all_required_columns(df: pd.DataFrame, required_columns: List[str]):
    if not all(column in df.columns for column in required_columns):
        raise PandasMissingColumnsException(columns_present=[col for col in df.columns], required_columns=required_columns)

def clean_a_dataframe(df: pd.DataFrame,
                      column_type_definition: Dict,
                      case_sensitive: bool = False,
                      allow_partial_columnset:bool=False,
                      fill_missing: bool=False,
                      column_name_replacement: Callable[[pd.DataFrame], Dict] = None,
                      keep_extra: bool = False,
                      nan_replacements: Dict = None) -> pd.DataFrame:

    required_columns = [key for key, value in column_type_definition.items()]

    # map columns that dont match name
    if column_name_replacement is not None:
        df = df.rename(columns=column_name_replacement(df))

    # update based on case-sensitivity
    if not case_sensitive:
        df.columns = map(str.lower, df.columns)
        col_indexes = {col: df.columns.get_loc(col.lower()) if col.lower() in df.columns else None for col in required_columns}
        name_replacements = {[x for x in df.columns][ind]: col for col, ind in col_indexes.items() if ind is not None}
        df.rename(columns=name_replacements, inplace=True)

    # Filter columns
    if not keep_extra:
        df = df[[col for col in required_columns if col in df.columns]]

    # raise error if not all columns exist
    if not allow_partial_columnset:
        verify_all_required_columns(df, required_columns)

    # handle empty dataframe
    if not any(df):
        df = pd.DataFrame(columns=required_columns)

    # add missing columns
    missing_columns = [column for column in required_columns if column not in df.columns]
    if fill_missing:
        for col in missing_columns:
            requested_type = column_type_definition[col]
            if requested_type in [int]:
                raise PandasFillColumnTypeException(f"Unable to create an empty column of type {requested_type}. {requested_type} is not nullable.")
            df[col] = pd.Series([], dtype=requested_type)

    # replace nans:
    if nan_replacements:
        for column, replacement in nan_replacements.items():
            df[column] = df[column].replace(np.nan, replacement)

    # column type conversions
    df = convert_pandas_data_columns_to_type(df, column_type_definition)

    # return
    return df

def try_parse_and_localize_date_series(date_column):
    try:
        return pd.to_datetime(date_column).dt.tz_localize(None)
    except:
        return pd.to_datetime(date_column)

def import_data_from_csv_with_specified_columns(filepath: str,
                                                column_type_definition: Dict,
                                                allow_partial:bool=False,
                                                fill_missing: bool=False) -> pd.DataFrame:
    # Get file contents
    if filepath is None or filepath == '':
        return None
    df = pd.read_csv(filepath)
    if df is None:
        return None

    # Return
    return clean_a_dataframe(df, column_type_definition=column_type_definition, allow_partial_columnset=allow_partial, fill_missing=fill_missing)


column_date_ge_filter = lambda df, col_name, val: df[col_name] >= val
column_date_le_filter = lambda df, col_name, val: df[col_name] <= val
column_date_bet_filter = lambda df, col_name, small, large: small <= df[col_name] <= large



if __name__ == "__main__":
    # TEST 1
    # df = pd.read_csv('../tests/testdata/dummy_data_clean.csv')
    # column_definitions = {"my_clean_int": int,
    #                       "my_clean_str": str,
    #                       "my_clean_date": datetime.date,
    #                       "my_missing_column": np.int64}
    #
    # converted = clean_a_dataframe(df, column_type_definition=column_definitions, allow_partial_columnset=True)
    #
    # converted['newdate'] = converted['my_clean_date'] + datetime.timedelta(days=1)
    #
    # print(converted.dtypes)
    #
    #
    #
    # print(converted.dtypes['my_clean_date'])
    # print(converted.dtypes['my_clean_date'] == np.datetime64)
    # print(converted)


    # TEST Summary_rows_cols
    data = {
        'a': [1, 2, 3],
        'b': [4, 5, 6],
        'c': [7, 8, 9]
    }

    df = pd.DataFrame(data)

    printable = summary_rows_cols(df, row_sum=True, column_sum=True, row_median=True)

    pretty_print_dataframe(printable)