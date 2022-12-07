import numpy as np
from mumpropagator import pymum
from ntsim.utils.report_timing import report_timing

import logging
log = logging.getLogger('MUMPropagator')

class MUMPropagator:
    def __init__(self):
        self.module_type = "propagator"
        self.propagator = pymum.mum()
        self.propagator.init() # TODO Check if propagator is initialized
        log.info("initialized")

    def configure(self, opts):
        log.info("configured")

    @report_timing
    def propagate(self, primaries):
        depth = 1e5 # FIXME should be till the muon surface (in cm)
        if primaries is None:
            log.warning("No primaries to propagate")
            return
        for i,event in enumerate(primaries['event']):
            e_ini = event['energy_mu']
            track = self.propagator.transport(e_ini,depth)
            e_fin = track[-1]['energy_out']
            log.debug(f'transport {e_ini} -> {e_fin}')
            yield track


    def propagate_multithread(self, primaries, jobs=0):
        from multiprocessing.pool import ThreadPool
        from multiprocessing import cpu_count
        if jobs == 0:
            jobs = cpu_count()
        if primaries is None:
            log.warning("No primaries to propagate")
            return
        t = ThreadPool(processes=jobs)
        log.debug("Propagate multithread start")
        t.map(self.propagate, primaries)
        t.close()
        log.debug("Propagate multithread done")
