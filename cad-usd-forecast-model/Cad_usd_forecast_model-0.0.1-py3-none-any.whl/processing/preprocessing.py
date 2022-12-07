#This module contains functions that will be used to preprocess the train data before fitting the model

from typing import List

import pandas as pd
from forecast_model.config.core import config

def drop_missing_values(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Checks training data for rows with na values and drops them."""
    train_data = input_data.copy()
    train_data.dropna(axis = 0, how ='any', inplace = True)

    return train_data


def drop_unwanted_features(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Removes unwanted columns from training data."""
    train_data = input_data.copy()
    train_data.drop(labels = config.model_config.columns_to_drop, axis = 1, inplace = True)

    return train_data


def rename_cols(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Renames two columns to Propet's expected format."""
    train_data = input_data.copy()
    train_data = train_data.rename(columns = config.model_config.columns_to_rename)

    return train_data


def change_date_to_datetime(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Changes the column with the date to a datetime format."""
    train_data = input_data.copy()
    train_data['ds'] = pd.to_datetime(train_data[config.model_config.column_to_datetime])

    return train_data
