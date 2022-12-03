import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import EnglishStemmer
import warnings
from math import isclose
from .utils import filter_non_capitalized_words_from_list

stemmer = EnglishStemmer()


class clean_class:
    def __init__(
        self,
        _df: pd.DataFrame,
        str_cols_to_clean: list,
        cols_to_drop: list,
        dict_with_cols_to_downcast: dict,
        unique_id_col_that_is_str_which_needs_to_be_inted: str = None,
        cols_that_should_not_have_negative: list = None,
        cols_that_should_not_have_zero: list = None,
        row_mask_to_drop: pd.Series = None,
        dict_with_col_name_as_key_and_mask_as_value_to_make_na: dict = None,
    ) -> None:
        df = _df.copy()
        # Reset index just in case there are duplicate index
        # df = df.reset_index(drop=True)

        # Save the raw input
        self.str_cols_to_clean = str_cols_to_clean
        self.cols_to_drop = cols_to_drop
        self.cols_in_tracker = [
            "order",
            "activity",
            "cols_impacted",
            "num_of_cols_impacted",
            "rows_impacted",
            "num_of_rows_impacted",
        ]
        self.na_like_values = [
            "na",
            "n/a",
            "nan",
            "none",
            "null",
            "missing",
            "unknown",
            "undefined",
            "",
        ]
        self.counter = 1

        # Working and ouput
        self.RAW_INPUT = df.copy()
        self.TRACKER = pd.DataFrame(columns=self.cols_in_tracker)
        df = self.drop_columns(_df=df)
        for downcast_to, list_of_cols in dict_with_cols_to_downcast.items():
            df = self.convert_one_dtype_at_a_time(
                _df=df, cols_to_downcast=list_of_cols, down_cast_dtype=downcast_to
            )
        if unique_id_col_that_is_str_which_needs_to_be_inted != None:
            df, df_mapping = self.convert_str_to_uid_int(
                _df_input=df,
                col_to_convert_to_int=unique_id_col_that_is_str_which_needs_to_be_inted,
                int_type="int32",
            )
            self.NEW_ID_TO_OLD_ID_MAPPING = df_mapping.copy()
        df = self.make_datetime_like_columns_datetime(_df=df)
        df = self.make_na_like_values_in_string_cols_na(_df=df)
        df = self.clean_str_columns(_df=df, str_cols_to_clean=str_cols_to_clean)
        df = self.drop_duplicate_rows(_df=df)

        # Make negative values in columns that should not have negative values NA
        if cols_that_should_not_have_negative != None:
            df = self.make_negative_na(
                _df=df,
                cols_that_should_not_have_negative=cols_that_should_not_have_negative,
            )

        # Make zero in certain columns na
        if cols_that_should_not_have_zero != None:
            df = self.make_zero_na(
                _df=df, cols_that_should_not_have_zero=cols_that_should_not_have_zero
            )

        # Drop certain rows
        if row_mask_to_drop != None:
            df = self.drop_rows(_df=df, row_mask_to_drop=row_mask_to_drop)

        # Make certain entries as NA
        if dict_with_col_name_as_key_and_mask_as_value_to_make_na != None:
            for (
                key,
                value,
            ) in dict_with_col_name_as_key_and_mask_as_value_to_make_na.items():
                df = self.make_masked_entries_na(
                    _df=df, row_mask_to_make_na=value, col=key
                )

        self.OUTPUT = df.copy()

    def make_mask_na(self, _df: pd.DataFrame, row_mask_to_make_na: pd.Series, col: str):
        df = _df.copy()
        df.loc[row_mask_to_make_na, col] = np.nan
        self.track_changes(
            activity="make_mask_na",
            cols_impacted=[col],
            num_of_cols_impacted=1,
            rows_impacted=row_mask_to_make_na.index.tolist(),
            num_of_rows_impacted=len(row_mask_to_make_na.index.tolist()),
        )

    def drop_rows(self, _df: pd.DataFrame, row_mask_to_drop: pd.Series) -> pd.DataFrame:
        df = _df.copy()
        df = df.loc[~row_mask_to_drop]
        self.track_changes(
            activity="drop_rows",
            cols_impacted=[],
            num_of_cols_impacted=0,
            rows_impacted=row_mask_to_drop.index.tolist(),
            num_of_rows_impacted=len(row_mask_to_drop.index.tolist()),
        )
        return df

    def make_negative_na(
        self, _df: pd.DataFrame, cols_that_should_not_have_negative: list
    ) -> pd.DataFrame:
        df = _df.copy()
        for col in cols_that_should_not_have_negative:
            filter = df[col] < 0
            df.loc[filter, col] = np.nan
            if filter.sum() > 0:
                self.track_changes(
                    activity="make_negative_na",
                    cols_impacted=[col],
                    num_of_cols_impacted=1,
                    rows_impacted=df.loc[filter].index.tolist(),
                    num_of_rows_impacted=len(df.loc[filter].index.tolist()),
                )

    def make_zero_na(
        self, _df: pd.DataFrame, cols_that_should_not_have_zero: list
    ) -> pd.DataFrame:
        df = _df.copy()
        for col in cols_that_should_not_have_zero:
            filter = df[col] == 0
            df.loc[filter, col] = np.nan
            if filter.sum() > 0:
                self.track_changes(
                    activity="make_zero_na",
                    cols_impacted=[col],
                    num_of_cols_impacted=1,
                    rows_impacted=df.loc[filter].index.tolist(),
                    num_of_rows_impacted=len(df.loc[filter].index.tolist()),
                )
        return df

    def _make_str_columns_lowercase(self, _df: pd.DataFrame) -> pd.DataFrame:
        df = _df.copy()
        df = df.apply(
            lambda col: col.str.lower() if col.dtypes == object else col, axis=0
        )
        return df

    def track_changes(
        self,
        activity: str,
        cols_impacted: list,
        num_of_cols_impacted: int,
        rows_impacted: list,
        num_of_rows_impacted: int,
    ) -> None:
        temp = pd.DataFrame(
            [
                [
                    self.counter,
                    activity,
                    cols_impacted,
                    num_of_cols_impacted,
                    rows_impacted,
                    num_of_rows_impacted,
                ]
            ],
            columns=self.cols_in_tracker,
        )
        self.TRACKER = pd.concat([self.TRACKER, temp])
        self.counter += 1

    def drop_columns(self, _df: pd.DataFrame) -> pd.DataFrame:
        df = _df.copy()
        df = df.drop(columns=self.cols_to_drop)
        self.track_changes(
            activity="drop_columns",
            cols_impacted=self.cols_to_drop,
            num_of_cols_impacted=len(self.cols_to_drop),
            rows_impacted=[],
            num_of_rows_impacted=0,
        )
        return df

    def make_na_like_values_in_string_cols_na(self, _df: pd.DataFrame) -> pd.DataFrame:
        df = _df.copy()
        string_cols = _df.select_dtypes(include=["object"]).columns.tolist()
        df = self._make_str_columns_lowercase(_df=df)
        df_original = df.copy()

        cols_impacted = []
        for col in string_cols:
            df[col] = df[col].replace(self.na_like_values, np.nan)
            # Find out if any replacement happened
            cols_impacted.append(col) if df[col].equals(
                df_original[col]
            ) == False else None
        self.track_changes(
            activity="make_na_like_values_in_string_cols_na",
            cols_impacted=cols_impacted,
            num_of_cols_impacted=len(cols_impacted),
            rows_impacted=[],
            num_of_rows_impacted=0,
        )
        return df

    def make_datetime_like_columns_datetime(self, _df: pd.DataFrame) -> pd.DataFrame:
        df = _df.copy()

        # Make datetime like columns datetime and track which columns were impacted
        datetime_cols_pre = df.select_dtypes(include=["datetime"]).columns.tolist()
        df = df.apply(
            lambda col: pd.to_datetime(col, errors="ignore")
            if col.dtypes == object
            else col,
            axis=0,
        )
        datetime_cols_post = df.select_dtypes(include=["datetime"]).columns.tolist()
        datetime_cols_impacted = list(set(datetime_cols_post) - set(datetime_cols_pre))

        # Initiate tracker
        self.track_changes(
            activity="make_datetime_like_columns_datetime",
            cols_impacted=datetime_cols_impacted,
            num_of_cols_impacted=len(datetime_cols_impacted),
            rows_impacted=[],
            num_of_rows_impacted=0,
        )
        return df

    def clean_str_columns(
        self, _df: pd.DataFrame, str_cols_to_clean: list
    ) -> pd.DataFrame:
        df = _df.copy()
        df_original = df.copy()
        columns_impacted = []

        # Identify string columns
        string_cols = _df.select_dtypes(include=["object"]).columns.tolist()
        string_cols = list(set(string_cols).intersection(set(str_cols_to_clean)))

        # Loop through evert string column and clean textual data
        for col in string_cols:
            # Make na values as empty string
            df[col] = df[col].fillna("")
            # Tokenize
            df[col] = df[col].apply(word_tokenize)
            # Remove stop words
            stop = stopwords.words("ENGLISH")
            df[col] = df[col].apply(lambda x: [item for item in x if item not in stop])
            # Stem every word
            df[col] = df[col].apply(lambda x: [stemmer.stem(y) for y in x])
            # Make column of list to str
            df[col] = df[col].apply(lambda x: " ".join(map(str, x)))
            # Remove punctuations
            df[col] = df[col].str.replace("[^\w\s]", "")
            # Remove everything other than alphabets
            df[col] = df[col].str.replace("[^a-zA-Z]", " ")
            # Make empty string as na
            df[col] = df[col].replace("", np.nan)
            # Remove words with length less than 3
            df[col] = df[col].str.findall("\w{3,}").str.join(" ")
            # Determine if the column was impacted
            columns_impacted.append(col) if df[col].equals(
                df_original[col]
            ) == False else None

        # Initiate tracker
        self.track_changes(
            activity="clean_str_columns",
            cols_impacted=columns_impacted,
            num_of_cols_impacted=len(columns_impacted),
            rows_impacted=[],
            num_of_rows_impacted=0,
        )
        return df

    def drop_duplicate_rows(self, _df: pd.DataFrame) -> pd.DataFrame:
        df = _df.copy()
        df_original = df.copy()
        df = df.drop_duplicates()
        num_of_rows_dropped = df_original.shape[0] - df.shape[0]
        self.track_changes(
            activity="drop_duplicate_rows",
            cols_impacted=[],
            num_of_cols_impacted=0,
            rows_impacted=list(set(df_original.index) - set(df.index)),
            num_of_rows_impacted=num_of_rows_dropped,
        )
        return df

    def get_attributes_of_class(self) -> list:
        return [
            attr
            for attr in dir(self)
            if not callable(getattr(self, attr)) and not attr.startswith("__")
        ]

    def get_output_attributes_of_class(self) -> list:
        all_attributes = self.get_attributes_of_class()
        return filter_non_capitalized_words_from_list(_list=all_attributes)

    def convert_one_dtype_at_a_time(
        self, _df: pd.DataFrame, cols_to_downcast: list, down_cast_dtype: str
    ):
        df = _df.copy()

        # Lets also ensure that the columns are numeric
        numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
        cols_to_downcast = list(set(cols_to_downcast).intersection(set(numeric_cols)))

        # Recording original df
        df_original = df.copy()

        # Downcast the columns
        for col in cols_to_downcast:
            df[col] = df[col].astype(down_cast_dtype)

            # Calculate mean of the columns in the original df and the downcasted df
            original_mean = df_original[col].mean()
            new_mean = df[col].mean()
            assert isclose(
                original_mean, new_mean, abs_tol=1e-3
            ), f"Downcasting to {down_cast_dtype} has resulted in loss of information for column {col}"

        # Track changes
        self.track_changes(
            activity=f"converting_to_{down_cast_dtype}",
            cols_impacted=cols_to_downcast,
            num_of_cols_impacted=len(cols_to_downcast),
            rows_impacted=[],
            num_of_rows_impacted=0,
        )
        return df

    def convert_str_to_uid_int(
        self,
        _df_input: pd.DataFrame,
        col_to_convert_to_int: str,
        int_type: str = "int32",
    ) -> tuple:
        """
        This function is used to map unique values in a column to integer with objective of saving memory

        Parameters
        ----------------------------------------
        _df_input (pd.DataFrame): Input dataframe
        col_to_convert_to_int (str): column name in _df_input that needs to coded up using random numbers
        int_type (str): Deafult: "int32" or altenatively use "int64"

        Returns
        ---------------------------------------
        (pd.DataFrame, pd.DataFrame)
        """
        df_input = _df_input.copy()

        # Input validation
        if not isinstance(df_input, pd.DataFrame):
            raise ValueError(
                f"df_input needs to be a dataframe but got {type(df_input)}"
            )
        if col_to_convert_to_int not in _df_input.columns:
            raise ValueError(
                f"The input dataframe does not have the column by the name {col_to_convert_to_int}"
            )
        if int_type not in ["int32", "int64"]:
            raise ValueError("The function supports int32 and int64 alone")

        # Get a dictionary that maps the column value to an unique int value
        df_mapping = pd.DataFrame()
        df_mapping[col_to_convert_to_int] = df_input[col_to_convert_to_int].unique()
        df_mapping = df_mapping.reset_index()
        df_mapping = df_mapping.rename(
            columns={"index": col_to_convert_to_int + "_int"}
        )
        df_mapping = df_mapping.set_index([col_to_convert_to_int])
        dict_mapping = df_mapping.to_dict()[col_to_convert_to_int + "_int"]

        # Replace the col value with the int value
        df_input[col_to_convert_to_int] = df_input[col_to_convert_to_int].map(
            dict_mapping
        )
        df_input[col_to_convert_to_int] = df_input[col_to_convert_to_int].astype(
            int_type
        )

        return df_input, df_mapping
