def parser():
    import configargparse, argparse

    p = configargparse.get_argument_parser()
# ntsim options
    p.add_argument('-l', '--log-level', choices=('deepdebug', 'debug', 'info', 'warning', 'error', 'critical'), default='INFO', help='logging level')
    p.add_argument('-p', '--primary_config',is_config_file=True,help='add primary config')
    p.add_argument('--geometry_config',is_config_file=True,default='configs/geometry.cfg',help='geometry config')
    p.add_argument("--h5writer_config", is_config_file=True,default='configs/h5writer.cfg',help="h5writer config")
    p.add_argument('--n_events',type=int,default=2,help='number of events to process')
    p.add_argument('--generators_path',env_var='GENERATORS_PATH',help='Path to generators folder')
    # p.add_argument('-j','--jobs',type=int,default=-1,help='number of multithread jobs [-1:singlethread;0:automatic;N:N jobs]')
    p.add_argument('--multithread',choices=('true','false'),default='false',help='run multithreaded') # TODO add limitation of number of threads
    p.add_argument('--photon_suppression',type=int,default=1000,help="Only every n-th photon is stored")
# Geometry options
    p.add_argument('--geometry_input',help='input file with geometry')
    p.add_argument('--geometry_output',help='output file with geometry')
    p.add_argument('--geometry_time_interval',nargs='+',help='time interval to read the geometry')
    p.add_argument('--geometry_clusters',nargs='+',type=int,help='list of clusters')
    p.add_argument('--geometry_true_radius',type=float,help='Optical Module true radius in m')
    p.add_argument('--geometry_prod_radius',type=float,help='Optical Module production radius in m')
# Primary options
    p.add_argument('--primary_name',help='primary particle name: numu, muon, g4particle, ...')
    p.add_argument('--primary_generator',help='primary particle generator')
    p.add_argument('--primary_propagator',nargs='+',help='simulation chain: primary --> photons')
# Medium options
    p.add_argument("--medium_scattering_model",default='HG',help="scattering model name: HG, Rayleigh, HG+Rayleigh")
    p.add_argument("--medium_anisotropy",type=float,default=0.99,help="light scattering anisotropy")
# h5Writer options
    p.add_argument("--h5_output_file",help="output file name")
    p.add_argument("--h5_output_dir",help="output directory name")
    ''' The following does not work with Python v. < 3.9 
    p.add_argument("--h5_save_geometry",default=False, action=argparse.BooleanOptionalAction,help="Boolean to save geometry")
    p.add_argument("--h5_save_medium_model",default=False, action=argparse.BooleanOptionalAction,help="Boolean to save water model: absorption & scattering")
    p.add_argument("--h5_save_prod_header",default=False, action=argparse.BooleanOptionalAction,help="Boolean to save production header")
    p.add_argument("--h5_save_event_header",default=False, action=argparse.BooleanOptionalAction,help="Boolean to save event header")
    p.add_argument("--h5_save_primary_header",default=False, action=argparse.BooleanOptionalAction,help="Boolean to save event header")
    p.add_argument("--h5_save_tracks",type=bool,default=False, action=argparse.BooleanOptionalAction,help="Boolean to save tracks")
    p.add_argument("--h5_save_photons",type=bool,default=False, action=argparse.BooleanOptionalAction,help="Boolean to save photons")
    p.add_argument("--h5_save_hits",type=bool,default=False, action=argparse.BooleanOptionalAction,help="Boolean to save hits")
    p.add_argument("--h5_save_vertices",default=False, action=argparse.BooleanOptionalAction,help="Boolean to save vertices")
    '''
    p.add_argument("--h5_save_geometry",default=False,help="Boolean to save geometry")
    p.add_argument("--h5_save_medium_model",default=False,help="Boolean to save water model: absorption & scattering")
    p.add_argument("--h5_save_prod_header",default=False,help="Boolean to save production header")
    p.add_argument("--h5_save_event_header",default=False,help="Boolean to save event header")
    p.add_argument("--h5_save_primary_header",default=False,help="Boolean to save event header")
    p.add_argument("--h5_save_tracks",type=bool,default=False,help="Boolean to save tracks")
    p.add_argument("--h5_save_particles",type=bool,default=False,help="Boolean to save particles")
    p.add_argument("--h5_save_photons",type=bool,default=False,help="Boolean to save photons")
    p.add_argument("--h5_save_hits",type=bool,default=False,help="Boolean to save hits")
    p.add_argument("--h5_save_vertices",default=False,help="Boolean to save vertices")
