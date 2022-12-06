from abc import abstractmethod
import numpy as np
from .function import function


class Optimizer():
    def __init__(self, learning_rate = 0.001, max_iteration = 10000, eps = 1e-15):
        if callable(learning_rate):
            self.eta = learning_rate
        else:
            self.eta = lambda t : learning_rate
        self.max_iteration = max_iteration
        self.eps = eps

    @abstractmethod
    def minimize(self,f, x_dim = 1, x0 = None,verbose=False):
        raise NotImplementedError

class GD(Optimizer):
    def minimize(self,f, x_dim = 1, x0 = None,verbose=False):
        if isinstance(f,function):
            if len(f.function_list) > 1:
                raise TypeError("Cannot optimize vector-valued function")
        else:
            f = function(f,x_dim = x_dim)
        if x0 is None:
            x0 = np.zeros(f.x_dim)
        x = x0
        t = 0
        history = []
        for i in range(self.max_iteration):
            x_new = x - self.eta(t)*f.grad(x)
            if abs(f(x)-f(x_new)) < self.eps:
                x = x_new
                break
            x = x_new
            t += 1
            if verbose:
                history.append((x,f(x)))
        if verbose:
            return x,f(x),history
        else:
            return x,f(x)

    # def maximize(self,f, x_dim = 1, x0 = None,verbose=False):
    #     if isinstance(f,function):
    #         if len(f.function_list) > 1:
    #             raise TypeError("Cannot optimize vector-valued function")
    #         neg_f = function(lambda *x: -1*f.function_list[0](*x),x_dim=x_dim)
    #     else:
    #         neg_f = function(lambda *x: -1*f(*x),x_dim = x_dim)
    #     if verbose:
    #         x,neg_f_min,history = self.minimize(neg_f,x_dim=x_dim,x0=x0,verbose=verbose)

    #     return self.minimize(neg_f,x_dim=x_dim,x0=x0,verbose=verbose)

class Adam(Optimizer):
    def __init__(self, learning_rate=0.001, max_iteration = 10000, beta_1 = 0.9, beta_2 = 0.999, epsilon = 1e-08):
        super().__init__(learning_rate, max_iteration)
        self.beta_1 = beta_1
        self.beta_2 = beta_2
        self.epsilon = epsilon

    def minimize(self,f, x_dim = 1, x0 = None,verbose=False):
        if isinstance(f,function):
            if len(f.function_list) > 1:
                raise TypeError("Cannot optimize vector-valued function")
        else:
            f = function(f,x_dim = x_dim)
        if x0 is None:
            x0 = np.zeros(f.x_dim)
        x = x0
        t = 0
        m = 0
        v = 0
        history = []
        for i in range(self.max_iteration):
            g = f.grad(x)
            m = self.beta_1 * m + (1-self.beta_1)*g
            v = self.beta_2 * v + (1-self.beta_2)*g**2
            m_hat = m/(1-self.beta_1**(t+1))
            v_hat = v/(1-self.beta_2**(t+1))
            x_new = x - self.eta(t)/np.sqrt(v_hat+self.epsilon)*m_hat
            if abs(f(x)-f(x_new)) < self.eps:
                x = x_new
                break
            x = x_new
            t += 1
            if verbose:
                    history.append((x,f(x)))
        if verbose:
            return x,f(x), history
        else:
            return x,f(x)
    
    # def maximize(self,f, x_dim = 1, x0 = None,verbose=False):
    #     if isinstance(f,function):
    #         if len(f.function_list) > 1:
    #             raise TypeError("Cannot optimize vector-valued function")
    #         neg_f = function(lambda *x: -1*f.function_list[0](*x),x_dim=x_dim)
    #     else:
    #         neg_f = function(lambda *x: -1*f(*x),x_dim = x_dim)
    #     return self.minimize(neg_f,x_dim=x_dim,x0=x0,verbose=verbose)


