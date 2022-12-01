#
#     Copyright (C) 2021 CCP-EM
#
#     This code is distributed under the terms and conditions of the
#     CCP-EM Program Suite Licence Agreement as a CCP-EM Application.
#     A copy of the CCP-EM licence can be obtained by writing to the
#     CCP-EM Secretary, RAL Laboratory, Harwell, OX11 0FA, UK.
#

import unittest
import os
import tempfile
import shutil
import test_data
import numpy as np
from ccpem_pyutils.model.gemmi_model_utils import (
    get_sequence_from_atom_records,
    get_sequence_resnum_from_atom_records,
)
import datetime


class GemmiModelUtilsTest(unittest.TestCase):
    def setUp(self):
        """
        Setup test data and output directories.
        """
        self.test_data = os.path.dirname(test_data.__file__)
        self.test_dir = tempfile.mkdtemp(prefix="coord_clust")
        # Change to test directory
        self._orig_dir = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        os.chdir(self._orig_dir)
        print(self.test_dir)
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_get_sequence(self):
        model_input = os.path.join(self.test_data, "5me2.pdb")
        dict_seq = get_sequence_from_atom_records(model_input)
        assert len(dict_seq) == 4
        assert len(dict_seq["A"]) == 140
        dict_seq = get_sequence_resnum_from_atom_records(model_input)[0]
        assert len(dict_seq) == 4
        assert len(dict_seq["A"]) == 140
