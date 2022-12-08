import warnings
import pynibs
import numpy as np
import unittest


class TestDataElements2Nodes(unittest.TestCase):
    """
    Test pynibs.data_elements2nodes()
    """
    np.random.seed(1)
    n_elm_small = 100
    n_elm_large = 100000
    con_small_tri = np.random.choice(n_elm_small, n_elm_small * 3)
    con_small_tri = np.reshape(con_small_tri, (n_elm_small, 3))
    con_small_tet = np.random.choice(n_elm_small, n_elm_small * 4)
    con_small_tet = np.reshape(con_small_tet, (n_elm_small, 4))

    data_small = np.random.rand(n_elm_small) * 1000
    data_small_zero = np.zeros(n_elm_small)
    data_small_nan = data_small.copy()
    data_small_nan[np.random.choice(n_elm_small,20,replace=False)] = np.nan
    datas_small = [np.random.rand(n_elm_small), np.random.rand(n_elm_small), np.random.rand(n_elm_small)]

    data_large = np.random.rand(n_elm_large) * 1000
    con_large_tri = np.random.choice(n_elm_large, n_elm_large * 3)
    con_large_tri = np.reshape(con_large_tri, (n_elm_large, 3))

    ret_small_tri = np.array([[3.81717394e+03, -3.44380754e+03, -1.04068361e+02,
                               -3.03672180e+03, 1.69162931e-11, 3.28735690e+02,
                               -1.90366377e+03, -1.75718804e+03, -1.01526253e+03,
                               1.04089987e+03, 2.77992727e+03, 1.09061487e+04,
                               5.38944819e+03, -3.79793187e+02, 9.39673305e+02,
                               1.98831328e+03, 1.58734484e+03, -1.13042037e+03,
                               -2.09536935e+03, 2.26513015e+03, 4.73078124e+03,
                               3.39876074e+03, -7.55140605e+02, -2.97782279e+02,
                               -1.40251390e+03, 2.05253645e+03, -5.02309550e+02,
                               2.96740726e+03, -3.00838583e+03, -5.50986205e+03,
                               1.48806206e+03, 4.16278309e+03, 2.62938829e+03,
                               1.93231842e+02, -4.61159330e+03, 2.59423044e+02,
                               -4.60235252e+03, -7.24318305e+03, 2.66801622e+03,
                               5.76236046e+03, 2.97453723e+03, 3.08128171e+02,
                               5.27098593e+02, 1.15281629e+03, -1.54514947e+03,
                               3.34553994e+03, 3.41534538e+03, -1.55617593e+03,
                               -4.47155698e+03, 1.36873183e+02, 2.63697251e+03,
                               1.90110815e-11, 1.91430775e+03, -2.15570486e+02,
                               3.79785433e+03, 6.35365607e+03, -7.24051657e+02,
                               5.20753754e+03, 3.19122804e-12, -5.82332417e+02,
                               2.01945775e+03, -2.75572686e+03, -1.19368661e+03,
                               1.65623497e+03, 1.09343732e+03, -6.13390936e+03,
                               1.14957878e+03, 1.37436400e+03, -7.85602469e+02,
                               -2.49699644e+03, -6.00553990e+02, 3.23686455e+03,
                               3.70927556e+03, 2.29986338e-13, 5.10659728e+02,
                               -1.22064351e+03, 5.40601193e+02, 1.08103027e+03,
                               -2.15922656e+03, -8.83769660e+02, -8.91707692e+02,
                               4.99875852e+03, -2.02433759e+03, 9.20401644e+02,
                               8.07942131e+01, 2.80601545e+03, 1.49195685e+03,
                               -2.74571524e+02, -1.13395172e+03, -1.41719240e+02,
                               -3.90122898e-14, -1.84344533e+02, -3.97735225e+03,
                               1.93231842e+02, 4.02650694e+02, 0.00000000e+00,
                               -6.16506432e+02, 2.20263338e+03, 2.65351685e+03,
                               1.54040912e+03]])

    def test_e2n_single_data_tri(self):
        ret = pynibs.data_elements2nodes(self.data_small, self.con_small_tri)
        assert ret.shape == (1, self.n_elm_small)
        assert np.all(np.isclose(ret, self.ret_small_tri))

    def test_e2n_single_data_tri_zero(self):
        ret = pynibs.data_elements2nodes(self.data_small_zero, self.con_small_tri, precise=True)

        assert ret.shape == (1, self.n_elm_small)
        assert np.nanmax(ret[0]) == 0
        assert np.isnan(ret[0][4])

    def test_e2n_single_data_tri_nan(self):
        ret = pynibs.data_elements2nodes(self.data_small_nan, self.con_small_tri)
        assert ret.shape == (1, self.n_elm_small)

    def test_e2n_single_data_tet(self):
        ret = pynibs.data_elements2nodes(self.data_small, self.con_small_tet)
        assert ret.shape == (1, self.n_elm_small)

    def test_e2n_mult_data(self):
        ret = pynibs.data_elements2nodes(self.datas_small, self.con_small_tri)
        assert len(ret) == 3
        assert ret[0].shape == (self.n_elm_small,)

    '''
    def test_e2n_single_data_tri_large(self):
        """
        This tests for the OOM catch. Results are not checked, due to long compuation time.
        """
        warnings.filterwarnings("error", "Cannot allocate enough RAM")
        with self.assertRaises(Exception):
            pynibs.data_elements2nodes(self.data_large, self.con_large_tri)
    '''

if __name__ == '__main__':
    unittest.main()
