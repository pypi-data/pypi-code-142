import numpy as np
import pandas as pd

from forecast_model import __version__ as _version
from forecast_model.config.core import config
from forecast_model.processing.data_manager import load_pipeline


pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
_forecast_pipe = load_pipeline(file_name=pipeline_file_name)

def get_forecast(*,forecast_period: int,) -> dict:
    """Make a prediction using a saved model pipeline."""

    #results = {"predictions": None, "version": _version, "errors": errors}

    errors = None


    try:
        future_df = _forecast_pipe.make_future_dataframe(periods = forecast_period, freq='B')
        forecast = _forecast_pipe.predict(future_df)
        #take only the predictions out of the DataFrame
        predictions = forecast.iloc[-forecast_period:]
        forecast_dates = list(predictions['ds'])
        forecast_prices = list(predictions['yhat'])

    except TypeError:
        errors = 'Oops! Looks like your forecast time frame isnt valid'

    results = {"forecast_dates": forecast_dates, "forecast_prices": forecast_prices,"version": _version, "errors": errors}

    return results
