from Bio import SeqIO, bgzf
from .util import _open
import os

def fastq(input = None, output = None, unique = None):
    """fastq subcommand
    Paramters
    ---------

    input : str
        output file name, auto detects .gz
    output : str
        output file name, auto detects .gz
    unique : str
        output unique fastq records by record ID

    """

    args = list(locals().keys())

    local = locals()
    if all(bool(local[key]) is not True for key in args): # use True since args can be either None or False
        print("scutls fastq: warning: use 'scutls fastq -h' for usage")

    # make fastq file unique:
    if unique:
        print("Saving to " + output + " ...")
        
        if not os.path.dirname(output) == "":
            os.makedirs(os.path.dirname(output), exist_ok=True)
        with _open(input) as f:
            unique_records = {}
            for record in SeqIO.parse(f, 'fastq'):
                if record.name not in unique_records:
                    unique_records[record.name] = record

            if output.endswith(".gz"):
                with bgzf.BgzfWriter(output, "wb") as outgz:
                    SeqIO.write(sequences = unique_records.values(), handle = outgz, format="fastq")
            else:
                SeqIO.write(unique_records.values(), output, "fastq")

        print("Done!")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type = str)
    parser.add_argument('--output', '-o', type = str)
    parser.add_argument('--unique', '-u', action='store_true')

    args = parser.parse_args()
    fastq(args.input, args.output, args.unique)

if __name__ == "__main__":
    main()
