import pandas as pd
from TCGCSUtils import GCSReader
import logging
import json
logging.basicConfig(format='%(levelname)s -> %(message)s', level=logging.INFO)


class BaseSource(object):
    def __init__(self, service_account_json: str, project: str) -> None:
        self.service_account = service_account_json
        self.project = project
        self.reader = GCSReader(service_account_info=self.service_account, gcp_project=self.project)

    def read_gcs(self, bucket: str, file_path: str, files_format: str, time_execution_value=None,
                 time_execution_type=None):

        if files_format == 'json':
            if time_execution_type is None:
                logging.info('Reading all json files')
                files_list = self.reader.read_from_json(
                    bucket,
                    file_path
                )
            else:
                logging.info(f'Reading json files from the last {time_execution_value} {time_execution_type}')
                files_list = self.reader.read_from_json(
                    bucket,
                    file_path,
                    delta_time_kwargs={time_execution_type: time_execution_value}
                )
        else:
            if time_execution_type is None:
                logging.info('Reading all parquet files')
                files_list = self.reader.read_from_parquet(
                    bucket,
                    file_path
                )
            else:
                logging.info(f'Reading all parquet files from the last {time_execution_value} {time_execution_type}')
                files_list = self.reader.read_from_parquet(
                    bucket,
                    file_path,
                    delta_time_kwargs={time_execution_type: time_execution_value}
                )

        if files_list is None:
            return None

        return files_list

    @staticmethod
    def get_raw_df(files_list: list, is_mongo: bool) -> pd.DataFrame:
        df_files_list = []
        logging.info('Starting to read files list')
        for msg in files_list:
            if msg['op'] == 'd':
                if is_mongo:
                    data = json.loads(msg['before'])
                else:
                    data = msg['before']
                data['__deleted'] = True
            else:
                if is_mongo:
                    data = json.loads(msg['after'])
                else:
                    data = msg['after']
                data['__deleted'] = False
            df_files_list.append(data)

        logging.info('Creating the dataframe')
        raw_df = pd.DataFrame.from_records(df_files_list)

        return raw_df
