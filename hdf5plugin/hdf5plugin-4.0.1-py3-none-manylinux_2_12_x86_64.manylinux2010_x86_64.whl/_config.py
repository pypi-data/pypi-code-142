from collections import namedtuple

HDF5PluginBuildConfig = namedtuple('HDF5PluginBuildConfig', ('openmp', 'native', 'sse2', 'avx2', 'cpp11', 'filter_file_extension', 'embedded_filters'))
build_config = HDF5PluginBuildConfig(**{'openmp': False, 'native': False, 'sse2': True, 'avx2': False, 'cpp11': False, 'filter_file_extension': '.so', 'embedded_filters': ('blosc', 'bshuf', 'bzip2', 'lz4', 'sz', 'zfp', 'zstd')})
