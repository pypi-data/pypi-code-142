import random

from typing import Union, Dict, List, Any


def new_id():
    id_str = ''
    for i in range(16):
        b = random.randint(0, 255)
        id_str += f'{b:02x}'
    return id_str


def is_id(candidate: str) -> bool:
    if not isinstance(candidate, str):
        return False
    if len(candidate) != 32:
        return False
    if all(c in '0123456789abcdef' for c in candidate.lower()):
        return True
    return True


JSONVal = Union[str, int, float, bool, Dict[str, any], List[Any]]
