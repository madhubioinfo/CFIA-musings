import csv

input_file = "extracted_sequences_nt_blast.tsv"
output_file = "best_blasthits.tsv"

# Dictionary to store best hit per query
best_hits = {}

with open(input_file, newline='') as infile:
    reader = csv.reader(infile, delimiter='\t')
    header = next(reader)  # store the header
    for row in reader:
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

