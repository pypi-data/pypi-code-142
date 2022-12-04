import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import EnglishStemmer
import warnings
from math import isclose
from .utils import filter_non_capitalized_words_from_list
from .const import std_vals

stemmer = EnglishStemmer()


class clean_class:
    def __init__(
        self,
    ) -> None:

        # Initialize tracker
        self.cols_in_tracker = [
            "order",
            "activity",
            "cols_impacted",
            "num_of_cols_impacted",
            "rows_impacted",
            "num_of_rows_impacted",
        ]
        self.na_like_values = std_vals.na_like_items_in_str
        self.counter = 1
        self.TRACKER = pd.DataFrame(columns=self.cols_in_tracker)

        """
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
        """

    def remove_existing_index_and_make_new_one(self, _df: pd.DataFrame) -> pd.DataFrame:
        df = _df.copy()
        df = df.reset_index(drop=True)

        # Track changes
        self.track_changes(
            activity="remove_existing_index_and_make_new_one",
            cols_impacted=[],
            num_of_cols_impacted=0,
            rows_impacted=[],
            num_of_rows_impacted=0,
        )

        # Save output
        self.OUTPUT = df.copy()

        # return df so that we can use pandas pipe
        return self.OUTPUT

    def make_one_col_mask_na(
        self, _df: pd.DataFrame, row_mask_to_make_na: pd.Series, col: str
    ):
        df = _df.copy()
        df.loc[row_mask_to_make_na, col] = np.nan
        self.track_changes(
            activity="make_mask_na",
            cols_impacted=[col],
            num_of_cols_impacted=1,
            rows_impacted=row_mask_to_make_na.index.tolist(),
            num_of_rows_impacted=len(row_mask_to_make_na.index.tolist()),
        )

        # Save output
        self.OUTPUT = df.copy()

        # return df so that we can use pandas pipe
        return self.OUTPUT

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

        # Save output
        self.OUTPUT = df.copy()

        # return df so that we can use pandas pipe
        return self.OUTPUT

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

        # Save output
        self.OUTPUT = df.copy()

        # return df so that we can use pandas pipe
        return self.OUTPUT

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

        # Save output
        self.OUTPUT = df.copy()

        # return df so that we can use pandas pipe
        return self.OUTPUT

    def _make_str_cols_lowercase(self, _df: pd.DataFrame, cols: list) -> pd.DataFrame:
        df = _df.copy()

        # Remove duplicates if any
        cols = list(set(cols))

        # Check if list of cols are in df
        cols_in_df = df.columns.tolist()
        cols_in_input_cols_not_in_df = list(set(cols) - set(cols_in_df))
        if len(cols_in_input_cols_not_in_df) > 0:
            warnings.warn(f"Some columns in {cols} are not in the dataframe")

        # Make sure cols are string
        str_cols_in_df = df.select_dtypes(exclude=np.number).columns.tolist()
        common_str_cols = list(set(cols).intersection(set(str_cols_in_df)))
        non_str_cols_in_input_cols = list(set(cols).difference(set(str_cols_in_df)))
        if len(non_str_cols_in_input_cols) > 0:
            warnings.warn(f"{non_str_cols_in_input_cols} are not string columns")

        # Make str_cols lowercase
        print(f"Making {common_str_cols} lowercase")
        for col in common_str_cols:
            try:
                df[col] = df[col].str.lower()
            except AttributeError:
                warnings.warn(f"Could not make {col} lowercase")

        # Track changes
        self.track_changes(
            activity="make_str_col_lowercase",
            cols_impacted=common_str_cols,
            num_of_cols_impacted=len(common_str_cols),
            rows_impacted=[],
            num_of_rows_impacted=0,
        )

        # Save output
        self.OUTPUT = df.copy()

        # return df so that we can use pandas pipe
        return self.OUTPUT

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

        # Save output
        self.OUTPUT = df.copy()

        # return df so that we can use pandas pipe
        return self.OUTPUT

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

        # Save output
        self.OUTPUT = df.copy()

        # return df so that we can use pandas pipe
        return self.OUTPUT

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

        # Save output
        self.OUTPUT = df.copy()

        # return df so that we can use pandas pipe
        return self.OUTPUT

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

        # Save output
        self.OUTPUT = df.copy()

        # return df so that we can use pandas pipe
        return self.OUTPUT

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
    ) -> pd.DataFrame:
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

        # Save output
        self.OUTPUT = df.copy()

        # return df so that we can use pandas pipe
        return self.OUTPUT

    def convert_str_to_uid_int(
        self,
        _df_input: pd.DataFrame,
        col_to_convert_to_int: str,
        int_type: str = "int32",
    ) -> pd.DataFrame:
        """
        This function is used to map unique values in a column to integer with objective of saving memory

        Parameters
        ----------------------------------------
        _df_input (pd.DataFrame): Input dataframe
        col_to_convert_to_int (str): column name in _df_input that needs to coded up using random numbers
        int_type (str): Deafult: "int32" or altenatively use "int64"

        Returns
        ---------------------------------------
        pd.DataFrame: Output dataframe with the str uid repalced with integer uid column
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

        # Save output
        self.OUTPUT = df_input.copy()
        self.UID_MAPPING_DF = df_mapping.copy()

        # return df so that we can use pandas pipe
        return self.OUTPUT
