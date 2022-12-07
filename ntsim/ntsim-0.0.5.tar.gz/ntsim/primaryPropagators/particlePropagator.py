import numpy as np
from ntsim.primaryPropagators.g4propagator import g4propagator
from ntsim.primaryPropagators.trackCherenkov import trackCherenkov
from ntsim.primaryPropagators.cascadeCherenkov import cascadeCherenkov
from ntsim.photonTransporters.Photons import Photons
from ntsim.utils.report_timing import report_timing
from ntsim.utils.gen_utils import get_particle_name_by_pdgid

import logging
log = logging.getLogger('particlePropagator')


class particlePropagator:

    def __init__(self, cherenkov=False):
        self.module_type = "propagator"
        self.g4prop = g4propagator(cherenkov=cherenkov)
        self.ccprop = cascadeCherenkov()
        self.tcprop = trackCherenkov()
        log.info("initialized")

    def configure(self, opts):
        self.g4prop.configure(opts)
        self.ccprop.configure(opts)
        self.tcprop.configure(opts)
        log.info("configured")

    @report_timing
    def propagate(self, input_particles):
        particles = np.empty((0,9), dtype=float)
        tracks = np.empty((0,7), dtype=float)
        photons = {'casc': Photons(),
                   'track': Photons()}
        for ip, input_particle_data in enumerate(input_particles.get_particles()):
            pdgid, x_m, y_m, z_m, t_ns, Px_GeV, Py_GeV, Pz_GeV, Etot_GeV = input_particle_data
            particle_name = get_particle_name_by_pdgid(pdgid)
            self.g4prop.setGunParticle(particle_name)
            self.g4prop.setGunPosition(x_m, y_m, z_m, "m")
            self.g4prop.setGunDirection(Px_GeV, Py_GeV, Pz_GeV)
            self.g4prop.setGunEnergy(Etot_GeV, "GeV")
            #
            g4output = self.g4prop.propagate()
            if self.g4prop.cherenkov:
                casc_starters, other_tracks, photons["geant4"] = g4output
            else:
                casc_starters, other_tracks = g4output
            particles = np.concatenate((particles, casc_starters))
            tracks = np.concatenate((tracks, other_tracks))
            photons['casc'] = photons['casc'].add_photons(self.ccprop.propagate(casc_starters))
            photons['track'] = photons['track'].add_photons(self.tcprop.propagate(other_tracks))
            #particles[f"{ip}_{particle_name}_geant4"] = casc_starters
            #tracks[f"{ip}_{particle_name}_geant4"] = other_tracks 
            #photons[f"{ip}_{particle_name}_cascades"] = self.ccprop.propagate(casc_starters)
            #photons[f"{ip}_{particle_name}_tracks"] = self.tcprop.propagate(other_tracks)
        return particles, tracks, photons
