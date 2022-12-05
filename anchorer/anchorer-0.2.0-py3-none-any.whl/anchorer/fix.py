import os
from os.path import realpath
import sys


def main():
    os.chdir(realpath(os.getcwd()))

    # resolve all paths under sys
    sys.path[:] = [realpath(p) for p in sys.path]
    sys.prefix = realpath(sys.prefix)
    sys.base_prefix = realpath(sys.base_prefix)
    sys.base_exec_prefix = realpath(sys.base_exec_prefix)
    sys.exec_prefix = realpath(sys.exec_prefix)
    sys.executable = realpath(sys.executable)
    if sys._home is not None:
        sys._home = realpath(sys._home)
    if hasattr('sys', '_base_executable'):
        # absent in python3.6
        sys._base_executable = realpath(sys._base_executable)

    # resolve all the module filenames to at least help debugging
    for name, module in sys.modules.items():
        # not all modules (e.g. builtins) do not have this attribute
        path = getattr(module, "__file__", None)
        if path is None:
            continue
        module.__file__ = realpath(path)

    # an example run (can ignore the pytest one)
    # [<_pytest.assertion.rewrite.AssertionRewritingHook object at 0x7fe50db08160>,
    #  <_distutils_hack.DistutilsMetaFinder object at 0x7fe5109ee340>,
    #  <_virtualenv._Finder object at 0x7fe510a60550>,
    #  <class '_frozen_importlib.BuiltinImporter'>,
    #  <class '_frozen_importlib.FrozenImporter'>,
    #  <class '_frozen_importlib_external.PathFinder'>,
    #  <pkg_resources.extern.VendorImporter object at 0x7fe50ff9a2e0>]

    for finder in sys.meta_path:
        # TODO: check which of these need handling, e.g. DistuilsMetaFinder, PathFinder, FrozenImporter, and VendorImporter
        # pkg_resources.extern.VendorImporter
        if type(finder).__name__ == 'VendorImporter':
            pass
        # TODO: see if invalidate_caches() is required, as things like _virtualenv._Finder and distutils_hack.DistutilsMetaFinder report no vars
        # ignoring _pytest.assertion.rewrite.AssertionRewritingHook
    # TODO: work out where the '' is added to sys.PATH

    import importlib

    importlib.invalidate_caches()


# from _distutils_hack import DistutilsMetaFinder
# from _virtualenv import _Finder # looks ok, probably don't need to worry
# from _frozen_importlib import BuiltinImporter
# from _frozen_importlib import FrozenImporter
# from _frozen_importlib_external import PathFinder
# from pkg_resources.extern import VendorImporter # finea

# when this module is copied into site-packages by the virtualenvwrapper plugin, it will have this name
# when imported using the .pth file, so fix the paths at that point
if __name__ == '__anchorer':
    main()
