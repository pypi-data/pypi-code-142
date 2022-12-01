import inspect
from types import ModuleType


INVOKING_MODULE_FRAME_IDX = 2


class ModuleFunctionalityWrapper:
    """
    Python versions < 3.7 hack (modules cannot implement __getattr__ and __dir__)
    """

    def __init__(self, functionality: object, module: ModuleType = None):
        self._module = module if module is not None else self._get_invoking_module()
        self._functionality = functionality

    def _get_invoking_module(self) -> ModuleType:
        """
        Current call stack illustration:
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

        Fr.#0  ║  self._get_invoking_module()          ║ (Current)
        ‾‾‾‾‾  ╠═══════════════════════════════════════╣
        Fr.#1  ║  self.__init__()                      ║
        ‾‾‾‾‾  ╠═══════════════════════════════════════╣
        Fr.#2  ║  module we're actually interested in  ║ (INVOKING_MODULE_FRAME_IDX)
        ‾‾‾‾‾  ╠═══════════════════════════════════════╣
         ...   ║  ...                                  ║
               ╚═══════════════════════════════════════╝
        """
        invoking_frame = inspect.stack()[INVOKING_MODULE_FRAME_IDX]
        invoking_module = inspect.getmodule(invoking_frame[0])
        return invoking_module

    def __getattr__(self, name):
        try:
            return getattr(self._functionality, name)
        except AttributeError:
            return getattr(self._module, name)
