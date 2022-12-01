"""Get info about BMP sessions on a Route Views collector.
"""
import logging
import socket
import sys

import configargparse
import uologging

import routeviews.exec
import routeviews.influx
import routeviews.parse
from routeviews.frr.bmp import BMPConnection

logger = logging.getLogger(__name__)
trace = uologging.trace(logger, capture_args=False)


@trace
def main(args):
    command = ['vtysh', '-c', 'show bmp']
    if args.sudo:
        command.insert(0, 'sudo')
    result = routeviews.exec.run(command)
    results = routeviews.parse.template_parse(result, 'bmp_summary')
    results = [BMPConnection.from_textfsm(data) for data in results]
    if args.influxdb:
        for result in results:
            print(
                generate_influxdb_line(
                    socket.gethostname(),
                    result
                )
            )
    else:
        if not results:
            print('No BMP Connections')
        else:
            for connection in results:
                print(connection.pprint())


def generate_influxdb_line(collector: str, connection_stats: BMPConnection,
                           measurement='bmp_edge'):
    """Generate a InfluxDB Line Protocol line.

    Args:
        hostname (str): Name of this collector that is sending data.
        measurement (str, optional): Name of measurement in InfluxDB. 
        Defaults to 'bmp_edge'.

    Returns:
        str: Single long string containing the vals we want to track.
    """
    return routeviews.influx.measurement_line(
        name=measurement,
        fields={
            'uptime_sec': connection_stats.uptime_seconds,
            'byte_queue': connection_stats.byte_queue,
            'byte_queue_kernel': connection_stats.byte_queue_kernel,
        },
        tags={
            'collector': collector,
            'bmp_collector': connection_stats.bmp_collector,
        },
    )


def parse_args(argv):
    parser = configargparse.ArgumentParser(description=__doc__)
    uologging.add_verbosity_flag(parser)
    parser.add_argument(
        '--influxdb',
        action='store_true',
        help='Produce a measurement as InfluxDB Line Protocol.'
    )
    parser.add_argument(
        '--sudo', '-b',  # '-b' is shorthand borrowed from Ansible CLI tool
        action='store_true',
        help='Use `sudo` when running underlying command.'
    )
    args = parser.parse_args(argv[1:])
    return args


def run_main():
    _main(sys.argv)


def _main(argv):
    """Parse args, set up logging, then call the inner 'main' function. 
    """
    package_name = __name__.split('.')[0]
    uologging.init_console(package_name)
    args = parse_args(argv)
    uologging.set_logging_verbosity(args.verbosity_flag, package_name)
    main(args)


if __name__ == '__main__':
    logger.warning(f'Invoked as script, not using entry point {__file__}')
    run_main()
