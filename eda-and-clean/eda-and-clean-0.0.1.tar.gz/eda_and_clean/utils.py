import pandas as pd


def generate_outlier_mask_based_on_iqr(df, col_name, iqr_multiplier=1.5):
    """
    Generates a mask for a given column in a dataframe based on the interquartile range.
    :param df: Pandas dataframe
    :param col_name: Column name
    :param iqr_multiplier: Multiplier for the interquartile range
    :return: Mask
    """
    q1 = df[col_name].quantile(0.25)
    q3 = df[col_name].quantile(0.75)
    iqr = q3 - q1
    outlier_mask = (df[col_name] < (q1 - iqr_multiplier * iqr)) & (
        df[col_name] > (q3 + iqr_multiplier * iqr)
    )
    return outlier_mask


def generate_outlier_mask_based_on_z_score(df, col_name, z_score_threshold=3):
    """
    Generates a mask for a given column in a dataframe based on the z-score.
    :param df: Pandas dataframe
    :param col_name: Column name
    :param z_score_threshold: Z-score threshold
    :return: Mask
    """
    z_score = (df[col_name] - df[col_name].mean()) / df[col_name].std()
    outlier_mask = (z_score > z_score_threshold) | (z_score < -z_score_threshold)
    return outlier_mask


def filter_non_capitalized_words_from_list(_list: list) -> list:
    return [word for word in _list if word.isupper()]
