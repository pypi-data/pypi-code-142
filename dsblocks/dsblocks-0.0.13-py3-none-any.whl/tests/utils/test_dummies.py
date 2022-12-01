# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/00_tests/utils/tst.dummies.ipynb.

# %% auto 0
__all__ = ['test_dummy_classifier']

# %% ../../../nbs/00_tests/utils/tst.dummies.ipynb 2
from dsblocks.utils.dummies import *

# %% ../../../nbs/00_tests/utils/tst.dummies.ipynb 3
import pytest
import os
import joblib
from IPython.display import display
import pandas as pd
import numpy as np
import logging
import shutil
from pathlib import Path

import dsblocks.config.bt_defaults as dflt

# %% ../../../nbs/00_tests/utils/tst.dummies.ipynb 4
def test_dummy_classifier ():
    X = np.array ([[2,1,3], [4,6,5], [10,20,30], [40, 50, 60]])
    y = np.array ([0, 1, 0, 1])
    cl = DummyClassifier (project_op='min', statistic='min')
    assert (cl.project_op (X)==np.array([1, 4, 10, 40])).all()
    assert (cl.fit_apply (X, y)==np.array([-2999, -2996, -2990, -2960])).all()
    assert cl.estimator=={'statistic_0': 1, 'statistic_1': 4, 'statistic': -3000}
    
    cl = DummyClassifier (project_op='max', statistic='sum')
    assert (cl.fit_apply (X, y)==np.array([-32997, -32994, -32970, -32940])).all()
    assert cl.estimator == {'statistic_0': 33, 'statistic_1': 66, 'statistic': -33000}
    
    cl = DummyClassifier (project_op='max', statistic='sum', apply_func='distance')
    assert (cl.fit_apply (X, y)==np.array([-33, -33, -33,  21])).all()
    assert (cl.project_op(X)==np.array([ 3,  6, 30, 60])).all()

