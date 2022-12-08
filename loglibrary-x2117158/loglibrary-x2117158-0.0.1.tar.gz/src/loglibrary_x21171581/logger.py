from __future__ import annotations


from .level import Level
from .notifier import Listenable, StateNotifier
from .log_record import LogRecord


class imdict(dict):
    def __hash__(self):
        return id(self)

    def _immutable(self, *args, **kws):
        raise TypeError('object is immutable')

    __setitem__ = _immutable
    __delitem__ = _immutable
    clear = _immutable
    update = _immutable
    setdefault = _immutable
    pop = _immutable
    popitem = _immutable


class Logger(object):
    __create_key = object()
    __loggers = dict()

    hierarchical_logging_enabled = False
    default_level = Level.INFO

    def __init__(self, create_key=None, name: str = None, parent: Logger = None, children: dict = None) -> None:
        assert(create_key == Logger.__create_key), \
            "Logger must be created using Logger.create"
        self.name = name
        self.parent = parent
        self.__children = children
        self.children = imdict(children)
        self.__level = None
        if (parent == None):
            self.__level = Logger.default_level
        else:
            parent.__children[name] = self
        self.__controller: StateNotifier = None

    @staticmethod
    def root() -> Logger:
        return Logger.create('')

    @property
    def full_name(self):
        if (self.parent != None and self.parent.name != ''):
            return f'{self.parent.full_name}.{self.name}'
        return self.name

    @classmethod
    def create(cls, name='') -> Logger:
        if name not in Logger.__loggers:
            Logger.__loggers[name] = Logger.__named(cls.__create_key, name)
        return Logger.__loggers[name]

    def child(self, name) -> Logger:
        return Logger.create(f'{self.full_name}.{name}')

    @staticmethod
    def __named(create_key, name: str):
        index_of_dot = name.find('.')
        if (index_of_dot == 0):
            raise NameError("name shouldn't start with a '.'")
        if (name != '' and index_of_dot == len(name) - 1):
            raise NameError("name shouldn't end with a '.'")
        dot = name.rfind('.')
        parent: Logger = None
        this_name: str = None
        if (dot == -1):
            if (name != ''):
                parent = Logger.create('')
            this_name = name
        else:
            parent = Logger.create(name[0: dot])
            this_name = name[dot + 1:]
        return Logger(create_key, this_name, parent, dict())

    @property
    def level(self) -> Level:
        effective_level: Level
        if (self.parent == None):
            effective_level = self.__level
        else:
            if (self.__level != None):
                effective_level = self.__level
            elif not Logger.hierarchical_logging_enabled:
                effective_level = Logger.root().__level
            else:
                effective_level = self.parent.level
        return effective_level

    @level.setter
    def level(self, value: Level):
        if (not Logger.hierarchical_logging_enabled and self.parent != None):
            raise ValueError(
                "unsupported: Please set \"Logger.hierarchical_logging_enabled\" to true if you want to change the level on a non-root logger.")
        if (self.parent == None and value == None):
            raise ValueError(
                "unsupported: Cannot set the level to `null` on a logger with no parent.")
        self.__level = value

    @property
    def on_record(self) -> Listenable:
        if (self.__controller == None):
            self.__controller = StateNotifier()
        return self.__controller

    def clear_listeners(self):
        if (Logger.hierarchical_logging_enabled or self.parent == None):
            if (self.__controller != None):
                self.__controller.dispose()
        else:
            Logger.root().clear_listeners()

    def is_loggable(self, value: Level) -> bool:
        return value >= self.level

    def __publish(self, record: LogRecord):
        if (self.__controller != None):
            self.__controller.value = record

    def log(self, logLevel: Level, message, error=None, stackTrace=None):
        object = None
        if (self.is_loggable(logLevel)):
            if callable(message):
                message = message()
            msg: str
            if (isinstance(message, str)):
                msg = message
            else:
                msg = str(message)
                object = message
            record = LogRecord(logLevel, msg, self.full_name,
                               error, stackTrace, object,)
            if (self.parent == None):
                self.__publish(record)
            elif (not Logger.hierarchical_logging_enabled):
                Logger.root().__publish(record)
            else:
                target: Logger = self
                while (target != None):
                    target.__publish(record)
                    target = target.parent

    def finest(self, message, error=None, stackTrace=None):
        return self.log(Level.FINEST, message, error, stackTrace)

    def finer(self, message, error=None, stackTrace=None):
        return self.log(Level.FINER, message, error, stackTrace)

    def fine(self, message, error=None, stackTrace=None):
        return self.log(Level.FINE, message, error, stackTrace)

    def config(self, message, error=None, stackTrace=None):
        return self.log(Level.CONFIG, message, error, stackTrace)

    def info(self, message, error=None, stackTrace=None):
        return self.log(Level.INFO, message, error, stackTrace)

    def warning(self, message, error=None, stackTrace=None):
        return self.log(Level.WARNING, message, error, stackTrace)

    def severe(self, message, error=None, stackTrace=None):
        return self.log(Level.SEVERE, message, error, stackTrace)

    def shout(self, message, error=None, stackTrace=None):
        return self.log(Level.SHOUT, message, error, stackTrace)
