import numpy as np

from ntsim.Primary import Primary
from ntsim.primaryGenerators.ChargedTrack import ChargedTrack

import logging
log = logging.getLogger('Charged_Track_Primary')
logformat='[%(name)20s ] %(levelname)8s: %(message)s'
logging.basicConfig(format=logformat)

class ChargedPrimary(Primary):

    def configure(self, opts):
        self.primary_name = 'ChargedTrack'
        self.configure_generator(opts)
        self.configure_propagators(opts)
        log.info('configured')

    def next(self):
        primaries = self.primary_generator.next()
        self.make_event_folder(self.gEvent.gProductionHeader.n_events)
        bunch = 0
        n_photons_total = 0
        while True:
            try:
                photons = next(primaries)
                hits = self.primary_propagator['mcPhotonTransporter'].transport(photons,self.medium.get_model(photons),self.geometry)
                self.write_photons_bunch(photons,bunch)
                self.add_hits(hits)
                bunch+=1
                n_photons_total += photons.n_tracks
            except StopIteration:
                break
        self.write_number_of_bunches(bunch,n_photons_total)
        self.write_hits()
        self.clear_hits()
        self.write_event_header()

    def get_photons_sampling_weight(self):
        return 1.

    def get_vertices(self):
        return []
