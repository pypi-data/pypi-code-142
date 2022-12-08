import os
import sys
import pandas as pd
import numpy as np
from docopt import docopt
from  multiprocessing import Pool
from .utils import comp2domins_by_twtest, loadtads, visualization
import warnings
warnings.filterwarnings('ignore')

import matplotlib
matplotlib.use('Agg')


