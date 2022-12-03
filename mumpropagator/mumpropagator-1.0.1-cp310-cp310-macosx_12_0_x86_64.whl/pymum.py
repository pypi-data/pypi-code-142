from mumpropagator import _mumpropagator  as pm
import numpy as np

class mum(object):
    def init(self,imed=1, ipn=1, ibre=1, em=1.e-2, vm=1e-2,
                  ilep=1, iqcd=1, lux=1, iseed=1):

        import os
        if not os.path.exists('cards'):
            print('create cards folder')
            os.makedirs('cards')
        pm.init_mu(imed, ipn, ibre, em, vm, ilep, iqcd, lux, iseed)

    def transport(self,energy,depth):
        iti = 0
        itime = 0
        pm.enew(energy, depth, iti, itime)
        # copy the entire track to python object
        data_type = np.dtype([('interaction_type',float),('propagated_distance',float),
                              ('energy_in',float),('energy_out',float),
                              ('energy_loss',float)])
        track = np.zeros(pm.vhistory.numb, dtype=data_type)
        for step in range(pm.vhistory.numb):
            track[step]['interaction_type'] = pm.vhistory.ityp[step]
            track[step]['propagated_distance'] = pm.vhistory.eleng[step]
            track[step]['energy_in'] = pm.vhistory.ener1[step]
            track[step]['energy_out'] = pm.vhistory.ener2[step]
            track[step]['energy_loss'] = pm.vhistory.ener1[step]-pm.vhistory.ener2[step]
        return track
