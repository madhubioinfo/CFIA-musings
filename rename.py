tsv_file_path = "allele_report.tsv"
fasta_file_path = "final_aa_ECs2973.fasta"
output_file_path = "output_ECs2973.fasta"

# Read ID mapping from TSV file
id_mapping = {}
with open(tsv_file_path, "r") as tsv_file:
    for line in tsv_file:
        fields = line.strip().split("\t")
        if len(fields) != 2:
            continue  # Skip line with incorrect number of fields
        old_id, new_id = fields
        id_mapping[old_id] = new_id

# Process FASTA file and write output to new FASTA file
with open(fasta_file_path, "r") as fasta_file, open(output_file_path, "w") as output_file:
    current_id = None
    current_sequence = ""
    for line in fasta_file:
        if line.startswith(">"):
            # New sequence
            if current_id is not None:
                # Write previous sequence to output file
                new_id = id_mapping.get(current_id, current_id)  # Use current ID if new ID not found
                output_file.write(">{new_id}\n{current_sequence}\n".format(new_id=new_id, current_sequence=current_sequence))
            current_id = line[1:].strip()
            current_sequence = ""
        else:
            # Append to current sequence
            current_sequence += line.strip()
    # Write last sequence to output file
    new_id = id_mapping.get(current_id, current_id)  # Use current ID if new ID not found
    output_file.write(">{new_id}\n{current_sequence}\n".format(new_id=new_id, current_sequence=current_sequence))
