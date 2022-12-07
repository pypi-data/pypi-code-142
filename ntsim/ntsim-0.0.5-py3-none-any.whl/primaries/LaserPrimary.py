from ntsim.Primary import *

class LaserPrimary(Primary):
    import numpy as np

    def configure(self,opts):
        self.primary_name = 'Laser'
        self.configure_generator(opts)
        track = np.array(self.primary_generator.position)
        self.primary_track = track.reshape(track.shape[0],1)
        self.configure_propagators(opts)
        log.info('configured')

    def next(self):
        self.clear_data()
        primaries = self.primary_generator.next()
        while True:
            try:
                photons = next(primaries)
                hits = self.primary_propagator['mcPhotonTransporter'].transport(photons,
                                                                                self.medium.get_model(photons),
                                                                                self.geometry)
                self.add_photons(photons)
                self.add_hits(hits)
            except StopIteration:
                break
        self.write_data()

    def get_photons_sampling_weight(self):
        return 1.

    def get_vertices(self):
        return []
