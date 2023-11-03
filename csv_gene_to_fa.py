# Specify the file paths for input and output
input_file_path = "test.csv"
output_file_path = "output.fasta"

# Define the gene names you want to filter
genes_to_include = ["stx1", "stx2"]

# Open the input file and the output file
with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    lines = input_file.readlines()
    
    for line in lines:
        line = line.strip()
        columns = line.split(",")
        
        if len(columns) >= 6:
            gene_name = columns[1]
            if gene_name in genes_to_include:
                header = ">" + columns[1] + "|" + columns[4]
                sequence = columns[6]
                output_file.write(f"{header}\n{sequence}\n")

print(f"Filtered FASTA output has been written to {output_file_path}")

