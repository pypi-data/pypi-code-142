from itertools import combinations

import numpy as np
from numpy import asarray, int32, stack


class Map(object):
    
    a1 = np.array([1,0])
    a2 = np.array([1 / 2., 3**0.5 / 2.])
    
    def __init__(self, nodes, not_shown=None, indices_node_light=None):
        
        _nodes = asarray(nodes, dtype=int32)
        if np.unique(_nodes, axis=0).shape[0] != _nodes.shape[0]:
            raise ValueError(f"There may be some duplicates in `nodes`: {nodes}")
        _not_shown = [] if not_shown is None else not_shown
        
        if indices_node_light is None:
            _indices_node_light = []
        elif type(indices_node_light) is int:
            _indices_node_light = [indices_node_light]
        else: _indices_node_light = indices_node_light
        assert type(_indices_node_light) is list
            
        nodes_exist = np.full((len(_nodes),), True)
        nodes_exist[_not_shown] = False
        
        self.nodes = _nodes
        self.nodes_exist = nodes_exist
        
        self.light_is_on = False
        self.indices_node_light = _indices_node_light
        self.nodes_visible = np.full((len(_nodes),), True)
    
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__): return False
        keys = ('nodes', 'nodes_exist', 
                'light_is_on', 'indices_node_light', 'nodes_visible')
        equal = not any((np.any(getattr(self, k) != getattr(other, k)) for k in keys))
        return equal
    
    
    def __lt__(self, other):
        if not isinstance(other, self.__class__): raise ValueError()
        return False
    
    
    @staticmethod
    def within_n_steps(node1, node2, n : int):

        assert n >= 0
        _node1, _node2 = (asarray(node) for node in (node1, node2))
        assert _node1.shape[-1] == 2 and _node2.shape[-1] == 2

        node12 = _node1 - _node2

        np1 = n + 1
        within_n = np.abs(node12[...,0]) < np1
        within_n &= np.abs(node12[...,1]) < np1
        within_n &= np.abs(node12.sum(axis=-1)) < np1

        return within_n

    
    @staticmethod
    def distance(node1, node2):

        _node1, _node2 = (asarray(node) for node in (node1, node2))
        assert _node1.shape[-1] == 2 and _node2.shape[-1] == 2
        
        node12 = _node1 - _node2
        distance_twice = \
            np.abs(node12[...,0]) \
            + np.abs(node12[...,1]) \
            + np.abs(node12.sum(axis=-1))
        d, r = np.divmod(distance_twice, 2)
        assert not np.any(r != 0)

        return d
    
    
    def distance_by_indices(self, j_node_0, j_node_1):
        return self.distance(self.nodes[j_node_0], self.nodes[j_node_1])
    
    
    def connected_nodes(self, j_node):
        assert 0 <= j_node and j_node < len(self.nodes)
        
        indices_node_within_dist_1 = self.get_neighbors(j_node, n=1)
        indices_node_connected = [j_node_ for j_node_ in indices_node_within_dist_1 if j_node_ != j_node]
        return indices_node_connected
    
    
    def update_node_existence(self, node_index, exist):
        if self.nodes_exist[node_index] == exist: return
        self.nodes_exist[node_index] = exist            
    
    
    def is_connected(self, j, k):
        return self.distance_by_indices(j,k) == 1
    
    
    def node_coords(self):
        nodes_xy = np.stack([node[0]*self.a1 + node[1]*self.a2 
                             for node in self.nodes])
        return nodes_xy

    
    def path_exists(self, j_node_1, j_node_2, visible_only=False):
        
        assert j_node_1 != j_node_2
        indices_j_node, = np.where(~self.nodes_exist[[j_node_1,j_node_2]])
        if indices_j_node.size > 0:
            _arr = np.asarray([j_node_1,j_node_2])
            raise ValueError(f"Nodes with following indices does not exist: {_arr[indices_j_node]}")
        assert np.all(self.nodes_exist[[j_node_1,j_node_2]])
        
        target_node_reached = False
        paths_found = []
        no_path_exist = False
        
        paths = [[j_node_1]]
        N_max_step = len(self.nodes) # 10
        
        for j in range(N_max_step):

            paths_next = []

            for j_path, path in enumerate(paths):

                indices_node_connected = self.connected_nodes(path[-1])
                indices_node_next = [index_node_connected for index_node_connected 
                                     in indices_node_connected if index_node_connected not in path[:-1]]
                
                for index_node_next in indices_node_next:
                    if self.nodes_exist[index_node_next] == False:
                        indices_node_next.remove(index_node_next)
                
                if visible_only:
                    for index_node_next in indices_node_next:
                        if not self.nodes_visible[index_node_next]:
                            indices_node_next.remove(index_node_next)

                for j_next, index_node_next in enumerate(indices_node_next):

                    path_next = path.copy()

                    path_next.append(index_node_next)

                    if index_node_next == j_node_2:
                        target_node_reached = True
                        paths_found.append(path_next)

                    paths_next.append(path_next)

            if len(paths_next) == 0:
                no_path_exist = True
                break

            paths = paths_next

            if target_node_reached: 
                break

        from operator import xor
        assert xor(target_node_reached, no_path_exist)

        return paths_found

    
    def get_neighbors(self, index_node: int, n: int):
        return [j_node for j_node, node in enumerate(self.nodes) 
                if self.within_n_steps(node, self.nodes[index_node], n=n) and self.nodes_exist[j_node]]
    
    
    def turn_on_light(self):
        if self.light_is_on == False: self.light_is_on = True
        for index_node_light in self.indices_node_light:
            indices_node_near_light = self.get_neighbors(index_node_light, n=2)
            for j_node in indices_node_near_light:
                self.nodes_visible[j_node] = True
