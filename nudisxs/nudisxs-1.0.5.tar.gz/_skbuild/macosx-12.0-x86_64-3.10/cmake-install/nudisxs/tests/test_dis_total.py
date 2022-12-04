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

def main():
    dis = disxs()
    dis.init_current('cc')
    enu = np.logspace(1,6,100)
    tot =  np.zeros_like(enu)
    for ie,e in enumerate(enu):
        tot[ie] = dis.calculate_total(e)
    plot_xsec_vs_enu(enu,tot)

main()
