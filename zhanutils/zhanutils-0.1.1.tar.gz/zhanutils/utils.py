from typing import Dict
import json

def get_secret(secret_json_file: str ) -> Dict:
    """
    get secrets
    Args:
        secret_json_file: a json containing secrets

    Returns: a dictionary containing secrets

    """
    with open(secret_json_file) as myfile:
        return json.load(myfile)
