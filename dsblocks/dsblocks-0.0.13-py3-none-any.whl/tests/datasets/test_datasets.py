# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/00_tests/datasets/tst.datasets.ipynb.

# %% auto 0
__all__ = ['MyDataSet', 'test_dataset']

# %% ../../../nbs/00_tests/datasets/tst.datasets.ipynb 2
from dsblocks.datasets.datasets import *

# %% ../../../nbs/00_tests/datasets/tst.datasets.ipynb 3
import pytest 
import logging
import os
import joblib
from IPython.display import display

# %% ../../../nbs/00_tests/datasets/tst.datasets.ipynb 4
class MyDataSet (DataSet):
    def __init__ (self, **kwargs):
        super().__init__ (**kwargs)
    def load (self):
        return [2, 1, 3]

# %% ../../../nbs/00_tests/datasets/tst.datasets.ipynb 5
def test_dataset ():
    dataset = MyDataSet ()
    x = dataset.load ()
    assert x==[2, 1, 3]
    assert isinstance(dataset.logger, logging.Logger)

