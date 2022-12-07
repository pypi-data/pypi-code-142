from typing import Optional

def add_many(start: float, others: list[float]) -> list[float]:
    """
    Add one number to a variable number of others.

    Parameters
    ----------
    start : The number to start with.
    others : The numbers to be added on.

    Returns
    -------
    output : The sum of start and the values in others.

    """

    return start + sum(others)

def add_many_optional(
    start: float, 
    others: Optional[list[float]]=None
) -> float:
    """
    Add one number to a variable number of others, maybe even no others.

    Parameters
    ----------
    start : The number to start with.
    others : The numbers to be added on. If None, defaults to the empty list.

    Returns
    -------
    output : The sum of start and the values in others.

    """

    if others is None:
        others = []

    return start + sum(others)

def add_two(a: float, b: float) -> float:
    """
    Add two numbers together.

    Parameters
    ----------
    a : The first number to add.
    b : The second number to add. But for whatever reason, b has a description
        that stretches over several lines.

    Returns
    -------
    c : The sum of a and b.

    """

    return a + b

def add_with_default(a: float, b: float=5) -> float:
    """
    Add two numbers with a sensible default.

    Parameters
    ----------
    a : The first number to add.
    b : The second number to add. Defaults to 5.

    Returns
    -------
    c : The sum of a and b.

    """

    return a + b

def add_with_optional_negation(a: float, b: float, negate: bool=False) -> float:
    """
    Add two numbers with a sensible default.

    Parameters
    ----------
    a : The first number to add.
    b : The second number to add.
    negate : Whether to negate the sum. Defaults to False.

    Returns
    -------
    c : The sum of a and b, maybe negated.

    """

    c = a + b
    if negate:
        c = -c

    return c

def add_with_negation(a: float, b: float, negate: bool) -> float:
    """
    Add two numbers with a sensible default.

    Parameters
    ----------
    a : The first number to add.
    b : The second number to add.
    negate : Whether to negate the sum.

    Returns
    -------
    c : The sum of a and b, maybe negated.

    """

    c = a + b
    if negate:
        c = -c

    return c

def subtract_three(a: float, b: float, c: float) -> float:
    """
    Subtract three numbers.

    The usage of this function is a little more complicated, so in addition to
    its short description it has a longer description that is split over not
    just two, but three lines.

    Parameters
    ----------
    a : The number we start with.
    b : The first number we subtract off.
    c : The second number we subtract off.

    Returns
    -------
    d : The result of subtraction, maybe negated.

    """

    return a - b - c
