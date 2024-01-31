from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# author: Madhu
# This function reverse complements the DNA seq
def reverse_complement(seq):
    return str(Seq(seq).reverse_complement())

# Reading the input fasta file
def process_fasta(file_path):
    sequences = SeqIO.parse(file_path, "fasta")
    updated_sequences = []
    discarded_sequences = []

    # Iterating through each sequence
    for seq_record in sequences:
        sequence = str(seq_record.seq)

        # looking for sequences starting with start codons
        start_codons = ["ATG", "GTG", "TTG"]
        # checking the end of the sequences with stop codons
        stop_codons = ["TAA", "TAG", "TGA"]

        if sequence[:3] in start_codons and sequence[-3:] in stop_codons:
            updated_sequences.append(seq_record)
            print(f"Sequence {seq_record.id} starts with a start codon and ends with a stop codon.")
        else:
            # Reverse complementing the sequence if needed
            reversed_seq = reverse_complement(sequence)
            if reversed_seq[:3] in start_codons and reversed_seq[-3:] in stop_codons:
                reversed_record = SeqRecord(Seq(reversed_seq), id=seq_record.id, description="")
                updated_sequences.append(reversed_record)
                print(f"Sequence {seq_record.id} has been reverse complemented and now starts with a start codon and ends with a stop codon.")
            else:
                discarded_sequences.append(seq_record)
                print(f"Sequence {seq_record.id} doesn't meet start and stop codon criteria and has been discarded.")

    return updated_sequences, discarded_sequences

# provide input file name
input_file = 'all_output.fa'
processed_sequences, discarded_sequences = process_fasta(input_file)

# provide output file name
output_file = 'updated_sequences.fasta'
SeqIO.write(processed_sequences, output_file, "fasta")

# file for the sequences with stop codons and which are discarded from outputting
discarded_file = 'discarded_sequences.fasta'
SeqIO.write(discarded_sequences, discarded_file, "fasta")
