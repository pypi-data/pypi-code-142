import os

import pynibs
import numpy as np
import unittest
import yaml


class TestRegressData(unittest.TestCase):
    """
    Test pynibs.regress_data()
    """
    np.random.seed(1)

    n_elm_small = 10
    # n_elm_large = 100000
    n_mep_small = 10
    # n_mep_large = 100

    e_small = np.zeros((n_mep_small, n_elm_small))
    e_small[:] = 1
    e_small *= np.linspace(0.1, 5, n_mep_small)[:, np.newaxis]
    e_small *= np.linspace(0.1, 5, n_elm_small)

    mep_small = np.linspace(0, 5, n_mep_small)

    con_small = np.array([[i, i + 1, i + 2] for i in range(n_elm_small)])

    def test_raise_assert_if_no_con(self):
        with self.assertRaises(AssertionError):
            pynibs.regress_data(self.e_small, self.mep_small)

    def test_all_default(self):
        r2 = pynibs.regress_data(self.e_small, self.mep_small, refit_discontinuities=False, n_cpu=1)
        assert r2.max() > .9
        assert r2.shape == (self.n_elm_small,)

    def test_return_fits(self):
        r2, fits = pynibs.regress_data(self.e_small, self.mep_small, refit_discontinuities=False, n_cpu=1,
                                       return_fits=True)
        assert r2.max() > .9
        assert r2.shape == (self.n_elm_small,)
        assert len(fits) == self.n_elm_small
        assert type(fits[0]) == dict
        for k in ['x0', 'r', 'amp', 'y0']:
            assert k in fits[0]

    def test_elm_idx_list(self):
        elm_idx_list = list(range(0, int(self.n_elm_small / 2)))
        r2 = pynibs.regress_data(self.e_small, self.mep_small, refit_discontinuities=False, n_cpu=1,
                                 elm_idx_list=elm_idx_list)
        assert r2.max() > .9
        assert r2.shape == (len(elm_idx_list),)

    def test_zap_idx(self):
        zap_idx = range(int(self.n_mep_small / 2), self.n_mep_small)
        r2 = pynibs.regress_data(self.e_small, self.mep_small, refit_discontinuities=False, n_cpu=1,
                                 zap_idx=zap_idx)
        assert r2.max() > .9
        assert r2.shape == (self.n_elm_small,)

    def test_element_list(self):
        element_list = [pynibs.Element(x=self.e_small[:, ele_id],
                                       y=self.mep_small,
                                       ele_id=ele_id,
                                       fun=pynibs.linear,
                                       score_type="R2",
                                       select_signed_data=False,
                                       constants=None) for ele_id in range(self.n_elm_small)]
        r2, fits = pynibs.regress_data(self.e_small, self.mep_small, refit_discontinuities=False, n_cpu=1,
                                       element_list=element_list, return_fits=True)
        assert r2.max() > .9
        assert r2.shape == (self.n_elm_small,)
        # let's check if really linear fits have been used
        assert 'm' in fits[0]
        assert 'n' in fits[0]

    def test_refit_discontinuities(self):
        r2 = pynibs.regress_data(self.e_small, self.mep_small, refit_discontinuities=True, n_cpu=1,
                                 con=self.con_small)
        assert r2.max() > .9
        assert r2.shape == (self.n_elm_small,)

    def test_n_refit(self):
        r2 = pynibs.regress_data(self.e_small, self.mep_small, refit_discontinuities=False, n_cpu=1,
                                 n_refit=0)
        assert r2.max() > .9
        assert r2.shape == (self.n_elm_small,)

    def test_exp(self):
        r2, fits = pynibs.regress_data(self.e_small, self.mep_small, refit_discontinuities=False, n_cpu=1,
                                       n_refit=0, fun=pynibs.exp0, return_fits=True)
        assert r2.max() > 0.90
        assert r2.shape == (self.n_elm_small,)
        assert 'x0' in fits[0]
        assert 'r' in fits[0]

    def test_yaml_exp(self):
        yaml_config = os.path.join(pynibs.__datadir__, 'configuration_exp0.yaml')
        with open(yaml_config, "r") as yamlfile:
            config = yaml.load(yamlfile, Loader=yaml.FullLoader)
        r2, fits = pynibs.regress_data(self.e_small, self.mep_small, refit_discontinuities=False, n_cpu=1,
                                       n_refit=0, fun=pynibs.exp0, return_fits=True, **config)
        assert r2.max() > 0.90
        assert r2.shape == (self.n_elm_small,)
        assert 'x0' in fits[0]
        assert 'r' in fits[0]


if __name__ == '__main__':
    unittest.main()
