import numpy as np
from g4camp.g4camp import g4camp
from ntsim.utils.report_timing import report_timing
from ntsim.photonTransporters.Photons import Photons

import logging
log = logging.getLogger('g4propagator')


class g4propagator(g4camp):

    def __init__(self, cherenkov=False):
        super().__init__(cherenkov, 'gun')
        self.module_type = "propagator"
        self.cherenkov=cherenkov
        if cherenkov:
            log.debug("Cherenkov effect enabled")
        else:
            log.debug("Cherenkov effect disabled")
        log.info("initialized")

    def configure(self, opts):
        # pre-init actions
        self.setPhotonSuppressionFactor(opts.photon_suppression)
        self.setSkipMinMax(0, opts.g4_casc_max)
        self.setRandomSeed(opts.g4_random_seed)
        self.setDetectorHeight(opts.g4_detector_height)
        self.setDetectorRadius(opts.g4_detector_radius)
        #
        super().configure() # /run/initialize happens here
        #
        # post-init actions
        self.setGunParticle(opts.g4_particle)
        self.setGunEnergy(float(opts.g4_energy[0]), opts.g4_energy[1])
        self.setGunPosition(float(opts.g4_position[0]), float(opts.g4_position[1]),
                            float(opts.g4_position[2]), opts.g4_position[3])
        self.setGunDirection(float(opts.g4_direction[0]), float(opts.g4_direction[1]),
                             float(opts.g4_direction[2]))
        log.info("configured")

    def getPhotonFraction(self):
        return 1./self.ph_suppression_factor

    def print_casc_starter_info(self, casc_starters):
        log.info(f"number of cascades : {len(casc_starters)}")
        #pdgids, counts = np.unique([vertex[2][0][0] for vertex in vertices], return_counts=True)
        #for pdgid, count in zip(pdgids, counts):
        #    log.debug(f"      {pdgid:<12} : {count}")

    def print_track_info(self, tracks):
        uid = tracks[:,0]
        n_tracks = len(np.unique(uid))
        n_points = len(tracks)
        n_segments = n_points - n_tracks
        log.info(f"number of tracks and segments : {n_tracks} / {n_segments}")

    @report_timing
    def propagate(self):
        log.info("running")
        evt_data = next(self.run(1))
        casc_starters = evt_data.particles
        tracks = evt_data.tracks
        self.print_casc_starter_info(casc_starters)
        self.print_track_info(tracks)
        if self.cherenkov == False:
            return casc_starters, tracks
        #
        photon_cloud = np.array(evt_data.photon_cloud)
        n_photons = photon_cloud.shape[0]
        position = photon_cloud[:,0:3]
        time = photon_cloud[:,3]
        direction = photon_cloud[:,4:7]
        wavelength = photon_cloud[:,7]
        position = np.expand_dims(position, axis=0) #FIXME in Photon: only one step by default
        direction = np.expand_dims(direction, axis=0)
        time = np.expand_dims(time, axis=0)
        n_steps = 1
        photons = Photons()
        photons.init(n_photons, n_steps, position, time, direction, wavelength)
        return casc_starters, tracks, photons
