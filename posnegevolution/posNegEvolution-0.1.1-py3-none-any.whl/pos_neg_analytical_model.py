import numpy as np
import math
import itertools
import scipy as sc
import copy
from threading import Thread
from multiprocessing import Pool

def mib(p,n,pe,ne):
    return ((1+pe)**p)/((1-ne)**n)

def calc(mut_prob, mut_effect, iPop, i, j, mdt, tau):
    A = mut_prob[0]*mib(iPop[0, j], iPop[i-1, 0], mut_effect[0], mut_effect[1])*iPop[i-1,j]*(i-1!=0)*(iPop[i-1,j]>=1)
    B = mut_prob[1]*mib(iPop[0, j-1], iPop[i, 0], mut_effect[0], mut_effect[1])*iPop[i,j-1]*(j-1!=0)*(iPop[i,j-1]>=1)
    C = (1-mut_prob[0]-mut_prob[1])*mib(iPop[0, j], iPop[i, 0], mut_effect[0], mut_effect[1])*iPop[i,j]*(iPop[i,j]>=1)
    D = mdt*iPop[i,j]*(iPop[i,j]>=1)
    return (A + B + C - D)*tau

def posNegAnalyticalModel(iPop, cap, tau, mut_prob, mut_effect, resume, lmbd, threads):
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
    if iPop[1:iPop._shape[0], [iPop._shape[1]-1]].sum() > 0:
        iPop._shape = (iPop._shape[0], iPop._shape[1]+1)
        iPop[0,iPop._shape[1]-1] = iPop[0,iPop._shape[1]-2] + 1
    if iPop[[iPop._shape[0]-1], 1:iPop._shape[1]].sum() > 0:
        iPop = sc.sparse.vstack([iPop, sc.sparse.csr_matrix(np.zeros(iPop._shape[1]))]).tocsr()
        iPop[iPop._shape[0]-1,0] = iPop[iPop._shape[0]-2,0] + 1
    
    x = iPop._shape[0]
    y = iPop._shape[1]
    
    popSize = iPop[1:x,1:y].sum()
    mdt = popSize/cap
    
    nPop = sc.sparse.csr_array((iPop._shape[0], iPop._shape[1]))
    
    for i in range(1,x):
        for j in range(1,y):
            nPop[i,j] = calc(mut_prob, mut_effect, iPop, i, j, mdt, tau)

    return nPop + iPop