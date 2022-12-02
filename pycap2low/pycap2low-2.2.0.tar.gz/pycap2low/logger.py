import logging

# from settings import FILE_LOG
from pycap2low.settings import FILE_LOG


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

# create console handler and set level to debug
ch = logging.FileHandler(FILE_LOG)
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)
