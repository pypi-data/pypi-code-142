import os

from . import services


def load_env(secret_name: str = None, version_id='latest', **kwargs):
    if secret_name is None:
        secret_name = os.environ.get('HUAWEICLOUD_SECRET_NAME')
    assert secret_name, 'Secret name is not set'

    client = services.CsmsService(**kwargs)
    secrets = client.get_json_secret(secret_name, version_id)
    for key, value in secrets.items():
        os.environ[key] = value
