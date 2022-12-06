from collections import namedtuple

HDF5PluginBuildConfig = namedtuple('HDF5PluginBuildConfig', ('openmp', 'native', 'sse2', 'avx2', 'cpp11', 'filter_file_extension', 'embedded_filters'))
build_config = HDF5PluginBuildConfig(**{'openmp': False, 'native': False, 'sse2': True, 'avx2': False, 'cpp11': True, 'filter_file_extension': '.dll', 'embedded_filters': ('blosc', 'bshuf', 'bzip2', 'fcidecomp', 'lz4', 'sz', 'zfp', 'zstd')})
