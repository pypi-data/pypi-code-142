from Adifpy.differentiate.node import Node


def reverse_mode(func, pt, seed_vector):
    """Compute the value and directional derivative at a point, for a given function.

    Reverse mode AD calculates the derivative of a function at point
    with respect to some seed vector, at machine precision.

    Args:
        func (Callable): the function on which to evaluate
        pt (float | ndarray): the point at which to evaluate
        seed_vector (ndarray): the direction in which to evaluate
          defaults to 1 when the function's input space is R

    Returns:
        If the function's output space is R, a tuple of the value and directional derivative
        Otherwise, a tuple of two lists: the values and directional derivatives for each component

    >>> f = lambda x: x**2 + 3*x
    >>> reverse_mode(f, 1, seed_vector=1)
    (4, 5.0)
    """

    # Forward pass
    input_node = Node(pt)
    output_node = func(input_node)

    # Account for functions that are in some way "disconnected" from the input
    if type(output_node) != Node:
        return float(output_node), 0.0

    # Initialize value of last node adjoint to 1
    output_node.node_adjoint = 1

    # Reverse pass
    return float(output_node.value), float(input_node.reverse_pass())
