import pandas as pd


def output_1_dtypes_fixture():
    # Dtypes
    dtypes_test_1 = {}
    dtypes_test_1["boolean_like_columns"] = ["random"]
    dtypes_test_1["datetime"] = ["date"]
    dtypes_test_1["categorical_like_columns"] = []
    dtypes_test_1["potential_uid_columns"] = pd.DataFrame(
        {
            "column_name": {
                0: "uid",
                1: "date",
                2: "id",
                3: "desc",
                4: "value",
                5: "volume",
                6: "random",
            },
            "unique_identifier_count": {0: 16, 1: 5, 2: 7, 3: 7, 4: 8, 5: 7, 6: 1},
            "number_of_explicit_na": {0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 2, 6: 2},
            "number_of_duplicates": {0: 1, 1: 12, 2: 10, 3: 10, 4: 8, 5: 8, 6: 14},
        }
    )

    # Not tested keys
    not_tested_keys = []

    return dtypes_test_1, not_tested_keys


def output_1_summary_fixture():
    summary_test_1 = {}
    summary_test_1["describe"] = pd.DataFrame(
        {
            "uid": {
                "sum": 137.0,
                "count": 17.0,
                "mean": 8.058823529411764,
                "std": 4.955685979701677,
                "mean-2*std": -1.8525484299915895,
                "IQR_lower": -8.0,
                "min": 1.0,
                "5%": 1.0,
                "25%": 4.0,
                "50%": 8.0,
                "75%": 12.0,
                "95%": 15.2,
                "max": 16.0,
                "IQR_upper": 24.0,
                "mean+2*std": 17.97019548881512,
                "IQR": 8.0,
            },
            "value": {
                "sum": 20000367.0,
                "count": 16.0,
                "mean": 1250022.9375,
                "std": 4999993.883383731,
                "mean-2*std": -8749964.829267463,
                "IQR_lower": -20.0,
                "min": 5.0,
                "5%": 5.0,
                "25%": 10.0,
                "50%": 20.0,
                "75%": 30.0,
                "95%": 5000075.0,
                "max": 20000000.0,
                "IQR_upper": 60.0,
                "mean+2*std": 11250010.704267463,
                "IQR": 20.0,
            },
            "volume": {
                "sum": 63.0,
                "count": 15.0,
                "mean": 4.2,
                "std": 2.596701204000403,
                "mean-2*std": -0.9934024080008061,
                "IQR_lower": -4.0,
                "min": 1.0,
                "5%": 1.0,
                "25%": 2.0,
                "50%": 4.0,
                "75%": 6.0,
                "95%": 8.599999999999998,
                "max": 10.0,
                "IQR_upper": 12.0,
                "mean+2*std": 9.393402408000807,
                "IQR": 4.0,
            },
            "random": {
                "sum": 15.0,
                "count": 15.0,
                "mean": 1.0,
                "std": 0.0,
                "mean-2*std": 1.0,
                "IQR_lower": 1.0,
                "min": 1.0,
                "5%": 1.0,
                "25%": 1.0,
                "50%": 1.0,
                "75%": 1.0,
                "95%": 1.0,
                "max": 1.0,
                "IQR_upper": 1.0,
                "mean+2*std": 1.0,
                "IQR": 0.0,
            },
        }
    )

    # Not tested keys
    not_tested_keys = ["info"]

    return summary_test_1, not_tested_keys


def output_1_missing_values_fixture():
    missing_values_test_1 = {}
    missing_values_test_1["dates_continuity_check"] = pd.DataFrame(
        {
            "col": {0: "date", 1: "date", 2: "date", 3: "date"},
            "freq": {0: "D", 1: "M", 2: "Q", 3: "A"},
            "max_value_of_diff_between_periods": {0: 92, 1: 3, 2: 1, 3: 1},
        }
    )
    missing_values_test_1["na_like_values_in_str_columns"] = {
        "id": ["na"],
        "desc": [""],
    }
    missing_values_test_1["na_in_datetime_columns"] = {"date": []}
    # Not tested keys
    not_tested_keys = [
        "plotly_missing_values_heatmap",
        "plotly_correlation_missing_values",
    ]

    return missing_values_test_1, not_tested_keys


def output_1_downcasting_fixture():
    downcasting_test_1 = {}
    downcasting_test_1["to_float32"] = ["value", "volume", "random"]

    # Not tested keys
    not_tested_keys = []

    return downcasting_test_1, not_tested_keys


def output_1_duplicates_fixture():
    duplicate_test_1 = {}
    duplicate_test_1["redundant_columns"] = {"random": 2}
    duplicate_test_1["duplicate_rows"] = [0, 1]

    # Not tested keys
    not_tested_keys = []

    return duplicate_test_1, not_tested_keys


def output_1_data_analysis_fixture():
    data_analysis_test_1 = {}
    data_analysis_test_1["top_10_most_frequent_values"] = pd.DataFrame(
        {
            "date": {
                0: pd.to_datetime("2020-03-31 00:00:00"),
                1: pd.to_datetime("2020-09-30 00:00:00"),
                2: pd.to_datetime("2020-12-31 00:00:00"),
                3: pd.to_datetime("2020-06-30 00:00:00"),
                4: pd.to_datetime("2019-12-31 00:00:00"),
            },
            "id": {0: "A", 1: "B", 2: "C", 3: "na", 4: "E"},
            "desc": {
                0: "this is A",
                1: "this is B",
                2: "this is C",
                3: "",
                4: "this is E",
            },
        }
    )

    # Not tested keys
    not_tested_keys = [
        "plotly_correlation_numerical",
        "plotly_correlation_non_numerical",
        "histogram_matplotlib",
    ]

    return data_analysis_test_1, not_tested_keys
