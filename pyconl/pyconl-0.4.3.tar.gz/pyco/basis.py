import pickle

class Singleton(type):
    """
    Metaclass om een normale klasse te tronsformeren naar een singleton.
    Ieder nieuwe instantie van klasse wordt genegeerd en er wordt altijd
    de eerste instantie (object) gebruikt.

    class MyClass(BaseClass, metaclass = Singleton):
        pass
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ObjectTeller(metaclass = Singleton):
    """
    ObjectTeller zorgt ervoor dat over hele applicatie objecten een nieuw
    oplopend nummer krijgen. Hierdoor kan achteraf gekeken worden welk object
    eerder was aangemaakt.

    import pyco.basis as pycob

    teller = pycob.ObjectTeller()
    self.object_nummer = teller.object_nummer
    """

    _object_teller = 0

    def __init__(self):
        pass

    @property
    def object_nummer(self):
        self._object_teller += 1
        return self._object_teller

    
class BasisObject(object):
    """Deze klasse dient als onderlegger voor alle klassen."""

    def __init__(self):
        self._documentatie = ''

        # ObjectTeller zorgt ervoor dat over hele applicatie objecten een nieuw
        # oplopend nummer krijgen. Hierdoor kan achteraf gekeken worden welk object
        # eerder was aangemaakt.
        teller = ObjectTeller()
        self._object_nummer = teller.object_nummer
        
    @classmethod
    def van_bestand(cls, pad):
        """Object laden vanuit bestand."""
        bestand = open(pad, 'rb')
        self = pickle.load(bestand)
        bestand.close()
        return self
    
    def naar_bestand(self, pad):
        """Object opslaan als bestand."""
        bestand = open(pad, 'wb')
        pickle.dump(self, bestand)
        bestand.close()

    def __rshift__(self, other:str):
        """Documentatie toevoegen.

        Object() >> "Documentatie."
        """
        self._documentatie = other.strip() if isinstance(other, str) else ''
        return self

    @classmethod
    def print_help(cls):
        name = cls.__name__
        underline = '+--' + len(name)*'-' + '--+'
        docstr = ''
        for line in cls.__doc__.strip().split('\n'):
            line = line[4:] if line[:4] == '    ' else line
            docstr += line + '\n'
        print(f"\n{underline}\n|  {name}  |\n{underline}\n\n{docstr}")
