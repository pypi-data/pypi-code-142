import numpy as np
from nudisxs.disxs import *

import matplotlib.pyplot as plt

def finetine_plt()-> None:
    plt.rcParams['figure.figsize'] = (8, 6)
    plt.rcParams['font.size'] = 12
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['savefig.dpi'] = 300

def main():
    dis = disxs()
    dis.init_current('cc')
    enu = np.logspace(1,6,100)
    for ie,e in enumerate(enu):
        dis.dis_kinematics(e,0.1,0.2)
        print(dis.particles)

main()
