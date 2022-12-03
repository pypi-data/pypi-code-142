import pandas as pd
import numpy as np
from eda_and_beyond.eda_tools import histograms_numeric_columns
from .chart import plotly_heatmap, line_plotly
from klib import cat_plot
from operator import attrgetter
from .utils import filter_non_capitalized_words_from_list


class eda_class:
    def __init__(self, _df: pd.DataFrame, categorical_data: list = None) -> None:
        df = _df.copy()

        self.raw_input = df.copy()
        self.DTYPES = {}
        self.DOWNCASTING = {}
        self.MISSING_VALUES = {}
        self.DUPLICATES = {}
        self.DATA_ANALYSIS = {}

        # OUTPUT

        # Identifying dtypes
        self.DTYPES["boolean_like_columns"] = self.identify_boolean_like_columns()
        self.DTYPES[
            "categorical_like_columns"
        ] = self.identify_categorical_like_columns()
        self.DTYPES["datetime_like_columns"] = self.identify_datetime_like_columns()
        self.DTYPES["potential_uid_columns"] = self.find_unique_identifier_columns()

        # Interim calculations
        self.correlation_matrix_numerical = self.make_upper_triangle_na(
            _df=self.make_diagonals_na(_df=self.raw_input.corr())
        )
        self.correlation_matrix_non_numerical = (
            self.get_correlation_of_non_numerical_columns()
        )

        # Downcasting options
        self.DOWNCASTING[
            "to_float32"
        ] = self.determine_candidates_for_float32_conversion()

        # Missing values
        self.MISSING_VALUES[
            "columns_with_no_null_values"
        ] = self.generate_list_of_columns_with_no_null_values()
        self.MISSING_VALUES[
            "columns_with_null_values"
        ] = self.generate_list_of_columns_with_null_values()
        self.MISSING_VALUES[
            "percentage_of_missing_values"
        ] = self.generate_dataframe_with_percentage_of_missing_values()
        self.MISSING_VALUES[
            "percentage_of_non_missing_values"
        ] = self.generate_dataframe_with_percentage_of_non_missing_values()
        self.MISSING_VALUES[
            "dates_continuity_check"
        ] = self.identify_if_dates_are_continuous()
        self.MISSING_VALUES["plotly_missing_values_heatmap"] = plotly_heatmap(
            _df=self.raw_input.isnull(), title="Missing Values Heatmap"
        )
        self.MISSING_VALUES["plotly_correlation_missing_values"] = plotly_heatmap(
            _df=self.generate_correlation_of_missing_values(),
            title="Correlation of Missing Values",
        )

        # Duplicates
        self.DUPLICATES["redundant_columns"] = self.identify_redundant_columns()

        # Data analysis
        self.DATA_ANALYSIS["plotly_correlation_numerical"] = plotly_heatmap(
            _df=self.correlation_matrix_numerical,
            title="Correlation Matrix Numerical",
        )
        self.DATA_ANALYSIS["plotly_correlation_non_numerical"] = plotly_heatmap(
            _df=self.correlation_matrix_non_numerical,
            title="Correlation Matrix Non Numerical",
        )
        self.DATA_ANALYSIS["histogram_matplotlib"] = histograms_numeric_columns(
            df=self.raw_input,
            numerical_columns=self.raw_input.select_dtypes(include="number"),
        ).figure

        # Categorical plot
        if categorical_data is None:
            self.categorical_data = self.DTYPES["categorical_like_columns"]
        else:
            self.categorical_data = categorical_data
        self.DATA_ANALYSIS["categorical_plot"] = cat_plot(
            self.raw_input[self.categorical_data]
        ).figure
        self.DATA_ANALYSIS["describe"] = self.generate_dataframe_describe(
            _df=self.raw_input
        )
        self.DATA_ANALYSIS[
            "top_10_most_frequent_values"
        ] = self.identify_top_n_most_frequent_value_across_non_numeric_columns(n=10)

    def identify_if_dates_are_continuous(self) -> bool:
        _df = self.raw_input.copy()
        df_datetime_continuity = pd.DataFrame(
            columns=["col", "freq", "max_value_of_diff_between_periods"]
        )

        for date_col in self.DTYPES["datetime_like_columns"]:
            df_temp = _df.copy()
            df_temp[date_col] = pd.to_datetime(df_temp[date_col])

            for freq in ["D", "M", "Q", "A"]:
                df = df_temp.copy()
                df[date_col + "_period"] = df[date_col]
                df = df.set_index(date_col + "_period")
                df.index = df.index.to_period(freq=freq)
                df = df.reset_index()
                df = df.groupby([date_col + "_period"]).sum().reset_index()
                df["period_diff"] = df[date_col + "_period"].diff()
                if df["period_diff"].iloc[1:].isna().any():
                    max_val = np.nan
                max_val = df["period_diff"].iloc[1:].apply(attrgetter("n")).max()

                # Record info
                df_datetime_continuity_temp = pd.DataFrame(
                    [[date_col, freq, max_val]],
                    columns=["col", "freq", "max_value_of_diff_between_periods"],
                )
                df_datetime_continuity = pd.concat(
                    [df_datetime_continuity, df_datetime_continuity_temp], axis=0
                )

        return df_datetime_continuity

    def generate_dataframe_describe(self, _df: pd.DataFrame) -> pd.DataFrame:
        df = _df.copy()
        df_describe = df.describe()
        return self.add_additional_columns_to_describe(
            _df_or_groupby_object=df, _df_describe=df_describe
        )

    def add_additional_columns_to_describe(
        self, _df_or_groupby_object, _df_describe: pd.DataFrame
    ) -> pd.DataFrame:
        """
        _df could be a dataframe or a groupby object
        """
        if type(_df_or_groupby_object) == pd.DataFrame:
            df = _df_or_groupby_object.copy()
        else:
            df = _df_or_groupby_object
        df_describe = _df_describe.copy()

        # Calculate required metrics
        IQR = df_describe.loc["75%"] - df_describe.loc["25%"]
        IQR_lower = df_describe.loc["25%"] - 1.5 * IQR
        IQR_upper = df_describe.loc["75%"] + 1.5 * IQR
        quantile_95 = df.quantile(0.95)
        quantile_5 = df.quantile(0.05)
        mean_plus_2_std = df_describe.loc["mean"] + 2 * df_describe.loc["std"]
        mean_minus_2_std = df_describe.loc["mean"] - 2 * df_describe.loc["std"]
        sum = df.sum()

        # Insert into df_describe
        df_describe.loc["IQR"] = IQR
        df_describe.loc["IQR_lower"] = IQR_lower
        df_describe.loc["IQR_upper"] = IQR_upper
        df_describe.loc["95%"] = quantile_95
        df_describe.loc["5%"] = quantile_5
        df_describe.loc["mean+2*std"] = mean_plus_2_std
        df_describe.loc["mean-2*std"] = mean_minus_2_std
        df_describe.loc["sum"] = sum

        # Reorder rows
        df_describe = df_describe.reindex(
            [
                "sum",
                "count",
                "mean",
                "std",
                "mean-2*std",
                "IQR_lower",
                "min",
                "5%",
                "25%",
                "50%",
                "75%",
                "95%",
                "max",
                "IQR_upper",
                "mean+2*std",
                "IQR",
            ]
        )

        return df_describe

    def generate_list_of_columns_with_null_values(self) -> list:
        df = self.raw_input.copy()
        return df.columns[df.isnull().any()].tolist()

    def generate_list_of_columns_with_no_null_values(self) -> list:
        df = self.raw_input.copy()
        return df.columns[df.notnull().all()].tolist()

    def generate_correlation_of_missing_values(self) -> pd.DataFrame:
        df_null = self.raw_input.copy().isnull()
        df_null = df_null[df_null.any(axis=1)]
        return df_null.corr()

    def generate_dataframe_with_percentage_of_missing_values(
        self, without_formating: bool = False
    ) -> pd.DataFrame:
        df = self.raw_input.copy()
        df_output = pd.DataFrame(
            df.isnull().sum() / len(df), columns=["percentage_missing_values"]
        )
        if without_formating:
            return df_output
        df_output = self.convert_float_to_percentage_in_dataframe(
            _df=df_output, cols=["percentage_missing_values"]
        )
        return df_output

    def generate_dataframe_with_percentage_of_non_missing_values(self) -> pd.DataFrame:
        df_output = self.generate_dataframe_with_percentage_of_missing_values(
            without_formating=True
        )
        df_output = df_output.rename(
            columns={"percentage_missing_values": "percentage_non_missing_values"}
        )
        df_output = 1 - df_output
        return df_output

    def convert_float_to_percentage_in_dataframe(
        self, _df: pd.DataFrame, cols: list
    ) -> pd.DataFrame:
        df = _df.copy()
        df[cols] = df[cols].applymap(lambda x: "{:.2%}".format(x))
        return df

    def top_n_most_frequent_values_in_column(
        self, _df: pd.DataFrame, col: str, n: int
    ) -> pd.DataFrame:
        df = _df.copy()
        return df[col].value_counts().head(n).reset_index()["index"]

    def identify_top_n_most_frequent_value_across_non_numeric_columns(
        self, n: int = 5
    ) -> pd.DataFrame:
        df = self.raw_input.copy()
        df_output = pd.DataFrame()
        for col in df.select_dtypes(exclude=[np.number]).columns:
            df_output[col] = self.top_n_most_frequent_values_in_column(
                _df=df, col=col, n=n
            )
        return df_output

    def get_attributes_of_class(self) -> list:
        return [
            attr
            for attr in dir(self)
            if not callable(getattr(self, attr)) and not attr.startswith("__")
        ]

    def get_output_attributes_of_class(self) -> list:
        all_attributes = self.get_attributes_of_class()
        return filter_non_capitalized_words_from_list(_list=all_attributes)

    def identify_boolean_like_columns(self) -> list:
        df = self.raw_input.copy()
        boolean_like_columns = []
        for col in df.columns:
            # Drop NA values
            df_temp = df[[col]].copy()
            df_temp = df_temp.dropna()

            # Now check if the column is boolean like
            if len(df[col].unique()) <= 2:
                boolean_like_columns.append(col)
        return boolean_like_columns

    def identify_redundant_columns(self) -> dict:
        df = self.raw_input.copy()
        redundant_columns_na_count = {}
        for col in df.columns:
            # Drop NA values
            df_temp = df[[col]].copy()
            len_pre_dropna = len(df_temp)
            df_temp = df_temp.dropna()
            len_post_dropna = len(df_temp)

            # Now check if the column is redundant
            if len(df[col].unique()) == 1:
                redundant_columns_na_count[col] = len_pre_dropna - len_post_dropna

        return redundant_columns_na_count

    def make_upper_triangle_na(self, _df: pd.DataFrame) -> pd.DataFrame:
        df = _df.copy()
        mask = np.triu(np.ones_like(df, dtype=bool))
        df = df.mask(mask)
        return df

    def identify_categorical_like_columns(self) -> list:
        df = self.raw_input.copy()
        categorical_like_columns = []
        for col in df.columns:
            # Drop NA values
            df_temp = df[[col]].copy()
            df_temp = df_temp.dropna()

            # Now check if the column is categorical like
            if len(df[col].unique()) > 2 and len(df[col].unique()) < 1 / 3 * len(df):
                categorical_like_columns.append(col)
        return categorical_like_columns

    def make_diagonals_na(self, _df: pd.DataFrame) -> pd.DataFrame:
        df = _df.copy()
        # fluctuating diagonals
        df.values[[np.arange(df.shape[0])] * 2] = np.nan
        return df

    def get_correlation_of_non_numerical_columns(self) -> pd.DataFrame:
        df = self.raw_input.copy()
        df = df.select_dtypes(exclude=[np.number])
        df = df.apply(lambda col: pd.factorize(col)[0])
        df_corr = self.make_diagonals_na(_df=df.corr())
        df_corr = self.make_upper_triangle_na(_df=df_corr)
        return df_corr

    def identify_datetime_like_columns(self) -> pd.DataFrame:
        df = self.raw_input.copy()
        df = df.apply(
            lambda col: pd.to_datetime(col, errors="ignore")
            if col.dtypes == object
            else col,
            axis=0,
        )
        datetime_cols = df.select_dtypes(include=["datetime"]).columns.tolist()
        return datetime_cols

    def filter_non_capitalized_words_from_list(self, _list: list) -> list:
        return [word for word in _list if word.isupper()]

    def get_output_attributes_of_class(self) -> list:
        all_attributes = self.get_attributes_of_class()
        return self.filter_non_capitalized_words_from_list(_list=all_attributes)

    def determine_candidates_for_float32_conversion(self) -> list:
        df = self.raw_input.copy()
        float32_cols = []
        for col in df.columns:
            if df[col].dtype == np.float64:
                if (
                    df[col].min() > np.finfo(np.float32).min
                    and df[col].max() < np.finfo(np.float32).max
                ):
                    float32_cols.append(col)
        return float32_cols

    def find_unique_identifier_columns(self) -> pd.DataFrame:
        df = self.raw_input.copy()
        cols_uid = [
            "column_name",
            "unique_identifier_count",
            "number_of_na",
            "number_of_duplicates",
        ]
        df_uid = pd.DataFrame(columns=cols_uid)
        for col in df.columns:
            # Drop na and count number of na
            df_temp = df[[col]].copy()
            df_temp = df_temp.dropna()
            original_len = len(df)
            non_na_len = len(df_temp)
            number_of_na = original_len - non_na_len

            # Drop duplicates and count number of unique values
            df_temp = df_temp.drop_duplicates()
            unique_identifier_len = len(df_temp[col].unique())
            duplicates_len = non_na_len - unique_identifier_len

            # Check the percentage of unique values
            if unique_identifier_len >= len(df_temp) * 0.9:
                df_uid = pd.concat(
                    [
                        df_uid,
                        pd.DataFrame(
                            [
                                [
                                    col,
                                    unique_identifier_len,
                                    number_of_na,
                                    duplicates_len,
                                ]
                            ],
                            columns=cols_uid,
                        ),
                    ]
                )
        return df_uid

    def calculate_empirical_cdf(self, _df: pd.DataFrame, col: str) -> pd.DataFrame:
        df = _df[[col]].copy()
        df["count"] = 1
        df = df.sort_values(by=col, ascending=True)
        df["cum_count"] = df["count"].cumsum()
        df["cdf"] = df["cum_count"] / df["count"].sum()
        df["1-cdf"] = 1 - df["cdf"]
        df["remaining_count"] = df["count"].sum() - df["cum_count"]

        return df

    def cdf_plotly(self, _df: pd.DataFrame, col: str):
        df_ecdf = self.calculate_empirical_cdf(_df=_df, col=col)

        # generate_chart
        df_ecdf = df_ecdf.round(3)
        fig = line_plotly(
            df=df_ecdf,
            x_col_name=col,
            hover_data=["cum_count", "remaining_count", "1-cdf"],
            title=f"Empirical CDF of {col}",
        )

        return fig

    def generate_describe_after_groupby(
        self, _df: pd.DataFrame, groupby_col_name: list, describe_col_name: str
    ):
        """
        Generates a describe table for multiple columns in a dataframe based on a groupby column.
        :param df: Pandas dataframe
        :param groupby_col_name: Groupby column name
        :param describe_col_names: Describe column names
        :return: Pandas dataframe
        """
        df = _df.copy()
        df_groupby_object = df.groupby(groupby_col_name)
        describe_df = df_groupby_object[describe_col_name].describe().T
        return self.add_additional_columns_to_describe(
            _df_or_groupby_object=df_groupby_object[describe_col_name],
            _df_describe=describe_df,
        )
