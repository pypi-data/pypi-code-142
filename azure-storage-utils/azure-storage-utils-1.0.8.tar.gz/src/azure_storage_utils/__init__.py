# Standard library imports
import logging
import argparse
from datetime import datetime
import os
import time

# Related third party imports

# Local application/library specific imports
from azure_storage_utils.mapping import ContainerMap
from azure_storage_utils.mapping import MapReporter


class PipelineOperator:

    logger = None
    OUTPUT_NAME_CSV = ""
    OUTPUT_NAME_JSON = ""
    CONTAINTER_NAME = ""
    CONNECTION_STRING_NAME = 'STORAGE_CONNECTION_STRING'

    def __init__(self, conn_str: str, storage_url: str, container_name: str, map_file_name=f"storage_map_{datetime.now().strftime('%Y_%m')}.json"):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)
        self.OUTPUT_NAME_JSON = map_file_name
        if '.json' not in self.OUTPUT_NAME_JSON:
            self.OUTPUT_NAME_JSON += ".json"
        self.OUTPUT_NAME_CSV = map_file_name.replace('json', 'csv')
        self.CONTAINTER_NAME = container_name
        conn_str = self._check_conn_str(
            conn_str=conn_str, storage_url=storage_url)
        os.environ['STORAGE_CONNECTION_STRING'] = conn_str
        self.logger.info(
            f"### Init complete for {storage_url}, preparing auth...")

    def collect_pipeline_data(self):
        container_mapper = ContainerMap(conn_string_name=self.CONNECTION_STRING_NAME,
                                        container_name=self.CONTAINTER_NAME, map_file_name=self.OUTPUT_NAME_JSON)
        storage_map = container_mapper.map_container()
        container_mapper.write_map_local(storage_map)
        map_reporter = MapReporter(storage_map=storage_map, depth=2)
        csv_data = map_reporter.print_csv()
        with open(self.OUTPUT_NAME_CSV, "w") as file:
            file.write(csv_data)

    def _check_conn_str(self, conn_str: str, storage_url: str) -> str:

        for kw in ['BlobEndpoint', 'QueueEndpoint', 'TableEndPoint', 'FileEndPoint', 'SharedAccessSignature', 'sv']:
            if kw not in conn_str:
                token = ""
                if 'sv=' in conn_str:
                    token = conn_str[conn_str.index('sv='):]
                conn_str = f"BlobEndPoint={storage_url};QueueEndPoint={storage_url};FileEndPoint={storage_url};TableEndPoint={storage_url};SharedAccessSignature="
                self.logger.warning(
                    f"Detected an invalid connection string not matching the format:\n" +
                    f"<BlobEndpoint=https://contosostorageaccount.blob.core.windows.net/;QueueEndpoint=https://contosostorageaccount.queue.core.windows.net/;FileEndpoint=https://contosostorageaccount.file.core.windows.net/;TableEndpoint=https://contosostorageaccount.table.core.windows.net/;SharedAccessSignature=sv=...>" +
                    f"\nAttempting to reconstruct connection string starting with:\n" +
                    f"{conn_str}...")
                conn_str += token
                time.sleep(10)
                break
        return conn_str


if __name__ == '__main__':
    """Initializes a pipeline operator to collect storage account metadata from the specified container.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--conn_str', type=str, required=True, help="Azure Storage Container connection string in the format: <BlobEndpoint=https://contosostorageaccount.blob.core.windows.net/;QueueEndpoint=https://contosostorageaccount.queue.core.windows.net/;FileEndpoint=https://contosostorageaccount.file.core.windows.net/;TableEndpoint=https://contosostorageaccount.table.core.windows.net/;SharedAccessSignature=sv=...>")
    parser.add_argument('--storage_url', type=str, required=True)
    parser.add_argument('--container_name', type=str, required=True)
    parser.add_argument('--map_name', type=str, required=False,
                        default=f"storage_map_{datetime.now().strftime('%Y_%m')}.json")
    args = parser.parse_args()
    pipeline_operator = PipelineOperator(conn_str=args.conn_str, storage_url=args.storage_url,
                                         container_name=args.container_name, map_file_name=args.map_name)
    pipeline_operator.collect_pipeline_data()
