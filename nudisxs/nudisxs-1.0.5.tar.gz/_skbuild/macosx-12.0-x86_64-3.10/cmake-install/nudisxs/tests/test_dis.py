from nudisxs.disxs import *
import numpy as np
import matplotlib.pyplot as plt

def finetine_plt()-> None:
    plt.rcParams['figure.figsize'] = (8, 6)
    plt.rcParams['font.size'] = 12
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['savefig.dpi'] = 300

def x_plot(enu,x,y,results)-> None:
    finetine_plt()
    (ne,ny,nx) = results.shape
    fig, axs = plt.subplots(ne, 1, sharex=True)
    # Remove vertical space between axes
    fig.subplots_adjust(hspace=0)

    for ie, ee in enumerate(enu):
        axs[ie].text(0.7,0.8,r"$\bf{E_\nu=}$"+f"{ee} GeV", weight="bold",transform=axs[ie].transAxes,fontsize=10)
        for iy, yy in enumerate(y):
            axs[ie].plot(x,results[ie,iy]/ee,label="y={0}".format(yy))
        if ie == 0:
            leg = axs[ie].legend(loc="upper left", bbox_to_anchor=[0, 1.4],
                             ncol=1, shadow=True,  fancybox=True)
    fig.supxlabel('x Bjorken', weight="bold")
    fig.supylabel(r'$\bf{\frac{1}{E_\nu}\frac{d^2\sigma}{dxdy}}$')
    plt.savefig('xs_vs_x.pdf')

def y_plot(enu,x,y,results)-> None:
    finetine_plt()
    (ne,ny,nx) = results.shape
    fig, axs = plt.subplots(nx, ne, figsize=(16, 10))
    # Remove vertical space between axes
#    fig.subplots_adjust(hspace=0)

    for ie, ee in enumerate(enu):
        for ix, xx in enumerate(x):
            if ix == 0:
                axs[ix,ie].text(0.4,1.05,r"$\bf{E_\nu=}$"+f"{ee} GeV", weight='bold',transform=axs[ix,ie].transAxes,fontsize=12)
            axs[ix,ie].plot(y,results[ie,:,ix]/ee,label="x={0}".format(xx))
            if ie== len(enu)-1:
                axs[ix,ie].text(1.05, 0.1, r'$\bf{x=}$'+f'{xx}',weight='bold',rotation=90,transform=axs[ix,ie].transAxes,fontsize=10)
#        if ie == 0:
#            leg = axs[ie].legend(loc="upper left", bbox_to_anchor=[0, 1.4],
#                             ncol=1, shadow=True,  fancybox=True)
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()
    fig.supxlabel('y Bjorken', weight="bold")
    fig.supylabel(r'$\bf{\frac{1}{E_\nu}\frac{d^2\sigma}{dxdy}}$')
    plt.savefig('xs_vs_y.pdf')

dis = disxs()
enu = np.array([10.,30.,100.])
x = np.linspace(0,1,100)
y = np.array([0.1,0.5,0.9])
results = dis.xs_cc_as_array(enu,x,y)
x_plot(enu,x,y,results)

x = np.array([0.015,0.045,0.08,0.125,0.175,0.225,0.3,0.5,0.6,0.7])
y = np.linspace(0,1,100)
results = dis.xs_cc_as_array(enu,x,y)
y_plot(enu,x,y,results)
