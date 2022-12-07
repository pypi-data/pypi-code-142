from ntsim.Primary import *
from ntsim.utils.report_timing import report_timing
from ntsim.utils.Particles import Particles

class Neutrino(Primary):
    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('NeutrinoPrimary')
        self.primary_propagator = {}

    def configure(self,opts):
        self.configure_generator(opts)
        self.configure_propagators(opts)

    def next(self):
        self.clear_data()
        #
        input_particles = Particles(number_of_particles=2)
        primaries = self.primary_generator.next()
        self.log.info('generated particles:')
        for p in primaries:
            input_particles.add_particle(pdgid=p[0], x_m=-100, y_m=-200, z_m=120, t_ns=0, 
                                         Px_GeV=p[1], Py_GeV=p[2], Pz_GeV=p[3], Etot_GeV=p[4])
        self.log.info(input_particles.print())
        #
        # Particle transport -> get photons (not transported!)
        pprop = self.primary_propagator['particlePropagator']
        particles, tracks, photons_dict = pprop.propagate(input_particles)
        self.add_particles(particles)
        self.add_tracks(tracks)
        #
        # Photon transport -> get hits

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
