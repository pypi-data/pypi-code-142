import abc
import configargparse
import sys

import logging
log = logging.getLogger('Primary')

import pkg_resources
available_packages = [pkg.key for pkg in pkg_resources.working_set]

try:
    from nupropagator.nuprop import NuProp
except:
    log.warning("'nupropagator' package is not available")

# Generators
from ntsim.primaryGenerators.CorsikaGVDDataBankReader import *
from ntsim.primaryGenerators.Laser import *
from ntsim.primaryGenerators.ToyGen import *
from nupropagator.nugen import NuGen
from ntsim.primaryGenerators.ChargedTrack import *

# Propagators
#from ntsim.primaryPropagators.muonPropagator import * # depricated
from ntsim.primaryPropagators.MUMPropagator import *
if 'geant4-pybind' in available_packages:
    from ntsim.primaryPropagators.g4propagator import *
else:
    log.warning("'geant4_pybind' is not installed; 'g4propagator' is not available.")
from ntsim.primaryPropagators.cascadeCherenkov import *
from ntsim.primaryPropagators.trackCherenkov import *
from ntsim.primaryPropagators.particlePropagator import *
from ntsim.photonTransporters.mcPhotonTransporter import *

# Read/write
from ntsim.io.h5Writer import *
from ntsim.io.gEventHeader import gEventHeader

class Primary(metaclass=abc.ABCMeta):
    def __init__(self):
        self.primary_generator = None
        self.primary_propagator = {}
        self.primary_name = ''
        self.primary_track = []
        self.medium   = None
        self.geometry = None
        self.writer   = None
        self.gEvent   = None
        self.clear_data()

    def init_h5Writer(self):
        self.writer = h5Writer()

    def clear_data(self):
        self.particles = np.empty((0,9), dtype=float) # FIXME: replace by a class object
        self.tracks = np.empty((0,7), dtype=float) # FIXME: replace by a class object
        self.photons_dict = {}
        self.hits = np.empty((0,15), dtype=float) # FIXME: replace by a class object

    def add_particles(self, particles):
        self.particles = np.concatenate((self.particles, particles))

    def add_tracks(self, tracks):
        self.tracks = np.concatenate((self.tracks, tracks))

    def add_photons(self, photons, label=""):
        if label in self.photons_dict.keys() and label != "":
            log.warning(f"photon label '{label}' exists!")
        self.photons_dict[label] = photons

    def add_hits(self, hits):
        self.hits = np.concatenate((self.hits, hits))

    def write_data(self):
        #
        self.writer.make_event_folder(self.gEvent.gProductionHeader.n_events)
        self.writer.write_particles(self.particles)
        self.writer.write_tracks(self.tracks)
        bunch_nb = 0
        n_photons_total = 0
        for label, photons in self.photons_dict.items():
            self.writer.write_photons_bunch(photons, bunch_nb, label)
            bunch_nb += 1
            n_photons_total += photons.n_tracks
        self.writer.write_hits(self.hits)
        self.writer.write_number_of_bunches(bunch_nb, n_photons_total)
        self.write_event_header()

    def write_event_header(self):
        eventHeader = gEventHeader()
        eventHeader.set_photons_sampling_weight(self.get_photons_sampling_weight())
        eventHeader.set_om_area_weight(self.get_om_area_weight())
        self.writer.write_event_header(eventHeader)

    @abc.abstractmethod
    def get_photons_sampling_weight(self):
        """
        Primary children must implement this method
        """

    def get_om_area_weight(self):
        return np.power(self.geometry.true_radius/self.geometry.prod_radius,2)

    def set_medium(self,medium):
        self.medium = medium

    def set_geometry(self,geometry):
        self.geometry = geometry

    def set_gEvent(self,event):
        self.gEvent = event

    @abc.abstractmethod
    def configure(self,opts):
        """
        next objects
        """

    def configure_generator(self,opts):
        module_name = opts.primary_generator
        if module_name not in globals().keys():
            log.error(f"No such generator available: '{module_name}'")
            sys.exit()
        #
        constructor_method = globals()[module_name]
        module = constructor_method() # initialized the module
        #
        #if module.module_type != "generator":  # FIXME NuGen does not have 'module_type'
        #    log.error(f"'{module_name}' is not generator")
        #    sys.exit()
        #
        if callable(getattr(module, "configure", None)):
            module.configure(opts) # configure the module
        else:
            log.warning(f"module {module_name} does not have 'configure' method")
        self.primary_generator = module

    def configure_propagators(self,opts,arg_dict={}):
        for module_name in opts.primary_propagator:
            if module_name not in globals().keys():
                log.error(f"No such propagator available: '{module_name}'")
                sys.exit()
            #
            constructor_method = globals()[module_name]
            if module_name in arg_dict.keys():
                args = arg_dict[module_name]
            else:
                args = ()
            module = constructor_method(*args) # initialized the module
            #
            #if module.module_type != "propagator":  # FIXME NuProp does not have 'module_type'
            #    log.error(f"'{module_name}' is not propagator")
            #    sys.exit()
            #
            if callable(getattr(module, "configure", None)):
                module.configure(opts) # configure the module
            else:
                log.warning(f"module {module_name} does not have 'configure' method")
            self.primary_propagator[module_name] = module
        #
        self.photons_sampling_weight = 1./opts.photon_suppression

    @abc.abstractmethod
    def next(self):
        """
        next objects
        """
    def get_photons_sampling_weight(self):
        return self.photons_sampling_weight



def getPrimary(name):
    if name == 'muon':
        from ntsim.primaries.Muon import Muon
        return Muon()
    elif name == 'neutrino':
        from ntsim.primaries.Neutrino import Neutrino
        return Neutrino()
    elif name == 'laser':
        from ntsim.primaries.LaserPrimary import LaserPrimary
        return LaserPrimary()
    elif name == 'ChargedTrack':
        from ntsim.primaries.ChargedPrimary import ChargedPrimary
        return ChargedPrimary()
    elif name == 'g4particle':
        if 'geant4-pybind' in available_packages:
            from ntsim.primaries.G4Particle import G4Particle
            return G4Particle()
        else:
            log.error("'geant4_pybind' is not installed; primary 'g4particle' is not available. install it with pip install geant4_pybind")
    elif name == "toyPrimary":
        from ntsim.primaries.ToyPrimary import ToyPrimary
        return ToyPrimary()
    else:
        log.error(f'Primary name {name} is unknown')
        return None
    log.info(f'created primary {name}')
