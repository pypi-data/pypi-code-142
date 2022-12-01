import os
import pandas as pd

from cc_py_commons.utils.logger import logger


def load_data(filename):
  path = os.path.join(os.getcwd(), 'test_data', 'raw', filename)
  logger.debug(f"load_data: loading from {path}")

  if (".csv" in filename.lower()):
    data = pd.read_csv(path)
  else:
    data = pd.read_excel(path)

  return data
