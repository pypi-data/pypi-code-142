from ntsim.photonTransporters.Photons import Photons
from ntsim.primaryGenerators.Diffuser import DiffuserExponential,DiffuserCone
from ntsim.utils.gen_utils import generate_cherenkov_spectrum
import numpy as np


import logging
log = logging.getLogger('Laser')

class Laser():
    def __init__(self):
        self.module_type = 'generator'
        self.diffuser = None
        log.info("initialized")

    def configure(self,opts):
        self.waves = opts.laser_waves
        self.n_bunches = opts.laser_n_bunches
        self.photon_weight = opts.laser_photon_weight
        self.steps = 1
        self.n_photons = int(opts.laser_n_photons/opts.laser_n_bunches)
        self.direction = opts.laser_direction
        self.position = opts.laser_position
        if opts.laser_diffuser[0] == 'exp':
            self.diffuser = DiffuserExponential(float(opts.laser_diffuser[1]))
        elif opts.laser_diffuser[0] == 'cone':
            self.diffuser = DiffuserCone(float(opts.laser_diffuser[1]))
        self.photons = Photons()
        log.info('configured')
        return

    def get_direction(self):
        dir0 = np.array(self.direction,dtype=np.float64)
        if not self.diffuser:
            self.dir = np.tile(dir0,(self.steps,self.n_photons,1))
        else:
            dir = np.tile(dir0,(self.n_photons,1))
            dir = self.diffuser.random_direction(dir)
            dir = np.tile(dir,(self.steps))
            dir = np.reshape(dir,(self.n_photons,self.steps,3))
            dir = np.swapaxes(dir, 0, 1)
            self.dir = dir

    def make_photons(self):
        self.get_direction()
        self.r  = np.tile(np.array(self.position,dtype=np.float64), (self.steps,self.n_photons,1))
        self.t = np.tile(np.array([0.],dtype=np.float64),(self.steps,self.n_photons))
        if self.waves[0] == self.waves[1]:
            wavelengths = np.tile(np.array([self.waves[0]],dtype=np.float64),self.n_photons)
        else:
            wavelengths = generate_cherenkov_spectrum(self.waves[0],self.waves[1],self.n_photons)
        self.photons.init(self.n_photons,self.steps,self.r,self.t,self.dir,wavelengths,weight=self.photon_weight)


    def next(self):
        for i in range(self.n_bunches):
            self.make_photons()
            yield self.photons
