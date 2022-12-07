import maz
import puan.ndarray
import numpy
import typing
import functools
import npycvx
import itertools

def convert_bound_to_constraint(bound: tuple, index: int, num_vars: int) -> numpy.ndarray:
    """
        Converts a variable bound to constraints

        Parameters
        ----------
            bound : tuple (lower, upper)
                a tuple with the lower and upper bound

            index : int
                index of the variable
            
            num_vars : int
                number of variables 

        Examples
        --------
            >>> convert_bound_to_constraint((-10, 10), 2, 5)
            array([[-10.,   0.,   1.,   0.,   0.],
                   [-10.,   0.,  -1.,   0.,   0.]])

        Returns
        -------
            out : numpy.array
        
        Notes
        -----
            A constraint is only created for bounds between the default int bounds.
    """
    res = None
    if bound[0] > puan.default_int_bounds[0]:
        constr = numpy.zeros((1,num_vars))
        constr[0,0] = bound[0]
        constr[0,index] = 1
        res = constr
    
    if bound[1] < puan.default_int_bounds[1]:
        constr = numpy.zeros((1,num_vars))
        constr[0, 0] = -bound[1]
        constr[0, index] = -1
        if res is not None:
            res = numpy.append(res, constr, axis=0)
        else: 
            res = constr
    return res

def convert_variable_bounds_to_constraints(ge_polyhedron: puan.ndarray.ge_polyhedron) -> puan.ndarray.ge_polyhedron:
    """
        Converts variable bounds of a polyhedron to constraints

        Parameters
        ----------
            ge_polyhedron : puan.ndarray.ge_polyhedron
                a polyhedron

        Examples
        --------
            >>> import puan
            >>> convert_variable_bounds_to_constraints(
            ...    puan.ndarray.ge_polyhedron([[4, 1, 1]],
            ...         [puan.variable(0, (1,1)),
            ...          puan.variable("x", bounds=(1,4)),
            ...          puan.variable("y")]))
            ge_polyhedron([[ 4,  1,  1],
                           [ 1,  1,  0],
                           [-4, -1,  0]])

        Returns
        -------
            out : puan.ndarray.ge_polyhedron
        
        Notes
        -----
            A constraint is only created for integer variables with bounds between the default int bounds.
    """
    return puan.ndarray.ge_polyhedron(
        numpy.vstack(
            [
                ge_polyhedron, 
                *list(
                    filter(
                        lambda x: x is not None,
                        map(
                            lambda x: convert_bound_to_constraint(x[1].bounds.as_tuple(), x[0], ge_polyhedron.variables.shape[0]),
                            filter(
                                lambda x: x[1].bounds.lower != x[1].bounds.upper and x[1].bounds.as_tuple() != (0,1),
                                enumerate(ge_polyhedron.variables)
                            )
                        )
                    )
                )
            ]
        ).reshape((-1, ge_polyhedron.variables.shape[0])),
        variables=ge_polyhedron.variables,
    )

def glpk_solver(ge_polyhedron: puan.ndarray.ge_polyhedron, objectives: typing.Iterable[numpy.ndarray], add_integer_constraints: bool = False) -> typing.Iterable[typing.Tuple[numpy.ndarray, int, int]]:
    
    """
        Maximizes objective functions ``w.dot(x)`` such that ``ge_polyhedron.A x >= ge_polyhedron.b`` using `GLPK` solver through npycvx python package. 
        Variable bounds are set in ``ge_polyhedron.variables``, where each variable in ``ge_polyhedron`` has the attribute ``bounds``.

        Parameters
        ----------
            ge_polyhedron: puan.ndarray.ge_polyhedron
                a polyhedron with greater or equal sign between A and b.

            objectives: Iterable[numpy.ndarray]
                an iterable of some kind of numpy ndarrays

            add_integer_constraints: bool
                if polyhedron automatically should add constraints to represent variable's bounds if variable is integer

        Examples
        --------
            >>> import puan, numpy
            >>> polyhedron = puan.ndarray.ge_polyhedron([[1, 1, 1]]) # no variables defaults to list of boolean variables
            >>> objectives = numpy.array([[1,1]])
            >>> list(glpk_solver(polyhedron, objectives))
            [(array([1, 1], dtype=int16), 2, 5)]

        Returns
        -------
            out : Iterable[Tuple[numpy.ndarray, int, int]]

    """
    if add_integer_constraints:
        extended_polyhedron = convert_variable_bounds_to_constraints(ge_polyhedron)
    else:
        extended_polyhedron = ge_polyhedron

    return itertools.starmap(
        lambda obj, sol_sc: (
            sol_sc[0],
            sol_sc[0].dot(obj) if sol_sc[0] is not None else None,
            sol_sc[1],
        ),
        zip(
            objectives,
            map(
                maz.compose(
                    maz.compose(
                        lambda x_status_code: (
                            x_status_code[1], 
                            5 if x_status_code[0] == 'optimal' else 3,
                        ),
                        functools.partial(
                            npycvx.solve_lp, 
                            *npycvx.convert_numpy(
                                extended_polyhedron.A, 
                                extended_polyhedron.b,
                                set(map(int, extended_polyhedron.A.integer_variable_indices)),
                            ), 
                            False, # means maximize
                        ),
                    )
                ),
                objectives
            )
        )
    )
