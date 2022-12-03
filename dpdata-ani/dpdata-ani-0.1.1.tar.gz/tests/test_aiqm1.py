import shutil
import numpy as np
import dpdata
import pytest


def test_aiqm_nn_driver():
    s = dpdata.System(data={
        "atom_names": ["O"],
        "atom_numbs": [2],
        "atom_types": np.zeros((2,), dtype=int),
        "coords": np.array([[[0., 0., 0.], [0., 0., 1.2]]]),
        "cells": np.zeros((1, 3, 3), dtype=np.float32),
        "orig": np.zeros(3, dtype=np.float32),
        "nopbc": True,
    })
    ls = s.predict(driver="aiqm1/nn")
    assert ls.get_natoms() == 2
    assert ls.get_nframes() == 1
    ls.check_data()


@pytest.mark.skipif(not shutil.which('mndo'), reason='mndo not found')
def test_aiqm_driver():
    s = dpdata.System(data={
        "atom_names": ["O"],
        "atom_numbs": [2],
        "atom_types": np.zeros((2,), dtype=int),
        "coords": np.array([[[0., 0., 0.], [0., 0., 1.2]]]),
        "cells": np.zeros((1, 3, 3), dtype=np.float32),
        "orig": np.zeros(3, dtype=np.float32),
        "nopbc": True,
    })
    ls = s.predict(driver="aiqm1")
    assert ls.get_natoms() == 2
    assert ls.get_nframes() == 1
    ls.check_data()
