import logging
from importlib import import_module

log = logging.getLogger(__name__)


def getargs(parser):
    """
    Function that set argparse for mbsim

    :param parser: Subparser from mbsim to allow addon to add it's commands
    :return: function to call to allow mbsim to use addon
    :rtype: function
    """
    log.debug("Creating sim command")
    args = parser(
        name="sim",
        description="Allow user to setup simple modbus simulator. With all values set to 0",
        help="Start modbus slave simulator",
    )
    log.debug("Creating protocol command")
    protoparser = args.add_subparsers(
        title="protocol",
        dest="sim_protocol",
    )
    log.debug("Creating sim:tcp command")
    tcp = protoparser.add_parser("tcp")
    tcp.add_argument(
        "-a",
        "--address",
        action="store",
        default="",
        dest="sim_address",
        help='The address to bind too. Default is "" this binds to all addresses',
    )
    tcp.add_argument(
        "-p",
        "--port",
        action="store",
        default=502,
        dest="sim_port",
        type=int,
        help="Select the port to open for the modbus server, Default: 502",
    )
    log.debug("Creating sim:udp command")
    udp = protoparser.add_parser("udp")
    udp.add_argument(
        "-a",
        "--address",
        action="store",
        default="",
        dest="sim_address",
        help='The address to bind too. Default is "" this binds to all addresses',
    )
    udp.add_argument(
        "-p",
        "--port",
        action="store",
        default=502,
        dest="sim_port",
        help="Select the port to open for the modbus server, Default: 502",
        type=int,
    )
    log.debug("Creating sim:rtu command")
    rtu = protoparser.add_parser("rtu")
    rtu.add_argument(
        "path",
        action="store",
        default="/dev/ttyS0",
        nargs="?",
        help="The path to device",
    )
    rtu.add_argument(
        "-b",
        "--buadrate",
        action="store",
        type=int,
        default=19200,
        dest="sim_buad",
        help="The buadrate. Default: 19200",
    )
    rtu.add_argument(
        "--bytesize",
        action="store",
        default=8,
        dest="sim_byte",
        type=int,
        help="The bytesize",
    )
    rtu.add_argument(
        "-s",
        "--stopbits",
        action="store",
        default=1,
        type=int,
        dest="sim_stopbits",
        help="Nuber of stops",
    )
    rtu.add_argument(
        "-p",
        "--parity",
        action="store",
        default="N",
        choices=["N", "O", "E"],
        dest="sim_parity",
        type=str,
        help="The parity. Default: N",
    )
    rtu.add_argument(
        "-t",
        "--timeout",
        action="store",
        default=0,
        type=int,
        dest="sim_timeout",
        help="Timeout",
    )
    rtu.add_argument(
        "-x",
        "--xonxoff",
        action="store",
        default=0,
        choices=[0, 1],
        dest="sim_xonxoff",
        type=int,
        help="Set xonxoff, software flow control",
    )
    rtu.add_argument(
        "-r",
        "--rtscts",
        action="store",
        default=0,
        choices=[0, 1],
        dest="sim_rtscts",
        type=int,
        help="Set rtscts, hardware flow control",
    )

    return run


def run(args):
    """
    Allow sim to run modbus servers

    :param args: Namespace from argparser
    :type args: Namespace
    """
    log.debug("Loading mbsim.core.server")
    mb = import_module("mbsim.core.server")
    if args.sim_protocol in ("tcp", "udp"):
        mb.start(
            args.sim_protocol,
            address=(args.sim_address, args.sim_port),
        )
    elif args.sim_protocol == "rtu":
        mb.start(
            args.sim_protocol,
            port=args.path,
            buadrate=args.sim_buad,
            bytesize=args.sim_byte,
            stopbits=args.sim_stopbits,
            parity=args.sim_parity,
            timeout=args.sim_timeout,
            xonxoff=args.sim_xonxoff,
            rtscts=args.sim_rtscts,
        )
    else:
        raise RuntimeError("Did not find accepted protocol")
