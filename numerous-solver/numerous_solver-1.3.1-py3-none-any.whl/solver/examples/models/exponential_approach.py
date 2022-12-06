r"""
=========================================
Solving a simple differential equation
=========================================

Implementing a differential equation inside `numerous solver` requires defining a model. In the :doc:`../tutorial`, you
could see how this could be done for the exponential approach. In this example, we will implement this model, solve it
and plot the results




The exponential approach model
------------------------------

This simple model solves the equation

.. math::
        y(t) = 1 - \exp(-k\cdot t)

by implementing the differential equation:

.. _`exponential approach differential equation`:

    .. math::
            \frac {dy} {dt} = k \cdot \exp(-k\cdot t)

The model is implemented in the :class:`ExponentialApproach` class. The model takes only one parameter as input:

=============   ==============================================================================================
Parameter       Description
=============   ==============================================================================================
k               The exponential approach factor (higher means faster approach, smaller means slower approach)
=============   ==============================================================================================

It contains one method, apart from the :meth:`__init__`, which is the :meth:`diff` method. Calling the :meth:`diff`
method returns the derivatives from the `exponential approach differential equation`_.

The :class:`ExponentialApproach` model is wrapped by the :meth:`~solver.interface.Model.with_interface` decorator,
which links the model to its interface :class:`ExponentialApproachInterface`. The interface defines the following class
methods:

* :meth:`~solver.interface.Interface.get_states`
* :meth:`~solver.interface.Interface.set_states`
* :meth:`~solver.interface.Interface.get_deriv`.

Here, :meth:`get_states` simply returns the array of states, `y` from the model :class:`ExponentialApproach`,
whereas :meth:`set_states` sets the states `y` from the solver onto the model :class:`ExponentialApproach`.
Finally, :meth:`get_deriv` returns the derivatives from the model, by calling the :meth:`diff` on the model.

Examples
--------------
Below is an example code that runs the model, and creates a plot for multiple values of :math:`k`.

"""

import numpy as np
from numerous.solver.interface import Interface, Model
from numerous.solver.numerous_solver import NumerousSolver
import plotly.graph_objects as go
import plotly

@Model.with_interface()
class ExponentialApproach:
    def __init__(self, k=1.0):
        self.y = np.array([0.0], dtype='float')
        self.k = k

    def diff(self, t, y) -> np.array:
        return np.array([self.k * np.exp(-self.k * t)])

    def reset(self):
        self.y = np.array([0.0], dtype='float')


class ExponentialApproachInterface(Interface):

    def __init__(self, model: ExponentialApproach):
        self.model = model

    def get_states(self) -> np.array:
        return self.model.y

    def set_states(self, y: np.array) -> None:
        self.model.y = y

    def get_deriv(self, t: float, y: np.array) -> np.array:
        return self.model.diff(t, y)


if __name__ == "__main__":

    model = ExponentialApproach(k=1.0) # Generate the model
    numsol = NumerousSolver(model=model, method='RK45', use_jit=True) # pass model to numerous solver
    time = np.append(np.arange(0, 10, 0.1), 10) # Generate a time vector
    compiled_model = model.compiled_model

    fig = go.Figure()  # Create a plotly figure
    k = [10, 1, 0.1]
    for k_ in k:
        numsol.reset()
        compiled_model.k = k_
        numsol.solve(time) # Solve model

        t = np.array(numsol.solution.results).T[0, :] # Extract the solution time from the solution object
        results = np.array(numsol.solution.results).T[1] # Extract the results from the solution object


        fig.add_trace(go.Scatter(x=t, y=results, name=f'exp approach. k={k_}')) # Add a trace
        fig.update_layout(xaxis_title='time', yaxis_title='y(t)') # Add titles

    plotly.io.show(fig) # Plot figure