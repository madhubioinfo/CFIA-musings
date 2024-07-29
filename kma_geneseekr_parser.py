import pandas as pd

# Load the mapping file
def load_mapping_file(filename):
    mapping_df = pd.read_csv(filename, sep='\t', header=0)
    mapping_df['seq_ids'] = mapping_df['seq_ids'].str.strip()
    mapping_df['strain_ids'] = mapping_df['strain_ids'].str.strip()
    return mapping_df

# Load the sequence and gene files
def load_gene_file(filename):
    gene_df = pd.read_csv(filename, sep='\t', header=0)
    gene_df['seq_ids'] = gene_df['seq_ids'].str.strip()
    gene_df['gene_ids'] = gene_df['gene_ids'].str.strip()
    return gene_df

# Replace seq_ids with strain_ids in gene file based on mapping
def substitute_strain_ids(gene_df, mapping_df):
    mapping_dict = dict(zip(mapping_df['seq_ids'], mapping_df['strain_ids']))
    gene_df['strain_ids'] = gene_df['seq_ids'].map(mapping_dict).fillna('NoMapping')
    gene_df['gene_ids'] = gene_df['gene_ids'].apply(lambda x: x if pd.notna(x) else 'NoGeneInfo')
    return gene_df

# Load mapping file [ this is mapping file :Noor]
mapping_file = 'temp'
mapping_df = load_mapping_file(mapping_file)

# Load and process file2 [ This file is kma output file with two columns : Noor]
file2 = 'kma_output.tsv' 
file2_df = load_gene_file(file2)
file2_df = substitute_strain_ids(file2_df, mapping_df)

# Save intermediate file2 output 
file2_output = 'file2_intermediate.tsv'
file2_df.to_csv(file2_output, sep='\t', index=False)
print(f"File2 intermediate output written to {file2_output}")

# Load and process file3  [ This is geneseekr output with two columns : Noor]
file3 = 'geneseekrparsed_output.tsv'
file3_df = load_gene_file(file3)
file3_df = substitute_strain_ids(file3_df, mapping_df)

# Save intermediate file3 output
file3_output = 'file3_intermediate.tsv'
file3_df.to_csv(file3_output, sep='\t', index=False)
print(f"File3 intermediate output written to {file3_output}")

# Merge intermediate files to get final output
def get_final_output(file2_df, file3_df):
    # Group by strain_ids and aggregate gene_ids
    file2_gene_groups = file2_df.groupby('strain_ids')['gene_ids'].apply(lambda x: ','.join(set(x))).reset_index()
    file3_gene_groups = file3_df.groupby('strain_ids')['gene_ids'].apply(lambda x: ','.join(set(x))).reset_index()

    # Merge the two intermediate DataFrames
    final_output_df = pd.merge(file2_gene_groups, file3_gene_groups, on='strain_ids', how='outer', suffixes=('_File2', '_File3'))

    # Fill NaN values with 'NA'
    final_output_df['gene_ids_File2'].fillna('NA', inplace=True)
    final_output_df['gene_ids_File3'].fillna('NA', inplace=True)

    return final_output_df

# Get final output
final_output_df = get_final_output(file2_df, file3_df)

# Save final output
final_output_file = 'final_output.tsv'
final_output_df.to_csv(final_output_file, sep='\t', index=False)
print(f"Final output written to {final_output_file}")

# Print the final output DataFrame
print("\nComplete Final Output DataFrame:")
print(final_output_df)

# Function to find matching genes between File2 and File3
def find_matching_genes(file2_genes, file3_genes):
    file2_set = set(file2_genes.split(',')) if file2_genes != 'NA' else set()
    file3_set = set(file3_genes.split(',')) if file3_genes != 'NA' else set()
    
    matching_genes = file2_set.intersection(file3_set)
    return ','.join(matching_genes) if matching_genes else 'NA'

# Calculate matching genes
final_output_df['Matching_Genes'] = final_output_df.apply(lambda row: find_matching_genes(row['gene_ids_File2'], row['gene_ids_File3']), axis=1)

# Count and calculate the percentage of matching genes
matching_count = final_output_df['Matching_Genes'].apply(lambda x: x != 'NA').sum()
total_count = len(final_output_df)
matching_percentage = (matching_count / total_count) * 100 if total_count > 0 else 0

# Print the results
print(f"\nNumber of Matching Rows: {matching_count}")
print(f"Percentage of Matching Rows: {matching_percentage:.2f}%")
print("\nMatching Genes:")
print(final_output_df[final_output_df['Matching_Genes'] != 'NA'])

