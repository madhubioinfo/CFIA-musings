# # Specifying the input file paths for csv geneseekr output as input and output file wanted to stdout

input_file_path = "test.csv"
output_file_path = "output.fasta"

# Defining the names of genes to search for
genes_to_include = ["stx1", "stx2"]

# Opening the given file paths
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

print(f"stx1 and stx2 fasta output is here {output_file_path}")

