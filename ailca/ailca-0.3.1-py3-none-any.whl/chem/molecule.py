"""
Molecular Structure
-------------------
This module provides abstracted functions to convert the molecular structures into the mathematical graphs.
The converted molecular structure is defined as a ``torch_geometric.Data`` object.
"""


import pandas
import warnings
import torch_geometric.data
from tqdm import tqdm
from typing import Union
from rdkit import Chem
from ailca.core.env import *
from ailca.chem.base import *
from ailca.data.base import Data, Dataset


def get_one_hot_feat(hot_category: str,
                     categories: list) -> torch.Tensor:
    """
    Generate a ``len(categories)``-dimensional one-hot encoding vector.
    All available categories are defined by ``categories``, and the selected category is indicated by ``hot_category``.

    :param hot_category: (*str*) The selected category.
    :param categories: (*str*) All available categories.
    :return: (*torch.Tensor*) The one-hot encoding vector.
    """

    # Initialize one-hot encoding dictionary.
    one_hot_feat = dict()
    for cat in categories:
        one_hot_feat[cat] = 0

    # Set value for the selected category if it exists in the given available categories.
    if hot_category in categories:
        one_hot_feat[hot_category] = 1

    # Convert the one-hot encoding dictionary to the one-hot encoding vector.
    return torch.tensor(list(one_hot_feat.values()), dtype=torch.float)


def get_mol_graph(smiles: str,
                  elem_attrs: torch.Tensor,
                  add_h: bool = False) -> Union[None, torch_geometric.data.Data]:
    """
    Generate an attributed graph of the given crystal structure in a CIF of ``path_cif_file``,
    which is a standard text file format for representing crystallographic information.
    The generated crystal graph contains chemical and structural information of the crystal structure
    represented by atoms, bonds, atom features, and bond features.

    :param smiles: (*str*) A SMILES representation of the molecular structure.
    :param elem_attrs: (*torch.Tensor*) A table containing elemental attributes in each row.
    :param add_h: (*bool, optional*) A flag variable that determines whether hydrogen is presented or not in the generated moleuclar graph.
    :return: (*torch_geometric.data.Data*) A graph object of the molecular structure.
    """

    # Get RDKit.Mol object from the given SMILES.
    mol = Chem.MolFromSmiles(smiles)

    # Present hydrogen in the molecule structure.
    if add_h:
        mol = Chem.AddHs(mol)

    # If SMILES was not converted normally, returns None object to denote failure of graph generation.
    if mol is None:
        warnings.warn('A given SMILES {} was not able to be converted to the molecular graph.'.format(smiles))
        return None

    # Global information of the molecule.
    n_rings = torch.tensor(mol.GetRingInfo().NumRings(), dtype=torch.float)

    # Structural information of the molecular graph.
    atom_attrs = list()
    bonds = list()
    bond_feats = list()

    # Generate atom-feature matrix.
    for atom in mol.GetAtoms():
        # Get elemental features of the atom.
        elem_attr = elem_attrs[atom.GetAtomicNum() - 1, :]

        # Get hybridization type of the atom.
        hbd_type = get_one_hot_feat(str(atom.GetHybridization()), cat_hbd)

        # Get formal charge of the atom.
        fc_type = get_one_hot_feat(str(atom.GetFormalCharge()), cat_fc)

        # Check whether the atom belongs to the aromatic ring in the molecule.
        mem_arom = torch.tensor(1, dtype=torch.float) if atom.GetIsAromatic() else torch.tensor(0, dtype=torch.float)

        # Get the number of bonds.
        degree = torch.tensor(atom.GetDegree(), dtype=torch.float)

        # Get the number of hydrogen bonds.
        n_hs = torch.tensor(atom.GetTotalNumHs(), dtype=torch.float)

        # Append a feature vector of the atom.
        atom_attrs.append(torch.hstack([elem_attr, hbd_type, fc_type, mem_arom, degree, n_hs, n_rings]))

    # Generate bond-feature matrix.
    for bond in mol.GetBonds():
        bonds.append([bond.GetBeginAtomIdx(), bond.GetEndAtomIdx()])
        bond_feats.append(get_one_hot_feat(str(bond.GetBondType()), cat_bond_types))
        bonds.append([bond.GetEndAtomIdx(), bond.GetBeginAtomIdx()])
        bond_feats.append(get_one_hot_feat(str(bond.GetBondType()), cat_bond_types))

    # Return None if the graph is isolated, which means invalid molecular graph.
    if len(bonds) == 0:
        return None

    # Add self-loop in graph edges.
    for i in range(0, len(atom_attrs)):
        bonds.append([i, i])
        bond_feats.append(get_one_hot_feat('SELF', cat_bond_types))

    # Save the atomic information as ``torch.Tensor`` objects.
    atom_attrs = torch.vstack(atom_attrs)
    bonds = torch.tensor(bonds, dtype=torch.long).t().contiguous()
    bond_feats = torch.vstack(bond_feats)

    return torch_geometric.data.Data(x=atom_attrs, edge_index=bonds, edge_attr=bond_feats)


def load_dataset(path_data_file: str,
                 elem_attrs: torch.Tensor,
                 idx_smiles: int,
                 idx_target: int = None,
                 add_h: bool = False,
                 verbose: bool = True) -> Dataset:
    """
    Load the dataset containing the atomic structures of the molecules.
    If ``idx_target`` is given, the dataset is loaded with the target values.

    :param path_data_file: (*str*) The path of the data file.
    :param elem_attrs:  (*torch.Tensor*) A 2-dimensional tensor containing the elemental attributes of the elements.
    :param idx_smiles: (*int*) An index of the SMILES in the data file.
    :param idx_target: (*int, optional*) An index of the target values in the data file (*default* = ``None``).
    :param add_h: (*str*) A variable indicating whether to add hydrogen to the molecules (*default* = ``False``).
    :param verbose: (*bool*) A flag variable to present the system log in data loading (*default* = ``True``).
    :return: (*Dataset*) A dataset object.
    """

    data_file = pandas.read_excel(path_data_file)
    data = numpy.array(data_file)
    names_feats = [data_file.columns.values[idx_smiles]]
    name_target = None if idx_target is None else data_file.columns.values[idx_target]
    iter_range = range(0, data.shape[0])
    list_data = list()

    # If ``verbose`` is ``True``, the loading bar is presented through the standard I/O.
    if verbose:
        iter_range = tqdm(iter_range)

    # Read molecular structures in the dataset.
    for i in iter_range:
        mol_graph = get_mol_graph(data[i, idx_smiles], elem_attrs, add_h)

        if mol_graph is None:
            warnings.warn('{}-th data has been discarded because invalid molecular graph is generated.'.format(i))
            continue

        if idx_target is None:
            list_data.append(Data(x=mol_graph, idx=i, dtype=DTYPE_MSTRUCT))
        else:
            list_data.append(Data(x=mol_graph, y=data[i, idx_target], idx=i, dtype=DTYPE_MSTRUCT))

    return Dataset(list_data,
                   idx_smiles=idx_smiles,
                   idx_target=idx_target,
                   names_feats=names_feats,
                   name_target=name_target,
                   types_feats=[DTYPE_MSTRUCT for i in range(0, len(names_feats))],
                   add_h=add_h)
