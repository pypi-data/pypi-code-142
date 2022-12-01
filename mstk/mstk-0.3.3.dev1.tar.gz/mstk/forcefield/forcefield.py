import os
from pathlib import Path
from .ffterm import *
from .errors import *
from mstk import DIR_MSTK, logger


class ForceField():
    '''
    ForceField is a set of :class:`FFTerm` objects describing the energy function of
    a :class:`~mstk.topology.Topology` with regard to the positions of atoms.

    Attributes
    ----------
    atom_types : dict, [str, AtomType]
        All the atom types in this force field.
        For each key value pair, the value is a AtomType object,
        the key is the :attr:`~AtomType.name` of the object.
    qinc_terms : dict, [str, ChargeIncrementTerm]
        All the charge increment terms.
        For each key value pair, the value is a ChargeIncrementTerm object,
        the key is the :attr:`~ChargeIncrementTerm.name` of the object.
    vdw_terms : dict, [str, subclass of VdwTerm]
        vdW terms between same types.
        For each key value pair, the value is a object of subclass of VdwTerm.
        the key is the :attr:`~VdwTerm.name` of the object.
        The term can be either :class:`LJ126Term` or :class:`MieTerm`,
        as long as it's a subclass of VdwTerm.
        Because we are using name of the term as key,
        there can only be one term to describe the vdW interactions between two atom types.
        Which means, there cannot be a LJ126Term and a MieTerm with same name in a ForceField.
        However, you can have LJ126Term for one pair of atom types and MieTerm for another pairs.
    pairwise_vdw_terms : dict, [str, subclass of VdwTerm]
        Pairwise vdW terms between unlike types.
        For each key value pair, the value is a object of subclass of VdwTerm.
        the key is the :attr:`~VdwTerm.name` of the object.
        If a pair of unlike atom types is not included in this dict,
        then the vdW interactions between this pair will be generated from mixing rule.
    polarizable_terms : dict, [str, subclass of PolarizableTerm]
        Polarization terms for polarizable atom types.
        For each key value pair, the value is a object of subclass of PolarizableTerm.
        the key is the :attr:`~PolarizableTerm.name` of the object.
        Currently, isotropic Drude model is implemented.
    virtual_site_terms: dict, [str, subclass of VirtualSiteTerm]
        Virtual site terms for delocalized interaction center.
        For each key value pair, the value is a object of subclass of VirtualSiteTerm.
        the key is the :attr:`~VirtualSiteTerm.name` of the object.
        Currently, TIP4P model is implemented.
    bond_terms : dict, [str, subclass of BondTerm]
        Bond terms between two atom types.
        For each key value pair, the value is a object of subclass of BondTerm.
        the key is the :attr:`~BondTerm.name` of the object.
    angle_terms : dict, [str, subclass of AngleTerm]
        Angle terms between three atom types.
        For each key value pair, the value is a object of subclass of AngleTerm.
        the key is the :attr:`~AngleTerm.name` of the object.
    dihedral_terms : dict, [str, subclass of DihedralTerm]
        Dihedral terms between four atom types.
        For each key value pair, the value is a object of subclass of DihedralTerm.
        the key is the :attr:`~DihedralTerm.name` of the object.
    improper_terms : dict, [str, subclass of ImproperTerm]
        Improper terms between four atom types.
        For each key value pair, the value is a object of subclass of ImproperTerm.
        the key is the :attr:`~ImproperTerm.name` of the object.
    vdw_cutoff : float
        Cutoff distance for vdW interactions.
        Will be ignored if periodic boundary condition is not used.
    vdw_long_range : str
        The method to handle the long-range vdW interactions.
        Optional values: :attr:`VDW_LONGRANGE_CORRECT`, :attr:`VDW_LONGRANGE_SHIFT`
        Will be ignored if periodic boundary condition is not used.
    lj_mixing_rule : str
        The rule to generate the pairwise LJ126 parameters if not provided.
        Optional values: :attr:`LJ_MIXING_NONE`, :attr:`LJ_MIXING_LB`, :attr:`LJ_MIXING_GEOMETRIC`
    scale_14_vdw : float
        The scaling factor for 1-4 vdW interactions
    scale_14_coulomb : float
        The scaling factor for 1-4 Coulomb interactions
    '''
    #: Truncated vdW interactions with long range continuum correction
    VDW_LONGRANGE_CORRECT = 'correct'
    #: Truncated vdW interactions with potential shifted so that vdW energy equal to zero at cutoff
    VDW_LONGRANGE_SHIFT = 'shift'

    #: Do not use mixing rule for LJ126 parameters
    LJ_MIXING_NONE = 'none'
    #: Lorentz-Berthelot mixing rule for LJ126 parameters (used by CHARMM and AMBER)
    LJ_MIXING_LB = 'lorentz-berthelot'
    #: Geometric mixing rule for LJ126 parameters (used by OPLS)
    LJ_MIXING_GEOMETRIC = 'geometric'

    SETTING_ATTRS = {'vdw_cutoff'      : float,
                     'vdw_long_range'  : str,
                     'lj_mixing_rule'  : str,
                     'scale_14_vdw'    : float,
                     'scale_14_coulomb': float,
                     }

    _class_map = {}

    @staticmethod
    def registor_format(extension, cls):
        ForceField._class_map[extension] = cls

    def __init__(self):
        self.atom_types: {str: AtomType} = {}
        self.qinc_terms: {str: ChargeIncrementTerm} = {}
        self.bond_terms: {str: BondTerm} = {}
        self.angle_terms: {str: AngleTerm} = {}
        self.dihedral_terms: {str: DihedralTerm} = {}
        self.improper_terms: {str: ImproperTerm} = {}
        self.vdw_terms: {str: VdwTerm} = {}
        self.pairwise_vdw_terms: {str: VdwTerm} = {}
        self.polarizable_terms: {str: PolarizableTerm} = {}
        self.virtual_site_terms: {str: VirtualSiteTerm} = {}

        self.vdw_cutoff = 1.0  # nm
        self._vdw_long_range = ForceField.VDW_LONGRANGE_CORRECT
        self._lj_mixing_rule = ForceField.LJ_MIXING_GEOMETRIC
        self.scale_14_vdw = 0.5
        self.scale_14_coulomb = 0.5

    @property
    def vdw_long_range(self):
        return self._vdw_long_range

    @vdw_long_range.setter
    def vdw_long_range(self, val):
        if val not in [ForceField.VDW_LONGRANGE_CORRECT, ForceField.VDW_LONGRANGE_SHIFT]:
            raise Exception(f'Invalid vdw_long_range: {val}')
        self._vdw_long_range = val

    @property
    def lj_mixing_rule(self):
        return self._lj_mixing_rule

    @lj_mixing_rule.setter
    def lj_mixing_rule(self, val):
        if val not in [ForceField.LJ_MIXING_NONE, ForceField.LJ_MIXING_LB, ForceField.LJ_MIXING_GEOMETRIC]:
            raise Exception(f'Invalid lj_mixing_rule: {val}')
        self._lj_mixing_rule = val

    @staticmethod
    def open(*files):
        '''
        Load ForceField from files.

        If the file does not exist, will try to locate it from `mstk/data/forcefield`.

        The parser for reading the files will be determined from the extension of the first file.
        Therefore, all the files should be in the same format.

        Parameters
        ----------
        files : str
            The files to be read. The extension can be `zfp`, `zff', `ppf` or `ff`.

            * `zfp` file is the native XML format of mstk, and will be parsed by :class:`Zfp`.
            * `zff` file is the plain text format of mstk, and will be parsed by :class:`Zff`.
            * `ppf` file will be parsed as DFF format by :class:`Ppf`.
            * `ff` file will be parsed as fftool format by :class:`Padua`.

        Returns
        -------
        forcefield : ForceField

        '''
        files_path = [f for f in files]
        for i, file in enumerate(files_path):
            if not Path(file).exists():
                file_internal = Path(DIR_MSTK) / 'data' / 'forcefield' / file
                if not file_internal.exists():
                    raise Exception(f'FF file not found: {file}')
                else:
                    files_path[i] = file_internal.as_posix()

        file = files_path[0]
        basename, ext = os.path.splitext(file)
        try:
            cls = ForceField._class_map[ext]
        except KeyError:
            raise Exception(f'Unsupported FF format: {file}')

        return cls(*files_path).forcefield

    def write(self, file):
        '''
        Write this force field into a file.

        The format of the file will be determined by its extension

        Parameters
        ----------
        file : str
        '''
        basename, ext = os.path.splitext(file)
        try:
            cls = ForceField._class_map[ext]
        except KeyError:
            raise Exception(f'Unsupported FF format: {file}')

        cls.save_to(self, file)

    @property
    def is_polarizable(self):
        '''
        Whether or not this is a polarizable force field.

        Return True as long as the :attr:`polarizable_terms` is not empty.

        Returns
        -------
        is : bool
        '''
        return len(self.polarizable_terms) != 0

    @property
    def has_virtual_site(self):
        '''
        Whether or not this force field contains virtual sites.

        Return True as long as the :attr:`virtual_site_terms` is not empty.

        Returns
        -------
        is : bool
        '''
        return len(self.virtual_site_terms) != 0

    def get_settings(self):
        '''
        Get the settings of this force field.

        Returns
        -------
        settings : dict, [str, str]

        '''
        d = {}
        for i in ('vdw_cutoff', 'vdw_long_range', 'lj_mixing_rule',
                  'scale_14_vdw', 'scale_14_coulomb'):
            d[i] = getattr(self, i)
        return d

    def restore_settings(self, d):
        '''
        Restore the settings of this force field

        Parameters
        ----------
        d : dict, [str, str]

        '''
        for i in ('vdw_cutoff', 'vdw_long_range', 'lj_mixing_rule',
                  'scale_14_vdw', 'scale_14_coulomb'):
            setattr(self, i, d[i])

    def add_term(self, term, replace=False):
        '''
        Add a force field term into this force field.

        If a terms already exists in the force field,
        the argument `replace` will determine the behavior.
        If replace is True, the one existed will be replaced by the new term.
        Otherwise, an Exception will be raised.

        Parameters
        ----------
        term : subclass of FFTerm
        replace : bool
        '''
        _duplicated = False
        if isinstance(term, AtomType):
            if term.name not in self.atom_types or replace:
                self.atom_types[term.name] = term
            else:
                _duplicated = True
        elif isinstance(term, ChargeIncrementTerm):
            if term.name not in self.qinc_terms or replace:
                self.qinc_terms[term.name] = term
            else:
                _duplicated = True
        elif isinstance(term, BondTerm):
            if term.name not in self.bond_terms or replace:
                self.bond_terms[term.name] = term
            else:
                _duplicated = True
        elif isinstance(term, AngleTerm):
            if term.name not in self.angle_terms or replace:
                self.angle_terms[term.name] = term
            else:
                _duplicated = True
        elif isinstance(term, DihedralTerm):
            if term.name not in self.dihedral_terms or replace:
                self.dihedral_terms[term.name] = term
            else:
                _duplicated = True
        elif isinstance(term, ImproperTerm):
            if term.name not in self.improper_terms or replace:
                self.improper_terms[term.name] = term
            else:
                _duplicated = True
        elif isinstance(term, VdwTerm):
            if term.type1 == term.type2:
                if term.name not in self.vdw_terms or replace:
                    self.vdw_terms[term.name] = term
                else:
                    _duplicated = True
            else:
                if term.name not in self.pairwise_vdw_terms or replace:
                    self.pairwise_vdw_terms[term.name] = term
                else:
                    _duplicated = True
        elif isinstance(term, PolarizableTerm):
            if term.name not in self.polarizable_terms or replace:
                self.polarizable_terms[term.name] = term
            else:
                _duplicated = True
        elif isinstance(term, VirtualSiteTerm):
            if term.name not in self.virtual_site_terms or replace:
                self.virtual_site_terms[term.name] = term
            else:
                _duplicated = True
        else:
            raise Exception('Invalid term to add')

        if _duplicated:
            raise Exception(f'{str(term)} already exist in FF')

    def get_vdw_term(self, type1, type2, mixing=True):
        '''
        Get the vdW term between two atom types.

        If type1 and type2 are the same, then will search parameters in :attr:`vdw_terms` and return the reference of the term.
        If not found, an Exception will be raised.
        If type1 and type2 are not the same, then will search parameters in :attr:`pairwise_vdw_terms` and return the reference of the term.
        If not found and `mixing` is True and :attr:`lj_mixing_rule` does not equal to :attr:`LJ_MIXING_NONE`,
        then a vdw term will be constructed from the mixing rule and be returned.
        Otherwise, an Exception will be raised.
        The constructed vdw term will be :class:`LJ126Term` if vdw for both type1 and type2 are :class:`LJ126Term`,
        otherwise a :class:`MieTerm` will be constructed.

        Parameters
        ----------
        type1 : AtomType or str
            If type1 is a AtomType object, then will search for its equivalent type for vdW parameters.
            If type1 is a str, then will match exactly this type.
        type2 : AtomType or str
            If type2 is a AtomType object, then will search for its equivalent type for vdW parameters.
            If type2 is a str, them will match exactly this type.
        mixing : bool
            Whether or not using combination rule for LJ126Term.

        Returns
        -------
        term : subclass of VdwTerm
        '''
        at1: str = type1.eqt_vdw if type(type1) is AtomType else type1
        at2: str = type2.eqt_vdw if type(type2) is AtomType else type2
        vdw = VdwTerm(at1, at2)
        if at1 == at2:
            vdw = self.vdw_terms.get(vdw.name)
            if vdw is not None:
                return vdw
            else:
                raise FFTermNotFoundError(f'VdwTerm for {at1} not found')

        vdw = self.pairwise_vdw_terms.get(vdw.name)

        if vdw is not None:
            return vdw
        elif not mixing:
            raise FFTermNotFoundError(f'VdwTerm for {at1}-{at2} not found')

        lj1 = self.vdw_terms.get(VdwTerm(at1, at1).name)
        lj2 = self.vdw_terms.get(VdwTerm(at2, at2).name)
        if lj1 is None or lj2 is None:
            raise FFTermNotFoundError(f'VdwTerm for {at1} or {at2} not found')
        if type(lj1) not in (LJ126Term, MieTerm) or type(lj2) not in (LJ126Term, MieTerm):
            raise Exception('Cannot use mixing rule for vdW terms other than LJ126Term and MieTerm')

        if self.lj_mixing_rule == self.LJ_MIXING_LB:
            epsilon = math.sqrt(lj1.epsilon * lj2.epsilon)
            sigma = (lj1.sigma + lj2.sigma) / 2
        elif self.lj_mixing_rule == self.LJ_MIXING_GEOMETRIC:
            epsilon = math.sqrt(lj1.epsilon * lj2.epsilon)
            sigma = math.sqrt(lj1.sigma * lj2.sigma)
        else:
            raise Exception('Unknown mixing rule for vdW terms')

        if type(lj1) is LJ126Term and type(lj2) is LJ126Term:
            return LJ126Term(at1, at2, epsilon, sigma)

        repulsion1, attraction1 = (lj1.repulsion, lj1.attraction) if type(lj1) is MieTerm else (12, 6)
        repulsion2, attraction2 = (lj2.repulsion, lj2.attraction) if type(lj2) is MieTerm else (12, 6)
        repulsion = math.sqrt(repulsion1 * repulsion2)
        attraction = math.sqrt(attraction1 * attraction2)
        return MieTerm(at1, at2, epsilon, sigma, repulsion, attraction)

    def get_eqt_for_bond(self, bond):
        '''
        Get the equivalent atom types for bond parameters of the two atoms in a bond.

        Parameters
        ----------
        bond : ~mstk.topology.Bond

        Returns
        -------
        type1 : str
            The equivalent atom type for bond parameters of the first atom in this bond.
        type2 : str
            The equivalent atom type for bond parameters of the second atom in this bond.
        '''
        try:
            at1 = self.atom_types.get(bond.atom1.type).eqt_bond
            at2 = self.atom_types.get(bond.atom2.type).eqt_bond
        except:
            raise FFTermNotFoundError(
                f'Atom type {bond.atom1.type} or {bond.atom2.type} not found in FF')
        return at1, at2

    def get_bond_term(self, type1, type2):
        '''
        Get the bond term for the bond formed by two atom types.

        If not found, an Exception will be raised.

        Parameters
        ----------
        type1 : AtomType or str
            If type1 is a AtomType object, then will search for its equivalent type for bond parameters.
            If type1 is a str, then will match exactly this type.
        type2 : AtomType or str
            If type2 is a AtomType object, then will search for its equivalent type for bond parameters.
            If type2 is a str, them will match exactly this type.

        Returns
        -------
        term : subclass of BondTerm
        '''
        at1: str = type1.eqt_bond if type(type1) is AtomType else type1
        at2: str = type2.eqt_bond if type(type2) is AtomType else type2
        bterm = BondTerm(at1, at2, 0)
        try:
            bterm = self.bond_terms[bterm.name]
        except:
            raise FFTermNotFoundError(f'{str(bterm)} not found in FF')

        return bterm

    def get_eqt_for_angle(self, angle):
        '''
        Get the equivalent atom types for angle parameters of the three atoms in a angle.

        Parameters
        ----------
        angle : ~mstk.topology.Angle

        Returns
        -------
        type1 : str
            The equivalent atom type for angle parameters of the first atom in this angle.
        type2 : str
            The equivalent atom type for angle parameters of the second atom in this angle.
        type3 : str
            The equivalent atom type for angle parameters of the third atom in this angle.
        '''
        try:
            at1 = self.atom_types.get(angle.atom1.type).eqt_ang_s
            at2 = self.atom_types.get(angle.atom2.type).eqt_ang_c
            at3 = self.atom_types.get(angle.atom3.type).eqt_ang_s
        except:
            raise FFTermNotFoundError(f'Atom type {angle.atom1.type} or {angle.atom2.type} '
                                      f'or {angle.atom3.type} not found in FF')
        return [(at1, at2, at3),
                (at1, at2, '*'),
                ('*', at2, at3),
                ('*', at2, '*'),
                ]

    def get_angle_term(self, type1, type2, type3):
        '''
        Get the angle term for the angle formed by three atom types.

        If not found, an Exception will be raised.

        Parameters
        ----------
        type1 : AtomType or str
            If type1 is a AtomType object, then will search for its equivalent type for angle side parameters.
            If type1 is a str, then will match exactly this type.
        type2 : AtomType or str
            If type2 is a AtomType object, then will search for its equivalent type for angle center parameters.
            If type2 is a str, them will match exactly this type.
        type3 : AtomType or str
            If type3 is a AtomType object, then will search for its equivalent type for angle side parameters.
            If type3 is a str, them will match exactly this type.

        Returns
        -------
        term : subclass of AngleTerm
        '''
        at1: str = type1.eqt_ang_s if type(type1) is AtomType else type1
        at2: str = type2.eqt_ang_c if type(type2) is AtomType else type2
        at3: str = type3.eqt_ang_s if type(type3) is AtomType else type3
        aterm = AngleTerm(at1, at2, at3, 0)
        try:
            aterm = self.angle_terms[aterm.name]
        except:
            raise FFTermNotFoundError(f'{str(aterm)} not found in FF')

        return aterm

    def get_eqt_for_dihedral(self, dihedral):
        '''
        Get the list of possible equivalent atom types for dihedral parameters of the four atoms in a dihedral.

        Because the wildcard (*) is allowed for the side atoms of a dihedral term,
        a list of possible equivalent atom types is returned.

        Parameters
        ----------
        dihedral : ~mstk.topology.Dihedral

        Returns
        -------
        types : list of tuple of str
            Each element of the list is a tuple of four str (type1, type2, type3, type4),
            which are the equivalent atom types for dihedral parameters of the four atom in this dihedral.
        '''
        try:
            at1 = self.atom_types.get(dihedral.atom1.type).eqt_dih_s
            at2 = self.atom_types.get(dihedral.atom2.type).eqt_dih_c
            at3 = self.atom_types.get(dihedral.atom3.type).eqt_dih_c
            at4 = self.atom_types.get(dihedral.atom4.type).eqt_dih_s
        except:
            raise FFTermNotFoundError(f'Atom type {dihedral.atom1.type} or {dihedral.atom2.type} '
                                      f'or {dihedral.atom3.type} or {dihedral.atom4.type} not found in FF')
        return [(at1, at2, at3, at4),
                (at1, at2, at3, '*'),
                ('*', at2, at3, at4),
                ('*', at2, at3, '*')]

    def get_dihedral_term(self, type1, type2, type3, type4):
        '''
        Get the dihedral term for the dihedral formed by four atom types.

        If not found, an Exception will be raised.

        Parameters
        ----------
        type1 : AtomType or str
            If type1 is a AtomType object, then will search for its equivalent type for dihedral side parameters.
            If type1 is a str, then will match exactly this type.
        type2 : AtomType or str
            If type2 is a AtomType object, then will search for its equivalent type for dihedral center parameters.
            If type2 is a str, them will match exactly this type.
        type3 : AtomType or str
            If type3 is a AtomType object, then will search for its equivalent type for dihedral center parameters.
            If type3 is a str, them will match exactly this type.
        type4 : AtomType or str
            If type4 is a AtomType object, then will search for its equivalent type for dihedral side parameters.
            If type4 is a str, them will match exactly this type.

        Returns
        -------
        term : subclass of DihedralTerm
        '''
        at1: str = type1.eqt_dih_s if type(type1) is AtomType else type1
        at2: str = type2.eqt_dih_c if type(type2) is AtomType else type2
        at3: str = type3.eqt_dih_c if type(type3) is AtomType else type3
        at4: str = type4.eqt_dih_s if type(type4) is AtomType else type4
        dterm = DihedralTerm(at1, at2, at3, at4)
        try:
            dterm = self.dihedral_terms[dterm.name]
        except:
            raise FFTermNotFoundError(f'{str(dterm)} not found in FF. You may use wildcard (*) for side atoms')

        return dterm

    def get_eqt_for_improper(self, improper):
        '''
        Get the list of possible equivalent atom types for improper parameters of the four atoms in a improper.

        Because the wildcard (*) is allowed for the side atoms of a improper term,
        a list of possible equivalent atom types is returned.

        Parameters
        ----------
        improper : ~mstk.topology.Improper

        Returns
        -------
        types : list of tuple of str
            Each element of the list is a tuple of four str (type1, type2, type3, type4),
            which are the equivalent atom types for improper parameters of the four atom in this improper.
        '''
        try:
            at1 = self.atom_types.get(improper.atom1.type).eqt_imp_c
            at2 = self.atom_types.get(improper.atom2.type).eqt_imp_s
            at3 = self.atom_types.get(improper.atom3.type).eqt_imp_s
            at4 = self.atom_types.get(improper.atom4.type).eqt_imp_s
        except:
            raise FFTermNotFoundError(f'Atom type {improper.atom1.type} or {improper.atom2.type} '
                                      f'or {improper.atom3.type} or {improper.atom4.type} not found in FF')
        return [(at1, at2, at3, at4),
                (at1, at2, at3, '*'),
                (at1, at2, '*', at4),
                (at1, '*', at3, at4),
                (at1, at2, '*', '*'),
                (at1, '*', at3, '*'),
                (at1, '*', '*', at4),
                (at1, '*', '*', '*')]

    def get_improper_term(self, type1, type2, type3, type4) -> ImproperTerm:
        '''
        Get the improper term for the improper formed by four atom types.

        If not found, an Exception will be raised.

        Parameters
        ----------
        type1 : AtomType or str
            If type1 is a AtomType object, then will search for its equivalent type for improper center parameters.
            If type1 is a str, then will match exactly this type.
        type2 : AtomType or str
            If type2 is a AtomType object, then will search for its equivalent type for improper side parameters.
            If type2 is a str, them will match exactly this type.
        type3 : AtomType or str
            If type3 is a AtomType object, then will search for its equivalent type for improper side parameters.
            If type3 is a str, them will match exactly this type.
        type4 : AtomType or str
            If type4 is a AtomType object, then will search for its equivalent type for improper side parameters.
            If type4 is a str, them will match exactly this type.

        Returns
        -------
        term : subclass of ImproperTerm
        '''
        at1: str = type1.eqt_imp_c if type(type1) is AtomType else type1
        at2: str = type2.eqt_imp_s if type(type2) is AtomType else type2
        at3: str = type3.eqt_imp_s if type(type3) is AtomType else type3
        at4: str = type4.eqt_imp_s if type(type4) is AtomType else type4
        iterm = ImproperTerm(at1, at2, at3, at4)
        try:
            iterm = self.improper_terms[iterm.name]
        except:
            raise FFTermNotFoundError(f'{str(iterm)} not found in FF. You may use wildcard (*) for side atoms')

        return iterm

    def get_eqt_for_qinc(self, bond):
        '''
        Get the equivalent atom types for charge increment parameters of the two atoms in a bond.

        Parameters
        ----------
        bond : ~mstk.topology.Bond

        Returns
        -------
        type1 : str
            The equivalent atom type for charge increment parameters of the first atom in this bond.
        type2 : str
            The equivalent atom type for charge increment parameters of the second atom in this bond.
        '''
        try:
            at1 = self.atom_types.get(bond.atom1.type).eqt_q_inc
            at2 = self.atom_types.get(bond.atom2.type).eqt_q_inc
        except:
            raise FFTermNotFoundError(
                f'Atom type {bond.atom1.type} or {bond.atom2.type} not found in FF')
        return at1, at2

    def get_qinc_term(self, type1, type2):
        '''
        Get the charge increment term for the bond formed by two atom types.
        A direction will also be returned, which equal to 1 if type1 in the charge increment term matches type1 in arguments, -1 otherwise.

        If not found, an Exception will be raised.

        Parameters
        ----------
        type1 : AtomType or str
            If type1 is a AtomType object, then will search for its equivalent type for charge increment parameters.
            If type1 is a str, then will match exactly this type.
        type2 : AtomType or str
            If type2 is a AtomType object, then will search for its equivalent type for charge increment parameters.
            If type2 is a str, them will match exactly this type.

        Returns
        -------
        term : subclass of BondTerm
        direction : [1, -1]
        '''
        at1: str = type1.eqt_q_inc if type(type1) is AtomType else type1
        at2: str = type2.eqt_q_inc if type(type2) is AtomType else type2
        qterm = ChargeIncrementTerm(at1, at2, 0)
        direction = 1 if qterm.type1 == at1 else -1
        try:
            qterm = self.qinc_terms[qterm.name]
        except:
            raise FFTermNotFoundError(f'{str(qterm)} not found in FF')

        return qterm, direction

    def assign_mass(self, top):
        '''
        Assign masses for all atoms in a topology or molecule from the force field.

        The atom types should have been defined, and the AtomType in FF should carry mass information.
        The masses of Drude particles will be determined ONLY from the DrudeTerm,
        and the the same amount of mass will be subtracted from the parent atoms.
        That is, if there is an AtomType for Drude particles, the mass attribute of this AtomType will be simply ignored.

        Parameters
        ----------
        top : Topology or Molecule
        '''
        _atype_not_found = set()
        _atype_no_mass = set()
        _zero_mass = set()
        for atom in top.atoms:
            if atom.is_drude:
                continue
            atype = self.atom_types.get(atom.type)
            if atype is None:
                _atype_not_found.add(atom.type)
                continue
            elif atype.mass == -1:
                _atype_no_mass.add(atom.type)
            elif atype.mass == 0:
                _zero_mass.add(atom.type)
            atom.mass = atype.mass

        if _atype_not_found != set():
            logger.error('%i atom types not found: %s' % (
                len(_atype_not_found), ' '.join(_atype_not_found)))
            raise Exception(f'Assign mass for {str(top)} failed')
        if _atype_no_mass != set():
            logger.error('%i atom types in FF do not carry mass information: %s' % (
                len(_atype_no_mass), ' '.join(_atype_no_mass)))
            raise Exception(f'Assign mass {str(top)}  failed')
        if _zero_mass != set():
            logger.warning(f'%i atoms in {str(top)} carry zero mass: %s' % (
                len(_zero_mass), ' '.join(_zero_mass)))

        for parent, drude in top.get_drude_pairs():
            atype = self.atom_types[parent.type]
            pterm = self.polarizable_terms.get(atype.eqt_polar)
            if pterm is None:
                raise Exception(f'Polarizable term for {atype} not found in FF')
            if type(pterm) != DrudeTerm:
                raise Exception('Polarizable terms other than DrudeTerm haven\'t been implemented')
            drude.mass = pterm.mass
            parent.mass -= pterm.mass

    def assign_charge(self, top, transfer_qinc_terms=False):
        '''
        Assign charges for all atoms in a topology or molecule from the force field.

        The atom types should have been defined.
        The charge of corresponding AtomType in FF will be assigned to the atoms first.
        Then if there are ChargeIncrementTerm, the charge will be transferred between bonded atoms.
        The charge of Drude particles will be determined ONLY from the DrudePolarizableTerm,
        and the the same amount of charge will be subtracted from the parent atoms.
        That is, if there is an AtomType for Drude particles, the charge attribute of this AtomType will be simply ignored.

        If charge increment parameters required by the topology are not found in the force field,
        `mstk` can try to transfer parameters from more general terms in the force field.
        e.g. if charge increment term between 'c_4o2' and 'n_3' is not found, the term between 'c_4' and 'n_3' will be used.
        This mechanism is initially designed for TEAM force field.
        It is disabled by default, and can be enabled by setting argument `transfer_qinc_terms` to True.

        Parameters
        ----------
        top : Topology or Molecule
        transfer_qinc_terms : bool, optional
        '''
        from .dff_utils import dff_fuzzy_match

        _q_zero = []
        for atom in top.atoms:
            if atom.is_drude:
                continue
            try:
                charge = self.atom_types[atom.type].charge
            except:
                raise Exception(f'Atom type {atom.type} not found in FF')
            atom.charge = charge
            if charge == 0:
                _q_zero.append(atom)

        if len(self.qinc_terms) == 0 and len(_q_zero) > 0:
            msg = '%i atoms in %s have zero charge. But charge increment terms not found in FF: %s' % (
                len(_q_zero), top, ' '.join([a.name for a in _q_zero[:10]]))
            if len(_q_zero) > 10:
                msg += ' and more ...'
            logger.warning(msg)

        if len(self.qinc_terms) > 0:
            _qterm_not_found = set()
            _qterm_transferred = set()
            for bond in filter(lambda x: not x.is_drude, top.bonds):
                _found = False
                ats = self.get_eqt_for_qinc(bond)
                if ats[0] == ats[1]:
                    continue
                _term = ChargeIncrementTerm(*ats, 0)
                try:
                    qterm, direction = self.get_qinc_term(*ats)
                    _found = True
                except FFTermNotFoundError:
                    if transfer_qinc_terms:
                        qterm, score = dff_fuzzy_match(_term, self)
                        if qterm is not None:
                            direction = 1 if _term.type1 == ats[0] else -1
                            _found = True
                            _qterm_transferred.add((_term.name, qterm.name, score))

                if _found:
                    increment = qterm.value * direction
                    bond.atom1.charge += increment
                    bond.atom2.charge -= increment
                else:
                    _qterm_not_found.add(_term.name)

            if len(_qterm_transferred) > 0:
                logger.warning('%i charge increment terms not found in FF. Transferred from similar terms with score\n'
                               '        %s' % (len(_qterm_transferred),
                                               '\n        '.join(['%-16s %-16s %i' % x for x in _qterm_transferred])))
            if len(_qterm_not_found) > 0:
                logger.warning('%i charge increment terms not found in FF. Make sure FF is correct\n'
                               '        %s' % (len(_qterm_not_found),
                                               '\n        '.join(_qterm_not_found)))

        for parent, drude in top.get_drude_pairs():
            atype = self.atom_types[parent.type]
            pterm = self.polarizable_terms.get(atype.eqt_polar)
            if pterm is None:
                raise Exception(f'Polarizable term for {atype} not found in FF')
            if type(pterm) != DrudeTerm:
                raise Exception('Polarizable terms other than DrudeTerm haven\'t been implemented')
            n_H = len([atom for atom in parent.bond_partners if atom.symbol == 'H'])
            alpha = pterm.alpha + n_H * pterm.merge_alpha_H
            drude.charge = -pterm.get_charge(alpha)
            parent.charge += pterm.get_charge(alpha)
            # update alpha and thole for Drude parent particle
            parent.alpha = alpha
            parent.thole = pterm.thole
