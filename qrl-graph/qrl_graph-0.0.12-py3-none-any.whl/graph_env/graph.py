from scipy.sparse.csgraph import laplacian
from scipy.optimize import root_scalar
import numpy as np
from numpy import linalg as LA
from qrl_graph.utils import _postive_filter

EPS = 1e-1
class Graph:
    """The Graph environment for the quantum reinforcement learning."""
    
    
    def __init__(self, g=None, L=None) -> None:
        """the initialization of the graph."""
        if g is not None: 
            self.g = g
            self.L = laplacian(g)
        elif L is not None:
            # ignore the g (not used)
            self.L = L
        else:
            assert False, "Either g or L should be provided."

        self.prepare_data()

    def prepare_data(self):
        """Prepare the data for the classical/quantum algorithm."""
        # number of nodes
        self.N = self.L.shape[0]
        # eigen decomposition (orthogonal decomposition)
        self.D, self.V = LA.eigh(self.L)
        self.Vt = self.V.T
        # initial state
        self.u0 = np.zeros(self.N)
        self.u0[0] = 1
        
        self.vtu0 = np.dot(self.Vt, self.u0)
    
    def _classical_objective(self, t, p0=0): 
        """compute the classical objective.
        
        Args: 
            t: the time for the classical algorithm.
        """
        diag_multiplier = np.exp(-self.D * t)
        u = np.copy(self.vtu0)
        u = np.multiply(diag_multiplier, u)
        out = np.dot(self.V, u)
        return self._compute_objective_theshold(out, p0, runtime_type='classical')

    def _quantum_objective(self, t, p0=0): 
        """compute the quantum objective.
        
        Args: 
            t: the time for the classical algorithm.
        """
        diag_multiplier = np.exp(1j * self.D * t) # the minus sign is missing because of `-D`.
        u = np.copy(self.vtu0)
        u = np.multiply(diag_multiplier, u)
        out = np.dot(self.V, u)
        return self._compute_objective_theshold(out, p0, runtime_type='quantum')


    def get_classical_time(self, p0=0):
        """Get the classical time for the graph.
        
        Args:
            p0: the probability of the classical algorithm to find the threshold for the endpoints.
        """
        
        # TODO(jim): hardcode now 
        T_limit = 1000
        out = root_scalar(lambda t: self._classical_objective(t, p0), bracket=[0.0, T_limit])
        assert out.flag == 'converged', "The classical algorithm does not converge."
        
        if 1:
            t = out.root
            diag_multiplier = np.exp(-self.D * t)
            u = np.copy(self.vtu0)
            u = np.multiply(diag_multiplier, u)
            res = np.dot(self.V, u)
            # print("classical output = ", res)
            # print("sum of probability = ", np.sum(res))
            print("classical exit time  = ", t)
            print("classical exit prob  = ", res[-1])
            print("classical total cost = ", t / res[-1])
        
        
        return out.root

    def _get_classical_cost(self, t):
        """Get the classical cost for the graph for a specified time t."""
        return t / self._classical_objective(t)
    
    def _get_classical_cost_range(self, delta_t=0.01, t_limit=10):
        """Get the classical cost for the graph for a range of time t."""
        # TODO: the objective here is convex, but the root_scalar is not guaranteed to find the global minimum.
        # hint: we might also use the multi-scale optimization to find the global minimum.
        t_range = np.arange(0, t_limit, delta_t) + delta_t 
        cost_list = []
        for t in t_range:
            cost_list.append(self._get_classical_cost(t))
        
        cost_list, t_range = _postive_filter(cost_list, t_range)
        return t_range, cost_list
    
    def get_classical_cost(self, delta_t=0.1, t_limit=20):
        """Get the classical cost for the graph."""
        t_range, cost_list = self._get_classical_cost_range(delta_t=delta_t, t_limit=t_limit)
        index = np.argmin(cost_list)
        if index == 0 or index == len(cost_list) - 1 or index == 1 or index == len(cost_list) - 2:
            print("graph = ", self.g)
            print("Warning: the classical cost is not well defined.")
        return t_range[index], cost_list[index]
    
    # Note: this does not give the optimal solution !!!!!
    # def get_quantum_time(self, p0):
    #     """Get the quantum time for the graph. 
        
    #     Args:
    #         p0: the probability of the quantum algorithm to find the threshold for the endpoints.
    #     """
    #     # TODO(jim): hardcode now 
    #     T_limit = 1000
    #     out = root_scalar(lambda t: self._quantum_objective(t, p0), bracket=[0.0, T_limit])
    #     assert out.flag == 'converged', "The classical algorithm does not converge."
    #     return out.root
   
    # def get_classical_time(self, p0):
        # """Get the classical time for the graph.
        # 
        # Args:
            # p0: the probability of the classical algorithm to find the threshold for the endpoints.
        # """
        # 
        # # TODO(jim): hardcode now 
        # delta_t = 0.1
        # T_limit = 1000
        # t = 0
        # diag_multiplier = np.exp(self.D * delta_t)
        # u = np.copy(self.vtu0)
        # for i in range(int(T_limit // delta_t)):
            # t += delta_t
            # u = np.multiply(diag_multiplier, u)
            # out = np.dot(self.V, u)
            # if self.check_theshold(out, p0, runtime_type='classical'):
                # break
        # print(out)
        # return t


    def get_quantum_time(self, p0=0):
        """Get the quantum time for the graph. 
        
        Args:
            p0: the probability of the quantum algorithm to find the threshold for the endpoints.
        """
        # TODO(jim): hardcode now 
        delta_t = 0.001
        T_limit = 2
        t = 0
        diag_multiplier = np.exp(-1j * self.D * delta_t)
        u = np.copy(self.vtu0)
        for i in range(int(T_limit // delta_t)):
            t += delta_t
            u = np.multiply(diag_multiplier, u)
            out = np.dot(self.V, u)
            if self.check_theshold(out, p0, runtime_type='quantum'):
                break

        # print("quantum output = ", np.abs(out)**2)
        # print("sum of probability = ", np.sum(np.abs(out)**2))
        print("quantum exit time  = ", t)
        print("quantum exit prob  = ", np.abs(out[-1]**2))
        print("quantum total cost = ", t / np.abs(out[-1]**2))
        
        return t

    def _get_quantum_cost(self, t):
        """Get the quantum cost for the graph for a specified time t."""
        return t / self._quantum_objective(t)


    def _get_quantum_cost_range(self, delta_t=0.1, t_limit=10):
        # TODO: the objective here is convex, but the root_scalar is not guaranteed to find the global minimum.
        # hint: we might also use the multi-scale optimization to find the global minimum.
        t_range = np.arange(0, t_limit, delta_t) + delta_t 
        cost_list = []
        for t in t_range:
            cost_list.append(self._get_quantum_cost(t))
        
        cost_list, t_range = _postive_filter(cost_list, t_range)
        
        return t_range, cost_list
    

    def get_quantum_cost(self, delta_t=0.1, t_limit=10):
        # TODO: the objective here is convex, but the root_scalar is not guaranteed to find the global minimum.
        # hint: we might also use the multi-scale optimization to find the global minimum.
        t_range, cost_list = self._get_quantum_cost_range(delta_t=delta_t, t_limit=t_limit)
        index = np.argmin(cost_list)
        if index == 0 or index == len(cost_list) - 1 or index == 1 or index == len(cost_list) - 2:
            print("graph = ", self.g)
            print("Warning: the quantum cost is not well defined.")
            
        return t_range[index], cost_list[index]
    
    def get_objective(self):
        return np.log(self.get_classical_cost()[1]) / np.log(self.get_quantum_cost()[1]) 
    
    def get_qc_ratio(self, p0):
        """Get the ratio of the quantum time to the classical time.
        
        Args:
            p0: the probability of the quantum algorithm to find the threshold for the endpoints.
        """ 
        return self.get_classical_time(p0) / self.get_quantum_time(p0) 

    def _compute_objective_theshold(self, u, p0, runtime_type='classical'):
        """compute the discrepency between the objective and the threshold.
        
        Args:
            u: the state of the quantum algorithm.
            p0: the probability of the quantum algorithm to find the threshold for the endpoints.
            runtime_type: the type of the runtime, classical or quantum.
        """
        if runtime_type == 'classical':
            # classical algorithm
            return u[-1] - p0
        elif runtime_type == 'quantum':
            return np.vdot(u[-1], u[-1]).real - p0
        
        
    def check_theshold(self, u, p0, runtime_type='classical'):
        """Check the threshold for the endpoints.
        
        Args:
            u: the state of the quantum algorithm.
            p0: the probability of the quantum algorithm to find the threshold for the endpoints.
            runtime_type: the type of the runtime, classical or quantum.
        """
        if runtime_type == 'classical':
            # classical algorithm
            return u[-1] > p0
        elif runtime_type == 'quantum':
            return np.vdot(u[-1], u[-1]) > p0
        
    @property
    def laplacian(self):
        """Get the laplacian matrix."""
        return self.L
    
    def show_graph(self, name='graph'):
        """Show the graph."""
        # TODO(jim): not implemented yet
        if self.g is not None:
            import networkx as nx
            import matplotlib.pyplot as plt
            G = nx.from_numpy_matrix(self.g)
            nx.draw(G)
            plt.savefig(f"{name}.png")
        else:
            assert False, "Not implemented yet."
