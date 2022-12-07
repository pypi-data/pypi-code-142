import numpy as np
from ntsim.utils.Particles import Particles
from ntsim.utils import gen_utils

import logging
log = logging.getLogger('ToyGen')

class ToyGen():
    def __init__(self):
        self.module_type = 'generator'
        log.info("initialized")

    def configure(self, opts):
        self.particles = Particles(1)
        pdgid = gen_utils.get_pdgid_by_particle_name(opts.toy_primary_name)
        position = opts.toy_primary_position
        time = 0
        direction = opts.toy_primary_direction
        energy = opts.toy_primary_energy
        self.particles.add_particle(pdgid, *position, time, *direction, energy)
        print(":::")
        print(self.particles)
        log.info('configured')

    def next(self):
        return self.particles
