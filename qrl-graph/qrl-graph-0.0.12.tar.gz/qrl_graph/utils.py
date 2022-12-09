import numpy as np
import random
import wandb
# the utils function 


##### utils function to construct the graph #####
# graph construction (glued tree)
def contruct_tree_graph(h):
    """contruct the graph for the balanced binary tree with height of h.

    Args:
        h (int): the height of the tree
        
    Returns:
        g (np.array): the graph of the tree
        list_child (list): the index of last layers of the tree
    """
    g = np.zeros((2**h-1, 2**h-1))
    index = 0
    list_parent = []
    list_parent.append(index)
    for _ in range(h-1):
        list_child = []
        for parent in list_parent:
            g[parent, index+1] = 1
            g[parent, index+2] = 1
            list_child.append(index+1)
            list_child.append(index+2)
            index += 2
        list_parent = list_child
    
    g = g + g.T
    return g, list_child

def generate_two_cycles(n):
    """construct the two cycles between the two list of length n.
    
    Args:
        n (int): the length of the two cycles.
        
    Returns:
        list_first_perm (list): the permutation of the first cycles.
        list_second_perm (list): the permutation of the second cycles.
    """

    list_first_perm = list(np.random.permutation(n))
    list_second_perm = []

    list_available = list(range(n))


    # the last element of the first perm must be in the entries before
    index_for_last = random.choice(range(n-1))
    list_available.remove(list_first_perm[-1])

    for i in range(n):
        if i == index_for_last:
            list_second_perm.append(list_first_perm[-1])
        else: 
            # one restriction (can not repeat the first cycle)
            list_available_i = [a for a in list_available if a != list_first_perm[i]]
            index = random.choice(list_available_i)
            list_available.remove(index)
            list_second_perm.append(index)

    return list_first_perm, list_second_perm

def construct_glued_tree_graph(h):
    """contruct the graph for the balanced binary tree with height of h.

    Args:
        h (int): the height of the tree
    """
    n = 2**h-1

    # number of layer double! 
    g = np.zeros((2*n, 2*n))
    g_tree, list_nodes_left = contruct_tree_graph(h)
    
    # reflection (last layer)
    list_nodes_right = [ 2*n-1-i for i in list_nodes_left]
    
    for i in range(n):
        for j in range(n):
            g[i, j] = g_tree[i, j]
            # reflection (binary tree)
            g[2*n-1-i, 2*n-1-j] = g_tree[i, j]
        
    # build the random connection between the two last nodes of the trees. 
    list_perms = generate_two_cycles(len(list_nodes_left))
    
    for perm in list_perms:
        for i, j in enumerate(perm):
            g[list_nodes_left[i], list_nodes_right[j]] = 1
            g[list_nodes_right[j], list_nodes_left[i]] = 1
    
    return g

def construct_linear_graph(n):
    """Construct the linear graph with n nodes.
    
    Args:
        n (int): the number of nodes.
    
    Returns:
        g (np.array): the graph of the linear graph.
    """
    g = np.zeros((n, n))
    for i in range(n-1):
        g[i,i+1] = 1
    g = g + g.T
    return g

def construct_actual_fully_connected_graph(n):
    """Construct the actual fully connected graph with n nodes.
    
    Args:
        n (int): the number of nodes.
    
    Returns:
        g (np.array): the graph of the linear graph.
    """
    g = np.ones((n, n))
    for i in range(n):
        g[i,i] = 0
    return g

def construct_fully_connected_graph(n):
    """Construct the fully connected graph with n nodes.
    
    Args:
        n (int): the number of nodes.
    
    Returns:
        g (np.array): the graph of the linear graph.
    """
    g = np.ones((n, n))
    for i in range(n):
        g[i,i] = 0
    g[0, n-1] = 0
    g[n-1, 0] = 0
    return g

##### utils function for the general graph #####
# general graph utils
def is_graph_connected(g):
    """Here g is an array of length (n-1)n/2, where n is the number of vertices.
    
    Try to find a path from the beginning point to the end point.
    
    Args: g (np.array): an array of length (n-1)n/2, where n is the number of vertices.
    """
    n = int(np.sqrt(2*g.shape[0]+0.25)+0.5)
    g_list_index = []
    for i in range(n-1):
        g0, g = g[:n-1-i], g[n-1-i:]
        index_set = np.where(g0 == 1)[0] + i + 1
        g_list_index.append(index_set)
    
    visited = []
    def dfs(i):
        if i == n-1:
            return True
        for j in g_list_index[i]:
            if j not in visited:
                visited.append(j)
                if dfs(j):
                    return True
                visited.pop()
        return False
    return dfs(0)

def is_start_end_connected(g):
    """Detect whether the start and end vertices are connected.
    
    Args: g (np.array): an array of length (n-1)n/2, where n is the number of vertices.
    """
    n = int(np.sqrt(2*g.shape[0]+0.25)+0.5)
    return g[n-2] == 1

def is_graph_valid(g):
    return is_graph_connected(g) and not is_start_end_connected(g)

def get_index(i, j, n):
    """i is the row index, j is the column index, n is the number of vertices."""
    assert j > i
    return int( (2 * n - 1 - i) * i // 2+ j - i -1 )

def g2adjacent_mat(g):
    """convert from the graph to the adjacent matrix.
    
    The graph is represented by an array of length (n-1)n/2, where n is the number of vertices.
    """
    if isinstance(g, list) or isinstance(g, tuple):
        g = np.array(g)
    n = int(np.sqrt(2*g.shape[0]+0.25)+0.5)
    graph = np.zeros((n, n), dtype=int)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            graph[i, j] = graph[j, i] = g[count]
            count += 1
    assert count == g.shape[0]
    return graph

def adjacent_mat2g(graph):
    """Convert from the adjacent matrix to the graph.
    
    The graph is represented by an array of length (n-1)n/2, where n is the number of vertices.
    """
    n = graph.shape[0]
    g = np.zeros(n * (n-1) // 2, dtype=int)
    
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            g[count] = graph[i, j]
            count += 1
    assert count == g.shape[0]
    return g


### utils for the special optimization ### 
def _burnin_modify(data, t_list):
    """modify the data to remove the burnin time
    
    1. remove the negative values
    2. start after the peak
    """
    last_negative = -1
    for i, value in enumerate(data): 
        if value < 0: 
            last_negative = i
    data = data[last_negative + 1: ]
    t_list = t_list[last_negative + 1: ]        
    max_index = np.argmax(data)
    return data[max_index:], t_list[max_index:]

def _postive_filter(data, t_list):
    """modify the data to remove the negative values

    1. remove the negative values
    """
    new_data_list = []
    new_t_list = []
    for value, t in zip(data, t_list): 
        if value > 0:
            new_data_list.append(value)
            new_t_list.append(t)
    return new_data_list, new_t_list

# numbers 
def array2binary(array):
    """Convert the array to binary.
    
    Args:
        array: the array to be converted.
    
    Returns:
        int: the binary representation of the array.
    """
    return int(''.join(map(lambda x: str(int(x)), array)), 2)

### logger
def setup_wandb(config, project_name):
    wandb.init(
            reinit=True,
            config=config,
            project=project_name,
            settings=wandb.Settings(
                start_method="thread",
                _disable_stats=True,
            ),
        )
    