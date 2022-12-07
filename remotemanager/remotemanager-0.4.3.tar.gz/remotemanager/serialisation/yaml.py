import yaml

from remotemanager.utils import ensure_filetype
from remotemanager.serialisation.serial import serial


class serialyaml(serial):
    """
    subclass of serial, implementing yaml methods
    """

    def dump(self, obj, file):
        file = ensure_filetype(file, self.extension)
        with open(file, 'w+') as ofile:
            yaml.dump(obj, ofile)

    def load(self, file):
        file = ensure_filetype(file, self.extension)
        with open(file, 'r') as ofile:
            data = yaml.safe_load(ofile)
        return data

    @property
    def extension(self):
        return ".yaml"

    @property
    def importstring(self):
        return "import yaml"

    @property
    def callstring(self):
        return "yaml"

    @property
    def dumpstring(self) -> str:
        return "dump"

    @property
    def loadstring(self) -> str:
        return "safe_load"

    def dumpfunc(self) -> str:
        lines = ['\ndef dump(obj, file):',
                 f'\t{self.importstring}',
                 f'\tif isinstance(obj, (set, tuple)):',
                 f'\t\tobj = list(obj)',
                 f'\tif not file.endswith("{self.extension}"):',
                 f'\t\tfile = file + "{self.extension}"',
                 f'\twith open(file, "{self.write_mode}") as o:',
                 f'\t\t{self.callstring}.{self.dumpstring}(obj, o)']

        return '\n'.join(lines)
