import inspect
import logging

import numba as nb
import numpy as np
from numba.experimental.jitclass.base import JitClassType
from numba.experimental import jitclass
from numpy.typing import NDArray
from typing import Optional
from abc import ABC

from .solve_states import SolveEvent

logger = logging.getLogger(__name__)

class Solution:
    """Default class which holds the solution in arrays.
    """
    def __init__(self):
        self.results = []
        self.event_results = []
        self.time_event_results = []

    def add(self, t, states):
        """
        Add model states to `results` list

        :param t: time
        :type t: float
        :param states: states to save in `results` list. Can be solver states, can be model states. The user decides
            by specifying in the :class:`~solver.interface.EventHandler`.
        :type states: any
        :return: None
        """
        self.results.append(np.append(t, states))

    def add_event(self, t_event, states):
        """
        Add model states to ´event_results` list after a state-event.

        :param t_event: time of state event
        :param states: states to save in `event_results` list. Can be solver states, can be model states. The user
            decides by specifying in the :class:`~solver.interface.EventHandler`.
        :return:
        """
        self.event_results.append(np.append(t_event, states))

    def add_time_event(self, t_event, states):
        """
        Add model states to ´time_event_results` list after a time-event.

        :param t_event:  time of time-event
        :param states: states to save in `time_event_results` list. Can be solver states, can be model states. The user
            decides by specifying in the :class:`~solver.interface.EventHandler`.
        :return:
        """
        self.time_event_results.append(np.append(t_event, states))

    def reset(self):
        self.__init__()


class Interface:  # pragma no cover
    """
    The interface is used to connect a Model to the solver. To solve an ODE, as a minimum the methods
    get_deriv and get_states.
    """

    def get_deriv(self, t: float, y: np.array) -> Optional[np.ascontiguousarray]:
        """Function to return derivatives of state-space model. Must be implemented by user

        :param t: time
        :type t: float
        :param y: states in numpy format
        :type y: :class:`numpy.ndarray`
        :return: derivatives as array (if any, otherwise None or empty array)
        :rtype: :class:`numpy.ndarray`
        """
        return

    def get_states(self) -> np.array:
        """Function to get states and return to solver. Must be implemented by user. If model contains no states, the
        function can return an empty array.

        :return: array of states
        :rtype: :class:`numpy.ndarray`
        """
        raise NotImplementedError

    def set_states(self, y: np.array) -> None:
        """Function called by solver to overwrite states. Must be implemented by user.

        :param y: current solver states
        :type y: :class:`numpy.ndarray`
        :return: None
        """
        raise NotImplementedError

    def historian_update(self, t: float, y: np.array) -> SolveEvent:
        """Function called each time the desired solution time evaluation is reached (after convergence)

        :param t: time
        :type t: float
        :return: SolveEvent that can be used to break solver loop for external updates
        :rtype: :class:`~solver.solve_states.SolveEvent`
        """
        return SolveEvent.Historian

    def pre_step(self, t: float, y: np.array) -> None:
        """Function called once every time solver is started, also called when solve resumes after exiting due to
        SolveEvent

        :param t: time
        :type t: float
        :param y: states in numpy format
        :type y: :class:`numpy.ndarray`
        :return: None
        """
        pass

    def init_solver(self, t: float, y: np.array) -> None:
        """Function called at once beginning of solve (normal, or step) method.

        :param t:
        :param y:
        :return:
        """
        pass

    def post_step(self, t: float, y: np.array) -> SolveEvent:
        """Function called every time step has converged, and there was no event step in between.

        :param t: time
        :type t: float
        :param y: current solver and model states in numpy format
        :type y: :class:`numpy.ndarray`
        :return: SolveEvent that can be used to break solver loop for external updates
        :rtype: :class:`~solver.solve_states.SolveEvent`
        """
        return SolveEvent.NoneEvent

    def post_event(self, t: float, y: np.array) -> SolveEvent:
        """Function called every time solver has converged to an event step.

        :param t: time
        :type t: float
        :param y: current solver and model states in numpy format
        :type y: :class:`numpy.ndarray`
        :return: SolveEvent that can be used to break solver loop for external updates
        :rtype: :class:`~solver.solve_states.SolveEvent`
        """
        return SolveEvent.StateEvent

    def post_time_event(self, t: float, y: np.array) -> SolveEvent:
        """Function called each time a time event has been reached

        :param t: time
        :type t: float
        :param y: current solver and model states in numpy format
        :type y: :class:`numpy.ndarray`
        :return: SolveEvent that can be used to break solver loop for external updates
        :rtype: :class:`~solver.solve_states.SolveEvent`
        """

        return SolveEvent.TimeEvent

    def get_event_results(self, t: float, y: np.array) -> Optional[np.array]:
        """Function called to find events. Used together with event directions to determine if an event occured.

        :param t: time
        :type t: float
        :param y: current solver and model states in numpy format
        :type y: :class:`numpy.ndarray`

        :return: list of values for the all events connected to the model. The triggered event is found using a \
        bisection method, and it's index is passed to run_event_action, or None (for no events).
        :rtype: :class:`numpy.ndarray` or None

        """

        pass

    def run_event_action(self, t_event: float, y: np.array, event_idx: int) -> np.array:
        """Function called each time an event has been found, and can be used to trigger an action. The event_id is used
        to be able to distinguish which event occured.

        :param t_event: time
        :type t: float
        :param y: current solver and model states in numpy format
        :type y: :class:`numpy.ndarray`
        :param event_idx: int index of event triggered
        :type event_idx: int
        :return: updated states
        :rtype: :class:`numpy.ndarray`
        """
        return y

    def get_next_time_event(self, t) -> Optional[tuple[list[int] | NDArray[int], float]]:
        """
        Function that is called after each converged solver step. Returns a tuple which contains an index of the next
        time event action function to be trigged, and the value of the time-step when the function is triggered.

        :param t: current time
        :type t: float
        :return: Optional: tuple of list of indexes of event function(s) and next time. If no function is triggered,
                 it should return None.
        :rtype: Optional[tuple[list[int] | NDArray[int], float]]
        """
        pass

    def get_event_directions(self) -> np.array:
        """
        Function that returns the event directions. Must be implemented by user if using event.

        :return: list of directions, the length of the array of events
        :rtype: :class:`numpy.ndarray`
        """

        return np.array([0])

    def run_time_event_action(self, t: float, y: np.array, event_idx: int) -> np.array:
        """
        Function called each time a time-event has occurred

        :param t: time
        :type t: float
        :param y: current solver and model states in numpy format
        :type y: :class:`numpy.ndarray`
        :param event_idx: index of time event action (if multiple) that was triggered
        :type event_idx: int
        :return: updated states
        :rtype: :class:`numpy.ndarray`
        """
        return y

    def get_jacobian(self, t):
        """
        Method for calculating the jacobian matrix.

        :param t: time
        :type t: float
        :return: should return jacobian matrix

        """
        raise NotImplementedError


