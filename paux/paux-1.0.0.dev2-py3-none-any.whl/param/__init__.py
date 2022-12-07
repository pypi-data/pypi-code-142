import numpy as np
import pandas as pd


# 函数中的局部变量变成字典
def to_local(data: dict, filter_keys=['self', '__class__']):
    local_data = {}
    for k, v in data.items():
        if k not in filter_keys:
            local_data[k] = v
    return local_data


def isnull(obj):
    if isinstance(obj, np.ndarray):
        return not obj.any()
    elif type(obj).__name__ == 'NoneType':
        return True
    elif isinstance(obj, int) or isinstance(obj, float):
        if pd.isnull(obj):
            return True
        else:
            return False
    else:
        return not bool(obj)
