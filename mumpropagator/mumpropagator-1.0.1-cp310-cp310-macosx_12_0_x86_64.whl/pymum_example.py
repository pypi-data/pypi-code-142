from hepunits.units import GeV, MeV, eV, km, cm, mm
import numpy as np
import os
import sys
from time import time
from argparse import Namespace
coloredlogs=None
import logging
logging.addLevelName(5, 'DEEPDEBUG')
log=logging.getLogger('test_rte')

sys.path.insert(1, os.path.join(sys.path[0], '..'))

def create_output(opts: Namespace) -> None:
    import os
    if not os.path.exists(opts.output):
        print(f'create {opts.output}')
        os.makedirs(opts.output)

def plot_total_eloss(energy_loss,plt) -> None:
    plt.hist(energy_loss,bins='auto')
    plt.xlabel('energy loss, [GeV]')
    plt.ylabel('entries')
    plt.savefig(opts.output+'/total_eloss.png')

def transport(opts: Namespace) -> None:
    from mumpropagator.pymum import mum
    m = mum()
    m.init(ilep=opts.type)
    energy = opts.energy*GeV
    depth  = opts.depth*km
    n = opts.n

    total_eloss = np.zeros(n,dtype=float)
    tic = time()
    for i in range(n):
        track = m.transport(energy/GeV,depth/cm)
        total_eloss[i] = track[0]['energy_in'] - track[-1]['energy_out']
    toc = time()
    print(f"{toc-tic:6.3E}s")

    if opts.savefig:
        create_output(opts)
        import matplotlib.pyplot as plt
        plt.rcParams['figure.figsize'] = (8, 6)
        plt.rcParams['font.size'] = 12
        plt.rcParams['lines.linewidth'] = 2
        plt.rcParams['axes.labelsize'] = 14
        plt.rcParams['savefig.dpi'] = 300
        plot_total_eloss(total_eloss,plt)


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--energy', default=1e3, type=float, help='particle energy in GeV')
    parser.add_argument('--depth', default=1e0, type=float, help='depth to travel in km')
    parser.add_argument('--n', default=1000, type=int, help='number of particles to propagate')
    parser.add_argument('--type', default=1, type=int, help='particle type')
    parser.add_argument('--savefig', default=True, type=bool, help='save figures')
    parser.add_argument('-o', '--output', default='figures', help='output path')
    parser.add_argument('-l', '--log-level', choices=('deepdebug', 'debug', 'info', 'warning'), default='INFO', help='logging level')

    opts = parser.parse_args()


    logformat='%(levelname)-10s │ %(message)s'
    if coloredlogs:
        coloredlogs.install(fmt=logformat, level=opts.log_level.upper(), logger=log)
    else:
        logging.basicConfig(format=logformat)
        log.setLevel(logging.getLevelName(opts.log_level.upper()))
    transport(opts)
else:
    from types import SimpleNamespace
    opts = SimpleNamespace()
    opts.energy = 1e3
    opts.depth = 1e0
    opts.n=1000
    opts.type = 1
    opts.savefig = True
    opts.output = 'figures'
    opts.log_level = 'INFO'
