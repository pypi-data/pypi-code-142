from __future__ import annotations
import base64, struct, binascii, subprocess, logging, re
from pathlib import Path
from hashlib import sha256
from types import FunctionType
from typing import TypeVar
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

RESET = '\033[0m'

BLACK = '\033[0;30m'
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
BLUE = '\033[0;34m'
PURPLE = '\033[0;35m'
CYAN = '\033[0;36m'
WHITE = '\033[0;37m'
GRAY = '\033[0;90m'
BOLD_RED = '\033[0;1;31m'

BLACK_FMT = f'{BLACK}%s{RESET}'
RED_FMT = f'{RED}%s{RESET}'
GREEN_FMT = f'{GREEN}%s{RESET}'
YELLOW_FMT = f'{YELLOW}%s{RESET}'
BLUE_FMT = f'{BLUE}%s{RESET}'
PURPLE_FMT = f'{PURPLE}%s{RESET}'
CYAN_FMT = f'{CYAN}%s{RESET}'
WHITE_FMT = f'{WHITE}%s{RESET}'
GRAY_FMT = f'{GRAY}%s{RESET}'
BOLD_RED_FMT = f'{BOLD_RED}%s{RESET}'


def command(add_arguments: FunctionType = None, doc: str = None, name: str = None):
    """
    A decorator to define attribues for command functions.
    """
    def decorator(func):
        if name is not None:
            func.command_name = name
        if doc is not None:
            func.__doc__ = doc
        if add_arguments is not None:
            func.add_arguments = add_arguments
        return func
    
    return decorator


def check_ssh_public_key(keycontent: str):
    # Source: https://gist.github.com/piyushbansal/5243418

    if not keycontent:
        return

    # Key must have 3 parts
    parts = keycontent.split()
    if len(parts) != 3:
        raise ValueError(f"invalid SSH public key: contains {length(parts)} parts, expected 3: \"{keycontent}\"")
    keynature, keystring, comment = parts

    # Keystring must contain only base64 chars
    try :
        keydata = base64.b64decode(keystring)
    except binascii.Error:
        raise ValueError(f"invalid SSH public key {comment}: keystring contains non-base64 chars")
    
    # Verify some properties of ssh keys:
    # - from data[:4], it must be equal to 7
    # - data[4:11] must equal keynature
    try :
        length = int(struct.unpack('>I', keydata[:4])[0])
    except struct.error :
        raise ValueError(f"invalid SSH public key {comment}: cannot unpack keydata")
    
    if length != 7:
        raise ValueError(f"invalid SSH public key {comment}: len is {length}, expected 7")

    actual_keynature = keydata[4:4+length].decode('ascii')
    if actual_keynature != keynature:
        raise ValueError(f"invalid SSH public key {comment}: actual keynature is {actual_keynature}, expected {keynature}")


T = TypeVar('T', str, Path) 

def without_j2(path: T) -> T:
    if path is None:
        return None

    if isinstance(path, str):
        return path[:-3] if path.endswith(".j2") else path    
    else:
        return path.parent.joinpath(without_j2(path.name))


def verify_gpg_signature(signature, public_key):
    logger.info("verify gpg signature: %s", signature)

    cmd = ["gpg", "--no-default-keyring", "--keyring", public_key, "--verify", signature]
    cp = subprocess.run(cmd, capture_output=True, text=True)
    
    if cp.returncode != 0:
        message = "gpg verification of %s returned code %s" % (signature, cp.returncode)
        
        if value := cp.stdout.strip():
           message +=(f", stdout: {value}")

        if value := cp.stderr.strip():
           message +=(f", stderr: {value}")
    
        logger.error(message)
        return False
    
    return True


def verify_sha256_hash(file: Path|str, sums_file: Path|str):
    if not isinstance(file, Path):
        file = Path(file)
    if not isinstance(sums_file, Path):
        sums_file = Path(sums_file)

    # Read expected sha256sum
    expected_sum = None
    for m in re.findall(r"([0-9a-f]+)\s+([^\s]+)", sums_file.read_text()):
        if m[1] == file.name:
            expected_sum = m[0]
            break 

    if not expected_sum:
        logger.error("cannot find expected sha256sum for %s" % file.name)
        return False

    # Verify ISO sha256sum
    logger.info("verify sha256 hash: %s", file)
    hash = sha256()
    with open(file, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            hash.update(byte_block)

        actual_sha256sum = hash.hexdigest()
        if actual_sha256sum != expected_sum:
            logger.error("invalid sha256sum for %s\nactual: %s\nexpected: %s" % (file.name, actual_sha256sum, expected_sum))
            return False

    return True

class ElementInfo:
    path: str
    relative_path: str
    is_dir: str
    is_file: str
    size: int
    last_modified: datetime

    def __init__(self, path: str|Path, relative_to: str|Path = None):
        if not isinstance(path, Path):
            path = Path(path)

        self.path = path.as_posix()

        if relative_to is not None:
            if not isinstance(relative_to, Path):
                relative_to = Path(relative_to)
            self.relative_path = path.relative_to(relative_to)
        else:
            self.relative_path = self.path

        self.is_dir = path.is_dir()
        self.is_file = path.is_file()
        
        stat = path.stat()
        self.size = stat.st_size
        self.last_modified = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)

    def __str__(self):
        return self.path
