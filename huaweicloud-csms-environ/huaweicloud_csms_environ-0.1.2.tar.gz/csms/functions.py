from . import services


def load_env(secret_name: str = None, version_id='latest', **kwargs):
    client = services.Csms(**kwargs)
    client.load_env(secret_name, version_id)


def get(secret_name: str, version_id='latest', **kwargs):
    client = services.Csms(**kwargs)
    return client.get_raw_secret(secret_name, version_id)


def get_json(secret_name: str, version_id='latest', **kwargs):
    client = services.Csms(**kwargs)
    return client.get_json_secret(secret_name, version_id)
