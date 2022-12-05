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
from ccpem_utils_tests import test_data
import numpy as np
from ccpem_pyutils.model.gemmi_model_utils import (
    get_coordinates,
    set_bfactor_attributes,
    get_residue_attribute,
)
from ccpem_pyutils.other.cluster import (
    cluster_coord_features,
    generate_kdtree,
    pairs_kdtree,
)
import datetime


class CoordClustTests(unittest.TestCase):
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

    def gemmi_get_coord(self, model_input, return_list=True, atom_selection="all"):
        list_ids, list_coordinates = get_coordinates(
            model_input, return_list=return_list, atom_selection=atom_selection
        )
        return list_ids, list_coordinates

    def cluster_coord_features(self, list_coordinates, dbscan_eps=2.3):
        cluster_labels = cluster_coord_features(
            np.array(list_coordinates), dbscan_eps=dbscan_eps, norm=False
        )
        return cluster_labels

    def cluster_coord_features_norm(self, list_coordinates, dbscan_eps=0.035):
        cluster_labels = cluster_coord_features(
            np.array(list_coordinates), dbscan_eps=dbscan_eps, norm=True
        )
        return cluster_labels

    def test_cluster_model_coordinates(self):
        model_input = os.path.join(self.test_data, "5me2.pdb")
        list_coordinates = self.gemmi_get_coord(model_input)[1]
        assert len(list_coordinates) == 4468
        cluster_labels = self.cluster_coord_features(list_coordinates)
        assert len(cluster_labels) == len(list_coordinates)
        assert len(np.unique(cluster_labels)) == 8

    def test_cluster_model_coordinates_norm(self):
        model_input = os.path.join(self.test_data, "5me2.pdb")
        list_coordinates = self.gemmi_get_coord(model_input)[1]
        assert len(list_coordinates) == 4468
        cluster_labels = self.cluster_coord_features_norm(list_coordinates)
        assert len(cluster_labels) == len(list_coordinates)
        assert len(np.unique(cluster_labels)) == 8

    def test_cluster_model_coordinates_backbone(self):
        model_input = os.path.join(self.test_data, "5me2.pdb")
        list_ids, list_coordinates = self.gemmi_get_coord(
            model_input, atom_selection="backbone"
        )
        assert len(list_coordinates) == 2436
        cluster_labels = self.cluster_coord_features(
            list_coordinates, dbscan_eps=2.8
        )  # norm: 0.04
        assert len(cluster_labels) == len(list_coordinates)
        assert len(np.unique(cluster_labels)) == 8

    def test_cluster_model_coordinates_representative(self):
        model_input = os.path.join(self.test_data, "5me2.pdb")
        list_ids, list_coordinates = self.gemmi_get_coord(
            model_input, atom_selection="one_per_residue"
        )
        assert len(list_coordinates) == 570
        cluster_labels = self.cluster_coord_features(
            list_coordinates, dbscan_eps=4.0
        )  # norm 0.07673
        assert len(cluster_labels) == len(list_coordinates)
        assert len(np.unique(cluster_labels)) == 5

    def test_cluster_model_coordinates_centre(self):
        model_input = os.path.join(self.test_data, "5me2.pdb")
        list_ids, list_coordinates = self.gemmi_get_coord(
            model_input, atom_selection="centre"
        )
        assert len(list_coordinates) == 570
        cluster_labels = self.cluster_coord_features(
            list_coordinates, dbscan_eps=5.22
        )  # norm 0.088
        assert len(cluster_labels) == len(list_coordinates)
        assert len(np.unique(cluster_labels)) == 23
        list_res_ids, list_res_attr = get_residue_attribute(list_ids, cluster_labels)
        dict_attr = {}
        for n in range(len(list_res_attr)):
            dict_attr[list_res_ids[n]] = list_res_attr[n]
        set_bfactor_attributes(model_input, dict_attr)

    def test_kdtree_model_coordinates_pairs(self):
        model_input = os.path.join(self.test_data, "5me2.pdb")
        list_ids, list_coordinates = self.gemmi_get_coord(
            model_input, atom_selection="one_per_residue"
        )
        assert len(list_coordinates) == 570
        print("Start: ", datetime.datetime.now())
        kdtree = generate_kdtree(list_coordinates, leaf_size=25)
        pair_indices = pairs_kdtree([(61.197, 39.327, 61.266)], kdtree, dist=5.0)
        print("End: ", datetime.datetime.now())
        assert len(pair_indices) == 6
        # for p in pair_indices:
        #     print(list_ids[p[1]])

    # def ():
    #     run_subprocess_get_map_parameters(self):
    #     map_input = os.path.join(self.test_data, "emd_3488.mrc")
    #     subprocess.call(
    #         [
    #             "python3 "
    #             + os.path.realpath(get_map_parameters.__file__)
    #             + " -m "
    #             + map_input
    #             + " -odir "
    #             + self.test_dir,
    #         ],
    #         shell=True,
    #     )
    #     assert os.path.isfile(
    #         os.path.join(self.test_dir, "emd_3488_map_parameters.json")
    #     )
    #     assert math.isclose(
    #         os.stat(
    #             os.path.join(self.test_dir, "emd_3488_map_parameters.json")
    #         ).st_size,
    #         275,
    #         rel_tol=0.05,
    #     )