class EventHandler(ABC):
    """Event handler abstract class. Used to create event handlers for numerous solver.
    """

    def handle_solve_event(self, interface: Interface, event_id: SolveEvent, t: float):
        """Method called each time the solver exits its inner loop

        :param interface: model interface
        :type interface: :class:`solver.interface.Interface`
        :param event_id: Type of event that lead to the solver breaking its inner loop
        :type event_id: :class:`solver.solve_states.SolveEvent`
        :param t: current solver time
        :type t: float
        :return:
        """

        if event_id == SolveEvent.Historian:
            pass
        elif event_id == SolveEvent.ExternalDataUpdate:
            pass
        elif event_id == SolveEvent.HistorianAndExternalUpdate:
            pass
        elif event_id == SolveEvent.TimeEvent:
            pass
        elif event_id == SolveEvent.StateEvent:
            pass

    def reset_solution(self):
        """Method called when resetting the solution. Must be implemented by user.

        :return:
        """
        raise NotImplementedError


class DefaultEventHandler(EventHandler):
    def __init__(self):
        self.solution = Solution()

    def handle_solve_event(self, interface: Interface, event_id: SolveEvent, t: float):
        """Default method for handling solve events. Solution is saved at each historian timestep, time event, and state
        event

        :param interface: model interface
        :type interface: :class:`solver.interface.Interface`
        :param event_id: Type of event that lead to the solver breaking its inner loop
        :type event_id: :class:`solver.solve_states.SolveEvent`
        :param t: current solver time
        :type t: float
        :return:
        """
        if event_id == SolveEvent.Historian:
            self.solution.add(t, interface.get_states())
        elif event_id == SolveEvent.StateEvent:
            self.solution.add_event(t, interface.get_states())
        elif event_id == SolveEvent.TimeEvent:
            self.solution.add_time_event(t, interface.get_states())

    def reset_solution(self):
        """Default method for resetting solution

        :return:
        """
        self.solution.reset()


