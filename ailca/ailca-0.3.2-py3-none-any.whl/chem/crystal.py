"""
Crystal Structure
-----------------
This module provides several functions to convert the crystal structures into the attributed graph
of node, edge, node features, and edge features.
Like the molecular structure, the converted crystal structure are defined as a ``torch_geometric.Data`` object.
"""


import numpy
import torch
import pandas
import pymatgen
import warnings
import torch_geometric.data
from tqdm import tqdm
from typing import Union, Tuple
from pymatgen.core.structure import Structure
from ailca.core.env import *
from ailca.chem.base import atom_nums
from ailca.data.base import Data, Dataset


def rbf(data: torch.Tensor,
        mu: torch.Tensor,
        beta: float) -> torch.Tensor:
    """
    Compute transformed value of ``data`` by radial basis function (RBF).

    :param data: (*torch.Tensor*) A data object.
    :param mu: (*torch.Tensor*) The mean vectors of the Gaussian kernels.
    :param beta: (*torch.Tensor*) The standard deviation vectors of the Gaussian kernels.
    :return: (*torch.Tensor*) A transformed data object by RBF.
    """

    return torch.exp(-(data - mu)**2 / beta**2)


def get_crystal_graph(path_cif: str,
                      elem_attrs: torch.Tensor,
                      rbf_means: torch.Tensor,
                      atomic_cutoff: float = 4.0) -> Union[None, torch_geometric.data.Data]:
    """
    Generate an attributed graph of the given crystal structure in a CIF of ``path_cif_file``,
    which is a standard text file format for representing crystallographic information.
    The generated crystal graph contains chemical and structural information of the crystal structure
    represented by atoms, bonds, atom features, and bond features.

    :param path_cif: (*str*) Path of CIF containing the crystal structure.
    :param elem_attrs: (*torch.Tensor*) A table containing elemental attributes in each row.
    :param rbf_means: (*torch.Tensor*) Mean vectors to generate edge features based on RBF kernel.
    :param atomic_cutoff: (*float*) Maximum radius in Angstrom to determine neighborhood atoms (*default* = ``4.0``).
    :return: (*torch_geometric.data.Data*) A graph object of the crystal structure.
    """

    # Get Crystal object from the given CIF.
    crystal = Structure.from_file(path_cif)

    # Get the atomic information of the crystal structure.
    atom_coord, atom_feats = get_atom_info(crystal, elem_attrs, atomic_cutoff)

    # Get the bond information of the crystal structure.
    bonds, bond_feats = get_bond_info(atom_coord, rbf_means, atomic_cutoff)

    # Return None if the graph is isolated, which means invalid crystal graph.
    if bonds is None:
        return None

    return torch_geometric.data.Data(x=atom_feats, edge_index=bonds, edge_attr=bond_feats)


