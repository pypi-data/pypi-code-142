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
    
def mutate_n(iPop, pdm, mut_effect):
    cells = len(pdm)
    if cells == 0:
        return iPop
    (a,b) = iPop._shape
    iPop = sc.sparse.vstack([iPop, copy.deepcopy(iPop[pdm,:])]).tocsr()
    (c,d) = iPop._shape
    for i in range(a,c):
        iPop[i, 0] = iPop[i, 0]/(1-mut_effect[1])
        iPop[i, 2] = iPop[i, 2]+1
    return iPop
    
def mutate_p(iPop, pdm, mut_effect):
    cells = len(pdm)
    if cells == 0:
        return iPop
    (a,b) = iPop._shape
    iPop = sc.sparse.vstack([iPop, copy.deepcopy(iPop[pdm,:])]).tocsr()
    (c,d) = iPop._shape
    for i in range(a,c):
        iPop[i, 0] = iPop[i, 0]*(1+mut_effect[0])
        iPop[i, 1] = iPop[i, 1]+1
    return iPop

def deleteZeroColumn(iPop):
    mask = np.ones(iPop._shape[1], dtype=bool)
    for i in range(iPop._shape[1]):
        _sum = (iPop[:,i]).count_nonzero()
        if _sum == 0:
            mask[i] = False
    return iPop[:,mask]

def posNegEvolutionLoop(iPop, cap, tau, mut_prob, mut_effect, resume, lmbd):
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
    pdv = np.random.exponential(1, popSize)
    pdm_p = np.random.binomial(1, mut_prob[0], popSize)
    pdm_n = np.random.binomial(1, mut_prob[1], popSize)
    
    pdt = pdt > tau
    pdv = pdv/mdv < tau
    pdm_n = pdm_n > np.zeros(popSize)
    pdm_p = pdm_p > np.zeros(popSize)
    
    pdv = pdv & pdt
    pdm_n = pdm_n & pdv
    pdm_p = pdm_p & pdv
    pdv[pdm_n] = False
    pdv[pdm_p] = False
    
    nr = np.array(range(popSize))
    pdv = nr[pdv]
    pdt = nr[pdt]
    pdm_p = nr[pdm_p]
    pdm_n = nr[pdm_n]
    
    iPop = divide(iPop, pdv)
    
    iPop = mutate_p(iPop, pdm_p, mut_effect)
    
    iPop = mutate_n(iPop, pdm_n, mut_effect) 
    
    pdt = np.append(pdt, range(max(pdt)+1, iPop._shape[0]))
    iPop = death(iPop, pdt)
    
    # iPop = deleteZeroColumn(iPop)
    
    return iPop