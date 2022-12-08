#!/usr/bin/env python3
# File       : newton.py
# Description: Computes Roots with an AD computed Jacobian
# from src import AutoDiffPy as adp
import src.autodiffpypi as adp


def newton(f, x_k, max_iterations=200, tol=1.0e-8):
    """ Newton's Method

    Args:
        f (lambda function) : the function we are looking for roots for
        x_k (int/float): the initial guess
        max_iterations (int, optional): Number of iterations of Newton's. Defaults to 200.
        tol (_type_, optional): Accuracy level representated by tolerance. Defaults to 1.0e-8.

    Returns:
        Float: Newton's approximation of the root based on the initial guess and iterations.
    """

    # Convert guess into dual number
    # x_k = adp.DualNumber(x_k)
    root = None
    flag = False
    fwd = adp.Forward(f, 1)

    for k in range(max_iterations):
        # Compute function at current guess
        fun = fwd.evaluate(x_k)

        # Run function through forward mode
        Jacobian = fwd.jacobian(x_k)
        fun = -fun
        der_xk = (fun / Jacobian[0])[0]
        
        # Check if difference is below tolerance
        if tol > abs(der_xk):
            # Compute final root approximation
            root = x_k + der_xk
            print(f"Root approximated at {root.real:e} from iteration {k+1}")
            flag = True
            break
        # Increment current guess
        x_k += der_xk
    
    if not flag:
        print(f"No root found after {max_iterations} iterations.")
        return x_k
    
    return root