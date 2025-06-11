from Bio import SeqIO
import os

input_fasta = "uniq_seqs.fasta"
output_base_dir = "out"

os.makedirs(output_base_dir, exist_ok=True)

for record in SeqIO.parse(input_fasta, "fasta"):
    # Clean the ID for safe folder names
    safe_id = record.id.replace("/", "_").replace(" ", "_").replace("|", "_")
    seq_dir = os.path.join(output_base_dir, safe_id)
    os.makedirs(seq_dir, exist_ok=True)
    
    fasta_path = os.path.join(seq_dir, f"{safe_id}.fasta")
    with open(fasta_path, "w") as f:
        SeqIO.write(record, f, "fasta")

print(f"Split completed into {output_base_dir}/")

