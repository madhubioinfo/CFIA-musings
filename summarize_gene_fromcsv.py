import os
import csv
from collections import defaultdict

# Directory containing the CSV files
input_directory = "/mnt/nas/users/madhu/poresippr_db_recent_minimap2_cdhit/stxdb_99/output_directory"

# Dictionary to store gene counts across files
gene_data = defaultdict(lambda: defaultdict(int))

# List to store filenames (for the header)
file_names = []

# Loop through each CSV file in the directory
for file in os.listdir(input_directory):
    if file.endswith(".csv"):
        file_path = os.path.join(input_directory, file)
        file_name = os.path.splitext(file)[0]  # Get the filename without extension
        file_names.append(file_name)  # Add to the header list

        # Read the CSV file and extract gene counts
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ')  # Split by space instead of comma

            next(reader)  # Skip the header row (Ref, Count)
            for row in reader:
                # Check if the row has at least two columns (Ref and Count)
                if len(row) >= 2:
                    gene_name = row[0]  # The 'Ref' column
                    try:
                        gene_count = int(row[1])  # The 'Count' column
                    except ValueError:
                        gene_count = 0  # If the count is not an integer, default to 0
                    gene_data[gene_name][file_name] = gene_count
                else:
                    print(f"Skipping row in file {file}: {row} (not enough columns)")

# Create the output file
output_file = "gene_counts_output.csv"
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header (Gene and file names)
    header = ['Gene'] + file_names
    writer.writerow(header)

    # Write the gene data rows
    for gene, counts in gene_data.items():
        row = [gene] + [counts.get(file_name, 0) for file_name in file_names]
        writer.writerow(row)

print(f"Gene count table written to {output_file}")
