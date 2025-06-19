import csv

input_file = "test.tsv"
output_file = "best_blasthits.tsv"

# Explicit header based on the BLASTN outfmt 6 specification you used
header = [
    "qseqid", "sseqid", "nident", "mismatch", "gaps", "evalue", "bitscore",
    "qlen", "slen", "length", "qstart", "qend", "sstart", "send",
    "pident", "qseq", "sseq"
]

# Dictionary to store best hit per query
best_hits = {}

with open(input_file, newline='') as infile:
    reader = csv.reader(infile, delimiter='\t')
    for row in reader:
        if len(row) != len(header):
            print(f"Skipping malformed row: {row}")
            continue
        query_id = row[0]
        evalue = float(row[5])
        bit_score = float(row[6])

        if query_id not in best_hits:
            best_hits[query_id] = row
        else:
            best_evalue = float(best_hits[query_id][5])
            best_bit_score = float(best_hits[query_id][6])
            # Select better hit
            if evalue < best_evalue or (evalue == best_evalue and bit_score > best_bit_score):
                best_hits[query_id] = row

# Write best hits to file
with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile, delimiter='\t')
    writer.writerow(header)
    for row in best_hits.values():
        writer.writerow(row)

