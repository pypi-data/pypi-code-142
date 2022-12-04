
    

from tensorlearn.decomposition import tensor_train
from tensorlearn.decomposition import candecomp_parafac
from tensorlearn.operations import tensor_operations as top
from tensorlearn.operations import matrix_operations as mop


############################################################
############################################################
#####               decompositions
def auto_rank_tt(tensor,epsilon):
    return tensor_train.auto_rank_tt(tensor,epsilon)
    
def cp_als_rand_init(tensor, rank, iteration, random_seed=None):
    return candecomp_parafac.cp_als_rand_init(tensor, rank, iteration, random_seed)
    
############################################################
############################################################
####               tensor operations

#### TT
def tt_to_tensor(factors):
    return top.tt_to_tensor(factors)
        
def tt_compression_ratio(factors):
    return top.tt_compression_ratio(factors)
## General
def tensor_resize(tensor, new_shape):
    return top.tensor_resize(tensor,new_shape)
    
def tensor_frobenius_norm(tensor):
    return top.tensor_frobenius_norm(tensor)
    
def unfold(tensor):
    return top.unfold(tensor)

### CP

def cp_to_tensor(weights, factors):
    return top.cp_to_tensor(weights, factors)
    
def cp_compression_ratio(weights, factors):
    return top.cp_compression_ratio(weights,factors)

############################################################
############################################################
######              matrix operations

def error_truncated_svd(x, error):
    return mop.error_truncated_svd(x,error)

def column_wise_kronecker(a,b):
    return mop.column_wise_kronecker(a,b)



    







