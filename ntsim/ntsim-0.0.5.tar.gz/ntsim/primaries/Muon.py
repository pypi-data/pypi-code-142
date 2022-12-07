from ntsim.Primary import *
from ntsim.MuonSurface import *



class Muon(Primary):
    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('Muon')
        self.log.info("initialized")

    def configure(self,opts):
        self.configure_generator(opts)
        self.configure_propagators(opts)

    def next(self):
        self.clear_data()
        primaries = self.primary_generator.next()
        #log.debug(primaries)

        #Calculate the surface for muons entering water based on first muon theta (they go in parallell anyway)
        ms = MuonSurface(self.geometry)
        if primaries is None:
            log.warning("No primaries to propagate")
            return
        oldx_first = 0
        oldy_first = 0
        shift_x = 0
        shift_y = 0
        for i,event in enumerate(primaries['event']):
            if i == 0:
                #calclate the surface only for first muon
                ms.calculateSurface(event['theta_mu'],event['energy_mu'])
                #Generate the entry point on the surface for first muon
                ms.generatePoint()
                #Caluculate shift for other muons in the bundle (based on their positions relative to the first one)
                shift_x = ms.x_firstMu - event['x_mu']
                shift_y = ms.y_firstMu - event['y_mu']
                #Update the event record for the first muon
                event['x_mu'] = ms.x_firstMu
                event['y_mu'] = ms.y_firstMu
            else:
                #If more muons in the bundle, shift the additional ones by the values calculated for the first one
                event['x_mu'] = event['x_mu'] + shift_x
                event['y_mu'] = event['y_mu'] + shift_y

        log.debug(primaries)

        #
        mum_particles = None
        if 'MUMPropagator' in self.primary_propagator.keys():
            mprop = self.primary_propagator['MUMPropagator']
            mum_particles = Particles(1) # How many muons?
            for track in mprop.propagate(primaries):
                print(track)
                #TODO: particles.add_particle(pdgid= ,
                #                             x_m= , y_m= , z_m= ,
                #                             t_ns= , 
                #                             Px_GeV= , Py_GeV= , Pz_GeV= ,
                #                             Etot_GeV= )
        #
        if 'particlePropagator' in self.primary_propagator.keys():
            if mum_particles != None: # MUM worked
                input_particles = mum_particles
            else: # without MOM
                n_muons = len(primaries['event'])
                input_particles = Particles(n_muons)
                for muon in primaries['event']:
                    input_particles.add_particle(pdgid=13,  #pdgid can be -13?
                                                 x_m=muon['x_mu'], y_m=muon['y_mu'], z_m=1360,  # TODO check units
                                                 t_ns=muon['time_mu'], # TODO: check units
                                                 Px_GeV=0, Py_GeV=0, Pz_GeV=-1, # TODO: calculate
                                                 Etot_GeV=muon['energy_mu'])

            pprop = self.primary_propagator['particlePropagator']
            particles, tracks, photons_dict = pprop.propagate(input_particles)
            self.add_particles(particles)
            self.add_tracks(tracks)
        #
        if 'mcPhotonTransporter' in self.primary_propagator.keys():
            for label, photons in photons_dict.items():
                hits = self.primary_propagator['mcPhotonTransporter'].transport(
                                                                          photons,
                                                                          self.medium.get_model(photons),
                                                                          self.geometry)
                self.add_hits(hits)
                self.log.info(f"  {label:<36}: {len(np.unique(hits[:,0]))} OMs fired")
                self.log.info(f"  {label:<36}: {hits.shape[0]} hits detected")
                self.add_photons(photons, label)
        self.write_data()


    def next_multithread(self,n,jobs=0):
        from multiprocessing.pool import ThreadPool
        from multiprocessing import cpu_count
        if jobs == 0:
            jobs = cpu_count()
        primaries_raw = self.primary_generator.next_record_bytes(n)
        t = ThreadPool(processes=jobs)
        primaries = t.map(self.primary_generator.parse_event_record, primaries_raw)
        t.close()
        self.primary_propagator['muonPropagator'].propagate_multithread(primaries)

    def get_photons_sampling_weight(self):
        return 1.

    def get_vertices(self):
        return []
