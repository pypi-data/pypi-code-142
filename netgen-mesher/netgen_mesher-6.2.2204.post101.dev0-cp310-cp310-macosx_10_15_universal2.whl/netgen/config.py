def _cmake_to_bool(s):
    return s.upper() not in ['', '0','FALSE','OFF','N','NO','IGNORE','NOTFOUND']

is_python_package    = _cmake_to_bool("TRUE")

BUILD_FOR_CONDA     = _cmake_to_bool("ON")
BUILD_STUB_FILES    = _cmake_to_bool("OFF")
CHECK_RANGE         = _cmake_to_bool("OFF")
DEBUG_LOG           = _cmake_to_bool("OFF")
ENABLE_CPP_CORE_GUIDELINES_CHECK  = _cmake_to_bool("OFF")
ENABLE_UNIT_TESTS   = _cmake_to_bool("OFF")
INSTALL_PROFILES    = _cmake_to_bool("OFF")
INTEL_MIC           = _cmake_to_bool("OFF")
TRACE_MEMORY        = _cmake_to_bool("OFF")
USE_CCACHE          = _cmake_to_bool("ON")
USE_CGNS            = _cmake_to_bool("OFF")
USE_GUI             = _cmake_to_bool("ON")
USE_INTERNAL_TCL    = _cmake_to_bool("ON")
USE_JPEG            = _cmake_to_bool("OFF")
USE_MPEG            = _cmake_to_bool("OFF")
USE_MPI             = _cmake_to_bool("OFF")
USE_MPI4PY          = _cmake_to_bool("ON")
USE_NATIVE_ARCH     = _cmake_to_bool("OFF")
USE_NUMA            = _cmake_to_bool("OFF")
USE_OCC             = _cmake_to_bool("ON")
USE_PYTHON          = _cmake_to_bool("ON")
USE_SPDLOG          = _cmake_to_bool("OFF")

CMAKE_INSTALL_PREFIX  = "/Users/gitlab-runner/builds/builds/rL7WHzyj/0/ngsolve/netgen/_skbuild/macosx-10.15-universal2-3.10/cmake-install"
NG_INSTALL_DIR_PYTHON   = "."
NG_INSTALL_DIR_BIN      = "bin"
NG_INSTALL_DIR_LIB      = "netgen"
NG_INSTALL_DIR_INCLUDE  = "netgen/include"
NG_INSTALL_DIR_CMAKE    = "netgen/cmake"
NG_INSTALL_DIR_RES      = "share"

NETGEN_PYTHON_RPATH_BIN = "bin"
NETGEN_PYTHON_RPATH     = "netgen"
NETGEN_PYTHON_PACKAGE_NAME = "netgen-mesher"

NG_COMPILE_FLAGS           = "-Xarch_x86_64|-march=core-avx2"
ngcore_compile_options     = "-Xarch_x86_64;-march=core-avx2"
ngcore_compile_definitions = "NETGEN_PYTHON;NG_PYTHON"

NETGEN_VERSION = "6.2.2204-101-g0a8bef49"
NETGEN_VERSION_GIT = "v6.2.2204-101-g0a8bef49"
NETGEN_VERSION_PYTHON = "6.2.2204.post101.dev"

NETGEN_VERSION_MAJOR = "6"
NETGEN_VERSION_MINOR = "2"
NETGEN_VERSION_TWEAK = "101"
NETGEN_VERSION_PATCH = "2204"
NETGEN_VERSION_HASH = "g0a8bef49"

version = NETGEN_VERSION_GIT
