import numpy as np
import logging
log = logging.getLogger('phTransformer')

class phTransformer:
    # transform photons: shift and rotate
    def __init__(self):
        self.module_type = "propagator"
        log.info("initialized")

    def configure(self, opts):
        log.info("configured")
