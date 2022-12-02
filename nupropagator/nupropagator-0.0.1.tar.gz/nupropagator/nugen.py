class NuGen:
    def __init__(self,nu_energy='random',nu_direction='random',target='random',nu_pdg=14,xBj='random',yBj='random'):
        self.nu_energy_mode = nu_energy
        self.nu_direction_mode = nu_direction
        self.target_mode = target
        self.nu_pdg_mode = nu_pdg
        self.xBj_mode = xBj
        self.yBj_mode = yBj
        import logging
        self.log = logging.getLogger('nupropagator.NuGen')
        self.log.info(f'neutrino energy mode={self.nu_energy_mode}')
        self.log.info(f'neutrino direction mode={self.nu_direction_mode}')
        self.log.info(f'target mode={self.target_mode}')
        self.log.info(f'neutrino pdg mode={self.nu_pdg_mode}')
        self.log.info(f'neutrino+nucleon xBj mode={self.xBj_mode}')
        self.log.info(f'neutrino+nucleon yBj mode={self.xBj_mode}')


    def get_event(self,nu_pdg=14,target = 'proton',nu_energy_GeV=100.,xBj=0.2,yBj=0.3):
        # get neutrino energy
        if self.nu_energy_mode != 'random':
            nu_energy = nu_energy_GeV
        else:
            # select random
            nu_energy = 0. # FIXME

        # get nucleon
        if self.target_mode != 'random':
            nucleon = target
        else:
            # select random
            nucleon = 0 # FIXME


        # a temp fix to illustrate the idea
        # return two fake particles
        final_lepton = [13,0.,0.,nu_energy_GeV/2,nu_energy_GeV/2]
        final_nucleon= [211,0.,0.,nu_energy_GeV/2,nu_energy_GeV/2]
        return final_lepton,final_nucleon


    def next(self):
        return self.get_event()
