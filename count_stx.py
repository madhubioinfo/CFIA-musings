import csv
from collections import defaultdict

# Initialize dictionaries to store Stx1 and Stx2 counts for each sequence ID
stx_counts = defaultdict(lambda: {'stx1_count': 0, 'stx2_count': 0})

# Read the input TSV file
input_file = 'allele_subtype_newcount.tsv'  # Change this to your actual file name
with open(input_file, 'r') as tsv_file:
    reader = csv.reader(tsv_file, delimiter='\t')
   
    for row in reader:
        seq_id = row[0]
        stx_type = row[1].lower()  # Convert to lowercase for consistent matching
        count = int(row[2])
       
        # Check if it's Stx1 or Stx2 and update counts accordingly
        if 'stx1' in stx_type:
            stx_counts[seq_id]['stx1_count'] += count
        elif 'stx2' in stx_type:
            stx_counts[seq_id]['stx2_count'] += count

# Write the result to a CSV file
output_file = 'stx_counts_output.csv'
with open(output_file, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['seq_id', 'stx1_count', 'stx2_count'])  # Header row
   
    for seq_id, counts in stx_counts.items():
        writer.writerow([seq_id, counts['stx1_count'], counts['stx2_count']])

print(f"Counts have been written to {output_file}")
