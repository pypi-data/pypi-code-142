try:
	import igl
	from .util import *
	from .fit import *
	from .flow import *
	from .stat import *
	from .dirac import *
	from .so3 import *

except ImportError:
	print("Error: libigl not found!")
	print("Please run `conda install -c conda-forge igl`")