# LaserPrimary options
    p.add_argument("--laser_waves",nargs='+',type=float,default=[350,600],help="wavelengths interval")
    p.add_argument("--laser_n_photons",type=int,default=10000, help="number of photons to generate")
    p.add_argument("--laser_n_bunches",type=int,default=1,help="number of bunches")
    p.add_argument("--laser_photon_weight",type=float,default=1,help="statistical weight of a photon")
    p.add_argument("--laser_direction",nargs='+',type=float,default=[0.,0.,1.],help="unit three vector for photons direction")
    p.add_argument("--laser_position",nargs='+',type=float,default=[0.,0.,0.],help="three vector for laser position")
    p.add_argument("--laser_diffuser",nargs='+',default=('none',0),help="laser diffuser mode: (exp,sigma) or (cone, angle)")
# CorsikaGVDDataBankReader options
    p.add_argument("--corsika_GVD_DB_reader-config", is_config_file=True,default='configs/CorsikaGVDDataBankReader.cfg',help="Config for CorsikaGVDDataBankReader")
    p.add_argument('--corsika_GVD_DB_reader_input',help='Corsika GVD DataBase input file')
    p.add_argument('--corsika_GVD_DB_reader_max_records',default=0,help='Corsika GVD DataBase maximum number of readed rows')
# ToyPrimary options
    p.add_argument("--toy_primary_name", default='mu-',
                   help="set particle by name, e.g. e-, mu-, pi+, gamma")
    p.add_argument("--toy_primary_energy", default=10, 
                   help="set particle total energy in GeV")
    p.add_argument("--toy_primary_position", nargs=3, default=[0, 0, 0], 
                   help="set particle position in meters (format: x, y, z)")
    p.add_argument("--toy_primary_direction", nargs=3, default=[0, 0, 1],
                   help="set particle direction (format: dx, dy, dz))")
# Geant4 options
    p.add_argument("--g4_casc_max", type=float, default=0., 
                   help="set maximal energy to store cascade starters (as fraction of initial energy)")
    p.add_argument("--g4_enable_cherenkov", dest="g4_cherenkov", action="store_true", 
                   help="enable production of phtons in Geant4")
    p.add_argument("--g4_random_seed", type=float, default=1,
                   help="set random seed for Geant4")
    p.add_argument("--g4_detector_height", type=float, default=1360.,
                   help="set height (in meters) of cylindrical detector volume")
    p.add_argument("--g4_detector_radius", type=float, default=1000.,
                   help="set radius (in meters) of cylindrical detector volume")
    # TODO remove from here ...
    p.add_argument("--g4_particle", default='mu-',
                   help="set particle by name (Geant4 names)")
    p.add_argument("--g4_energy", nargs=2, default=[10, "GeV"], 
                   help="set particle energy (format: value, unit)")
    p.add_argument("--g4_position", nargs=4, default=[0, 0, 0, "m"], 
                   help="set particle position (format: x, y, z, unit)")
    p.add_argument("--g4_direction", nargs=3, default=[0, 0, 1],
                   help="set particle direction (format: dx, dy, dz))")
    # TODO ... to here
# particlePropagator options
#   cascadeCherenkov options
    p.add_argument("--casc_param_X0", type=float, default=0.3608, help="radiation lenght, in meters")
#   trackCherenkov options
    p.add_argument("--cherenkov_wavelengths", nargs=2, type=float, default=[350,650], 
                   help="wavelength range")
    p.add_argument("--refraction_index", type=float, default=1.34,
                   help="average refraction index for photon generators")
# ChargedPrimary options
    #p.add_argument("--charged_energy",nargs='+',type=float,default=200,help="wavelengths interval")
    p.add_argument("--charged_primary_cherenkov_waves",nargs='+',type=float,default=[350,600],help="wavelengths interval")
    p.add_argument("--charged_direction",nargs='+',type=float,default=[0.,0.,1.],help="unit three vector for charged particle direction")
    p.add_argument("--charged_position_m",nargs='+',type=float,default=[0.,0.,0.],help="three vector for charged particle position")
    p.add_argument("--charged_length_m",nargs='+',type=float,default=100,help="travel length of charged particle")

    return p
