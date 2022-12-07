import sys

from ntsim.Primary import *
from ntsim.utils.Particles import Particles
from ntsim.utils.report_timing import report_timing
from ntsim.utils import gen_utils

class ToyPrimary(Primary):
    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('ToyPrimary')
        self.primary_propagator = {}

    def configure(self, opts):
        # it will generate primaries and propagate them in the same module
        self.configure_generator(opts)
        self.configure_propagators(opts)
        self.photon_suppression = opts.photon_suppression
        self.log.info('configured')

    @report_timing
    def next(self, thread_id=0):
        self.clear_data()
        # Particle transport -> photons
        input_particles = self.primary_generator.next()
        pprop = self.primary_propagator['particlePropagator']
        particles, tracks, photons_dict = pprop.propagate(input_particles)
        self.add_particles(particles)
        self.add_tracks(tracks)
        #
        # Photon transport -> Get hits
        for label, photons in photons_dict.items():
            hits = self.primary_propagator['mcPhotonTransporter'].transport(
                                                                      photons,
                                                                      self.medium.get_model(photons),
                                                                      self.geometry)
            self.add_hits(hits)
            self.log.info(f"  {label:<36}: {len(np.unique(hits[:,0]))} OMs fired")
            self.log.info(f"  {label:<36}: {hits.shape[0]} hits detected")
            self.add_photons(photons, label)
        self.write_data()
        #

    def next_multithread(self, n, jobs=0):
#        self.next()
        from multiprocessing.pool import ThreadPool
        from multiprocessing import cpu_count
        if jobs == 0:
            jobs = cpu_count()
        t = ThreadPool(processes=jobs)
        t.map(self.next, range(1,n))
        t.close()
