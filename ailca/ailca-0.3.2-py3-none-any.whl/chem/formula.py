"""
Chemical Formula
----------------
For machine learning, the chemical formulas should be converted into the machine-readable feature vectors.
The ``ailca.chem.formula`` module provides useful data processing functions to convert
the chemical formulas into the feature vectors.
"""


import numpy
import pandas
import torch
from tqdm import tqdm
from chemparse import parse_formula
from ailca.core.env import *
from ailca.chem.base import atom_nums
from ailca.data.base import Data, Dataset


def get_form_vec(form: str,
                 rep_method: str = REP_FORM_COMPACT,
                 elem_attrs: torch.Tensor = None) -> torch.Tensor:
    """
    Calculate feature vector for a given chemical formula ``form`` according to the representation type ``rep_type``.
    For the compact and sparse representations, a table of the elemental attributes must be provided by ``elem_attrs`.

    :param form: (*str*) Chemical formula.
    :param rep_method: (*str, optional*) Representation method of the feature vector (*default* = ``REP_FORM_COMPACT``).
    :param elem_attrs: (*torch.Tensor*) A table containing elemental attributes in each row.
    :return: (*torch.Tensor*) Feature vector of the chemical formula.
    """

    if rep_method == REP_FORM_COMPACT:
        return __get_compact_form_vec(form, elem_attrs)
    elif rep_method == REP_FORM_CONTENT:
        return __get_content_form_vec(form)
    else:
        raise AssertionError('Unknown representation type \'{}\' is given.'.format(rep_method))


def load_dataset(path_data_file: str,
                 elem_attrs: torch.Tensor,
                 idx_form: int,
                 idx_target: int = None,
                 form_rep_type: str = REP_FORM_COMPACT,
                 verbose: bool = True) -> Dataset:
    """
    Load the dataset containing the chemical formula of the materials.
    If ``idx_target`` is given, the dataset is loaded with the target values.

    :param path_data_file: (*str*) The path of the data file.
    :param elem_attrs:  (*torch.Tensor*) A 2-dimensional tensor containing the elemental attributes of the elements.
    :param idx_form: (*int*) An index of the chemical formula in the data file.
    :param idx_target: (*int, optional*) An index of the target values in the data file (*default* = ``None``).
    :param form_rep_type: (*str*) Representation method of the chemical formula(s) (*default* = ``REP_FORM_COMPACT``).
    :param verbose: (*bool*) A flag variable to present the system log in data loading (*default* = ``True``).
    :return: (*Dataset*) A dataset object.
    """

    data_file = pandas.read_excel(path_data_file)
    data = numpy.array(data_file)
    names_feats = [data_file.columns.values[idx_form]]
    name_target = None if idx_target is None else data_file.columns.values[idx_target]
    iter_range = range(0, data.shape[0])
    list_data = list()

    if verbose:
        iter_range = tqdm(iter_range)

    for i in iter_range:
        form_vec = get_form_vec(data[i, idx_form], form_rep_type, elem_attrs)

        if idx_target is None:
            list_data.append(Data(x=form_vec, idx=i, dtype=DTYPE_FORM))
        else:
            list_data.append(Data(x=form_vec, y=data[i, idx_target], idx=i, dtype=DTYPE_FORM))

    return Dataset(list_data,
                   idx_form=idx_form,
                   idx_target=idx_target,
                   names_feats=names_feats,
                   name_target=name_target,
                   types_feats=[DTYPE_FORM for i in range(0, len(names_feats))],
                   form_rep_type=form_rep_type)


def get_pristine_form(form):
    """
    Return a chemical formula of the pristine material of the given ``form``.

    :param form: (*str*) A chemical formula of the material.
    :return: (*str*) A chemical formula of the pristine material.
    """

    form_dict = parse_formula(form)
    pristine_mat = dict()

    sorted_keys = sorted(form_dict.keys(), key=lambda x: x.lower())
    for e in sorted_keys:
        if form_dict[e] >= 0.5:
            pristine_mat[e] = round(form_dict[e])

    form_pristine_mat = ''
    for e in pristine_mat:
        if pristine_mat[e] > 0:
            form_pristine_mat += e + str(pristine_mat[e])

    return form_pristine_mat


def __get_compact_form_vec(form: str,
                           elem_attrs: torch.Tensor) -> torch.Tensor:
    """
    Convert a given chemical formula in ``form`` into a feature vector.
    For a set of computed atomic features :math:`S = \{\mathbf{h} = f(e) | e \in c \}`
    where :math:`c` is the given chemical formula, the feature vector is calculated as a concatenated vector based on
    weighted sum with a weight :math:`w_\mathbf{h}`, standard deviation :math:`\sigma`, and max operation as:

    .. math::
        \mathbf{x} = \sum_{\mathbf{h} \in S} w_\mathbf{h} h \oplus \sigma(S) \oplus \max(S).

    Note that the standard deviation :math:`\sigma` and the max operations are applied feature-wise (not element-wise).
    This formula-to-vector conversion method is common in chemical machine learning
    [`1 <https://pubs.acs.org/doi/abs/10.1021/acs.jpclett.8b00124>`_,
    `2 <https://journals.aps.org/prb/abstract/10.1103/PhysRevB.93.115104>`_,
    `3 <https://www.nature.com/articles/s41524-021-00564-y>`_].

    :param form: (*str*) Chemical formula (e.g., ZnIn2S4).
    :param elem_attrs: (*torch.Tensor*) The NumPy array of elemental features.
    :return: (*torch.Tensor*) A feature vector of the given chemical formula.
    """

    wt_sum_feats = torch.zeros(elem_attrs.shape[1])
    list_atom_feats = list()

    # Convert the refined chemical formula to a dictionary of the chemical formula.
    form_dict = parse_formula(form)
    sum_elem_nums = sum([float(form_dict[e]) for e in form_dict.keys()])

    # Get atomic features for each element.
    for e in form_dict.keys():
        atom_feats = elem_attrs[atom_nums[e] - 1, :]
        list_atom_feats.append(atom_feats)
        wt_sum_feats += (float(form_dict[e]) / sum_elem_nums) * atom_feats
    form_atom_feats = torch.vstack(list_atom_feats)

    # Generate a feature vector of the formula based on the weighted sum, std., and max. of the atomic features.
    form_vec = torch.hstack([wt_sum_feats,
                             torch.std(form_atom_feats, dim=0),
                             torch.max(form_atom_feats, dim=0)[0],
                             torch.min(form_atom_feats, dim=0)[0]])

    return form_vec


def __get_content_form_vec(form: str) -> torch.Tensor:
    """
    Convert a given chemical formula into a sparse feature vector of elemental contents.
    The feature vector has real values for the elements in the chemical formula.

    :param form: (*str*) Chemical formula (e.g., ZnIn2S4).
    :return: (*torch.Tensor*) A feature vector of the given chemical formula.
    """
    
    form_dict = parse_formula(form)
    form_vec = numpy.zeros(len(atom_nums))

    for e in form_dict:
        form_vec[atom_nums[e] - 1] = form_dict[e]

    return torch.tensor(form_vec, dtype=torch.float)
