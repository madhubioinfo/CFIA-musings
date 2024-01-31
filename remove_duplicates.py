from Bio import SeqIO

# Function to read FASTA file and return a set of sequence strings
def read_fasta(file_path):
    sequences = []
    seen_seqs = set()
    with open(file_path, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            seq_str = str(record.seq)
            if seq_str not in seen_seqs:
                seen_seqs.add(seq_str)
                sequences.append(record)
    return sequences

# Paths to your FASTA files
file1_path = "Stx_nt_all_unique_240116.fasta"  # Replace with your first FASTA file db file of stx
file2_path = "duplicate_removed_stx_.fa"  # Replace with your second FASTA file

# Read unique sequences from both files
unique_sequences_file1 = read_fasta(file1_path)
unique_sequences_file2 = read_fasta(file2_path)

# Find unique sequences in file 2 that are not in file 1
unique_in_file2 = [seq for seq in unique_sequences_file2 if str(seq.seq) not in {str(f.seq) for f in unique_sequences_file1}]

# Write unique sequences from file 2 to an output file
output_file = "unique_sequences_file1_more_complete.fasta"  # Replace with your output file name

with open(output_file, "w") as output_handle:
    SeqIO.write(unique_in_file2, output_handle, "fasta")

print(f"Unique sequences from {file2_path} that are not in {file1_path} are written to {output_file}")
