import numpy as np
from numba import njit


# convert bnlearn format to my format
def from_bnlearn(dag):
    dag = dag[1: len(dag) - 1]
    output = {}
    for node in dag.split(']['):
        if '|' not in node:
            output[node] = {'par': [], 'nei': []}
        else:
            output[node.split('|')[0]] = {'par': node.split('|')[1].split(':'), 'nei': []}
    return output


def score(dag, data, score_function='bic'):
    if type(dag) is str:
        dag = from_bnlearn(dag)
    elif type(dag) is not dict:
        raise Exception('The format of input true DAG is invalid.')
    varnames = list(data)
    if all(data[var].dtype.name == 'category' for var in data):
        data = data.apply(lambda x: x.cat.codes).to_numpy()
    elif all(data[var].dtype.name != 'category' for var in data):
        data = data.to_numpy()
    else:
        raise Exception('Mixed data is not supported.')

    sco = 0
    for var in varnames:
        cols = [varnames.index(v) for v in [var] + dag[var]['par']]
        sco += local_score(data, cols, score_function)
    return sco


def bic(data, cols, weight=None):
    arities = np.amax(data, axis=0) + 1
    return bic_counter(data, arities, cols, weight)


@njit(fastmath=True)
def bic_counter(data, arities, cols, weight=None):
    if weight is None:
        weight = np.ones(data.shape[0])
    strides = np.empty(len(cols), dtype=np.uint32)
    idx = len(cols) - 1
    stride = 1
    while idx > -1:
        strides[idx] = stride
        stride *= arities[cols[idx]]
        idx -= 1
    N_ijk = np.zeros(stride)
    N_ij = np.zeros(stride)
    for rowidx in range(data.shape[0]):
        idx_ijk = 0
        idx_ij = 0
        for i in range(len(cols)):
            idx_ijk += data[rowidx, cols[i]] * strides[i]
            if i != 0:
                idx_ij += data[rowidx, cols[i]] * strides[i]
        N_ijk[idx_ijk] += weight[rowidx]
        for i in range(arities[cols[0]]):
            N_ij[idx_ij + i * strides[0]] += weight[rowidx]
    bic = 0
    for i in range(stride):
        if N_ijk[i] != 0:
            bic += N_ijk[i] * np.log(N_ijk[i] / N_ij[i])
    bic -= 0.5 * np.log(data.shape[0]) * (arities[cols[0]] - 1) * strides[0]
    return bic


def bic_g(data, cols, weights=None):
    X = data[:, cols[1:]]
    y = data[:, cols[0]]
    X = np.hstack((np.ones(len(y)).reshape(len(y), 1), X))
    if len(y) <= X.shape[1] or np.linalg.det(X.T @ X) == 0:
        bic = np.nan
    else:
        b = np.linalg.inv(X.T @ X) @ X.T @ y
        ssr = np.sum((y - X @ b) ** 2)
        df = X.shape[0] - X.shape[1]
        bic = - X.shape[0] / 2 * np.log(2 * np.pi * ssr / df) - df / 2 - np.log(X.shape[0]) / 2 * (1 + X.shape[1])
    return bic


def local_score(data, cols, score_function='default', weights=None):
    '''
    :param weights: weight for data
    :param data: numbered version of data set
    :param cols: the index of node and its parents, the first element represents the index of the node and the following elements represent the indices of its parents
    :param score_function: name of score function, currently support bic, nal, bic_g
    :return: local score of node (cols[0]) given its parents (cols[1:])
    '''
    if len(data) == 0:
        return np.nan
    else:
        if score_function == 'default':
            score_function = 'bic' if 'int' in data.dtype.name else 'bic_g'
        try:
            ls = globals()[score_function](data, np.asarray(cols), weights)
        except Exception as e:
            raise Exception(
                'score function ' + score_function + ' is undefined or does not fit to data type. Available score functions are: bic (BIC for discrete variables) and bic_g (BIC for continuous variables).')
        return ls
