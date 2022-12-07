import numpy as np
from ntsim.photonTransporters.Photons import Photons
from ntsim.utils.report_timing import report_timing
from ntsim.utils.gen_utils import rotate_photons
from ntsim.utils.gen_utils import generate_cherenkov_spectrum
from ntsim.utils.gen_utils import sample_cherenkov_photon_directions
from particle import Particle
from numba import jit, njit

import logging
log = logging.getLogger('trackCerenkov')

from time import time
prev_time = time()
def timing(label=""):
  global prev_time
  t0 = prev_time
  prev_time = time()
  return f"< {label:<30}>: {(time() - t0)*3e3:10.1f} ms"


#@jit
def distance(x1, x2):
    return np.sqrt(np.sum((x2-x1)**2, axis=1))


def get_sin2th(E, pdgid, n): 
    mask_e = np.isin(pdgid, [11,-11])
    mask_mu = np.isin(pdgid, [13,-13])
    electron = Particle.from_pdgid(11)
    muon = Particle.from_pdgid(13)
    beta = np.ones_like(E)
    # note that mass in 'particle' may be less than in Geant4
    beta[mask_e]  = ( 1. - ((electron.mass/1000.001)/E[mask_e])**2 )**0.5
    beta[mask_mu] = ( 1. - ((muon.mass/1000.001)   /E[mask_mu])**2 )**0.5
    sin2th = (1. - 1./(n*beta)**2)
    sin2th[sin2th<0] = 0
    return sin2th



class trackCherenkov():

    def __init__(self):
        self.module_type = "propagator"
        log.info("initialized")

    def configure(self, opts):
        self.ph_fraction = 1./opts.photon_suppression
        self.lambda_min = opts.cherenkov_wavelengths[0]
        self.lambda_max = opts.cherenkov_wavelengths[1]
        self.refr_index = opts.refraction_index
        log.info("configured")

    @report_timing
    def propagate(self, tracks):
        log.info("running")
        if len(tracks) == 0:
            self.log.warning("No tracks!")
        #
        # count segments
        n_tracks = len(np.unique(tracks[:,0]))
        n_points = len(tracks)
        n_segments = n_points - n_tracks
        #
        # filling positions and times of segment ends
        seg_uid1 = tracks[:-1,0]
        seg_uid2 = tracks[1:,0]
        mask1 = seg_uid1 == seg_uid2  # both segment end points must have same uid
        seg_pdgid = tracks[:-1,1]
        mask2 = np.isin(seg_pdgid, [11, -11, 13, -13])
        mask = (mask1 & mask2)
        seg_R1 = tracks[:-1,2:5][mask]
        seg_R2 = tracks[1:,2:5][mask]
        seg_T1 = tracks[:-1,5][mask]
        seg_T2 = tracks[1:,5][mask]
        seg_E = (tracks[1:,6][mask] + tracks[:-1,6][mask])/2.
        seg_sin2th = get_sin2th(seg_E, seg_pdgid[mask], self.refr_index)
        #
        n_per_cm_mean = 369.81 * 1239.84193 * (1./self.lambda_min - 1./self.lambda_max) * seg_sin2th
        seg_N_photons = np.random.poisson(n_per_cm_mean * distance(seg_R2, seg_R1) * 100 * self.ph_fraction)
        n_photons = seg_N_photons.sum()
        #
        # replicating segment ends positions and times for each photon
        ph_R1 = np.repeat(seg_R1, seg_N_photons, axis=0)
        ph_R2 = np.repeat(seg_R2, seg_N_photons, axis=0)
        ph_T1 = np.repeat(seg_T1, seg_N_photons)
        ph_T2 = np.repeat(seg_T2, seg_N_photons)
        #
        ph_rnd = np.random.uniform(size=(n_photons,1))
        ph_time = ph_T1 + ph_rnd[:,0] * (ph_T2 - ph_T1)
        ph_pos = ph_R1 + ph_rnd * (ph_R2 - ph_R1)
        ph_dir = sample_cherenkov_photon_directions(n_photons, self.refr_index)
        ph_dir = rotate_photons(ph_dir, ph_R2-ph_R1)
        ph_wavelength = generate_cherenkov_spectrum(self.lambda_min, self.lambda_max, n_photons)
        #
        # add an extra dummy dimension for further steps
        ph_pos = np.expand_dims(ph_pos, axis=0)
        ph_dir = np.expand_dims(ph_dir, axis=0)
        ph_time = np.expand_dims(ph_time, axis=0)
        photons = Photons()
        n_steps = 1
        photons.init(n_photons, n_steps, ph_pos, ph_time, ph_dir, ph_wavelength)
        #
        log.info(f"  {n_photons} photons produced")
        return photons
