import uuid

from .file import read_file, save_file
from .string import b2s


# UUID

def get_uuid(save_path: str = './uuid.uuid'):
    if now_uuid := read_file(save_path):
        return b2s(now_uuid)

    now_uuid = uuid.uuid1()
    now_uuid = str(uuid.uuid1())
    save_file(save_path, now_uuid)
    return now_uuid
