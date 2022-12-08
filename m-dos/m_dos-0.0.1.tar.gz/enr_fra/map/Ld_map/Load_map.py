#%%
import os
import pandas as pd
import pooch
from enr_fra.map.Ld_map import url_map_reg, url_map_dep, path_target_dep, path_target_reg


class Load_map_dep:
    def __init__(self, url=url_map_dep, target_name=path_target_dep):
        path, fname = os.path.split(path_target_dep)
        pooch.retrieve(url, path=path, fname=fname, known_hash=None)

    @staticmethod
    def save_as_df():
        df_pred = pd.read_csv(
            path_target_dep,
            na_values="",
            low_memory=False,
            converters={"data": str, "heure": str},
        )
        return df_pred

class Load_map_reg:
    def __init__(self, url=url_map_reg, target_name=path_target_reg):
        path, fname = os.path.split(path_target_reg)
        pooch.retrieve(url, path=path, fname=fname, known_hash=None)

    @staticmethod
    def save_as_df():
        df_reg = pd.read_csv(
            path_target_reg,
            na_values="",
            low_memory=False,
            converters={"data": str, "heure": str},
        )
        return df_reg