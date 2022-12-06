import logging
from typing import Union, Optional, List
from copy import deepcopy
import numpy as np
from .exceptions import TILMediaErrorIncompatibleVectorLength, TILMediaErrorInvalidParameter, TILMediaErrorInvalidMedium, TILMediaErrorInvalidLicense
from .batchcaller import BatchFunctionCaller
from .datacontainer import DataContainer
from .core import license_is_valid, ExternalObject, Liquid_isValid_getInfo_errorInterface, getLiquidInformation_pointer, Liquid_minimalTemperature_xi_, Liquid_maximalTemperature_xi_
from .logger import LoggerWrapper
from . import _internals as internals

_fullProperties = [
    ('d', np.float64, None, None),
    ('h', np.float64, None, None),
    ('p', np.float64, None, None),
    ('s', np.float64, None, None),
    ('T', np.float64, None, None),
    ('xi', np.float64, -1, None),
    ('cp', np.float64, None, None),
    ('beta', np.float64, None, None),
    ('Pr', np.float64, None, None),
    ('lamb', np.float64, None, None),
    ('eta', np.float64, None, None),
    ('sigma', np.float64, None, None),
    ('current_T_min', np.float64, None, None),
    ('current_T_max', np.float64, None, None)]


class Liquid(DataContainer):
    """
    This Liquid class can calculate the thermopyhsical properties of a pure or mixture of incompressible liquids.

    The following combinations of inputs can be used to calculate properties by calling a setState function:

    1. xi: mass fraction
    2. h, xi: specific enthalpy and mass fraction
    3. T, xi: temperature and mass fraction
    4. p, h, xi: pressure, specific enthalpy and mass fraction
    5. p, T, xi: pressure, temperature and mass fraction

    Args:
        liquid_name (str): complete name of the liquid
        xi (list or numpy.ndarray, optional): mass faction vector. Always one less than the number of components in mixtures. Defaults to None.
        fixed_mixing_ratio (bool, optional): if true, the mixture is treated as pure component in this interface. Defaults to False.
        compute_transport_properties (bool, optional): if true, transport properties are calculated. Defaults to True.
        instance_name (str, optional): instance name, appears in error messages. Defaults to "Liquid_Python".
        logger (logging.Logger, optional): logger instance for log and error messages of this class instance. If not set, the global setting will be used. Defaults to None.

    Example:
        >>> import tilmedia
        >>> liquid = tilmedia.Liquid('TILMedia.Water')
        >>> liquid.set_Txi(300)
        >>> round(liquid.d, 6)
        996.425346
        >>> liquid.set_pTxi(1e5, 300)
        >>> round(liquid.s, 6)
        394.977757
        >>> liquid.set(p=liquid.p, T=300)
        >>> round(liquid.s, 6)
        394.977757
        >>> liquid.set_Txi([300, 310, 320])
        >>> liquid.cp.round(6)
        array([4180.308149, 4177.312533, 4177.805418])

    """

    # static function call list
    _batch_function_calls = {
        1: [
            ("TILMedia_Liquid_minimalTemperature_xi_", lambda self: (self, ['xi'], None, ['current_T_min'])),
            ("TILMedia_Liquid_maximalTemperature_xi_", lambda self: (self, ['xi'], None, ['current_T_max'])),
        ],
        2: [
            ("TILMedia_Liquid_minimalTemperature_xi_", lambda self: (self, ['xi'], None, ['current_T_min'])),
            ("TILMedia_Liquid_maximalTemperature_xi_", lambda self: (self, ['xi'], None, ['current_T_max'])),
        ],
        3: [
            ("TILMedia_Liquid_minimalTemperature_xi_", lambda self: (self, ['xi'], None, ['current_T_min'])),
            ("TILMedia_Liquid_maximalTemperature_xi_", lambda self: (self, ['xi'], None, ['current_T_max'])),
            ("TILMedia_Liquid_specificEntropy_pTxi", lambda self: (self, ['p', 'T', 'xi'], None, ['s'])),
        ],
    }

    class _Info:
        _allowed = [
            "MediumName",
            "LibraryName",
            "LibraryLiteratureReference",
            "Description",
            "LiteratureReference",
            "T_min",
            "T_max",
            "T_data_min",
            "T_data_max",
            "xi_min",
            "xi_max",
        ]

        def __init__(self):
            self.MediumName = None
            self.LibraryName = None
            self.LibraryLiteratureReference = None
            self.Description = None
            self.LiteratureReference = None
            self.T_min = None
            self.T_max = None
            self.T_data_min = None
            self.T_data_max = None
            self.xi_min = None
            self.xi_max = None

        def __repr__(self):
            return 'TILMedia.Liquid.Info ' + self.LibraryName + ' ' + self.MediumName

        def keys(self):
            return [member for member in self._allowed if getattr(self, member) is not None]

        def __len__(self):
            return len(self._allowed)

        def __getitem__(self, key):
            if key in self._allowed:
                return getattr(self, key)
            raise KeyError("Invalid parameter requested")

        def dump(self):
            s = str(self)
            if len(s) > 0:
                print(s)

        def __str__(self):
            data = dict(self)
            units = {
                'T_min': ' K',
                'T_max': ' K',
                'T_data_min': ' K',
                'T_data_max': ' K'
            }
            return "\n".join([key + ': ' + str(value) + units.get(key, '') for key, value in data.items()])

    _status = 0
    _property_list = []

    def __init__(
        self,
        liquid_name,
        xi: Optional[Union[np.ndarray, List[float]]] = None,
        fixed_mixing_ratio=False,
        compute_transport_properties=True,
        instance_name='Liquid_Python',
        logger: Optional[logging.Logger] = None
    ):
        self._property_list = _fullProperties + self._property_list
        # properties of liquidObject
        #    [[[cog
        # import cog
        # from TILMedia import Liquid
        # import numpy as np
        # from TILMedia.internals import _generate_code
        # gas = Liquid("Water")
        # v = gas._property_list
        # cog.outl("\n".join(_generate_code(v)))
        # ]]]
        self.d = np.float64(0)  # : Density [kg/m^3]
        self.h = np.float64(0)  # : Specific enthalpy [J/kg]
        self.p = np.float64(0)  # : Pressure [Pa]
        self.s = np.float64(0)  # : Specific entropy [J/(kg*K)]
        self.T = np.float64(0)  # : Temperature [K]
        self.xi = np.zeros((1, 0), dtype=np.float64)  # : Water Mass fraction [1]
        self.cp = np.float64(0)  # : Specific isobaric heat capacity cp [J/(kg*K)]
        self.beta = np.float64(0)  # : Isobaric thermal expansion coefficient [1/K]
        self.Pr = np.float64(0)  # : Prandtl number [1]
        self.lamb = np.float64(0)  # : Thermal conductivity [W/(m*K)]
        self.eta = np.float64(0)  # : Dynamic viscosity [Pa*s]
        self.sigma = np.float64(0)  # : Surface tension [J/m^2]
        self.current_T_min = np.float64(0)  # : Minimal temperature of the valid region [K]
        self.current_T_max = np.float64(0)  # : Maximal temperature of the valid region [K]

        self._d_vector = np.zeros(1, dtype=np.float64)
        self._h_vector = np.zeros(1, dtype=np.float64)
        self._p_vector = np.zeros(1, dtype=np.float64)
        self._s_vector = np.zeros(1, dtype=np.float64)
        self._T_vector = np.zeros(1, dtype=np.float64)
        self._xi_vector = np.zeros((1, 0), dtype=np.float64)
        self._cp_vector = np.zeros(1, dtype=np.float64)
        self._beta_vector = np.zeros(1, dtype=np.float64)
        self._Pr_vector = np.zeros(1, dtype=np.float64)
        self._lamb_vector = np.zeros(1, dtype=np.float64)
        self._eta_vector = np.zeros(1, dtype=np.float64)
        self._sigma_vector = np.zeros(1, dtype=np.float64)
        self._current_T_min_vector = np.zeros(1, dtype=np.float64)
        self._current_T_max_vector = np.zeros(1, dtype=np.float64)
        # [[[end]]]
        self._xiFixed_vector = np.zeros((1, 0), dtype=np.float64)

        self._medium = None
        self._medium_wrapper = []

        self._compute_transport_properties = compute_transport_properties

        valid_license = license_is_valid()
        if valid_license != 1:
            raise TILMediaErrorInvalidLicense("License not valid")

        # prepare error function pointer
        if logger is None:
            logger = internals._logger
        self._exceptions = []
        message_function = internals.CPRINTFUNCTION(
            lambda x, e=self._exceptions, m=self._medium_wrapper:
            internals.tilmedia_message_logger_function(e, m, logger, x)
        )
        error_function = internals.CPRINTFUNCTION(
            lambda x, e=self._exceptions, m=self._medium_wrapper:
            internals.tilmedia_error_logger_function(e, m, logger, x)
        )

        # Check if name is valid and calculate number of components
        self.fixed_mixing_ratio = fixed_mixing_ratio
        self._liquid_name = liquid_name
        self._nc_internal: int = -1
        _xi_autodetect = np.zeros(20, dtype=np.float64)
        c_logger = LoggerWrapper(logger, self._medium_wrapper, message_function, error_function)
        self.__c_logger = c_logger
        self._status, self._nc_internal = Liquid_isValid_getInfo_errorInterface(
            liquid_name+'',
            _xi_autodetect,
            True,
            c_logger)
        if self._status == 0:
            raise TILMediaErrorInvalidMedium('LiquidName "'+liquid_name +
                                             '" not valid. Could not create TILMedia object.')
        self._xi_autodetect = np.zeros(self._nc_internal-1)

        # forwarding information to other classes
        if fixed_mixing_ratio:
            self._nc = 1
        else:
            self._nc = self._nc_internal
        DataContainer.__init__(self, self._nc, 'xi')

        # update to new nc
        self._resize_properties((1,))
        self._make_properties_scalar((1,), {None: []})

        # evaluate concentration
        if self._nc_internal > 1:
            # it is a mixture
            if fixed_mixing_ratio:
                if xi is not None:
                    _, self._xiFixed_vector = internals.var_normalize_inputs(0, xi)
                    # xi is given
                    if self._xiFixed_vector.shape[-1] != self._nc_internal-1:
                        # but has the wrong length
                        raise TILMediaErrorIncompatibleVectorLength("length of xi vector should be {nc} but is {length}".format(
                            nc=self._nc_internal-1, length=self._xiFixed_vector.shape[-1]))
                else:
                    # xi is not given
                    if _xi_autodetect[0] < -1e200:
                        # and autodetection failed (should work for e.g. Refprop.R407c.mix)
                        raise TILMediaErrorInvalidParameter(
                            "xi vector with length {nc} expected, but none was given".format(nc=self._nc_internal-1))
                    # and autodetection was successful
                    for i in range(self._nc_internal-1):
                        self._xi_autodetect[i] = _xi_autodetect[i]
            else:
                # variable concentration
                if xi is None:
                    if _xi_autodetect[0] < -1e200:
                        # and autodetection failed (should work for e.g. Refprop.R407c.mix)
                        raise TILMediaErrorInvalidParameter(
                            "xi vector with length {nc} expected, but none was given".format(nc=self._nc_internal-1))
                    # and autodetection was successful
                    for i in range(self._nc_internal-1):
                        self._xi_autodetect[i] = _xi_autodetect[i]
                else:
                    _, self._xi_vector = internals.var_normalize_inputs(0, xi)
                    if self._xi_vector.shape[-1] != self._nc_internal-1:
                        # but the concentration vector has the wrong length
                        raise TILMediaErrorIncompatibleVectorLength("Length of xi vector should be {nc} but is {length}".format(
                            nc=self._nc_internal-1, length=self._xi_vector.shape[-1]))
        else:
            if xi is not None:
                _, xi = internals.var_normalize_inputs(0, xi)
                internals.check_vector_size(xi, self._nc_internal - 1)
        if xi is None:
            xi = self._xi_autodetect

        # creating TILMediaObject
        flags = 0
        if self._compute_transport_properties:
            flags = 1
        if self.fixed_mixing_ratio:
            _xi_call = self._xiFixed_vector[0]
        else:
            _xi_call = self._xi_vector[0]
        self._medium = ExternalObject(
            "Liquid",
            liquid_name,
            flags,
            _xi_call,
            self._nc,
            -1,
            instance_name,
            c_logger
            # self._messageFunction,
            # self._errorFunction,
            # c_void_p(0)
        )
        if not self._medium.ptr:
            if self._exceptions:
                exceptions = deepcopy(self._exceptions)
                while self._exceptions:
                    self._exceptions.pop()
                raise exceptions[0]
            else:
                raise TILMediaErrorInvalidMedium('LiquidName "'+liquid_name +
                                                 '" not valid. Could not create TILMedia object.')
        self._medium_wrapper.append(self._medium)
        self.xi = self._xi_vector[0]

        # initializing Info
        self.info = self._Info()
        getLiquidInformation_pointer(self.info, self._medium)

        if self._nc == 1:
            self.current_T_min = Liquid_minimalTemperature_xi_(self.xi, self._medium)
            self.current_T_max = Liquid_maximalTemperature_xi_(self.xi, self._medium)

        if self._exceptions:
            exceptions = deepcopy(self._exceptions)
            while self._exceptions:
                self._exceptions.pop()
            raise exceptions[0]

    def __del__(self):
        if self._status != 0:
            self._medium = 0

    def dump(self):
        """ Prints the current thermophysical properties of the liquid to stdout. """

        s = "---------------------------------"
        s += str(self)
        s += "---------------------------------"
        print(s)

    def __str__(self):
        value = []
        value += ["Medium: " + self._liquid_name]
        value += [DataContainer.__str__(self)]
        return "\n".join([v for v in value if v])

    def __repr__(self):
        return 'TILMedia.Liquid "' + self._liquid_name + '" (nc = '+str(self._nc)+')'

    def set_xi(self, xi: Optional[Union[np.ndarray, List[float]]] = None) -> None:
        """
        Calculates all thermophysical properties depending on the concentration.

        Args:
            xi (list, numpy.ndarray): mass fraction [1]
        """

        if self.fixed_mixing_ratio and xi is not None:
            raise TILMediaErrorInvalidParameter('If fixed_mixing_ratio is True, then xi input must not be used')
        if xi is None:
            xi = self._xi_vector[tuple([0]*(self._xi_vector.ndim-1))]

        xi, = internals.var_normalize_inputs(xi)
        internals.check_vector_size(xi, self._nc - 1)

        shape = xi.shape[:-1]
        self._resize_properties(shape)
        self._xi_vector[:] = xi

        batch_caller = BatchFunctionCaller()
        for function_name, arguments in self._batch_function_calls[1]:
            batch_caller.add_call(function_name, *arguments(self))

        calculated_properties = batch_caller.execute(self._medium, np.prod(shape))
        self._s_vector[:] = 0

        self._make_properties_scalar(shape, calculated_properties[None])

        if self._exceptions:
            if len(shape) > 1 or max(shape) > 1:
                failure_index = np.unravel_index(batch_caller.current_point, shape)
                if len(failure_index) == 1:
                    failure_index = failure_index[0]
                exception = self._exceptions[0].__class__(
                    self._exceptions[0].message
                    + '\nThe error was caused by element %s: xi=%s.'
                    % (str(failure_index), str(xi[failure_index])))
            else:
                failure_index = 0
                exception = self._exceptions[0].__class__(
                    self._exceptions[0].message
                    + '\nThe inputs were xi=%s.'
                    % (str(xi[failure_index])))
            while self._exceptions:
                self._exceptions.pop()

            raise exception

    def set_Txi(self, T: Union[float, np.ndarray, List[float]], xi: Optional[Union[np.ndarray, List[float]]] = None) -> None:
        """
        Calculates all thermophysical properties depending on temperature and independent mass fractions (always one less than the number of components in mixtures).
        Pressure and specific entropy are set to 0.

        Args:
            T (float, list, numpy.ndarray): temperature [K]
            xi (list, numpy.ndarray): mass fraction [1] (optional)
        """

        if self.fixed_mixing_ratio and xi is not None:
            raise TILMediaErrorInvalidParameter('If fixed_mixing_ratio is True, then xi input must not be used')
        if xi is None:
            xi = self._xi_vector[tuple([0]*(self._xi_vector.ndim-1))]

        T, xi = internals.var_normalize_inputs(T, xi)
        internals.check_vector_size(xi, self._nc - 1)

        shape = T.shape
        self._resize_properties(shape)
        self._p_vector[:] = 0
        self._T_vector[:] = T
        self._xi_vector[:] = xi

        batch_caller = BatchFunctionCaller()
        batch_caller.add_call("TILMedia_Liquid_properties_Txi", self, ['T', 'xi'], None, ['d', 'cp', 'beta'])
        batch_caller.add_call("TILMedia_LiquidObjectFunctions_specificEnthalpy_Txi", self, ['T', 'xi'], None, ['h'])
        if self._compute_transport_properties:
            batch_caller.add_call("TILMedia_Liquid_transportProperties_Txi", self, [
                                  'T', 'xi'], None, ['Pr', 'lamb', 'eta', 'sigma'])
        for function_name, arguments in self._batch_function_calls[2]:
            batch_caller.add_call(function_name, *arguments(self))

        calculated_properties = batch_caller.execute(self._medium, np.prod(shape))
        self._s_vector[:] = 0

        self._make_properties_scalar(shape, calculated_properties[None])

        if self._exceptions:
            if len(shape) > 1 or max(shape) > 1:
                failure_index = np.unravel_index(batch_caller.current_point, shape)
                if len(failure_index) == 1:
                    failure_index = failure_index[0]
                exception = self._exceptions[0].__class__(self._exceptions[0].message + '\nThe error was caused by element %s: T=%s, xi=%s.' %
                                                          (str(failure_index), str(T[failure_index]), str(xi[failure_index])))
            else:
                failure_index = 0
                exception = self._exceptions[0].__class__(
                    self._exceptions[0].message
                    + '\nThe inputs were T=%s, xi=%s.'
                    % (str(T[failure_index]), str(xi[failure_index])))
            while self._exceptions:
                self._exceptions.pop()

            raise exception

    def set_hxi(self, h: Union[float, np.ndarray, List[float]], xi: Optional[Union[np.ndarray, List[float]]] = None) -> None:
        """
        Calculates all thermophysical properties depending on specific enthalpy and independent mass fractions (always one less than the number of components in mixtures).
        Pressure and specific entropy are set to 0.

        Args:
            h (float, list, numpy.ndarray): specific entphalpy [J/kg]
            xi (list, numpy.ndarray): mass fraction [1] (optional)
        """

        if self.fixed_mixing_ratio and xi is not None:
            raise TILMediaErrorInvalidParameter('If fixed_mixing_ratio is True, then xi input must not be used')
        if xi is None:
            xi = self._xi_vector[tuple([0]*(self._xi_vector.ndim-1))]

        h, xi = internals.var_normalize_inputs(h, xi)
        internals.check_vector_size(xi, self._nc - 1)

        shape = h.shape
        self._resize_properties(shape)
        self._p_vector[:] = 0
        self._h_vector[:] = h
        self._xi_vector[:] = xi

        batch_caller = BatchFunctionCaller()
        batch_caller.add_call("TILMedia_Liquid_properties_hxi", self, ['h', 'xi'], None, ['d', 'cp', 'beta'])
        batch_caller.add_call("TILMedia_LiquidObjectFunctions_temperature_hxi", self, ['h', 'xi'], None, ['T'])
        if self._compute_transport_properties:
            batch_caller.add_call("TILMedia_Liquid_transportProperties_Txi", self, [
                                  'T', 'xi'], None, ['Pr', 'lamb', 'eta', 'sigma'])
        for function_name, arguments in self._batch_function_calls[2]:
            batch_caller.add_call(function_name, *arguments(self))

        calculated_properties = batch_caller.execute(self._medium, np.prod(shape))
        self._s_vector[:] = 0

        self._make_properties_scalar(shape, calculated_properties[None])

        if self._exceptions:
            if len(shape) > 1 or max(shape) > 1:
                failure_index = np.unravel_index(batch_caller.current_point, shape)
                if len(failure_index) == 1:
                    failure_index = failure_index[0]
                exception = self._exceptions[0].__class__(self._exceptions[0].message + '\nThe error was caused by element %s: h=%s, xi=%s.' %
                                                          (str(failure_index), str(h[failure_index]), str(xi[failure_index])))
            else:
                failure_index = 0
                exception = self._exceptions[0].__class__(
                    self._exceptions[0].message
                    + '\nThe inputs were h=%s, xi=%s.'
                    % (str(h[failure_index]), str(xi[failure_index])))
            while self._exceptions:
                self._exceptions.pop()

            raise exception

    def set_pTxi(self, p: Union[float, np.ndarray, List[float]], T: Union[float, np.ndarray, List[float]], xi: Optional[Union[np.ndarray, List[float]]] = None):
        """
        Calculates all thermophysical properties depending on pressure, temperature and independent mass fractions
        (always one less than the number of components in mixtures).

        Args:
            p (float, list, numpy.ndarray): pressure [Pa]
            T (float, list, numpy.ndarray): temperature [K]
            xi (list, numpy.ndarray): mass fraction [1] (optional)
        """

        if self.fixed_mixing_ratio and xi is not None:
            raise TILMediaErrorInvalidParameter('If fixed_mixing_ratio is True, then xi input must not be used')
        if xi is None:
            xi = self._xi_vector[tuple([0]*(self._xi_vector.ndim-1))]

        p, T, xi = internals.var_normalize_inputs(p, T, xi)
        internals.check_vector_size(xi, self._nc - 1)

        shape = p.shape
        self._resize_properties(shape)
        self._p_vector[:] = p
        self._T_vector[:] = T
        self._xi_vector[:] = xi

        batch_caller = BatchFunctionCaller()
        batch_caller.add_call("TILMedia_Liquid_properties_Txi", self, ['T', 'xi'], None, ['d', 'cp', 'beta'])
        batch_caller.add_call("TILMedia_LiquidObjectFunctions_specificEnthalpy_Txi", self, ['T', 'xi'], None, ['h'])
        if self._compute_transport_properties:
            batch_caller.add_call("TILMedia_Liquid_transportProperties_Txi", self, [
                                  'T', 'xi'], None, ['Pr', 'lamb', 'eta', 'sigma'])
        for function_name, arguments in self._batch_function_calls[3]:
            batch_caller.add_call(function_name, *arguments(self))

        calculated_properties = batch_caller.execute(self._medium, np.prod(shape))

        self._make_properties_scalar(shape, calculated_properties[None])

        if self._exceptions:
            if len(shape) > 1 or max(shape) > 1:
                failure_index = np.unravel_index(batch_caller.current_point, shape)
                if len(failure_index) == 1:
                    failure_index = failure_index[0]
                exception = self._exceptions[0].__class__(self._exceptions[0].message + '\nThe error was caused by element %s: p=%s, T=%s, xi=%s.' %
                                                          (str(failure_index), str(p[failure_index]), str(T[failure_index]), str(xi[failure_index])))
            else:
                failure_index = 0
                exception = self._exceptions[0].__class__(
                    self._exceptions[0].message
                    + '\nThe inputs were p=%s, T=%s, xi=%s.'
                    % (str(p[failure_index]), str(T[failure_index]), str(xi[failure_index])))
            while self._exceptions:
                self._exceptions.pop()

            raise exception

    def set_phxi(self, p: Union[float, np.ndarray, List[float]], h: Union[float, np.ndarray, List[float]], xi: Optional[Union[np.ndarray, List[float]]] = None):
        """
        Calculates all thermophysical properties depending on pressure, specific enthalpy and independent mass fractions (always one less than the number of components in mixtures).

        Args:
            p (float, list, numpy.ndarray): pressure [Pa]
            h (float, list, numpy.ndarray): specific entphalpy [J/kg]
            xi (list, numpy.ndarray): mass fraction [1] (optional)
        """

        if self.fixed_mixing_ratio and xi is not None:
            raise TILMediaErrorInvalidParameter('If fixed_mixing_ratio is True, then xi input must not be used')
        if xi is None:
            xi = self._xi_vector[tuple([0]*(self._xi_vector.ndim-1))]

        p, h, xi = internals.var_normalize_inputs(p, h, xi)
        internals.check_vector_size(xi, self._nc - 1)

        shape = p.shape
        self._resize_properties(shape)
        self._p_vector[:] = p
        self._h_vector[:] = h
        self._xi_vector[:] = xi

        batch_caller = BatchFunctionCaller()
        batch_caller.add_call("TILMedia_Liquid_properties_hxi", self, ['h', 'xi'], None, ['d', 'cp', 'beta'])
        batch_caller.add_call("TILMedia_LiquidObjectFunctions_temperature_hxi", self, ['h', 'xi'], None, ['T'])
        if self._compute_transport_properties:
            batch_caller.add_call("TILMedia_Liquid_transportProperties_Txi", self, [
                                  'T', 'xi'], None, ['Pr', 'lamb', 'eta', 'sigma'])
        for function_name, arguments in self._batch_function_calls[3]:
            batch_caller.add_call(function_name, *arguments(self))

        calculated_properties = batch_caller.execute(self._medium, np.prod(shape))

        self._make_properties_scalar(shape, calculated_properties[None])

        if self._exceptions:
            if len(shape) > 1 or max(shape) > 1:
                failure_index = np.unravel_index(batch_caller.current_point, shape)
                if len(failure_index) == 1:
                    failure_index = failure_index[0]
                exception = self._exceptions[0].__class__(self._exceptions[0].message + '\nThe error was caused by element %s: p=%s, h=%s, xi=%s.' %
                                                          (str(failure_index), str(p[failure_index]), str(h[failure_index]), str(xi[failure_index])))
            else:
                failure_index = 0
                exception = self._exceptions[0].__class__(
                    self._exceptions[0].message
                    + '\nThe inputs were p=%s, h=%s, xi=%s.'
                    % (str(p[failure_index]), str(h[failure_index]), str(xi[failure_index])))
            while self._exceptions:
                self._exceptions.pop()

            raise exception

    def set(self, **kwargs):
        keys = frozenset(kwargs)
        mapping = {
            frozenset({'p', 'h'}): self.set_phxi,
            frozenset({'p', 'h', 'xi'}): self.set_phxi,
            frozenset({'p', 'T'}): self.set_pTxi,
            frozenset({'p', 'T', 'xi'}): self.set_pTxi,
            frozenset({'h'}): self.set_hxi,
            frozenset({'h', 'xi'}): self.set_hxi,
            frozenset({'T'}): self.set_Txi,
            frozenset({'T', 'xi'}): self.set_Txi,
            frozenset({'xi'}): self.set_xi,
        }
        function = mapping.get(keys)
        if function:
            function(**kwargs)
        else:
            raise TILMediaErrorInvalidParameter(
                f'Properties cannot be computed from the arguments {keys}'
            )
