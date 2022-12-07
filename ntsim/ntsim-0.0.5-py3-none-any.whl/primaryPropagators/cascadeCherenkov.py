import numpy as np
from ntsim.photonTransporters.Photons import Photons
from ntsim.utils.report_timing import report_timing
from ntsim.utils.gen_utils import rotate_photons
from ntsim.utils.gen_utils import generate_cherenkov_spectrum
from ntsim.utils.gen_utils import sample_cherenkov_photon_directions

import logging
log = logging.getLogger('cascadeCherenkov')

class cascadeCherenkov:
    def __init__(self):
        self.module_type = "propagator"
        self.ph_fraction = None
        self.par_tmax_a = 2.00
        self.par_tmax_b = 0.98
        self.par_q_const = 4.13
        log.info("initialized")

    def configure(self, opts):
        self.ph_fraction = 1./opts.photon_suppression
        self.X0 = opts.casc_param_X0
        self.lambda_min = opts.cherenkov_wavelengths[0]
        self.lambda_max = opts.cherenkov_wavelengths[1]
        self.refr_index = opts.refraction_index # FIXME to remove once not used
        self.costh_a = 2.87
        self.costh_b = -5.71
        self.costh_c = 0.341
        self.costh_d = -0.00131
        self.costh_values = np.random.uniform(-1, 1, 10000000)
        self.costh_prob = self.costh_distribution(self.costh_values, 1./self.refr_index)
        self.costh_prob = self.costh_prob / self.costh_prob.sum()
        log.info("configured")

    def costh_distribution(self, x, costh_ch):
        return self.costh_a * np.exp( self.costh_b * np.abs(x - costh_ch)**self.costh_c ) + self.costh_d

    def sample_photon_directions(self, n_photons):
        phi = np.random.uniform(-np.pi, np.pi, size=n_photons)
        costh = np.random.choice(self.costh_values, p=self.costh_prob, size=n_photons)
        sinth = np.sqrt(1. - costh**2)
        x = sinth * np.sin(phi)
        y = sinth * np.cos(phi)
        z = costh
        return np.array([x, y, z]).T

    @report_timing
    def propagate(self, vertices):
        log.info("running")
        if len(vertices) == 0:
            log.warning("No vertices!")
        #
        photons = Photons()
        #
        casc_pdgid = vertices[:,0]
        casc_pos = vertices[:,1:4]
        casc_time = vertices[:,4]
        casc_dir = vertices[:,5:8] / np.sum(vertices[:,5:8]**2)**0.5
        casc_E = vertices[:,8]        
        #
        casc_n_photons = np.random.poisson(1.18e5*casc_E*self.ph_fraction)
        # TODO: check it has Poisson distribution
        casc_q_central = np.ones_like(casc_E) * self.par_q_const
        casc_tmax_central = self.par_tmax_a + self.par_tmax_b * np.log(casc_E)
        casc_q = casc_q_central # TODO: fluctuate it!
        casc_tmax = casc_tmax_central # TODO: fluctuate it!
        casc_gamma_k = casc_q + 1
        casc_gamma_theta = casc_tmax / (casc_q + 1)
        casc_gamma_theta[casc_gamma_theta<0] = 0.
        #
        n_photons = casc_n_photons.sum()
        #
        ph_pos = np.zeros((n_photons,3))
        ph_gamma_k = np.repeat(casc_gamma_k, casc_n_photons)
        ph_gamma_theta = np.repeat(casc_gamma_theta, casc_n_photons)
        ph_t = np.random.gamma(shape=ph_gamma_k, scale=ph_gamma_theta, size=n_photons)
        ph_pos[:,2] += ph_t*self.X0
        ph_casc_pos = np.repeat(casc_pos, casc_n_photons, axis=0)
        ph_casc_dir = np.repeat(casc_dir, casc_n_photons, axis=0)
        ph_pos = rotate_photons(ph_pos, ph_casc_dir)
        ph_pos += ph_casc_pos
        #
        c_const = 0.3 # m / ns
        ph_time = np.repeat(casc_time, casc_n_photons) + ph_t*self.X0 / c_const
        #
        #ph_dir = sample_cherenkov_photon_directions(n_photons, self.refr_index) 
        # TODO to be replaced by parametrized direction distributions
        ph_dir = self.sample_photon_directions(n_photons)
        ph_dir = rotate_photons(ph_dir, ph_casc_dir)
        #
        ph_wavelength = generate_cherenkov_spectrum(self.lambda_min, self.lambda_max, n_photons)
        #
        # add an extra dummy dimension for further steps
        ph_pos = np.expand_dims(ph_pos, axis=0)
        ph_dir = np.expand_dims(ph_dir, axis=0)
        ph_time = np.expand_dims(ph_time, axis=0)
        n_steps = 1 # or ph_pos.shape[0]
        photons.init(n_photons, n_steps, ph_pos, ph_time, ph_dir, ph_wavelength)
        #
        log.info(f"  {n_photons} photons produced")
        return photons
