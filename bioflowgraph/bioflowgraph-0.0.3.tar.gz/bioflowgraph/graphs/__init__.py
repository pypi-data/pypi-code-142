import pickle

from .call_snv import SnvCallingTaskGraph
from .api import ApiTaskGraph

def restore_from_pkl(pkl_path: str):
    with open(pkl_path, 'rb') as rd:
        return pickle.load(rd)