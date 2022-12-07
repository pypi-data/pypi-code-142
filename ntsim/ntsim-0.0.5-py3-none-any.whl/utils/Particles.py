import numpy as np
import logging
log = logging.getLogger('Particles')

class Particles():
    def __init__(self,number_of_particles=2) -> None:
        self.n_particles = 0
        self.data_type = [('pdgid',int),('x_m',float),('y_m',float),('z_m',float),('t_ns',float),
                          ('Px_GeV',float),('Py_GeV',float),('Pz_GeV',float),('Etot_GeV',float)]
        self.max_number = number_of_particles
        self.particles = np.zeros(shape=(self.max_number),dtype=self.data_type)

        return

    def add_particle(self,pdgid, x_m, y_m, z_m, t_ns, Px_GeV, Py_GeV, Pz_GeV, Etot_GeV) -> None:

        if self.n_particles>self.max_number-1:
            # the number of particles exceed assumed array size.
            particles = np.zeros(shape=(self.max_number),dtype=self.data_type)
            self.particles = np.concatenate((self.particles,particles),axis=0)
            self.max_number = self.particles.shape[0]

        self.particles[self.n_particles]['pdgid'] = pdgid
        self.particles[self.n_particles]['x_m'] = x_m
        self.particles[self.n_particles]['y_m'] = y_m
        self.particles[self.n_particles]['z_m'] = z_m
        self.particles[self.n_particles]['t_ns'] = t_ns
        self.particles[self.n_particles]['Px_GeV'] = Px_GeV
        self.particles[self.n_particles]['Py_GeV'] = Py_GeV
        self.particles[self.n_particles]['Pz_GeV'] = Pz_GeV
        self.particles[self.n_particles]['Etot_GeV'] = Etot_GeV
        self.n_particles +=1
        return

    def get_particles(self):
        #return self.particles[0:self.n_particles-1] # ???
        return self.particles

    def print(self):
        for i in range(self.n_particles):
            pdgid = self.particles[i]['pdgid']
            x = self.particles[i]['x_m']
            y = self.particles[i]['y_m']
            z = self.particles[i]['z_m']
            t = self.particles[i]['t_ns']
            px = self.particles[i]['Px_GeV']
            py = self.particles[i]['Py_GeV']
            pz = self.particles[i]['Pz_GeV']

            log.info(f'particle pdgid={pdgid}, (x,y,z)=({x},{y},{z}), (px,py,pz)=({px},{py},{pz})')
