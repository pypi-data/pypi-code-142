"""
Base Module
-----------
It includes basic information and utilities to process chemical data.
Several pre-defined chemical and physical features can be accessed by the global variables of this module.
"""


import numpy
import torch
import json
from mendeleev.fetch import fetch_table
from sklearn.preprocessing import scale


# A dictionary of atomic number for each atomic symbol.
atom_nums = {
    'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10,
    'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20,
    'Sc': 21, 'Ti': 22, 'V': 23, 'Cr': 24, 'Mn': 25, 'Fe': 26, 'Co': 27, 'Ni': 28, 'Cu': 29, 'Zn': 30,
    'Ga': 31, 'Ge': 32, 'As': 33, 'Se': 34, 'Br': 35, 'Kr': 36, 'Rb': 37, 'Sr': 38, 'Y': 39, 'Zr': 40,
    'Nb': 41, 'Mo': 42, 'Tc': 43, 'Ru': 44, 'Rh': 45, 'Pd': 46, 'Ag': 47, 'Cd': 48, 'In': 49, 'Sn': 50,
    'Sb': 51, 'Te': 52, 'I': 53, 'Xe': 54, 'Cs': 55, 'Ba': 56, 'La': 57, 'Ce': 58, 'Pr': 59, 'Nd': 60,
    'Pm': 61, 'Sm': 62, 'Eu': 63, 'Gd': 64, 'Tb': 65, 'Dy': 66, 'Ho': 67, 'Er': 68, 'Tm': 69, 'Yb': 70,
    'Lu': 71, 'Hf': 72, 'Ta': 73, 'W': 74, 'Re': 75, 'Os': 76, 'Ir': 77, 'Pt': 78, 'Au': 79, 'Hg': 80,
    'Tl': 81, 'Pb': 82, 'Bi': 83, 'Po': 84, 'At': 85, 'Rn': 86, 'Fr': 87, 'Ra': 88, 'Ac': 89, 'Th': 90,
    'Pa': 91, 'U': 92, 'Np': 93, 'Pu': 94, 'Am': 95, 'Cm': 96, 'Bk': 97, 'Cf': 98, 'Es': 99, 'Fm': 100
}

# A dictionary of atomic symbol for each atomic number.
atom_syms = {v: k for k, v in atom_nums.items()}

# Basic elemental features of the Python Mendeleev package.
elem_attr_names = [
    'atomic_number', 'atomic_weight', 'atomic_radius', 'atomic_volume', 'atomic_weight',
    'boiling_point', 'covalent_radius_pyykko', 'density', 'dipole_polarizability', 'electron_affinity',
    'en_allen', 'en_ghosh', 'en_pauling', 'evaporation_heat', 'fusion_heat', 'heat_of_formation',
    'melting_point', 'mendeleev_number', 'period', 'specific_heat', 'thermal_conductivity', 'vdw_radius'
]

# Hybridization types of the atoms.
cat_hbd = ['SP', 'SP2', 'SP3', 'SP3D', 'SP3D2']

# Types of the formal charge of the atoms.
cat_fc = ['-4', '-3', '-2', '-1', '0', '1', '2', '3', '4']

# Types of chemical bondings between two atoms.
cat_bond_types = [
    'UNSPECIFIED', 'SINGLE', 'DOUBLE', 'TRIPLE', 'QUADRUPLE', 'QUINTUPLE', 'HEXTUPLE',
    'ONEANDAHALF', 'TWOANDAHALF', 'THREEANDAHALF', 'FOURANDAHALF', 'FIVEANDAHALF',
    'AROMATIC', 'IONIC', 'HYDROGEN', 'THREECENTER', 'DATIVEONE', 'DATIVE', 'DATIVEL',
    'DATIVER', 'OTHER', 'ZERO', 'SELF'
]

