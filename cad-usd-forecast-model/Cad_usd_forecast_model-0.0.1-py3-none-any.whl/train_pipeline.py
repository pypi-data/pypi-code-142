#This module contains the code & function for training the forecast_model

import numpy as np
import pandas as pd
from config.core import config #Config class holds the config variables for the package & model
from processing.data_manager import load_dataset, save_pipeline #the data manager module has functions for loading data, saving new pipelines etc
from processing.preprocessing import drop_missing_values, drop_unwanted_features, rename_cols, change_date_to_datetime
from prophet import Prophet


def run_training() -> None:
    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.app_config.training_data_file)

    #Check for & drop missing values
    data_without_na = drop_missing_values(input_data = data)

    #Drop unwanted columns
    data_without_othercols = drop_unwanted_features(input_data=data_without_na)

    #Rename columns
    data_with_renamed = rename_cols(input_data=data_without_othercols)

    #Change Date column to datetime object
    data_date_to_datetime = change_date_to_datetime(input_data=data_with_renamed)

    cleaned_data = data_date_to_datetime

    #Create the model
    forecast_pipeline = Prophet()

    #fit the model to the cleaned training data
    forecast_pipeline.fit(cleaned_data)

    # persist the trained model
    save_pipeline(pipeline_to_persist=forecast_pipeline)


if __name__ == "__main__":
    run_training()
