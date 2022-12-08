import numpy as np
import time
import math
import scipy as sc
import pandas as pd
from pathlib import Path  
from threading import Thread

from posNegEvolution.pos_neg_evolution_loop import posNegEvolutionLoop as PNEL
from posNegEvolution.pos_neg_evolution_loop_VAF import posNegEvolutionLoopVAF as PNELV
from posNegEvolution.pos_neg_analytical_model import posNegAnalyticalModel as PNAM

end = False

def saveToFile(df, file_localization, file_name, iter_outer):    
    sc.sparse.save_npz(file_localization + "\\" + file_name + "_" + str(iter_outer), df)

def mutationWavePlot(iMuts, iClones=None, cln=0, name="", local="", f_num=0, ret=0):
    print("inavaliable, TODO")

def fitnessWavePlot(iProp, iClones=None, cln=0, name="", local="", f_num=0):
    print("inavaliable, TODO")

def corrPlot(iPop, select):
    mutWave = []
    if select == 0:
        mutWave = iPop[:, [1,2]].toarray().T
    elif select == 1:
        mutWave = np.zeros([iPop._shape[0], 2])
        t = iPop[:, 1:iPop._shape[1]].toarray()
        for i in range(iPop._shape[0]):
            a = t[i, :]
            mutWave[i,0] = sum(a[a>0])
            mutWave[i,1] = abs(sum(a[a<0]))
        mutWave = mutWave.T
    return mutWave

def commands(q, ID, iPop, file_localization, file_name, iter_outer, skip, iter_inner, cycle, tau, select):
    global end
    queue_data = q.get()
    if(queue_data[0] == '1' and queue_data[1] == str(ID)):
        if(queue_data[2] == "exit"):
            print("exit")
            end = True
        elif(queue_data[2] == "size" and select != 2):
            q.put(['0', str(ID), str(iPop._shape[0])])
        elif(queue_data[2] == "size" and select == 2):
            q.put(['0', str(ID), str(iPop[0].sum())])
        elif(queue_data[2] == "time"):
            q.put(['0', str(ID), str((iter_outer-1)*skip + (iter_inner%cycle)*tau)])
        elif(queue_data[2] == "save"):
            if file_localization == "" or file_name == "":
                q.put(['0', str(ID), "unable to save file"])
            else:
                saveToFile(iPop, file_localization, file_name, iter_outer)
        elif(queue_data[2] == "corr_plot" and select != 3):        
            q.put(['-1', str(ID), corrPlot(iPop, select)])
        elif(queue_data[2] == "mut_wave"):
            print("TODO")
    else:
        q.put(queue_data)
 
    
def plotter(iPop, file_name, file_localization, iter_outer, plots, select):
    if plots & 1:
        print("TODO")
    if plots & 2:
        print("TODO")
    if plots & 16: 
        saveToFile(iPop, file_localization, file_name, iter_outer)
    
def posNegEvolutionMainLoop(iPop, params, file_name="", file_description="", file_localization="", plots=0, t_iter=0, q=None, ID=0, select=0, break_type=1):
    global end
    """
    Main simulation loop
        iPop: population matrix 
            One row represents one cell
            Fitness, [Mutations] (in not VAF apprach mutation number (pos and neg))
        [initial population size, population capacity, simulation steps number, tau step [s], one cycle time [s], 
         mutation probability (list) adequate index for mutation effect, mutation effect (list), mutations intesity, number of threads]
        file_name: save file name, data will be saved to file_name.csv, figures: file_name_typeofplot.jpg
        file_localization: path to file, figures will be saved in path: file_localization/Figures/Cycle_number
        plots: binary interpreted value defines which plots will be generated: 
            1 - mutation wave
            2 - fitness wave
            16 - ack to save data
        t_iter - value of starting iteration (for resume t_iter != 0)
        q - queue to comunicate with simulation in thread
        ID - simulation ID
        select - 0 normal, 1 binned
    """
    cap = params[1]
    steps = params[2]
    tau = params[3]
    skip = params[4]
    mut_effect = params[6]
    mut_prob = params[5]
    lmbd = params[7]
    threads = params[8]

    iter_inner = 0 + 1*(t_iter>0)
    begin = 0 + 1*(t_iter==0)
    iter_outer = t_iter
    resume = 0 + 1*(t_iter>0)
    cycle = round(skip/tau)
    
    t = time.time()
    clear = False
    
    while 1:   
        if q != None:
            if not q.empty():
                commands(q, ID, iPop, file_localization, file_name, iter_outer, skip, iter_inner, cycle, tau, select)

        if end:
            break

        if iter_inner % cycle == 0 or begin:
            begin = 0
            t = time.time() - t  
            print(str(ID) + ':' + str(t))
            
            plotter(iPop, file_name, file_localization, iter_outer, plots, select)

            iter_outer = iter_outer + 1   
            clear = True
            t = time.time()
        
        if iter_outer % steps == 0 and break_type == 1:
            print('all steps')
            break
        elif len(iPop) >= steps and break_type == 0 and select != 2:
            print('all cells')
            break
        
        if select == 0:            
            iPop = PNEL(iPop, cap, tau, mut_prob, mut_effect, resume, lmbd)
        elif select == 1:            
            iPop = PNELV(iPop, cap, tau, mut_prob, mut_effect, resume, lmbd, threads, clear)
        elif select == 2:            
            iPop = PNAM(iPop, cap, tau, mut_prob, mut_effect, resume, lmbd, threads)
        
        resume = 0
        iter_inner = iter_inner + 1
             