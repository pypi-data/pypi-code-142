import pandas as pd
from TCGCSUtils import GCSWriter
import logging

logging.basicConfig(format='%(levelname)s -> %(message)s', level=logging.INFO)


class BaseSink(object):
    def __init__(self, service_account_json: str, project: str) -> None:
        self.service_account = service_account_json
        self.project = project
        self.writer = GCSWriter(service_account_info=self.service_account, gcp_project=self.project)

    def write_gcs(self, df: pd.DataFrame, bucket: str, file_path: str, file_name: str, files_format: str) -> None:

        if files_format == 'json':
            logging.info(f'Writing json into {bucket} at {file_path}/{file_name}')
            self.writer.write_json(df, bucket, file_path, file_name)
        else:
            logging.info(f'Writing parquet into {bucket} at {file_path}/{file_name}')
            self.writer.write_parquet(df, bucket, file_path, file_name)

        logging.info('Files saved')