from Bio import SeqIO
from bfscan.filter import BFScanFilter
from bfscan.model import BFScanModel
from bfscan.utils import read_sequence_file
from bfscan.logo import logo
from sklearn.ensemble import ExtraTreesClassifier
import argparse
import time

def main():
    print(logo)
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='Input fasta/fastq file')
    parser.add_argument('-m', '--model', required=True, help='Trained model')
    parser.add_argument('-o', '--output', required=True, help='Output file prefix')
    parser.add_argument('-F', '--output-format', default='fasta', choices=['fasta', 'fastq'], help='Output format')
    arguments = parser.parse_args()

    bfscan_model  = BFScanModel.load(arguments.model)
    records = read_sequence_file(arguments.input)

    writers = {}
    for class_name in bfscan_model.filter.classes:
        writers[class_name] = open(f"{arguments.output}_{class_name}.fasta", "w")
    
    start_time = time.time()

    for r, record in enumerate(records):
        read_class = bfscan_model.le.transform(bfscan_model.predict([str(record.seq)], n_jobs=1))
        read_class = bfscan_model.le.inverse_transform(read_class)[0]
        if read_class != "other":
            writers[read_class].write(record.format(arguments.output_format))
        end_time = time.time()

        if r % 100 == 0 and r > 0:
            elapsed_time = "%.2f" %(end_time - start_time)
            reads_per_seconds = "%.2f"%(r / (end_time - start_time))
            print(f"{r} reads processed in {elapsed_time} seconds ({reads_per_seconds} reads per second)")
 
    for class_name in bfscan_model.filter.classes:
        writers[class_name].close()
        
if __name__ == '__main__':
    main()
    



