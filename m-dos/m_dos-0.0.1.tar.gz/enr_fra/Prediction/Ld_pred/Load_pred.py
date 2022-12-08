import os
import pandas as pd
import pooch
from enr_fra.Prediction.Ld_pred import url_pred, path_target

class Load_pred:
    def __init__(self, url=url_pred, target_name=path_target):
        path, fname = os.path.split(path_target)
        pooch.retrieve(url, path=path, fname=fname, known_hash=None)

    @staticmethod
    def save_as_df():
        df_bikes = pd.read_csv(
            path_target,
            na_values="",
            low_memory=False,
            converters={"data": str, "heure": str},
        )
        return df_bikes
