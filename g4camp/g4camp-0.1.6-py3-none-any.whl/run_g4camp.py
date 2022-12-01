from g4camp.g4camp import g4camp
import time
import numpy as np
import h5py
import sys
import configargparse
import logging

log = logging.getLogger('run_g4camp')
logformat='[%(name)12s ] %(levelname)8s: %(message)s'
logging.basicConfig(format=logformat)

def report_timing(func):
    def func_wrapper(*args, **kwargs):
        tic = time.time()
        result = func(*args, **kwargs)
        toc = time.time()
        dt = toc - tic
        log .info(f'{func.__name__}'.ljust(40)+f'{dt:6.3f} seconds'.rjust(30))
        return result
    return func_wrapper


def parse_arguments():
    p = configargparse.get_argument_parser()
    p.add_argument('-n', default=100, help="number of events")
    p.add_argument('-o', default='output.h5', help="output file name")
    p.add_argument('--enable_optics', help="enable optics", action='store_true')
    p.add_argument('-p', '--primary-generator', default='gun', choices=('gun', 'gps'), help="type of primary generator type")
    p.add_argument('--gps_macro', default='muons.mac', help="macro files with Geant4 GPS commands to congigure particle source")
    p.add_argument('--skip_min', default=0.002, help="minimal of particle energy to skip")
    p.add_argument('--skip_max', default=0.01, help="maximal of particle energy to skip")
    p.add_argument('--random_seed', default=1, help="random seed")
    p.add_argument('--photon_suppression', default=10, help="photon suppression factor")
    p.add_argument('-l', '--log-level', choices=('deepdebug', 'debug', 'info', 'warning', 'error', 'critical'), default='info', help='logging level')

    opts = p.parse_args()
    #
    log.setLevel(opts.log_level.upper())
    log.info("----------")
    log.info(p.format_help())
    log.info("----------")
    log.info(p.format_values())    # useful for logging where different settings came from
    return opts


@report_timing
def run(app, n_events=10, ofname="output.h5"):
    h5file = h5py.File(ofname, "w")  # create empty file
    h5file.close()
    for ievt, data in enumerate(app.run(n_events)):
        h5file = h5py.File(ofname, "a")
        g = h5file.create_group(f"event_{ievt}")
        g.create_dataset('photons', data = data.photon_cloud)
        vpositions = [vertex[0] for vertex in data.vertices]
        vparticles = [vertex[2][0] for vertex in data.vertices]
        g.create_dataset('vertex_positions', data = vpositions)
        g.create_dataset('vertex_particles', data = vparticles)
        #g.create_dataset('tracks', data = data.tracks)
        g.create_dataset('tracks', 
                          data = np.array( [tuple(row) for row in data.tracks], 
                                           dtype = [('uid', float), ('pdgid', float), 
                                                    ('x_m', float), ('y_m', float), ('z_m', float),
                                                    ('t_ns', float),('E_GeV', float)]) 
                        )
        h5file.close()
        #log.info(f" Event #{ievt}/{n_events}")
        log.info(f"   Number of vertices:     {len(data.vertices)}")
        log.info(f"   Number of tracks:       {len(np.unique(data.tracks[:,0]))}")
        log.info(f"   Number of track points: {len(data.tracks)}")
        log.info(f"   Number of photons:      {len(data.photon_cloud)}")
        db = app.data_buffer
        #log.info(f"   Number of vertices / tracks points / photons : {len(db.vertices):6.0f} / {len(db.tracks):6.0f} / {len(db.photon_cloud):6.0f}")
        log.info(" ")


def main():
    opts = parse_arguments()
    optics = opts.enable_optics
    #
    if opts.primary_generator == 'gun':
        gun_args = {'particle': 'mu-', 
                    'energy_GeV': 200, 
                    'position_m': [0,0,0],
                    'direction': [0,0,1]}
        app = g4camp(optics=optics, primary_generator='gun', gun_args=gun_args)
    elif opts.primary_generator == 'gps':
        app = g4camp(optics=optics, primary_generator='gps')
        app.setGPSMacro(opts.gps_macro)
    else:
        log.error(f"Wrong primary type '{opts.primary_generator}'")
    app.log = log
    app.setRandomSeed(int(opts.random_seed))
    app.setSkipMinMax(float(opts.skip_min), float(opts.skip_max))
    app.setPhotonSuppressionFactor(float(opts.photon_suppression))
    app.configure()
    run(app, n_events=int(opts.n), ofname=opts.o)


if __name__ == "__main__":
    main()

