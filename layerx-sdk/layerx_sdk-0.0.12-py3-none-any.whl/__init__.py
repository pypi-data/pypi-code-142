import base64

from layerx import datalake, dataset


class LayerxClient:
    """
    Python SDK of LayerX
    """

    def __init__(self, api_key: str, secret: str, layerx_url: str) -> None:
        _string_key_secret = f'{api_key}:{secret}'
        _key_secret_bytes = _string_key_secret.encode("ascii")
        _encoded_key_secret_bytes = base64.b64encode(_key_secret_bytes)
        self.encoded_key_secret = _encoded_key_secret_bytes.decode("ascii")
        self.layerx_url = layerx_url

    def upload_annoations_for_folder(
            self,
            collection_base_path: str,
            operation_unique_id: str,
            json_data_file_path: str,
            shape_type: str,
            is_normalized: bool,
            is_model_run: bool
    ):
        """
        Upload annotation data from a json file
        """
        # init datalake client
        _datalake_client = datalake.DatalakeClient(self.encoded_key_secret, self.layerx_url)

        if is_model_run:
            _datalake_client.upload_modelrun_from_json(
                collection_base_path,
                operation_unique_id,
                json_data_file_path,
                shape_type,
                is_normalized
            )
        else:
            _datalake_client.upload_groundtruth_from_json(
                collection_base_path,
                operation_unique_id,
                json_data_file_path,
                shape_type,
                is_normalized)

    """
    Download dataset """

    def download_dataset(self, version_id: str, export_type: str):
        # init dataset client
        _dataset_client = dataset.DatasetClient(self.encoded_key_secret, self.layerx_url)

        # start download
        _dataset_client.download_dataset(version_id, export_type)

    """"
    Images/vidoe upload
    """

    def file_upload(self, path: str, collection_type, collection_name, meta_data_object="", override=False):
        _datalake_client = datalake.DatalakeClient(self.encoded_key_secret, self.layerx_url)
        _datalake_client.file_upload(path, collection_type, collection_name, meta_data_object, override)

    """
    Download collection annotations
    From datalake
    @param collection_id - id of dataset version """

    def download_collection(self, collection_id: str):
        # init dataset client
        _dataset_client = dataset.DatasetClient(self.encoded_key_secret, self.layerx_url)

        # start download
        _dataset_client.download_collection(collection_id)
