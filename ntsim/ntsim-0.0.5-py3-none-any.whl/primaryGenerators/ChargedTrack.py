import numpy as np

from ntsim.utils.gen_utils import unit_vector, align_unit_vectors, generate_cherenkov_spectrum
import ntsim.utils.systemofunits as units
from ntsim.photonTransporters.Photons import Photons

from bgvd_model.BaikalWater import BaikalWater

import logging
log = logging.getLogger('Charged_Track')


class ChargedTrack():
    def __init__(self):
        self.module_type = 'generator'
        log.info("initialized")

    def configure(self,opts):
        self.cherenkov_waves = opts.charged_primary_cherenkov_waves
        self.direction = opts.charged_direction
        self.position = opts.charged_position_m
        self.track_length = opts.charged_length_m
        self.n_steps = int(self.track_length[0] / (units.ns * units.light_velocity_vacuum))
        self.photons = Photons()
        self.random_walk()
        self.cherenkov_spectrum()
        log.info('configured generator')

    def random_walk(self, t_step = units.ns):
        self.r = np.tile(np.array(self.position, dtype = np.float64), (self.n_steps, 1))
        self.t = np.tile(0., (self.n_steps,))
        self.dir = unit_vector(np.tile(self.direction, (self.n_steps, 1)))
        for n in range(1, self.n_steps):
            self.t[n] = self.t[n-1] + t_step
            self.r[n] = self.r[n-1] + self.dir[n-1] * t_step * units.light_velocity_vacuum
        self.t_min = np.min(self.t)
        self.t_max = np.max(self.t)

    def cherenkov_spectrum(self, n_photons = 10**3):
        self.wave_min, self.wave_max = self.cherenkov_waves[0], self.cherenkov_waves[1]
        self.waves = np.linspace(self.wave_min, self.wave_max, n_photons)
        self.BaikalWaterProps = BaikalWater()
        refractive_index  = np.interp(self.waves, self.BaikalWaterProps.wavelength, self.BaikalWaterProps.group_refraction_index)
        sinsq = 1. - np.power(refractive_index, -2)
        prob = 2 * np.pi * units.alpha_em / self.waves**2 * sinsq * np.diff(self.waves)[0]
        self.spectrum_integral = np.sum(prob)
        self.spectrum_prob = prob/self.spectrum_integral
        self.dr = np.diff(self.r, axis = 0)
        self.dr_length = np.sqrt(np.sum(np.power(self.dr, 2), axis = 1))[0]
        self.n_photons_mean = (self.spectrum_integral * units.m / units.nm) * self.dr_length

    def track_light(self, steps):
        n_photons_rndm = np.random.default_rng().poisson(lam = self.n_photons_mean)
        n_tot = np.sum(n_photons_rndm)
        s = np.random.default_rng().uniform(size = n_tot)
        s = np.sort(s)
        ph_t = self.t_min + s*(self.t_max - self.t_min)
        indices = np.searchsorted(self.t, ph_t, side = 'right')
        indices = np.sort(indices)
        dt = ph_t - self.t[indices]
        ph_r = self.r[indices, :] + self.dir[indices, :] * dt[:, None] * units.light_velocity_vacuum
        wave_min, wave_max = self.cherenkov_waves[0], self.cherenkov_waves[1]
        self.rwaves = generate_cherenkov_spectrum(self.wave_min, self.wave_max, n_tot)
#        self.rwaves = np.random.default_rng().choice(self.waves, n_tot, p = self.spectrum_prob)
        wavelength = self.rwaves
        refractive_index = np.interp(self.rwaves, self.BaikalWaterProps.wavelength, self.BaikalWaterProps.group_refraction_index)
        costheta = 1. / refractive_index
        sintheta = np.sqrt(1 - costheta**2)
        phi = 2 * np.pi * np.random.default_rng().uniform(size = n_tot)
        cosphi = np.cos(phi)
        sinphi = np.sin(phi)
        ph_dir = np.array([cosphi * sintheta, sinphi * sintheta, costheta]).T
        z_dir = np.tile(np.array([0. ,0., 1]), (n_tot, 1))
        rot = align_unit_vectors(z_dir, self.dir[indices, :])
#        print(rot[0].as_euler('xyz', degrees=True))
        ph_dir = rot.apply(ph_dir)
        ph_r   = np.tile(ph_r.T, (steps))
        ph_r = np.reshape(ph_r.T, (steps,n_tot, 3))
        ph_dir = np.tile(ph_dir.T, (steps))
        ph_dir = np.reshape(ph_dir.T, (steps,n_tot, 3))
        ph_t   = np.tile(ph_t.T,  (steps,))
        ph_t  = np.reshape(ph_t.T,( steps, n_tot))
        return self.photons.init(n_tot, steps, ph_r, ph_t, ph_dir, wavelength)

    def next(self):
        for n in range(self.n_steps):
            self.track_light(1)
            yield self.photons
