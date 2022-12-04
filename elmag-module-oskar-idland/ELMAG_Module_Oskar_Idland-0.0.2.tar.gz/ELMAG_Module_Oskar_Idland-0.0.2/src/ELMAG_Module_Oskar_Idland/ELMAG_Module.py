from numba import njit
import numpy as np

'''
Module for calculating electric fields and potentials in 3d. Requires numba and numpy\n
efield, epot - Field and potential from point charge\n
efieldLine, epotLine - Field and potential from line charge\n
efieldCircle, epotCirle - Field and potential from circle charge
'''

class Field():
    def __init__(self):
        pass
    
    @staticmethod
    @njit
    def efield(self, r, particle_pos, q, ϵ):
        '''
        Calculates electric field from point charge
        r - point of observation\n
        particle_pos - particle position\n
        q - Charge of particle\n
        eps0 - permittivity
        '''
        R = r - particle_pos
        R_norm = np.linalg.norm(R)
        E = q/(4*np.pi*ϵ) * (R/R_norm**3)
        
        return E

    @staticmethod
    @njit
    def epot(self, r, particle_pos, q, eps0):
        R_norm = np.linalg.norm(r-particle_pos)
        V = q/(4*np.pi*eps0*R_norm)
        return V

    @staticmethod
    @njit
    def efieldLine(self, q, line_length, r, N, eps0):
        E = np.zeros(3)
        dl = line_length/N
        dq = q/N
        for i in range(N):
            r_q = np.array([-line_length/2 + i*dl ,0.0, 0.0])
            R = r - r_q
            R_norm = np.linalg.norm(R) 
            E += dq/(4*np.pi*eps0) * R/R_norm**3
            
        return E

    @staticmethod
    @njit
    def epotLine(self, q, line_length, r, N, eps0):
        V = 0
        dl = line_length/N
        dq = q/N
        for i in range(N):
            r_q = np.array([-line_length/2 + i*dl, 0.0, 0.0])
            R_norm = np.linalg.norm(r-r_q)
            V += dq/(4*np.pi*eps0*R_norm)
        return V

    @staticmethod
    @njit
    def efieldCircle(self, r, q, rad, N, eps0):
        E = np.zeros(3)
        
        if np.linalg.norm(r) < rad:
            return E
        
        else:
            dq = q/N
            for i in range(N):
                θ = 2*np.pi/N * i
                r_q = rad * np.array([np.cos(θ), np.sin(θ), 0.0])
                R = r - r_q
                R_norm = np.linalg.norm(R)
                E += dq/(4*np.pi*eps0) * R/R_norm**3
            
            return E
        
    @staticmethod
    @njit
    def epotCirle(self, r, q, rad, N, eps0):
        
        V = 0
        dq = q/N
        if np.linalg.norm(r) < radius:
            return q/(4*np.pi*eps0*rad)
        
        else:
            for i in range(N):
                θ = 2*np.pi/N * i
                r_q = rad * np.array([np.cos(θ), np.sin(θ), 0.0])
                R = r - r_q
                R_norm = np.linalg.norm(R)
                V += dq/(4*np.pi*eps0*R_norm)
                
        return V