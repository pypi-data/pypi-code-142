from typing import Union

def parse_to_number(num: str) -> Union[float,int]:
    try:
        return int(num)
    except ValueError:
        return float(num)