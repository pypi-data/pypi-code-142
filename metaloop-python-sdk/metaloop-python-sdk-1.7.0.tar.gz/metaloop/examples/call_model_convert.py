from typing import Dict
from metaloop.client import MDS

if __name__ == '__main__':
    mds_client = MDS("0c02ca70e142b75a75ca4118ce33dbb0", "http://192.168.100.71:30301")
    mc: Dict[str, any] = {
                "mpid": 6985,
                "enc_way": "NetWork",
                "minio_path": "minio_path",
                "ftp_path": "ftp_path",
                "secret_key": "secret_key",
                "status": 1,
                "is_arm": False
    }
    mds_client.call_model_convert_path_status(mc)