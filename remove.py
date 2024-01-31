from Bio import SeqIO

def remove_identical_sequences(input_file, output_file):
    sequences = {}
    with open(input_file, 'r') as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            sequence = str(record.seq)
            if sequence not in sequences:
                sequences[sequence] = record.description  # Storing the sequence ID

    with open(output_file, 'w') as output_handle:
        for sequence, seq_id in sequences.items():
            output_handle.write(f'>{seq_id}\n')  # Writing the sequence ID
            output_handle.write(f'{sequence}\n')  # Writing the sequence itself

# Replace 'input.fasta' with the path to your input FASTA file
input_filename = 'updated_complete_new_old_stx_seq.fasta'

# Replace 'output.fasta' with the desired name of the output file
output_filename = 'duplicate_removed_stx_.fa'

remove_identical_sequences(input_filename, output_filename)