# First ionization energies for each element.
first_ion_energies = [
    1312, 2372.3, 520.2, 899.5, 800.6, 1086.5, 1402.3, 1313.9, 1681, 2080.7,
    495.8, 737.7, 577.5, 786.5, 1011.8, 999.6, 1251.2, 1520.6, 418.8, 589.8,
    633.1, 658.8, 650.9, 652.9, 717.3, 762.5, 760.4, 737.1, 745.5, 906.4,
    578.8, 762, 947, 941, 1139.9, 1350.8, 403, 549.5, 600, 640.1,
    652.1, 684.3, 702, 710.2, 719.7, 804.4, 731, 867.8, 558.3, 708.6,
    834, 869.3, 1008.4, 1170.4, 375.7, 502.9, 538.1, 534.4, 527, 533.1,
    540, 544.5, 547.1, 593.4, 565.8, 573, 581, 589.3, 596.7, 603.4,
    523.5, 658.5, 761, 770, 760, 840, 880, 870, 890.1, 1007.1,
    589.4, 715.6, 703, 812.1, 899.003, 1037, 380, 509.3, 499, 587,
    568, 597.6, 604.5, 584.7, 578, 581, 601, 608, 619, 627,
    635, 642, 470, 580, 665, 757, 740, 730, 800, 960,
    1020, 1155, 707.2, 832.2, 538.3, 663.9, 736.9, 860.1, 463.1, 563.3
]


def load_elem_attrs(path_elem_attr: str = None) -> torch.Tensor:
    """
    Load elemental attributes from user-defined elemental attributes in ``path_elem_attr``.
    By employing this function, the users can employ customized elemental attributes in their machine learning.
    The user-defined elemental attributes should be provided as a :obj:`JSON file`
    with a format of :obj:`{element: list of elemental attributes}`.
    If the argument ``path_elem_attr`` is ``None``, basic elemental attributes from
    the `Python Mendeleev package <https://mendeleev.readthedocs.io/en/stable/>`_ is returned.

    :param path_elem_attr: (*str, optional*) Path of the JSON file including user-defined elemental attributes (*default* = ``None``).
    :return: (*torch.Tensor*) A 2-dimensional array containing element features for each element in a row.
    """

    if path_elem_attr is None:
        # Load basic elemental attributes from the Mendeleev package.
        elem_attrs = load_mendeleev_attrs(elem_attr_names)

        # Load first ionization energies for each element.
        ion_energies = numpy.array(first_ion_energies[:elem_attrs.shape[0]]).reshape(-1, 1)
        ion_energies = torch.tensor(ion_energies, dtype=torch.float)

        # Normalize elemental attributes.
        elem_attrs = scale(numpy.hstack([elem_attrs, ion_energies]))

        return torch.tensor(elem_attrs, dtype=torch.float)[:len(atom_nums), :]
    else:
        # Load the elemental attributes from the user-defined elemental attributes.
        with open(path_elem_attr) as json_file:
            elem_attr = json.load(json_file)
            elem_attrs = [torch.tensor(elem_attr[elem], dtype=torch.float) for elem in atom_nums.keys()]

        return torch.vstack(elem_attrs)[:len(atom_nums), :]


def load_mendeleev_attrs(elem_feat_names):
    """
    Load elemental attributes from the `Python Mendeleev package <https://mendeleev.readthedocs.io/en/stable/>`_.
    This function loads total nine elemental attributes and returns the a 2-dimensional ``torch.Tensor`` object
    containing the elemental attributes for each element in a row.

    :param elem_feat_names: (*list*) A list of attribute names to be loaded from Mendeleev package.
    :return: (*torch.Tensor*) A 2-dimensional array containing element features for each element in a row.
    """

    # Load chemical and physical attributes of the elements from the Python Mendeleev package.
    elem_attrs = numpy.array(fetch_table('elements')[elem_feat_names])

    return torch.tensor(numpy.nan_to_num(elem_attrs), dtype=torch.float)
