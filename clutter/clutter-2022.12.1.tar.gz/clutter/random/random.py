import logging
import random
from datetime import datetime
from typing import Union

logger = logging.getLogger(__file__)


def is_test_date(_datetime: Union[str, datetime], *, test_ratio=0.1):
    if not isinstance(_datetime, datetime):
        _datetime = datetime.fromisoformat(_datetime)
    _datetime = _datetime.strftime("%Y%m%d%H%M%S")
    random.seed(_datetime)
    r = random.random()
    if r < test_ratio:
        return True
    return False
