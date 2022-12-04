import vegas
import math
import numpy as np
from nudisxs.disxs import *

import matplotlib.pyplot as plt

def finetine_plt()-> None:
    plt.rcParams['figure.figsize'] = (8, 6)
    plt.rcParams['font.size'] = 12
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['savefig.dpi'] = 300

def plot_xsec_vs_enu(enu,xsec)->None:
    finetine_plt()
    fig, axs = plt.subplots(1, 1)
    plt.plot(enu,xsec)
    fig.supxlabel(r'$\bf{E_\nu}$, [GeV]', weight="bold")
    fig.supylabel(r'$\bf{\sigma}$')
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('xs_vs_enu.pdf')

np.random.seed((1,2, 3))   # causes reproducible random numbers

class cross_section(vegas.BatchIntegrand):
    def init(self, enu):
        self.enu = enu

    def __call__(self, x):
        f = np.zeros(x.shape[0])
        xs.d2sdiscc_dxdy_array(self.enu,x[:,0],x[:,1],f,x.shape[0])
        return f

def main():
    # create integrand
    dis = disxs()
#    f = cross_section()
#    integ = vegas.Integrator([[0.0,1.0], [0.0,1.0]], nhcube_batch=2000, sync_ran=False)
    enu = np.logspace(1,6,100)
    tot =  np.zeros_like(enu)
    for ie,e in enumerate(enu):
        tot[ie] = dis.calculate_total(e)
#        result = integ(f,  nitn=10)
#        tot[ie] = result.mean
#        print(result)
    plot_xsec_vs_enu(enu,tot)
main()
