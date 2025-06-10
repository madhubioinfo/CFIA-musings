from Bio import SeqIO

# Build a dictionary with full record (not just .seq) so we retain .description
contigs = {record.id: record for record in SeqIO.parse("all_contigs.fasta", "fasta")}

with open("contig_coords") as infile, open("extracted_sequences.fasta", "w") as out:
    next(infile)  # skip header line
    for line in infile:
        contig, start, stop, strand = line.strip().split()
        start, stop = int(start), int(stop)

        if contig not in contigs:
            print(f"Warning: {contig} not found in FASTA file.")
            continue

        full_record = contigs[contig]
        sub_seq = full_record.seq[start - 1:stop]

        if strand == "-":
            sub_seq = sub_seq.reverse_complement()

        # Use full FASTA description
        header = f"{contig}:{start}-{stop} {full_record.description[len(contig):].strip()}"
        out.write(f">{header}\n{sub_seq}\n")

