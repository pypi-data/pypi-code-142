r"""
=============================================================
Solving without an differential equation model
=============================================================

In the example :ref:`sphx_glr_auto_examples_exponential_approach.py`, we implemented the solution to the equation

.. math::
        y(t) = 1 - \exp(-k\cdot t)

using the typical differential equation implementation :math:`\frac{dy}{dt}=f(t, y)`. It is possible to use numerous
solver without any differential equations, and simply solve :math:`y(t)` above. This can be done by implementing the
:meth:`~solver.model.Interface.post_step` method.

**note**: In a future release, we may add the possibility to solve algebraic equations as well (e.g. :math:`f(t,y)=0`),
but for now this is not possible with numerous solver.

Implementation in numerous solver
---------------------------------------------------

The :class:`ExponentialApproach` model is wrapped by the :meth:`~solver.interface.Model.with_interface` decorator,
which links the model to it's interface :class:`ExponentialApproachInterface`. It takes just one parameters as input:

=============   ==============================================================================================
Parameter       Description
=============   ==============================================================================================
k               The exponential approach factor (higher means faster approach, smaller means slower approach)
=============   ==============================================================================================

It contains one method, apart from the :meth:`__init__`, which is the :meth:`update_step` method. Calling the
:meth:`update_step` method returns the value of the exponential approach:

.. math::
        y(t) = 1 - \exp(-k\cdot t)

The interface :class:`ExponentialApproachInterface`, defines the following class methods:

* :meth:`~solver.interface.Interface.get_states`
* :meth:`~solver.interface.Interface.set_states`
* :meth:`~solver.interface.Interface.post_step`

In this model-interface pair, :meth:`get_states` simply returns the array
of states, `y` from the model :class:`ExponentialApproach`, whereas :meth:`set_states` sets the states `y` from the
solver onto the model :class:`ExponentialApproach`. Finally, :meth:`post_step` returns the derivatives from the model,
by calling the :meth:`update_step` and then :meth:`set_states`.

Examples
--------------
Below is an example code that runs the model, and creates a plot for multiple values of :math:`k`.

"""

import numpy as np

from numerous.solver.interface import Interface, Model
from numerous.solver.solve_states import SolveEvent
from numerous.solver.numerous_solver import NumerousSolver
import plotly.graph_objects as go
import plotly


@Model.with_interface()
class ExponentialApproach():
    def __init__(self, k=1.0):
        self.y = np.array([0.0])
        self.k = k

    def update_step(self, t) -> float:
        return 1-np.exp(-self.k * t)

    def reset(self):
        self.y = np.array([0.0])


class ExponentialApproachInterface(Interface):

    def __init__(self, model: ExponentialApproach):
        self.model = model

    def set_states(self, states):
        self.model.y = states

    def get_states(self):
        return self.model.y

    def post_step(self, t: float, y: np.array) -> SolveEvent:
        y = np.array([self.model.update_step(t)])
        self.set_states(y)
        return SolveEvent.NoneEvent

if __name__ == "__main__":
    model = ExponentialApproach(k=1.0)  # Generate the model
    numsol = NumerousSolver(model=model, method='RK45', use_jit=True)  # pass model to numerous solver
    time = np.append(np.arange(0, 10, 0.1), 10)  # Generate a time vector
    compiled_model = model.compiled_model

    fig = go.Figure()  # Create a plotly figure
    k = [10, 1, 0.1]
    for k_ in k:
        numsol.reset()
        compiled_model.k = k_
        numsol.solve(time)  # Solve model

        t = np.array(numsol.solution.results).T[0, :]  # Extract the solution time from the solution object
        results = np.array(numsol.solution.results).T[1]  # Extract the results from the solution object

        fig.add_trace(go.Scatter(x=t, y=results, name=f'exp approach. k={k_}'))  # Add a trace
        fig.update_layout(xaxis_title='time', yaxis_title='y(t)')  # Add titles

    plotly.io.show(fig)  # Plot figure