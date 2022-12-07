from argparse import Namespace
from email.policy import default
import logging
log=logging.getLogger('NTsim')
logformat='[%(name)20s ] %(levelname)8s: %(message)s'
logging.basicConfig(format=logformat)
from ntsim.utils.report_timing import report_timing

class NTsim:
    def __init__(self):
        self.geometry = None
        self.primary  = None
        self.medium   = None
        self.gEvent   = None

    def init(self,geometry=None,primary=None,medium=None) -> None:
        from ntsim.io.gEvent import gEvent
        from ntsim.io.gEventHeader import gEventHeader
        from ntsim.io.gProductionHeader import gProductionHeader
        from ntsim.io.gPrimaryHeader import gPrimaryHeader

        self.geometry = geometry
        self.primary = primary
        self.medium = medium
        self.gEvent = gEvent()
        self.gEvent.setProductionHeader(gProductionHeader())
        self.gEvent.setEventHeader(gEventHeader())
        self.gEvent.setPrimaryHeader(gPrimaryHeader())
        self.primary.set_medium(self.medium)
        self.primary.set_geometry(self.geometry)
        self.primary.set_gEvent(self.gEvent)
        self.primary.init_h5Writer()

    def configure(self,opts: Namespace) -> None:
        self.n_events = opts.n_events
        self.primary.configure(opts)
        self.geometry.configure(opts)
        self.medium.configure(opts)
        self.primary.writer.configure(opts)

    def writePrimaryHeader(self):
        self.gEvent.gPrimaryHeader.set_name(self.primary.primary_name)
        self.gEvent.gPrimaryHeader.set_track(self.primary.primary_track)
        self.primary.writer.write_primary_header(self.gEvent.gPrimaryHeader)

    def writeProductionHeader(self):
        if self.medium.model != None:
            self.gEvent.gProductionHeader.set_scattering_model_name(self.medium.model.name)
            self.gEvent.gProductionHeader.set_anisotropy(self.medium.model.g)
        self.primary.writer.write_prod_header(self.gEvent.gProductionHeader)

    def writeGeometry(self):
        self.primary.writer.write_geometry(self.geometry)

    def init_h5(self):
        self.primary.writer.init_h5()

    def close_h5(self):
        self.primary.writer.close()

    @report_timing
    def process(self):
        # yet under development
        self.init_h5()

        if opts.multithread:
            self.primary.next_multithread(self.n_events)
            return
        for ev in range(self.n_events):
            log.info("---------------------------")
            log.info(f"Event #{ev}")
            self.primary.next() # it writes the event because photons can be in bunches
            self.gEvent.gProductionHeader.n_events +=1


        self.writePrimaryHeader()
        self.writeProductionHeader()
        self.writeGeometry()
        self.close_h5()

if __name__ == '__main__':
    from ntsim.arguments import parser
    p = parser()
    opts = p.parse_args()   # using p.parse_args() here may raise errors.
    if opts.log_level == 'deepdebug':
        print("Logging level deepdebug not implemented, using DEBUG instead")
        log.setLevel(logging.getLevelName("DEBUG"))
        logging.root.setLevel(logging.getLevelName("DEBUG")) # set global logging level
    else:
        log.setLevel(logging.getLevelName(opts.log_level.upper()))
        logging.root.setLevel(logging.getLevelName(opts.log_level.upper()))  # set global logging level

    opts.multithread = eval(opts.multithread.lower().capitalize())
    log.info(p.format_values())

    simu = NTsim()
    from ntsim.Primary import getPrimary
    from ntsim.Geometry import Geometry
    from ntsim.Medium import Medium
    primary = getPrimary(opts.primary_name)
    if primary != None:
        simu.init(geometry=Geometry(),primary=primary,medium=Medium())
        simu.configure(opts)
        simu.process()
    else:
        log.info('No primary = no simulation. Consider --primary_config option')
