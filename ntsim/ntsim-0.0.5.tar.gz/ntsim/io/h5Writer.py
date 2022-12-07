import h5py
import numpy as np
import logging
log = logging.getLogger('h5Writer')
from ntsim.utils.report_timing import report_timing

class h5Writer:
    def __init__(self):
        self.event_folder = None

    def configure(self,options):
        self.save_event_header = options.h5_save_event_header
        self.save_tracks       = options.h5_save_tracks
        self.save_particles    = options.h5_save_particles
        self.save_photons      = options.h5_save_photons
        self.save_hits         = options.h5_save_hits
        self.save_vertices     = options.h5_save_vertices
        self.h5_output_file    = options.h5_output_file
        self.h5_output_dir     = options.h5_output_dir
        self.save_geometry     = options.h5_save_geometry
        self.save_medium_model = options.h5_save_medium_model
        self.save_prod_header  = options.h5_save_prod_header
        self.save_primary_header  = options.h5_save_primary_header

        log.info('configured')
        return

    def make_event_folder(self,n_events):
        self.event_folder = self.h5_file.create_group(f'event_{n_events}')

    def init_h5(self):
        import os
        if not os.path.exists(self.h5_output_dir):
            os.makedirs(self.h5_output_dir)
        log.info(f"open  {self.h5_output_dir}/{self.h5_output_file}.h5")
        self.h5_file =  h5py.File(f'{self.h5_output_dir}/{self.h5_output_file}.h5', 'w')

    def write_particles(self,particles):
        if not self.save_particles or len(particles) == 0:
            return
        log.info("writing particles")
        #
        particles_folder = self.event_folder.create_group('particles')
        data_type = [('pdgid', int),
                     ('x_m', float), ('y_m', float), ('z_m', float),
                     ('t_ns', float),
                     ('Px_m', float), ('Py_m', float), ('Pz_m', float),
                     ('E_GeV', float)]
        named_data = np.array([tuple(particle) for particle in particles], dtype=data_type)
        particles_folder.create_dataset("particles", data=named_data)

    def write_tracks(self,tracks):
        if not self.save_tracks or len(tracks) == 0:
            return
        log.info("writing tracks")
        #
        tracks_folder = self.event_folder.create_group('tracks')
        data_type = [('uid', int), ('pdgid', int),
                     ('x_m', float), ('y_m', float), ('z_m', float),
                     ('t_ns', float), ('E_GeV', float)]
        named_data = np.array([tuple(point) for point in tracks], dtype=data_type)
        tracks_folder.create_dataset("points", data=named_data)

    def write_photons_bunch(self,photons,bunch_number,label=""):
        if not self.save_photons:
            return
        log.info(f"writing a photon bunch: {label}")
        if photons:
            photons_folder = self.event_folder.create_group(f'photons_{bunch_number}')
            photons_folder.create_dataset("weight",     data=photons.weight)
            photons_folder.create_dataset("n_tracks",   data=photons.n_tracks)
            photons_folder.create_dataset("n_steps",    data=photons.n_steps)
            photons_folder.create_dataset("r",          data=photons.r)
            photons_folder.create_dataset("t",          data=photons.t)
            photons_folder.create_dataset("dir",        data=photons.dir)
            photons_folder.create_dataset("wavelength", data=photons.wavelength)
            photons_folder.create_dataset("ta",         data=photons.ta)
            photons_folder.create_dataset("ts",         data=photons.ts)
            photons_folder.attrs["label"] = label

    def write_hits(self,hits):
        if not self.save_hits or len(hits) == 0:
            return
        log.info("writing hits")
        #
        hits_folder = self.event_folder.create_group('hits')
        # name data fields
        data_type = [('uid', int), ('cluster', int), ('id', int),
                     ('time_ns', float),
                     ('w_noabs', float), ('w_pde', float), ('w_gel', float), ('w_angular', float),
                     ('x_m', float), ('y_m', float), ('z_m', float),
                     ('outside_mask', float), ('photon_id', int),
                     ('step_number', int), ('weight',float)]
        named_data = np.array([ tuple(row) for row in hits ], dtype=data_type)
        hits_folder.create_dataset('data', data=named_data)

    def write_number_of_bunches(self,n_bunches,n_photons_total):
        self.event_folder.create_dataset("n_bunches", data=n_bunches)
        self.event_folder.create_dataset("n_photons_total", data=n_photons_total)

    def write_prod_header(self,productionHeader):
        if self.save_prod_header:
            g_header = self.h5_file.create_group('ProductionHeader')
            g_header.create_dataset("n_events",data=productionHeader.n_events)
            g_header.create_dataset("scattering_model",data=str(productionHeader.scattering_model_name))
            g_header.create_dataset("anisotropy",data=productionHeader.anisotropy)

    def write_primary_header(self,primHeader):
        if self.save_primary_header:
            g_header = self.h5_file.create_group('PrimaryHeader')
            g_header.create_dataset("name",data=primHeader.name)
            g_header.create_dataset("track",data=primHeader.track)


    def write_geometry(self,geometry):
        if self.save_geometry:
            geometry_folder = self.h5_file.create_group('geometry')
            geometry_folder.create_dataset('geom',data=geometry.geom)
            geometry_folder.create_dataset('bounding_box_strings',data=geometry.bounding_box_strings)
            geometry_folder.create_dataset('bounding_box_cluster',data=geometry.bounding_box_cluster)
            geometry_folder.create_dataset('det_normals',data=geometry.det_normals)

    def write_event_header(self,evtHeader):
        g_header = self.event_folder.create_group('event_header')
        g_header.create_dataset("photons_sampling_weight",data=evtHeader.get_photons_sampling_weight())
        g_header.create_dataset("om_area_weight",data=evtHeader.get_om_area_weight())
        return g_header

    @report_timing
    def close(self):
        log.info(f"close {self.h5_output_dir}/{self.h5_output_file}.h5")
        self.h5_file.close()
