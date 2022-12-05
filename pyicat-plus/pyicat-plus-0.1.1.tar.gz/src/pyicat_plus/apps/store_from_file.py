import os
import sys
import argparse
from glob import glob
from ..client.main import IcatClient


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(description="Register stored data with ICAT")
    add_store_parameters(parser)
    args = parser.parse_args(argv[1:])
    apply_store_parameters(args)

    client = IcatClient(metadata_urls=args.metadata_urls)

    for filename in args.files:
        print("Register", filename)
        client.store_dataset_from_file(filename)


def add_store_parameters(parser):
    parser.add_argument("filter", help="File search filter")

    parser.add_argument(
        "--queue",
        dest="metadata_urls",
        action="append",
        help="ActiveMQ queue URLS. Example: bcu-mq-01.esrf.fr:61613",
        default=[],
    )


def apply_store_parameters(args):
    args.files = sorted(glob(args.filter), key=os.path.getmtime)

    if not args.metadata_urls:
        args.metadata_urls = ["bcu-mq-01.esrf.fr:61613", "bcu-mq-02.esrf.fr:61613"]


if __name__ == "__main__":
    sys.exit(main())