class _JitHelper:
    """
    The _JitHelper object class is used to wrap the 
    """
    def __init__(self, model_class, *args, **kwargs):
        self.model_class = model_class
        self.args = args
        self.kwargs = kwargs
        self.python_model = None

        args_ = self._add_args(args)
        kwargs_ = self._add_kwargs(kwargs)

        self.python_model = model_class(*args_, **kwargs_)
        self.compiled_model = None

        #  Make functions available to ModelWrapper
        callables = [func for func in dir(self.python_model) if callable(getattr(self.python_model, func))]
        for fun in callables:
            if fun.startswith('__'):
                continue
            setattr(self, fun, getattr(self.python_model, fun))

    def _add_args(self, args_: iter, jit=False):
        args__ = []
        for arg in args_:
            if not self._is_reserved_nested_type(arg):
                try:
                    _ = iter(arg)
                    args__.append(self._add_args(arg, jit))
                except TypeError as e:
                    if not "is not iterable" in e.__repr__():
                        raise
                    if isinstance(arg, _JitHelper):
                        args__.append(arg(jit=jit))
                        #args__.append(arg.python_model)
                    else:
                        args__.append(arg)
            else:
                args__.append(arg)
        return args__

    def _add_kwargs(self, kwargs_: dict, jit=False):
        kwargs__ = {}
        for k,v in kwargs_.items():
            if not self._is_reserved_nested_type(v):
                try:
                    _ = iter(v)
                    kwargs__.update({k: self._add_args(v, jit)})
                except TypeError as e:
                    if not "is not iterable" in e.__repr__():
                        raise
                    if isinstance(v, _JitHelper):
                        kwargs__.update({k: v(jit=jit)})
                        #kwargs__.update({k: v.python_model})
                    else:
                        kwargs__.update({k: v})
            else:
                kwargs__.update({k: v})
        return kwargs__

    def __call__(self, jit=False):
        """Call to _JitHelper if model needs to be jitted. In arguments contain other _JitHelper items, they are jitted 
        first before being passed to the _JitHelper function.

        :param jit: True if class needs to be jitted (must obey Numba specs), or false if using regular python
        :return: Jitted (or not) model class
        """
        if hasattr(self.python_model, '_numba_model_'):
            return self.python_model

        args = tuple(self._add_args(self.args, jit=jit))
        kwargs = self._add_kwargs(self.kwargs, jit=jit)        

        compiled_model = self.jithelper(self.model_class, jit=jit, return_wrapper=False)(*args, **kwargs)
        self.compiled_model = compiled_model
        return self.compiled_model

    def _is_reserved_nested_type(self, arg) -> bool:
        return isinstance(arg, (str, np.ndarray))

    @staticmethod
    def jithelper(model_class: callable, jit=True, return_wrapper=False) -> callable:
        """Method to create a jitted class using the spec from the model arguments. If jit=True, then all parameters
        must be resolved to numba classes.

        :param model_class: The model class to be jitted
        :type model_class: :class:`solver.interface.Model`
        :param jit: To jit or not
        :type jit: bool
        :return: Returns wrapper, jitted class, or python model (jit=False)
        :rtype: Union[:class:`numba.core.registry.CPUDispatcher`, :class:`solver.interface.Model`\
        :class:`numba.experimental.jitclass.boxing.Wrapper`]
        """
        def wrapper(*args, **kwargs):
            python_model = model_class(*args, **kwargs)

            if not jit:
                if return_wrapper:
                    return model_class
                return python_model

            spec = []
            for v in python_model.__dict__:
                obj = getattr(python_model, v)
                if type(obj) == JitClassType:
                    obj = obj()
                nbtype = nb.typeof(obj)

                if type(nbtype) == nb.types.Array:  # Array must be type 'A' -
                    # by default the nb.typeof evaluates them to type 'C'
                    spec.append((v, nb.types.Array(nbtype.dtype, nbtype.ndim, 'A')))
                else:
                    spec.append((v, nbtype))


            @jitclass(spec=spec)
            class Wrapper(model_class):
                pass

            return Wrapper(*args, **kwargs)

        return wrapper

    def _reset(self):
        """
        Method wrapper to reset numba compiled jitclasses to their default values. Calls the reset() method on the model
        """
        if not self.compiled_model:
            raise AttributeError('cannot reset - model not compiled')

        reset = getattr(self.compiled_model, 'reset', None)
        if not reset:
            logger.warning("could not reset model - no reset method specified")
            return

        reset()

