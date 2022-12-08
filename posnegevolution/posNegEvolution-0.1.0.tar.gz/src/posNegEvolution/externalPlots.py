import scipy as sc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sys
import os

def readPaths(file_path):
    path = file_path.split("/")
    out = ""
    name = ""
    number = ""
    
    for i in path:
        if i.endswith(".npz"):
            i = i.split('_')
            for x in i:
                if x.endswith(".npz"):
                    number = x.rstrip(".npz")
                else:
                    name = name + x + '_'
            name.lstrip('_')
        else:
            out = out + i + '/'
    out = out + "Figures/" + number + "/"
    return [file_path, out, name, number]

def VAFplot(file_path):
    _in, _out, _name, _num = readPaths(file_path)
    
    pop = sc.sparse.load_npz(_in)
    
    popSize = pop._shape[0]
    mutLen = pop._shape[1]
    muts = np.zeros(mutLen - 1)
    
    for i in range(1, mutLen):
        muts[i-1] = pop[:,i].sum()/popSize
    
    muts = muts[np.argsort(np.absolute(muts))]
    
    t_freq = [x/200 for x in range(0,201)]
    freq = np.zeros([3,len(t_freq)])
    freq[2,:] = np.array(t_freq)
    
    idx = 1
    for i in muts:
        while abs(i) > t_freq[2*idx]:
            idx = idx + 1
            if idx == 101:
                break
        else:
            if i < 0:
                freq[1,2*idx-1] = freq[1,2*idx-1] + 1
            else:
                freq[0,2*idx-1] = freq[0,2*idx-1] + 1
       
    df = pd.DataFrame(freq.T)
    df.columns = ["positive", "negative", "freq"]
    ax = df.plot.bar(x="freq", stacked=True, width=2, figsize=(40,20))
    ax.legend(prop={'size':30})
    
    ax.set_xlabel("VAF", labelpad=50, fontdict={'fontsize':50})
    ax.set_ylabel("Frequency", labelpad=50, fontdict={'fontsize':50})
    ax.set_title("Population VAF, Population: %i, Mutations: %i" % (popSize, mutLen), pad=50, fontdict={'fontsize':70})
    ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(40) 
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(40) 
    fig = ax.get_figure()
    
    try:
        os.makedirs(_out, exist_ok=True) 
    except OSError as error:
        print(error)
    finally:
        if os.path.exists(_out + "%s_VAF_plot.jpg" % _num):
            os.remove(_out + "%s_VAF_plot.jpg" % _num)
        fig.savefig(_out + "%s_VAF_plot.jpg" % _num)
        plt.close(fig)            
    
def mutationWave(file_path):
    _in, _out, _name, _num = readPaths(file_path)
    
    pop = sc.sparse.load_npz(_in)
    
    popSize = pop._shape[0]
    mutLen = pop._shape[1]
    cells = np.zeros(popSize)
    
    for i in range(0,popSize):
        cells[i] = pop[i,1:mutLen].count_nonzero()
        
    df = pd.DataFrame(cells)
    ax = df.plot.hist(figsize=(40,20))
    ax.legend(prop={'size':30})
    
    ax.set_xlabel("Mutation number", labelpad=50, fontdict={'fontsize':50})
    ax.set_ylabel("Cells", labelpad=50, fontdict={'fontsize':50})
    ax.set_title("Mutation Wave, Population: %i, Mutations: %i" % (popSize, mutLen), pad=50, fontdict={'fontsize':70})
    
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(40) 
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(40) 
    
    fig = ax.get_figure()
    
    try:
        os.makedirs(_out, exist_ok=True) 
    except OSError as error:
        print(error)
    finally:
        if os.path.exists(_out + "%s_mutation_wave.jpg" % _num):
            os.remove(_out + "%s_mutation_wave.jpg" % _num)
        fig.savefig(_out + "%s_mutation_wave.jpg" % _num)
        plt.close(fig)            
    
def fitnessWave(file_path):
    _in, _out, _name, _num = readPaths(file_path)
    
    pop = sc.sparse.load_npz(_in)
    
    popSize = pop._shape[0]
    mutLen = pop._shape[1]
    
    df = pd.DataFrame(pop[:,0].toarray())
    ax = df.plot.hist(figsize=(40,20))
    ax.legend(prop={'size':30})
    
    ax.set_xlabel("Fitness", labelpad=50, fontdict={'fontsize':50})
    ax.set_ylabel("Cells", labelpad=50, fontdict={'fontsize':50})
    ax.set_title("Fitness Wave, Population: %i, Mutations: %i" % (popSize, mutLen), pad=50, fontdict={'fontsize':70})
    
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(40) 
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(40) 
    
    fig = ax.get_figure()    
    
    try:
        os.makedirs(_out, exist_ok=True) 
    except OSError as error:
        print(error)
    finally:
        if os.path.exists(_out + "%s_fitness_wave.jpg" % _num):
            os.remove(_out + "%s_fitness_wave.jpg" % _num)
        fig.savefig(_out + "%s_fitness_wave.jpg" % _num)
        plt.close(fig)            
    
if __name__ == "__main__":
    VAFplot("E:/Simulations/Pos Neg Evolution/to_prez/tp_852.npz")
    mutationWave("E:/Simulations/Pos Neg Evolution/to_prez/tp_852.npz")
    fitnessWave("E:/Simulations/Pos Neg Evolution/to_prez/tp_852.npz")