def get_atom_info(crystal: pymatgen.core.Structure,
                  elem_attrs: torch.Tensor,
                  atomic_cutoff: float) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Extract atomic information from the Pymatgen object of the crystal structure.
    It returns a tuple of XYZ coordinates and feature vectors of atoms in the crystal structure.

    :param crystal: (*pymatgen.core.Structure*) A Pymatgen object of the crystal structure.
    :param elem_attrs: (*torch.Tensor*) A table containing elemental attributes in each row.
    :param atomic_cutoff: (*float*) Maximum radius in Angstrom to determine neighborhood atoms.
    :return: (*Tuple[torch.Tensor, torch.Tensor])*) A tuple of atomic coordinates and atomic features.
    """

    atoms = list(crystal.atomic_numbers)
    atom_coord = list()
    atom_feats = list()
    list_nbrs = crystal.get_all_neighbors(atomic_cutoff)

    # Get overall charge of the crystal structure.
    charge = torch.tensor(crystal.charge, dtype=torch.float)

    # Get density in units of g/cc.
    density = torch.tensor(crystal.density, dtype=torch.float)

    # Get volume of the crystal structure.
    volume = torch.tensor(crystal.volume, dtype=torch.float)

    # Get XYZ coordinate of the atoms.
    coords = dict()
    for coord in list(crystal.cart_coords):
        coord_key = ','.join(list(coord.astype(str)))
        coords[coord_key] = True

    # Find neighborhood atoms.
    for i in range(0, len(list_nbrs)):
        nbrs = list_nbrs[i]

        for j in range(0, len(nbrs)):
            coord_key = ','.join(list(nbrs[j][0].coords.astype(str)))
            if coord_key not in coords.keys():
                coords[coord_key] = True
                atoms.append(atom_nums[nbrs[j][0].species_string])

    # Get XYZ coordinate of the atoms and their neighborhood atoms.
    for coord in coords.keys():
        atom_coord.append(torch.tensor([float(x) for x in coord.split(',')], dtype=torch.float))
    atom_coord = torch.vstack(atom_coord)

    # Get elemental attributes to generate the feature vectors of the atoms.
    for i in range(0, len(atoms)):
        elem_attr = elem_attrs[atoms[i]-1, :]
        atom_feats.append(torch.hstack([elem_attr, charge, density, volume]))
    atom_feats = torch.vstack(atom_feats)

    return atom_coord, atom_feats


def get_bond_info(atom_coord: torch.Tensor,
                  rbf_means: torch.Tensor,
                  atomic_cutoff: float) -> Union[Tuple[None, None], Tuple[torch.Tensor, torch.Tensor]]:
    """
    Generate chemical bondings and their feature vectors from the XYZ coordinate of the atoms.
    The chemical bondings (edges) are generated when the distance between two atoms is less than ``atomic_cutoff`.

    :param atom_coord: (*torch.Tensor*) XYZ coordinates of the atoms in the crystal structure.
    :param rbf_means: (*torch.Tensor*) Mean vectors to generate edge features based on RBF kernel.
    :param atomic_cutoff: (*float*) Maximum radius in Angstrom to determine neighborhood atoms.
    :return: (*Tuple[torch.Tensor, torch.Tensor]*) A tuple of chemical bondings and their bond features.
    """

    bonds = list()
    bond_feats = list()
    pdist = torch.cdist(atom_coord, atom_coord)

    # Calculate bond information.
    for i in range(0, atom_coord.shape[0]):
        for j in range(0, atom_coord.shape[0]):
            if i != j and pdist[i, j] < atomic_cutoff:
                bonds.append(torch.tensor([i, j], dtype=torch.long))
                bond_feats.append(rbf(torch.full((1, rbf_means.shape[0]), pdist[i, j]), rbf_means, beta=0.5))

    if len(bonds) == 0:
        # If there is no bond in the given crystal structure, i.e., the crystal structure is isolated.
        return None, None
    else:
        bonds = torch.vstack(bonds).t().contiguous()
        bond_feats = torch.vstack(bond_feats)

        return bonds, bond_feats


def load_dataset(path_metadata_file: str,
                 path_structs: str,
                 elem_attrs: torch.Tensor,
                 idx_mat_id: int,
                 idx_target: int = None,
                 atomic_cutoff: float = 4.0,
                 n_kerl_centers: int = 128,
                 verbose: bool = True) -> Dataset:
    """
    Load the dataset containing the crystal structures of the material.
    If ``idx_target`` is given, the dataset is loaded with the target values.

    :param path_metadata_file: (*str*) The path of the metadata file of the crystal structures.
    :param path_structs: (*str*) A directory of the structure files.
    :param elem_attrs:  (*torch.Tensor*) A 2-dimensional tensor containing the elemental attributes of the elements.
    :param idx_mat_id: (*int*) An index of the material identifier in the metadata file.
    :param idx_target: (*int, optional*) An index of the target values in the data file (*default* = ``None``).
    :param atomic_cutoff: (*float, optional*) Maximum radius in Angstrom to define the neighborhood atoms (*default* = ``4.0``).
    :param n_kerl_centers: (*int, optional*) The number of kernel centers in radial basis function to the generate edge features (*default* = ``128``).
    :param verbose: (*bool, optional*) A flag variable to present the system log in data loading (*default* = ``True``).
    :return: (*Dataset*) A dataset object.
    """

    metadata_file = pandas.read_excel(path_metadata_file)
    metadata = numpy.array(metadata_file)
    names_feats = [metadata_file.columns.values[idx_mat_id]]
    name_target = None if idx_target is None else metadata_file.columns.values[idx_target]
    rbf_means = torch.tensor(numpy.linspace(start=0.7, stop=atomic_cutoff, num=n_kerl_centers), dtype=torch.float)
    iter_range = range(0, metadata.shape[0])
    list_data = list()

    if verbose:
        iter_range = tqdm(iter_range)

    for i in iter_range:
        path_struct_file = path_structs + '/' + metadata[i, idx_mat_id]
        crystal_graph = get_crystal_graph(path_struct_file, elem_attrs, rbf_means, atomic_cutoff)

        if crystal_graph is None:
            warnings.warn('{}-th data has been discarded because invalid crystal graph is generated.'.format(i))
            continue

        if idx_target is None:
            list_data.append(Data(x=crystal_graph, idx=i, dtype=DTYPE_CSTRUCT))
        else:
            list_data.append(Data(x=crystal_graph, y=metadata[i, idx_target], idx=i, dtype=DTYPE_CSTRUCT))

    return Dataset(list_data,
                   idx_mat_id=idx_mat_id,
                   idx_target=idx_target,
                   names_feats=names_feats,
                   name_target=name_target,
                   types_feats=[DTYPE_CSTRUCT for i in range(0, len(names_feats))],
                   atomic_cutoff=atomic_cutoff)
