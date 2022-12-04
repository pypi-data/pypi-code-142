import sys
import pkg_resources
from argparse import ArgumentParser
from scutls import cli
from scutls.__init__ import __version__

parser = ArgumentParser(description = "Single-cell sequencing utility tools")
parser.add_argument("-v", "--version", action="version", version="%(prog)s " + str(__version__))

subparsers = parser.add_subparsers(title = "Subcommands")

# subcommand: download
parser_download = subparsers.add_parser(
    "download", description = "download genome/annotation file from UCSC/ENSEMBL")
parser_download.add_argument(
    "-o", "--outdir",
    help = "output directory, default to ./",
    required = False, type = str, default = "./"
)
parser_download.add_argument(
    "-lgu",
    "--list_genome_ucsc",
    help="list all available UCSC genome names",
    required = False,
    default = False,
    action='store_true' # quick hack to skip requred input: https://stackoverflow.com/questions/59363298/argparse-expected-one-argument
)
parser_download.add_argument(
    "-gu",
    "--genome_ucsc",
    help="a UCSC genome name to download",
    required = False,
    default = None,
    type = str
)
parser_download.add_argument(
    "-lge",
    "--list_genome_ensembl",
    help="list all available ENSEMBL genome names",
    required = False,
    default = False,
    action='store_true' # quick hack to skip requred input: https://stackoverflow.com/questions/59363298/argparse-expected-one-argument
)
parser_download.add_argument(
    "-ge",
    "--genome_ensembl",
    help="an ENSEMBL genome name to download",
    required = False,
    default = None,
    type = str
)
parser_download.add_argument(
    "-au",
    "--annotation_ucsc",
    help="an UCSC genome name to download annotation file",
    required = False,
    default = None,
    type = str
)
parser_download.add_argument(
    "-ae",
    "--annotation_ensembl",
    help="an ENSEMBL genome name to download annotation file",
    required = False,
    default = None,
    type = str
)
parser_download.add_argument(
    "-er",
    "--ensembl_release",
    help="list all ENSEMBL releases and the one in use",
    required = False,
    default = False,
    action='store_true' # quick hack to skip requred input: https://stackoverflow.com/questions/59363298/argparse-expected-one-argument
)
parser_download.add_argument(
    "-eru",
    "--ensembl_release_use",
    help="update ENSEMBL release in use, input 4 release numbers separated by comma (vetebrate, plants, fungi, metazoa), e.g. -eru '104, 51, 51, 51'",
    required = False,
    default = None,
    type = str
)
parser_download.add_argument(
    "-erup",
    "--ensembl_release_update",
    help="update ENSEMBL releases",
    required = False,
    default = False,
    action='store_true' # quick hack to skip requred input: https://stackoverflow.com/questions/59363298/argparse-expected-one-argument
)
parser_download.set_defaults(func=cli.run_download)

# subcommand: fastq
parser_fastq = subparsers.add_parser(
    "fastq", description = "process fastq files")
parser_fastq.add_argument(
    "-i", "--input",
    help = "input fastq, can end with .gz",
    required = True, type = str, default = None
)
parser_fastq.add_argument(
    "-o", "--output",
    help = "output fastq name, can end with .gz",
    required = True, type = str, default = None
)
parser_fastq.add_argument(
    "-u", "--unique",
    help = "keep unique records (by sequence ID) in fastq file",
    required = False, default = False, action='store_true'
)
parser_fastq.set_defaults(func=cli.run_fastq)


def main():
    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()
    else:
        args = parser.parse_args()
        args.func(args) # parse the args and call whatever function was selected

if __name__ == "__main__":
    main()
