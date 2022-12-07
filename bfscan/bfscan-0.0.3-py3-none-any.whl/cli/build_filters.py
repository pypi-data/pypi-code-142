from Bio import SeqIO
from bfscan.logo import logo
from bfscan.filter import BFScanFilter
from bfscan.utils import read_sequence_file
import argparse
import os

def main():
    print(logo)
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', nargs='*', metavar='FASTAFILE', required=True, help='Input fasta file')
    parser.add_argument('-k', '--k-size', type=int, default=17, help='Input k size')
    parser.add_argument('-o', '--output', required=True, help='Output filter file')
    parser.add_argument('-m', '--max-elements', type=int, default=50_000_000, help='Input max elements')
    parser.add_argument('-e', '--error', type=float, default=0.0001, help ='Input error rate') 
    arguments = parser.parse_args()

    bfscan_filter = BFScanFilter(arguments.k_size, arguments.max_elements, arguments.error)

    for file in arguments.input:

        file_basename_name = os.path.splitext(os.path.basename(file).strip(".gz"))[0]
        records = (str(record.seq) for record in read_sequence_file(file))
        bfscan_filter.partial_fit(records, class_name=file_basename_name)
        print(f"filter for '{file}' added ...")
        
    bfscan_filter.save(arguments.output)
        
if __name__ == '__main__':
    main()
    



