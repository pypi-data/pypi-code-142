"""
A Modbus Simulator
"""
import argparse
import logging

try:
    from importlib.metadata import entry_points
except ImportError:
    from importlib_metadata import entry_points

log = logging.getLogger(__name__)


class EntryPoints(object):
    """
    A wrapper for entry point for when it returns a dict
    """

    def __init__(self, eps):
        """
        Init wrapper
        """
        self.eps = eps

    def select(self, name=None, group=None):
        """
        If entry_points return a dict this will wrap the dict
        """
        if name:
            for vals in self.eps.values():
                for val in vals:
                    if val.name == name:
                        return val
        elif group:
            return self.eps.get(group, {})
        return self.eps


def main(pargs=None):
    """
    The main function to start the mbsim
    """
    log.debug("mbsim is Starting")
    parser = argparse.ArgumentParser(prog="mbsim", description="A simple Modbus Slave Simulator")
    parser.add_argument(
        "-l",
        "--log",
        action="store",
        dest="log",
        help="set log level",
        default="INFO",
        choices=["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"],
    )
    entrys = entry_points()
    if isinstance(entrys, dict):
        entrys = EntryPoints(entrys)
    cmds = {ep.name: ep for ep in entrys.select(group="mbsim_command")}
    cmdparser = parser.add_subparsers(
        title="Commands",
        description="Command for mbsim to execute, if omitted tcp modbus server will be started on port 502",
        dest="cmd",
    )

    mods = {}
    for name, ep in cmds.items():
        log.debug("Loading %s argparser", name)
        mods[name] = ep.load()(cmdparser.add_parser)
        log.debug("Loaded argparser for %s", name)

    log.debug("Reading command line arguments")
    args = parser.parse_args(pargs)

    logging.basicConfig(level=getattr(logging, args.log))
    log.setLevel(getattr(logging, args.log))
    log.debug("Changed log level: %s", args.log)

    log.debug("Loading addon %s", getattr(args, "cmd", "sim"))
    mods.get(args.cmd)(args)


if __name__ == "__main__":
    main()
