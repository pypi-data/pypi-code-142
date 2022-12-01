from remotemanager.utils import ensure_filetype
from remotemanager.storage.sendablemixin import SendableMixin


class serial(SendableMixin):

    """
    Baseclass for holding serialisation methods. Subclass this class when
    implementing new serialisation methods
    """

    def __init__(self):
        pass

    def dump(self, obj, file: str) -> None:
        """
        Dumps object `obj` to file `file`

        Args:
            obj:
                object to be dumped
            file (str):
                filepath to dump to

        Returns:
            None
        """
        raise NotImplementedError

    def load(self, file: str):
        """
        Loads previously dumped data from file `file`

        Args:
            file (str):
                filepath to load

        Returns:
            Stored object
        """
        raise NotImplementedError

    @property
    def extension(self) -> str:
        """
        Returns (str):
            intended file extension
        """
        raise NotImplementedError

    @property
    def importstring(self) -> str:
        """
        Returns (str):
            Module name to import.
            See subclasses for examples
        """
        raise NotImplementedError

    @property
    def callstring(self) -> str:
        """
        Returns (str):
            Intended string for calling this module's dump.
            See subclasses for examples
        """
        raise NotImplementedError

    @property
    def bytes(self):
        """
        Set to True if serialiser requires open(..., 'wb')
        """
        return False

    @property
    def write_mode(self):
        """
        Mode for writing to dumped files.
        """
        if self.bytes:
            return 'wb+'
        return 'w+'

    @property
    def read_mode(self):
        """
        Mode for reading dumped files.
        """
        if self.bytes:
            return 'rb'
        return 'r'

    @property
    def loadstring(self) -> str:
        return "load"

    @property
    def dumpstring(self) -> str:
        return "dump"

    def dumpfunc(self) -> str:
        lines = ['\ndef dump(obj, file):',
                 f'\t{self.importstring}',
                 f'\tif not file.endswith("{self.extension}"):',
                 f'\t\tfile = file + "{self.extension}"',
                 f'\twith open(file, "{self.write_mode}") as o:',
                 f'\t\t{self.callstring}.{self.dumpstring}(obj, o)']

        return '\n'.join(lines)

    def loadfunc(self) -> str:
        lines = ['\ndef load(file):',
                 f'\t{self.importstring}',
                 f'\tif not file.endswith("{self.extension}"):',
                 f'\t\tfile = file + "{self.extension}"',
                 f'\twith open(file, "{self.read_mode}") as o:',
                 f'\t\treturn {self.callstring}.{self.loadstring}(o)']

        return '\n'.join(lines)
