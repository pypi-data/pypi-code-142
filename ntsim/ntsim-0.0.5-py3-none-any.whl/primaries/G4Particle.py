import sys

from ntsim.Primary import *
#from ntsim.primaryPropagators.cascadeCherenkov import cascadeCherenkov
#from ntsim.primaryPropagators.trackCherenkov import trackCherenkov
from ntsim.utils.report_timing import report_timing

class G4Particle(Primary):
    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('G4ParticlePrimary')
        self.primary_propagator = {}

    def configure(self, opts):
        # it will generate primaries and propagate them in the same module
        self.configure_propagators(opts, arg_dict={"g4propagator": [opts.g4_cherenkov]})
        self.log.info(f"primary propagators: {[key for key in self.primary_propagator.keys()]}")
        self.photon_suppression = opts.photon_suppression
        self.log.info('configured')

    @report_timing
    def next(self, thread_id=0):
        photons = {}  # keys: 'cascade', 'track'
        self.vertices = []
        self.tracks = []
        self.hits = []
        self.make_event_folder(self.gEvent.gProductionHeader.n_events) #FIXME : should not it be in the parent class?
        if 'g4propagator' in self.primary_propagator.keys():
            g4prop = self.primary_propagator['g4propagator']
            result = g4prop.propagate()
            if g4prop.cherenkov:
                self.vertices, self.tracks, new_photons = result
                photons['geant4'] = new_photons
                self.log.info(f"{len(np.unique(self.tracks[:,0]))} tracks simulated")
                self.log.info(f"{new_photons.n_tracks} photons produced " +
                              f"(1/{self.photon_suppression} of real number)")
            else:
                self.vertices, self.tracks = result
        #
        if 'cascadeCherenkov' in self.primary_propagator.keys():
            log.debug(self.vertices)
            new_photons = self.primary_propagator['cascadeCherenkov'].propagate(self.vertices)
            self.log.info(f"{new_photons.n_tracks} photons in cascades (1/{self.photon_suppression} of real number)")
            if new_photons.n_tracks > 0:
                photons['cascades'] = new_photons
        #
        if 'trackCherenkov' in self.primary_propagator.keys():
            log.debug(self.tracks)
            new_photons = self.primary_propagator['trackCherenkov'].propagate(self.tracks)
            self.log.info(f"{new_photons.n_tracks} photons from tracks (1/{self.photon_suppression} of real number)")
            if new_photons.n_tracks > 0:
                photons['tracks'] = new_photons
        #
        if 'mcPhotonTransporter' in self.primary_propagator.keys():
            self.clear_hits()
            photons_to_transport = Photons()
            for photons_to_transport in photons.values():
                new_hits = self.primary_propagator['mcPhotonTransporter'].transport(
                                                            photons_to_transport,
                                                            self.medium.get_model(photons_to_transport),
                                                            self.geometry)
                if len(self.hits) == 0:
                    self.hits = new_hits
                else:
                    self.hits = np.concatenate((self.hits, new_hits), axis=0)
            #self.write_hits()
            self.log.info(f"{len(np.unique(self.hits[:,0]))} OMs fired")
            self.log.info(f"{self.hits.shape[0]} hits detected")
        #
        if self.tracks != []:
            self.write_tracks()
        if self.hits != []:
            self.write_hits()
        bunch_id = 0
        n_photons_total = 0
        for label, photon_bunch in photons.items():
            n_photons_total += photon_bunch.n_tracks
            self.log.debug(f"photon bunch {bunch_id}: {label}")
            self.write_photons_bunch(photon_bunch, bunch_id, label)
            bunch_id += 1            
        self.write_number_of_bunches(bunch_id, n_photons_total)
        #
        self.write_event_header()


    def next_multithread(self, n, jobs=0):
#        self.next()
        from multiprocessing.pool import ThreadPool
        from multiprocessing import cpu_count
        if jobs == 0:
            jobs = cpu_count()
        t = ThreadPool(processes=jobs)
        t.map(self.next, range(1,n))
        t.close()

    def get_photons_sampling_weight(self):
        return 1./self.photon_suppression

    def get_vertices(self):  #FIXME: do we need vertices?
        return self.vertices