class Model:
    """Helper class to decorate models.
    Holds the python model, interface and compiled model (generated once solver is compiled). The model allows
    inputs in its constructor that can be compiled with numba, for example: homogeneous lists, strings, floats.
    When the solver is called, the solver attempts to jit the model. If it fails, it will raise a numba error.
    If the user wishes, they may revert to jit=False.
    """

    def __init__(self, model_class: object, interface: str | Interface | None = None, iscomponent: bool = False):
        self.model_class = model_class
        self._interface = interface
        self.interface = None
        self.python_model = None
        self.iscomponent = iscomponent
        self.compiled_model = None
        self._JitHelper = None

    def __call__(self, *args, **kwargs):
        """When calling the Model object, the model is jitted. If the model is a component it returns the jitted class.
        Creates a new class of type Model, the calls its init function.

        :param args: Arguments to the Model
        :param kwargs: Keyword arguments to the Model
        :return: returns either a new instance of the Model class ifself, or a new instance of the jitted/non-jitted
        model_class
        :rtype: :class:`solver.interface.Model` | :class:`numba.core.registry.CPUDispatcher` | :class:object
        """

        new_class = self.__new__(self.__class__)
        new_class.__init__(self.model_class, self.interface, self.iscomponent)
        new_class._JitHelper = _JitHelper(new_class.model_class, *args, **kwargs)
        new_class.python_model = new_class._JitHelper.python_model
        if new_class.iscomponent:
            return new_class._JitHelper

        return new_class

    @classmethod
    def with_interface(cls, interface: type(Interface) | str | None = None):
        """decorator to link model to interface. Classes inside the model class must be passed as arguments, if using
        numba compiled solver (jit=True). This is due to limitations of numba.

        :param interface: the Interface connected to the model. May be omitted, in which case a string search is used.
        :type interface: `solver.interface.Interface` | str | None
        :return: Model class used for Numerous solver to generate interface and jit Model classes and arguments.
        :rtype: :class:`solver.interface.Model`
        """
        def inner(model_class):
            return cls(model_class, interface)

        return inner

    @classmethod
    def component(cls, model_class: object):
        """Decorator helper to jit models, which are used in arguments to other models ('components')

        :param model_class: The model class
        :type model_class: object`
        :return: callable Model object
        :rtype: :class:`~solver.interface.Model`
        """
        return cls(model_class, interface=None, iscomponent=True)

    def load_interface(self) -> type(Interface):
        """
        Method to load interface belonging to model

        :return:
        :rtype:
        """
        #  If no interface specified try default interface
        if not self._interface:
            self._interface = f"{self.model_class.__name__}Interface"

        #  If interface is string, use inspect to import module. Must be in same file as model class.
        interface = Interface
        if type(self._interface) == str:
            interface = getattr(inspect.getmodule(self.model_class), self._interface)
        elif hasattr(self._interface, '__class__') and self._interface.__bases__[0] == Interface:
            # If interface is not string, use class. Must be an interface class.
            interface = self._interface

        assert interface, "No interface was instantiated"
        assert interface.__bases__[0] == Interface, "Unknown type of interface"

        interface_instance = interface(self.python_model)

        has_events = interface_instance.get_event_results(0, interface_instance.get_states()) is not None
        has_time_events = interface_instance.get_next_time_event(0) is not None

        def get_event_results_mock(self, t, y):
            return np.array([0], dtype='float')

        def get_next_time_event_mock(self, t):
            return [-1], -1

        if not has_events:
            interface.get_event_results = get_event_results_mock
        if not has_time_events:
            interface.get_next_time_event = get_next_time_event_mock

        return interface

    def generate_interface(self, jit=True) -> Interface:
        """Method used by :class:`solver.numerous_solver.NumerousSolver` to generate model interface

        :param jit: if True then use numba to jit
        :type jit: bool
        :return: Returns the generated model interface
        :rtype: :class:`solver.interface.Interface`
        """
        logger.info("compiling interface")
        interface = self.load_interface()
        model_ = self._JitHelper(jit=jit)
        self.interface = _JitHelper.jithelper(interface, jit)(model_)
        self._interface_dict = interface(model_).__dict__  # Instantiate interface to get its default values
        self.compiled_model = self.interface.model

        return self.interface

    def reset(self):
        """
        Resets the model and its interface. Can be called directly, or indirectly from \
        :meth:`solver.numerous_solver.NumerousSolver.reset`. Calls the compiled model, and it's reset method, which must
        be specified by the user.

        Raises an error if interface is not compiled

        :return:
        """
        if not self.interface:
            raise AttributeError("Interface not compiled - cannot reset")

        self._JitHelper._reset()

        for k,v in self._interface_dict.items():
            if k == 'model':
                continue
            setattr(self.interface, k, v)
