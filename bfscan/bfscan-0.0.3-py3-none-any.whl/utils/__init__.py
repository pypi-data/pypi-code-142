from Bio import SeqIO
from Bio.Seq import Seq
import os
import gzip

def sequence_to_kmer(sequence, k):
    
    sequence = Seq(sequence).upper()
    c_rev_seq = sequence.reverse_complement()
    kmer_list = []
    
    base_index = 0
    for i in sequence:
        if (len(sequence) - base_index) >= k:
            kmer_list.append(str(sequence[base_index:(base_index+k)]))
            kmer_list.append(str(c_rev_seq[base_index:(base_index+k)]))
        base_index+=1
    
    return kmer_list

def read_sequence_file(filename):

    if filename.endswith('.gz'):
        reader = gzip.open(filename, 'rt')
        filename = filename.strip(".gz")
    else:
        reader = open(filename)

    file_basename_name, file_basename_extension = os.path.splitext(os.path.basename(filename))

    if file_basename_extension in ['.fasta', '.fas', '.fna', '.fa']:
        file_format = "fasta"
    elif file_basename_extension in ['.fastq', '.fq']:
        file_format = "fastq"
    else:
        raise ValueError("Unsupported file format")

    records = SeqIO.parse(reader, file_format)
    
    return records