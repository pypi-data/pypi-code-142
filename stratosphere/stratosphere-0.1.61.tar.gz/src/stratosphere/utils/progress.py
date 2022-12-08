import warnings

from stratosphere.utils.environment import is_colab, is_pyodide

with warnings.catch_warnings():
    warnings.simplefilter("ignore")

    if is_colab():
        from tqdm import tqdm
    else:
        from tqdm.auto import tqdm

    if is_pyodide():
        tqdm.monitor_interval = 0


def progress(*args, **kwargs):
    return tqdm(*args, **kwargs)
