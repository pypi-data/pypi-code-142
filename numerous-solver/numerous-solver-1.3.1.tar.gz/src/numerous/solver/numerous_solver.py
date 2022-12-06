import time
import logging
from collections import namedtuple

from numba import njit
import numpy as np
from copy import deepcopy
from typing import Union, Optional

from .solver_methods import BaseMethod, RK45, Euler, BDF, NoDiff
from .interface import DefaultEventHandler, Interface, _JitHelper, Model, Solution, \
    EventHandler
from .solve_states import SolveEvent, SolveStatus


solver_methods = {'RK45': RK45, 'Euler': Euler, 'BDF': BDF, 'NoDiff': NoDiff}

_Info = namedtuple('Info', ['status', 'event_id', 'step_info', 'initial_step', 'dt', 't', 'y', 'order_', 'roller',
                           'solve_state', 'ix_eval', 'g', 'step_converged', 'event_trigger'])

try:
    FEPS = np.finfo(1.0).eps
except AttributeError:
    FEPS = 2.220446049250313e-16

logger = logging.getLogger(__name__)


class NumerousSolver:
    """Initialization method of Numerous solver.

    :param model: an instance of the model
    :type model: :class:object
    :param use_jit: bool: Use numba jit. Default is False.
    :type use_jit: bool
    :param event_handler: event handler :class:`solver.interface.EventHandler`
    :param options: Additional options to pass to the solver. Allowed values are
    * :attr:`rtol`: The relative tolerance
    * :attr:`atol`: the absolute tolerance
    * :attr:`meth`: the solver method. Possible choices are 'RK45' :meth:`~solver.solver_methods.RK45`, \
        'BDF': :meth:`~solver.solver_methods.BDF` and 'Euler' :meth:`~solver.solver_methods.Euler`.

    """

    def __init__(self, model: Union[Model, object],
                 use_jit: bool = False, event_handler=None,
                 **options):

        if not event_handler:
            event_handler = DefaultEventHandler()
        self.event_handler: EventHandler = event_handler
        self.options = options
        self.use_jit = use_jit
        self.model = model
        self.interface = model.generate_interface(use_jit)
        if not hasattr(self.interface, '_numba_type_') and use_jit:
            raise TypeError("when requesting a jitted solver, the interface must also be jitted")

        odesolver_options = {
            'longer': self.options.get('longer', 1.2), 'shorter': self.options.get('shorter', 0.8),
            'min_step': self.options.get('min_step', 10 * FEPS), 'strict_eval': True,
            'max_step': self.options.get('max_step', np.inf), 'first_step': self.options.get('first_step', None),
            'atol': self.options.get('atol', 1e-6), 'rtol': self.options.get('rtol', 1e-3),
            'submethod': self.options.get('submethod', None),
        }
        self.method_options = odesolver_options

        y0 = self.interface.get_states()
        self.g = self.interface.get_event_results(0, y0)
        method = self.options.get('method', 'RK45')
        self.f0 = self.interface.get_deriv(0, y0)
        if self.f0 is None or len(self.f0) == 0:
            logger.debug("Using no derivatives solver. If this is not intended, make sure you specify the 'get_deriv' "
                         "method for the model")
            method = "NoDiff"
        try:
            self.method = solver_methods[method]
        except KeyError:
            raise ValueError(f"Unknown method {self.options.get('method', 'RK45')}, "
                             f"allowed methods: {list(solver_methods.keys())}")

        self.number_of_events = len(self.g)

        self.interface.set_states(y0)

        self.info = None

        self.y0 = y0

        self._method = self.method(self.interface, self.use_jit, **self.method_options)
        assert issubclass(self.method, BaseMethod), f"{self.method} is not a BaseMethod"

        # Generate the solver
        if self.use_jit:
            self._non_compiled_solve = njit(self._generate_solver())
            self._solve = self._compile_solver()
        else:
            self._solve = self._generate_solver()

    def _generate_solver(self):
        def _solve(interface, _solve_state, initial_step, dt_0, order, order_, roller, strict_eval,
                   min_step, max_step, step_integrate_, g, number_of_events, step_converged, event_trigger,
                   t0=0.0, t_end=1000.0, t_eval=np.linspace(0.0, 1000.0, 100), ix_eval=1, event_tolerance=1e-6) -> _Info:

            # Init t to t0
            imax = int(100)
            step_info = 0
            t = t0
            t_start = t0
            dt = dt_0
            interface.pre_step(t, interface.get_states())
            y = interface.get_states()

            solve_status = SolveStatus.Running
            solve_event_id = SolveEvent.NoneEvent

            t_previous = t0
            y_previous = np.copy(y)

            # Define event derivatives, values and event guess times
            te_array = np.zeros(3)

            def is_internal_historian_update_needed(t_next_eval, t):
                if abs(t_next_eval - t) < 100 * FEPS:
                    return True
                return False

            def handle_converged(t, y, dt, ix_eval, t_next_eval):

                solve_event_id = SolveEvent.NoneEvent

                if is_internal_historian_update_needed(t_next_eval, t):
                    solve_event_id = interface.historian_update(t, y)
                    if strict_eval:
                        te_array[1] = t_next_eval = t_eval[ix_eval + 1] if ix_eval + 1 < len(t_eval) else t_eval[-1]
                    else:
                        t_next_eval = t_eval[ix_eval + 1] if ix_eval + 1 < len(t_eval) else t_eval[-1]
                    ix_eval += 1
                    te_array[0] = t + dt

                t_start = t
                t_new_test = min(te_array)

                return solve_event_id, ix_eval, t_start, t_next_eval, t_new_test

            def add_ring_buffer(t_, y_, rb, o):

                if o == order:
                    y_temp = rb[2][:, :]
                    t_temp = rb[1]
                    rb[1][0:order - 1] = t_temp[1:order]
                    rb[2][0:order - 1, :] = y_temp[1:order, :]

                o = min(o + 1, order)
                rb[1][o - 1] = t_
                rb[2][o - 1, :] = y_

                return o

            def get_order_y(rb, order):
                y = rb[2][0:order, :]
                return y

            # 0 index is used to keep next time step defined by solver
            te_array[0] = t
            # 1 index is used to keep next time to eval/save the solution

            te_array[1] = t_eval[ix_eval] + dt if strict_eval else np.inf
            t_next_eval = t_eval[ix_eval]

            event_ix = -1
            t_event = t
            y_event = y
            t_event_previous = -1
            time_event_ixs, t_next_time_event = interface.get_next_time_event(t)
            if time_event_ixs[0] >= 0:
                te_array[2] = t_next_time_event
            else:
                te_array[2] = max(te_array)

            while solve_status != SolveStatus.Finished:
                # updated events time estimates
                # # time acceleration
                if not step_converged:
                    if min_step > dt:
                        raise ValueError('dt shortened below min_dt')
                    te_array[0] = t_previous + dt
                elif step_converged and not event_trigger:
                    dt = min(max_step, dt)
                    te_array[0] = t + dt
                else:  # event
                    te_array[0] = t_event

                # Determine new test - it should be the smallest value requested by events, eval, step
                t_new_test = min(te_array)

                # Determine if rollback is needed
                # check if t_new_test is forward
                # no need to roll back if time-step is decreased, as it's not a failed step
                if (t_new_test < t) or (not step_converged):
                    # Need to roll back!
                    t_start = t_previous
                    y = y_previous

                    if t_new_test < t_start:
                        # t_new_test = t_rollback
                        # TODO: make more specific error raising here!
                        raise ValueError('Cannot go back longer than rollback point!')

                dt_ = min([t_next_eval - t_start, t_new_test - t_start])

                if order_ == 0:
                    order_ = add_ring_buffer(t, y, roller, order_)

                # solve from start to new test by calling the step function
                t, y, step_converged, step_info, _solve_state, factor = step_integrate_(interface,
                                                                                        t_start,
                                                                                        dt_, y,
                                                                                        get_order_y(roller, order_),
                                                                                        order_,
                                                                                        _solve_state)

                dt = min(dt * factor, t_end)

                event_trigger = False
                t_events = np.zeros(number_of_events) + t
                y_events = np.zeros((len(y), number_of_events))

                def sol(t, t_r, y_r):
                    yi = np.zeros(len(y))
                    tv = np.append(roller[1][0:order], t_r)
                    yv = np.append(roller[2][0:order], y_r)
                    yv = yv.reshape(order + 1, len(y)).T
                    for i, yvi in enumerate(yv):
                        yi[i] = np.interp(t, tv, yvi)
                    return yi

                def check_event(event_fun, ix, t_previous, y_previous, t, y):
                    t_l = t_previous
                    y_l = y_previous
                    e_l = event_fun(t_l, y_l)[ix]
                    t_r = t
                    y_r = y
                    e_r = event_fun(t_r, y_r)[ix]
                    status = 0
                    if np.sign(e_l) == np.sign(e_r):
                        return status, t, y
                    i = 0
                    t_m = (t_l + t_r) / 2
                    y_m = sol(t_m, t, y)

                    while status == 0:  # bisection method
                        e_m = event_fun(t_m, y_m)[ix]
                        if np.sign(e_l) != np.sign(e_m):
                            t_r = t_m
                        elif np.sign(e_r) != np.sign(e_m):
                            t_l = t_m
                        if abs(e_m) < 1e-6 or abs(t_l - t_r) < 1e-6:
                            status = 1
                        if i > imax:
                            status = -1
                        t_m = (t_l + t_r) / 2
                        y_m = sol(t_m, t, y)

                    return status, t_r, sol(t_r, t, y)

                if step_converged:
                    time_event_ixs, t_next_time_event = interface.get_next_time_event(t)
                    if time_event_ixs[0] >= 0:
                        te_array[2] = t_next_time_event
                    else:
                        te_array[2] = max(te_array)

                    g_new = interface.get_event_results(t, y)

                    up = (g <= 0) & (g_new >= 0) & (interface.get_event_directions() == 1)
                    down = (g >= 0) & (g_new <= 0) & (interface.get_event_directions() == -1)
                    g = g_new

                    for ix in np.concatenate((np.argwhere(up), np.argwhere(down))):
                        eps = 1.e-6  # for case to t_event = t
                        status, t_event, y_event = check_event(interface.get_event_results, ix[0],
                                                               t_previous, y_previous, t, y)
                        t_events[ix[0]] = t_event - eps
                        y_events[:, ix[0]] = y_event

                if min(t_events) < t:
                    event_trigger = True
                    event_ix = np.argmin(t_events)
                    t_event = t_events[event_ix]
                    y_event = y_events[:, event_ix]
                    g = interface.get_event_results(t_event, y_event)

                if not event_trigger and step_converged:
                    y_previous = y
                    t_previous = t
                    if abs(t - t_next_time_event) < 1e-6:
                        interface.set_states(y)
                        for time_event_ix in time_event_ixs:
                            y_previous = interface.run_time_event_action(t, y_previous, time_event_ix)  # todo: use interface to get y.
                        interface.set_states(y_previous)
                        solve_event_id = interface.post_time_event(t, y_previous)
                        if solve_event_id != SolveEvent.NoneEvent:
                            break

                if event_trigger:
                    # Improve detection of event

                    if abs(t_event - t_event_previous) > event_tolerance:
                        t_event_previous = t_event
                        step_converged = False  # roll back and refine search
                        dt = initial_step
                        g = interface.get_event_results(t, y_previous)
                    else:
                        interface.set_states(y_event)
                        y_previous = interface.run_event_action(t_event, y_event, event_ix)
                        interface.set_states(y_previous)

                        t_previous = t_event

                        # TODO: Update solve in solver_methods with new solve state after changing states due to events

                        solve_event_id = interface.post_event(t_event, y_previous)
                        # Immediate rollback in case of exit
                        t = t_previous
                        y = y_previous

                        if solve_event_id != SolveEvent.NoneEvent:
                            break

                if step_converged:
                    interface.set_states(y)
                    solve_event_id = interface.post_step(t, y)
                    if solve_event_id != SolveEvent.NoneEvent:
                        break

                    order_ = add_ring_buffer(t, y, roller, order_)

                    solve_event_id, ix_eval, t_start, t_next_eval, t_new_test = \
                        handle_converged(t, y, dt, ix_eval, t_next_eval)

                    if abs(t - t_end) < 100 * FEPS:
                        solve_status = SolveStatus.Finished
                        break

                    if solve_event_id != SolveEvent.NoneEvent:
                        break

            return _Info(status=solve_status, event_id=solve_event_id, step_info=step_info,
                        dt=dt, t=t, y=np.ascontiguousarray(y), order_=order_, roller=roller, solve_state=_solve_state,
                        ix_eval=ix_eval, g=g, initial_step=initial_step, step_converged=step_converged,
                        event_trigger=event_trigger)

        return _solve

    def _compile_solver(self):

        logger.info("Compiling Numerous Solver")
        generation_start = time.time()

        argtypes = []

        max_step = self.method_options.get('max_step')
        min_step = self.method_options.get('min_step')

        strict_eval = self.method_options.get('strict_eval', True)

        order = self._method.order
        initial_step = min_step

        step_integrate_ = self._method.step_func
        roller = self._init_roller(order)
        order_ = 0

        args = (self.interface,
                self._method.get_solver_state(),
                initial_step,
                initial_step,
                order,
                order_,
                roller,
                strict_eval,
                min_step,
                max_step,
                step_integrate_,
                self.g,
                self.number_of_events,
                False,
                False,
                0.0,
                0.1,
                np.array([0.0, 0.1]),
                1,
                self.method_options.get('atol')
                )
        for a in args:
            argtypes.append(self._non_compiled_solve.typeof_pyval(a))
        # Return the solver function

        _solve = self._non_compiled_solve.compile(tuple(argtypes))

        generation_finish = time.time()
        logger.info(f"Solver compiled, compilation time: {generation_finish - generation_start}")

        return _solve

    def _init_roller(self, order):
        n = order + 2
        rb0 = np.zeros((n, len(self.y0)))
        roller = (n, np.zeros(n), rb0)
        return roller

    def _init_solve(self, time: np.array, info=None, delta_t=None):

        max_step = self.method_options.get('max_step')
        min_step = self.method_options.get('min_step')
        atol = self.method_options.get('atol')
        strict_eval = self.method_options.get('strict_eval')
        step_integrate_ = self._method.step_func
        order = self._method.order

        if not info:
            self.interface.init_solver(time[0], self.y0)
            self.interface.pre_step(time[0], self.y0)
            solve_event_id = self.interface.historian_update(time[0], self.y0)
            self.event_handler.handle_solve_event(interface=self.interface, event_id=solve_event_id, t=time[0])

            # Call the solver

            y0 = deepcopy(self.y0)

            # Set options

            initial_step = self._method.initial_step

            dt = initial_step if len(y0) > 0 else time[1]-time[0]

            # figure out solve_state init
            solve_state = self._method.get_solver_state()

            roller = self._init_roller(order)
            order_ = 0
            g = self.interface.get_event_results(time[0], y0)
            step_converged = False
            event_trigger = False
        else:

            dt = delta_t  # internal solver step size
            order_ = self.info.order_
            roller = self.info.roller
            solve_state = self.info.solve_state
            g = self.info.g
            initial_step = self.info.initial_step
            step_converged = self.info.step_converged
            event_trigger = self.info.event_trigger

        return dt, strict_eval, step_integrate_, solve_state, roller, order_, order, initial_step, min_step, \
               max_step, atol, g, step_converged, event_trigger

    def reset(self):
        """Resets the solution and calls the model reset method.

        :return: None
        """
        self.event_handler.reset_solution()
        self.model.reset()
        self.info = None

    def solve(self, t_eval: np.array, y0: Optional[np.array] = None):
        """Solves the model.

        :param: t_eval: Input array of all timestamps for which solution is to be evaluated
        :param y0: States to set as initial states (optional)
        :return: None

        """
        if y0 is not None:  # Sets the initial states and resets the solution
            self.event_handler.reset_solution()
            self.interface.set_states(y0)
            self.info = None

        t_eval = t_eval.astype('float')
        logger.info('Solve started')

        self._solver(t_eval)
        logger.info("Solve ended")

    def solver_step(self, t: float, delta_t: float):
        """Performs a single step in the solver time.

        :param t: Current time
        :param delta_t: The timestep to perform
        :return: tuple: next timestep and actual internal solver step time (should match).
        """

        t_eval = np.linspace(t, t+delta_t, 2, dtype=np.float64)
        t_end = t_eval[-1]

        info = self._solver(t_eval, info=self.info, delta_t=delta_t)
        self.info = info

        return t_end, self.info.t

    def _solver(self, t_eval, info=None, delta_t=None):

        dt, strict_eval, step_integrate_, solve_state, roller, order_, order, initial_step, min_step, max_step, \
            atol, g, step_converged, event_trigger = self._init_solve(t_eval, info, delta_t)

        t_start = t_eval[0]
        t_end = t_eval[-1]

        info = self._solve(self.interface, solve_state, initial_step, dt, order, order_,
                           roller, strict_eval, min_step, max_step, step_integrate_, g, self.number_of_events,
                           step_converged, event_trigger, t_start, t_end, t_eval, 1, atol*100)

        while info.status == SolveStatus.Running:
            self.event_handler.handle_solve_event(self.interface, info.event_id, info.t)

            info = self._solve(self.interface, info.solve_state, initial_step, info.dt, order,
                               info.order_, info.roller, strict_eval, min_step, max_step, step_integrate_, info.g,
                               self.number_of_events, info.step_converged, info.event_trigger, info.t, t_end, t_eval,
                               info.ix_eval, atol*100)

        self.event_handler.handle_solve_event(self.interface, info.event_id, info.t)
        return info

    def register_endstep(self, __end_step):
        """Unused method

        :param __end_step: n/a
        :return:
        """
        self.__end_step = __end_step

    @property
    def solution(self) -> Union[Solution, str, None]:
        """Contains the solution

        :return: The solution object
        :rtype: Union[:class:`solver.interface.Solution`, str, None]
        """
        if hasattr(self.event_handler, 'solution'):
            return self.event_handler.solution
        else:
            return "no solution object in event handler"
