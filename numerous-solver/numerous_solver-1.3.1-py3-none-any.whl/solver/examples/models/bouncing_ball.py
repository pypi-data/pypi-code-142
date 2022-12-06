r"""
=====================================================
Solving a differential equation with discrete events
=====================================================

In this model a ball is released from a specific height, and the as the ball hits the ground it bounces back up.
This model demonstrates the use of solver events to implement discrete behavior.

The bouncing ball analytical solution
--------------------------------------

The bouncing ball model calculates the position of a ball dropped from an initial height, at rest. The ball
bounces once it hits the ground, and looses some energy as it bounces back up. This continues until the ball comes
to a rest.

The equation of motion of the ball is:

.. math::

    \frac{d^2x}{dt^2} = -g

where :math:`x` is the position of the ball, and :math:`g` is the gravitational constant.


Integration yields:

.. math::

    x(t) = -\frac{1}{2} g t^2 + v_0 \cdot t + x_0


where :math:`v_0` is the initial velocity and :math:`x_0` is the initial height of the ball. The ball hits the ground
when :math:`x(t) = 0`, so we can solve the above equation to get the initial hit, since :math:`v_0=0` initially:

.. math::

    \Delta t_{hit,1} = \frac{-v_0 + \sqrt{v_0^2 +2gx_0}}{-g}

As the ball hits the ground it looses some momentum, because of the plasticity of the bounce. If we call that loss
:math:`f_{loss}` then the velocity just after the bounce is:

.. math::

    v_{0,1} = g \sqrt{\frac{2 x_0}{g}}(1-f_{loss})

where :math:`v_{0,1}` indicates that it's the initial velocity just after the plastic deformation following hit no. 1.
Entering this into the equation of motion, we may find the time between hit no. 1 and hit no. 2 as:

.. math::

    \Delta t_{hit,2} = 2\sqrt{\frac{2x_0}{g}}(1-f_{loss})

Therefore, the total time for two hits is:

.. math::

    t_{hit,2} = \Delta t_{hit,1} + \Delta t_{hit,2} = \sqrt{\frac{2x_0}{g}} (1+2(1-f_{loss}))

Continuing along, we can find the general expression for N hits:

.. math::

    t_{hit,N} = \sqrt{\frac{2 x_0}{g}} \left ( 2\sum_{i=1}^{N} (1-f_{loss})^{i-1} -1 \right )



Implementation into numerous solver
------------------------------------

The equation of motion may also be written as two seperate ODE's for implementation into numerous solver:

.. math::

    \frac{dv}{dt} = -g

.. math::

    \frac{dx}{dt} = v

This is implemented in the `BouncingBall` models :meth:`diff` function.

To handle the momentum loss we implement an `event function` so that whenever the ball passes the zero crossing:

.. math::

    x(t) > 0 \rightarrow x(t+t_{event}) < 0

we apply the discontinuous `event action`:

.. _`event action`:

    .. math::

        v(t_{event}) = -v(t_{event}) (1-f_{loss})


To implement these we need to specify the following methods:

* :meth:`~solver.interface.Interface.get_event_results`
* :meth:`~solver.interface.Interface.get_event_directions`
* :meth:`~solver.interface.Interface.run_event_action`

Firstly, the :meth:`get_event_results` looks for an event
occuring when the event function has a root (i.e. zero crossing) between last converged solution time and current
converged solution time. The event function then simply returns the value of the position of the ball :math:`x(t)`,
because :math:`event\_fun=x(t)`, is zero when :math:`x(t)=0`.
Secondly, since we specified `-1` for the :meth:`get_event_directions`, this means that we're only interested in when
this happens as the ball falls down (as opposed to the bouncing back up). And thirdly,
:meth:`~solver.interface.Interface.run_event_action` applies the `event action`_.


Other methods that need to be implemented
for the interface are the :meth:`~solver.interface.Interface.get_deriv`, :meth:`~solver.interface.Interface.get_states`,
and the :meth:`~solver.interface.Interface.set_states`, but by now we consider these known as they have already been
discussed in e.g. :ref:`sphx_glr_auto_examples_exponential_approach.py`, :ref:`sphx_glr_auto_examples_coupled_tanks.py`
and other examples.

These are implemented in the model interface `BouncingBallInterface`, :meth:`get_event_results`

Examples
--------------------

Below is the result of running the bouncing ball model with numerous solver.

"""

import numpy as np
from numerous.solver.interface import Interface, Model
from numerous.solver.numerous_solver import NumerousSolver
import plotly.graph_objects as go
import plotly


@Model.with_interface()
class BouncingBall:

    def __init__(self, x0=1, v0=0, f_loss=0.05, g=9.81):
        self.x0 = x0
        self.y = np.array([x0, v0], dtype='float')
        self.f_loss = f_loss
        self.g = g

    def analytical_solution(self, max_hits) -> np.array:
        t_hits = np.zeros(max_hits, dtype='float')
        summation = 0
        for i in range(max_hits):
            summation += (2 * (1 - self.f_loss) ** (i))
            t_hit = np.sqrt(2 * self.x0 / self.g) * (summation - 1)
            t_hits[i] = t_hit

        return t_hits

    def diff(self, t, y):
        dvdt = -self.g
        dxdt = y[1]

        return np.array([dxdt, dvdt], dtype='float')


class BouncingBallInterface(Interface):
    def __init__(self, model):
        self.model: BouncingBall = model

    def get_deriv(self, t: float, y: np.array) -> np.ascontiguousarray:
        return self.model.diff(t, y)

    def get_event_directions(self) -> np.array:
        return np.array([-1])

    def get_event_results(self, t: float, y: np.array) -> np.array:
        return np.array([y[0]])

    def run_event_action(self, t_event: float, y: np.array, event_id: int) -> np.array:
        if event_id >= 0:
            y[1] = -y[1] * (1-self.model.f_loss)
        return y

    def get_states(self) -> np.array:
        return self.model.y

    def set_states(self, y: np.array) -> None:
        self.model.y = y


if __name__ == "__main__":

    model = BouncingBall()
    numsol = NumerousSolver(model=model, use_jit=False)
    time = np.append(np.arange(0, 10, 0.1), 10)
    numsol.solve(time)
    t = np.array(numsol.solution.results).T[0, :]
    y = np.array(numsol.solution.results).T[1, :]
    events = np.array(numsol.solution.event_results).T  # get the events
    t_events = events[0,:]  # The time which the ball hits the ground
    y_events = events[1,:]  # The position (should be 0) when the ball hits the ground

    t_ = np.append(t, t_events)  # Append to solution time vector
    ix_sort = np.argsort(t_)  # Sort arguments and find indexes to apply sorting later
    y_ = np.append(y, y_events)  # Also append position to solution position vector

    fig = go.Figure()  # Create a plotly figure
    fig.add_trace(go.Scatter(x=t_[ix_sort], y=y_[ix_sort], name=f'bouncing ball', mode="lines+markers"))  # Add a trace
    fig.update_layout(xaxis_title='time', yaxis_title='height of ball')  # Add titles

    plotly.io.show(fig)  # Plot figure




