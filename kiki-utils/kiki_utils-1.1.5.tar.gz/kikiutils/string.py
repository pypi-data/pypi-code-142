import random
import re
import string

from typing import Union

from .check import isbytes, isstr


_RANDOM_LETTERS = string.ascii_letters + string.digits


def random_str(min_l: int = 8, max_l: int = 8):
    return ''.join(random.choice(_RANDOM_LETTERS) for i in range(random.randint(min_l, max_l)))


def s2b(text: str, encoding: str = 'utf-8') -> Union[bytes, None]:
    """Convert string to bytes."""

    try:
        if isstr(text):
            return bytes(text, encoding)
        if not isbytes(text):
            raise ValueError('Data is not string or bytes!')
        return text
    except:
        return None


def b2s(byte: bytes, encoding: str = 'utf-8') -> Union[str, None]:
    """Convert bytes to string."""

    try:
        if isbytes(byte):
            return bytes.decode(byte, encoding)
        if not isstr(byte):
            raise ValueError('Data is not bytes or string!')
        return byte
    except:
        return None


# Text

def search_text(
    pattern: re.Pattern,
    text: str,
    group_index: int = 0,
    **kwargs
):
    """Search text by passern and return result."""

    result = re.search(pattern, text, **kwargs)
    return result[group_index] if result else None
