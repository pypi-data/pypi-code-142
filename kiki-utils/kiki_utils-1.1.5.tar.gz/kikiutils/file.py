import aiofiles
import io
import magic
import os
import shutil

from typing import Callable, Union


# File

async def async_read_file(path: str, **kwargs):
    """Async read file."""

    async with aiofiles.open(path, 'rb', **kwargs) as f:
        return await f.read()


async def async_save_file(
    path: str,
    file: Union[bytes, io.BytesIO, io.FileIO, str],
    replace: bool = True,
    **kwargs
):
    """Async save file."""

    mode = 'w' if isinstance(file, str) else 'wb'

    try:
        if os.path.exists(path) and not replace:
            raise FileExistsError()
        if getattr(file, 'read', None):
            file = file.read()

        async with aiofiles.open(path, mode, **kwargs) as f:
            await f.write(file)

        return True
    except:
        return False


def clear_dir(path: str):
    """Clear dir. (Remove and create.)"""

    rmdir(path)
    mkdirs(path)


def del_file(path: str):
    """Del file."""

    try:
        os.remove(path)
        return True
    except:
        return False


def get_file_mime(file: Union[bytes, io.BytesIO, io.FileIO]):
    """Get file mime."""

    is_file = getattr(file, 'read', None) != None
    data = file.read(2048) if is_file else file[:2048]
    file_mime = magic.from_buffer(data, mime=True)

    if is_file:
        file.seek(0)
    if file_mime:
        return file_mime.split('/')


def mkdir(path: str):
    """Create dir."""

    try:
        os.mkdir(path)
        return True
    except:
        return False


def mkdirs(path: str):
    """Create dir (use makedirs)."""

    try:
        os.makedirs(path)
        return True
    except:
        return False


def read_file(path: str):
    """Read file."""

    try:
        with open(path, 'rb') as f:
            data = f.read()
            return data
    except:
        pass


def rmdir(path: str):
    """Remove dir."""

    try:
        shutil.rmtree(path)
        return True
    except:
        return False


def save_file(
    path: str,
    file: Union[bytes, io.BytesIO, io.FileIO, str],
    replace: bool = True
):
    """Save file."""

    mode = 'w' if isinstance(file, str) else 'wb'

    try:
        if os.path.exists(path) and not replace:
            raise FileExistsError()
        if getattr(file, 'read', None):
            file = file.read()
        with open(path, mode) as f:
            f.write(file)
        return True
    except:
        return False


def save_file_as_bytesio(
    save_fnc: Callable,
    get_bytes: bool = False,
    **kwargs
):
    """Save file to io.BytesIO."""

    with io.BytesIO() as output:
        save_fnc(output, **kwargs)
        file_bytes = output.getvalue()

    if get_bytes:
        return file_bytes

    return io.BytesIO(file_bytes)


def move_file(path: str, target_path: str):
    """Move file or dir."""

    try:
        shutil.move(path, target_path)
        return True
    except:
        return False


def rename(path: str, name: str):
    """Rename file or dir."""

    try:
        os.rename(path, name)
        return True
    except:
        return False
