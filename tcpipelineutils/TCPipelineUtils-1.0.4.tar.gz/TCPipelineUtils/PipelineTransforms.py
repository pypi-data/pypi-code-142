import numpy as np
import pandas as pd
import logging

logging.basicConfig(format='%(levelname)s -> %(message)s', level=logging.INFO)


class PipelineTransformations(object):

    @staticmethod
    def clean_df(df):
        df = df.replace({np.nan: None, '': None, 'none': None})

        return df

    @staticmethod
    def transform_data_field(df: pd.DataFrame, cols: list, time_unit='ms') -> pd.DataFrame:
        for col in cols:
            df[col] = pd.to_datetime(df[col], unit=time_unit)

        return df

    @staticmethod
    def remove_mongo_format(df: pd.DataFrame, mongo_subset_dict: dict) -> pd.DataFrame:
        for key, value in mongo_subset_dict.items():
            df[key] = df.get(key).apply(lambda row: row.get(value) if row is not np.nan else None)

        return df

    @staticmethod
    def explode_dict_to_columns(df: pd.DataFrame, columns_to_explode: list):
        for col in columns_to_explode:
            df = pd.concat([df.drop([col], axis=1), df[col].apply(pd.Series)], axis=1)

        return df

    @staticmethod
    def explode_list_to_columns(df: pd.DataFrame, columns_to_explode: list):
        for col in columns_to_explode:
            df = df.explode(col)

        return df

    @staticmethod
    def get_value_from_request(request_json: dict, value: str):
        if request_json and value in request_json:
            return request_json[value]
        else:
            raise Exception(f'No {value} in HTTP call')

