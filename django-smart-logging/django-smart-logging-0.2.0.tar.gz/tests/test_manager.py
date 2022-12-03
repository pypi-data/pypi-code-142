from logging import Handler

from smart_logging.manager import LoggingConfManager


def test_manager_init(manager: LoggingConfManager):
    manager._collect_handlers()
    assert manager.handlers.names == [
        "__online__",
        "console",
        "console1",
        "console2",
        "null",
    ]
    assert len(manager.handlers.names) == len(manager.handlers.instances)
    assert {"log1", "log2", "log3", "log_null"}.issubset(manager.loggers.names)


def test_manager_get_handler(manager: LoggingConfManager):
    assert manager.get_handler("null")
    assert manager.get_handler(manager.get_handler("null"))


def test_manager_get_name(manager: LoggingConfManager):
    assert manager.get_handler("null")
    assert manager.get_handler(manager.get_handler("null"))


def test_manager_get_logger(manager: LoggingConfManager):
    assert manager.get_handler("null")
    assert manager.get_handler(manager.get_handler("null"))


def test_manager_create_mapping(manager: LoggingConfManager):
    manager.create_mapping()
    assert {"log1", "log2", "log3", "log_null", "root"}.issubset(manager.mapping.keys())


def test_manager_get_initial_config(manager: LoggingConfManager):
    cfg = manager.get_initial_config()
    assert {"log1", "log2", "log3", "log_null", "root"}.issubset(cfg.keys())


def test_manager_configure_logger(manager: LoggingConfManager):
    cfg = manager.configure_logger("log1", level="ERROR")
    assert cfg == ["log1: setting level ERROR"]
    assert manager.mapping["log1"]["active"]["level"] == "ERROR"

    cfg = manager.configure_logger("log1", propagate=True)
    assert cfg == ["log1: setting propagate True"]
    assert manager.mapping["log1"]["active"]["propagate"]


def test_manager_reset_logger(manager: LoggingConfManager):
    target = "log1"
    manager.configure_logger(target, handlers=[])
    assert manager.is_changed(target)
    assert manager.mapping[target]["active"]["handlers"] == []

    manager.reset_logger(target)
    assert not manager.is_changed(target), {
        "diff": manager.diff(target),
        "initial": manager.mapping[target]["initial"],
        "active": manager.mapping[target]["active"],
    }


def test_manager_is_changed(manager: LoggingConfManager):
    target = "log3"
    manager.reset_logger(target)
    manager.refresh()
    assert not manager.is_changed(target), {
        "diff": manager.diff(target),
        "initial": manager.mapping[target]["initial"],
        "active": manager.mapping[target]["active"],
    }
    manager.configure_logger(target, level="ERROR")
    assert manager.is_changed(target)
    assert manager.diff(target) == {"level": "DEBUG"}


def test_manager_find_handler_name_by_instance(manager: LoggingConfManager):
    lgr = manager.handlers["console1"]
    assert manager._find_handler_name_by_instance(lgr) == "console1"
    h = Handler()
    assert manager._find_handler_name_by_instance(h) is None


# def test_manager_register():
#     manager.inspect()
#     assert manager.config['log1'] == {'handlers': ['console1'], 'level': 'DEBUG', 'propagate': False}
#     assert manager.config['log2'] == {'handlers': ['console2'], 'level': 'DEBUG', 'propagate': True}
#
#
# def test_inspect_custom_handler():
#     rootlogger = logging.getLogger()
#     rootlogger.addHandler(logging.Handler())
#     manager.inspect()
#     # currentConfig.create_signature()
#     # print(111, inspect())
#     pprint(manager.config)
#     # pprint(currentConfig.idToHandler)
#     # pprint(currentConfig.nameToHandler)
