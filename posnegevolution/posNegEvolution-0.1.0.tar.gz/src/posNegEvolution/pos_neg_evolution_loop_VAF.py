import numpy as np
import math
import itertools
import scipy as sc
import copy
from threading import Thread
from multiprocessing import Pool

def death(iPop, pdt):
    return iPop[pdt,:]
  
def divide(iPop, pdv):
    return sc.sparse.vstack([iPop, copy.deepcopy(iPop[pdv,:])]).tocsr()
 
#TODO merge mutation into one   
def mutate_n(iPop, pdm, mut_effect):
    cells = len(pdm)
    if cells == 0:
        return iPop
    (a,b) = iPop._shape
    rows = copy.deepcopy(iPop[pdm,:]).toarray()
    rows[:,0] = rows[:,0]/(1-mut_effect[1])
    iPop = sc.sparse.vstack([iPop, rows]).tocsr()
    iPop._shape = (iPop._shape[0], iPop._shape[1] + cells)
    (c,d) = iPop._shape
    iPop[range(a,c,1), range(b,d,1)] = -1
    # for i in range(a,c):
    #     iPop[i, 0] = iPop[i, 0]/(1-mut_effect[1])
    return iPop
    
def mutate_p(iPop, pdm, mut_effect):
    cells = len(pdm)
    if cells == 0:
        return iPop
    (a,b) = iPop._shape
    rows = copy.deepcopy(iPop[pdm,:]).toarray()
    rows[:,0] = rows[:,0]*(1+mut_effect[0])
    iPop = sc.sparse.vstack([iPop, rows]).tocsr()
    iPop._shape = (iPop._shape[0], iPop._shape[1] + cells)
    (c,d) = iPop._shape
    iPop[range(a,c,1), range(b,d,1)] = 1  
    # for i in range(a,c):
    #     iPop[i, 0] = iPop[i, 0]*(1+mut_effect[0])
    return iPop

# def mutate(iPop, p, n, mut_effect):
#     if len([p, d])

def deleteZeroColumn(iPop):
    mask = np.ones(iPop._shape[1], dtype=bool)
    for i in range(iPop._shape[1]):
        _sum = (iPop[:,i]).count_nonzero()
        if _sum == 0:
            mask[i] = False
    return iPop[:,mask]

def posNegEvolutionLoopVAF(iPop, cap, tau, mut_prob, mut_effect, resume, lmbd, threads, clear):
    """    
    Description:
        One cycle to update population - tau loop iteration method
        Prameters:
            iPop: population matrix 
                One row represents one cell
                Fitness, [Mutations] (in not VAF apprach mutation number (pos and neg))
            cap: population capacity
            tau: tau step
            mut_prob: list in form of: [driver mutation probability, passenger mutation probability]
            mut_effect: list in form of: [driver mutation effect, passenger muatation effect]
            resume: acknowledge to resume simulation !!TODO!!
            q: common queue
            THREADS: threads number used in simulation !!TODO!!            
    """
    popSize = iPop._shape[0]
    
    mdt = popSize/cap
    mdv = iPop[:,0].toarray()[:,0]
    
    pdt = np.random.exponential(1, popSize)/mdt
    pdv = np.random.exponential(1, popSize)/mdv
    
    pdt = pdt > tau
    pdv = pdv < tau
    
    pdv = pdv & pdt
    # pdm_n = pdm_n & pdv
    # pdm_p = pdm_p & pdv
    # pdv[pdm_n] = False
    # pdv[pdm_p] = False
    
    nr = np.array(range(popSize))
    pdv = nr[pdv]
    pdt = nr[pdt]
    
    pdm_p = np.random.binomial(1, mut_prob[0], len(pdv))
    pdm_n = np.random.binomial(1, mut_prob[1], len(pdv))
    pdm_n = pdm_n > np.zeros(len(pdv))
    pdm_p = pdm_p > np.zeros(len(pdv))
    
    pdv_t = pdv[~pdm_n & ~pdm_p]
    
    pdm_p = pdv[pdm_p]
    pdm_n = pdv[pdm_n]
    pdv = pdv_t
    
    iPop = divide(iPop, pdv)
    
    # iPop = mutate(iPop, pdm_p, pdm_n, mut_effect)
    
    iPop = mutate_p(iPop, pdm_p, mut_effect)
    
    iPop = mutate_n(iPop, pdm_n, mut_effect) 
    
    pdt = np.append(pdt, range(max(pdt)+1, iPop._shape[0]))
    iPop = death(iPop, pdt)
    
    if clear:
        iPop = deleteZeroColumn(iPop)
        clear = False
    
    return iPop